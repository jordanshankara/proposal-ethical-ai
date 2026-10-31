import pathlib
H = pathlib.Path(__file__).resolve().parent
ROOT = H.parent
A = (ROOT / "assets").as_uri() + "/"
F = (ROOT / "fonts").as_uri() + "/"
css = """
@font-face{font-family:P;src:url(FF/Poppins-Bold.ttf);font-weight:700}
@font-face{font-family:P;src:url(FF/Poppins-ExtraBold.ttf);font-weight:800}
@font-face{font-family:M;src:url(FF/Montserrat-Regular.ttf);font-weight:400}
@font-face{font-family:M;src:url(FF/Montserrat-Medium.ttf);font-weight:500}
@font-face{font-family:M;src:url(FF/Montserrat-SemiBold.ttf);font-weight:600}
@font-face{font-family:M;src:url(FF/Montserrat-Italic.ttf);font-weight:500;font-style:italic}
:root{--navy:#060E1C;--navy2:#0E1F3A;--blue:#0066CC;--sky:#3B8FF0;--cy:#5EE0FF;--ice2:#CADCFC;--mut:#9DB2D3}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#060E1C;font-family:M;color:#fff}
.pg{position:relative;width:210mm;height:297mm;overflow:hidden;page-break-after:always;padding:8mm 9mm 0;
 background:radial-gradient(70% 40% at 90% 0%,rgba(59,143,240,.38),transparent 70%),radial-gradient(60% 35% at 0% 55%,rgba(0,102,204,.28),transparent 70%),radial-gradient(60% 30% at 100% 100%,rgba(94,224,255,.18),transparent 70%),linear-gradient(180deg,#07122A,#050C19 60%,#071328)}
.pg:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(127,192,255,.06) .2mm,transparent .2mm),linear-gradient(90deg,rgba(127,192,255,.06) .2mm,transparent .2mm);background-size:7mm 7mm;mask-image:linear-gradient(180deg,#000,transparent 85%);-webkit-mask-image:linear-gradient(180deg,#000,transparent 85%)}
.pg:last-child{page-break-after:auto}
.pg>*{position:relative}
.gl{border-radius:3.4mm;background:linear-gradient(145deg,rgba(255,255,255,.13),rgba(255,255,255,.04));border:.25mm solid rgba(140,190,255,.38);box-shadow:0 2mm 7mm rgba(0,0,0,.45),inset 0 .2mm .4mm rgba(255,255,255,.25)}
.kick{font:700 5.2pt P;letter-spacing:.24em;color:var(--cy)}
h1{font:800 14.6pt/1.12 P;letter-spacing:-.01em}
.sub{font:500 6.8pt/1.45 M;color:var(--ice2)}
.sec{display:flex;align-items:center;gap:2.4mm;margin:3mm 0 2mm}
.sec b{font:800 8.2pt P;letter-spacing:.01em;white-space:nowrap}
.sec b em{font-style:normal;color:var(--cy);margin-right:1.4mm}
.sec:after{content:"";flex:1;height:.3mm;background:linear-gradient(90deg,rgba(94,224,255,.8),transparent)}
.sec span{order:3;font:600 6pt M;color:var(--mut);white-space:nowrap}
.sec .sp{order:2}
.hero{display:grid;grid-template-columns:1fr 62mm;gap:3mm;height:42mm}
.hero .l{padding:3.6mm 5mm;overflow:hidden}
.hero .l:after{content:"";position:absolute;left:-10mm;bottom:-24mm;width:80mm;height:60mm;background:radial-gradient(circle,rgba(59,143,240,.5),transparent 65%)}
.hero .r{position:relative;overflow:hidden;border-radius:3.4mm}
.hero .r img{position:absolute;object-fit:cover;border-radius:2.2mm;border:.35mm solid rgba(255,255,255,.75);box-shadow:0 1.6mm 5mm rgba(0,0,0,.6)}
.land{height:16mm;display:flex;align-items:center;gap:3.4mm;padding:0 4.6mm;font:500 6.6pt/1.45 M;color:var(--ice2);margin-top:3mm}
.land b{color:#fff;font-weight:700}
.land i{flex:none;width:9mm;height:9mm;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,#3B8FF0,#0066CC);box-shadow:0 0 4mm rgba(59,143,240,.8)}
.s1{display:grid;grid-template-columns:1fr 70mm;gap:3.4mm;height:97mm}
.tl{position:relative;display:flex;flex-direction:column;justify-content:space-between;padding-left:1mm}
.tl:before{content:"";position:absolute;left:5.1mm;top:4mm;bottom:4mm;width:.35mm;background:linear-gradient(180deg,var(--cy),rgba(59,143,240,.15))}
.it{display:flex;gap:3mm;align-items:flex-start;padding:1.2mm 3mm 1.2mm 0}
.it .n{flex:none;width:8.2mm;height:8.2mm;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 30% 30%,#7FC0FF,#0066CC);box-shadow:0 0 0 .8mm rgba(94,224,255,.2),0 0 3.4mm rgba(59,143,240,.9);z-index:2}
.it h4{font:700 7pt/1.2 P}
.it em{display:block;font:700 6.1pt/1.3 M;font-style:normal;color:var(--cy);margin-top:.3mm}
.it p{font:500 5.8pt/1.38 M;color:var(--mut);margin-top:.5mm}
.cv{position:relative;height:97mm}
.cv figure{position:absolute;width:25mm;perspective:200mm}
.cv img{display:block;width:100%;aspect-ratio:210/297;object-fit:cover;border-radius:.9mm;box-shadow:-1.4mm 2.2mm 4mm rgba(0,0,0,.7),0 0 6mm rgba(59,143,240,.45)}
.cv figcaption{position:absolute;left:1.2mm;top:1.2mm;z-index:3;font:700 5pt P;background:rgba(6,14,28,.92);border:.2mm solid rgba(94,224,255,.7);padding:.5mm 1.8mm;border-radius:2mm;color:#fff;white-space:nowrap}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:2.4mm;height:27mm}
.ph{position:relative;overflow:hidden;padding:2.6mm 2.8mm;border-radius:3mm;border:.25mm solid rgba(140,190,255,.45);box-shadow:0 1.4mm 5mm rgba(0,0,0,.5)}
.ph:before{content:"";position:absolute;inset:0;background:var(--bg) center/cover;filter:saturate(.8)}
.ph:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,14,28,.45),rgba(6,14,28,.95) 62%)}
.ph>*{position:relative;z-index:2}
.ph h4{font:700 7pt/1.2 P}.ph em{display:block;font:700 6pt/1.25 M;font-style:normal;color:var(--cy);margin-top:.4mm}.ph p{font:500 5.7pt/1.38 M;color:#D6E3F7;margin-top:.7mm}
.q{height:17mm;display:flex;gap:3mm;align-items:center;padding:0 5mm;margin-top:3mm;position:relative;overflow:hidden}
.q:before{content:"\\201C";position:absolute;left:2mm;top:-5mm;font:800 44pt P;color:rgba(94,224,255,.25)}
.q div{margin-left:7mm}
.q q{display:block;font:italic 700 7.2pt/1.4 M;quotes:none}
.q p{font:500 6pt/1.4 M;color:var(--mut);margin-top:1mm}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:2.6mm;height:22mm;position:relative}
.g3:before{content:"";position:absolute;left:4mm;right:4mm;top:-1.9mm;height:.3mm;background:linear-gradient(90deg,var(--cy),var(--sky),transparent)}
.fa{padding:2.6mm 3mm;position:relative}
.fa:before{content:"";position:absolute;left:3mm;top:-3.1mm;width:2.4mm;height:2.4mm;border-radius:50%;background:var(--cy);box-shadow:0 0 3mm var(--cy)}
.fa h4{font:700 7pt/1.2 P}.fa p{font:500 5.8pt/1.4 M;color:var(--mut);margin-top:.9mm}
.bar{height:10mm;margin-top:3mm;display:flex;justify-content:space-between;align-items:center;padding:0 4mm;font:500 5.9pt/1.45 M;color:var(--ice2);background:linear-gradient(100deg,rgba(0,102,204,.55),rgba(14,31,58,.7));border-radius:3mm;border:.25mm solid rgba(94,224,255,.5)}
.bar b{color:var(--cy);font-weight:700}.bar .pill{background:linear-gradient(90deg,#5EE0FF,#3B8FF0);color:#04101F;padding:1.4mm 3.4mm;border-radius:5mm;font:800 6.4pt P;white-space:nowrap;box-shadow:0 0 4mm rgba(94,224,255,.6)}
.ft{position:absolute;left:9mm;right:9mm;bottom:5.2mm;display:flex;justify-content:space-between;font:600 6.4pt M;color:var(--mut);border-top:.25mm solid rgba(140,190,255,.3);padding-top:1.6mm}
/* page 2 */
.h2{height:32mm;position:relative;padding:4.4mm 5.4mm;overflow:hidden;margin-bottom:3mm}
.h2:after{content:"";position:absolute;right:-8mm;top:-14mm;width:70mm;height:56mm;background:radial-gradient(circle,rgba(94,224,255,.45),transparent 66%)}
.h2 img{position:absolute;right:6mm;top:4.4mm;width:34mm;z-index:2}
.h2 h1{font-size:13.4pt;margin-top:1.4mm;width:140mm}
.h2 .sub{margin-top:1.6mm;width:150mm}
.hl{height:44mm;position:relative;padding:3.2mm 4mm;overflow:hidden;border-radius:4mm;border:.3mm solid rgba(94,224,255,.75);background:radial-gradient(90% 120% at 50% 100%,rgba(0,102,204,.7),rgba(10,22,40,.4) 70%),linear-gradient(145deg,rgba(255,255,255,.1),rgba(255,255,255,.02));box-shadow:0 0 9mm rgba(59,143,240,.5),inset 0 0 8mm rgba(59,143,240,.25)}
.hl h3{text-align:center;font:800 11pt/1.2 P;letter-spacing:-.005em;color:#fff}
.orb{position:absolute;left:0;right:0;bottom:2.4mm;height:27mm;display:flex;align-items:center;justify-content:center;gap:2.4mm;padding:0 4mm}
.orb .ch{flex:1;height:22mm;border-radius:3mm;padding:2.2mm 2.4mm;background:linear-gradient(160deg,#16386A,#0B1D38);border:.25mm solid rgba(127,192,255,.7);box-shadow:0 1mm 4mm rgba(0,0,0,.5);position:relative;z-index:2}
.orb .ch i{display:grid;place-items:center;width:7mm;height:7mm;border-radius:2mm;background:linear-gradient(135deg,#5EE0FF,#0066CC);margin-bottom:1.6mm;box-shadow:0 0 3.4mm rgba(94,224,255,.7)}
.orb .ch b{display:flex;gap:1.2mm;font:600 6.8pt/1.3 M;color:#fff}
.orb .ch b:before{content:"\\2713";flex:none;color:#7FFFC0;font-weight:800}
.orb .nd{flex:none;width:23mm;height:23mm;border-radius:50%;display:grid;place-items:center;position:relative;z-index:2;background:radial-gradient(circle at 35% 30%,#7FE6FF,#0066CC 70%);box-shadow:0 0 0 1.4mm rgba(94,224,255,.2),0 0 0 3mm rgba(94,224,255,.1),0 0 9mm rgba(94,224,255,.9)}
.orb:before{content:"";position:absolute;left:5mm;right:5mm;top:50%;height:.4mm;background:linear-gradient(90deg,transparent,var(--cy) 25%,var(--cy) 75%,transparent);box-shadow:0 0 2mm var(--cy)}
.thx{display:grid;grid-template-columns:8mm 40mm 1fr;gap:2mm;margin-top:3mm;height:6mm;align-items:center;padding:0 4mm;border-radius:2mm;background:linear-gradient(90deg,rgba(0,102,204,.75),rgba(14,31,58,.7));border:.25mm solid rgba(94,224,255,.6);font:700 6.8pt P}.thx span:first-child{text-align:center}
.tg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:3mm 3.4mm}
.tile{min-width:0;overflow:hidden;height:56mm;padding:2mm 2.4mm 2.4mm}
.tile .sc{position:relative;width:100%;height:36mm;overflow:hidden;border-radius:2.2mm;background:#050B16}
.tile .app{transform:scale(.3386);transform-origin:0 0}
.tile .fl{position:absolute;right:1.6mm;bottom:1.6mm;z-index:5;padding:.9mm 1.8mm;border-radius:1.8mm;background:rgba(255,255,255,.16);backdrop-filter:blur(2mm);border:.25mm solid rgba(255,255,255,.5);font:700 4.6pt M;color:#fff;box-shadow:0 1mm 3mm rgba(0,0,0,.5)}
.tile .tx{display:flex;gap:2.2mm;margin-top:1.4mm}
.tile .no{flex:none;width:6mm;height:6mm;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,#5EE0FF,#0066CC);font:800 7pt P;box-shadow:0 0 3mm rgba(94,224,255,.7)}
.tile h5{font:700 7.2pt/1.2 P}
.tile p{font:500 6pt/1.38 M;color:var(--ice2);margin-top:.7mm}
.tile.k h5,.tile.k p{font-weight:700}
.cta{height:12.4mm;margin-top:2mm;border-radius:3mm;padding:1.6mm 5mm;background:linear-gradient(100deg,rgba(0,102,204,.7),rgba(14,31,58,.8));border:.3mm solid rgba(94,224,255,.7);box-shadow:0 0 6mm rgba(59,143,240,.35)}
.cta p{font:700 7pt M}.cta li{list-style:none;font:500 6.6pt/1.5 M;display:flex;gap:2mm;align-items:center}.cta li:before{content:"";width:1.6mm;height:1.6mm;border-radius:50%;background:var(--cy);box-shadow:0 0 2mm var(--cy)}
/* ===== dashboards ===== */
.app{width:1000px;height:400px;display:flex;background:linear-gradient(180deg,#0C1830,#08111F);font:500 12px M;color:#DCE8FB;position:relative}
.app .sb{width:58px;background:#070E1C;border-right:1px solid #1B2C4A;display:flex;flex-direction:column;align-items:center;gap:14px;padding-top:14px}
.app .sb b{width:30px;height:30px;border-radius:9px;background:linear-gradient(135deg,#5EE0FF,#0066CC)}
.app .sb s{width:22px;height:22px;border-radius:6px;background:#1B2C4A}.app .sb s.on{background:#3B8FF0;box-shadow:0 0 10px #3B8FF0}
.app .mn{flex:1;display:flex;flex-direction:column;min-width:0}
.app .tp{height:46px;border-bottom:1px solid #1B2C4A;display:flex;align-items:center;padding:0 18px;gap:14px}
.app .tp h6{font:700 15px P;color:#fff}.app .tp .se{margin-left:auto;width:230px;height:26px;border-radius:13px;background:#12233F;border:1px solid #23406B;padding:5px 12px;color:#7F97BE;font-size:11px}
.app .tp .av{width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#FFD27F,#E07A5F)}
.app .bd{flex:1;display:flex;gap:12px;padding:12px;min-height:0}
.c{background:#0F2039;border:1px solid #1F3558;border-radius:10px;padding:10px 12px;min-width:0;position:relative}
.c h7{display:block;font:700 12px P;color:#fff;margin-bottom:8px}
.c.f{flex:1}
.bdg{display:inline-block;padding:2px 8px;border-radius:9px;font:700 10px M;background:#173B6B;color:#7FC0FF}
.bdg.g{background:#0F4A36;color:#5FF0B0}.bdg.y{background:#5A4410;color:#FFD36B}.bdg.r{background:#5A1B1B;color:#FF8E8E}
.rwx{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid #1A2D4D;font-size:11.5px}
.rwx:last-child{border:0}
.mut{color:#7F97BE}.kp{font:800 24px P;color:#fff}.kp small{font:600 11px M;color:#5FF0B0;margin-left:6px}
.bar2{height:7px;border-radius:4px;background:#1B2C4A;overflow:hidden}.bar2 i{display:block;height:100%;background:linear-gradient(90deg,#3B8FF0,#5EE0FF)}
.dot{width:22px;height:22px;border-radius:50%;flex:none}
.hlw{background:rgba(255,213,107,.25);color:#FFE29A;padding:0 3px;border-radius:3px}
.add{background:rgba(95,240,176,.18);color:#8FF7C8;padding:0 3px;border-radius:3px}.del{background:rgba(255,120,120,.18);color:#FFA7A7;padding:0 3px;border-radius:3px;text-decoration:line-through}
.btn{display:inline-block;padding:6px 14px;border-radius:8px;background:linear-gradient(90deg,#3B8FF0,#0066CC);font:700 11px M;color:#fff;box-shadow:0 0 12px rgba(59,143,240,.6)}
"""
css = css.replace("FF/", F)
def im(f): return f"{A}{f}"
KICK = "PROGRAM RESMI ASOSIASI AI INDONESIA (ASOSIASI.AI)"
FOOT = '<div class="ft"><span>Narahubung Kelembagaan: +62 819-0111-2308 (Adah)</span><span>Sekretariat : 08111-91-3553</span></div>'
def svg(p, w=15): return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
ICO = {
 "work": '<rect x="3" y="7" width="18" height="12" rx="2"/><path d="M8 7V5h8v2M3 12h18"/>',
 "bank": '<path d="M3 10l9-5 9 5M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
 "mind": '<path d="M12 4a5 5 0 00-5 5c0 1.5.6 2.6 1.4 3.4.5.5.6 1 .6 1.6V16h6v-2c0-.6.1-1.1.6-1.6A5 5 0 0012 4zM10 19h4"/>',
 "book": '<path d="M4 5.5C6 4.5 9 4.5 12 6c3-1.500 6-1.500 8-.5V18c-2-1-5-1-8 .5-3-1.500-6-1.500-8-.5z"/><path d="M12 6v12.500"/>',
 "build": '<path d="M4 20V8l7-3v15M11 20V10l9 3v7M7 11h1M7 14h1M7 17h1M15 15h1M15 18h1"/>',
 "shop": '<path d="M4 9l1.500-4h13L20 9M4 9v10h16V9M4 9a2.700 2.700 0 005.300 0 2.700 2.700 0 005.400 0 2.700 2.700 0 005.300 0"/>',
 "shield": '<path d="M12 3l7.500 3v5.500c0 4.600-3 8.200-7.500 9.500-4.500-1.300-7.500-4.900-7.500-9.500V6z"/><rect x="9" y="10.500" width="6" height="5" rx="1"/><path d="M10.200 10.500V9a1.800 1.800 0 013.600 0v1.500"/>',
 "card": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M6 15h4"/><path d="M4 4l16 16" stroke="#9fe8ff"/>',
 "srv": '<rect x="4" y="4" width="16" height="6" rx="1.500"/><rect x="4" y="14" width="16" height="6" rx="1.500"/><path d="M8 7h.01M8 17h.01"/>',
 "users": '<circle cx="9" cy="8" r="3"/><path d="M3 19c0-3.300 2.700-5 6-5s6 1.700 6 5"/><path d="M16 5.500a3 3 0 010 5.500M18 19c0-2.400-1-3.900-2.800-4.600"/>',
 "coin": '<circle cx="12" cy="12" r="8"/><path d="M9.500 9.500c.6-.9 1.500-1.200 2.500-1.200 1.400 0 2.500.7 2.500 1.800 0 2.400-5 1.200-5 3.800 0 1.100 1.100 1.800 2.500 1.800 1 0 1.900-.3 2.500-1.200M12 6.500v1.800M12 15.700v1.800"/>',
 "doc": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M9.500 12h5M9.500 15.500h5"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
}
r6 = [("Riset Upskilling & Reskilling AI", "Masa Depan Dunia Kerja", "Pola adaptasi kompetensi aparatur sipil, pekerja, dan wirausaha terhadap adopsi generative AI di berbagai negara maju.", "work"),
      ("Riset Penerapan AI di Keuangan & Tata Kelola Risiko", "Kepatuhan Ketat & Mitigasi", "Standar kepatuhan data kerahasiaan tinggi, otomasi analitis presisi, serta mitigasi kebocoran rahasia institusi dan negara.", "bank"),
      ("Riset Dampak Penggunaan AI pada Kesehatan Mental", "Kesejahteraan & Mental Health", "Studi mitigasi kelelahan kognitif kerja, batas etika interaksi AI, dan menjaga kesehatan psikologis aparatur di era automasi.", "mind"),
      ("Riset Pendidikan AI Komparatif", "Pendidikan Dasar s.d. Perguruan Tinggi", "Struktur kurikulum dan kerangka penerapan AI terstruktur dari Finlandia, Singapura, dan AS untuk pembinaan SDM adaptif.", "book"),
      ("Riset Penerapan AI pada Korporasi dan Bisnis", "Efisiensi Aset & Proyek", "Optimalisasi proses operasional, analisis naskah teknis proyek, dan automasi rantai birokrasi skala besar berbasis AI.", "build"),
      ("Riset Penerapan AI pada UMKM", "Daya Saing Ekosistem Usaha", "Strategi implementasi AI praktis, penciptaan efisiensi operasional cepat, dan pemberdayaan sektor ekonomi produktif.", "shop")]
