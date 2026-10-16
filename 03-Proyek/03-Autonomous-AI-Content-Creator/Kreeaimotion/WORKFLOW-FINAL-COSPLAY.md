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

---

## 11. PELAJARAN TERPENTING: HASIL YANG DISUKAI ITU UNDIAN, BUKAN RESEP
Diuji ulang (15 Okt 2026): prompt V2 asli dijalankan lagi dengan gambar & acuan yang **sama persis**
→ hasilnya **BEDA** (rok jadi panjang penuh tertutup, bukan belah tinggi seperti yang disukai user).

**Sebab:** mesin gambar itu stokastik — satu hasil = satu undian. Mengulang prompt yang sama
**tidak menjamin** hasil serupa.

**Akibat untuk rancangan (dua aturan baru):**
1. **Gaya harus DIPERINTAHKAN, bukan diharapkan.** Jangan tulis "rok boleh pendek/belah" (itu cuma
   izin) — tulis **"rok HARUS pendek atau berbelah tinggi supaya kakinya terlihat; siluet ramping;
   pose dinamis (tangan di pinggul, satu kaki maju)"**. Sudah dipasang di `PROMPT_ANIME`.
2. **Kirim BEBERAPA SAMPEL lalu user memilih.** Satu hasil bukan "hasil final" — user yang menilai.
   Ini juga menutup risiko undian jelek.

**Jangan pernah menjanjikan** "hasilnya pasti seperti contoh yang lu suka" — yang bisa dijamin adalah
*arahnya sama*, bukan gambar identik.

**Aturan yang sudah dipasang di kode** (`tools/cosplay.py`):
- `PROMPT_ANIME` = direktif: ramping + rok pendek/belah + pose dinamis + glamor + vibe anime + kunci
  identitas/kacamata. **Ini default.**
- `PROMPT_ANIME_RASA` = varian lembut (kebebasan penuh) — hasil: anggun tapi tertutup.
- `PROMPT_ANIME_SETIA` = salin semua potongan — hasil: kaku seperti kostum panggung. **Jangan dipakai.**
- Ketahanan: mesin sibuk (502/503/504/524) → **jatuh otomatis ke mesin kedua**; gagal simpan berkas
  **tidak** memicu render ulang.

---

## 12. IMPLEMENTASI KE BOT — SELESAI (16 Okt 2026, commit `15c6b15`)
Fitur 🎭 Cosplay sudah **hidup di bot**, bukan lagi rancangan.

**Yang ditambah:**
| Bagian | Isi |
|---|---|
| Menu | tombol **🎭 Cosplay** (baris sendiri, di bawah Ganti Baju/Pose) + perintah `/cosplay` |
| Setelan | `MOTIONBOT_COSPLAY_COST` (default **1 credit**, isi `0` = gratis) · `MOTIONBOT_COSPLAY_KANDIDAT` (default **2**) |
| Status alur | `cosplay_base` (minta foto karakter) · `cosplay_ref` (minta acuan) |
| Alur | tekan 🎭 → **pemilih karakter** yang sudah ada (atau kirim foto baru) → kirim acuan (foto cosplay / gambar anime) → job masuk antrean |
| Hasil | dikirim **beberapa versi** (label "versi 1 dari 2") + berkas ukuran penuh; ada tombol **🔁 Coba acuan lain** (tanpa pilih karakter ulang) |
| Mesin | `tools/cosplay.py` dijalankan di worker; **0 koin RunningHub** |
| Pengaman | mesin sibuk (502/503/504/524) → otomatis pindah mesin kedua · gagal simpan tidak memicu render ulang · gagal total → credit dikembalikan |

**Bukti uji alur** (`tools/uji_cosplay.py`, lewat Dispatcher aiogram asli — tanpa menyentuh Telegram):
```
1️⃣ tekan '🎭 Cosplay'      → pemilih karakter ADA (cp:use / cp:new) ✅
2️⃣ tekan karakter #6       → base BERGANTI & sama persis dengan karakter itu ✅
                            → state = Flow:cosplay_ref ✅
3️⃣ kirim foto acuan        → job #50 model=cosplay dibuat, acuan tersimpan 1443 KB, state bersih ✅
4️⃣ bersih-bersih           → job uji ditandai selesai (tidak ikut jalan saat restart) ✅
✅ PASS
```

**Uji end-to-end sungguhan:** job #51 dimasukkan ke bot yang hidup → worker memungutnya →
`INFO job cosplay 51: karakter=base_8886993492.jpg | acuan=...` → hasil dikirim ke Telegram user.

---

## 13. HASIL BOT HIDUP + TEMUAN GAYA (16 Okt 2026)
Job #51 (dimasukkan ke bot hidup, dipungut worker sendiri) → **2 versi terkirim**: `state=done`, tanpa galat.

