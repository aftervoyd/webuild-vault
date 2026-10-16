# FITUR COSPLAY — WORKFLOW FINAL (Kreeaimotion)

Ditetapkan 15 Okt 2026 · keputusan masukan dari user · mesin: Inferhub (0 koin RunningHub)
Kode: `tools/cosplay.py` · uji: `python3 tools/cosplay.py <gambar_orang> <gambar_acuan> [folder]`

## 0. KEPUTUSAN USER (mengikat, jangan diubah tanpa izin)
1. **Jalur utama = "V2"** — gambar acuan **DIKIRIM LANGSUNG** ke mesin edit (bukan diubah dulu
   jadi deskripsi teks). User menilai hasil V2 paling pas.
2. **KACAMATA = IDENTITAS.** Arunika/character sheet memakai kacamata dan itu bagian identitasnya →
   kacamata **WAJIB selalu dipertahankan**. JANGAN pernah menghapus/mengganti kacamata.
   (Menggantikan rancangan awal yang sempat mengusulkan "saklar buang kacamata".)
3. Penilaian hasil = **hak user**, bukan mesin.

## 1. MASUKAN
- **Gambar 1 – orang**: (a) character sheet yang sudah tersimpan → pakai pemilih karakter yang ada,
  atau (b) foto baru yang dikirim user.
- **Gambar 2 – acuan**: (a) foto cosplay orang lain untuk ditiru, atau (b) gambar karakter anime/kartun.

## 2. ALUR FINAL
```
[1] User pilih Gambar 1  →  karakter tersimpan (pemilih)  ATAU  foto baru
[2] User kirim Gambar 2  →  foto cosplay  ATAU  gambar karakter anime
[3] 1 panggilan vision (±5 dtk)  →  jenis acuan: "foto" atau "ilustrasi"
                                    (kalau ilustrasi, sekaligus ditarik spesifikasi kainnya)
[4] Jalankan edit:
      ┌ acuan FOTO   → Kandidat A: gpt-image-2   (prompt salin-kostum + kunci identitas)
      │                 Kandidat B: gemini-3.0-pro-image (mesin kedua, pembanding)
      └ acuan ANIME  → Kandidat A: gpt-image-2   (JALUR V2: gambar anime dikirim mentah)
                        Kandidat B: gemini-3.0-pro-image (anime + spesifikasi kain)
[5] Kirim 2 hasil ke user (tanpa menyebut merek mesin) + tombol:
       ✅ Pakai kandidat ini   ·   🔁 Ulangi   ·   🎭 Cosplay lagi
[6] Opsional pass kedua: "pertegas jadi foto" / koreksi detail tertentu
```

## 3. ATURAN PROMPT (terkunci — sudah ada di `tools/cosplay.py`)
| Aturan | Isi |
|---|---|
| **KUNCI IDENTITAS** | wajah, fitur wajah, warna kulit, bentuk badan, pose, sudut kamera, framing, latar, cahaya = sama persis |
| **KACAMATA** | "kacamata di gambar pertama WAJIB tetap di wajahnya, jangan pernah dihapus/diganti" |
| **RAMBUT / WIG** | diganti mengikuti wig karakter acuan (warna, panjang, gaya) + makeup senada — **wajah tidak berubah** |
| **INTERPRETASI BEBAS + RASA** | "adaptasi bebas, tidak wajib menyalin setiap potongan" · rok boleh pendek/belah, siluet lebih ramping, cape boleh pendek · **suasana fantasi/anime dipertahankan**: warna pekat, cahaya dramatis, kesan fotografi cosplay sinematik |
| ~~SALIN SEMUA POTONGAN~~ | ❌ **DIBATALKAN.** Perintah ini bikin hasil kaku seperti kostum panggung dan **wajahnya ikut bergeser** (dinilai mesin & dibuktikan user). Disimpan sebagai `PROMPT_ANIME_SETIA`, bukan default |
| **REALISTIS** | pori kulit terlihat, serat & berat kain nyata, bayangan natural · BUKAN ilustrasi/anime/kartun/cel-shading/warna flat |
| **TANGAN** | kedua tangan terlihat utuh, jari natural (artefak tangan muncul di semua uji) |
| **LARANGAN** | tanpa teks, tanpa watermark, tanpa logo |

## 4. MESIN
| Peran | Model | Waktu | Catatan |
|---|---|---|---|
| Pembaca gambar (jenis acuan) | `gemini-3.8-flash` | ±5 dtk | hasil terbukti sangat detail |
| Kandidat A (jalur V2) | `gpt-image-2` | ±32 dtk | paling setia pose & identitas |
| Kandidat B (pembanding) | `gemini-3.0-pro-image` | ±34 dtk | tekstur kain paling nyata |
| Ukuran | 1536x2304 (uji) · bisa **2160x3840 (4K)** | — | gpt-image-2 menuruti `size` tepat |
| Darurat (Inferhub mati) | RunningHub AI App `2095689306085285890` | — | 40 koin, slot 20=orang · 21=pose · 41=baju |