r4 = [("Industri Keuangan", "Bank Indonesia, OJK", "Penerapan tata kelola data sangat ketat, audit kepatuhan, dan analitis risiko moneter.", "image14.jpeg"),
      ("Lembaga Negara & ASN", "15+ Kementerian / Lembaga", "Drafting naskah dinas, audit dokumen, dan analisis opini publik berbasis AI etis.", "image15.jpeg"),
      ("Korporasi & BUMN", "Hutama Karya, Garudafood, AP Land", "Automasi pelaporan kinerja, materi presentasi eksekutif, dan mitigasi disrupsi kerja.", "imp_4.jpg"),
      ("Pendidikan & UMKM", "Universitas & 2.500+ UMKM", "Pengembangan talenta masa depan, efisiensi harian, dan scaling manajemen usaha.", "image17.jpeg")]
r3 = [("Kurikulum Customize", "Materi dirancang khusus menyesuaikan tugas, jenis berkas dinas, dan rutinitas kerja harian di direktorat Bapak/Ibu agar langsung memberi dampak efisiensi sejak hari pertama."),
      ("Konsultasi & Diskusi Lanjutan", "Pendampingan dan forum tanya jawab teknis pasca-pelatihan bersama instruktur untuk memastikan kelancaran adopsi alat bantu AI di lingkungan kerja instansi."),
      ("Keanggotaan Asosiasi AI", "Peserta tergabung dalam ekosistem keanggotaan Asosiasi AI Indonesia, menerima berkala riset terbaru, update regulasi etika AI, serta panduan teknologi mutakhir.")]
