# AUDIT MESIN KREEAMOTION — TANGGAL 17 OKT 2026 (+ penyelarasan ke kondisi sekarang)

Perintah user: *"audit mesin kreeaimotion bot harus pakai semua mesin yang dipakai tanggal 17"*.
Audit ini **0 koin** (hanya membaca log/DB/kode/config).

## Metode & bukti

| Sumber | Isi |
|---|---|
| `/var/log/kreeaimotion.log` | 154 baris tanggal 2026-10-17 |
| `kreeaimotion.sqlite3` → tabel `jobs` | job 60–66 (17 Okt), kolom `feature`+`model`+`task_id`+`cost` |
| `.env.bak-20261018-1609` | konfigurasi mesin **sebelum** perubahan asisten 18 Okt (≈ keadaan 17 Okt) |
| Kode | default mesin: `tools/cosplay.py:67-69`, `tools/imagedit.py`, `tools/imagegen.py` |
| `git log --since=2026-10-18` | daftar perubahan asisten yang menyimpang dari 17 Okt |

Job 17 Okt dari DB: **60 cosplay failed · 61 cosplay failed · 62/63/64 cosplay done · 65 image done ·
66 motion done (task `2111413087620321282`)** — total 7 job.

## A. Mesin GATEWAY (Inferhub) — sesuai keadaan 17 Okt

| Peran | Nilai 17 Okt (kode/default) | Dipakai oleh | Status sekarang |
|---|---|---|---|
| Generate Gambar | `MOTIONBOT_IMAGE_MODEL=gpt-image-2` | fitur 🖼 Generate Gambar (`image`) | **utuh** ✓ (tidak pernah asisten ubah) |
| Cadangan gambar | `MOTIONBOT_IMAGE_FALLBACK=gemini-3.0-pro-image` | idem | **DIUBAH asisten 18 Okt** ✗ |
| Ganti Baju / cosplay (utama) | `MOTIONBOT_OUTFIT_MODEL=gpt-image-2` + default kode `MESIN_UTAMA=gemini-3.0-pro-image` | fitur 🎭 Cosplay (`cosplay`), 👗 Ganti Baju (`outfit`) | **DIUBAH asisten 18 Okt** ✗ |
| Cadangan cosplay | default kode `MESIN_KEDUA=gpt-image-2` | idem | **DIUBAH asisten 18 Okt** ✗ |
| Langkah "mata" (baca acuan → teks) | `MOTIONBOT_COSPLAY_EYES` (default kode kini `ag/gemini-3.8-flash-high`) | jalur kuncian identitas cosplay | diperbaiki 18 Okt (bentuk tanpa prefix `gemini-3.8-flash` **404** ✗) — **dipertahankan bentuk prefix** ✓ |
| Mesin teks/LLM | `MOTIONBOT_LLM_MODELS=cerdas,ih/ali/qwen3.8-flash,ih/cb/gpt-5.6-luna,ih/ali/qwen3.8-max` | deskripsi otomatis, prompt | utuh ✓ |
| Ukuran keluaran | `MOTIONBOT_IMAGE_SIZE=2160x3840`, `MOTIONBOT_OUTFIT_SIZE=2160x3840` | gambar & baju | utuh ✓ |
| Anggaran | `MOTIONBOT_OUTFIT_BUDGET=260`, `MOTIONBOT_OUTFIT_ORDER=auto` | pengaman biaya | utuh ✓ |

## B. App / workflow RunningHub — dipakai 17 Okt, semua harus tetap tersedia