## 5. BIAYA & HARGA
- **Biaya asli kita: ±Rp 100–150 per permintaan** (2 gambar + 1 vision) — **0 koin RunningHub**.
- Waktu: ±40 dtk (1 kandidat) sampai ±140 dtk (2 kandidat, jalan berurutan).
- **Saran harga: 1 kredit (Rp 1.000)** — samakan dengan Ganti Baju. Margin ±85%.
- **Opsi umpan (rekomendasi)**: jadikan Cosplay **gratis** untuk menarik user, lalu monetisasi di
  **Motion Control** yang memang makan koin. Cosplay = pintu masuk, motion = mesin uang.

## 6. RISIKO & BATAS
- **Hak cipta karakter**: ini alat bikin konten fan; jangan klaim resmi, jangan jual sebagai lisensi.
- **Izin wajah**: hanya foto yang dikirim user sendiri.
- **Kualitas acuan menentukan hasil**: acuan buram/gelap → hasil ikut jelek.
- **Tidak boleh menjanjikan 100% sama**: mesin menginterpretasi desain; baju anime yang mustahil
  dijahit akan jadi interpretasi terbaik mesin, bukan replika.
- **Glitch rambut saat bergerak** (kasus job #48) hanya berlaku di video, bukan di gambar diam.

## 7. YANG MASIH PERLU DIKERJAKAN (kalau user menyetujui)
1. Tombol menu **🎭 Cosplay** + alur FSM (`cosplay_base` → `cosplay_ref` → proses)
2. Sambungkan pemilih karakter yang sudah ada ke langkah Gambar 1
3. Panel hasil: kirim 2 kandidat + tombol pilih/ulangi
4. Tampilkan spesifikasi kostum kalau acuan ilustrasi (biar user paham mesin membaca apa)
5. Catat di DB (job cosplay) + batas kredit
---

## 8. HASIL UJI PROMPT FINAL (15 Okt 2026, `data/cosplay_final/`)
Uji: Arunika (`data/base_8886993492.jpg`, **berkacamata**) + acuan karakter anime.

| Yang diuji | Hasil |
|---|---|
| **Kacamata tetap ada?** | ✅ **YA di kedua kandidat** — kunci identitas bekerja |
| **Potongan kostum lengkap?** | ✅ YA di keduanya: rok panjang, cape panjang, panel depan, armour lengan (sebelumnya di uji V2 semua ini HILANG) |
| **Sepatu bot** | ⚠️ masih tidak jelas (terbaca seperti sepatu pendek/hak) → prompt sudah ditambah perintah bot tinggi, **belum diuji ulang** |
| **Wajah identik?** | ⚠️ mirip tapi bukan replika fotografis 100% — ini batas wajar mesin edit |
| **Kandidat A (gpt-image-2, jalur V2)** | dinilai lebih rapi/final |
| **Kandidat B (gemini-3.0-pro-image)** | lebih banyak artefak kecil |
| Waktu | 67 dtk (A) + 42 dtk (B) · **0 koin RunningHub** |

Bukti: `BUKTI-COSPLAY/FINAL_uji_kacamata.jpg` · kode: `tools/cosplay.py`

---

## 9. KOREKSI SELERA USER (15 Okt 2026) — aturan "salin semua" DIBATALKAN
User menilai hasil FINAL (perintah "salin semua potongan") **kalah** dari V2 lama, dengan alasan:
*"hasilnya jadi sedikit sexy tanpa ngerubah wajah dan vibes animenya"*.

Dibuktikan mesin (perbandingan `BUKTI-COSPLAY/BANDING_V2LAMA_vs_KAKU.jpg`):
| | V2 lama (interpretasi bebas) | FINAL "salin semua" |
|---|---|---|
| Rok | panjang **dengan belah tinggi** (kaki terlihat) | panjang penuh tertutup |
| Cape | lebih pendek/sedang | sampai lantai |
| Siluet | **ramping** | lebar (A-line) |
| Pose | dinamis (satu kaki maju) | tegak kaku |
| Kesan | **glamor, modis, atraktif** | seperti kostum panggung |
| Wajah | **lebih natural/hidup** | lebih kaku |

**Kesimpulan teknis:** memaksa kostum menyalin acuan **juga menarik wajah menjauh** — jadi jalur
interpretasi bebas lebih baik di dua hal sekaligus (estetika + identitas).

**Aturan baru (default):** interpretasi bebas + rasa glamor (`PROMPT_ANIME` di `tools/cosplay.py`).
Versi setia desain disimpan sebagai `PROMPT_ANIME_SETIA` (bukan default).

## 10. PERBAIKAN KETAHANAN (15 Okt 2026)
Uji "rasa" pertama kena **HTTP 524 (upstream error)** dari Inferhub untuk `gpt-image-2` → diuji
mesin lain. `tools/cosplay.py` sekarang punya **cadangan otomatis**: kalau mesin utama memulangkan
502/503/504/524 (sibuk/mati), permintaan **langsung jatuh ke mesin kedua** tanpa menggagalkan user.
Pelajarannya: 524 bukan salah prompt — jangan mengubah prompt, pindah mesin.
