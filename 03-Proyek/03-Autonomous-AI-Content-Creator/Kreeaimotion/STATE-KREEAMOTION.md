# KREE.AI MOTION — KARTU PROYEK (STATE)

> **BACA FILE INI PERTAMA** di setiap sesi baru (termasuk setelah `/new`).
> Diperbarui tiap milestone + langsung di-commit/push. Ini yang menjaga konteks antar-sesi.
> ⚠️ TIDAK BOLEH memuat rahasia — hanya LOKASI kredensial.

---

## 0. ⭐ STATUS TERKINI — 10 Okt 2026, 19:54 WIB (BACA INI DULU; bagian di bawah = riwayat)

### Bot LIVE: **Kreeaimotion** — `@kreeaimotionbot` (id 8787755168)
- Kode: `/root/projects/kreeaimotion` (repo git lokal, **belum ada remote GitHub**)
- Service: `kreeaimotion` · Log: `/var/log/kreeaimotion.log` · DB: `kreeaimotion.sqlite3`
- **Rename 10 Okt 19:54 WIB**: `motionbot` → `kreeaimotion` (folder, unit systemd, file DB, log, teks bot).
  Environment `MOTIONBOT_*` **sengaja tidak diubah** (internal, tidak terlihat user).
- Proyek **BERSIH dari kreaibot** (arahan user: jangan pakai kode kreaibot untuk fitur).
- Flow sengaja **identik dengan pembanding `@motioncontrolpro_bot`**.

### Alur user (LIVE)
```
🎬 Generate Motion Control
   ↓ (langsung: daftar harga + "kirim FOTO Karakter")
🖼️ FOTO  →  🎥 VIDEO / LINK (TikTok · IG · FB · YT · X · Threads · Douyin)
   ↓ (bot hitung durasi sendiri → HARGA OTOMATIS muncul)
✅ Konfirmasi → Mulai Generate
```
- **Pilihan 10/15/20 dtk di depan DIHAPUS** — harga 100% otomatis dari panjang video.
  Efek: **tidak mungkin kelebihan bayar** (dulu: pilih 20 dtk + video 8 dtk = kena 2 credit).

| video user | tarif | cap frame | harga (placeholder) | render nyata (taskCostTime) |
|---|---|---|---|---|
| ≤ 10 dtk | `t10` | 161 | 1 cr | 4,4 menit |
| 11–15 dtk | `t15` | 240 | 1,5 cr | ± 6 menit |
| 16–20 dtk | `t20` | 320 | 2 cr | 8,4–9,6 menit |
| **> 20 dtk** | **2 pilihan** | potong 20 dtk (2 cr) **atau** "sesuai video" (4 cr, cap = durasi×16+8, maks 60 dtk) | 47 dtk = 19,1 menit |

> Harga final = keputusan user (masih placeholder di `.env`). Aturan user: **"harga tentuin nanti kalo bot nya udah bener-bener maksimal"**.

### Yang SUDAH terbukti (jangan diragukan lagi)
- **Suara selalu ada**: audio referensi dipertahankan + `ensure_audio()` sebagai jaring pengaman
  (hasil bisu ≤ -60 dB → ditempel audio referensi). Terbukti pada file user sendiri.
- **Durasi tidak terpotong**: cap frame diatur di NODE WORKFLOW (`frame_load_cap`), bukan di kode.
- **Link**: TikTok (selalu OK — **kalau dibatasi usia/audiens otomatis lewat jalur cadangan API tikwm**,
  user tidak perlu login) · Instagram (4/4 reel) · **Facebook publik 5/6 = 83%** ·
  **Facebook terkunci = ~100% setelah cookie** · YouTube/X/Threads/Douyin.
  Format FB `/share/r/...` juga jalan. Rantai penuh dari link FB terbukti sampai hasil jadi.
- **Pesan error WAJIB sesuai situsnya**: pernah kejadian user kirim link TikTok tapi pesannya
  menyebut Facebook (template lama) → sudah dibetulkan jadi sadar-situs (`friendly_error(msg, url)`).
- **Hasil**: 464×832 · 16 fps · **orientasi mengikuti video referensi** (menu 16:9/9:16 dibuang) · 2–13 MB.
- **Audio FB bisa pelan** (mis. -16,7 dB) → diteruskan apa adanya (bukan bug).

