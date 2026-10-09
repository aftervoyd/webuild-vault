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

### ✅ FITUR BARU LIVE: AI Image Editor (9 Okt 09:49)
- **Fitur ke-4 di katalog** (`SIAP_JUAL` = ugc, allinone, i2v, **editor**) · harga **0,3 Token**.
- **Jalur AI APP** (bukan workflow): `RUNNINGHUB_APP_EDITOR=2061699451919618049` (All-in-One Image V2 I2I, low-cost channel).
- **Binding:** node `2.image` ← `@photo1` · node `1.prompt` ← `@prompt` · node `1.resolution` = `1k` · node `1.aspectRatio` ← `@ratio`.
  ⚠️ **Wajib pakai `resolution 1k` + `aspectRatio`.** `aspectRatio` sendirian (tanpa resolution) → task **FAILED**.
  ⚠️ App ini **kadang flaky** (~1 gagal dari 4 percobaan) — bot sudah punya refund otomatis untuk kasus gagal.
- **Hasil: GAMBAR PNG** 768×1376 (9:16) · **±31 detik** · tanpa zip.
- **Delivery gambar:** helper baru `send_result()` di `bot.py` — ekstensi gambar (`.png/.jpg/.jpeg/.webp`) → `send_photo`, selain itu → `send_video` (dipakai 2 tempat: worker + `_resume_one`).
- Alat uji: **`tools/backend_editor_test.py`** (+ `ref1.jpg`).
- **App editor lain yang JALAN tapi hasilnya ZIP (jangan dipakai):** 2029825493565968385 (91s) · 2057860352582438914 (91s) · 2062724963311898626 (51s) · 2049488928721346561 (72s). App 2037019022239211522 & 2049465637889646594 → FAILED.
- **`tools/rh_app.py --list` sekarang TIDAK mengunduh cover** (dulu mengisi `/tmp` tmpfs 851 MB sampai penuh) — cover hanya kalau `RH_COVERS=1`.

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

## 3. TEARDOWN KUZUSHIGENBOT (bot pembanding) — DIPERBARUI 9 Okt 2026, pukul 09:20 WIB

> Detail lengkap: **`TEARDOWN-KUZUSHI-9OKT.md`** (menu, alur 6 fitur, top up, referral, perbandingan harga, rencana implementasi).

- **Menu (1 pesan, harga tampil di tombol):** 🎭 Face Swap & Motion **2T** · 🎬 Image to Video **0,5–2T** · 🖌️ AI Image Editor **0,3T** · 🕺 Pose Transfer **0,5T** · 🎤 Lip Sync **0,5T** · 🌌 Video All-in-One Star Trail H3 (30s) **1T** · Top Up QRIS · Referral · Profil · Voucher · Panduan.
- **Daftar harga resmi mereka:** i2v **5s=0,5 · 10s=1 · 15/30s=2** · Face Swap 2 · Image Editor 0,3 · Pose 0,5 · Lip Sync 0,5 · All-in-One H3 1.
- **Token mereka ≈ Rp 667** (paket Rp10.000 = 15 Token). **Token kita Rp 1.000** → kita 1,5× lebih mahal.
- **Kesenjangan besar:** All-in-One **30s = Rp667** vs All-in-One 15s kita **Rp2.500** (3,7× lebih mahal). Kita juga **tidak jual i2v 15s & 30s**.
- **Sudah punya social proof** di menu: "Total Komunitas: 2.781 Member" + Profil "Total Render Bot: 2732" + Referral "Penukaran Terakhir: @wahyu_hidayat menukarkan 50 Token".
- **Referral mereka = komisi RUPIAH per top up** (Rp5rb→2T · 10rb→3T · 25rb→5T · 50rb→15T · 100rb→20T), link `?start=ref_<uid>`.
- **Alur fitur (terverifikasi):** Image Editor = foto → prompt → render. Pose = foto subjek → foto referensi pose. Lip Sync = foto wajah → file audio (.mp3/voice note). All-in-One = 1–6 foto (tombol "✅ Lanjut Ketik Prompt") → prompt. Face Swap = foto wajah → video .mp4 (disarankan 15s, maks 30s).
- **Pelajaran UX:** mereka menaruh **pilihan durasi + harganya di pesan pembuka** dan **harga di label tombol menu** — user tahu biaya sebelum klik.
- Saldo uji setelah eksplorasi: **12,6 Token**.

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

