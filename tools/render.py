#!/usr/bin/env python3
"""Render an HTML design to crisp PNG / JPG / PDF at any size, with print support (bleed, trim/bleed boxes,
crop marks) and an automatic QC report (effective image dpi, fonts, safe-area violations).

The HTML only has to use the CSS variables this script injects:
    --page-w / --page-h     full page incl. bleed  (mm for print sizes, px for screen sizes)
    --trim-w / --trim-h     the finished size
    --bleed                 bleed width (0 for screen sizes)
    --safe                  safe margin from the trim edge (from --safe)
See assets/template.html.

Examples
  # Instagram 4:5, 2x pixels (2160x2700 PNG) + PDF
  render.py design.html --size 1080x1350px --scale 2 --out out/ig_post --formats png,pdf
  # A5 print cover with 3 mm bleed: print PDF (+ crop marks) and 300 dpi PNG of the trim area
  render.py cover.html --size 148x210mm --bleed 3 --dpi 300 --out out/cover --formats pdf,png --crop-marks
  # Full wrap (back+spine+front) : give the TOTAL trim size
  render.py wrap.html --size 328x210mm --bleed 3 --out out/wrap --formats pdf --crop-marks --spine-marks 151,183
  # transparent PNG sticker/overlay
  render.py logo.html --size 1200x1200px --scale 2 --transparent --out out/logo --formats png
"""
import argparse, json, math, os, pathlib, re, shutil, subprocess, sys, tempfile

MM_PER_IN = 25.4
PX_PER_MM = 96 / MM_PER_IN          # CSS px per mm
PT_PER_MM = 72 / MM_PER_IN

QC_JS = r"""
<script id="__qc_script">
window.addEventListener('load', async () => {
  try { await document.fonts.ready; } catch (e) {}
  await new Promise(r => setTimeout(r, 300));
  const cs = getComputedStyle(document.documentElement);
  const unit = cs.getPropertyValue('--__unit').trim() || 'px';
  const bleed = parseFloat(cs.getPropertyValue('--__bleed')) || 0;
  const trimW = parseFloat(cs.getPropertyValue('--__trimw')), trimH = parseFloat(cs.getPropertyValue('--__trimh'));
  const safe = parseFloat(cs.getPropertyValue('--__safe')) || 0;
  const k = unit === 'mm' ? 96 / 25.4 : 1;              // css px per unit
  const pages = document.querySelectorAll('.page');
  const relIn = (el) => { const pg = el.closest('.page') || document.body; const pr = pg.getBoundingClientRect(), r = el.getBoundingClientRect();
    return {x0: (r.left - pr.left) / k, y0: (r.top - pr.top) / k, x1: (r.right - pr.left) / k, y1: (r.bottom - pr.top) / k, pg: Array.prototype.indexOf.call(pages, pg) + 1}; };
  const out = {unit, bleed, trim: [trimW, trimH], safe, fonts: [], images: [], safe_violations: [], boxes: {}, pageCount: pages.length || 1};
  document.fonts.forEach(f => { if (f.status === 'loaded') out.fonts.push(f.family.replace(/"/g, '') + ' ' + f.weight); });
  document.querySelectorAll('img').forEach(img => {
    const r = img.getBoundingClientRect(); if (!r.width) return;
    const inches = r.width / 96;                          // displayed width in inches
    out.images.push({src: (img.currentSrc || img.src).split('/').pop().slice(0, 60), natural: [img.naturalWidth, img.naturalHeight],
      dpi: Math.round(img.naturalWidth / inches), css_px_ratio: +(img.naturalWidth / r.width).toFixed(2)});
  });
  document.querySelectorAll('[data-safe]').forEach(el => {
    const b = relIn(el);
    const lo = bleed + safe, hiX = bleed + trimW - safe, hiY = bleed + trimH - safe;
    const bad = b.x0 < lo - .2 || b.y0 < lo - .2 || b.x1 > hiX + .2 || b.y1 > hiY + .2;
    if (bad) out.safe_violations.push({page: b.pg, el: (el.dataset.safe || el.className || el.tagName).toString().slice(0, 40),
      box: [b.x0, b.y0, b.x1, b.y1].map(v => +v.toFixed(1))});
  });
  document.querySelectorAll('[data-qc]').forEach(el => { const b = relIn(el); out.boxes[(b.pg > 1 || pages.length > 1 ? 'p' + b.pg + ' ' : '') + (el.dataset.qc || el.className)] = [b.x0, b.y0, b.x1, b.y1].map(v => +v.toFixed(1)); });
  const pre = document.createElement('pre'); pre.id = '__qc'; pre.style.display = 'none'; pre.textContent = JSON.stringify(out);
  document.body.appendChild(pre);
});
</script>
"""