### Progres UX (LIVE 10 Okt 20:53 WIB)
```
🟢 SEDANG MEMPROSES MOTION CONTROL…

🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜  *50%*  _(± perkiraan)_

⠹ 🟩 🎬 Merender di mesin cloud
🟩 Sudah berjalan: 2 mnt 38 dtk
🟩 Perkiraan sisa: ± 4 mnt (total ± 6 mnt)
🟩 📦 Paket: 15 detik (1,5 credit)
⬜ 🆔 ID Tugas: 2108896497959768065
```
- **hijau = sudah jalan, abu = belum**, spinner `⠋⠙⠹…` muter tiap 30 dtk (Telegram tidak punya warna teks → pakai emoji kotak).
- Edit pesan tiap 30 dtk; pesan "📤 mengunggah…" diubah jadi pesan progres yang sama (tidak spam).
- Estimasi: `sec_per_frame = 1,62` · selalu dilabeli **"(± perkiraan)"** — tidak membohongi user.
- Tahap yang ditampilkan: `⬜ Menunggu giliran mesin cloud` → `🟩 Merender di mesin cloud`.

### ⭐ Ketahanan restart (fitur penting)
- `_adopt_job()`: kalau bot restart saat render jalan, task RunningHub yang **sudah ada diadopsi**
  (dipantau lanjut + hasil tetap dikirim) — **tidak render ulang = coin user tidak kebuang**.
- Job yang belum sempat submit → ditandai gagal + **credit otomatis dikembalikan**.
- ⚠️ Sebelum restart/update tetap cek: `SELECT id,state FROM jobs WHERE state IN ('new','queued','running')`.

### Cookie Facebook
- Lokasi: `secrets/fb_cookies.txt` (mode 600, folder 700, **di luar git**). **Isi JANGAN pernah ditampilkan.**
- Saklar: `tools/install_cookies.sh --aktif` · `--off` (file tetap) · `--hapus` · atau `install_cookies.sh /path/cookies.txt`.
- Umur sesi: cookie `xs` s/d **2027-10-10** (`fr` 2027-01-08). Kalau FB minta login lagi → export ulang.
- ⚠️ Dipakai dari IP server → FB bisa minta verifikasi & **mengeluarkan sesi login di HP user**.
  Saran yang sudah disampaikan: pakai **akun FB kedua**.

### Intel pembanding `@motioncontrolpro_bot`
- Backend = **RunningHub** (PROVEN: URL output di bucket `rh-hk-images-1252422369.cos.ap-hongkong.myqcloud.com`
  + `PropagateID RH_…`). Model = keluarga **Wan Animate**.
- Output HD mereka: **1072×1920 · 24 fps · 505 frame · 21,04 dtk · 65,5 MB · render 28 MENIT** (15:55→16:23 WIB).
  File >50 MB **tidak dikirim sebagai video Telegram** — mereka kasih **link 24 jam**.
  (Bot Telegram biasa dibatasi 50 MB upload; bot kita belum pernah kena karena hasil kita 2–13 MB.)
- Punya kita: **3–10× lebih cepat per detik output**, dan **menurut user lebih realistis**.
  Resolusi kita lebih kecil (464×832 vs 1072×1920) — trade-off yang user terima.
  **Tingkatan HD DITOLAK dulu** ("gua lebih puas sama hasil bot kita").

### Angka penting
- Saldo user (owner, id 8886993492): **17,5 credit** (10 Okt 20:53 WIB).
- Coin RunningHub: **25.222** (cek 10 Okt) — turun ~1.543 untuk ±7 render uji.
- RAM server 1,9 GB (aman; render berat di mesin RH, bukan di VPS).

### 🎁 Referral (SELESAI 12 Okt 2026) — anti-farming
- Bonus **2,5 : 2,5** (pengundang & yang diundang). Link `?start=ref_<id>` + menu **🎁 Kode Referral**.
- **5 lapis pengaman**: (1) `referrals.invitee_id` PRIMARY KEY → 1 akun = 1 bonus seumur hidup;
  (2) pengundang wajib user terdaftar + self-referral ditolak (dijaga di lapisan DB **dan** bot);
  (3) cap 10/hari & 30/30hari → kelebihan DITAHAN, tidak hilang; (4) bonus pengundang cair
  **setelah invitee selesai render pertama** (mode aman, `MOTIONBOT_REF_INVITER_AFTER_RENDER=1`);
  (5) gate channel komunitas (opsional, aktif setelah bot jadi ADMIN).