## 7. 🏆 JALUR AI APP — PILIHAN PRODUKSI (uji 9 Okt 01:34–01:57)

**Aturan main (WAJIB):** `--api-key <key platform>` (supaya dibayar **KOIN**) + `--upload-key <key SHARED>` (**upload DITOLAK key platform**, "ApiKey verification failed"). Format node: `nodeId:fieldName=value` (pakai `=`, bukan `:`).

| App (webappId) | Node | Waktu | Koin | Wajah | Badan | Putusan |
|---|---|---|---|---|---|---|
| **Wan2.2 2075128386959265793** | 292 image · 293 text · 336 durasi · 339 width | 305s | 61 | **39,2** | 22,3 | ✅ **DIPAKAI (i2v)** — 720×1280, wajah ≈ Kuzushi (42,7) |
| LTX2.3 2072511984289017857 | 7 image · 4 text | **165s** | **33** | 24,6 | 24,6 | ⏳ kandidat **tier "Hemat"** (nyaris statis + artefak ekor) |
| bernini 2074672423118663682 | 30 image · 56 text | 476s | 96 | — | — | ❌ mahal & lambat |
| workflow FL2VA (@empty) | 6 foto · 4 kosong | 324s | 61 | 31,7 | 19,0 | fallback (allinone/ugc) |

**Aktif sekarang:** `.env` → `RUNNINGHUB_APP_I2V=2075128386959265793` + `RUNNINGHUB_APP_NODES_I2V` (292 image @photo1 · 293 text @prompt · 336 value @duration) ✓
**Cara daftar app:** `rh-skills/scripts/runninghub_app.py --list --sort HOTTEST --size 30` · input: `--info <webappId>` (app harus pernah dijalankan di web dulu).
**Backend:** `backends/runninghub.py` branch `RUNNINGHUB_APP_<FEATURE>` → `POST /task/openapi/ai-app/run` (webappId + nodeInfoList) ✓ selftest 80/80.
**Terbuka:** durasi 10/15s di app belum terbukti (default 5s) — jangan jual durasi yang belum bisa dipenuhi.

### VERIFIKASI LANJUT (9 Okt 02:04–02:15)
- ✅ **5s lewat backend produksi** (jalur app): 263s · 720×1280 · wajah 37,4 · badan 23,4 (koin 61)
- ✅ **10s TERBUKTI BISA**: hasil **10,06s** · 720×1280 · 566s · **112 koin** (≈Rp500) — binding node336 @duration dihormati app ✓
- ⏳ 15s belum diuji (estimasi ~160 koin ≈ Rp715)
- **UGC (produk berubah bentuk):** belum ada app Ref2VA di katalog → rencana **2 tahap**: app image-edit (gabung foto orang + foto produk → 1 gambar) → lalu i2v Wan2.2 ✓ (bukan dua-ujung workflow)
- **Ekonomi terukur:** 1 koin ≈ Rp4,46 · 5s=61 koin (Rp272) · 10s=112 koin (Rp500) → harga jual sekarang 0,5T/1,5T (Rp500/1.500) = margin ~45-65% ✓; **Kuzushi 10s=1T** → kita masih lebih mahal di 10s

### ❌ 15s i2v GAGAL & HARGA FINAL (9 Okt 03:17–03:30)
- **App Wan2.2 GAGAL di 15s** (status FAILED, 384s, **0 koin** — RunningHub tak menagih task gagal) → **i2v 15s DIMATIKAN** dari katalog (aturan: jangan jual durasi yang belum terbukti). allinone & UGC 15s TETAP (jalur workflow, terbukti 269 koin).
- **HARGA FINAL i2v: 5s = 0,5T · 10s = 1T** (paritas Kuzushi; margin terukur 46% & 50%). User tak menjawab pertanyaan harga dalam 1 jam → keputusan diambil otomatis (kontrol penuh sudah diberikan).
- `selftest` 79/79 · `ux_audit` bersih · commit `7ea264a`.

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

## 6c. AKAR MASALAH "SLOW MOTION + TANPA SUARA" (9 Okt 10:15)

