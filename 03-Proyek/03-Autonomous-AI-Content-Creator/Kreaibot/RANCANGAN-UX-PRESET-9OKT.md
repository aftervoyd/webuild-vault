# RANCANGAN UX v2 — TOMBOL PRESET 1-TAP (9 Okt 2026)

> Koreksi dari user: rancangan wizard 5 langkah (mode → pose → tujuan → kualitas → konfirmasi) **NGGAK user friendly**.
> Pembanding nyata: Kuzushi (@KuzushiGenBot) alurnya cuma **foto → prompt → pilih durasi → jadi** (lihat `TEARDOWN-KUZUSHI-9OKT.md`).
> Jadi target kita: **lebih sedikit langkah dari Kuzushi**, bukan lebih banyak.

---

## 1. PRINSIP

1. Setelah kirim foto, user cukup **1 TAP** untuk mulai render.
2. **Harga tampil di tombol** (contek Kuzushi — user tahu biaya sebelum klik).
3. **Prompt tidak perlu diketik** — preset = prompt siap pakai. Ini keunggulan kita: Kuzushi masih nyuruh user ngetik prompt sendiri, kita nggak.
4. Kerumitan (multi-scene, frame chaining, konsistensi wajah) **disembunyikan di dalam preset**.
5. Opsi lanjutan **ada tapi tidak wajib** (`⚙️ Atur sendiri`).

## 2. ALUR INTI (2 langkah total)

```
[user kirim foto]
        ↓
[1 pesan: "Mau diapain? 👇" + grid preset + baris durasi + ⚙️ Lanjutan]
        ↓
[user tap 1 preset]  ← SELESAI. render jalan.
```

Pesan yang sama juga memuat:
- baris **⏱ Durasi** (5s/10s/15s/30s) → default sudah dipilih otomatis per preset
- **⚙️ Atur sendiri** (opsional, untuk yang mau ngetik prompt & pilih kamera)

## 3. GRID PRESET (satu layar, 12 tombol)

| Tombol | Isi internal (tidak diketik user) | Mesin | Default | Harga |
|---|---|---|---|---|
| 😄 Tertawa & melambai | 1 prompt + kamera maju pelan | i2v | 5 s | 0,5 T |
| 💃 Menari | 1 prompt + kamera statis | i2v | 10 s | 1 T |
| 🚶 Vlog jalan santai | 1 prompt + kamera handheld slow | i2v | 10 s | 1 T |
| 🏃 Lari dikejar kamera | **3 scene otomatis** (lari → tersandung → noleh/tertawa) | story | 15 s | 1,5 T |
| 😮 Kaget / terkejut | 1 prompt | i2v | 5 s | 0,5 T |
| 💪 Pose model / fashion | 1 prompt + kamera orbit pelan | i2v | 5 s | 0,5 T |
| 🌬️ Rambut & angin natural | 1 prompt (gerak halus, aman) | i2v | 10 s | 1 T |
| 📖 Cerita panjang | **6 scene**, user tulis ceritanya | story | 30 s | 2,5 T |
| 🎭 Ganti wajah ke foto lain | foto ke-2 = target | faceswap | — | 0,5 T |
| 🖼️ Edit foto (baju/latar) | editor + prompt singkat | editor | — | 0,3 T |
| ✍️ Tulis sendiri | prompt bebas user | i2v | 10 s | 1 T |
| 🎲 Kejutan | preset acak (untuk yang bingung) | auto | auto | sesuai |

Catatan: preset "🏃 Lari dikejar kamera" **pakai mesin multi-scene** — user tetap cuma 1 tap, tapi yang jalan di belakang 3 render + frame chaining + jahit. Inilah "kuzushi bisa, kita juga bisa" — malah hasilnya lebih nyambung.

## 4. DIMENSI "BUAT APA" (opsional, 1 tap, boleh dilewat)

Baris kecil di bawah grid: `🎯 Buat apa?` → mengubah gaya kamera + nada prompt:

| Pilihan | Efek internal |
|---|---|
| 📱 Vlog selfie HP | kamera selfie handheld, jarak dekat, natural |
| 🎵 Konten TikTok/Reels | gerak dinamis, ritme cepat, hook di 1 detik pertama |
| 🛍️ Jualan produk UMKM | produk tetap tajam, cahaya studio |
| 🖼️ Status WA / Story | pendek, manis, tanpa gerakan aneh |
| 🎞️ Sinematik | kamera film, cahaya dramatis, gerak lambat |
| (default: 🎯 Santai) | kamera pelan biasa |

Semua tetap **vertikal 9:16** — itu batas app LTX kita sekarang.

## 5. KUALITAS / RESOLUSI — JUJUR, jangan jual yang belum terbukti

- **Sekarang (LIVE):** 768×1280 · 24 fps · audio AAC 48 kHz. Ini yang dijual.
- **Tahap 2 (WAJIB diuji dulu):** upscale 1080p / 4K pakai node upscale RunningHub → bisa jadi add-on "🎞️ HD (+0,5 T)".
- **8K: JANGAN dijual.** Mesin kita tidak menghasilkan 8K. Kalau dipaksa, itu klaim palsu → user kecewa.

## 6. MODEL DATA (siap dipakai kode)

```python
PRESET = {
  key, label, emoji, engine,        # engine: i2v | story | faceswap | editor
  prompt,                            # prompt inti (sudah patuh 1-aksi)
  camera,                            # klausa kamera
  duration, durations,               # durasi default + pilihan
  need_photos, need_prompt,
  cost,                              # token (ditampilkan di tombol)
}
prompt_final = preset.prompt + " " + usecase.camera + " " + IDENTITY_CLAUSE
```

## 7. RENCANA PASANG (urut, kecil → besar)

1. `presets.py` — tabel preset + fungsi `build_prompt(preset, usecase)`.
2. Layar baru setelah foto: grid preset (1 pesan, teks harga di tombol).
3. Default pintar: preset "Lari dikejar kamera" → otomatis mode `story` (3 scene).
4. Baris `🎯 Buat apa?` (opsional).
5. `⚙️ Atur sendiri` = alur lama (prompt + durasi manual) tetap hidup.
6. Uji: tiap preset minimal 1 render nyata sebelum masuk `SIAP_JUAL` (aturan lama: jangan jual yang belum terbukti).

## 8. YANG TIDAK DILAKUKAN

- ❌ Wizard 5 langkah sebelum render.
- ❌ Maksa user ngetik prompt (boleh, tapi tidak wajib).
- ❌ Menampilkan pilihan teknis (fps, koin, nama model) ke user awam.
- ❌ Jual 4K/8K sebelum terbukti.