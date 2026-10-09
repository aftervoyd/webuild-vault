# TEARDOWN KUZUSHI (@KuzushiGenBot) — 9 Okt 2026

> Hasil eksplorasi langsung via Telegram Desktop headless di VPS (akun user, User ID 8886993492).
> Tujuan: contek fitur & harga mereka → implement di KREE.AI.
> Saldo saat eksplorasi: **13.6 → 12.6 Token** (12.6 = sisa setelah render 10s milik user).

---

## 1. MENU UTAMA (persis, urutan baris)

Header pesan: `AI STUDIO BOT` · `Pengguna: <nama>` · `Saldo Token: x` · `Total Komunitas: 2,781 Member`

| # | Tombol | Harga |
|---|---|---|
| 1 | 🎭 Face Swap & Motion Video | 2 Token |
| 2 | 🎬 Image to Video | 0.5–2 Token |
| 3 | 🖌️ AI Image Editor | 0.3 Token |
| 4 | 🕺 Pose Transfer & Style | 0.5 Token |
| 5 | 🎤 AI Video Lip Sync | 0.5 Token |
| 6 | 🌌 Video All-in-One · Star Trail H3 | 1 Token |
| 7 | ⚡ Top Up Token (QRIS) · 👥 Program Referral (Cuan) | — |
| 8 | 👤 Profil & Saldo · 🎁 Redeem Voucher · 📘 Panduan | — |

## 2. DAFTAR HARGA RESMI (dari layar Profil & Saldo)

```
• 🎭 Face Swap Video: 2 Token
• 🖼️ Image to Video: 0.5 - 2 Token (5s=0.5, 10s=1, 15/30s=2)
• 🖌️ Image Editor: 0.3 Token
• 🕺 Pose Transfer: 0.5 Token
• 👄 Lip Sync Video: 0.5 Token
• 🌠 Star Trail H3 All-in-One: 1 Token
```

## 3. ALUR TIAP FITUR

### 🎭 Face Swap & Motion Video — 2 Token
1. Kirim **FOTO WAJAH / KARAKTER** (harus BERSIH: tanpa watermark/teks/logo, kalau tidak → watermark ikut ke video)
2. Kirim **VIDEO GERAKAN SUMBER (.mp4)**
3. Video otomatis diproses & dibalas.
Durasi disarankan 15 detik, maksimal 30 detik.
Tombol: `⬅️ Batal / Kembali`

### 🎬 AI Image to Video (Minimax / LTX 2.3) — 0.5 / 1 / 2 Token
Pesan pembuka langsung memuat tabel harga:
```
• 5 Detik 🤙 0.5 Token
• 10 Detik 🤙 1 Token
• 15 Detik [MAX] 🤙 2 Token
```
1. Kirim 1 FOTO
2. Ketik prompt deskripsi gerakan
3. **Pilih durasi (5s / 10s / 15s / 30s)** ← menurut Panduan
4. Render otomatis.
Tombol: `🔙 Batal / Kembali`

### 🖌️ AI Image Editor — 0.3 Token
1. Kirim 1 FOTO
2. Bot: `✅ Foto Diterima!` → ketik prompt/instruksi edit
   Contoh yang ditampilkan bot: `make it cyberpunk style, neon lighting, 8k` · `anime style, detailed background`
3. Foto diproses otomatis.
Tidak ada tombol inline.

### 🕺 Pose Transfer & Style — 0.5 Token
1. Kirim **FOTO UTAMA / KARAKTER** → `✅ Foto Subjek/Karakter Diterima!`
2. Kirim **FOTO REFERENSI POSE** (gambar pose tubuh/gaya yang mau ditiru)
3. (render)
Tombol: `⬅️ Batal / Kembali`

### 🎤 AI Video Lip Sync (MiniMax H3) — 0.5 Token
1. Kirim 1 **FOTO WAJAH / KARAKTER** → `✅ Foto Karakter Diterima!`
2. Kirim **FILE SUARA / LAGU (.mp3 / rekaman suara / voice note)**
3. (render)
Tombol: `⬅️ Batal / Kembali`

### 🌌 Video All-in-One · Star Trail H3 (30s) — 1 Token
1. **Langkah 1/3:** kirim 1–6 foto referensi
   - Foto 1 = Frame Awal · Foto 2 = Frame Akhir (opsional) · Foto 3–6 = elemen tambahan (opsional)
   - Balasan per foto: `✅ Foto Referensi #N Diterima! (N/6 Foto)`
   - Tombol: `✅ Lanjut Ketik Prompt (Foto Selesai)` · `❌ Batal`
2. Ketik prompt
3. (render) — judul fitur menyebut **30 detik**

## 4. TOP UP (QRIS) — paket token

```
🌑 8 Token  (Bonus 3)   - Rp 5.000
💎 15 Token (Bonus 5)   - Rp 10.000
🔥 25 Token (Bonus 5)   - Rp 20.000
🚀 58 Token (Bonus 8)   - Rp 50.000
🎉 120 Token (Bonus 20) - Rp 100.000
✏️ Top Up Nominal Custom
⬅️ Menu Utama
```
Pembayaran: GoPay, OVO, Dana, ShopeePay, BCA, Mandiri, BRI, dll.

**Token efektif:** Rp 10.000 → 15 Token (+bonus) ≈ **Rp 667/token**.

## 5. PROGRAM REFERRAL (Cuan)