**Diagnosa (bukti ffprobe, bukan dugaan):** hasil bot kita = **16 fps, tanpa trek audio**.
Jalur lama (FL2VA) keluar 24 fps; app Wan2.2 (jalur koin yang dipakai sekarang) turun ke **16 fps**
→ di layar 60 Hz terlihat patah-patah / seperti gerak lambat. Model Wan2.2 memang **tidak** menghasilkan audio.

**Kenapa Kuzushi lebih cepat:** mereka pakai **LTX 2.3** (menu bot-nya sendiri menulis "Minimax / LTX 2.3").
LTX-2.3 di katalog RunningHub **$0,01/detik**, "generates matching ambient sound effects … in a single pass",
5–20 s, native 9:16. Model kita (Wan2.2) jauh lebih berat + antrean "low-cost channel".

**PERBAIKAN TERPASANG (gratis, LIVE 10:23):** `backends/mediafix.py` → `smooth_fps()`
interpolasi `minterpolate` 16 fps → **30 fps** TANPA mengubah durasi/kecepatan gerak.
Saklar `KREAIBOT_FPS=30` di `.env` (isi 0 = mati). Biaya: **±1 mnt 55 s per video 10 s** (VPS 2 core).
Dipakai di 2 titik pengiriman (`worker` + `_resume_one`). Hasil editor (PNG) otomatis dilewati.

**OPSI PREMIUM (teruji, BELUM dipakai):** `alibaba/wan-2.6/image-to-video-flash` lewat API model
→ **30 fps + audio AAC 44,1 kHz stereo**, durasi 2–15 s, 720p/1080p, `enableAudio=true` (default).
Ukur: **5 s = 42 detik** (±6× lebih cepat dari app koin 263 s) tapi **$0,20 ≈ Rp3.240** (vs 61 koin ≈ Rp272).
Di harga jual sekarang (5 s = Rp500) → **RUGI**. Layak hanya sebagai tier premium / harga 15 s dinaikkan.

**Endpoint LTX-2.3 SUDAH KETEMU (9 Okt 10:45):** nama aslinya **`rhart-video/ltx-2.3/image-to-video`**
(bukan `ltx-2.3/image-to-video`) — didapat dari `POST /api/sku/detail?id=2034461796984971265` (`rhEndpoint`).
Harga **$0,01/detik**, ada audio ambient, 9:16 native, 5–20 s. **TAPI submit diblokir `errorCode 605
"balance insufficient"`** walau saldo $0,28 (5 s cuma $0,05) → perlu top up dulu (saran $5–10).
Rincian lengkap + daftar harga model lain: **`API-MODEL-RUNNINGHUB-9OKT.md`**.
Catatan: `wan-2.6-image-to-video-flash` versi id pendek **$0,02/s** (separuh dari slug `alibaba/` yang gue tes).

## 6d. GANTI MESIN i2v → LTX-2.3 JALUR KOIN (9 Okt 11:00) — INI JAWABAN "CELAH KUZUSHI"

**Temuan kunci:** RunningHub punya DUA jalur bayar (halaman `vip-rights`):
- **Plan A = RHCoins** → "for AI apps, workflows, and **open-source models** (Qwen, Wan, **Ltx**)"
- Plan B = dompet USD → model **tertutup** (Kling, Sora, NanoBanana)

Akun kita = **Personal, $89,9/tahun → 36.000 RHCoins + $1 per bulan** (koin kedaluwarsa tiap bulan).
**1 RHCoin ≈ $0,00021 ≈ Rp3,4.** Jadi jalur koin itu **4–8× lebih murah** dari Model API dolar
(LTX API $0,01/s = Rp810/5s, sedangkan app koin cuma ±45 koin = Rp152/5s). **Inilah cara Kuzushi jual murah.**

**App baru terpasang:** `RUNNINGHUB_APP_I2V=2065707741691334658`
("Ltx2.3图生视频带声音（极速）zip" = LTX 2.3 i2v + suara, jalur koin)
Bindings: `345.image ← @photo1` · `304.text ← @prompt` · `301.value ← @frames`
(`@frames` = durasi × 24 fps — token baru di `_bind()`).

| | Wan2.2 app (lama) | **LTX-2.3 app (baru)** |
|---|---|---|
| fps | 16 | **24** |
| audio | ❌ | **✅ AAC 48 kHz stereo** |
| ukuran | 720×1280 | **768×1280** |
| 5 s: waktu / koin | 263 s / 61 | **243 s / 45** |
| 10 s: waktu / koin | 566 s / 112 | **343 s / 68** |
| 10 s: harga koin (Rp) | ±Rp378 | **±Rp229** |

