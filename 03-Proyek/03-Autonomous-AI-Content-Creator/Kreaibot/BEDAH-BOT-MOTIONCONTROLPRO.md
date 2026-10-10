# BEDAH BOT @motioncontrolpro_bot — fokus MOTION GRAFIS
> Riset 10 Okt 2026, via Telegram Desktop headless (Xvfb :99) + probe RH API. Akun: Nimara Official.
> ⚠️ Tanpa kredensial apa pun yang ditampilkan. Semua angka di bawah = hasil observasi langsung.

## 1. IDENTITAS BOT
- Username: `@motioncontrolpro_bot` · Nama tampilan: **motioncontrolpro** (bahasa UI: Indonesia)
- Bio/deskripsi profil kosong (bio default Telegram) → tidak ada link website
- Bot publik, ada **1 grup yang sama** dengan akun kita
- Nama bot = fitur utamanya: **Motion Control (MC)** = memindahkan gerakan dari video referensi ke foto karakter

## 2. MENU UTAMA (tombol inline dari /start)
```
🎬 Generate Motion     🎬 Generate Video
🖼️ Generate Gambar
🚀 Langganan Unlimited  🎁 Kode Referral
💳 Saldo Credit        💰 Top Up Credit
```

## 3. DAFTAR FITUR + HARGA (credit) — disalin apa adanya dari bot
| Fitur | Harga | Dugaan backend di RunningHub |
|---|---|---|
| ⚡ Standard S1 | 1 credit | Wan / model video murah |
| ⚡ Standard Fast | 1 credit | Wan turbo |
| 🎬 **MC 16:9 (landscape)** | **1 credit** | **Motion Control** (Kling v2.6 Std / Wan ATI) |
| ⚡ Standard HD | 1.5 credit | Wan HD |
| 💎 Pro | 2 credit | Kling v2.6 Pro / Wan Pro |
| 🎥 Image to Video | 1 credit | Wan i2v |
| 🎥 Lipsync Video | 2 credit | lip-sync (SadTalker/Wav2Lip/Hedra) |
| 🔥 **MiniMax H3 UltraHD** | **2 credit** | **MiniMax Hailuo H3** (model berbayar RH) |
| 👕 Ganti Fashion | 0.2 credit | Qwen-Image-Edit / CatVTON |
| 🪄 Upscale & Retouch Gambar | 0.2 credit | Upscale (ESRGAN dkk) |
| 🖼️ Qwen Image 2.1 | 0.2 credit | Qwen-Image |
| 🎬 Grok Imagine Video | 7 credit | Grok Imagine (API pihak ketiga, mahal) |
| 🤯 GPT Image 2.5 Flare | 0.2 credit | gpt-image (OpenAI) |

**Catatan penting:** setiap nama model di daftar ini (MiniMax H3, Qwen Image, GPT Image, Grok Imagine,
Lipsync, Ganti Fashion) = **model yang memang ada di RunningHub** → hampir pasti bot ini adalah
**wrapper RunningHub API**. Ini kabar bagus: user sudah punya akun + API key RH.

## 4. HARGA TOP-UP (langsung dari bot — paket yang muncul setelah pilih Top Up)
```
6 credit   - Rp.5.000     → Rp833 / credit
16 credit  - Rp.10.000    → Rp625 / credit
50 credit  - Rp.25.000    → Rp500 / credit
110 credit - Rp.50.000    → Rp455 / credit
```
**Harga jual per generate (paket terkecil → terbesar):**
- MC 16:9 (1 credit) = **Rp 455 – Rp 833**
- MiniMax H3 UltraHD / Pro (2 credit) = **Rp 910 – Rp 1.666**
- Grok Imagine Video (7 credit) = **Rp 3.185 – Rp 5.831**

## 5. ALUR PEMBAYARAN (kebongkar penuh)
```
📦 Paket 16 Credit   Harga Rp.10.000

Cara top up:
1. Transfer/scan QRIS sesuai harga di atas
2. Kirim foto/screenshot bukti bayar langsung di chat ini
3. Admin akan mengecek, lalu credit masuk otomatis ke saldo kamu

📥 Silakan kirim bukti transfer sekarang.
```
Tombol: `❌ Batalkan Order` · `📦 Lihat Paket Lain` · `⬅️ Kembali ke Menu Utama`

- Gambar QR = **QRIS statis nasional** (GPN, "SATU QRIS UNTUK SEMUA", ID merchant tercetak, ASPI, diawasi BI)
- Jadi: **tanpa payment gateway, tanpa fee** → QRIS statis + verifikasi bukti transfer oleh admin.
  Ini kunci margin: tidak ada potongan 0,7–2,5% seperti gateway.
- `💳 Saldo Credit` menampilkan: `Saldo X credit` + `Unlimited ❌ Belum langganan` + daftar harga.

