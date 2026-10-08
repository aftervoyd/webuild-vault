---
status: rencana
tanggal: 2026-10-08
segmen: umum/creator
posisi-webuild: Proyek 3 — Autonomous AI untuk Content Creator
---

# 🤖 Proyek 3 — Bot Telegram Karakter AI untuk Content Creator — KREAIBOT

**Nama project (keputusan user, 8 Okt 2026): Kreaibot** — krea(ktif) + bot.
Alternatif yang sempat diajukan (tidak dipakai): Wayang.AI, KARVA, Rupa.

## Konsep inti (satu kalimat)
User upload **master character sheet** (foto), bot mengunci identitas wajahnya jadi satu "karakter", lalu user bisa: ganti baju/scene (struktur wajah tetap identik), generate foto konsisten dalam jumlah banyak, ubah foto jadi video, dan transfer pose — semua dari dalam Telegram.

## Alur sistem
1. `/start` → menu: Buat Karakter · Lemari · Foto · Video · Pose · Galeri
2. Upload master sheet (1–5 foto: depan, profil, full body) → deteksi wajah (InsightFace/FaceNet embedding) → simpan **kartu karakter** = embedding wajah + set referensi + lemari outfit
3. **Uji konsistensi otomatis** sebelum karakter aktif: generate 3 pose uji → hitung kemiripan wajah (embedding ≥ ambang) → cuma lolos kalau wajahnya nyambung
4. Generator jalan di **cloud API** (VPS 2GB TANPA GPU): fal.ai / Google Gemini API / Replicate / Modal
5. Antrean tugas + notifikasi hasil ke bot (webhook)
6. Monetisasi: **Telegram Stars** (kredit per generasi) atau Midtrans (IDR)
7. Storage: lokal dulu (26GB bebas), pindah S3-compatible kalau aset membesar

## Fitur
**P0 — MVP (harus)**
- Upload master sheet multi-sudut
- Generate foto konsisten (teks → gambar, wajah terkunci)
- **Ganti pakaian/aksesori/background — struktur wajah tetap** (inti fitur)
- Galeri per karakter + lemari outfit (simpan hasil outfit → dipakai ulang)
- Uji konsistensi otomatis (embedding)

**P1 — Konten**
- **Image-to-video** (Kling / Veo): foto diam → gerak (bicara, gestur, jalan), 5–10 dtk
- **Transfer pose** (Viggle / Kling pose): dari foto referensi apa pun
- Format 9:16 / 16:9 / 1:1, HD

**P2 — Skala**
- Lip-sync + kloning suara (wajib izin pemilik suara)
- Batch/kampanye (ratusan aset sekali jalan)
- API publik → Webuild jual ke UMKM/creator lain

## Model terbaik (riset Okt 2026)
- **Kunci identitas wajah:** Nano Banana 2 (Gemini API) — wajah paling setia; cadangan open-source Flux + PuLID (gratis, kontrol penuh, butuh GPU sendiri)
- **Ganti baju / scene, wajah tetap:** Flux Kontext (fal.ai) — paling andal untuk edit pakaian, dukung hingga 8 gambar referensi; cadangan Nano Banana 2 (edit iteratif)
- **Foto → video:** Kling 3 / Kling 2.6 (karakter paling konsisten + audio native); Veo 3.1 (fisika terbaik); open-source Wan 2.5 (murah, bagus); Runway Gen-4.5 (sinematik)
- **Transfer pose:** Viggle AI (dari 1 foto, berbasis fisika); cadangan open Animate Anyone-2 / MusePose / ControlNet pose
- **Lip-sync (P2):** LatentSync / Hedra; suara: ElevenLabs atau GPT-SoVITS open-source (dukung bahasa Indonesia)

**Pola kerja yang benar (dari riset):** jangan umpan master sheet langsung ke model video. Rantai: master sheet → Nano Banana 2/Flux Kontext (foto kunci konsisten) → masih terbaik → umpan ke Kling/Veo → video. Identitas nempel lebih kuat lewat rantai ini.

## Biaya (perlu diverifikasi saat riset lanjutan)
- Foto: ±$0.03–0.10 / gambar
- Video: ±$0.10–0.50 / 5 detik
- GPU on-demand (Modal/RunPod) untuk model open-source kalau mau murah di volume besar

## Legal & etika (PENTING)
- Wajah orang → **wajib izin tertulis pemilik wajah** (UU PDP No.27/2022 + norma deepfake). Bot wajib minta persetujuan saat upload.
- Kloning suara: hanya untuk pemilik suara itu sendiri.

## Langkah berikutnya (kalau di-GAS)
1. Riset harga API + pilih provider (fal vs Gemini vs Replicate)
2. Prototipe P0: upload → lock wajah → ganti baju (target 1 pekan)
3. Uji kualitas standar 6 scene (wajah 40%, rambut/ciri khas 20%, usia/proporsi 15%, outfit 10%, gaya 10%, artefak 5%)
4. Susun harga kredit + cara bayar (Telegram Stars)