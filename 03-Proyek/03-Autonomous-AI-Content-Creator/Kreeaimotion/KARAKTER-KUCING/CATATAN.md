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

## Varian VLOG tanpa HP (revisi user: "selfie hp nya jangan keliatan, kaya lagi vlog")
| Kode | Isi | Catatan |
|---|---|---|
| W1 | vlog close-up, mulut terbuka, menatap kamera | **paling pas buat wajah vlogger** — anatomi normal, tanpa HP |
| W2 | vlog full body di jalan | ❌ berdiri bipedal seperti manusia — tidak natural |
| W3 | vlog ceria, suasana sore | bagus (anatomi normal), vibe malam |

Analisa: ketiganya TANPA HP/kamera/mikrofon/tangan manusia, menatap kamera, dan masih kucing yang sama.
Rekomendasi sheet: **master identitas = B** (full body) + **wajah vlogger = W1**.

## Revisi 2 (user): "tangannya kaya pegang hp dong" — tangan POSISI menggenggam, HP tidak digambar
| Kode | Framing | Catatan |
|---|---|---|
| X1 | close-up (muka + dada + paw naik) | paw agak seperti mitten, toe kurang jelas |
| X2 | medium (dada, paw jelas) | mulut terbuka jelas, paw menggenggam |
| X3 | full body duduk, 1 paw naik | ekor melingkar, latar sudut jalan |

Bukti: satu kaki depan NAIK dengan pose menggenggam, **tidak ada objek** di genggaman (HP tidak
digambar), mata ke kamera, mulut terbuka. Masih kucing yang sama, tanpa kaki berlebih/tangan manusia.

## Revisi 3 (FINAL, dari user): "paw nya nggak keliatan karena lagi pegang hp"
Maksudnya: kucing memegang HP di depan → yang terlihat PUNGGUNG HP (+ modul kamera),
paw-nya TERTUTUP HP / di bawah frame → tidak digambar sama sekali. (Bukan "tanpa HP".)
| Kode | Isi | Paw kelihatan? | HP |
|---|---|---|---|
| K1 | HP di samping muka | tidak | punggung HP + modul kamera |
| K2 | HP di depan dada | ya (paw di tanah) | punggung HP |
| K3 | HP gede di depan bawah | tidak | punggung HP, bawah kepotong frame |
| K4 | HP di bawah kamera, bawah kepotong | tidak | paling wajar "dipegang dari bawah" |
| K5 | HP miring di bawah kiri | tidak | punggung HP |

Catatan: karena pemegangnya memang tidak boleh kelihatan, HP cenderung terkesan mengambang —
K4 paling tidak terasa mengambang (bawah HP kepotong tepi frame).
