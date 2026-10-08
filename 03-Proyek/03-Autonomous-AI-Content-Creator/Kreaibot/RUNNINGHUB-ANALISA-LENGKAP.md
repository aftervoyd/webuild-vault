# Analisa Menyeluruh RunningHub — 8 Okt 2026

Sumber: langsung dari situs (login akun **Nimara Official**). Bukti mentah: `runninghub_analisa.md` (di workspace) + `bukti/runninghub-analisa-8okt.md`.

---

## A. Status akun (temuan penting)

| Item | Nilai |
|---|---|
| Akun | Nimara Official · ID `2108050207926067202` |
| **Membership** | **AKTIF** — plan `Personal`, **$9.9/bulan**, aktif s/d **2026-11-08** (auto-renew) |
| Jatah bulanan | **36.000 RHCoins** + $1 wallet (Plan A: power user AI apps/workflow/open-source spt Qwen, Wan, LTX) |
| Saldo saat analisa | **34.993 RHCoins** + **$1** |
| Invite code akun | `baaxhjzz` |

Artinya: biaya render bulanan **sudah dibayar** sampai 8 Nov 2026.

## B. Ekonomi (terverifikasi dari menu Tasks & Billing)

- **Tier runtime koin**: Lite `0,02` · **Standard `0,2`** · Plus `0,4` koin per detik → akun kita di **Standard**.
- **Terverifikasi**: 5s i2v = 59–68 koin (~Rp263–303) · 15s UGC = 257 koin (~Rp1.146) · 11 task total 1.107 koin, **Wallet $0** (semua koin).
- 36.000 koin/bulan ÷ ~66 koin = **±545 render i2v 5 detik per bulan** untuk $9.9 (~Rp160rb) → **±Rp290/render**.
- Urutan pemakaian: bonus harian → koin member → koin undangan → koin beli.
- Masa berlaku: koin member 31 hari · koin beli/undangan 1 tahun.
- Paket koin: 18.000/$9.9 · 28.000/$14.9 · 42.000/$17.9 · 78.000/$32.9 · 200.000/$79.9.
- ⚠️ **Koin TIDAK berlaku untuk Shared/Dedicated API** (API dihitung $ terpisah) — jalur workflow kita tetap yang termurah.

## C. Penawaran besar (potensi hemat/pendapatan)

1. **MiniMax H3 RH Enhanced — member dapat 1 BULAN GENERASI UNLIMITED + 13 JAM GRATIS/HARI** (9AM–10PM ET / 6AM–7PM PT). → perlua diuji: apakah task workflow kita kena gratisnya.
2. **Vidu Q4 Preview** — member dari `$0.023/detik`, sampai 4K, kontrol kamera lebih natural.
3. **Seedance 2.5** — sampai `$0.036/detik` (subsidi $100M).
4. **GPT-5.6/5.5 API** — diskon s/d 65%.
5. **RH Upscale** (RH Original) — video SR generatif 5 mode (ULTRA/MAX/HIGH/MEDIUM/LOW), 540p→1080p, Face Score 0.640 → bahan tier "HD".

## D. Harga Model API ($/detik) — jalur $ (bukan jalur koin kita)

| Model | 480p | 720p/768p | 1080p |
|---|---|---|---|
| **LTX-2.3 image-to-video** (model Kuzushi) | $0.01/s | $0.02/s | $0.03/s |
| **MiniMax H3 RH Enhanced i2v / multi-ref / t2v** | $0.03/s | $0.04/s | $0.06/s |
| MiniMax H3 max-turbo i2v | $0.032/s | $0.05/s | — |
| Wan 3.0 t2v | $0.04/s | $0.07/s | $0.14/s |

H3 Context-IR (i2va/r2va): $0.83/1M token input · $3.29/1M token output.
→ Jalur workflow koin (0,2 koin/s ≈ $0.00008/s) jauh lebih murah daripada Model API.

## E. Perpustakaan workflow — SEMUA yang kita butuh ada

- `MINIMAX H3 IMAGE-TO-VIDEO WORKFLOW` (post `2084508334299897858`)
- `MINIMAX H3 FL2VA-FIRST FRAME TO VIDEO` / `-LAST FRAME` / `T2VA`
- **`MINIMAX H3 ALL-IN-ONE REFERENCE`** (post `2084237808348286977`) — **Ref2VA: referensi GAMBAR + VIDEO + AUDIO** (17 node: `RHMiniMaxH3Ref2VAImageReference`, `...VideoReference`, `...AudioReference`, `...Target`, `DualSigmaSampler`, dll)
- `MINIMAX H3 ALL-IN-ONE REFERENCE 2K DIRECT OUTPUT`
- `[ONE-CLICK BACKGROUND CHANGE] PRODUCT PICTURE PHOTOGRAPHY`
- `INFINITETALK DIGITAL HUMAN` (lip sync / digital human)
- `TEXT-TO-VIDEO FAST LTX2.5 SYNC AUDIO & VIDEO`
- `ALMIGHTY VIDEO X VIDEO CONTINUATION` (sambung video >15 dtk)
- `SEEDANCE 2.0 ALL-IN-ONE REFERENCE VIDEO`

