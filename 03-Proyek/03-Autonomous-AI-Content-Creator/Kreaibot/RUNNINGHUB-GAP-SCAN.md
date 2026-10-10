# RunningHub — SCAN CELAH PASOKAN (riset workflow #2)
> 10 Okt 2026. Sumber: `POST /api/search/workflow` (param `search`, field hasil = **`id`**, bukan `workflowId`).
> Angka = jumlah workflow yang cocok. Skrip: `tools/rh_gap_scan_cn.py`, `tools/rh_gap_scan.py`, `work/rh_gap_probe.py`.

## 1. Hasil (CN vs EN)

| Niche | CN | EN | Baca |
|---|---|---|---|
| 一寸照片 (pas foto 1 inci) | **0** | 0 | 🔥 celah nyata |
| 建筑表现 (render arsitektur) | **0** | 0 | 🔥 |
| 简历 / cv / resume | **1** | 0 | 🔥 |
| 菜单 / menu design | **3** | 0 | 🔥 |
| 模特换人 (model swap) | **5** | — | 🔥 |
| 户型图 / floor plan | **9** | 0 | 🔥 |
| PPT | 21 | — | ⚪ |
| 美食 / food photo | 30 | 0 | ⚪ |
| 婚纱 / wedding | 44 | — | ⚪ |
| 海报生成 | 57 | — | 🟡 |
| 贴纸 | 58 | — | 🟡 |
| logo | 84 | 84 | 🟡 |
| 商品图 / product shot | 133 | 1 | 🟡 |
| 证件照 / ID photo | 178 | 5 | 🟡 (supply ada, demand tinggi) |
| 头像 | 207 | — | 🟡 |
| 老照片修复 | 259 | 3 | 🟡 |
| 抠图 / background remove | 469 | 6 | ❌ rame |
| 海报 | 526 | 9 | ❌ rame |
| 写真 / portrait | 681 | 217 | ❌ rame |
| 去水印 / watermark | 728 | 55 | ❌ rame |
| 服装 | 1154 | — | ❌ rame |
| 换脸 / face swap | 1407 | 36 | ❌ rame |
| 换装 / outfit | 1484 | — | ❌ rame |
| 修复 / repair | 1829 | — | ❌ rame |
| **一致性 (character consistency)** | **2121** | 20 | ❌❌ SANGAT rame |
| 电商 / ecommerce | 2223 | — | ❌ rame |
| 放大 / upscale | 4044 | 11625 | ❌❌❌ jenuh |

**Kesimpulan penting:** workflow #1 kita (`Konsistensi Karakter`) berada di lane **paling rame (2121)** →
wajar kalau run-nya tidak meledak. Ini aset starter, bukan jackpot. (Sudah dikoreksi sejak awal.)

## 2. Kelayakan teknis (bukti dari workflow publik RH)

`work/rh_gap_probe.py` menarik 4 workflow publik per niche dan membaca node + file model yang dipakai:

| Niche | Node pack yang dipakai | Model yang terbukti ADA di RH |
|---|---|---|
| 抠图 (matting) | `RMBG`, `RembgByBiRefNet`, `LayerMask: SegmentAnythingUltra V2` | `Matting.safetensors`, `SDMatte_plus.pth` |
| 证件照 (ID photo) | **`HivisionLayOutNode`**, `AddBackgroundNode`, `LaterProcessNode`, `ImageScaleToTotalPixels` | `Qwen-Image-Edit-2509_fp8`, `Qwen-Image-Edit-Lightning-8steps`, `seedvr2_ema_3b` (restore wajah) |
| 菜单 (menu) | `ttN text`, `PrimitiveNode`, `StringReplace`, `Text`, `CLIPLoader` | `boogu_image_turbo_bf16`, `qwen3vl_8b_fp8` |
| 商品图 | `VAEEncode`, `KSampler`, controlnet | `FireRed-Image-Edit-1.1`, `Qwen-Image-Lightning-8steps-V2`, `RealESRGAN_x2`, `control_v11p_sd15_lineart` |
| 模特换人 | WanVideo + `FireRed-Image-Edit` | `FastWan_T2V_14B`, `Qwen-Image-Lightning-4steps-V2` |

→ Niche yang "kosong" **bukan karena tidak bisa dibuat** — model & node pack-nya sudah ada di server RH.

## 3. Batasan yang menentukan bentuk app (temuan dari publish #1)
- RunningHub **hanya bisa expose widget node STANDAR** sebagai input user. Widget node custom
  (`Easy_QwenEdit2509.prompt`, `HivisionLayOutNode.*`) **tidak muncul** di langkah "tambah node input".
- Konsekuensi: app yang digerakkan node custom = **one-click** (parameter di-bake).
  App yang mau punya **input teks bebas** harus dibangun dari node standar (`CLIPTextEncode`,
  `PrimitiveNode`, `Text`).
- **Tag WAJIB** saat publish; taksonomi ada di `RUNNINGHUB-TAGS.md`.

## 4. Kandidat workflow #2

| # | Kandidat | Celah | Input user | Catatan |
|---|---|---|---|---|
| A | **Pembuat menu/poster UMKM** (`菜单`/`海报生成`) | 3 / 57 | ✅ teks bebas (node standar) | Nyambung ke klien UMKM user; app bisa dipakai berulang (promo baru tiap minggu) |
| B | **Pas foto ID 1-inci multi-ukuran** (`一寸照片`, generik 178) | 0 untuk ukuran spesifik | ❌ one-click (pack Hivision) | Permintaan massal & berulang; butuh diferensiasi karena generik sudah 178 |
| C | **Restorasi + pewarnaan foto lama** (`老照片修复`) | 259 | ❌ one-click | Daya tarik emosional tinggi, tapi `修复` sudah 1829 |

## 5. Rekomendasi
**A dulu** — satu-satunya kandidat yang memberi user **kontrol teks**, celahnya paling lebar,
dan langsung nyambung ke bisnis user (UMKM). B & C menyusul sebagai app kedua/ketiga.