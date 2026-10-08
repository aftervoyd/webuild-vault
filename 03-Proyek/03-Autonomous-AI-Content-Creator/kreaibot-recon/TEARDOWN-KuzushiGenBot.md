---
target: "@KuzushiGenBot / Kuzushi — 'AI STUDIO BOT'"
tanggal: 2026-10-08
metode: probing via Telegram Desktop (VPS, Xvfb) + analisa file + riset web
status: TEMUAN FINAL (semua fitur terverifikasi langsung dari bot)
---

# 🔍 TEARDOWN @KuzushiGenBot — hasil probing langsung

## Identitas bot
- Nama: **Kuzushi** · username `@KuzushiGenBot` · label diri: **"🤖 AI STUDIO BOT"**
- **Bot Indonesia** (bahasa Indonesia, bayar **QRIS**, fitur "Program Referral (Cuan)")
- Skala: **2.779 member komunitas**, pernah sampai **Generate #2675** → bot matang & ramai
- Akun uji: nemora (ID 8886993492), saldo saat probe: **2.9 Token** (nggak ada token yang dibelanjakan — semua probe menu, gratis)

## 💰 Ekonomi & fitur (persis dari menu utama)

| Fitur | Harga | Model (dari bot) | Catatan |
|---|---|---|---|
| 🎭 Face Swap & Motion Video | 2.0 Token | (tidak disebut) | foto wajah bersih + video gerakan sumber (.mp4); disarankan 15 dtk, maks 30 dtk; ada peringatan watermark |
| 🎬 Image to Video | 0.5–2 Token | **MiniMax / LTX 2.3** | 5 dtk=0.5 · 10 dtk=1 · 15 dtk (MAX)=2 |
| 🖌️ AI Image Editor | 0.3 Token | (tidak disebut) | kirim 1 foto + prompt gaya (mis. "cyberpunk 8k") |
| 🕺 Pose Transfer & Style | 0.5 Token | (tidak disebut) | Langkah 1: kirim foto utama/karakter |
| 🎤 AI Video Lip Sync | 0.5 Token | **MiniMax H3** | kirim 1 foto wajah → dibuat bernyanyi/bicara |
| 🌌 Video All-in-One · Star Trail H3 | 1.0 Token | **"Star Trail H3"** (≈ MiniMax H3) | 1–6 foto: Foto1=Frame Awal, Foto2=Frame Akhir, Foto3-6=elemen; sampai 30 dtk |
| ⚡ Top Up Token | — | — | **QRIS** (payment lokal Indonesia) |
| 👥 Program Referral | — | — | "Cuan" (komisi referral) |
| 👤 Profil & Saldo · 🎁 Redeem Voucher · 📖 Panduan | — | — | — |

## Alur bot (3 langkah)
1. Pilih fitur → **kirim 1–6 foto referensi** (dibatasi maks 6)
2. **Ketik prompt** gerakan/deskripsi (ID atau EN)
3. Render → bot kirim video (klaim: ~30 detik, **tanpa watermark**)

Bot juga **auto-generate prompt konsistensi karakter** (contoh nyata dari riwayat: *"Create a short viral TikTok-style 9:16 video using the uploaded photo as the exact character reference. Keep her face, hair, glasses, skin tone, body… outfit/appearance changes, no extra people, no distorted hands or face. Make the ending naturally loop back to the opening frame."*)

## 🧠 Kesimpulan stack model
**Bukti berlapis:**
1. Label bot sendiri: "MiniMax / LTX 2.3" (Image to Video) & "MiniMax H3" (Lip Sync)
2. Fitur andalan bernama **"Star Trail H3"** — "H3" = **MiniMax H3**
3. Riset web: **MiniMax H3 = Hailuo 3**, rilis **31 Juli 2026** — 2K native, 24fps, **audio stereo native**, 15 dtk, **omni-reference input** (gambar/video/audio referensi), open weights
4. Forensik sampel video user: 10 dtk + **audio native** + gaya selfie photoreal + artefak kacamata/face-wobble → persis profil MiniMax H3/Hailuo

**Jadi:**
- Video utama (All-in-One, Lip Sync) → **MiniMax H3 (Hailuo 3)** — kemungkinan besar
- Image to Video standar → **MiniMax (Hailuo) + LTX 2.3** (LTX = model open-source Lightricks → opsi hemat)
- Face Swap & Motion Video → pipeline face-swap video (model tidak diungkap; kandidat: InsightFace/InSwapper, LivePortrait, atau face-swap milik MiniMax)
- AI Image Editor → model edit gambar (tidak diungkap; kandidat Gemini/Nano Banana atau Flux Kontext)

## 💡 Implikasi untuk Kreaibot (kompetitor langsung)
1. **Ini produk yang persis mau kita bangun** — pelajari harga & paket fiturnya sebagai baseline
2. Model stack yang terbukti jalan: MiniMax H3 (flagship, audio native, omni-ref) + LTX 2.3 (murah) + pipeline face-swap
3. Monetisasi: token + QRIS + referral — pola terbukti di pasar Indonesia
4. Peluang diferensiasi Kreaibot: **uji konsistensi wajah otomatis** (embedding check sebelum kirim), lemari outfit tersimpan, API publik, dan Zero-Watermark yang bisa dibuktikan (bot ini klaim tanpa watermark)

## Sisa yang belum terbongkar (butuh 1 generate = keluar token)
- Model di balik Face Swap & AI Image Editor (tidak diungkap di UI)
- C2PA/sidik jari file asli (butuh file hasil yang dikirim sebagai dokumen, bukan re-encode Telegram)
- Infrastruktur backend (API aggregator mana, queue, dsb.) — tidak bisa dilihat dari luar