covers = [("cov_0.jpg", "Pendidikan"), ("cov_1.jpg", "Upskilling & Reskilling"), ("cov_2.jpg", "Kesehatan Jiwa"), ("cov_3.jpg", "Properti"), ("cov_4.jpg", "Keuangan"), ("cov_5.jpg", "UMKM")]
cpos = [(5, 0, -2), (38, 5, 2), (5, 28, 2), (38, 33, -2), (5, 56, -2), (38, 61, 2)]  # left, top (mm), rot

def pic(f, l, t, w, h, rot=0): return f'<img src="{A}{f}" style="left:{l}mm;top:{t}mm;width:{w}mm;height:{h}mm;transform:rotate({rot}deg)">'
p1 = f'''<div class="pg page">
<div class="hero"><div class="gl l"><img src="{A}image1.png" style="width:26mm;display:block;margin-bottom:1.8mm;position:relative;z-index:2"><div style="position:relative;z-index:2"><div class="kick">{KICK}</div>
<h1 style="margin-top:1.6mm">APA YANG ANDA PEROLEH DARI PELATIHAN BERSAMA ASOSIASI AI INDONESIA?</h1>
<div class="sub" style="margin-top:1.6mm">Materi teruji berbasis riset komparatif 12 negara dan implementasi riil untuk efisiensi serta produktivitas tanpa kompromi terhadap kerahasiaan data.</div></div></div>
<div class="r gl">{pic("imp_2.jpg", 3, 3, 33, 21, -3)}{pic("imp_5.jpg", 27, 18, 32, 20, 3)}{pic("imp_3.jpg", 5, 27, 33, 17, -2)}</div></div>
<div class="gl land"><i>{svg(ICO["book"], 17)}</i><div><b>Landasan Akademik & Portofolio Nyata:</b> Seluruh modul disusun langsung dari publikasi resmi 6 buku riset sektoral Asosiasi AI Indonesia serta telah diimplementasikan dalam masterclass dan workshop bersama kementerian, regulator keuangan, dan BUMN nasional.</div></div>
<div class="sec"><b><em>1</em>SUMBER MATERI: RISET STUDI BANDING 12 NEGARA</b><span>Uni Eropa, UK, AS, Singapura, Korsel, Finlandia, China, Australia, dll.</span></div>
<div class="s1"><div class="tl">{"".join(f'<div class="it"><div class="n">{svg(ICO[k], 14)}</div><div><h4>{t}</h4><em>{e}</em><p>{d}</p></div></div>' for t, e, d, k in r6)}</div>
<div class="cv">{"".join(f'<figure style="left:{l}mm;top:{t}mm;transform:rotate({r}deg)"><img src="{A}{f}"><figcaption>{c}</figcaption></figure>' for (f, c), (l, t, r) in zip(covers, cpos))}</div></div>
<div class="sec"><b><em>2</em>IMPLEMENTASI HASIL RISET PADA DUNIA INDUSTRI</b><span>Validasi Praktis di Lapangan</span></div>
<div class="g4">{"".join(f'<div class="ph" style="--bg:url({A}{f})"><h4>{t}</h4><em>{e}</em><p>{d}</p></div>' for t, e, d, f in r4)}</div>
<div class="gl q"><div><q>“Hanya hasil riset yang telah terbukti Ethical, Efektif, dan Efisien dalam proses implementasi yang kami formulasikan menjadi materi edukasi dan sertifikasi kompetensi.”</q><p>Menjamin seluruh peserta mendapatkan materi aplikatif yang siap pakai, aman dari kebocoran data rahasia/kedinasan, serta berlandaskan kepatuhan hukum dan regulasi nasional.</p></div></div>
<div class="sec"><b>FASILITAS KHUSUS & LAYANAN PASCA-PELATIHAN</b><span>Dukungan Berkelanjutan</span></div>
<div class="g3">{"".join(f'<div class="gl fa"><h4>{t}</h4><p>{d}</p></div>' for t, d in r3)}</div>
<div class="bar"><div><b>Dipandu Langsung oleh:</b> Dian Martin (Ketua Umum Asosiasi AI Indonesia) &amp; Dewan Pakar<br>Telah dipercaya oleh <b>15+ Kementerian</b>, Regulator Keuangan, BUMN Infrastruktur, dan Industri Nasional.</div><span class="pill">Publikasi Riset: asosiasi.ai</span></div>
{FOOT}</div>'''