- Admin: `/refstats` · `/refbayar <invitee_id>`. Uji: `tools/ref_selftest.py` (21),
  `tools/ref_e2e.py` (11), `tools/ref_route.py` (8, lewat Dispatcher aiogram asli),
  `tools/ref_gate.py` (12, gate channel) = **52 lulus**.
- ✅ **Gate channel AKTIF (12 Okt 2026)**: `@kreeaimotionbot` sudah jadi **administrator** di
  `@KreeaCommunity` (nama tampilan channel = **Kreeativ Community**, 7 subscriber) — ditambahkan
  lewat otomasi GUI Telegram Desktop (xdotool+OCR, resep di skill `telegram-desktop-gui-automation`).
  Terverifikasi dari sisi Bot API: `get_chat_member` → bot `administrator`, user `creator`,
  non-member → BadRequest "member not found" (ditangkap kode = "belum join").
  `MOTIONBOT_CHANNEL=KreeaCommunity`.

### Pending / next
0. **Character sheet (hasil riset 12 Okt)** → baca `RISET-CHARACTER-SHEET.md` + `prompt-sheet-3view.txt`.
   Terbukti: workflow sheet publik jalan via API kita (50 & 56 koin, ±53 koin ≈ Rp 235), hasil 1344×768
   rapi. Arsitektur: sheet 3-view → potong per view → pilih otomatis sesuai framing video pemandu
   → kirim potongan (BUKAN sheet utuh) ke `LoadImage #55`. Sudah ada bukti di `bukti/`.
0b. **REALISME (bab 8 & 10 dokumen itu)** — sudah diuji di akun RH (24,1rb koin):
   - Upgrade kualitas TERBUKTI: bf16 + 720×1280 + 6 step = **+34% ketajaman**, biaya 1,61×
     (365 koin / 925 dtk vs 226 / 575). Caranya: override `#94 model`, `#84 width/height`, `#70 steps`.
   - **Modul baru `tools/iphone_look.py`** (sudah commit): naik-res 1080p + tajam + butir sensor +
     warna + vignette, preset ringan/standar/kuat, 0 koin, ±4,7× durasi klip. Ukur: +14–19% tajam,
     +1,88× butir.
   - **Telegram mengompres foto user** (terbukti: semua foto masuk 1280 px / ±95 KB; aslinya
     3000×4000) → bot HARUS menyuruh kirim foto sebagai **FILE/dokumen**.
   - Workflow "skin texture" RH = penghalus kulit (3–4/10), TIDAK bisa menciptakan pori.
   - `bg_images`/`mask`/`face_images` kita KOSONG (sebab latar belakang dihalusinasi); workflow
     publik `1973232104739835906` tersambung lengkap tapi output-nya `save_output=False` di dalam
     grup → tak bisa diambil lewat API. Perlu fork ke akun kita + pakai editor RH.
1. **Harga final** tingkatan (tunggu user; placeholder 1 / 1,5 / 2 / 4 cr).
2. **Proxy rotate** untuk downloader (jaga rate-limit IP VPS kalau banyak user kirim link beruntun).
3. Top-up / pembayaran (belum digarap; rencana ikut pola kreaibot = Aulaa QRIS).
4. Kalau nanti mau HD: workflow berat sudah tersedia (Wan 2.2 Animate V7) — user belum mau.

---

## 1. Lokasi kredensial — ⚠️ HANYA LOKASI, JANGAN NILAI
- Token bot Telegram: `.env` (`MOTIONBOT_TOKEN`)
- RunningHub API key + upload key: `.env`
- Cookie Facebook: `secrets/fb_cookies.txt` (isi = rahasia penuh akun FB)
- DB & folder kerja: `MOTIONBOT_DB`, `MOTIONBOT_WORK`
- Login RunningHub (browser): Hermes browser vault

## 2. Detail teknis penting
- Durasi = `frame_load_cap` di node workflow (binding `MOTIONBOT_T10_CAP=2:frame_load_cap:161` dst).
- Workflow dipakai: `2106585458498420737` (10 dtk, dipakai berulang untuk semua tingkatan + full).
- `instanceType=plus` untuk task berat (menyelesaikan `torch.OutOfMemoryError`).
- Downloader = modul **yt-dlp** (+ fallback CLI), 4 bentuk URL FB (www/m/mbasic/plugin/embed),
  nama file unik (uuid) → aman multi-user paralel.
- Multi-user: maks 1 job aktif/user, janitor hapus file > 3 hari + cek disk.

