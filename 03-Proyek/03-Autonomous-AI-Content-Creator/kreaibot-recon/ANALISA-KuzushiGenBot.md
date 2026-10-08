---
target: "@KuzushiGenBot"
tanggal-analisa: 2026-10-08
jenis: black-box fingerprint dari 1 sampel video (Telegram re-encode)
status: hipotesis (belum probing interaktif)
---

# Recon @KuzushiGenBot — catatan analisa

## Profil publik (t.me/KuzushiGenBot)
- Nama: **Kuzushi** · username @KuzushiGenBot
- Deskripsi: default Telegram ("You can contact right away") — tidak ada bio/pricing/website yang terlihat
- Arti nama: "Kuzushi" (崩し, Jepang) + Gen — indikasi gaya visual; "Kuzushi" juga nama teknik seni bela diri (off-balance). Belum tentu relevan.

## Forensik file sampel (video 10s, 9:16, ADA AUDIO)
| Cek | Hasil | Arti |
|---|---|---|
| Durasi | 10.033 s | Khas Kling (5/10s) / Hailuo (10s) |
| Resolusi | 368×640 (re-encode) | Sumber asli ≥720×1280 kemungkinan |
| Codec | h264 723kbps + aac 33kbps | RE-ENCODE TELEGRAM — bukan codec sumber |
| handler_name | "Core Media Video" | Penanda pipeline AVFoundation Telegram, bukan sumber |
| creation_time | 2026-10-08T01:16:11Z | Jam re-encode Telegram (= jam upload), bukan jam generate |
| C2PA/metadata | TIDAK ADA | Dicuci Telegram; konfirmasi definitif butuh file ASLI |
| Audio | Jalan 10s penuh, ada spike SFX di akhir | Model video generatif dengan **audio native** |

## Analisa visual (Gemini 3.6 via Inferhub, dari 3 frame)
- Subjek: wanita ±20an, rambut hitam panjang, **kacamata**, crop top putih + celana pendek abu, kalung emas
- Gaya: **PHOTOREAL**, nuansa "video selfie handheld"
- Kulit: natural tapi ada smoothing/waxy khas video AI; artefak halus: **frame kacamata bergeser antar sudut**, kontur wajah sedikit melar saat kepala bergerak — ciri tipikal image-to-video diffusion
- Adegan: ruang tamu, duduk di sofa, sudut selfie, kamera bergoyang halus; ngomong ke kamera → menoleh → senyum
- Gerakan: ~25% piksel berubah antar frame (gestur + sway kamera)

## Verdict model
**Paling mungkin: keluarga KLING (2.x/3).** Alasan:
1. Durasi 10s + audio native (Kling 2.6+ punya audio)
2. Gaya "selfie talking head" — format paling populer di Kling creator scene
3. Artefak karakteristik: kacamata bergeser, face-contour wobble saat head movement
4. Render kulit smoothing ringan — khas Kling (bukan Veo yang lebih "kering/natural", bukan Runway yang sinematik)

**Alternatif:** Hailuo/MiniMax M2 (kualitas mirip, 10s, audio) · Wan 2.5 (open-source — kalau botnya hemat, ini kandidat kuat) · Veo 3.1 (kemungkinan kecil: motion lebih fisikal, 8s lebih umum).

**Tingkat keyakinan: menengah (±60-70%).** Karena Telegram mencuci semua metadata, ini belum definitif.

## Sistem bot (hipotesis kerja)
- Arsitektur paling umum untuk bot jenis ini: Telegram frontend → API video (fal.ai / Replicate / TensorArt / provider China) → kirim hasil
- Monetisasi kemungkinan pay-per-generate (kredit) atau freemium — perlu probe
- Workflow karakter: upload foto → referensi karakter → i2v dengan foto tsb

## Langkah berikut (untuk validasi)
1. **Probe interaktif** (butuh login web.telegram.org di browser): /help, /start, error probing, batas gratis
2. **Minta bot kirim hasil sebagai FILE/dokumen** (bukan video) → C2PA bisa lolos dari Telegram → definitif (Kling API nandatanganin C2PA)
3. Cek harga & opsi resolusi/durasi (UI khas provider tertentu)