def find_chrome():
    env = os.environ.get("CHROME_PATH")
    if env and os.path.exists(env):
        return env
    cands = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for c in cands:
        if os.path.exists(c):
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"):
        p = shutil.which(name)
        if p:
            return p
    sys.exit("Chrome/Edge not found. Install Chrome or set CHROME_PATH.")


def parse_size(s):
    m = re.fullmatch(r"\s*([\d.]+)\s*[xX×]\s*([\d.]+)\s*(px|mm|cm|in)?\s*", s)
    if not m:
        sys.exit(f"bad --size {s!r}; use 1080x1350px, 148x210mm, 21x29.7cm or 8.5x11in")
    w, h, u = float(m.group(1)), float(m.group(2)), (m.group(3) or "px")
    if u == "cm":
        w, h, u = w * 10, h * 10, "mm"
    if u == "in":
        w, h, u = w * MM_PER_IN, h * MM_PER_IN, "mm"
    return w, h, u


def run(cmd, timeout=240):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
    return r


def build_tmp_html(src, w, h, unit, bleed, safe, transparent):
    html = pathlib.Path(src).read_text(encoding="utf-8")
    u = "mm" if unit == "mm" else "px"
    pw, ph = w + 2 * bleed, h + 2 * bleed
    if unit == "mm":
        rnd = math.ceil if bleed else round                                   # Chrome rounds to whole points: with bleed never end up short of it; without bleed avoid a white sliver on dark pages
        page_pt = (rnd(pw * PT_PER_MM), rnd(ph * PT_PER_MM))
        page_css = f"@page{{size:{page_pt[0]}pt {page_pt[1]}pt;margin:0}}"
    else:
        page_css = f"@page{{size:{pw}px {ph}px;margin:0}}"
    bg = "transparent" if transparent else "#fff"
    inj = (f"<style id='__inj'>:root{{--page-w:{pw}{u};--page-h:{ph}{u};--trim-w:{w}{u};--trim-h:{h}{u};--bleed:{bleed}{u};--safe:{safe}{u};"
           f"--__unit:{u};--__bleed:{bleed};--__trimw:{w};--__trimh:{h};--__safe:{safe}}}{page_css}"
           f"html,body{{margin:0;padding:0;background:{bg}}}*{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}"
           f".page{{break-after:page;page-break-after:always}}.page:last-of-type{{break-after:auto;page-break-after:auto}}#__qc{{display:none}}</style>")
    if "</head>" in html:
        html = html.replace("</head>", inj + "</head>", 1)
    else:
        html = inj + html
    html = html.replace("</body>", QC_JS + "</body>", 1) if "</body>" in html else html + QC_JS
    tmp = pathlib.Path(src).resolve().parent / f".__render_{os.getpid()}.html"
    tmp.write_text(html, encoding="utf-8")
    return tmp, (pw, ph)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html")
    ap.add_argument("--size", required=True, help="finished (trim) size, e.g. 1080x1350px, 148x210mm, 8.5x11in")
    ap.add_argument("--bleed", type=float, default=0, help="bleed in mm (print sizes only)")
    ap.add_argument("--safe", type=float, default=0, help="safe margin from trim edge, same unit as --size (elements with data-safe are checked)")
    ap.add_argument("--scale", type=float, default=2, help="device scale factor for screenshots of px sizes (2 = retina)")
    ap.add_argument("--dpi", type=int, default=300, help="dpi of the PNG rasterised from the PDF (print sizes)")
    ap.add_argument("--out", required=True, help="output path without extension")
    ap.add_argument("--formats", default="png,pdf", help="comma list of png,jpg,pdf")
    ap.add_argument("--transparent", action="store_true", help="transparent PNG (screenshot route; px or mm sizes)")
    ap.add_argument("--with-bleed", action="store_true", help="PNG/JPG include the bleed area (default: trimmed)")
    ap.add_argument("--crop-marks", action="store_true", help="also write <out>_cropmarks.pdf (12 mm slug)")
    ap.add_argument("--spine-marks", default="", help="comma list of x positions (mm from trim left) for fold marks, e.g. 151,183")
    ap.add_argument("--multipage", action="store_true", help="document with several .page sections: keep all PDF pages, write <out>_pNN.png per page")
    ap.add_argument("--budget", type=int, default=20000, help="virtual time budget ms (raise for slow fonts/images)")
    a = ap.parse_args()

    w, h, unit = parse_size(a.size)
    if unit == "px" and a.bleed:
        sys.exit("--bleed only applies to mm/in/cm sizes")
    fmts = [f.strip().lower() for f in a.formats.split(",") if f.strip()]
    out = pathlib.Path(a.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    chrome = find_chrome()
    tmp, (pw, ph) = build_tmp_html(a.html, w, h, unit, a.bleed, a.safe, a.transparent)
    uri = tmp.as_uri()
    base = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--virtual-time-budget={a.budget}"]
    made = []
    try:
        # ---- QC (DOM measurements) ----
        win_w, win_h = (math.ceil(pw * PX_PER_MM), math.ceil(ph * PX_PER_MM)) if unit == "mm" else (math.ceil(pw), math.ceil(ph))
        r = run(base + [f"--window-size={max(win_w, 800)},{max(win_h, 600)}", "--dump-dom", uri])
        m = re.search(r'<pre id="__qc"[^>]*>(.*?)</pre>', r.stdout, re.S)
        qc = json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&")) if m else None

        # ---- PDF ----
        want_pdf = "pdf" in fmts or ("png" in fmts and unit == "mm" and not a.transparent) or a.crop_marks
        pdf_path = out.with_suffix(".pdf")
        if want_pdf:
            r = run(base + ["--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", uri])
            if not pdf_path.exists():
                sys.exit("PDF render failed:\n" + r.stderr[-800:])
            try:
                import pymupdf
                d = pymupdf.open(str(pdf_path))
                npages = len(d)
                if qc and qc.get("pageCount") and npages != qc["pageCount"] or (not a.multipage and npages > 1):
                    print(f"WARNING: PDF has {npages} pages but the HTML has {qc.get('pageCount') if qc else 1} .page element(s). Something overflows a page (check margins, extra elements).")
                if unit == "mm":
                    for p in d:
                        mw, mh = p.rect.width, p.rect.height          # boxes must stay inside the MediaBox (page may be rounded down by <1 pt)
                        p.set_bleedbox(pymupdf.Rect(0, 0, min(pw * PT_PER_MM, mw), min(ph * PT_PER_MM, mh)))
                        p.set_trimbox(pymupdf.Rect(a.bleed * PT_PER_MM, a.bleed * PT_PER_MM, min((a.bleed + w) * PT_PER_MM, mw), min((a.bleed + h) * PT_PER_MM, mh)))
                d.set_metadata({"title": out.stem, "producer": "html-design-studio"})
                tmpbytes = d.tobytes(deflate=True, garbage=3)
                d.close()
                pdf_path.write_bytes(tmpbytes)
            except ImportError:
                print("note: pymupdf not installed, PDF boxes/crop marks skipped (pip install pymupdf)")
            if "pdf" in fmts:
                made.append(str(pdf_path))
            elif pdf_path.exists() and "pdf" not in fmts and not a.crop_marks:
                pass

        # ---- crop marks (every page) ----
        if a.crop_marks and unit == "mm":
            try:
                import pymupdf
                src = pymupdf.open(str(pdf_path))
                SL = 12.0
                n = pymupdf.open()
                for pi in range(len(src)):
                    PW, PH = src[pi].rect.width, src[pi].rect.height
                    pg = n.new_page(width=(pw + 2 * SL) * PT_PER_MM, height=(ph + 2 * SL) * PT_PER_MM)
                    pg.show_pdf_page(pymupdf.Rect(SL * PT_PER_MM, SL * PT_PER_MM, SL * PT_PER_MM + PW, SL * PT_PER_MM + PH), src, pi)
                    tx0, ty0 = (SL + a.bleed) * PT_PER_MM, (SL + a.bleed) * PT_PER_MM
                    tx1, ty1 = tx0 + w * PT_PER_MM, ty0 + h * PT_PER_MM
                    off, ln = (a.bleed + 1.5) * PT_PER_MM, 6 * PT_PER_MM
                    L = lambda x0, y0, x1, y1: pg.draw_line((x0, y0), (x1, y1), color=(0, 0, 0), width=0.25)
                    for x in (tx0, tx1):
                        L(x, ty0 - off, x, ty0 - off - ln); L(x, ty1 + off, x, ty1 + off + ln)
                    for y in (ty0, ty1):
                        L(tx0 - off, y, tx0 - off - ln, y); L(tx1 + off, y, tx1 + off + ln, y)
                    for sx in [float(v) for v in a.spine_marks.split(",") if v.strip()]:
                        x = tx0 + sx * PT_PER_MM
                        L(x, ty0 - off, x, ty0 - off - ln); L(x, ty1 + off, x, ty1 + off + ln)
                    pg.insert_text((SL * PT_PER_MM + 2, SL * PT_PER_MM - 14), f"{out.stem} | p. {pi + 1}/{len(src)} | trim {w:g} x {h:g} mm | bleed {a.bleed:g} mm", fontsize=6, color=(.3, .3, .3))
                    pg.set_bleedbox(pymupdf.Rect(SL * PT_PER_MM, SL * PT_PER_MM, (SL + pw) * PT_PER_MM, (SL + ph) * PT_PER_MM))
                    pg.set_trimbox(pymupdf.Rect(tx0, ty0, tx1, ty1))
                cm = out.parent / (out.name + "_cropmarks.pdf")
                n.save(str(cm), deflate=True, garbage=3); made.append(str(cm))
            except ImportError:
                print("note: pymupdf not installed, crop marks skipped")
        if not ("pdf" in fmts) and pdf_path.exists() and "png" in fmts and unit == "mm" and not a.transparent:
            pass  # kept temporarily; removed below after rasterising

        # ---- PNG / JPG ----
        if "png" in fmts or "jpg" in fmts or "jpeg" in fmts:
            png_path = out.with_suffix(".png")
            if unit == "mm" and not a.transparent and pdf_path.exists():
                import pymupdf
                z = a.dpi / 72
                clip = None if a.with_bleed else pymupdf.Rect(a.bleed * PT_PER_MM, a.bleed * PT_PER_MM, (a.bleed + w) * PT_PER_MM, (a.bleed + h) * PT_PER_MM)
                doc = pymupdf.open(str(pdf_path))
                if a.multipage and len(doc) > 1:
                    for i, pgx in enumerate(doc, 1):
                        pp = out.parent / f"{out.name}_p{i:02d}.png"
                        pgx.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip, alpha=False).save(str(pp)); made.append(str(pp))
                    png_path = None
                else:
                    doc[0].get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip, alpha=False).save(str(png_path))
            else:
                S = a.scale if unit == "px" else a.dpi / 96
                cw, ch = (pw, ph) if unit == "px" else (pw * PX_PER_MM, ph * PX_PER_MM)
                ww, wh = max(math.ceil(cw), 500), max(math.ceil(ch), 500)       # new headless has a minimum window size
                cmd = base + [f"--window-size={ww},{wh}", f"--force-device-scale-factor={S}", f"--screenshot={png_path}", uri]
                if a.transparent:
                    cmd.insert(1, "--default-background-color=00000000")
                run(cmd)
                from PIL import Image
                im = Image.open(png_path)
                if unit == "px":
                    box = (0, 0, round(pw * S), round(ph * S))
                elif a.with_bleed:
                    box = (0, 0, round(pw * PX_PER_MM * S), round(ph * PX_PER_MM * S))
                else:
                    bl = a.bleed * PX_PER_MM * S
                    box = (round(bl), round(bl), round(bl + w * PX_PER_MM * S), round(bl + h * PX_PER_MM * S))
                if im.size != (box[2] - box[0], box[3] - box[1]) or box[0]:
                    im = im.crop(box)
                im.save(png_path)
            if "png" in fmts and png_path is not None:
                made.append(str(png_path))
            if ("jpg" in fmts or "jpeg" in fmts) and png_path is not None:
                from PIL import Image
                im = Image.open(png_path).convert("RGB")
                jp = out.with_suffix(".jpg"); im.save(jp, quality=95, subsampling=0, dpi=(a.dpi, a.dpi)); made.append(str(jp))
                if "png" not in fmts:
                    png_path.unlink(missing_ok=True)
        if "pdf" not in fmts and pdf_path.exists():
            pdf_path.unlink()
    finally:
        tmp.unlink(missing_ok=True)

    # ---- report ----
    print("\n== outputs ==")
    for f in made:
        p = pathlib.Path(f); line = f"{p.name}  {p.stat().st_size // 1024} KB"
        if p.suffix in (".png", ".jpg"):
            from PIL import Image
            line += "  " + "x".join(map(str, Image.open(p).size)) + " px"
        print(" ", line)
    if qc:
        print("\n== QC ==")
        print("  fonts loaded:", ", ".join(sorted(set(qc["fonts"]))) or "(none: system fonts only?)")
        need = a.dpi if unit == "mm" else 96 * a.scale
        for im in qc["images"]:
            flag = "" if im["dpi"] >= need * 0.85 else f"   <-- LOW: want >= {int(need * .85)} dpi at this size"
            print(f"  img {im['src']}: {im['natural'][0]}x{im['natural'][1]} px -> {im['dpi']} dpi effective{flag}")
        if qc["safe_violations"]:
            print("  SAFE-AREA violations:")
            for v in qc["safe_violations"]:
                print("   ", v)
        elif a.safe:
            print("  safe area: OK (all [data-safe] elements inside)")
        for k, b in qc["boxes"].items():
            print(f"  box {k}: x {b[0]}-{b[2]}  y {b[1]}-{b[3]} {qc['unit']}")
    else:
        print("QC skipped (no DOM result)")


if __name__ == "__main__":
    main()
