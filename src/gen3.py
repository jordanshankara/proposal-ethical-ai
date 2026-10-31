import pathlib, re
import pathlib
H = pathlib.Path(__file__).resolve().parent
ROOT = H.parent
A = (ROOT / "assets").as_uri() + "/"
F = (ROOT / "fonts").as_uri() + "/"
D = (ROOT / "duo").as_uri() + "/"
g2 = (H / "gen2.py").read_text(encoding="utf-8")
# reuse helpers + dashboards from gen2
exec(g2[g2.index("def im(f)"):g2.index("r6 = [")])
exec(g2[g2.index("# ================= dashboards"):g2.index("chk = [")])
dash_css = g2[g2.index("/* ===== dashboards ===== */"):g2.index('""".replace("FF/"') if '""".replace("FF/"' in g2 else g2.index('"""\ncss = css.replace')]

NV, NV2, BL, SK = "#0A1628", "#163358", "#0066CC", "#3B8FF0"
css = """
@font-face{font-family:P;src:url(FF/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(FF/Poppins-ExtraBold.ttf);font-weight:800}
@font-face{font-family:M;src:url(FF/Montserrat-Regular.ttf);font-weight:400}
@font-face{font-family:M;src:url(FF/Montserrat-Medium.ttf);font-weight:500}
@font-face{font-family:M;src:url(FF/Montserrat-SemiBold.ttf);font-weight:600}
@font-face{font-family:M;src:url(FF/Montserrat-Italic.ttf);font-weight:500;font-style:italic}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#fff;font-family:M;color:#0A1628}
.pg{position:relative;width:210mm;height:297mm;overflow:hidden;page-break-after:always;background:#fff}
.pg:last-child{page-break-after:auto}
.a{position:absolute}
.ph{position:absolute;object-fit:cover;display:block}
.blk{position:absolute;background:#163358;color:#fff}
.kick{font:700 5.2pt P;letter-spacing:.24em;color:#7FC0FF}
.t1{font:800 17pt/1.1 P;letter-spacing:-.01em}
.sub{font:500 6.8pt/1.5 M;color:#CADCFC}
.sl{display:flex;gap:1.2mm}.sl i{display:block;width:2.2mm;height:7mm;background:#7FC0FF;opacity:.75;transform:skewX(-24deg);border-radius:.3mm}.sl i:nth-child(2){opacity:.5}.sl i:nth-child(3){opacity:.3}.sl i:nth-child(4){opacity:.18}
.hd2{display:flex;align-items:center;gap:2mm;font:800 8.4pt P;color:#0A1628}
.hd2 b{display:grid;place-items:center;width:5.6mm;height:5.6mm;background:#0066CC;color:#fff;font:700 6.6pt P}
.note{font:600 6pt M;color:#5D6B82}
.rs{display:flex;gap:2.6mm;padding-bottom:2mm;border-bottom:.25mm solid #D5E0F2}
.rs .ic{flex:none;width:7.6mm;height:7.6mm;border:.3mm solid #0066CC;border-radius:50%;display:grid;place-items:center}
.rs h4{font:700 7pt/1.2 P;color:#0A1628}.rs em{display:block;font:700 6pt/1.3 M;font-style:normal;color:#0066CC;margin-top:.3mm}.rs p{font:500 5.8pt/1.4 M;color:#4A5A72;margin-top:.5mm}
.cvs figure{position:absolute;width:23mm;text-align:left}
.cvs img{display:block;width:100%;aspect-ratio:210/297;object-fit:cover;box-shadow:0 1.2mm 3mm rgba(10,22,40,.35)}
.cvs figcaption{font:700 5.4pt P;color:#163358;margin-top:1.4mm}
.col h4{font:700 7pt/1.2 P;color:#0A1628}.col em{display:block;font:700 6pt/1.3 M;font-style:normal;color:#0066CC;margin-top:.3mm}.col p{font:500 5.8pt/1.4 M;color:#4A5A72;margin-top:.6mm}
.ft{position:absolute;left:10mm;right:10mm;font:600 6.4pt M}
.q q{display:block;font:italic 700 7.6pt/1.35 M;quotes:none;color:#fff}
.q p{font:500 6.2pt/1.4 M;color:#CADCFC;margin-top:1mm}
/* page 2 */
.chk{display:flex;align-items:center;gap:3.4mm;padding:0 5mm;height:12.5mm;border-bottom:.25mm solid #D5E0F2;font:700 7.4pt/1.25 M;color:#0A1628}
.chk:last-child{border:0}
.chk i{flex:none;width:8.4mm;height:8.4mm;border:.35mm solid #163358;border-radius:1.4mm;display:grid;place-items:center}
.tx2{font:700 6.8pt P;color:#163358;letter-spacing:.02em}
.tile{position:absolute;width:92mm}
.tile .sc{position:relative;width:92mm;height:33mm;overflow:hidden;background:#050B16;box-shadow:0 1.2mm 3.4mm rgba(10,22,40,.4)}
.tile .app{transform:scale(.3446);transform-origin:0 0;height:384px}
.tile .tx{display:flex;gap:2.4mm;margin-top:2.4mm}
.tile .no{flex:none;width:6mm;height:6mm;background:#163358;color:#fff;display:grid;place-items:center;font:800 7pt P}
.tile h5{font:700 7.2pt/1.2 P;color:#163358}
.tile p{font:500 6pt/1.38 M;color:#33465F;margin-top:.7mm}
.tile.k h5,.tile.k p{font-weight:700}
""" + dash_css
css = css.replace("FF/", F)