→ Lebih murah, lebih cepat, fps benar, **ada suara**. Itu sekaligus mematikan masalah "slow motion + tanpa suara".

**Perbaikan teknis pendukung (LIVE, selftest 79/79):**
- `backends/mediafix.py`: `unwrap_media()` — hasil app kadang **ZIP**, otomatis diekstrak (terbukti di app ini).
- **Upload API BARU:** `POST /openapi/v2/media/upload/binary` (field `file` + header Bearer).
  Endpoint lama `/task/openapi/upload` mulai ditolak ("ApiKey verification failed") → sudah dipasang sebagai pilihan pertama.
- `KREAIBOT_FPS=24` (interpolasi hanya jalan kalau hasil < 24 fps, jadi jalur LTX tidak kena biaya ekstra).

**Belum dites:** durasi 15 s / 20 s (frame 360/480) — API LTX mendukung 5–20 s.

### 6d-2. DURASI PANJANG: 15 s & 30 s TERBUKTI (9 Okt 11:20–12:00)

App LTX-2.3 jalur koin ternyata **sanggup sampai 30 detik dalam satu render**
(dugaan awal cuma 20 s dari dokumentasi API — ComfyUI app-nya lebih longgar).

| Durasi | Frame (×24) | Koin | Biaya (Rp) | Waktu render |
|---|---|---|---|---|
| 5 s | 120 | 45 | ±Rp153 | 243 s (4 m) |
| 10 s | 240 | 68 | ±Rp231 | 343 s (5,7 m) |
| 15 s | 360 | 89 | ±Rp303 | 465 s (7,8 m) |
| **30 s** | **720** | **135** | **±Rp459** | **688 s (11,5 m)** |

Semua keluar **768×1280, 24 fps, ada audio AAC 48 kHz** — identik kualitasnya.

**Fitur baru LIVE: 🎥 Video 30 Detik** (`key="long"`, 1 Token = Rp1.000, margin 54%).
Katalog sekarang: `ugc` (15 s) · `allinone` (5/15 s) · `i2v` (**5/10/15 s**) · `long` (**30 s**) · `editor`.
Semua fitur video = maksimal 15 s + satu fitur khusus 30 s, sesuai permintaan.

**Catatan aset:** `RUNNINGHUB_APP_LONG` + `RUNNINGHUB_APP_NODES_LONG` = app LTX yang sama (bindings sama, `@frames` → 720).
`instanceType: plus` (GPU 48G) sudah didukung backend via `RUNNINGHUB_INSTANCE_TYPE` — belum diuji kecepatannya.

**Margin terukur (koin ≈ Rp3,4):** i2v 5s 69% · 10s 77% · 15s 80% · 30s 54%.

### 6d-3. FITUR BARU LIVE: 🎭 Face Swap Karakter (9 Okt 12:20)

**App:** `1889155568379092993` — "极速换脸（最强光影适配）" (super cepat, adaptasi cahaya terbaik), jalur koin.
Labels node dari `/api/webapp/detail`: **163 = 脸型/Face shape** (foto wajah) · **145 = 模特/Model** (foto target).
Metadata app: success rate 100 %, rata-rata render 38 s.

**Uji produksi nyata:** 2 foto (wajah + sheet model) → **PNG, 52 detik, hanya 10 koin (≈Rp34)**.
→ Dijual **0,5 Token (Rp500)** = **margin ±93 %**, jauh di bawah harga Kuzushi (2T ≈ Rp1.334).

Katalog sekarang (6 fitur jual): `ugc` 15s · `allinone` 5/15s · `i2v` 5/10/15s · `long` 30s · `faceswap` · `editor`.
Aset: `RUNNINGHUB_APP_FACESWAP` + `RUNNINGHUB_APP_NODES_FACESWAP`. Uji: `tools/backend_faceswap_test.py`.

**Catatan penting:** face swap kita = **hasil GAMBAR** (bukan video). Kuzushi menjual "Face Swap & Motion" (video).
Kalau mau versi video: rangkai face swap → i2v (atau cari app "视频换脸" yang menerima input video).

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