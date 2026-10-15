# KARAKTER KUCING OREN (kandidat, 15 Okt 2026)

## Identitas terkunci (dipakai di SEMUA generate berikutnya)
> a photorealistic orange tabby (ginger) cat: slightly chubby with a round belly, short dense fur
> with soft darker orange stripes, white chin and a white chest patch, white socks on all four paws,
> round amber eyes, pink nose, small rounded ears, friendly slightly smug expression

## Kandidat master (4 varian, semua kucing yang sama)
| Kode | Pose | Catatan |
|---|---|---|
| A | selfie pegang HP (close-up) | paling iconic, tapi HP kebalik → sudah diperbaiki lewat V1 |
| B | duduk di trotoar (full body) | **paling bersih** — kandidat master |
| C | vlog mulut terbuka | lengan terlalu panjang/aneh |
| D | jalan ke kamera | sesuai, badan agak memanjang |

## Bukti konsistensi (dari master B)
- V1 pose baru: selfie, HP menghadap muka kucing (lihat punggung HP + modul kamera) — sama kucingnya
- V2 background baru: kamar hijau zaitun + kursi cokelat — sama kucingnya
- Analisa: identitas (belang, dagu/dada putih, mata amber, badan gemuk) tetap; yang berubah hanya
  pose/latar. Tidak ada kaki berlebih / tulisan.

## Catatan teknis
- `/images/generations` (teks→gambar): gpt-image-2 & gemini-3.0-pro-image dua-duanya jalan.
- `/images/edits` 1 gambar (ganti pose/latar): gpt-image-2 jalan (~1-2 mnt).
- `/images/edits` 2 gambar (komposit): gpt-image-2 sering 524 → pakai gemini-3.0-pro-image.
- Ukuran: minta 1024x1536 → gpt-image-2 patuh persis; gemini balik 848x1264.