# ================= dashboards =================
def shell(title, body, active=0):
    sb = "".join(f'<s class="{"on" if i == active else ""}"></s>' for i in range(5))
    return f'<div class="app"><div class="sb"><b></b>{sb}</div><div class="mn"><div class="tp"><h6>{title}</h6><div class="se">Cari…</div><div class="av"></div></div><div class="bd">{body}</div></div></div>'
def av(c1, c2): return f'<span class="dot" style="background:linear-gradient(135deg,{c1},{c2})"></span>'
def bars(vals, h=120, col="#3B8FF0"):
    return '<div style="display:flex;align-items:flex-end;gap:8px;height:%dpx">' % h + "".join(f'<div style="flex:1;height:{v}%;border-radius:4px 4px 0 0;background:linear-gradient(180deg,#5EE0FF,{col})"></div>' for v in vals) + '</div>'

d1 = shell("Meeting & Execution Intelligence",
 '<div class="c" style="width:252px"><h7>Rapat Hari Ini</h7>' + "".join(f'<div class="rwx">{av(a,b)}<div style="flex:1"><div style="font-weight:700;color:#fff">{t}</div><div class="mut" style="font-size:10.5px">{s}</div></div><span class="bdg {g}">{st}</span></div>' for (a, b, t, s, g, st) in [("#5EE0FF", "#0066CC", "Rapat Koordinasi Anggaran", "09.00 · Ruang Rapat 2", "g", "Selesai"), ("#FFD27F", "#E07A5F", "Evaluasi Kinerja Triwulan", "11.30 · Daring", "", "Berjalan"), ("#B28DFF", "#5B3FD6", "Telaah Draf Kebijakan", "14.00 · Ruang Rapat 1", "y", "Terjadwal"), ("#7FFFC0", "#0E8F63", "Sinkronisasi Program Prioritas", "15.30 · Daring", "y", "Terjadwal")]) + '</div>'
 '<div class="c f"><h7>Transkrip Langsung &nbsp;<span class="bdg r">● Merekam 00:42:18</span></h7><div style="display:flex;gap:2px;align-items:center;height:22px;margin-bottom:8px">' + "".join(f'<i style="width:4px;border-radius:3px;background:#3B8FF0;height:{h}%"></i>' for h in [30, 55, 80, 45, 90, 60, 35, 70, 95, 50, 40, 75, 55, 85, 45, 65, 30, 60, 80, 40, 70, 50, 90, 35, 60, 45, 75, 55, 30, 65, 85, 50, 40, 70]) + '</div>' + "".join(f'<div style="display:flex;gap:8px;margin-bottom:9px">{av(a,b)}<div style="font-size:11.5px;line-height:1.5"><b style="color:#fff">{n}</b> <span class="mut">{tm}</span><br>{tx}</div></div>' for (a, b, n, tm, tx) in [("#FFD27F", "#E07A5F", "Bu Ratna", "00:41:02", 'Serapan anggaran triwulan ini <span class="hlw">baru 62%</span>, perlu percepatan.'), ("#5EE0FF", "#0066CC", "Pak Dimas", "00:41:40", 'Kami usulkan <span class="hlw">laporan dikirim Jumat</span> setelah verifikasi PIC.'), ("#B28DFF", "#5B3FD6", "Adah", "00:42:05", 'Disepakati. Tenggat disesuaikan dengan jadwal bimtek.')]) + '</div>'
 '<div class="c" style="width:277px"><h7>Ringkasan &amp; Tindak Lanjut</h7>' + "".join(f'<div class="rwx"><span style="flex:1"><b style="color:#fff">{t}</b><div class="mut" style="font-size:10.5px">PIC: {p} · {d}</div></span><span class="bdg {g}">{s}</span></div>' for (t, p, d, g, s) in [("Revisi laporan kinerja", "Dimas", "14 Nov", "g", "Disetujui"), ("Verifikasi data anggaran", "Ratna", "13 Nov", "y", "Menunggu"), ("Susun materi bimtek", "Adah", "20 Nov", "g", "Disetujui"), ("Presentasi pimpinan", "Dimas", "22 Nov", "y", "Menunggu")]) + '<div style="margin-top:10px" class="bar2"><i style="width:68%"></i></div><div class="mut" style="font-size:10.5px;margin:4px 0 8px">KPI terhubung · 68% selesai</div><span class="btn">Setujui &amp; Kirim Notifikasi</span></div>')