## KARAKTER SAYA (LIVE 12 Okt 2026)
- Menu **🧑 Karakter Saya** di bot: bikin sheet (cukup **foto biasa**, tak wajib FILE) → sheet 3-view
  **full-body** (depan·samping·belakang) + crop wajah dari foto ASLI → kasih nama → tersimpan.
- **Kenapa bisa "dibaca bot"**: sheet dipotong **deterministik** (bukan deteksi AI) → file per view
  disimpan di kolom `views_json`; `tools/sheet.py:pick_view()` yang menentukan file mana dipakai.
  Terbukti: potongan panel jatuh di ruang kosong antar figur (vision: "no character is split").
- Prompt penentu full-body ada di node **#97** (`prompt`) workflow `1962303327478464513`;
  tanpa prompt itu hasilnya kepotong di paha. Biaya 1× sheet ≈ 50 koin ≈ Rp 220 (~90 dtk).
- Crop wajah: **deteksi wajah OpenCV** (frontal+profil + verifikasi MATA untuk buang deteksi palsu di badan) dengan cadangan heuristik (foto badan penuh → wajah di bagian atas). Kotak dirapatkan 1,35× agar pori-pori terlihat.
- BUG yang sudah dibasmi (12 Okt): handler bukti-bayar `@router.message(F.photo)` tanpa `StateFilter(None)` didaftarkan paling awal & memanggil `step_photo()` untuk state APA PUN → foto di alur Karakter kebajak jadi alur motion. Sekarang filter ketiga handler foto saling eksklusif + ada jaring pengaman "mau dipakai untuk apa?".
- Di alur Generate, tombol **🧑 Pakai: <nama>** memakai view DEPAN & menyalin filenya ke work_dir
  (aman walau karakter dihapus) → lanjut seperti biasa (kirim video).
- Uji: `char_hub`/`char_new`/`char_step_name`/`char_pick_kb`/`char_use` semua lulus harness handler;
  8 handler karakter terdaftar; service `kreeaimotion` sudah restart.
- BELUM: mode Realistis belum di-wire ke worker (mesin `tools/realism.py` masih dipanggil manual).

## PROPORSI TUBUH (temuan 12 Okt 2026)
- **Masalah nyata**: prompt sheet lama menghasilkan figur **6,5–7 kepala** dengan kepala kegedean,
  kaki pendek, torso panjang, panggul lebar/bahu sempit (jurnal penilai visual).
- **Obatnya (TERBUKTI)**: tambahkan ke prompt — `natural adult human body proportions, about 7.5
  heads tall, correct leg-to-torso ratio, natural hip-to-waist ratio, realistic anatomy` dan ke
  negatif — `chibi, doll-like proportions, oversized head, short legs, long torso, deformed anatomy`.
  Hasil v3 vs v2 (1 run nyata, 50 koin): **~7,5 kepala**, kepala lebih kecil, kaki lebih panjang,
  bahu lebih seimbang.
- **v4 (final, terbukti)**: tambah `natural hip-to-waist ratio` → tetap 7,5 kepala, **pinggang tak
  lagi terjepit**, panggul lebih penuh, **tangan lebih rapat ke badan** (pose netral), sebaran skala
  antar-view turun 1,2% → **0,7%**. Penilai visual: "v4 decisively the better reference — v3's
  stylized waist/hip and floating arms can cause warping/morphing saat bergerak". KONFIG FINAL = v4.
- **Seberapa "digarap model"**: foto *selfie* (bukan seluruh badan) → bagian bawah tubuh **tidak ada
  di foto** → memang DIKARANG model. Karena itu tip di bot: foto seluruh badan (kepala–kaki) =
  proporsi lebih mirip aslinya. Ini informasi, bukan syarat (user tak mau ada gerbang FILE).
- **Skala antar-view sheet sudah konsisten** di v2/v3 (tinggi figur 730/729/721 & 738/734/729 px,
  sebaran ~1,2%) → tak perlu normalisasi panel.
- **Pengukur otomatis proporsi: JANGAN dipercaya.** Deteksi "garis bahu" dan "garis pisah kaki"
  dua-duanya salah pada figur ini (kaki rapat → pisah tak terdeteksi; bahu terdeteksi terlalu
  rendah). Oracle yang sahih = **penilai visual** (hitungan "berapa kepala"). Jangan bangun fitur
  dari siluet mentah tanpa verifikasi mata.
- Di tahap render, bentuk tubuh hasil lebih banyak mengikuti **video pemandu** (+ acuan karakter),
  jadi pilih video yang orangnya sepadan; rasio aspek acuan vs video juga berpengaruh.
