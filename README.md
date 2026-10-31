# Proposal Pelatihan Ethical AI - Asosiasi AI Indonesia (PDF A4, 2 halaman)

Desain ulang "Lampiran 1_Proposal Pelatihan Ethical AI" dalam HTML/CSS, dirender ke PDF oleh GitHub Actions.
Hasil terbaru: **`output/Proposal.pdf`** (buka langsung dari HP lewat aplikasi GitHub atau browser).

## Cara ubah dari HP
1. Buka repo di aplikasi GitHub atau github.com, lalu buka `src/gen3.py`.
2. Tekan ikon pensil (Edit), ubah teks (semua teks ada di file ini, cari kata yang mau diganti), lalu Commit.
3. Tab **Actions** otomatis menjalankan "Build PDF" (sekitar 1 menit). Setelah hijau, `output/Proposal.pdf` terbarui.
4. Mau jalankan manual: Actions -> Build PDF -> Run workflow.

## Isi folder
- `src/gen3.py` : layout dan seluruh teks halaman 1 dan 2. `src/gen2.py` : dashboard 6 aplikasi dan ikon.
- `assets/` : foto dan cover buku. Ganti foto dengan mengunggah file bernama sama.
- `fonts/` : Poppins dan Montserrat. `tools/render.py` : HTML ke PDF (Chrome headless).
- `output/Proposal.pdf` : hasil jadi.

## Jalankan di komputer
```bash
pip install -r requirements.txt
python src/gen3.py
sed -i 's/class="pg"/class="pg page"/g' build/proposal.html
python tools/render.py build/proposal.html --size 210x297mm --dpi 150 --out output/Proposal --formats pdf --multipage
```
Perlu Google Chrome atau Edge terpasang (atau set `CHROME_PATH`).

## Catatan
- Warna mengikuti identitas Asosiasi AI: navy `#0A1628`, `#163358`, biru `#0066CC`, `#3B8FF0`.
- Nama dokumen, pasal, dan angka di dashboard hanya contoh tampilan, mohon cek sebelum dikirim ke klien.
- Repo ini berisi foto kegiatan dan cover buku Asosiasi AI. Biarkan **private** kecuali sudah disetujui dipublikasikan.