def line(p, w=14, col="#163358"): return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
KICK = "PROGRAM RESMI ASOSIASI AI INDONESIA (ASOSIASI.AI)"
ORIG = {"imp_2": "imp_2.jpg", "imp_5": "imp_5.jpg", "imp_4": "imp_4.jpg", "image18": "image18.jpeg", "image14": "image14.jpeg", "image15": "image15.jpeg", "image17": "image17.jpeg", "image185": "image185.jpeg"}
def P(f, x, y, w, h, extra=""): return f'<img class="ph" src="{A}{ORIG[f.rsplit(".", 1)[0]]}" style="left:{x}mm;top:{y}mm;width:{w}mm;height:{h}mm;{extra}">'
def logo_tab(): return f'<div class="a" style="left:0;top:0;width:46mm;height:14mm;background:#fff;display:grid;place-items:center;z-index:5"><img src="{A}image3.png" style="width:34mm"></div>'

# ============ PAGE 1 ============
r6 = [("Riset Upskilling & Reskilling AI", "Masa Depan Dunia Kerja", "Pola adaptasi kompetensi aparatur sipil, pekerja, dan wirausaha terhadap adopsi generative AI di berbagai negara maju.", "work"),
      ("Riset Penerapan AI di Keuangan & Tata Kelola Risiko", "Kepatuhan Ketat & Mitigasi", "Standar kepatuhan data kerahasiaan tinggi, otomasi analitis presisi, serta mitigasi kebocoran rahasia institusi dan negara.", "bank"),
      ("Riset Dampak Penggunaan AI pada Kesehatan Mental", "Kesejahteraan & Mental Health", "Studi mitigasi kelelahan kognitif kerja, batas etika interaksi AI, dan menjaga kesehatan psikologis aparatur di era automasi.", "mind"),
      ("Riset Pendidikan AI Komparatif", "Pendidikan Dasar s.d. Perguruan Tinggi", "Struktur kurikulum dan kerangka penerapan AI terstruktur dari Finlandia, Singapura, dan AS untuk pembinaan SDM adaptif.", "book"),
      ("Riset Penerapan AI pada Korporasi dan Bisnis", "Efisiensi Aset & Proyek", "Optimalisasi proses operasional, analisis naskah teknis proyek, dan automasi rantai birokrasi skala besar berbasis AI.", "build"),
      ("Riset Penerapan AI pada UMKM", "Daya Saing Ekosistem Usaha", "Strategi implementasi AI praktis, penciptaan efisiensi operasional cepat, dan pemberdayaan sektor ekonomi produktif.", "shop")]
