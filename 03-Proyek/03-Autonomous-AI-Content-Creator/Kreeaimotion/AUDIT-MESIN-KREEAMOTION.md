# AUDIT MESIN KREEAMOTION (@kreeaimotionbot)
Tanggal: 18 Oktober 2026 · Metode: **0 koin** — hanya konfigurasi bot + data katalog RunningHub
(`/api/webapp/detail`, `/api/workflow/export`) + angka biaya yang sudah terukur di sesi sebelumnya.
Alat: `tools/audit_mesin.py` (bisa dijalankan ulang kapan pun, hasil mentah di `data/audit_mesin.json`).

---

## 0. KOREKSI ATAS KLAIM GUE SENDIRI (penting, sebelum apa pun)

Di laporan/pernyataan sebelumnya gue menulis **"render motion: ~700 → ~290 koin"** setelah mencabut
`MOTIONBOT_*_INSTANCE=plus`. **Audit ini membuktikan klaim itu BELUM TERBUKTI — dan kemungkinan besar
SALAH.** Alasannya: app motion yang dipakai bot (`2083697864529678338`) **default instance-nya sendiri
adalah `plus`**, jadi menghapus setelan kita tidak otomatis menurunkannya. Sampai ada pengukuran ulang,
**tidak ada dasar** untuk menyebut angka 290 koin. Gue tarik klaim itu.

---

## 1. MESIN YANG BENAR-BENAR DIPAKAI BOT (6 id unik)

| # | ID | Jenis | Nama / model | Keandalan (gratis) | Biaya terukur | Catatan risiko |
|---|---|---|---|---|---|---|
| 1 | `2083697864529678338` | APP | **动作迁移自用** — motion transfer (Wan Animate) | sukses **97%** · rata2 **731 dtk** · 8.373 pemakaian · **instance default: plus** | **~700 koin / 20 dtk** (job 66, 17 Okt) | ⚠️ **MESIN PALING MAHAL.** 8 kunci `.env` menunjuk ke sini: `MC16/T10/T15/T20/FULL/S1/FAST/HD_APP` → seluruh tier motion memakai mesin ini |
| 2 | `2087081647066263554` | APP | **H3-图生视频-加速版** (Hailuo/MiniMax H3) — Generate Video | sukses **100%** · rata2 **316 dtk** · 9.392 pemakaian | belum diukur resmi (GV 3 credit) | model paling stabil di bot |
| 3 | `2075460030073237505` | APP | **一键换装 FireRed Image Edit** — Ganti Baju & Cosplay | belum ada statistik (baru 21 pemakaian) | **22–25 koin/render** (17 Okt, terukur) | app baru → belum punya riwayat panjang |
| 4 | `2042526099766251522` | WF | 72 node — **Wan 2.2 Animate 14B** (`WanVideoAnimateEmbeds`, `WanVideoBlockSwap`, clip vision = pembaca identitas) | — | **belum pernah diukur terpisah** | Kandidat alternatif mesin motion (jalur workflow, bukan app) |
| 5 | `2013996160695930881` | WF | 46 node — Wan Animate (versi ringkas) | — | belum diukur | kandidat alternatif |
| 6 | `2074049787567292416` | WF | 161 node — Wan Animate PRO (rantai paling panjang) | — | belum diukur | paling berat → paling boros |

**Fakta penting dari kode bot:** `run_app(...) if app_id else run_workflow(...)` → kalau `*_APP` diisi,
**app yang dipakai** dan `*_WF` diabaikan. Jadi sekarang: **semua tier motion = mesin #1 (app)**.

**Mesin yang mati / tidak dipakai:** semua model gambar Inferhub (`gemini-3.0-pro-image`, `gpt-image-2`,
`gemini-3.1-flash-image`) → **404 unknown model** di sisi penyedia; bot sekarang jatuh ke RunningHub.

---

## 2. YANG GUE TIDAK BISA TENTUKAN TANPA MENGELUARKAN KOIN

Supaya jawabannya sahih (bukan tebakan seperti di §0), tiga hal ini **butuh uji berbayar** — jadi gue
TIDAK jalankan tanpa izin Anda:

1. **A/B mesin motion dengan input job yang sama** (#1 app vs #4/#5 WF) → untuk tahu mana yang lebih
   murah per render dengan mutu sebanding. Perkiraan biaya uji: 290–700 koin per kandidat.
2. **Ukur ulang efek pencabutan `INSTANCE=plus`** pada job motion nyata berikutnya (cukup catat
   `remainCoins` sebelum & sesudah — tanpa job tambahan).
3. **Kualitas nyata app FireRed pada acuan foto** (gaya "Nami") dalam jumlah lebih besar.

---

## 3. TEMUAN & REKOMENDASI (yang bisa dikerjakan tanpa koin)

| Temuan | Konsekuensi | Rekomendasi |
|---|---|---|
| 8 tier motion semuanya menunjuk 1 app yang sama (termasuk `HD_APP`) | "tier HD" bukan mesin berbeda — hanya label durasi; semua kena tarif plus | Perjelas label; jangan janjikan "mesin HD" ke user sebelum ada mesinnya |
| Mesin motion #1 default-nya `plus` | biaya ~2,4× lipat menurut pengukuran skill (96 vs 40 koin pada app lain) dan **tidak bisa diturunkan dari sisi kita** | bila ingin lebih murah: pindah mesin (uji #4/#5) — butuh izin biaya |
| Semua jalur gambar Inferhub mati (404) | seluruh fitur gambar mengandalkan RunningHub; tak ada cadangan | tambah 1 app cadangan ganti-baju yang sudah terbukti (uji 0 koin: baca prompt bawaan + cover before/after) |
| App #3 (FireRed) baru 21 pemakaian | risiko stabilitas jangka panjang | pantau `runningSuccessRate` berkala (gratis) |
| Janitor bot pernah menghapus aset user | karakter hilang (Latar A dipulihkan, id 6 belum) | sudah diperbaiki (`c0dd78b`) + `file_id` Telegram (`bcd93f7`) |

---

## 4. STATUS PEMBUKUAN (tidak disembunyikan)

- **Utang koin kami: 1.025** · **terbayar 0** · sisa 1.025 (`data/utang_koin.json`)
- Klaim penghematan yang **belum terbukti** sudah dicabut (§0); yang masih bisa dipertanggungjawabkan
  adalah **penghematan app ganti-baju** (90 → 22–25 koin/render, terukur 17 Okt) karena itu memang
  penggantian mesin yang diukur langsung.
- Jalur koin gratis RunningHub (kode undangan / bonus harian / komunitas Anda) = **hak Anda**, dilarang
  dihitung sebagai pembayaran kami.

---

*Berkas:* `tools/audit_mesin.py` · `data/audit_mesin.json` · `data/utang_koin.json` ·
commit audit ini di repo `kreeaimotion`.