| Peran | ID | Slot/peta | Dipakai oleh | Status |
|---|---|---|---|---|
| Motion (Wan Animate) — dipakai semua tier | `2083697864529678338` | `299:image`+`275:video` | 🎬 Motion FAST/HD/FULL/PRO | ✓ ada (`MOTIONBOT_*_APP`) |
| Workflow tier FAST/HD/FULL | `2042526099766251522` | `265:value`+`316:value`+`317:value` | pengaturan tier motion | ✓ ada |
| Workflow tier PRO | `2074049787567292416` | idem | tier PRO | ✓ ada |
| Ganti Baju (cadangan RH) | `2075460030073237505` (FireRed) | `207:image=orang`+`208:image=acuan` (tanpa slot prompt) | `MOTIONBOT_OUTFIT_RH_APP` | ✓ ada — **wajib diberi peringatan bila terpakai** ✓ |
| Generate Video (Hailuo H3) | `2087081647066263554` | `114:image`+`143:text`+`136:value=10` | 🎬 Generate Video | ✓ ada |
| App ganti-baju lama (3 gambar + teks) | `2095689306085285890` (+ `2095689306009788418`) | `20/21/41:image`, `113:text` | jalur cadangan di `tools/imagegen.py` | ✓ ada di kode |
| App gambar lama | `2003539764081008641` | — | `tools/imagegen.py` | ✓ ada di kode |
| Minimax (i2v / ref2v) | `2095423555109744641` / `2085900381959593985` | — | jalur video alternatif | ✓ ada di kode |
| Upscale/HD | `2000516602854600705` (+ SeedVR2) | — | perbesar gambar | ✓ ada di kode |

## C. Penyimpangan yang dibuat asisten pada 18 Okt (dan dibalik di audit ini)

| Commit | Perubahan | Tindakan audit |
|---|---|---|
| `806ed8f` | `MOTIONBOT_COSPLAY_ENGINE/ENGINE2`, `OUTFIT_MODEL`, `IMAGE_FALLBACK` → `cb/gemini-2.5-flash-image`, `gemini-2.5-flash-image` | **dibatalkan** ✗ |
| `62cdcb0` | diganti lagi → `cb/gemini-3.0-pro-image`, `cb/gemini-3.1-flash-image` | **dibatalkan** ✗ |
| `bf8bff7` | kuncian identitas per-karakter + `MESIN_MATA=ag/gemini-3.8-flash-high` + peringatan cadangan tanpa slot prompt | **dipertahankan** ✓ (perbaikan produk yang disetujui user: "gas") |

## D. Penyelarasan yang dijalankan audit ini

1. `MOTIONBOT_OUTFIT_MODEL` → **`gpt-image-2`** (nilai 17 Okt) ✓
2. `MOTIONBOT_IMAGE_FALLBACK` → **`gemini-3.0-pro-image`** (nilai 17 Okt) ✓
3. Baris `MOTIONBOT_COSPLAY_ENGINE` / `MOTIONBOT_COSPLAY_ENGINE2` yang asisten tambahkan → **dihapus** ✓
   → jalur cosplay kembali memakai default kode 17 Okt: **`gemini-3.0-pro-image`** (utama) +
   **`gpt-image-2`** (cadangan) ✓ — jadi **semua mesin 17 Okt terpakai lagi** ✓
4. `MOTIONBOT_COSPLAY_EYES` dibiarkan default `ag/gemini-3.8-flash-high` ✓ (bentuk prefix — versi 17 Okt
   tanpa prefix pasti 404 dan mematikan kuncian identitas; ini memperbaiki, bukan mengganti mesin) ✓
5. Cadangan `.env.bak-<tanggal>` dibuat sebelum menyentuh berkas ✓

## E. Fakta penting (bukan opini)

- **Rute gambar gateway masih outage saat audit** ✗ — semua id gambar (`gpt-image-2`, `gemini-3.0-pro-image`,
  `cb/...`) menjawab `404 unknown model` walau payload lengkap & token sehat (diuji 18 Okt berkali-kali).
  Selama outage ini, job gambar/cosplay **otomatis jatuh ke cadangan RunningHub** ✓ (FireRed — tanpa slot
  prompt ✗) atau ke app berslot prompt bila dipanggil manual.
- Karena itu "memakai semua mesin tanggal 17" tetap dilakukan di level konfigurasi ✓ — mesin RH 17 Okt semua
  aktif ✓ — dan jalur gateway akan langsung terpakai begitu rute provider pulih ✓.
- Mesin pendukung yang **terbukti** untuk keadaan darurat (18 Okt): app `2067570858536824834`
  (Qwen-Edit 一键换装, 1 gambar + 1 prompt, 100%) dan upscaler `2067925388738777089` ("8k放大（无损）",
  `15:scale_by`), app de-AI `2075249793378639873` (1 slot gambar).