r4 = [("Industri Keuangan", "Bank Indonesia, OJK", "Penerapan tata kelola data sangat ketat, audit kepatuhan, dan analitis risiko moneter.", "image14"),
      ("Lembaga Negara & ASN", "15+ Kementerian / Lembaga", "Drafting naskah dinas, audit dokumen, dan analisis opini publik berbasis AI etis.", "image15"),
      ("Korporasi & BUMN", "Hutama Karya, Garudafood, AP Land", "Automasi pelaporan kinerja, materi presentasi eksekutif, dan mitigasi disrupsi kerja.", "imp_4"),
      ("Pendidikan & UMKM", "Universitas & 2.500+ UMKM", "Pengembangan talenta masa depan, efisiensi harian, dan scaling manajemen usaha.", "image17")]
r3 = [("Kurikulum Customize", "Materi dirancang khusus menyesuaikan tugas, jenis berkas dinas, dan rutinitas kerja harian di direktorat Bapak/Ibu agar langsung memberi dampak efisiensi sejak hari pertama."),
      ("Konsultasi & Diskusi Lanjutan", "Pendampingan dan forum tanya jawab teknis pasca-pelatihan bersama instruktur untuk memastikan kelancaran adopsi alat bantu AI di lingkungan kerja instansi."),
      ("Keanggotaan Asosiasi AI", "Peserta tergabung dalam ekosistem keanggotaan Asosiasi AI Indonesia, menerima berkala riset terbaru, update regulasi etika AI, serta panduan teknologi mutakhir.")]
