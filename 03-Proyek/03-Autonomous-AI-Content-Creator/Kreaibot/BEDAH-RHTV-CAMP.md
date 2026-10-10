# BEDAH RHTV "SPOTLIGHT CAMP" — kenapa workflow orang hasilnya keren
> Riset 10 Okt 2026. Sumber: API internal `POST https://www.runninghub.ai/canvas/common-workflow/list`
> (tanpa login; balasan berisi **workflowContent lengkap** dari setiap template). Data mentah: `work/rhtv_templates.json`.

## Apa itu halaman itu
`https://rhtv.runninghub.ai/projects/canvas/camp?category=...&section=workflow&type=workflow`
= **RHTV Canvas Camp** — galeri template "one-click remix" milik RunningHub. Tab: `Spotlight Camp`,
`One-click Remix`, `Workflow Templates`. Template-nya bukan workflow ComfyUI biasa, tapi format
**canvas** (node `data.kind` = `rh-image` / `rh-video` / `rh-text` + `group`).

## API yang dipakai halaman (tanpa login, JSON polos)
| Endpoint | Isi |
|---|---|
| `POST /canvas/common-workflow/list` | 20 template + **workflowContent penuh** |
| `POST /canvas/common-workflow/type/list` | daftar kategori |
| `POST /canvas/community/category/list` | kategori komunitas |
| `POST /canvas/community/composition/list` | karya komunitas (Spotlight Camp) |
| `POST /task/quick-creation/inspiration/tags` · `/templates` | inspirasi |

## 20 TEMPLATE + MESIN YANG DIPAKAI
| id | nama | node | mesin |
|---|---|---|---|
| 364 | H3 RH Enhanced Model | 12 | `multimodal-video-rhart-video-minimax-h3-rh-enhanced` |
| 363 | RH Upscale | 8 | — |
| 362 | Floating product | 6 | — |
| 361 | Time freeze | 4 | — |
| 360 | Fall-to-Barbie trans | 6 | **MiniMax Hailuo H3** |
| 358 | Pet hairstyle | 4 | — |
| 357 | Snap transform | 4 | — |
| 356 | Drink making | 4 | **MiniMax H3 Max (image-to-video)** |
| 355 | Clutch-clothes trans | 3 | **Alibaba Wan 3.0 Prime (reference-to-video)** |
| 353 | 3D map transition (JP) | 9 | — |
| 352 | 3D map transition (KR) | 9 | — |
| 351 / 347 | Body lotion ad (KR) | 3 | — |
| 350 | Bare-face transform (KR) | 4 | **Wan 3.0 Prime** |
| 349 | Water Challenge | 3 | — |
| 348 | Screen Overflow | 3 | **MiniMax H3** |
| 346 | Y2K magazine transform | 4 | **MiniMax H3** |
| 345 | Food Ad | 3 | **MiniMax H3** + prompt timeline panjang |
| 344 | Beauty ad (KR) | 5 | **MiniMax H3** |
| 342 | GPT-Image2.5-Edit | 0 | — |

## RESEP "KEREN"-NYA (ini yang harus ditiru)
1. **Struktur minimal: 3–6 node.** `rh-image` (foto input / GPT-Image edit untuk rapiin dulu) →
   `rh-video` (mesin video) → output. Tidak ada node rumit — **kualitas datang dari prompt, bukan graph.**
2. **Mesin video = MiniMax Hailuo H3** (paling sering) atau **Alibaba Wan 3.0 Prime**.
   H3 = omni-modal (teks/gambar/video/audio), bisa **first+last frame**, native **stereo audio**,
   sampai **1080p / 15 detik**, banyak rasio.
3. **Promptnya berbentuk TIMELINE per detik** — contoh asli dari template *Food Ad*:
   ```
   【Content】
   0–2s: A fresh raw potato rests in r...
   ```
   Ditambah blok gaya: 【Camera / Visual Style】, 【Music】, dan larangan (mis. "no text").
   Ini pola `【】` yang bikin hasilnya konsisten dan sinematik.
4. **Harga H3 (dari catatan template):** 480p ¥0.10/detik · 768p ¥0.20/detik · 1080p ¥0.42/detik;
   **member RH gratis pukul 21.00–10.00** (limited RH Enhanced).
5. **Efek yang laku di camp:** transisi gaya (Barbie, Y2K magazine, bare-face), iklan produk
   (body lotion, food ad, drink making, floating product), transformasi hewan (pet hairstyle),
   challenge (water, screen overflow), transisi 3D map.

## IMPLIKASI UNTUK BOT MOTION-GRAFIS USER
- Fitur "motion grafis" yang menjual = **image-to-video dengan prompt timeline**, bukan sekadar animasi.
- Backend termurah yang sudah terbukti: **Wan 3.0 Prime** (reference-to-video) & **MiniMax H3**.
- Pola tombol: **1 foto masuk → 1 video keluar** (one-click remix) = UX yang sama dengan `MC 16:9` di
  bot @motioncontrolpro_bot. Artinya pasar ini sudah terbukti ada dua pemain.
- Jadi: bot motion user = Telegram → (RH workflow t2i/i2v) → video. Prompt timeline + preset gaya
  disimpan per tombol (mirip 20 template di atas).