# KREE.AI — KARTU PROYEK (STATE)

> **BACA FILE INI PERTAMA** di setiap sesi baru (termasuk setelah `/new`).
> Diperbarui setiap milestone + langsung di-commit/push. Ini yang menjaga konteks antar-sesi.
> Detail panjang: `RUNNINGHUB-ANALISA-LENGKAP.md` · `UPGRADE-UX-3LANGKAH.md` · `AULAA-GO-LIVE.md`.
> ⚠️ TIDAK BOLEH memuat rahasia — hanya LOKASI kredensial.

---

## 1. STATUS SEKARANG (8 Okt 2026, dini hari WIB)

- Bot **KREE.AI** `@kreeaibot` **LIVE** di VPS — `/root/projects/kreaibot`, systemd `kreaibot` (auto-restart), log `/var/log/kreaibot.log`.
- **73/73 selftest lulus**, tombol **Menu Telegram aktif**, `tools/ux_audit.py` bersih.
- **UX 3 langkah** LIVE: pilih fitur → kirim foto → **langsung ketik prompt** (tanpa tombol "Lanjut"); durasi/rasio di-edit di tempat.
- **Perapian prompt video** (LLM + fallback ke prompt asli, saklar `KREAIBOT_REFINE_VIDEO`) — LIVE, tidak pernah ditampilkan ke user.
- **Pembayaran Aulaa QRIS LIVE** (teruji uang nyata), channel `@KreeaCommunity` + gate referral aktif.
- **Backend render = RunningHub WORKFLOW `FL2VA`** (jalur koin). ⚠️ Lambat (276–340s per 5s) **dan mengunci gerakan orang** → ini yang sedang kita ganti.

## 2. TEMUAN KUNCI RUNNINGHUB (ringkas)

- Membership **Personal** aktif s/d **8 Nov 2026**: **36.000 RHCoins/bulan** ($9,9/bln) + $1 wallet. Saldo terakhir **34.993 koin**.
- **Tier koin**: Lite 0,02 · **Standard 0,2** · Plus 0,4 koin/detik → kita Standard. Terukur: 5s i2v = 59–68 koin (≈Rp290) · 15s UGC = 257 koin.
- **Harga model API ($/detik)**: LTX-2.3 i2v $0,01–0,03 · H3 RH Enhanced i2v/multi-ref $0,03–0,06 · Veo3.1-Fast jalur murah · Wan3.0 $0,04–0,14.
- **Runtime Enterprise-Shared**: Lite $0,07/jam · Standard $0,7/jam · Plus $0,9/jam · Ultra $1,35/jam.
  → **Jalur koin membership (±Rp0,88/detik GPU) tetap 3,5× lebih murah** dari shared (Rp3,1/detik) — jalur koin menang **asalkan modelnya cepat**.
- **Perpustakaan workflow** (semua yang kita butuh ada): H3 Image-to-Video, **H3 All-in-One Reference (Ref2VA: referensi gambar + video + audio)**, H3 FL2VA-First/Last, INFINITETALK Digital Human (lip sync), LTX2.5 t2v, ALMIGHTY video continuation, Seedance 2.0 all-in-one.
- **BLOCKER AKTIF**: API model cepat (LTX-2.3, Veo 3.1 Fast, Kling 3.0 Pro, H3 single-frame) menolak key kita → `error 1014: Standard Model API is restricted to Enterprise-Shared API Keys only`.
  Halaman: `/call-api/bill-task?tab=keys&type=shared` → akun **sudah punya 2 key shared** (aksi Copy/Reset/Modify) + "Platform Universal Key" (yang dipakai backend sekarang).
- **Script resmi RH CACAT** (`github.com/HM-RunningHub/OpenClaw_RH_Skills`): fungsi upload hardcode `Bearer ***`; host `.cn` menolak key kita → **pakai `.ai`**. Sudah ditambal di `rh-skills/` (salinan lokal).
- **Program cuan**: invite **500 koin/orang** (maks 5.000 koin/hari; partner promosi tanpa batas) · kontes film AIGC hadiah s/d **USD 150.000** · insentif creator **¥20.000** kredit.

## 3. TEARDOWN KUZUSHIGENBOT (bot pembanding)

- Bot menyatakan sendiri: **"🎬 AI Image to Video (Minimax / LTX 2.3)"**.
- **Harga mereka**: 5s = **0,5T** · 10s = **1T** · 15s = **2T** (kita: 0,5 / **1,5** / **2,5** → kita lebih mahal di 10s & 15s).
- **Flow mereka**: klik Image to Video → kirim 1 foto → "✅ Foto Berhasil Diterima!" → **langsung minta prompt** (tanpa tombol Lanjut) ✓ identik dengan UX kita.
- Menu mereka: Face Swap & Motion 2T · AI Image Editor 0,3T · Pose Transfer 0,5T · Lip Sync 0,5T · Video All-in-One Star Trail H3 1T.
- Saldo uji: **15,9 Token** (user top-up). Uji banding foto+prompt sama → hasil ukur disimpan di sesi.