covers = [("cov_0.jpg", "Pendidikan"), ("cov_1.jpg", "Upskilling & Reskilling"), ("cov_2.jpg", "Kesehatan Jiwa"), ("cov_3.jpg", "Properti"), ("cov_4.jpg", "Keuangan"), ("cov_5.jpg", "UMKM")]
ICO2 = {k: v.replace('stroke="#fff"', "") for k, v in ICO.items()}
rs_html = ""
for i, (t, e, d, k) in enumerate(r6):
    x = 19 + (i % 2) * 93; y = 104 + (i // 2) * 18.8
    rs_html += f'<div class="a rs" style="left:{x}mm;top:{y}mm;width:89mm"><div class="ic">{line(ICO[k], 13, "#0066CC")}</div><div><h4>{t}</h4><em>{e}</em><p>{d}</p></div></div>'
cov_html = "".join(f'<figure style="left:{12 + i * 31.6}mm;top:161.3mm"><img src="{A}{f}"><figcaption>{c}</figcaption></figure>' for i, (f, c) in enumerate(covers))
r4_html = ""
for i, (t, e, d, f) in enumerate(r4):
    x = i * 52.5
    r4_html += P(f + ".jpg", x, 208.5, 52.5, 12, "border-right:.5mm solid #fff")
    r4_html += f'<div class="a col" style="left:{x + 5}mm;top:222.6mm;width:44mm"><h4>{t}</h4><em>{e}</em><p>{d}</p></div>'
r3_html = "".join(f'<div class="a col" style="left:{10 + i * 65}mm;top:263.4mm;width:59mm;padding-left:3mm;border-left:.7mm solid #0066CC"><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(r3))

p1 = f'''<div class="pg">
{P("imp_2.jpg", 0, 0, 140, 60)}{P("image18.jpg", 140.5, 0, 69.5, 30)}{P("imp_5.jpg", 140.5, 30.5, 69.5, 29.5)}
{logo_tab()}
<div class="blk" style="left:0;top:38mm;width:152mm;height:40mm;padding:5mm 7mm 0 10mm"><div class="kick">{KICK}</div>
<div class="t1" style="margin-top:2mm">APA YANG ANDA PEROLEH DARI PELATIHAN BERSAMA ASOSIASI AI INDONESIA?</div>
<div class="sub" style="margin-top:2mm;width:132mm">Materi teruji berbasis riset komparatif 12 negara dan implementasi riil untuk efisiensi serta produktivitas tanpa kompromi terhadap kerahasiaan data.</div></div>
<div class="a sl" style="left:158mm;top:66mm"><i></i><i></i><i></i><i></i></div>
<div class="a" style="left:10mm;top:82mm;width:190mm;padding-left:3mm;border-left:.8mm solid #0066CC;font:500 6.6pt/1.5 M;color:#33465F"><b style="color:#0A1628;font-weight:700">Landasan Akademik & Portofolio Nyata:</b> Seluruh modul disusun langsung dari publikasi resmi 6 buku riset sektoral Asosiasi AI Indonesia serta telah diimplementasikan dalam masterclass dan workshop bersama kementerian, regulator keuangan, dan BUMN nasional.</div>
<div class="a blk" style="left:0;top:97mm;width:13mm;height:62mm"><div class="a" style="left:4.6mm;top:61mm;transform-origin:0 0;transform:rotate(-90deg);white-space:nowrap;font:800 6pt P;letter-spacing:.02em;color:#fff"><span style="color:#7FC0FF;margin-right:2mm">1</span>SUMBER MATERI: RISET STUDI BANDING 12 NEGARA</div></div>
<div class="a note" style="left:19mm;top:97mm;width:182mm;text-align:right">Uni Eropa, UK, AS, Singapura, Korsel, Finlandia, China, Australia, dll.</div>
{rs_html}
<div class="a" style="left:0;top:159.8mm;width:210mm;height:40mm;background:#E8EEF8"></div>
<div class="cvs">{cov_html}</div>
<div class="a sl" style="left:196mm;top:178mm"><i></i><i></i><i></i></div>
<div class="a hd2" style="left:10mm;top:201.6mm"><b>2</b>IMPLEMENTASI HASIL RISET PADA DUNIA INDUSTRI</div><div class="a note" style="right:10mm;top:202.4mm">Validasi Praktis di Lapangan</div>
{r4_html}
<div class="a blk q" style="left:0;top:238.6mm;width:210mm;height:17mm;padding:2.2mm 10mm 0 16mm"><div class="a" style="left:5mm;top:-1mm;font:800 34pt P;color:#3B8FF0;opacity:.8">“</div><q>Hanya hasil riset yang telah terbukti Ethical, Efektif, dan Efisien dalam proses implementasi yang kami formulasikan menjadi materi edukasi dan sertifikasi kompetensi.”</q><p>Menjamin seluruh peserta mendapatkan materi aplikatif yang siap pakai, aman dari kebocoran data rahasia/kedinasan, serta berlandaskan kepatuhan hukum dan regulasi nasional.</p></div>
<div class="a hd2" style="left:10mm;top:249mm;display:none"></div>
<div class="a" style="left:10mm;top:241.5mm;display:none"></div>
{r3_html}
<div class="a blk" style="left:0;top:281.4mm;width:210mm;height:15.6mm;background:#0A1628"></div>
<div class="a" style="left:10mm;top:282.6mm;width:150mm;font:500 5.9pt/1.5 M;color:#CADCFC"><b style="color:#7FC0FF;font-weight:700">Dipandu Langsung oleh:</b> Dian Martin (Ketua Umum Asosiasi AI Indonesia) &amp; Dewan Pakar<br>Telah dipercaya oleh <b style="color:#7FC0FF;font-weight:700">15+ Kementerian</b>, Regulator Keuangan, BUMN Infrastruktur, dan Industri Nasional.</div>
<div class="a" style="right:10mm;top:283mm;background:#3B8FF0;color:#fff;font:800 6.4pt P;padding:1.5mm 3.4mm">Publikasi Riset: asosiasi.ai</div>
<div class="ft" style="top:291.6mm;display:flex;justify-content:space-between;color:#9DB2D3"><span>Narahubung Kelembagaan: +62 819-0111-2308 (Adah)</span><span>Sekretariat : 08111-91-3553</span></div>
</div>'''
# fix: section-3 heading must exist ("FASILITAS KHUSUS...") -> insert before r3_html
p1 = p1.replace(r3_html, '<div class="a hd2" style="left:10mm;top:257.6mm;font-size:8.4pt;display:flex">FASILITAS KHUSUS & LAYANAN PASCA-PELATIHAN</div><div class="a note" style="right:10mm;top:258.4mm">Dukungan Berkelanjutan</div>' + r3_html)
p1 = p1.replace('top:222.6mm;width:44mm', 'top:222.6mm;width:44mm')

# ============ PAGE 2 ============
chk = [("Tidak berlangganan lagi pada AI asing", "card"), ("Server berada di local dan", "srv"), ("Tidak perlu antri dengan pengguna umum dan", "users"), ("Tidak perlu pembelian atau penambahan token", "coin")]
net = '<svg class="a" style="left:0;top:0" width="118mm" height="50mm" viewBox="0 0 440 190" preserveAspectRatio="none"><g stroke="#3B8FF0" stroke-opacity=".55" stroke-width="1" fill="none"><path d="M0 150L70 110L140 135L210 70L280 105L350 40L440 70M70 110L100 40L210 70M140 135L190 185M280 105L330 170L440 140M350 40L400 0M210 70L240 10L350 40"/></g><g fill="#7FC0FF"><circle cx="70" cy="110" r="3"/><circle cx="140" cy="135" r="2.4"/><circle cx="210" cy="70" r="3.6"/><circle cx="280" cy="105" r="2.6"/><circle cx="350" cy="40" r="3.4"/><circle cx="100" cy="40" r="2.2"/><circle cx="330" cy="170" r="2.4"/><circle cx="240" cy="10" r="2.2"/><circle cx="440" cy="70" r="2.6"/></g></svg>'
hl = f'''<div class="a" style="left:0;top:62mm;width:210mm;height:50mm;background:linear-gradient(110deg,#07122A,#0F2F66 70%,#0A1628)"></div>
<div class="a" style="left:0;top:62mm;width:118mm;height:50mm;overflow:hidden">{net}</div>
<div class="a" style="left:10mm;top:70mm;width:96mm"><div style="width:11mm;height:11mm;border-radius:50%;background:#0066CC;display:grid;place-items:center;box-shadow:0 0 0 1.2mm rgba(59,143,240,.35)">{line(ICO["shield"], 21, "#fff")}</div><div style="font:800 14.6pt/1.18 P;color:#fff;margin-top:4mm">Aplikasi Intelligence ini menggunakan Local Personal dan Private AI</div></div>
<div class="a" style="left:118mm;top:62mm;width:92mm;height:50mm;background:#fff;padding-top:0">{"".join(f'<div class="chk"><i>{line(ICO[k], 16)}</i><span>{t}</span></div>' for t, k in chk)}</div>
<div class="a" style="left:118mm;top:62mm;width:1.4mm;height:50mm;background:#3B8FF0"></div>'''
apps = [("Meeting & Execution Intelligence", "Mengolah rapat tatap muka dan daring menjadi notula, ringkasan, presentasi, serta usulan tindak lanjut. Setelah disetujui, keputusan terhubung dengan PIC, tenggat, proyek, KPI, bukti penyelesaian, dan notifikasi.", d1),
        ("Program Performance & Risk Intelligence", "Membaca data pelaksanaan program, capaian indikator, anggaran, dan laporan lapangan untuk menandai penyimpangan, menjelaskan kemungkinan penyebab, serta menyarankan tindak lanjut.", d2),
        ("Policy & Regulatory Intelligence", "Membantu menelusuri regulasi, membandingkan perubahan ketentuan, memeriksa kesesuaian rancangan kebijakan, serta menyusun bahan telaah dengan rujukan pasal dan sumber sah.", d3),
        ("Document & Reporting Intelligence", "Mengubah bahan kerja yang tersebar menjadi draf nota dinas, laporan kegiatan, laporan kinerja, dan paparan pimpinan. Memeriksa konsistensi angka, periode, istilah, dan kelengkapan bukti.", d4),
        ("Knowledge & Technical Assistance Intelligence", "Asisten pengetahuan berdasarkan SOP, juknis, pedoman, dan pengalaman kerja yang disahkan. Membantu pegawai serta mitra memahami prosedur, menyiapkan materi bimtek, dan meneruskan pertanyaan yang belum terjawab kepada pejabat terkait.", d5),
        ("Aplikasi Kustomisasi Berbasis AI", "Kami mengembangkan Platform Kustomisasi Berbasis AI yang dirancang khusus agar selalu selaras dengan dinamika kebutuhan operasional direktorat/lembaga.", d6)]
tiles = "".join(f'<div class="tile {"k" if i == 5 else ""}" style="left:{10 + (i % 2) * 100}mm;top:{121 + (i // 2) * 52}mm"><div class="sc">{d}</div><div class="tx"><div class="no">{i + 1}</div><div><h5>{n}</h5><p>{t}</p></div></div></div>' for i, (n, t, d) in enumerate(apps))
p2 = f'''<div class="pg">
{P("image185.jpg", 0, 0, 210, 50)}
{logo_tab()}
<div class="blk" style="left:0;top:26mm;width:168mm;height:36mm;padding:5mm 8mm 0 10mm"><div class="kick">{KICK}</div>
<div class="t1" style="font-size:14.6pt;margin-top:1.6mm;width:150mm">Contoh Aplikasi Berbasis AI untuk Direktorat Kementerian dan Lembaga</div>
<div class="sub" style="margin-top:1.8mm;width:148mm">Materi teruji berbasis riset komparatif 12 negara dan implementasi riil untuk efisiensi serta produktivitas tanpa kompromi terhadap kerahasiaan data.</div></div>
<div class="a sl" style="left:175mm;top:50mm"><i></i><i></i><i></i><i></i></div>
{hl}
<div class="a" style="left:0;top:112mm;width:210mm;height:185mm;background:#EEF3FB"></div>
<div class="a" style="left:10mm;top:114.5mm;width:190mm;height:5.4mm;background:#163358;color:#fff;display:grid;grid-template-columns:12mm 62mm 1fr;align-items:center;padding:0 3mm;font:700 6.8pt P"><span>No</span><span>Nama Aplikasi AI</span><span>Deskripsi &amp; Dukungan Tupoksi</span></div>
{tiles}
<div class="a blk" style="left:0;top:279mm;width:210mm;height:18mm;background:#0A1628"></div>
<div class="a" style="left:10mm;top:279.6mm;font:700 7pt M;color:#fff">Bapak/Ibu dapat menghubungi kami di:</div>
<div class="a" style="left:10mm;top:283.6mm;font:500 6.4pt/1.45 M;color:#CADCFC;width:190mm"><span style="color:#7FC0FF">●</span> Sekretariat Resmi Asosiasi AI Indonesia: 08111-91-3553 / 0811-1218-448<br><span style="color:#7FC0FF">●</span> Narahubung Kelembagaan: +62 819-0111-2308 (Adah)</div>
<div class="ft" style="top:292.4mm;display:flex;justify-content:space-between;color:#9DB2D3;font-size:6pt"><span>Narahubung Kelembagaan: +62 819-0111-2308 (Adah)</span><span>Sekretariat : 08111-91-3553</span></div>
</div>'''
(ROOT / "build").mkdir(exist_ok=True)
(ROOT / "build" / "proposal.html").write_text(f'<!doctype html><meta charset=utf-8><style>{css}@page{{size:210mm 297mm;margin:0}}</style>{p1}{p2}', encoding="utf-8")
print("ok")
