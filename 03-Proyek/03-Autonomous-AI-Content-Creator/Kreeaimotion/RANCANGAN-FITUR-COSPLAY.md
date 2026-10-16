# RANCANGAN FITUR "COSPLAY" (image-to-image) — Kreeaimotion

Status: rancangan + uji nyata 15 Okt 2026 · mesin: Inferhub (0 koin RunningHub)

## 1. APA YANG DIMINTA
- **Gambar 1 (dasar)**: character sheet yang sudah tersimpan ATAU foto baru dari user
- **Gambar 2 (acuan)**: (a) foto cosplay orang lain untuk ditiru · ATAU (b) gambar karakter anime/kartun
- Syarat utama: **hasil harus REALISTIS** (foto, bukan gambar).

## 2. DUA KASUS + TITIK GAGALNYA

### Kasus A — acuan FOTO cosplayer lain
Meniru kostum dari foto orang lain. Ini **kelas masalah yang sama dengan Ganti Baju** yang sudah
jalan di bot → risiko rendah, mesin sudah terbukti.

### Kasus B — acuan KARAKTER ANIME/KARTUN  ← kasus sulit
Beda domain: ilustrasi 2D → harus jadi foto orang nyata. Titik gagal yang wajib dihindari:

| # | Kegagalan | Kenapa terjadi |
|---|---|---|
| 1 | **Ketularan gaya (style bleed)** | Gambar anime dikirim mentah ke mesin edit → mesin meniru *gaya*, bukan cuma *isinya*. Hasil jadi anime/kartun. |
| 2 | **Identitas luntur** | Kostum terlalu dominan → wajah/badan ikut berubah |
| 3 | **Detail karangan** | Mesin menambah hiasan yang tidak ada di acuan (pernah terjadi: app Qwen-Edit menambah motif bunga yang tidak ada) |
| 4 | **Kostum setengah jadi** | Cuma baju yang ikut; wig/hair, makeup, aksesori, armour tidak → tidak terasa "cosplay" |
| 5 | **Cahaya tidak nyambung** | Hasil terasa "tempelan" karena arah cahaya/bayangan beda |

## 3. PRINSIP RANCANGAN (dari pelajaran yang sudah terbukti di proyek ini)
1. **Selalu EDIT foto asli, jangan generate dari nol** — skor kulit ±8/10 vs ±5/10.
2. **Untuk acuan ilustrasi: PISAHKAN GAYA DARI ISI.** Ubah dulu gambar kartun jadi
   **SPESIFIKASI TEKS dunia nyata** (nama bahan, potongan, warna, wig, makeup), lalu edit
   **hanya dengan gambar orang + teks itu**. Ini yang membunuh style bleed dari akarnya.
3. **Kunci identitas secara eksplisit**: wajah, warna kulit, bentuk badan, pose, sudut kamera,
   latar, dan cahaya harus disebut "tetap sama persis".
4. **Perintah anti-kartun eksplisit**: "fotografi, bukan ilustrasi, bukan anime, bukan cel-shading,
   tanpa warna flat, tekstur kulit berpori, serat kain nyata".
5. **Kosplay = bukan cuma baju** — wig/hair, makeup, dan aksesori harus ikut diminta.
6. **4K gratis**: `gpt-image-2` menuruti `size` dengan tepat (2160x3840) → detail kain muncul.
7. **Serahkan penilaian ke user**: kirim 2 kandidat (mesin berbeda), user yang memilih.

## 4. ALUR YANG DIRANCANG (final)

```
Masukan user
 ├─ Gambar 1 (dasar) : karakter tersimpan (pemilih yang sudah ada) ATAU foto baru
 └─ Gambar 2 (acuan) : foto cosplay ATAU karakter anime
          │
          ▼
 [0] DETEKSI JENIS ACUAN — 1 panggilan vision:
     "Ini foto orang atau ilustrasi/kartun?" + sekaligus ambil spesifikasi kostumnya
          │
          ├── ACUAN FOTO ─────► [2] EDIT 2 GAMBAR (jalur cepat)
          │                      prompt: "pakai kostum dari gambar 2 pada orang di gambar 1"
          │
          └── ACUAN ILUSTRASI ► [1] TEKS: ubah kartun → SPESIFIKASI KOSTUM dunia nyata
                                 (potongan, bahan asli, warna, armour, wig, makeup, cara lampu)
                                 ▼
                                 [2] EDIT 1 GAMBAR + TEKS (tanpa gambar anime!)
                                     → gaya kartun tidak mungkin bocor karena tidak dikirim
          ▼
 [3] PEMERIKSAAN MUTU otomatis (1 panggilan vision):
     "masih ada jejak kartun? wajah identik? kostum lengkap?" → gagal = ulangi mesin cadangan
          ▼
 [4] KIRIM 2 KANDIDAT ke user → user yang menilai & memilih
```

### Mesin (berdasarkan hasil uji di `data/cosplay_proto/`)
| Peran | Model | Catatan |
|---|---|---|
| Teks/vision (baca kostum) | `gemini-3.8-flash` | sangat detail; hasil sudah terbukti |
| Edit utama | `gpt-image-2` | patuh `size` (bisa 4K), ±Rp 40–60/gambar |
| Edit cadangan | `gemini-3.0-pro-image` | instruksi paling nurut (8,3/10) |
| Alternatif | `flux-kontext-pro`, `seedream-5.0-pro`, `nano-banana-2` | sedang dibandingkan |
| Darurat (kalau Inferhub mati) | RunningHub AI App `2095689306085285890` | 40 koin, slot: 20=orang · 21=pose · 41=baju |