## 4. METRIK VIDEO (heat-map 12 frame; angka lebih besar = lebih banyak gerakan)

| Video | Latar | Wajah | Badan | Durasi | FPS |
|---|---|---|---|---|---|
| job3 kita (FL2VA + intro balon) | 54,9 | 43,7 | **36,3** | 5,2s | 24 |
| nobalon (foto sama di 2 ujung) | 47,3 | 28,2 | **13,4** | 5,2s | 24 |
| **H3 single-frame via API (uji 9 Okt 00:42)** | 42,4 | 38,2 | **22,1** | 5,2s | 24 (768×1344) |
| Kuzushi (i2v murni) | 38,2 | **42,7** | 26,9 | 10s | 30 |

**KESIMPULAN TERBUKTI (uji H3 single-frame API):** menghilangkan kunci frame-akhir **membebaskan gerakan orang** → wajah 28,2→**38,2** (+35%) · badan 13,4→**22,1** (+65%), mendekati Kuzushi (42,7/26,9) dengan latar lebih hidup.
→ **Fix = workflow i2v SATU gambar** (bukan FL2VA dua ujung).

### ✅ SOLUSI TERKUNCI (9 Okt 00:55) — JALUR KOIN, TANPA WORKFLOW BARU

Uji `empty2` = workflow yang **sama** (FL2VA) tapi **frame-akhir dikosongkan eksplisit**:

| Video | Latar | Wajah | Badan | Biaya |
|---|---|---|---|---|
| FL2VA (foto 2 ujung) | 47,3 | 28,2 | 13,4 | 64 koin (Rp290) |
| **FL2VA frame-akhir KOSONG** | 41,7 | **38,0** | **25,8** | **61 koin (Rp270)** |
| H3 single-frame via API | 42,4 | 38,2 | 22,1 | **$0,385 (Rp6.300)** |
| Kuzushi | 38,2 | **42,7** | 26,9 | — |

**Gerakan badan +93% · wajah +35% DENGAN BIAYA SAMA** → setara Kuzushi, 20× lebih murah dari jalur API.

**Implementasi (SUDAH LIVE):**
1. `backends/runninghub.py` — sentinel **`@empty`**: kirim `fieldValue:""` **eksplisit** (jangan dilewati; melewati node = workflow pakai contoh bawaan → bug balon).
2. `.env` — `RUNNINGHUB_NODES_I2V` node4: `@photo1` → **`@empty`**.
3. `selftest.py` — 2 tes baru (**75/75 lulus**); service direstart.
4. Verifikasi end-to-end lewat backend produksi: `tools/backend_i2v_test.py` (tool baru).
- **JANGAN** kembali ke "foto di dua ujung" untuk i2v — itu yang membekukan gerakan. Untuk UGC (produk berubah bentuk) solusinya workflow Ref2VA, BUKAN dua ujung.
- Jalur API model standar (key SHARED) **mahal** → hanya untuk eksperimen terbatas.

## 5. PERBAIKAN PENTING (9 Okt 01:20–01:30) — sudah LIVE

1. **Bug video hilang setelah restart** — service yang restart kehilangan loop poll, jadi render yang sudah jalan (dan sudah dibayar) tak pernah terkirim. Bukti: **job 5 user (15s, 242 koin) nyangkut**.
   → FIX: `_resume_jobs()`/`_resume_one()` di `bot.py` (dipanggil saat startup) + `db.running_jobs()` + alat manual **`tools/deliver_job.py <job_id>`** (job 5 sudah dikirim pakai ini).
2. **`rh-skills/scripts/runninghub_app.py`: `API_HOST` `.cn` → `.ai`** (host `.cn` tolak key kita: "ApiKey verification failed"). Format argumen `--node` = `nodeId:fieldName=value` (**pakai `=`**, bukan `:` — prompt ber-":" bikin gagal).
3. **`tools/sync_vault.sh`** — sinkron kode server → vault `kode/` + commit/push (JANGAN copy .env/venv/work/db).
4. **`.env`**: `KREAIBOT_JOB_TIMEOUT=3600` (render 20 menit pernah kejadian), `KREAIBOT_REF_INVITER=1.5` (sempat kehapus patch fuzzy — **hati-hati patch .env, pakai Python**).
5. `selftest.py` **78/78**. Commit vault: `165d7c9`.