## 6. PERILAKU SAAT SALDO 0 (penting untuk UX bot tiruan)
- Mengetik sembarang teks / nama menu saat saldo 0 → bot **menahan alur generate** dan mendorong top-up.
  ("Saldo credit kamu masih kosong. Top up dulu lewat menu 💰 Top Up Credit, atau ambil 🚀 Langganan Unlimited")
- Artinya **fitur generate baru bisa dibedah setelah ada credit** → user melakukan top-up untuk membuka alur lengkap.
- Ada indikasi langganan **"Unlimited"** (generate Motion Control & MiniMax H3 UltraHD tanpa batas) — harga langganan belum terbaca.

## 7. BACKEND MOTION CONTROL DI RUNNINGHUB (terverifikasi lewat API RH)
Pencarian `Motion Control` di RunningHub mengembalikan **9 workflow**, antara lain:
| workflowId | nama |
|---|---|
| 2057856312750465025 | wan motion control |
| 2055806978252918785 | wan_ati_motion_control + Full Node Comments |
| 2033808877589897217 | Kling_V30ProMotionControl_v3.0 |
| 2033808723172397057 | Kling_V26ProMotionControl_v2.6 |
| 2033808851971088386 | Kling_V26StdMotionControl_v2.6 |
| 2033748217984192513 | Kling_26_MotionControl_v2.6 |
| 2016763198224994306 | Kling v2.6 Motion Control |
| 2039168673016975361 / 2018215664321830914 | 可灵 v2.6 Motion Control |

Plus `Lipsync` (1 hasil) dan `Qwen Image` (10 hasil) → seluruh katalog bot punya padanan di RH.

## 8. EKONOMI UNIT (hitung kasar, perlu verifikasi harga node RH)
- **Motion Control (1 credit = Rp455–833)**: hanya untung kalau backend **Wan ATI / Wan motion control**
  (open-source, biaya RH rendah). Kalau pakai **Kling v2.6** (¥3–5 sekali run ≈ Rp7.000–11.000) → **RUGI**.
  → Untuk bot tiruan: pakai jalur **Wan ATI Motion Control**, bukan Kling.
- **MiniMax H3 (2 credit = Rp910–1.666)**: RH H3 = **480p ¥0.10/s · 768p ¥0.20/s · 1080p ¥0.42/s**.
  Klip 6 detik 1080p ≈ ¥2.5 ≈ Rp5.700 → **rugi** kalau tidak ada trik. TRIK-nya: **member RH gratis H3
  pukul 21.00–10.00** → di jam itu biaya ≈ 0, margin ≈ 100%.
- **Model gambar 0.2 credit (Rp91–167)**: Qwen-Image di RH ≈ 18 koin/run (murah) → margin sehat.
- **Grok Imagine 7 credit (Rp3.185–5.831)**: tier "penutup biaya API mahal" → jangan dijadikan andalan.

## 9. BLUEPRINT BOT MOTION GRAFIS TIRUAN (untuk kreaibot/Webuild)
Arsitektur: `aiogram (Telegram) → worker → RunningHub API → kirim video balik`
1. **Menu sama persis**: Motion (MC 16:9 / 9:16), Video (Fast/HD/Pro), Gambar, Lipsync, Saldo, Top Up.
2. **Alur Motion Control**: user kirim **1 foto (karakter) + 1 video referensi gerakan** → bot jalankan
   workflow `wan_ati_motion_control` (bukan Kling) → output 16:9 → kirim sebagai video.
3. **Credit ledger** di SQLite (kolom: user_id, delta, alasan, ts); cek saldo sebelum tiap job.
4. **Top up**: QRIS statis sendiri + user kirim bukti → admin (user) approve via command → credit masuk.
   Alternatif otomatis: gateway QRIS (Aulaa — sudah dipakai kreaibot).
5. **Anti-abuse**: queue + limit 1 job/user, cek durasi video referensi (maks 5–10 dtk), tolak file >20 MB.
6. **Chat list Telegram Desktop** (tempat evidence kalau perlu): bot berbalas cepat, jadi ubah `send.py`
   untuk menyadap balasan bot saat debugging.

## 10. ALUR MOTION CONTROL — TERVERIFIKASI LANGKAH DEMI LANGKAH (10 Okt, saldo 16 credit)
Semua di bawah ini hasil jalan nyata di bot (bukan dugaan):

**Langkah 0** — tombol reply-keyboard `🎬 Generate Motion Control`

**Langkah 1 — pilih model**
```
🎬 Generate Motion Control
Saldo credit kamu: 16
Pilih model yang mau dipakai:
[⚡ Standard S1 (1 credit)] [🚀 Standard Fast (1 credit)]
[🖥️ MC 16:9 (landscape) (1 credit)]
[⚡ Standard HD (1.5 credit)] [💎 Pro (2 credit)]
[❌ Batal]
```

