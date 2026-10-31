# Proyek: Proposal Pelatihan Ethical AI - Asosiasi AI Indonesia

PDF A4, **tepat 2 halaman**, dibuat dari HTML/CSS (Python menghasilkan HTML, Chrome merender PDF).

## Aturan
- Balas dalam Bahasa Indonesia.
- Jangan ubah, tambah, atau hapus teks kecuali diminta. Teks asli pengguna harus tetap persis. Perbaiki typo hanya bila diminta.
- Hasil harus tetap 2 halaman A4. Jangan sampai ada halaman ke-3.
- Warna wajib identitas Asosiasi AI: navy #0A1628 / #163358, biru #0066CC / #3B8FF0. Font: Poppins (judul), Montserrat (isi). Foto pakai warna asli (tidak diberi tint biru).
- Gaya desain: editorial datar (blok warna solid, foto full-bleed, ruang putih), bukan kartu kaca atau gelembung.
- Teks di dalam dashboard adalah contoh tampilan buatan, bukan data nyata.

## Struktur
- `src/gen3.py`: layout dan semua teks halaman 1 dan 2 (posisi dalam mm, absolute).
- `src/gen2.py`: helper ikon dan 6 dashboard desktop (dipakai oleh gen3 lewat exec).
- `assets/`, `fonts/`: foto, cover buku, font.
- `output/Proposal.pdf`: hasil build.

## Build
Di GitHub, push ke `main` akan menjalankan workflow "Build PDF" (.github/workflows/build.yml) yang merender PDF dan meng-commit `output/Proposal.pdf`. Workflow gagal bila PDF bukan 2 halaman.

Lokal (butuh Chrome/Edge):
```
pip install -r requirements.txt
python src/gen3.py
sed -i 's/class="pg"/class="pg page"/g' build/proposal.html
python tools/render.py build/proposal.html --size 210x297mm --dpi 150 --out output/Proposal --formats pdf --multipage
```
Jangan commit `build/`. Setelah mengubah desain, cek PDF hasilnya terlihat benar (tidak ada teks terpotong atau menumpuk) sebelum menyatakan selesai.