## 5. SISI BOT (yang perlu ditambah)
- Tombol menu baru: **🎭 Cosplay** (image-to-image)
- FSM: `cosplay_base` (pilih karakter tersimpan / kirim foto) → `cosplay_ref` (kirim foto cosplay
  atau gambar karakter) → proses → kirim hasil
- Tampilkan **spesifikasi kostum** ke user saat acuan ilustrasi → transparan + user bisa koreksi
- Kirim **2 kandidat** + tombol "pakai yang ini" / "ulangi" / "pertegas jadi foto" (pass kedua)
- Biaya ke user: bisa 0 kredit (mesin 0 koin) atau kecil; biaya nyata kita ±Rp 40–100/gambar

## 6. CATATAN PENTING / RISIKO
- **Hak cipta karakter**: cosplay karakter berhak cipta = fan content. Jangan klaim resmi, jangan
  jual sebagai produk resmi. Fitur ini alat bikin konten, bukan penjual lisensi.
- **Izin wajah**: hanya boleh memakai foto yang dikirim user sendiri.
- **Kualitas acuan menentukan hasil**: acuan buram/hitam-putih → hasil ikut jelek.
- **Jangan janjikan 100% sama**: mesin menginterpretasi kostum; kalau acuannya tidak masuk akal
  secara fisik (baju anime tidak mungkin dijahit), hasilnya interpretasi terbaik mesin.
---

## 7. HASIL UJI NYATA (15 Okt 2026) — 4 varian diuji, bukti di `data/cosplay_proto/`

Bahan uji: base = `data/base_8886993492.jpg` (Arunika) · acuan anime = karakter ksatria putih/emas/biru
(dibuat sendiri) · acuan foto = cosplayer mantel merah.

| Varian | Jalur | Realisme | Kesetiaan kostum | Hasil |
|---|---|---|---|---|
| **V1** | acuan FOTO → edit 2 gambar | **8/10** | tinggi | identitas tetap, kostum pindah ✓ |
| **V2** | acuan ANIME → edit 2 gambar mentah | 6,5–7/10 | **paling buruk** ✗ | rok jadi belah tinggi, cape jadi selendang pendek, panel depan & armour kaki HILANG |
| **V3** | acuan ANIME → **TEKS** → edit 1 gambar (`gpt-image-2`) | 7,5–8/10 | **paling lengkap** ✓ | korset, cape panjang, panel depan, rok panjang, gauntlet, bot — semua ada |
| **V5** | acuan ANIME + teks bersama (`gemini-3.0-pro-image`) | **8–8,5/10** ⬆️ | baik | render paling meyakinkan; panel depan biru hilang |
| V4 | `flux-kontext-pro` | — | — | **404 unknown model** (beda dari daftar `/models`) |

### Kesimpulan uji
1. **Hipotesis awal gue salah di mekanismenya, tapi benar di kesimpulan.** Anime mentah TIDAK membuat
   hasil jadi kartun (mesin menahan gaya) — tapi hasilnya **kehilangan detail kostum** dan justru
   **paling lemah**. Jalur terbaik tetap **tidak mengirim gambar anime mentah**.
2. **Jalur TEKS (V3) = basis produksi terbaik**: kostum paling lengkap & setia, dan paling mudah
   diperbaiki. **V5 = juara realisme tekstur** (satin, lipatan, pantulan logam paling nyata).
3. **Keputusan rancangan: kirim DUA kandidat** — V3 (lengkap) + V5 (realistis) — user yang memilih.
4. **Acuan FOTO tetap jalur cepat** yang sudah terbukti (V1, 8/10) → pakai mesin Ganti Baju yang ada.

### Tiga cacat yang wajib diperbaiki di prompt produksi
1. **Kacamata ikut terbawa** padahal acuan tidak pakai → tambah saklar "buang kacamata" (default: buang
   untuk cosplay).
2. **Mesin vision MENAMBAH detail yang tidak ada** → spesifikasi berisi "ikat pinggang kulit coklat
   chestnut" yang tidak ada di acuan, dan ikat pinggang itu muncul di V3. → perintah vision harus:
   *"deskripsikan HANYA yang terlihat; jangan menambah apa pun"*.
3. **Tangan tidak jelas / jari hilang** di semua hasil → tambah perintah "kedua tangan terlihat utuh,
   jari natural".

### Mesin final
- Jalur teks (pembaca kostum): `gemini-3.8-flash` — hasil terbukti sangat detail
- Kandidat 1 (lengkap): `gpt-image-2` — 1 gambar + teks, ±97 dtk
- Kandidat 2 (realistis): `gemini-3.0-pro-image` — 1 gambar + anime + teks, ±34 dtk
- Acuan foto: `gpt-image-2` 2 gambar, ±32 dtk
- Semua **0 koin RunningHub** (Inferhub). Perintah uji: `.venv/bin/python -B tools/cosplay_proto.py`