d2 = shell("Program Performance & Risk Intelligence",
 '<div style="display:flex;flex-direction:column;gap:12px;flex:1.35;min-width:0"><div style="display:flex;gap:12px">' + "".join(f'<div class="c f"><div class="mut" style="font-size:10.5px">{l}</div><div class="kp">{v}<small style="color:{c}">{d}</small></div></div>' for (l, v, d, c) in [("Serapan Anggaran", "78%", "▲ 4,2%", "#5FF0B0"), ("Capaian Indikator", "84%", "▲ 1,8%", "#5FF0B0"), ("Program Berisiko", "3", "▼ 1", "#5FF0B0"), ("Deviasi Terdeteksi", "7", "▲ 2", "#FF8E8E")]) + '</div><div class="c f"><h7>Anggaran vs Realisasi per Bulan</h7>' + bars([40, 52, 48, 66, 60, 75, 70, 84, 78, 90, 82, 94], 150) + '<svg style="position:absolute;left:12px;right:12px;top:50px" width="96%" height="116" viewBox="0 0 100 40" preserveAspectRatio="none"><polyline points="2,34 11,30 20,32 29,24 38,26 47,18 56,20 65,12 74,15 83,8 92,12 98,5" fill="none" stroke="#FFD36B" stroke-width=".8"/><circle cx="83" cy="8" r="1.4" fill="#FF6B6B"/></svg></div></div>'
 '<div class="c" style="width:210px"><h7>Matriks Risiko</h7><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:4px">' + "".join(f'<i style="height:29px;border-radius:5px;background:{c}"></i>' for c in ["#1E4D7A", "#1E4D7A", "#7A6A1E", "#8A3F1E", "#A12A2A", "#1E4D7A", "#7A6A1E", "#7A6A1E", "#8A3F1E", "#A12A2A", "#18694E", "#1E4D7A", "#7A6A1E", "#7A6A1E", "#8A3F1E", "#18694E", "#18694E", "#1E4D7A", "#1E4D7A", "#7A6A1E", "#18694E", "#18694E", "#18694E", "#1E4D7A", "#1E4D7A"]) + '</div></div>'
 '<div class="c" style="width:244px"><h7>Peringatan &amp; Penyebab</h7>' + "".join(f'<div class="rwx"><span class="bdg {g}">{s}</span><span style="flex:1"><b style="color:#fff">{t}</b><div class="mut" style="font-size:10.5px">{d}</div></span></div>' for (g, s, t, d) in [("r", "Tinggi", "Output 2 menyimpang", "Realisasi 31% di bawah target"), ("y", "Sedang", "Serapan belanja modal", "Kontrak terlambat 3 minggu"), ("y", "Sedang", "Laporan lapangan tertunda", "2 dari 8 satker belum lapor"), ("g", "Rendah", "Indikator kinerja utama", "Sesuai rencana")]) + '<span class="btn" style="margin-top:8px">Usulkan Tindak Lanjut</span></div>', 1)
