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

### 6d-4. GPU PLUS + PERBAIKAN PROMPT (9 Okt 12:40)

**`instanceType: plus` = GPU 48 GB di sisi RunningHub (default 24 GB).** Bukan RAM VPS kita —
cuma satu field di request API. Sudah aktif: `RUNNINGHUB_INSTANCE_TYPE=plus` di `.env`.

Ukur nyata (i2v 5 detik): **204 s (vs 243 s default) = 16 % lebih cepat**, tapi koin **73 (vs 45) = +62 %**.
Margin i2v 5 s turun 69 % → **50 %** (masih di atas ambang 45 %). Kalau mau hemat: batasi `plus` hanya untuk fitur `long` (30 s).

**Akar "hasil aneh" job 10:** brief user berisi **5 aksi bertumpuk** (ketawa → lari → hampir jatuh → noleh →
kamera ngejar). i2v cuma sanggup SATU gerakan menerus; dipaksa banyak aksi → meleleh.
Bukti ffmpeg + vision: latar **berubah** (pantai sunset → parkiran mobil), kacamata warp, gigi menyatu, jari blob.

**Perbaikan terpasang (`promptsmith.VIDEO_REFINE_SYSTEM`):**
- Aturan baru #2: **ONE ACTION ONLY** — kompres banyak aksi jadi satu gerakan; larang rantai "then … then".
- Aturan baru #3: **larang chase-cam / handheld lari / whip pan** (sumber utama warping).
- Batas panjang 90 → **70 kata**.
- Bukti: brief job 10 yang sama sekarang jadi 3 kalimat, 1 aksi, kamera halus.

**Bahasa Indonesia:** sudah didukung sejak awal (`promptsmith` menerima brief Indonesia & menerjemahkan ke Inggris).
Ditambah panduan di deskripsi fitur i2v & `long`: "Boleh nulis PAKAI BAHASA INDONESIA" + "Tulis SATU aksi sederhana".

### 6e. MODE CERITA / MULTI-SCENE — jawaban "prompt gak jelas" (9 Okt 13:00)