| | Versi 1 (slug `_1_langsung`) | Versi 2 (slug `_2_realistis`) |
|---|---|---|
| Prompt | `PROMPT_ANIME` (direktif: ramping, belah/pendek, pose dinamis, glamor) | `PROMPT_ANIME2` (lewat spesifikasi kain — gaya setia desain) |
| Rok | **belah/pendek, kaki terlihat** | panjang penuh, tanpa belah |
| Pose | dinamis (tangan di pinggul, satu kaki maju) | tegak kaku |
| Kacamata | ✅ tetap | ✅ tetap |
| Rasa vs V2 lama | **paling mirip** ✓ | kurang mirip |

**Bukti:** `BUKTI-COSPLAY/HASIL_BOT_job51.jpg`

**Temuan:** beda rasa antar versi itu **disebabkan prompt**, bukan mesin — versi 2 masih memakai prompt
"setia desain" (rok panjang elegan). Kalau user mau dua-duanya bergaya sama (dua undian gaya favorit,
mesin berbeda) → cukup ganti prompt versi 2 jadi `PROMPT_ANIME`.

## 14. INGATAN KEMACETAN (16 Okt 2026)
`gpt-image-2` memulangkan **524 tiga kali berturut-turut** saat tiga sampel dibuat (semuanya diselamatkan
mesin kedua). Setiap percobaan gagal membuang ±60 detik waktu user, jadi ditambah ingatan di
`tools/cosplay.py`: setelah `AMBANG_SIBUK=2` kali 524 berturut-turut, mesin itu **didoakan** 15 menit —
mesin kedua didahulukan. Teruji: ambang → didoakan → pulih setelah sukses.

---

## 15. VERSI 2 = GAYA ELEGAN (16 Okt 2026) — permintaan user
User memilih **sampel2** sebagai rasa favorit → versi 2 diubah mengikuti rasa itu.

**Prompt baru `PROMPT_ANIME_ELEGAN`** (dipakai kandidat 2): rok **panjang penuh dengan belahan tinggi
di satu sisi** (satu kaki terlihat lewat belahan) · **bukan** rok mini · bodice ketat → pinggang ramping ·
rok tetap bervolume A-line sampai lantai · cape menyampir dari bahu · pose tenang: berdiri tegak, satu
tangan di pinggul, dagu sedikit terangkat · tetap setia desain (armour, gown, cape, trim metalik) ·
realistis (bukan anime) · kunci identitas + **kacamata wajib tetap**.

**Hasil uji (2 kandidat sekali jalan):**
| | Mesin | Waktu | Realism | Ciri |
|---|---|---|---|---|
| Versi 1 (glamor) | gemini-3.0-pro-image (utama) | **44 dtk** | 7/10 | belahan lebih tinggi, glamor |
| Versi 2 (elegan) | gpt-image-2 | 84 dtk | **8/10** | **"sangat mirip" sampel2** ✓ + sepatu bot perak ✓ |

**Enggine utama dibalik** (lihat §14): gemini jadi utama karena gpt-image-2 0/5 sukses sehari penuh.
Sesudah dibalik: kandidat 1 selesai 44 dtk (dulu 126 dtk karena menunggu mesin ngadat).
Bisa dibalik tanpa ubah kode: `MOTIONBOT_COSPLAY_ENGINE` / `MOTIONBOT_COSPLAY_ENGINE2` di `.env`.

Bukti: `BUKTI-COSPLAY/UJI_ELEGAN.jpg`

---

## 16. PELAJARAN DARI TES USER (16 Okt 2026) — job #52
User mengirim **foto karakter BARU** lewat "📸 foto baru" (bukan Arunika) → job #52 jalan ✓
(foto base jadi 987 KB, tidak cocok dengan karakter mana pun yang tersimpan).

**Tiga cacat yang ketemu dari tes itu:**

1. **Restart bot = job dirender ULANG dari nol.** Nama berkas dulu memakai detik (`cosplay_<detik>_1_...`),
   jadi saat bot di-restart di tengah job, run baru memakai nama berbeda → `edit()` tidak melihat
   berkas lama → kandidat 1 dirender ulang (44 dtk terbuang; job #52 total jadi ±8 menit).
   **PERBAIKAN:** nama berkas pakai **id job** (`cosplay_job52_1_langsung.png`) → hasil yang sudah jadi DILEWATI.
   Bot meneruskan `kunci=f"job{id}"` ke `COSPLAY.cosplay(...)`.

2. **Batas waktu 420 detik terlalu sabar.** Kandidat 2 job #52 menggantung ±7 menit menunggu
   `gpt-image-2` yang mengantre (bukan error, jadi tidak memicu cadangan sampai timeout).
   **PERBAIKAN:** default `timeout` 420 → **180 detik** (permintaan normal 31–84 dtk).

3. **Teks mesin di bot salah** ("GPT Image (utama)") setelah urutan dibalik.
   **PERBAIKAN:** jadi "🤖 Gemini (utama) + GPT Image (cadangan)".

**ATURAN BARU:** jangan restart bot selagi ada job berjalan. Cek `pending_jobs()` dulu.