## F. Fitur produk platform

- **AI Apps** — app ComfyUI siap pakai; Seedance 2.5 mendukung **output 30 detik**, action transfer, dress-up, multimodal. Billing: `Model API Fee + Runtime Fee`.
- **Quick Create** (`/ai-generator`) — generator terpandu (pilih profesi → tool) + tab `API call`.
- **rhTV** (`rhtv.runninghub.ai`) — platform publikasi film AI: Projects, Asset Library, Skills, Community, Plugins, Star Agent. → kandidat kanal publikasi konten KREE.AI.
- **AI Canvas / RHSTORY / ShortDramaAI** — halaman SPA (belum sempat ambil detail; render kosong).
- **RH_Skills · RH_CLI · ComfyUI Plugin · AI Developer Kit** — tooling dev; `RH_Skills` = skill agent siap pakai (bisa dipasang ke Hermes).

## G. Program cuan

1. **Undangan**: 1 user baru = **500 koin** (pengundang + diundang); maks **5.000 koin/hari**; **partner promosi tanpa batas** (bisa diajukan).
2. **AIGC Feature Film Competition (Chinese Nebula Awards)**: hadiah tunggal s/d **USD 150.000 cash**; total CNY 5,5M (3,5M cash + 2M compute). Deadline teaser ≥2 menit: **09 Okt 2026**; film final 03 Nov. Tema: Sci-Fi / Glimmer / Brand Studio.
3. **Social Creator Incentive**: 28 Sep–10 Nov; pool **¥20.000 kredit** (11 pemenang), top-200 partisipasi ¥20 kredit, 50 kursi potential creator (member 1 bulan ¥199). Platform: Douyin/Xiaohongshu/Bilibili/WeChat.
4. **My Earnings** (menu akun) — belum berhasil dibuka (klik tidak navigasi).

## H. Rekomendasi berurutan (kualitas + untung)

| # | Langkah | Kenapa | Dampak |
|---|---|---|---|
| 1 | Uji **13 jam gratis/hari + 1 bulan unlimited H3** untuk task workflow kita | kalau kena → biaya render H3 ≈ Rp0 selama 13 jam/hari | 💰 hemat besar |
| 2 | Pindah i2v ke **H3 Image-to-Video / Ref2VA** | data: FL2VA (foto di 2 ujung) → gerak orang jatuh (wajah 28,2 · badan 13,4); Kuzushi i2v murni wajah 42,7 · badan 26,9 | 🎬 kualitas |
| 3 | UGC pakai **All-in-One Reference (Ref2VA)** | referensi gambar produk + orang (bukan frame awal/akhir) → produk tidak berubah bentuk | 🎬 produk benar |
| 4 | Tambah **RH Upscale** → tier "HD 1080p" | 540p→1080p generatif, identitas stabil | 💰 jualan premium |
| 5 | Fitur Kuzushi yang belum ada: **lip sync** (INFINITETALK), face swap, pose transfer, **30 detik** (Seedance 2.5) | fitur pesaing | 🎬 kompetitif |
| 6 | Pasang **kode undangan RH** kita di bot/kanal | +500 koin/orang (maks 5.000/hari); ajukan partner kalau serius | 💰 koin gratis |
| 7 | Kontes & insentif creator (USD 150K / ¥20rb kredit) + publikasi rhTV | pendapatan sampingan | 💰 opsional |

## I. Bukti metrik video (heat-map 12 frame)

| Video | Latar | Wajah | Badan | Durasi | FPS |
|---|---|---|---|---|---|
| job3 (ada balon, prompt user) | 54,91 | 43,73 | **36,27** | 5,2s | 24 |
| nobalon (foto sama di 2 ujung, prompt sama) | 47,27 | 28,23 | 13,36 | 5,2s | 24 |
| Kuzushi (i2v murni) | 38,19 | **42,74** | 26,92 | 10,0s | 30 |

Kesimpulan: **yang bikin video job3 hidup adalah dua gambar ujung yang BERBEDA**, bukan prompt. Dengan foto sama di dua ujung, gerak badan turun 63% (36,3 → 13,4). Solusi benar = workflow **i2v/Ref2VA** (satu gambar masuk, model bebas menganimasi).