d3 = shell("Policy & Regulatory Intelligence",
 '<div style="display:flex;flex-direction:column;gap:12px;flex:1;min-width:0"><div class="c" style="padding:8px 14px;color:#9DB2D3;font-size:12px">🔍 &nbsp;kewajiban pelindungan data pribadi pada sistem AI pemerintah</div><div style="display:flex;gap:12px;flex:1;min-width:0"><div class="c" style="width:244px"><h7>Hasil Penelusuran (12)</h7>' + "".join(f'<div class="rwx"><span style="flex:1"><b style="color:#fff">{t}</b><div class="mut" style="font-size:10.5px">{d}</div></span><span class="bdg {g}">{s}</span></div>' for (t, d, g, s) in [("UU No. 27 Tahun 2022", "Pelindungan Data Pribadi", "g", "Berlaku"), ("Draf Perpres Tata Kelola AI", "Versi 3 · diperbarui", "y", "Draf"), ("Rancangan Peraturan Direktorat", "Pasal 12 ayat (3)", "y", "Ditelaah"), ("Pedoman Keamanan Informasi", "Edisi terbaru", "g", "Berlaku")]) + '</div>'
 '<div class="c f"><h7>Perbandingan Perubahan Ketentuan</h7><div style="display:flex;gap:12px;font-size:11.5px;line-height:1.7"><div style="flex:1"><b class="mut">Sebelum</b><br>Pasal 12 ayat (3): Data dapat <span class="del">diolah pada layanan pihak ketiga</span> setelah mendapat persetujuan atasan.</div><div style="flex:1"><b class="mut">Sesudah</b><br>Pasal 12 ayat (3): Data <span class="add">wajib diolah pada infrastruktur lokal</span> setelah mendapat persetujuan atasan.</div></div><div style="margin-top:10px"><span class="bdg">Pasal 12</span> <span class="bdg">Ayat 3</span> <span class="bdg g">Sumber sah</span></div></div></div></div>'
 '<div class="c" style="width:210px"><h7>Telaah Kesesuaian Rancangan</h7><div class="kp">86%<small>sesuai</small></div><div class="bar2" style="margin:6px 0 10px"><i style="width:86%"></i></div>' + "".join(f'<div class="rwx"><span style="color:{c}">{i}</span><span style="flex:1">{t}</span></div>' for (i, c, t) in [("✓", "#5FF0B0", "Dasar hukum tercantum"), ("✓", "#5FF0B0", "Rujukan pasal valid"), ("!", "#FFD36B", "Ayat (3) perlu penyesuaian"), ("✗", "#FF8E8E", "Sanksi belum diatur")]) + '</div>', 2)