**Masalah yang dijawab:** user nulis skenario panjang (mis. "wanita lari membelakangi kamera, kamera
mengejar, sesekali menoleh, hampir terjatuh, lanjut lari sambil ketawa"). i2v cuma bisa SATU aksi
menerus → kalau dipaksa, hasilnya meleleh.

**Solusi (fitur baru `story` — "🎬 Video Cerita (Multi-Scene)"):**
1. `promptsmith.split_story()` → LLM memecah cerita jadi N scene, **1 aksi per scene**, kamera lambat,
   tiap scene menyertakan klausa konsistensi wajah. Bahasa Indonesia/berantakan tetap diterima.
2. `storyboard.render_story()` → render N klip 5 detik **berurutan**, dan **frame terakhir klip ke-i
   dipakai sebagai gambar awal klip ke-(i+1)** (frame chaining) biar karakter + latar nyambung.
3. `storyboard.stitch()` → jahit semua klip jadi 1 video (concat + re-encode h264 + aac).

**Katalog:** `story` durasi 15 (3 scene, 1,5 Token) / 30 (6 scene, 2,5 Token).
`plan_shots()` → total ÷ 5 = jumlah scene. GPU untuk `story` sengaja **default** (bukan plus)
lewat `RUNNINGHUB_INSTANCE_STORY=default` supaya koin tetap murah.

**File:** `storyboard.py` (baru), `promptsmith.split_story()` (+`STORY_SPLIT_SYSTEM`, `_fallback_split`),
branch `krea_story` di `bot.py` `process_job()`, uji `tools/story_test.py`.

**Hasil pemecahan (terbukti, cerita persis punya user):**
- 3 scene: lari menjauh (kamera track maju) → tersandung & mengembalikan keseimbangan → menoleh & tertawa
- 6 scene: versi lebih rinci dari alur yang sama

### 6f. PRESET 1-TAP LIVE (9 Okt 13:20) + hasil uji mode cerita

**Preset 1-tap (permintaan user: "user dikasih pilihan situasi/pose")** — sudah terpasang:
kirim foto → bot kirim **grid preset** (harga tampil di tiap tombol) → 1 tap → layar konfirmasi → 🚀 Render.
File: `presets.py` (baru), `presets.kb_rows()`, handler `p:*` + grid di `on_photo()` (`bot.py`).
Preset video: 😄 tertawa · 💃 menari · 🚶 vlog selfie · 😮 kaget · 💪 pose model · 🌬️ angin natural ·
✍️ tulis sendiri · 🎲 kejutan. Preset editor: 👕 ganti baju · 🏝️ ganti latar · 🌆 cyberpunk · 🧽 hapus objek · 📸 studio.
Dokumen rancangan: `RANCANGAN-UX-PRESET-9OKT.md`.

**Uji mode cerita (3 scene, frame chaining, jahit) — SELESAI, hasil JUJUR:**
- Mesinnya BEKERJA: 3 klip → frame terakhir dirantai ke klip berikutnya → jahit jadi
  `hasil_cerita.mp4` **768×1280 · 24 fps · 14,1 detik · ada audio**, 561 s, **216 koin** (pakai GPU plus).
- TAPI kualitas output **belum layak jual**: 3 scene-nya jadi selfie close-up semua, aksi "lari menjauh"
  TIDAK muncul, dan latar berubah antar scene (indoor → luar malam → parkiran mobil).
- **Keputusan sesuai aturan "jangan jual yang belum terbukti": `story` DIKELUARKAN dari SIAP_JUAL**
  dan preset `larikejar` + `cerita` ditandai `beta=True` (tidak tampil di grid) sampai akar masalahnya beres.

**Hipotesis akar masalah yang sedang diuji:** mungkin **prompt tidak benar-benar sampai ke model**
(binding node `304.text` salah). Uji diagnostik: prompt mustahil-terlewat (wig badut merah + topi
pelangi + bendera kuning + latar gunung salju) → `tools/prompt_probe.py`.
Kalau output tidak memuat itu → binding prompt salah, bukan salah prompt user.

### 6g. HASIL PROBE PROMPT — BINDING BENAR (9 Okt 13:20)

**Uji:** render i2v 5 s dengan prompt mustahil-terlewat — *"wig badut merah + topi pelangi tinggi +
bendera kuning + latar gunung salju"* (`tools/prompt_probe.py`, 159 s, 64 koin).
**Hasil (vision, 2 frame):** semuanya MUNCUL — wig badut merah ✔, topi pelangi ✔, bendera kuning ✔,
latar gunung salju ✔.

⇒ **Binding node `304.text` BENAR. Prompt benar-benar sampai ke model.** Hipotesis "binding salah" GUGUR.

**Kesimpulan akar masalah sebenarnya:** model LTX kuat untuk mengubah **penampilan/kostum/latar**
(malah bisa mengubah seluruh scene), tapi **lemah untuk gerak tubuh besar** (lari menjauh dari kamera,
kamera mengejar) — dia cenderung mempertahankan framing close-up selfie input.

**Implikasi produk:**
- Preset yang mengandalkan ekspresi/gerak halus (😄 tertawa, 😮 kaget, 🌬️ angin, 💪 pose, 🚶 vlog) → **cocok** dengan mesin sekarang.
- Preset lokomosi (🏃 lari dikejar kamera) → butuh jalur lain (masih beta).

**Insight kunci (cara Kuzushi dapat gerak lari):** fitur mereka **"Face Swap & Motion"** menerima
**VIDEO sumber gerakan (.mp4)** — jadi gerak lari/chase diambil dari footage nyata, wajah user
ditransfer ke situ. **Bukan** gerak yang digenerate dari still. Ini sebabnya mereka bisa dan kita belum.

**Rencana berikutnya:** cari + uji app **VIDEO face swap** (input: foto user + video gerakan),
lalu jual sebagai "Face Swap & Motion" (±1 Token vs 2 Token Kuzushi).

### 6h. 🔥 MOTION TRANSFER (Wan2.2 Animate) — CELAH KUZUSHI KETEMU (9 Okt 13:30)

**Temuan:** app AI `2039639280896708610` = **"New Wan2.2 Animate Motion Transfer"** (useCount 6.954).
Ini **persis fitur andalan Kuzushi "Face Swap & Motion"**: foto karakter + **video sumber gerakan** → video.
Model open-source (Wan 2.2) → **jalur koin**, bukan jalur dolar.

**Node (dibaca dari `/api/webapp/apiCallDemo?apiKey=…&webappId=…`):**

| Node | Fungsi | Nilai kita |
|---|---|---|
| 484 | LoadImage 主图 | `@photo1` (foto user) |
| 485/486/487 | LoadImage 副图1–3 | tidak dipakai |
| **488** | **VHS_LoadVideo** | `@video` (video gerakan) |
| 476 | 秒数 (detik) | `@duration` |
| 475 | 帧率 | 16 |
| 482 | 分辨率 | **3 = vertikal 720p** |
| 478 | 姿势 (1=vitpose, 2=sdpose, 3=scailpose) | 1 |
| 470 / 479 | 抖动幅度 / 表情强度 | 0,5 / 1,0 |

Catatan: contoh curl RESMI dari RunningHub untuk app ini memakai `"instanceType": "plus"` → pilihan plus kita valid.

**Uji produksi nyata (5 detik, foto ref1 + video 10 s):**
`state=done` · **308 s** · **121 koin** (±Rp411) · output **720×1280 · 16 fps · 5,06 s · ADA AUDIO (AAC 48 kHz)**.
(gunakan `smooth_fps()` untuk 16→24 fps di produksi.)

**Uji face-swap pakai video di app LAMA: GAGAL** (`FAILED`) — app `1889155568379092993` hanya menerima GAMBAR.
Jadi fitur motion WAJIB memakai app Wan2.2 Animate di atas.

**Konfigurasi `.env` (sudah dipasang, belum dijual):**
`RUNNINGHUB_APP_MOTION=2039639280896708610` · `RUNNINGHUB_APP_NODES_MOTION=[484.image←@photo1, 488.video←@video, 476.int←@duration, 482.value=3, 478.select=1]` · `RUNNINGHUB_INSTANCE_MOTION=plus`.
Uji: `tools/motion_test.py`. Backup `.env.bak-before-motion`.

**Yang BELUM terbukti (jangan dijual dulu):** fidélitas wajah lintas-orang. Semua material uji kita
orang yang sama (ref1, app_bernini, app_wan22) sehingga swap tidak bisa dibedakan secara visual.
Perlu 1 uji dengan **video gerakan orang LAIN**.

### 6i. INVENTORY: 🧑🎨 KARAKTER SAYA + 🛍️ PRODUK SAYA (9 Okt 13:45)

**Permintaan user:** user bisa simpan master character sheet (dan produk untuk UGC), bisa ditambah/dihapus/
dinamai sendiri, lalu **tinggal sebut namanya** → otomatis dipakai secara identik. Ditaruh di **paling atas
inventory/menu**.

**DB:** tabel `characters` + kolom `kind` (`char` | `produk`), `UNIQUE(telegram_id, kind, name_lower)`
(nama tidak boleh kembar per jenis). Method: `char_save/list/count/get/find_in_text/rename/delete/bump`
(+ migrasi `ALTER TABLE characters ADD COLUMN kind`).
**Kunci identik:** yang disimpan adalah **file_id foto master**; dipakai ulang foto yang SAMA tiap render →
wajah/karakter konsisten antar hasil.

**UI:**
- Menu utama: 2 tombol **di paling atas** → `🧑🎨 Karakter Saya (N)` · `🛍️ Produk Saya (N)`.
- Daftar → tap item = lihat foto + `✏️ Ganti nama` / `🗑 Hapus`; tombol `➕ Tambah baru`.
- Tambah: kirim foto → ketik nama (contoh "si rina" / "kopi arabika").
- **Auto-pakai:** `db.char_find_in_text()` — user cukup menulis *"bikin video si rina joget"* di prompt
  (atau *"promo kopi arabika diskon"* di brief UGC) → bot otomatis memakai aset tersimpan itu + menaikkan `uses`.
- Tombol 1-tap juga disediakan di alur: `use:c:<id>` (video: karakter → lanjut pilih preset),
  `u:ch:<id>` (UGC karakter), `u:pr:<id>` (UGC produk).

**UGC jadi 2 langkah gampang:** langkah 1 karakter (tersimpan / baru) → langkah 2 produk (tersimpan / baru)
→ ketik brief. Semua bisa 1 tap kalau asetnya sudah disimpan.

**Uji:** `selftest` **93/93** (9 tes baru: simpan, anti-kembar, panggil dari nama, deteksi di teks,
deteksi produk, rename, hapus).

**KEPUTUSAN HARGA (user, 9 Okt):** **jangan** lebih murah dari Kuzushi — **samakan harganya**; kita menang di
**KUALITAS**: kemiripan wajah, konsistensi karakter, dan gerakan yang natural seperti manusia.

### 6j. LIPSYNC / DIGITAL HUMAN — LTX 2.3 NGOMONG (9 Okt 14:20)

**App ketemu:** `2031016553440878594` = *"LTX2.3数字人说话唱歌对口型 kj版"* — **foto + AUDIO → video orang ngomong lip-sync**,
1280p, fps 25–30 (klaim app: ~5 menit per 10 detik).

**Node (dari `apiCallDemo`):**
| node | isi | catatan |
|---|---|---|
| `444` | image | 人物图 (9:16 / 16:9 lebih bagus) |
| `1755` | audio | upload lagu/suara |
| `1583` | seconds | durasi (≤35 dtk, 0 = seluruh audio) |
| `1776` | float | audio mulai dari detik ke-berapa |
| `1624` | text | 动作提示词 (motion prompt) — default "角色面向镜头深情的说话，固定镜头。" |
| `1606` | int | resolusi maks (≤1600) = 1280 |
| `1586` | float | fps = 25 |

**Kenapa ini penting:** ini **separuh realisme** yang belum kita punya — orang yang *benar-benar ngomong*
(prompt-based motion kita lemah lokomosi, tapi **talking-head** justru paling gampang terasa nyata).
Pasangan alaminya: **base Karakter Saya** (wajah konsisten) + **TTS Bahasa Indonesia** (suara) + node prompt tetap.

**Sudah dipasang:** `.env` `RUNNINGHUB_APP_LIPSYNC=2031016553440878594` + `RUNNINGHUB_APP_NODES_LIPSYNC`
(audio masuk lewat `@video` karena backend belum punya slot audio khusus), `tools/lipsync_test.py`.
**Uji produksi:** `ref1.jpg` (719×1280) + TTS Indonesia 15 dtk → task `2108441505478221826`.

### 6k. PARITAS FITUR KUZUSHI — 2 FITUR BARU NYALA (9 Okt 14:40)

**Keputusan user:** *"tinggal pake fitur original aja kaya yang dipake kuzushi"* — stop eksperimen, samain
daftar fitur Kuzushi, pakai mesin original.

**Cek menu Kuzushi vs kita** (Kuzushi 8 item · kita 8 fitur):
| # | Kuzushi | Harga | Kita |
|---|---|---|---|
| 1 | 🎭 Face Swap & Motion Video | 2T | ✅ **BARU NYALA** `motion` (app Wan2.2 Animate `2039639280896708610`) |
| 2 | 🎬 Image to Video | 0,5–2T | ✅ `i2v` 5/10/15 + `long` 30 |
| 3 | 🖌️ AI Image Editor | 0,3T | ✅ `editor` |
| 4 | 🕺 Pose Transfer & Style | 0,5T | ⏳ masih DITAHAN (butuh app pose-dari-GAMBAR) |
| 5 | 🎤 AI Video Lip Sync | 0,5T | ✅ **BARU NYALA** `lipsync` (app LTX digital human `2031016553440878594`) |
| 6 | 🌌 Video All-in-One | 1T | ✅ `allinone` |
| 7 | Top Up QRIS + Referral | — | ✅ |
| 8 | Profil & Saldo, Voucher, Panduan | — | ✅ |

**Harga DISAMAKAN dengan Kuzushi** (keputusan user: jangan lebih murah): motion 2T, lipsync 0,5T.
**Margin terukur:** motion 5 dtk **73%** (121 koin) · lipsync 10 dtk **57%** (≈48 koin).

**Cara pakai (di bot):**
- 🎭 Face Swap & Motion: kirim **FOTO orang** → kirim **VIDEO gerakan contoh** → jadi (gerak asli dari video, wajah dari foto).
- 🎤 Lip Sync: kirim **FOTO orang** → kirim **SUARA** (voice note/audio ≤10 dtk) → orang itu ngomong, mulutnya cocok.
  Durasi otomatis ikut panjang suara (ffprobe, maks 10 dtk).

**Perubahan kode:** `catalog.py` (fitur `motion` baru; `lipsync` 2 aset foto+suara; harga; SIAP_JUAL 8),
`bot.py` (terima VIDEO & AUDIO sebagai aset; label per-aset "Foto orang / Video gerakan / Suara";
motion+lipsync langsung ke konfirmasi tanpa preset; aset ke-2 → `video_in`; durasi lipsync dari suara),
`selftest.py` (koin terukur motion/lipsync). Uji: **selftest 95/95**, ux_audit bersih, bot restart OK.

### 6l. KEPUTUSAN: 100% MESIN RUNNINGHUB ORIGINAL (9 Okt 15:05)

**Pertanyaan user:** *"pastiin pake model dari runninghub.ai doang kan atau ada opsi lain? kalo ngerusak
kualitas mending pake dari ori runninghub aja."*

**Jawaban teknis (terverifikasi):** SEMUA render pakai RunningHub original — `KREAIBOT_BACKEND=runninghub`,
`RUNNINGHUB_BASE=https://www.runninghub.ai`, tiap fitur → AI App/workflow RunningHub (tidak ada provider
generasi lain sama sekali).

| Fitur | App RunningHub (orisinil) |
|---|---|
| 🎬 i2v + 30 dtk | LTX 2.3 `2065707741691334658` |
| 🎭 Face Swap & Motion | Wan 2.2 Animate `2039639280896708610` |
| 🎤 Lip Sync | LTX Digital Human `2031016553440878594` |
| 🕺 Pose Transfer | 姿势迁移 `2038158176293494785` |
| 🎭 Face Swap gambar | 极速换脸 `1889155568379092993` |
| 🌌 All-in-One · 🛍️ UGC · 🖌️ Editor | workflow RunningHub |

**3 hal NON-RunningHub (tak ada yang model generasi):**
1. PromptSmith (LLM) — cuma **menulis teks prompt**, tidak bikin gambar/video. Saklar: `KREAIBOT_REFINE_VIDEO=0`.
2. edge-tts — bikin **suara**; HANYA dipakai di skrip uji. Di bot, audio lip-sync = **voice note user** (original).
3. ffmpeg — post-processing lokal. ⚠️ **DITEMUKAN MASALAH:** `smooth_fps()` dulu pakai `minterpolate`
   (membuat FRAME SINTETIS) → bisa menurunkan kualitas. **Sudah DIMATIKAN secara default**
   (`KREAIBOT_SMOOTH_FPS=0`): hasil keluar apa adanya dari RunningHub. Nyalakan hanya bila diminta.

### 6m. POSE TRANSFER NYALA — PARITAS KUZUSHI LENGKAP 9/9 (9 Okt 15:00)

App `2038158176293494785` (姿势迁移, node `24`=人物图←@photo1 · `31`=姿势图←@photo2), GPU default.
Harga **0,5 Token** (sama Kuzushi). Uji produksi: **172 dtk, 32 koin ≈ Rp143 → margin 71%**, output
gambar **936×1664**. Kualitas uji belum meyakinkan (pose hanya sebagian pindah, tangan aneh) — **penyebab:
bahan uji jelek** (foto orang rebahan + berkacamata hitam; "foto pose" dari frame hasil AI sebelumnya).
Butuh 2 foto bersih dari user untuk verdict final.

### 6n. BUG FIX: "➕ Tambah baru" muncul popup "Jenis tidak dikenal" (9 Okt 15:08)

**Laporan user:** klik ➕ Tambah baru di Karakter/Produk Saya → popup **"Jenis tidak dikenal"**.

**Akar masalah:** `cb_inv` membaca `parts[2]` dari callback. Untuk `m:inv:add:char` (4 bagian),
`parts[2]` = `"add"` → tidak ada di `INV_ICON` → alert salah. Callback `m:inv:char` (3 bagian) kebetulan benar.

**Perbaikan:** fungsi `inv_parse()` (bisa diuji) yang membaca aksi & jenis dengan benar:
`m:inv:char` → ('char','buka') · `m:inv:add:char` → ('char','add').

**Sekalian ditutup (anti-bingung, dulu bot DIEM):**
- kirim video/stiker/teks padahal diminta foto → sekarang dijawab "Kirim FOTO ya".
- kirim foto padahal diminta nama → dijawab "Ketik nama-nya ya".
- kirim dokumen non-gambar (PDF) → ditolak jelas.

**Uji:** selftest **104/104** (4 tes baru untuk parsing inventory + 3 tes anti-bingung), ux_audit bersih.

### 6o. AKAR "HASIL ANEH": USER KIRIM CHARACTER SHEET KE I2V (9 Okt 16:05) — FIXED

**Laporan user:** "lihat hasil video generate gue di kreeai bot, kenapa malah jadi kaya gitu" (job 13, i2v 15s).

**Akar masalah (dibuktikan, bukan dugaan):** foto yang dikirim ke i2v = **character sheet 15 panel**
(`work/tests/j13/job13_ref.jpg`, 853×1280) — ada label "MAIN VIEW (CLOSE UP)", "SIDE VIEW (RIGHT)",
"BACK VIEW", "EYES/NOSE/LIPS DETAIL", "SKIN TEXTURE", plus color swatch & teks kecil.
Model i2v **menggerakkan gambar itu apa adanya** → video jadi berisi **kotak-kotak panel**, bukan orang.
Cacat kedua: prompt minta "selfie pakai hp iphone orange" → **tangan + HP** (kelemahan umum AI) muncul ~detik 12–14.
Job 10–12 pakai foto normal (717×1276) — jadi masalah ini KHUSUS job 13 (input sheet).

**FIX LIVE — `sheetfix.py`:**
1. Sebelum render, foto diperiksa **model vision** (PromptSmith `ag/gemini-3.6-flash-high` — output JSON teks saja,
   bukan model generator): `{"sheet": true/false, "box":[x,y,w,h]}`.
2. Kalau sheet → **potong panel orangnya** (PIL, buang margin 2%, tolak kotak < 220px) → panel itu yang dirender.
3. User dapat pesan "🔍 Memeriksa fotonya sebentar…" → lalu panel hasil potong + penjelasan.
4. Berlaku di: `SHEET_GUARD = {i2v, long, allinone, faceswap, motion, lipsync, pose}` (aset ke-1) **dan**
   saat menyimpan ke Karakter/Produk Saya (biar sheet tersimpan tidak merusak semua render berikutnya).
   UGC di-skip (di sana sheet memang karakter sheet). Gagal/ragu → **foto asli dipakai** (bot tetap jalan); ada cache per file_id.

**Bukti uji:** sheet user → terdeteksi `sheet=true box=[0,0,508,682]` → panel **488×656** (8,8 dtk per cek);
foto normal → `sheet=false` (tidak false-positive). Selftest **113/113** (10 tes baru sheetfix).

**Sisa kelemahan yang jujur:** tangan + objek kecil (HP) tetap titik lemah model — bukan bug bot.

### 6p. BUG "Image Editor jadi kayak video + gepeng" (9 Okt 16:20) — FIXED

**Laporan user:** bikin image creator, "hasilnya malah jadi seperti video dan rasionya nggak 9:16, jadi kaya gepeng".

**Akar masalah (dibuktikan):** app AI Image Editor mengembalikan **GAMBAR PNG 768×1376 (9:16 BENAR)**,
tapi worker menyimpannya dengan **nama tetap `hasil.mp4`** (`out = work / "hasil.mp4"`).
`send_result()` memilih jalur kirim dari **ekstensi nama file** → PNG dikirim sebagai **VIDEO**
(Telegram menampilkannya di pemutar video → kelihatan "gepeng"). Bukan rasio yang salah, cuma
salah jalur kirim.

**Dampak sama di job 14** (editor, 16:04): render SUKSES tapi **gagal di `send_video`**
(`ServerDisconnectedError`) → job ditandai gagal → token **sudah direfund** (ledger: −0,3 lalu +0,3 ✓).

**FIX:** `backends/mediafix.fix_ext()` — baca 16 byte pertama file, tentukan jenis dari ISI
(PNG/JPG/GIF/WEBP/MP4/WEBM/ZIP) lalu ganti ekstensi. Dipanggil **sebelum** `smooth_fps` + `send_result`
di jalur utama dan jalur cerita. Jadi gambar selalu dikirim sebagai foto.

**Tindakan tambahan:** file job 15 dinama-ulang `hasil.mp4 → hasil.png`, DB diupdate, dan hasilnya
**dikirim ulang ke user sebagai FOTO** (message_id 166) supaya user lihat hasil aslinya.

**Uji:** selftest **119/119** (6 tes baru fix_ext: PNG↔MP4 bolak-balik, nama benar tak diubah, file hilang aman).

### 6q. BUG "kirim foto ke i2v tapi bot DIEM" (9 Okt 16:35) — FIXED (sesi tahan restart)

**Laporan user:** pilih Image to Video → kirim foto (tanpa pilih karakter tersimpan) → **tidak terjadi apa-apa**,
tidak lanjut ke langkah prompt.

**Akar masalah (dari log, bukan dugaan):** `16:13:51` bot di-**RESTART** (deploy saya), `16:14:12` user kirim foto →
log: **"Update id=300858148 is not handled"**. aiogram menyimpan state FSM di **RAM** (`MemoryStorage`):
restart = **semua sesi user hilang** → handler foto cari state `Flow.photos` → tidak ada → tidak ada yang cocok
→ bot **diam total**. Jadi fitur i2v-nya TIDAK rusak; sesinya yang kehapus oleh restart.

**FIX 1 — sesi tahan restart:** `fsmstore.py` = `SQLiteStorage` (BaseStorage aiogram 3, file `kreaibot_fsm.sqlite3`,
JSON untuk data sesi, auto-bersih > 30 hari, aman dari crash). `Dispatcher(storage=SQLiteStorage(fsm_path))`.
Sekarang: pilih fitur → kirim foto → prompt nyambung walau bot baru restart.

**FIX 2 — anti-DIEM permanen:** handler `fallback_tak_ditangani` sebagai handler **TERAKHIR** (setelah command
admin & teks bebas, dengan guard `~F.text.startswith("/")`). Pesan/berkas yang tidak cocok handler mana pun
→ bot SELALU menjawab ("sesi ke-reset, tekan /start") + tombol menu. Jangan pernah diam lagi.

**Uji:** selftest **125/125** (6 tes baru: state & data bertahan di instance baru = simulasi restart,
Dispatcher pakai storage file, fallback terdaftar & posisinya paling akhir).

### 6r. "PAKAI KARAKTER ARUNIKA, WAJAH TIDAK IDENTIK" (9 Okt 16:40) — 2 SEBAB, 2 FIX

**Laporan user:** bikin AI Image Editor pakai karakter tersimpan "Arunika" → struktur wajah tidak identik.
Masih setelah perbaikan pertama: **"tetep gak mirip sama sekali"** (mata user = kebenaran; skor model vision ~70–90% TIDAK dipakai sebagai bukti).

**SEBAB 1 — Arunika tersimpan sebagai CHARACTER SHEET 15 panel.** Dibuktikan vision atas `work/job_18/ref1.bin`
(853×1280): MAIN VIEW / SIDE VIEW / BACK VIEW / EYES+NOSE+LIPS DETAIL / SKIN / 4 swatch.
Model harus **mengarang wajah** dari kolase yang memuat sisi samping-belakang → wajah tak konsisten.
Karakter disimpan sebelum sensor `sheetfix` ada, jadi lolos.
*FIX:* `tools/fix_saved_chars.py` (migrasi) — unduh foto tiap karakter → deteksi sheet → potong panel → unggah ulang →
`db.char_set_file_id()`. Dijalankan: **Arunika diperbaiki** (panel dikirim ke user, file_id DB diganti).
Ditambah: `editor` masuk `SHEET_GUARD`; karakter tersimpan dijaga lagi saat DIPAKAI (`use:c:` / `u:ch:` →
`_sheet_panel_from_file(fix_char_id=…)` = perbaikan permanen).

**SEBAB 2 — model editor MENGGAMBAR ULANG wajah.** Render ulang editor pakai panel bersih: user tetap bilang
tidak mirip. Model `RhinatImageNG31Flash Image2Image` (app "All-in-One Image V2 Image-to-Image") mengganti proporsi
rahang/bibir; prompt "keep face identical" tidak menolong (sudah dicoba di job 15/18).

**FIX 2 — KUNCI IDENTITAS (`identity.py`):** setelah render, wajah asli karakter **di-swap balik** ke hasil render
(app Face Swap 极速换脸 yang sama dipakai fitur Face Swap Karakter) → hasil memakai **pixel wajah asli**.
Nyala OTOMATIS kalau: fitur `editor` + foto referensi = karakter/produk **tersimpan** user (`db.char_by_file_id`)
+ hasil berupa gambar. Biaya internal +10 koin, +~60 dtk; harga jual tidak berubah. Gagal → hasil asli tetap dikirim.

**Uji:** editor 41 dtk (11 koin) → face swap 10 koin → hasil dikirim ke user (msg 221) untuk **penilaian mata user**.
Selftest **133/133** (8 tes baru). Prinsip: **"jangan jual yang belum terbukti"** — jangan klaim mirip sebelum user bilang mirip.

### 6s. "GAGAL TERUS" — SALDO $ vs KOIN + FALLBACK APP (9 Okt 17:35) — FIXED

**Keluhan user:** "gue bikin gambar gagal terus, lu sengaja halangin padahal runninghub bebas".

**AKAR MASALAH (dibaca dari log, bukan dugaan):** job 25/26/27 (editor, 17:25–17:29) gagal dengan
`code 433` → `"Your API balance is insufficient, please recharge and use it"`
pada node `RH_RhartImageNG31FlashImageToImage` (app **"全能图片V2-图生图-低价渠道版"** = `2061699451919618049`).

**Pelajaran kunci:** di RunningHub ada DUA dompet:
 - **KOIN** (remainCoins, sekarang ±31.7 ribu) → dipakai app biasa (LTX, Wan, Kontext, Qwen 2511) ✅
 - **SALDO API $** (remainMoney, sekarang **$0,037**) → dipakai app **"低价渠道版" (low-cost channel)** ❌
Koin banyak tapi $ kosong → app kelas cheap-channel **menolak jalan seketika**. Bukan pembatasan pihak lain;
murni saldo dompet kedua. App Seedream/即梦5.0Pro 单图编辑 juga kelas ini (makanya "FAILED" 16–22 detik).

**FIX 1 — app editor dipindah ke mesin yang bayar KOIN:** `RUNNINGHUB_APP_EDITOR=2075393520445251586`
(**Flux Kontext 智能图文编辑**) — TERBUKTI jalan 57 dtk/21 koin, **menjaga rasio foto input** (488×526 → 488×520)
dan menjaga identitas. (Cadangan: `2056741213927206914` Qwen 2511 一致性.)

**FIX 2 — FALLBACK APP OTOMATIS (permanen):** `backends/runninghub.py`:
 - `RUNNINGHUB_APP_<FITUR>_ALT` = app cadangan.
 - Gagal saat **submit** → langsung coba app cadangan (`_run_app`).
 - Gagal saat **poll** (state FAILED) → submit ulang ke cadangan SEKALI, `taskId` lama dipetakan ke task baru
   lewat `_alias`, user tidak melihat error.
 - Uji paksa: app rusak di depan → **FALLBACK BERHASIL 61 dtk** (pindah sendiri ke cadangan).
 - “Jangan jual yang belum terbukti”: ini yang bikin satu app mati tidak lagi berarti "gagal terus".

**Refund:** job 25/26/27 otomatis direfund (−0,30 lalu +0,30 ×3) — token user utuh (22 token).

**Pilihan user (bukan pembatasan):** kalau mau app kelas cheap-channel (即梦/Seedream 5.0 Pro, 全能图片V2 —
per gambar cuma 2 koin ≈ Rp7), tinggal **isi saldo API $** di akun RunningHub; kalau tidak, semua fitur
tetap jalan lewat app berkoin.

### 6t. PANEL PER-TUJUAN + FULL BODY ARUNIKA (9 Okt 17:5x)

**Masalah user:** "ukuran body nya nggak sesuai ... buatin gua karakter sheet full body yang mudah dibaca sistem,
struktur wajah & proporsi body harus identik".

**Yang dikerjakan:**
1. **`sheetfix` dua mode (`purpose`)**: `body` → panel SATU ORANG SELURUH BADAN (referensi render → proporsi konsisten);
   `face` → panel WAJAH CLOSE-UP (untuk face-swap/kunci identitas). Prompt vision berbeda per mode;
   cache di bot dipisah per tujuan (`file_id:purpose`).
2. **Kunci identitas ambil panel wajah**: worker kini menganalisa foto karakter dengan `purpose="face"` dan
   memotong panel wajahnya sebelum face-swap (sebelumnya bisa memakai panel badan → swap jelek).
3. **Full body Arunika (outfit asli)** dari app RunningHub **三视图/多视图** (`2075468800715214850`):
   hasil **1080×2160**, kepala-sampai-sepatu, wajah tetap Arunika, outfit asli (kardigan putih/atasan hitam/celana hitam).
   Biaya nyata: **10 menit + 262 koin** (app berat). Catatan: input foto WAJAH → output hanya 1 tampilan depan;
   percobaan ke-2 dengan input FULL BODY dijalankan untuk memicu output multi-sudut.
4. **Sheet 4 panel** (FACE CLOSE UP + FRONT/SIDE/BACK FULL BODY, latar seragam, label strip di luar panel,
   tanpa teks di dalam panel) dibuat `tools/make_sheet.py`; panel wajah dibersihkan dari label sisa sheet lama.
5. Tersimpan di bot: 🧑🎨 **Arunika** (wajah) · 🧍 **Arunika Full Body** (outfit asli) · 📋 **Arunika Sheet** (4 panel).

Selftest **145/145**. Vault sync.

### 6u. BUST/FIGUR FIDELITY — RESEP TERUKUR (9 Okt 18:0x)

**Keluhan user:** "lihat ukuran dada nya ... percuma gua build bot kalo tetep pake kuzushi ujung ujungnya".

**Fakta & angka (bukan opini):**
- Referensi user = foto **dada-ke-atas**, dada **penuh/besar** (kardigan terbuka + atasan hitam low-cut).
- Full body v1 (Qwen, prompt hoodie) → **dada kecil/tertutup** ✗ (salah saya: outfit hoodie menyembunyikan bentuk).
- **三视图/多视图 app `2075468800715214850`** (input wajah maupun full body): **10 menit, 225–262 koin, hanya keluar 1 tampilan depan, dada 50–70%** → TIDAK dipakai lagi.
- **Qwen 2511 (`2056741213926904`/`2056741213927206914`) + prompt eksplisit "same full bust size, same figure, no change to her body proportions" + outfit ASLI** →
  **dada 85–95% mirip** (dinilai vision berulang), **21 koin / 51 dtk** (samping malah 8 koin / 21 dtk).
  → **RESEP RESMI** untuk panel full body: mesin Qwen 2511 + prompt jaga-bentuk + outfit referensi.

**Sheet v2 (`work/tests/arunika_sheet2.png`)**: FACE CLOSE UP = **foto asli user** (pixel asli, label dibuang),
FRONT/SIDE/BACK = resep Qwen di atas, latar seragam, label DI LUAR panel, tanpa teks nyasar.
Subjudul diubah jadi JUJUR ("face close-up is the real photo; full-body panels are AI views generated FROM that photo")
— tidak lagi mengklaim "identical". Cacat jujur: dada antar panel belum persis sama (SIDE lebih penuh dari FRONT),
artefak kecil di kepala panel BACK. Tersimpan sebagai karakter **"Arunika Sheet"** (id 3).

**Kesimpulan produk:** IDENTIK 100% hanya dari **foto asli multi-sudut** (badan/dada nyata). Semua jalur generate
= "mirip". Ini pembeda nyata vs Kuzushi: kumpulkan **bank foto asli** user → tiap render nembak foto paling cocok.

### 6v. BUG KRITIS: BOT SALAH AMBIL PANEL SHEET (9 Okt 18:3x) — SUDAH DIPERBAIKI

**Bukti nyata:** kotak yang dikasih model vision TIDAK sinkron dengan geometri sheet (koordinat balik
di ruang ~1000px, sedangkan sheet 1778px). Akibatnya `crop_panel` memotong **judul + potongan wajah
ekstrem** dan itu yang dipakai sebagai referensi render → ini AKAR "wajah nggak mirip sama sekali".
Dibuktikan dengan komposit (kiri = hasil crop lama = teks "ARUNIKA — CHARA" + potongan mata; kanan = panel benar).

**FIX (sheetfix.py):** bot TIDAK lagi nebak koordinat model.
- `GRID` = konstanta tata letak `tools/make_sheet.py` (cols 2, margin 24, gutter 24, label_h 64, ph 1280, head 120).
- `layout_panels(size)` → hitung kotak semua panel kalau gambar = sheet buatan kita (None kalau bukan).
- `panel_for(path, purpose)` → `face` = panel 1 (FACE CLOSE UP), `body` = panel 2 (FULL BODY FRONT) — PASTI.
- `crop_panel(..., purpose=)` → prioritas geometri; kalau bukan sheet kita baru pakai box model
  (dinormalkan f = W/1000 kalau W>1200) → tidak salah skala lagi.
- `bot.py` sekarang mengirim `purpose` ke `crop_panel`.
- 7 tes baru; **selftest 152/152**.

**Konsekuensi:** sheet 6-panel Arunika final sekarang benar-benar dipakai (mode badan = full body asli
dengan proporsi & dada asli; mode wajah = close-up asli). Ini juga memperbaiki SEMUA karakter sheet lama.

### 6w. BUG KEDUA (LEBIH PARAH): KUNCI IDENTITAS GAGAL SENYAP SELALU (9 Okt 18:4x)

**Bukti:** `identity.lock_identity` memanggil `backend.generate(req)`. `RunningHubBackend` **tidak punya**
metode itu (API nyata: `submit(req) -> taskId`, `poll(taskId) -> GenStatus`). Karena seluruh blok dibungkus
`try/except` yang cuma `log.warning`, kegagalan **tidak pernah kelihatan** → SEMUA render editor selalu
memakai hasil mentah (wajah karangan model). Jadi akar "tetep gak mirip sama sekali" ada DUA:
(1) panel sheet yang salah dipotong, (2) kunci identitas yang tidak pernah jalan.

**FIX:** `identity.py` → `task = await backend.submit(req)` + loop `backend.poll(task)`.
Log dinaikkan ke `log.error` (tidak senyap lagi). Diuji sungguhan: render editor (28 koin, 72 dtk)
→ kunci identitas (极速换脸) **berhasil** menghasilkan `proof_locked.png`; panel 3 lebih dekat ke wajah asli
(alis/mata/bibir/warna kulit), sisa cacat: warna kulit leher sedikit beda.

**Tes anti-regresi (2):** (a) `identity.py` tidak boleh memanggil `.generate(` lagi, (b) backend palsu
`submit/poll` → hasil lock benar-benar dipakai. **selftest 154/154.**

**Pelajaran aturan:** semua penangkapan `except Exception` di jalur yang memengaruhi hasil user WAJIB
`log.error` + ada tes fungsional yang memanggil backend/nama metode nyata. `warning` senyap menyembunyikan
fitur mati total.

### 6x. KUNCI IDENTITAS JADI NYATA + KATALOG APP (9 Okt 19:0x)

**Katalog app** baru: `tools/rh_apps.py` (`pull`/`find`/`show`). 298 app terindeks, dan tiap app
membawa `invokeExample` yang berisi **nodeInfoList lengkap** (nodeId + fieldName + description) →
binding app sekarang PASTI, tidak ditebak lagi. (Ini akar kenapa dulu "face swap" jadi no-op:
node-nya salah tafsir.)

**Uji berlabel 4 mesin (wajah sama, satu render cafe):**
| Mesin | Mirip | Biaya | Waktu |
|---|---|---|---|
| **换头换脸提高相似度优化版 `2020760401977282562`** (Flux2-Klein, 4K) | **93%** | 71 koin | 104 dtk |
| Kontext (input wajah close-up + prompt "jangan ubah wajah") | 82% | 29 koin | 72 dtk |
| render mentah (editor Kontext) | 72% | 28 koin | 72 dtk |
| 换头换脸-真实自然 `2044289076647432194` | 58% | 18 koin | 47 dtk |
| 极速换脸 `1889155568379092993` (yang dipakai sebelumnya) | **no-op (0% perubahan)** | 10 koin | — |

**Binding app 93%:** node `6` = GAMBAR UTAMA (basis) · node `26` = FOTO REFERENSI WAJAH ·
node `70` = 1920 (sisi panjang) · node `25` = prompt (ada bawaan; kita kirim prompt teruji).

**Perubahan kode:** `identity.py` → `feature_key="idlock"`, `photos=[result, face_photo]`, `IDLOCK_PROMPT`.
`.env`: `RUNNINGHUB_APP_IDLOCK=2020760401977282562` + `RUNNINGHUB_APP_NODES_IDLOCK=...`;
fitur wajah pengguna **Face Swap juga pindah** ke app yang sama (app lamanya no-op),
ALT = `2044289076647432194` (真实自然, 18 koin) dengan binding 17=badan, 23=wajah.
`tools/rh_edit_probe.py` kini dukung 2 gambar (`RH_PROBE_PHOTOS`). **selftest 159/159.**

**⚠️ EKONOMI belum diputuskan user:** kunci = 71 koin ≈ Rp244. Editor 0.3T (Rp300) + render 28 koin
(≈Rp96) + kunci 71 koin (≈Rp244) = ±Rp340 untuk harga Rp300 → **RUGI**. Usul: opsi premium
"🔒 Kunci wajah" (mis. editor+kunci 0.8T) ATAU pakai kunci hanya kalau user pilih sendiri.

### 6y. FITUR BARU: CHARACTER CREATOR — MASTER SHEET OTOMATIS (9 Okt 19:4x)

**Permintaan user:** fitur kreator karakter — user kirim referensi wajah, lalu dipandu pilih
gender, penampilan/ras (Asia/Eropa/dst.), vibe wajah (imut/dst.), bentuk dada 1–3, langsing 1–3,
pinggul-bawah 1–3 → mesin menggambar **master character sheet** yang mudah dibaca sistem.
Biaya ditentukan sendiri; margin harus besar.

**Desain (nol-prompt, semua tombol):** menu utama → **🧬 Bikin Karakter Baru (2,5 Token)**.
Alur 8 langkah: foto wajah → gender → penampilan (8 pilihan) → vibe (7) → dada (1–3) → langsing (1–3)
→ pinggul (1–3) → outfit (7) → rangkuman + harga → **✅ Generate**.
Hasil: 1 panel WAJAH close-up + 3 panel BADAN (depan/samping/belakang) → disusun jadi sheet
tata letak `sheetbuild.py` (sama dengan yang dibaca bot) → **otomatis disimpan sebagai karakter**.
Token didebit di depan, **DIKEMBALIKAN otomatis kalau gagal**.

**Ekonomi (margin 76%):**
| item | koin | ≈ Rp |
|---|---|---|
| 1 wajah + 3 badan (Qwen 2511) | ±176 | ±600 |
| **harga jual** | — | **Rp2.500 (2,5 Token)** |
→ margin ±76%. Harga dinaikkan gampang: `chargen.COST`.

**File baru:** `sheetbuild.py` (TATA LETAK TUNGGAL: GRID + build + layout_panels),
`chargen.py` (tabel pilihan + prompt + `run()` + COST).
**Refactor:** `sheetfix.py` & `tools/make_sheet.py` sekarang delegasi ke `sheetbuild` (angka tata letak
tidak lagi ditulis dua kali — penyebab bug potong panel 9 Okt).
**Env baru:** `RUNNINGHUB_APP_CHARGEN=2056741213927206914` (Qwen 2511 konsistensi, node 52=image/54=prompt),
cadangan `..._CHARGEN_ALT=2075393520445251586` (Flux Kontext, node 390/399).
**selftest 172/172** (13 tes baru untuk creator).

### 6z. CHARACTER CREATOR — UJI NYATA & PERBAIKAN (9 Okt 19:5x)

**Uji pertama (CHARACTER CREATOR v1):** 174 dtk, 4 panel 1440×1750, sheet 1778×2880 (dibaca bot: 4 panel ✓).
Tapi penilaian jujur = **BELUM LAYAK JUAL**, 3 cacat nyata:
1. **Kotak tofu di judul** — subtitle sheet pakai emoji (👩🌸🍬) yang tidak ada di font DejaVu.
2. **Outfit & sepatu BEDA antar panel** (depan: dress beige + sneakers; samping/belakang: rok hitam + heels).
   Sebabnya: tiap panel digambar langsung dari panel WAJAH → model menafsir ulang pakaian.
3. Wajah antar panel belum 100%.

**PERBAIKAN (chargen.py):**
- `_ascii()` — buang karakter non-ASCII dari subtitle sheet (emoji → hilang, "·" → "-"). Tofu beres.
- `SHOES` per outfit (dress → black high heels, kasual → white sneakers, dst.) + prompt badan menyebut
  **sepatu eksplisit** dan menegaskan "Same outfit and same shoes as the reference image — do not change
  the clothes".
- **RANTAI GENERASI**: wajah → **badan DEPAN** → samping & belakang digambar **DARI PANEL DEPAN**
  (bukan dari wajah). Ini yang mengunci baju, sepatu, rambut & proporsi supaya konsisten.

**Uji kedua: 93 dtk** (lebih cepat dari uji pertama 174 dtk) — outfit + sepatu **konsisten**, tofu hilang, wajah konsisten antar panel ✓ (dinilai vision).
**Harga disesuaikan:** `chargen.COST = 3.0` (Rp3.000) karena biaya mesin TERUKUR ±200–220 koin ≈ Rp700–760
→ margin ±75%. Estimasi waktu di UI jadi "±1,5–4 menit" (terukur 93–174 dtk).

**Pelajaran:** kalau panel sheet digambar semua dari satu wajah, atribut (baju/sepatu) akan bervariasi →
selalu RANTAI dari panel tubuh pertama. Fon PIL tidak punya emoji → jangan taruh emoji di gambar.

### 7a. CHARACTER CREATOR — PERBAIKAN PROPORSI TUBUH (9 Okt 20:0x)

**Keluhan user:** "belum, ini proporsi tubuh paling ideal buat master karakter wanita"
(kirim foto full-body dress merah + heels) → badan hasil AI **belum** sesuai.

**Diagnosa (dibuktikan, bukan opini):** dibandingkan 3 panel berdampingan
(1 = foto user, 2 = wajah user ditempel ke badan foto user, 3 = badan digambar AI murni):
- panel 2 (tempel wajah) = **hampir identik** dengan foto user — proporsi, postur, kaki panjang ✓
- panel 3 (AI murni) = lebih pendek/lebar, pinggang kurang tegas, kaki lebih pendek, pose kaku ✗
→ **AKAR: model bahasa-teks tidak bisa meniru proporsi spesifik; harus pakai FOTO sebagai badan.**

**SOLUSI (terpasang):** langkah **9/9 OPSIONAL — "foto proporsi tubuh"**.
Kalau user kirim foto tubuh full-body: panel DEPAN dibuat dengan **menempel wajah user ke foto itu**
(app identitas 93% `2020760401977282562`, image1=foto tubuh, image2=wajah), lalu samping & belakang
dirantai dari panel depan → proporsi/baju/postur **PERSIS** foto user.
Kalau gagal → otomatis balik ke cara AI (user tidak pernah gagal).

**Catatan ukur:** percobaan mengukur proporsi pakai pixel GAGAL (latar bergradasi; deteksi orang ambruk)
→ jalur yang dipakai: garis ukur di gambar + model vision baca posisi sendi (bahu 22%, pinggang 41%,
pinggul 51%, kaki 48% tinggi). Pelajaran: **jangan buang waktu bikin segmentasi klasik di latar
bergradasi; pakai grid + vision atau langsung pakai foto sebagai acuan.**

### 7b. CHARACTER CREATOR — VERSI FINAL + HARGA (9 Okt 20:3x)

**Perbaikan tambahan:** panel WAJAH sekarang **DITURUNKAN dari panel badan** (`face_from_body_prompt()`),
bukan digambar terpisah dari foto wajah. Sebab: panel wajah terpisah → rambut & baju beda dari panel
badan (dinilai vision). Sekarang rambut/kacamata/baju SAMA di 4 panel ✓.

**Bukti uji bertingkat:**
- v1 (semua dari wajah): baju & sepatu beda antar panel ❌ + tofu di judul ❌
- v2 (rantai dari panel depan): baju/sepatu konsisten ✅ tapi panel wajah masih beda ❌
- v3 (badan dari FOTO user): proporsi persis foto user ✅ tapi panel wajah masih beda ❌
- **v4 FINAL**: badan dari foto user + panel wajah dari panel badan → **4 panel konsisten** ✅
  (1 sisa catatan kecil: panjang gaun depan sedikit lebih mini dari samping/belakang)

**Dimensi sheet bisa berubah** (1778×2880 atau 1522×2880) tergantung rasio panel — TIDAK masalah karena
`sheetbuild` = satu sumber tata letak yang dipakai penulis sheet DAN pembaca (`sheetfix`) ✓ terverifikasi
bot tetap membaca 4 panel.

**HARGA FINAL = `chargen.COST = 4.0` Token (Rp4.000).** Alasan (biaya mesin TERUKUR nyata):
| jalur | render | koin | ≈ Rp |
|---|---|---|---|
| pakai foto tubuh | 5 | **361** | Rp1.227 |
| tanpa foto tubuh | 4 | 200–250 | Rp700–850 |
→ margin 69% (paling berat) s/d 80%. (Catatan: `remainCoins` dari API bisa LAG — pengukuran
"sebelum/sesudah" di dalam skrip sempat melaporkan 111 koin padahal nyatanya 361; ukur ulang
setelah ±5 menit.)

**Waktu:** 208–290 dtk (3,5–5 menit) dengan foto tubuh; 93–174 dtk tanpa.

### 7c. BUG BESAR: BOT "NGGAK BEBAS" + HASIL DIRUSAK (job 28) — 9 Okt 20:4x

**Keluhan user:** "RUSAK BOT GUA JADI RUSAK NGGAK BEBAS KAYA KUZUSHI, LIAT IMAGE CREATOR TERAKHIR
YANG GUA BIKIN" (job 28: *"ganti outfit sesuai vibes, memakai bikini di sunset pantai, selfie, 8k"*).

**AKAR #1 (bot tidak bebas — paling parah):** fitur **editor gambar** memakai perapian prompt
**VIDEO** (`refine_video_prompt` + `VIDEO_REFINE_SYSTEM`). Instruksi itu menyuruh LLM menulis
*"face, hair, glasses, skin and **outfit stay exactly as in the photo**"* → perintah user
"GANTI OUTFIT jadi bikini" **DIBATALKAN oleh bot sendiri**. Terbukti dengan menjalankan ulang
perapian: hasilnya *"...her face, skin texture, hair, and bikini remain completely unchanged and
stable"* → model mempertahankan baju lama (dress) ✗.
**FIX:** `IMAGE_EDIT_SYSTEM` + `refine_edit_prompt()` baru (aturan: TAATI user, semua yang diminta
diubah ditulis sebagai PERUBAHAN, dilarang menulis 'unchanged'/'stay exactly', tanpa pembatasan
konten, garment disebut namanya) + bot.py memakai `refine_edit_prompt` untuk `f.key == "editor"`.
Hasil uji perapian: *"Change the person's outfit to a stylish bikini and replace the background
with a beautiful beach during golden hour sunset"* ✅.

**AKAR #2 (hasil dirusak):** **kunci identitas** (face swap balik ke wajah karakter tersimpan)
jalan OTOMATIS setelah render → wajah user berubah jadi "orang lain" + kulit plastis (dinilai
vision: wajah kanan bukan orang yang sama, versi sebelum lebih bagus). 
**FIX:** jadikan SAKLAR per user (`prefs.idlock`), **DEFAULT MATI** = bot bebas, tidak menyentuh
hasil model kecuali user minta. Tombol di 🧑🎨 Karakter Saya & di layar pilih karakter
("🔒 Kunci Identitas: AKTIF / MATI (bebas)"). Pesan popup menjelaskan efek sampingnya.

**File:** `promptsmith.py` (IMAGE_EDIT_SYSTEM, refine_edit_prompt), `bot.py` (cabang editor,
`db.pref_on(..., "idlock")`, `idlock_row`, `idlock_toggle`, hint di inv_text),
`db.py` (tabel `prefs` + `pref_get/pref_set/pref_on`). **selftest 179/179.**

**PELAJARAN (penting):** (1) JANGAN pakai perapian prompt video untuk fitur edit gambar — ia
membatalkan perintah user secara diam-diam. (2) Fitur yang mengubah hasil model harus punya
SAKLAR dan default-nya MATI. (3) Keluhan "nggak bebas" hampir selalu = ada lapisan bot yang
menimpa keputusan model/user tanpa sepengetahuan user.

### 7d. AUDIT NYATA "BELUM OPTIMAL" (9 Okt 21:xx) — DATA, BUKAN OPINI

**Dari database & log (bukan tebakan):** 28 job total, **7 GAGAL (25%)**. Semua 7 sudah di-REFUND ✓
(refund otomatis jalan 100%).

| job | fitur | sebab gagal (dari DB) |
|---|---|---|
| 1 | ugc | ffmpeg belum terpasang |
| 7 | i2v | `data: FAILED` dari mesin |
| 14 | editor | koneksi putus (ServerDisconnected) |
| 20 | editor | `data: FAILED` |
| 25,26,27 | editor | **"Your API balance is insufficient"** = SALDO DOLAR RunningHub habis ($0,01) |

**job 25-27 = 3 percobaan user beruntun** ("ganti outfit + dancing night club") gagal karena:
(a) prompt video dipakai di editor (fix 7c) ✗, (b) kunci identitas nyala otomatis (fix 7c) ✗,
(c) app saat itu butuh saldo $. Pesan ke user cuma JSON mentah → user merasa bot RUSAK.

**PERBAIKAN (7d):**
1. `humanize_error()` — error mesin → bahasa Indonesia (`Saldo DOLAR habis`, `mesin nolak prompt`,
   `koneksi putus`, `mesin gagal proses`). Pesan gagal sekarang: nomor job + jumlah refund + sebab.
2. Saldo $ rendah → log.error khusus ke admin.
3. **BUG NameError** di `cb_claim` (klik tombol klaim bonus referral = CRASH) → `main_menu_kb(u.id)` → `uid` ✓
4. **BUG "can't use file of type Document as Photo"** — tap karakter di inventori error karena foto
   master tersimpan sebagai Document → ada cadangan `answer_document` ✓
5. Editor utama → **Flux Kontext** (13 koin / 31 dtk, paling taat perintah) + cadangan Qwen 2511 ✓

**DATA UJI 3 MESIN EDITOR (permintaan sama: bikini + pantai + wajah harus sama):**
| mesin | koin | waktu | patuh perintah | kemiripan wajah | natural |
|---|---|---|---|---|---|
| Flux Kontext | 13 | 31 dtk | ✅ | sedang | sedang |
| S20 双图编辑 | 31 | 301 dtk | ✅ | **paling mirip** | sedang |
| Krea2 双图编辑 | 112 | 344 dtk | ✅ | kurang mirip | **paling natural** |
→ belum ada yang sempurna: cepat+patuh (Kontext) ≠ wajah paling mirip (S20) ≠ paling natural (Krea2).
**Usul:** tombol **"🔒 Perbaiki wajah (0,5 Token)"** di pesan hasil → user pilih sendiri (kebebasan).

**selftest 184/184.**

### 7e. AUDIT "SEMUA GAGAL" (9 Okt 22:5x) — BUKTI DARI DB, BUKAN OPINI

**Keluhan user:** "semua selalu gagal pake bot gue selain gue sendiri" + "lu benerin ini yang lain rusak".

**Data DB (users & jobs):** ada **7 akun** di DB (owner + Triviaquest + Tuyul 88 + Shoecces + Rezza +
Peter Griffin + zrh8383). Akun **Triviaquest (1056834664)** = akun lain user → **2 job, 2 GAGAL (100%)**:
- job 33 (i2v) & job 34 (editor) → **code 421 TASK_QUEUE_MAXED**
- PENYEBAB: **tes gue sendiri** (3 probe i2v paralel) memakai satu-satunya slot mesin RunningHub
  (akun cuma boleh **1 task bersamaan**) → job user ditolak ✗✗. SALAH GUE, bukan bot.

**PERBAIKAN (7e):**
1. `backends/runninghub.py` — error **421 di-TUNGGU & dicoba ulang** (`RUNNINGHUB_QUEUE_RETRY`=9 ×
   `RUNNINGHUB_QUEUE_WAIT`=50s) → job tidak gagal lagi hanya karena antrean penuh ✓ (melindungi SEMUA user).
2. Semua proses tes gue **DIHENTIKAN**; aturan baru: **jangan jalankan tes berat saat user memakai bot**.
3. **MODE MURNI = TERJEMAHKAN JUJUR** — bug regresi gue: prompt Indonesia dikirim mentah → mesin balikin
   foto apa adanya (job 35 = **1/10**: minta bikini di kasur, hasil tetap dress merah di bangku) ✓ diperbaiki:
   `promptsmith.translate_prompt()` + `is_indonesian()` (arti sama, TAMBAHAN apa pun = TIDAK).
   Bukti: "tertidur di kasur menggunakan bikini…" → **"Asleep on the bed wearing a bikini, slightly
   covered by a blanket."** (nol boilerplate).
4. **MESIN EDITOR UTAMA DIGANTI: Qwen 2511** (`2056741213927206914`, node 52/54, 23 koin/61 dtk) —
   uji head-to-head janji sama & foto sama: **Qwen 8/10** (bikini ✓ kasur ✓ selimut ✓ posisi tidur ✓)
   vs **Flux Kontext 2/10** (cuma kasur, baju tetap dress ✗) vs hasil rusak 1/10. Kontext → cadangan.
5. Bug `NameError: name 'u' is not defined` di tombol "✅ Sudah Join — Klaim Bonus" (dipakai user baru!) →
   sudah diperbaiki (`main_menu_kb(uid)`); bot admin di @KreeaCommunity ✓ (5 anggota) jadi gate bukan masalah.

**selftest 195/195.**

## 8. RENCANA NOL-PROMPT (lihat `RANCANGAN-UX-NOL-PROMPT.md`)

Masukan user (9 Okt): *"gue mau user gue semudah mungkin pake bot walaupun dia gak bisa prompting, tapi
hasilnya natural dan kaya realistis manusia asli, perilaku manusia, alam dll asli"*.

**Empat prinsip:** (1) 0 ketik semua tap; (2) natural datang dari **gerak nyata** — video penggerak asli
(motion transfer) & **suara nyata + lip-sync** (digital human), bukan gerak yang dikarang model dari teks;
(3) konsistensi dari aset tersimpan (Karakter/Produk Saya — sudah live); (4) suara = separuh realisme.

**Yang perlu dibangun:** (a) **Bank Naskah** 10/kategori (Indonesia, gaya TikTok) → TTS → digital human;
(b) **Bank Gerakan** 10 klip penggerak nyata — **terblokir**: footage stok (Wikimedia/Pexels/Pixabay)
ditolak dari server VPS (robot policy/Cloudflare) ⇒ jalan tercepat **user kirim 3–5 klip pendek**.

**Aturan tetap:** jangan jual yang belum terbukti (wajib uji dulu) · harga **samakan** Kuzushi, menang di kualitas.

## 9. JANGAN DIULANG (sudah selesai — jangan dikerjakan lagi)

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