**Langkah 2 — minta foto karakter**
```
✅ Model: 🖥️ MC 16:9 (landscape) (1 credit)

Sekarang kirim foto Karakter.

Ketik /batal untuk membatalkan.
```

**Langkah 3 — minta video referensi gerakan**
```
✅ Foto diterima.

Sekarang kirim video referensi, atau kirim link TikTok (bot akan download otomatis).
```

**Langkah 4 — konfirmasi (credit BELUM dipotong sampai di sini)**
```
✅ Foto & video sudah siap.
Model: 🖥️ MC 16:9 (landscape) (1 credit)
Lanjut proses generate sekarang?
[✅ Mulai Generate]  [❌ Batal]
```

**Langkah 5 — HASIL (terekam)**
Bot mengirim **video hasil** dengan caption:
```
✅ Motion control selesai!
```
- Waktu: konfirmasi 1:41 PM → hasil **1:56 PM** (≈15 menit; **TIDAK ada pesan "sedang diproses"/antrean** —
  bot diam lalu kirim hasil. Ini celah UX yang bisa dikalahkan bot tiruan.)
- File: **1920×1072 (16:9)**, durasi **3,77 dtk**, h264 + **AAC audio**, 1,6 MB (113 frame video, 163 frame audio)
- Diverifikasi: antar-frame beda **32–47** → gerakan nyata (bukan gambar diam); frame-0 vs foto input beda **70** → benar-benar di-render ulang
- Output menyertakan **audio track** (mewarisi audio dari video referensi) → konsisten dengan pipeline
  motion-transfer ber-audio (Wan ATI / Wan Animate / Kling Motion Control)
- **Saldo: 16 → 15 credit = tepat 1 credit** sesuai label model ✓
- File bukti disimpan: `work/rh_bot_probe/mc_output_16-9.mp4` + `fr_0.png`, `fr_3.5.png`

### 📌 Ringkasan ekonomi fitur Motion Control (data nyata)
| Item | Nilai |
|---|---|
| Harga jual | 1 credit = **Rp455–833** |
| Output | 1920×1072, ~3,8 dtk, ada audio |
| Waktu proses | beberapa menit s/d ~15 menit, **tanpa progress bar** |
| Peluang bot tiruan | (a) tampilkan status antrean + ETA, (b) output rasio 9:16 juga, (c) durasi lebih panjang |

## 11. JEBAKAN TEKNIS (wajib ditiru kalau bikin bot sendiri)
1. **Video referensi HARUS video asli (punya audio track).** mp4 senyap 4 detik dikirim Telegram
   sebagai **animasi/GIF** (`message.animation`) → **bot DIAM TOTAL** (tidak merespons). Setelah
   ditambah audio AAC senyap (`anullsrc`), langsung diproses. Artinya handler bot cek `message.video`,
   bukan `message.animation`. → Di bot tiruan: **tolak animasi**, atau konversi sendiri.
2. **Bot menerima LINK TikTok dan mengunduh videonya sendiri** — ini fitur UX terkuatnya:
   user cukup paste link (tidak perlu simpan video). Perlu implementasi downloader di bot tiruan.
3. Command batal = **`/batal`**; ada juga tombol `❌ Batal`.
4. Credit **hanya** dipotong di langkah 4 (setelah ada foto + video), bukan saat pilih model.
5. Bot **mem-pause alur generate saat saldo 0** dan mendorong top-up.
6. Ada kartu data user (`Motion Control Bot · Data Keterangan · Username · Status AKTIF`) — indikasi
   panel admin di dalam bot.

## 12. CATATAN TEKNIS SESI (biar tidak mengulang kerja)
- Telegram Desktop di VPS: akun **sudah login di tdata** → TIDAK perlu QR. Launch:
  `Xvfb :99` → `openbox` → `DISPLAY=:99 DBUS_SESSION_BUS_ADDRESS=disabled: LIBGL_ALWAYS_SOFTWARE=1 /opt/telegram/Telegram`
- **Input ke Qt WAJIB XTEST**: `xdotool windowactivate` + `xdotool key/type` **TANPA** flag `--window`
  (dengan `--window` = XSendEvent → Qt mengabaikan).
- **Window minimal 1270×780**; kotak pesan ada di **y≈762** (klik lalu ketik). Kotak pencarian: `ctrl+f` lalu ketik.
- OCR (`tesseract tsv` via helper `/root/.hermes/cache/scratch/tg.py`) memberi **koordinat pixel akurat**;
  vision dipakai untuk transkripsi penuh (tesseract sering pecah di teks kecil).
- `scrot` menyimpan screenshot penuh 1280×800; crop chat = `x 280–1275, y 55–760`.