d4 = shell("Document & Reporting Intelligence",
 '<div class="c" style="width:168px"><h7>Bahan Kerja Terhimpun</h7>' + "".join(f'<div class="rwx"><span style="color:#5EE0FF">▤</span><span style="flex:1">{t}</span><span class="mut">{n}</span></div>' for (t, n) in [("Laporan kegiatan", "8"), ("Data anggaran", "5"), ("Notulen rapat", "12"), ("Foto bukti", "34"), ("Laporan kinerja", "4")]) + '</div>'
 '<div class="c f" style="background:#F4F8FF;color:#13233F;padding:16px 28px"><div style="font:800 15px P;text-align:center">NOTA DINAS</div><div style="text-align:center;font-size:10.5px;color:#5D6B82;margin-bottom:10px">Draf disusun otomatis · v2</div><div style="font-size:11.5px;line-height:1.75">Kepada Yth. Pimpinan Direktorat<br>Hal: Laporan pelaksanaan kegiatan triwulan III<br><br>Realisasi anggaran sebesar <span style="background:#FFE9A8;padding:0 3px">Rp 4,82 miliar</span> atau <span style="background:#FFE9A8;padding:0 3px">78%</span> dari pagu, dengan capaian indikator <span style="background:#FFE9A8;padding:0 3px">84%</span> pada periode Juli–September.</div></div>'
 '<div class="c" style="width:277px"><h7>Pemeriksaan Konsistensi</h7>' + "".join(f'<div class="rwx"><span style="color:{c};font-weight:800">{i}</span><span style="flex:1">{t}</span><span class="bdg {g}">{s}</span></div>' for (i, c, t, g, s) in [("✓", "#5FF0B0", "Angka antar dokumen", "g", "Konsisten"), ("!", "#FFD36B", "Periode laporan", "y", "1 selisih"), ("✓", "#5FF0B0", "Istilah baku", "g", "Sesuai"), ("✓", "#5FF0B0", "Kelengkapan bukti", "g", "92%")]) + '<div style="margin:10px 0 4px" class="bar2"><i style="width:92%"></i></div><div class="mut" style="font-size:10.5px;margin-bottom:8px">Siap diserahkan ke pimpinan</div><span class="btn">Ekspor Nota Dinas</span> <span class="bdg" style="margin-left:6px">Paparan</span></div>', 3)
d5 = shell("Knowledge & Technical Assistance Intelligence",
 '<div class="c" style="width:193px"><h7>Basis Pengetahuan</h7>' + "".join(f'<div class="rwx"><span style="color:#5EE0FF">◆</span><span style="flex:1">{t}</span><span class="bdg">{n}</span></div>' for (t, n) in [("SOP", "24"), ("Juknis", "18"), ("Pedoman", "11"), ("Pengalaman Kerja", "37")]) + '<div class="mut" style="font-size:10.5px;margin-top:10px">Hanya dokumen yang telah disahkan</div></div>'
 '<div class="c f"><h7>Asisten Prosedur</h7><div style="background:#173B6B;border-radius:10px 10px 2px 10px;padding:8px 12px;width:60%;margin-left:auto;font-size:11.5px">Bagaimana prosedur pertanggungjawaban SPJ perjalanan dinas?</div><div style="display:flex;gap:8px;margin-top:10px">' + av("#5EE0FF", "#0066CC") + '<div style="background:#13294A;border:1px solid #23406B;border-radius:2px 10px 10px 10px;padding:8px 12px;font-size:11.5px;line-height:1.6">Prosedur SPJ dilakukan dalam 4 tahap: pengajuan, verifikasi, pengesahan, dan arsip. Batas waktu penyampaian <span class="hlw">5 hari kerja</span> setelah kegiatan selesai.<div style="margin-top:6px"><span class="bdg">SOP-07 hal. 12</span> <span class="bdg">Juknis 2025</span></div></div></div></div>'
 '<div class="c" style="width:252px"><h7>Sumber Rujukan</h7><div style="font-size:11px;line-height:1.7;color:#BFD0EA"><b style="color:#fff">SOP-07 · Pertanggungjawaban Perjalanan Dinas</b><br>…SPJ disampaikan paling lambat <span class="hlw">5 (lima) hari kerja</span> setelah kegiatan, dilengkapi bukti pengeluaran sah…</div><div style="margin-top:12px"><span class="bdg g">Disahkan</span> <span class="bdg">Versi 2025</span></div><div style="margin-top:12px" class="mut">Pertanyaan belum terjawab?</div><span class="btn" style="margin-top:6px">Teruskan ke Pejabat Terkait</span></div>', 4)