## 6. CATATAN JALAN PINTAS
- **Jam bebas H3 RH Enhanced (member):** 13 jam/hari gratis (6 AM–7 PM PT ≈ **21:00–10:00 WIB**) — belum diverifikasi apakah berlaku untuk workflow kita.
- **AI App (jalur koin, tanpa key SHARED):** daftar app `--list`, input app `--info <webappId>` (butuh app pernah dijalankan di web). Kandidat LTX2.3 i2v: `2072511984289017857`, `2073941041631293442`, `2074067101232488449`; dipercepat/e-commerce: `2074672423118663682`.

## 4b. UJI API MODEL STANDAR (9 Okt 00:42–00:46) — hasil + batas

- Key **Enterprise-Shared** dibuat & tersimpan `/root/.secrets/runninghub_shared.key` (chmod 600) → `apiType: SHARED`; blokir 1014 hilang ✓
- `minimax/hailuo-h3/image-to-video` (768P, 5s, foto = firstFrameUrl saja): **212 detik · biaya $0,385 (≈Rp6.300) · wallet $1,000 → $0,615**
- ⚠️ **Jalur API model terlalu mahal** (Rp6.300 vs jalur koin Rp290 = 20×) dan cuma 1,5× lebih cepat → **TIDAK dipakai untuk produksi**.
- Kalau butuh kualitas/jalur khusus, pakai API hanya untuk eksperimen terbatas (wallet tipis).
- Endpoint `ltx-2.3/image-to-video` **tidak ada di host `.ai`** (katalog mencantumkan $0,01/s tapi URL panggilan invalid).

**Kesimpulan terkunci**: biang kerok gerakan beku = **jenis workflow (FL2VA)**, bukan prompt. Solusi = **i2v murni / Ref2VA**.

## 5. KEPUTUSAN TERKUNCI (jangan dibuka lagi tanpa temuan baru)

1. Prompt user **dikirim apa adanya** + dirapikan LLM secara aman (tanpa klausa karangan seperti "LIVING BACKGROUND").
2. **Tidak** memakai zoom sintetis / gambar sintetis di workflow.
3. Harga **bertingkat durasi** (`DURATION_COST` / `cost_for`).
4. Jalur **koin RunningHub** = rute produksi termurah; API $ hanya untuk eksperimen/cepat.
5. Webhook Aulaa **tidak diganti** (pakai polling 6s).
6. SSH/UFW/iptables **tidak diubah** tanpa izin eksplisit; SSH tetap port 22.
7. **Tidak menyimpan kredensial** di folder yang di-push ke GitHub (vault / `/root/.secrets/`).
8. Git vault selalu: `git push origin master:main`.

## 6. TUGAS BERIKUTNYA (urutan prioritas)

1. **Key Enterprise-Shared** → uji i2v cepat (LTX-2.3 / Veo 3.1 Fast / H3 single-frame) → ukur waktu, biaya, kualitas vs Kuzushi.
2. **Ganti backend bot** dari FL2VA ke **i2v murni** (+ **Ref2VA** untuk UGC produk) → kualitas + kecepatan.
3. Tambah **RH Upscale** → tier "HD 1080p".
4. Pasang **kode undangan RunningHub** di bot/kanal → koin gratis (500/orang).
5. Fitur susulan: **lip sync** (INFINITETALK), **30 detik** (Seedance 2.5), pose transfer, face swap.

## 7. JANGAN DIULANG (sudah selesai — jangan dikerjakan lagi)

- Analisa seluruh situs RunningHub (SELESAI — baca `RUNNINGHUB-ANALISA-LENGKAP.md`).
- UX 3 langkah, tombol Menu Telegram, fix pesan berulang, perapian prompt (semua LIVE + teruji).
- Uji zoom sintetis & klausa "latar hidup" (SUDAH DIPUTUSKAN: dicabut; bikin warp +45%).
- Teardown alur/menu Kuzushi (SELESAI).

## 8. LOKASI PENTING (tanpa nilai rahasia)

- Kode: `/root/projects/kreaibot` (+ `rh-skills/` = skill resmi RunningHub yang sudah ditambal).
- Dokumen: `/root/Documents/Webuild/03-Proyek/03-Autonomous-AI-Content-Creator/Kreaibot/`.
- Bukti analisa: `…/Kreaibot/bukti/runninghub-analisa-8okt.md` (3.973 baris).
- Kredensial: **Hermes Vault** (login RunningHub/Gmail) + `/root/.secrets/` (chmod 700/600).
- GUI Telegram Desktop (aksi user): `DISPLAY=:99`, window `2097162`, helper OCR `/root/.hermes/cache/scratch/ocr.py`, `td_state.py`.