Komisi per top up teman:
```
Rp 5.000   → 2 Token
Rp 10.000  → 3 Token
Rp 25.000  → 5 Token
Rp 50.000  → 15 Token
Rp 100.000 → 20 Token
```
- Link: `https://t.me/KuzushiGenBot?start=ref_<user_id>`
- Menampilkan: Total Teman Diundang · Saldo Komisi Siap Tukar (Rp) · Total Komisi
- **Social proof:** `🔥 Penukaran Terakhir: @wahyu_hidayat baru saja menukarkan 50 Token Bot`
- Tombol: `🌐 Tukar Komisi ke Token Bot` · `🔙 Menu Utama`

## 6. PROFIL & SALDO
`👤 PROFIL PENGGUNA` · `🆔 User ID` · `🪙 Saldo Token` · `📊 Total Render Bot: 2732` + Daftar Harga Layanan.
Tombol: `⚡ Top Up Token (QRIS)` · `🎁 Masukkan Kode Voucher` · `⬅️ Menu Utama`

## 7. PANDUAN (teks resmi mereka)
- Face Swap: foto wajah → video .mp4 → auto.
- Image to Video: foto → prompt → **pilih durasi (5s, 10s, 15s, 30s)** → auto render.
- Image Editor: foto → prompt (mis. `make it cyberpunk style, 8k`) → auto.
- Top Up QRIS 24 jam.

---

## 8. PERBANDINGAN KREEAIBOT vs KUZUSHI

Token KREE.AI = Rp 1.000 (10 token / Rp 10.000). Token Kuzushi ≈ Rp 667.

| Fitur | Kuzushi | Kuzushi (Rp) | KREEAIBOT sekarang | KREE (Rp) | Catatan |
|---|---|---|---|---|---|
| i2v 5s | 0.5 T | Rp 333 | 0.5 T | Rp 500 | kita 1,5× lebih mahal |
| i2v 10s | 1 T | Rp 667 | 1 T | Rp 1.000 | kita 1,5× lebih mahal |
| i2v 15s | 2 T | Rp 1.333 | — | — | **kita TIDAK jual 15s** |
| i2v 30s | 2 T | Rp 1.333 | — | — | **kita TIDAK punya** |
| All-in-One 30s | 1 T | Rp 667 | 15s = 2.5 T | Rp 2.500 | **kita 3,7× lebih mahal** |
| Image Editor | 0.3 T | Rp 200 | — | — | fitur ada di katalog, belum dijual |
| Pose Transfer | 0.5 T | Rp 333 | — | — | belum dijual |
| Lip Sync | 0.5 T | Rp 333 | — | — | belum dijual |
| Face Swap | 2 T | Rp 1.333 | — | — | belum dijual |

**Biaya produksi kita (RunningHub, terukur):** 5s = 61 koin ≈ Rp 272 · 10s = 112 koin ≈ Rp 500 · UGC 15s ≈ 269 koin ≈ Rp 1.200.

## 9. KESENJANGAN / TEMUAN PENTING

1. **Harga kita kalah di semua titik.** Token kita 1,5× lebih mahal, dan fitur unggulan mereka (All-in-One 30s = Rp 667) 3,7× lebih murah dari All-in-One 15s kita.
2. **Kita tidak punya durasi 15s & 30s i2v.** Mereka punya sampai 30s.
3. **4 fitur kita belum dijual:** Image Editor, Pose Transfer, Lip Sync, Face Swap.
4. **Referral mereka berbasis komisi rupiah per top up** (2–20 token), + social proof ("Penukaran Terakhir: ...").
5. **Social proof di menu:** "Total Komunitas: 2.781 Member", "Total Render Bot: 2732".
6. **Menu mereka 1 pesan, semua harga tampil di tombol** → user tahu harga sebelum klik.

## 10. RENCANA IMPLEMENTASI DI KREE.AI (urutan prioritas)

1. **Tampilkan harga di tombol menu** (murah, langsung, menaikkan konversi).
2. **Aktifkan AI Image Editor (0.3 T)** — backend: app image-edit RunningHub + prompt.
3. **Aktifkan Pose Transfer & Lip Sync (0.5 T)** — Lip Sync pakai workflow INFINITETALK yang sudah teridentifikasi; input audio (.mp3).
4. **Aktifkan Face Swap (2 T)** — input foto + video .mp4.
5. **Tambah durasi 30s** All-in-One + i2v (butuh app/workflow terbukti; aturan lama: jangan jual durasi yang belum terbukti).
6. **Kaji ulang harga token** (harga_10k / bonus top up) supaya tidak 1,5× lebih mahal.
7. **Referral: tambah komisi rupiah per top up + social proof**.

## 11. CATATAN TEKNIS GUI (penting untuk sesi berikutnya)

- Telegram Desktop di VPS **mati** setelah reboot; Xvfb + openbox + Telegram harus dijalankan ulang.
- **WAJIB** `libopengl0` (kalau tidak: `RHI: OpenGL library unavailable` → layar putih kosong).
- Telegram Desktop **hang ~120 detik** gara-gara panggilan DBus portal yang timeout → **jalan dengan `DBUS_SESSION_BUS_ADDRESS=disabled:`** supaya gagal cepat.
- `/tmp` adalah tmpfs 966 MB dan **pernah 100% penuh** (851 MB dari `/tmp/openclaw` hasil browsing app RunningHub) → tmpfs = RAM, jadi ini juga bikin memori sesak.
- Jendela Telegram = `0x200016` (2097174), geometri `231,68 818x642`; baris tombol menu: **y = 360, 398, 436, 474, 512, 550, 588, 626** (pitch 38), x tengah ≈ 800.