d6 = shell("Aplikasi Kustomisasi Berbasis AI",
 '<div class="c" style="width:168px"><h7>Modul</h7>' + "".join(f'<div class="rwx"><span style="width:15px;height:15px;border-radius:5px;background:{c}"></span><span style="flex:1">{t}</span><span class="mut">＋</span></div>' for (t, c) in [("Anggaran", "#3B8FF0"), ("Laporan", "#5EE0FF"), ("Perizinan", "#B28DFF"), ("Aset", "#5FF0B0"), ("Kepegawaian", "#FFD36B")]) + '</div>'
 '<div class="c f" style="background:repeating-linear-gradient(0deg,#0F2039,#0F2039 19px,#142848 20px)"><h7>Kanvas Rancangan · Direktorat</h7><div style="display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:10px"><div class="c" style="height:92px;grid-row:span 2;border-color:#3B8FF0;box-shadow:0 0 14px rgba(59,143,240,.5)"><b style="font-size:11px">Modul Anggaran</b>' + bars([40, 60, 55, 80, 70, 90], 66) + '</div><div class="c" style="height:42px"><b style="font-size:11px">Modul Laporan</b><div class="bar2" style="margin-top:8px"><i style="width:72%"></i></div></div><div class="c" style="height:42px"><b style="font-size:11px">Modul Aset</b><div class="kp" style="font-size:16px">248</div></div><div class="c" style="height:40px;grid-column:span 2;border:1px dashed #3B8FF0;display:grid;place-items:center;color:#5EE0FF">＋ Tambah modul kustom</div></div></div>'
 '<div class="c" style="width:202px"><h7>Pengaturan Modul</h7>' + "".join(f'<div class="rwx"><span class="mut" style="width:76px">{l}</span><span style="flex:1;background:#12233F;border:1px solid #23406B;border-radius:6px;padding:4px 8px">{v}</span></div>' for (l, v) in [("Sumber data", "SIMAK-BMN"), ("Peran", "Operator"), ("Alur", "Persetujuan 2 tingkat"), ("Notifikasi", "Aktif")]) + '<span class="btn" style="margin-top:10px">Terapkan</span></div>', 0)

chk = [("Tidak berlangganan lagi pada AI asing", "card"), ("Server berada di local dan", "srv"), ("Tidak perlu antri dengan pengguna umum dan", "users"), ("Tidak perlu pembelian atau penambahan token", "coin")]
chs = "".join(f'<div class="ch"><i>{svg(ICO[k], 14)}</i><b>{t}</b></div>' for t, k in chk)
orb = f'<div class="orb">{"".join([f"<div class=ch><i>{svg(ICO[chk[0][1]], 14)}</i><b>{chk[0][0]}</b></div>", f"<div class=ch><i>{svg(ICO[chk[1][1]], 14)}</i><b>{chk[1][0]}</b></div>", f"<div class=nd>{svg(ICO["shield"], 38)}</div>", f"<div class=ch><i>{svg(ICO[chk[2][1]], 14)}</i><b>{chk[2][0]}</b></div>", f"<div class=ch><i>{svg(ICO[chk[3][1]], 14)}</i><b>{chk[3][0]}</b></div>"])}</div>'
apps = [("Meeting & Execution Intelligence", "Mengolah rapat tatap muka dan daring menjadi notula, ringkasan, presentasi, serta usulan tindak lanjut. Setelah disetujui, keputusan terhubung dengan PIC, tenggat, proyek, KPI, bukti penyelesaian, dan notifikasi.", d1),
        ("Program Performance & Risk Intelligence", "Membaca data pelaksanaan program, capaian indikator, anggaran, dan laporan lapangan untuk menandai penyimpangan, menjelaskan kemungkinan penyebab, serta menyarankan tindak lanjut.", d2),
        ("Policy & Regulatory Intelligence", "Membantu menelusuri regulasi, membandingkan perubahan ketentuan, memeriksa kesesuaian rancangan kebijakan, serta menyusun bahan telaah dengan rujukan pasal dan sumber sah.", d3),
        ("Document & Reporting Intelligence", "Mengubah bahan kerja yang tersebar menjadi draf nota dinas, laporan kegiatan, laporan kinerja, dan paparan pimpinan. Memeriksa konsistensi angka, periode, istilah, dan kelengkapan bukti.", d4),
        ("Knowledge & Technical Assistance Intelligence", "Asisten pengetahuan berdasarkan SOP, juknis, pedoman, dan pengalaman kerja yang disahkan. Membantu pegawai serta mitra memahami prosedur, menyiapkan materi bimtek, dan meneruskan pertanyaan yang belum terjawab kepada pejabat terkait.", d5),
        ("Aplikasi Kustomisasi Berbasis AI", "Kami mengembangkan Platform Kustomisasi Berbasis AI yang dirancang khusus agar selalu selaras dengan dinamika kebutuhan operasional direktorat/lembaga.", d6)]
tiles = "".join(f'<div class="gl tile {"k" if i == 5 else ""}"><div class="sc">{d}</div><div class="tx"><div class="no">{i + 1}</div><div><h5>{n}</h5><p>{t}</p></div></div></div>' for i, (n, t, d) in enumerate(apps))
p2 = f'''<div class="pg page">
<div class="gl h2"><img src="{A}image1.png"><div class="kick" style="position:relative;z-index:2">{KICK}</div><h1 style="position:relative;z-index:2">Contoh Aplikasi Berbasis AI untuk Direktorat Kementerian dan Lembaga</h1><div class="sub" style="position:relative;z-index:2">Materi teruji berbasis riset komparatif 12 negara dan implementasi riil untuk efisiensi serta produktivitas tanpa kompromi terhadap kerahasiaan data.</div></div>
<div class="hl"><h3>Aplikasi Intelligence ini menggunakan Local Personal dan Private AI</h3>{orb}</div>
<div class="thx"><span>No</span><span>Nama Aplikasi AI</span><span>Deskripsi &amp; Dukungan Tupoksi</span></div><div class="tg" style="margin-top:2mm">{tiles}</div>
<div class="cta"><p>Bapak/Ibu dapat menghubungi kami di:</p><ul><li>Sekretariat Resmi Asosiasi AI Indonesia: 08111-91-3553 / 0811-1218-448</li><li>Narahubung Kelembagaan: +62 819-0111-2308 (Adah)</li></ul></div>
{FOOT}</div>'''
(H / "lamp2.html").write_text(f'<!doctype html><meta charset=utf-8><style>{css}@page{{size:210mm 297mm;margin:0}}</style>{p1}{p2}', encoding="utf-8")
print("ok")
