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

### Pending / next
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