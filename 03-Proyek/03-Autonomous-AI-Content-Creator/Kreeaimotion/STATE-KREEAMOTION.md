# KREE.AI MOTION — KARTU PROYEK (STATE)

> **BACA FILE INI PERTAMA** di setiap sesi baru (termasuk setelah `/new`).
> Diperbarui tiap milestone + langsung di-commit/push. Ini yang menjaga konteks antar-sesi.
> ⚠️ TIDAK BOLEH memuat rahasia — hanya LOKASI kredensial.

---



#
#
#
#
**Verifikasi jalur produksi (job #47, 15 Okt 18:30→18:37):** `tools/uji_rambut_e2e.py` memanggil
`run_job()` asli → log membuktikan `job 47: setelan SET node 265 value=0.2` terkirim → hasil
`data/out_47.mp4` rambut panjang UTUH sampai frame terakhir, setara uji T2. T1 (setelan lama) tetap
rusak di ekor. Bukti gambar: `BUKTI-RAMBUT/perbandingan_T1_T2_T3.jpg`.
Catatan: bot sempat di-restart saat render jalan dan **mengadopsi task yang sama** (tidak render ulang,
koin tidak terbuang) — perilaku ini benar dan disengaja (`_adopt_job`).
Koin RunningHub: 14.817 → 13.499 (habis ~1.318 koin untuk seluruh investigasi + uji).

## 🆕 (17 Okt) GANGGUAN PENYEDIA: SEMUA MODEL GAMBAR 404 → CADANGAN RunningHub + PROTO COSPLAY SEXY SIAP

**1) GANGGUAN SISI PENYEDIA (bukan kode kita).** Mulai ±13:35, gateway Inferhub membalas
`404 unknown model` untuk SEMUA model gambar (`gemini-3.0-pro-image`, `gpt-image-2`,
`gemini-3.1-flash-image`, versi `cb/` juga) — **di dua kunci berbeda** (kunci bot + kunci provider
Hermes). Jalur TEKS tetap sehat. Katalog `/models` masih mengiklankan model itu → pola sama dengan model
video dulu: "diiklankan, tidak dirutekan". Akibatnya Generate Gambar / Ganti Baju / Cosplay mati selama
gangguan.

**2) CADANGAN OTOMATIS RunningHub (commit `e78c85f`).** Kalau SELURUH jalur Inferhub gagal (404 semua
model / timeout / 524), job TIDAK mati — otomatis pindah ke RunningHub (server & koin sendiri):
`tools/imgedit.py` (`_rh_cadangan`) + `tools/cosplay.py`. Saklar `MOTIONBOT_OUTFIT_RH_FALLBACK` (default 1).
**Teruji 2 kasus** (`tools/uji_cadangan_rh.py`, total 148 koin):
- A. Cosplay dengan acuan GAMBAR ANIME → ✅ 760x1360, 470 dtk, **92 koin**. Fakta: kacamata tetap, wajah
  masih dikenali, tetap foto (bukan gaya anime), elemen kostum ikut (putih/biru/emas, japa biru, permata
  merah, gauntlet perak, sabuk) tapi BELUM lengkap (tiara/rambut perak/gaun panjang tidak penuh), latar
  di-regenerate → layak DARURAT, di bawah jalur normal (4K).
- B. Edit berperintah dari SATU foto (kasus Generate Gambar) → ✅ 760x1352, 289 dtk, **56 koin**: gaun
  putih floral → bikini navy sesuai perintah, wajah + kacamata tetap, latar di-regenerate.
- Bukti: `data/uji_cadangan_rh/BANDING_CADANGAN.jpg`, `BANDING_EDIT.jpg`.

**3) PROTO COSPLAY "SEXY + VIBE ACUAN" — SIAP, TINGGAL RENDER.** Permintaan user: *"hasilnya sexy tapi
vibes-nya sesuai gambar anime yang dikirim"*. Desain acuan (princess-knight) itu SOPAN (rok panjang tanpa
belahan, bahu tertutup) → sexy harus DIPERINTAHKAN; vibe harus DIBACA tiap kali (user ganti gambar).
Solusi: **pembaca vibe** (model mata) mengembalikan palet/suasana/pencahayaan/latar + siluet + bagian yang
terbuka → disuntik ke prompt. Dari acuan user terbaca: "Regal princess-knight; palet royal blue/white/gold/
silver; cahaya siang terang; korset + sweetheart neckline + rok panjang + kapa terbuka". Empat register
diuji di `tools/cosplay_sexy.py`: `1_belah_tinggi`, `2_mini_depan`, `3_glamor_megah`, `4_berani` (semua
tetap: kacamata + wajah identitas, palet/mood acuan, material nyata, bukan gaya gambar). **Render 4 varian
GAGAL 404 karena gangguan** → dijadwalkan ulang otomatis: cron `616528fd9526` tiap 15 menit (tanpa LLM,
DIAM selagi turun) menjalankan `tools/cron_sexy_saat_pulih.py` → begitu gateway pulih, 4 varian dirender
dan lembar banding dikirim sendiri ke user.

**4) BUG: CADANGAN TIDAK PERNAH MENYALA (job #60/#61 gagal) — DIPERBAIKI.** Dua cacat, keduanya lolos dari
uji sebelumnya karena uji itu memanggil app RunningHub LANGSUNG (menguji MESIN-nya, bukan SAMBUNGANnya):
 (a) `edit()` memulangkan `None` begitu mesin saat itu menolak dengan kode NON-sibuk (`404 unknown model`)
     → blok cadangan di bawah loop tak pernah tercapai (cadangan cuma hidup untuk 502/524);
 (b) `os.getenv` tidak membaca berkas `.env`, jadi id app terbaca KOSONG di proses yang tidak memuat dotenv
     → cadangan dilewati DIAM-DIAM (0 dtk, tanpa satu baris log pun).
Perbaikan: `break` (bukan `return None`) saat daftar mesin habis; cadangan memuat `.env` sendiri + SELALU
mencatat kalau dilewati; `cosplay()` memakai cadangan SEKALI per job (bukan per kandidat — 2 kandidat =
184 koin kalau dibiarkan). Commit `a56324e` + lanjutannya, bot sudah restart. Diverifikasi dengan
mereproduksi job #61 PERSIS melalui `tools/cosplay.py` saat gangguan masih hidup: kedua mesin dicoba →
`CADANGAN RunningHub — task 2111358433019072513`. Pelajaran ditulis ke skill `inferhub-image-models`.

**5) PROMPT COSPLAY: DARI "SEWENANG MESIN" → BERBASIS SPESIFIKASI (perbaikan keluhan user).** Keluhan
user (17 Okt): *"bajunya tidak mirip dengan contoh anime, vibes nya harus mirip tapi versi sexy"* lalu
*"tidak mirip dengan karakter sheet gue dan hasilnya nggak sexy"*. Akar masalah: pembaca gambar (MATA)
sudah mengeluarkan spesifikasi kostum potong-per-potong, TAPI prompt hanya bilang "pakai kostum dari
gambar 2" secara umum → mesin mengarang potongan (uji-1: cuma capelet + kerah yang ikut). Perbaikan:
(a) prompt `PROMPT_ANIME_SPEK` memasukkan spesifikasi itu apa adanya + "SALIN, jangan tukar potongan";
(b) `MATA` sekarang juga mengembalikan **vibe** (palet/suasana/cahaya) yang dikunci ke hasil;
(c) 2 register sexy (`SEXY_1`/`SEXY_2`) yang menjaga potongan tapi membuka siluet;
(d) prompt ringkas untuk cadangan (`prompt_cadangan`) dengan **URUTAN PENJAGA**: identitas + kacamata di
AWAL, blok SEXY di tengah (430 char), "jangan salin wajah image 2" di AKHIR — karena medan teks cadangan
(1.600 char) memotong ekor; penataan lama (1.300 char, spesifikasi 700 + vibe 260) membuat blok SEXY dan
baris "keep her glasses" KEPOTONG → hasil uji-1 bajunya mirip tapi kacamata hilang & tidak sexy.
**Hasil uji-2 (cadangan, 47 koin):** wajah sama + kacamata tetap + rambut ikut karakter sheet, SEMUA
potongan acuan muncul (mini dress putih/trim gold/capelet/kerah tegak+bros merah/atasan bergaris/tights/
boots tan), mini + belahan tinggi (sexy) → DUA keluhan user beres. Sisa cacat: jari tangan menyatu;
sexy masih "sedang" karena capelet + kerah tegak memang menutup dada sesuai desain acuan.
Commit `f7a53c8`, `2e53359`, `edccf35`; pengawas cron kini merender alur ini lewat JALUR UTAMA begitu
gateway pulih. Bukti: `BUKTI-SPEK/BANDING_SPEK.jpg` (uji-1) + `BANDING_SPEK2.jpg` (uji-2).

**6) KOREKSI USER: "TERLALU BANYAK EDIT PROMPT SAMPAI HASILNYA NGGAK SESUAI FOTO KARTUN CONTOH".**
Diagnosis user benar. Lapisan yang gue tumpuk (spesifikasi + kunci vibe + 2 register sexy + larangan) justru
MENJAUHKAN hasil dari acuan; dan "KUNCI" identitas lama ikut mengunci **pose, sudut kamera, latar, cahaya**
→ mesin mempertahankan segalanya dari karakter sheet lalu menempelkan baju baru (HIBRIDA, bukan cosplay).
Perbaikan = `PROMPT_SETIA_SPEK` (commit `9c0e0ed`): **pemisahan bersih** — wajah + kacamata dari karakter
sheet, SEMUA sisanya (rambut, kostum, aksesori, siluet) dari kartun acuan; NOL lapisan gaya; kunci
pose/latar/cahaya dilepas; larangan "jangan dipendekkan/ditambah/dikurangi/di-redesign". Prompt ringkas
cadangan juga jadi versi setia (vibe & register sexy dibuang).
**Hasil uji-setia (cadangan, 103 koin):** yang IKUT acuan → rambut perak + twintails ✓ (pertama kali rambut
mengikuti kartun, bukan karakter sheet), tunic putih A-line ✓, trim gold hem ✓, capelet bercelah depan ✓,
kerah tegak ✓, bros permata merah ✓, atasan bergaris ✓, tights charcoal ✓, tetap FOTO ✓, kacamata tetap ✓.
Yang BELUM → **boots tan mid-calf diganti sepatu hak gelap** ✗ dan tunic **dipendekkan** ✗ (meski prompt
melarang) + ada kesan uncanny di area kacamata/telinga. Catatan: jalur cadangan memang "menafsir ulang";
versi paling setia menunggu jalur utama. Bukti: `BUKTI-SPEK/BANDING_SETIA.jpg`.

**7) JALUR FOTO DIPERBAIKI + BATAS CADANGAN TERUKUR (acuan foto cosplayer "Nami").** Acuan yang dikirim
user = **FOTO ASLI cosplayer** (bukan ilustrasi) → jalur foto. Dua cacat jalur itu diperbaiki (commit
`29c2092`): (a) kunci lama "pertahankan pose/kamera/latar/cahaya" **dibuang** (itu bikin hasil hibrida
"foto user + baju tempelan"); (b) pembaca gambar sekarang **mengisi spesifikasi outfit untuk acuan foto**
(dulu sengaja dikosongkan → mesin menebak) + **1 percobaan ulang** supaya gagal-baca tidak diam-diam
menjalankan prompt tanpa spesifikasi.
**Hasil uji (cadangan, 89 koin):** SEMUA potongan acuan muncul ✓✓ — bikini halter putih bergaris teal,
jeans denim biru low-rise, sabuk kulit hitam berstud logam + buckle bulat, rambut oranye, **tato pinwheel**,
jeruk di tangan; kacamata tetap ✓; tetap foto ✓.
**TAPI wajahnya BUKAN orang yang sama dengan karakter sheet** ✗ (mesin membangun ulang wajah dari acuan),
plus jari tangan yang memegang jeruk menyatu & wajah terlalu mulus; muncul tambahan dari karakter sheet
(latar ruang tamu, sepatu hak putih, kalung tipis).
**Kesimpulan terukur:** app cadangan RunningHub MENGUTAMAKAN penyalinan outfit dan **membangun ulang
wajah** → untuk pekerjaan yang identitas wajahnya wajib (aturan keras user), jalur cadangan TIDAK layak
sebagai hasil akhir; jalur utama (`/images/edits`) yang menjaga identitas. **Jangan bakar koin lagi untuk
menguji jalur cadangan** — pakai pengawas cron yang menunggu gateway pulih.
Gejala gangguan baru yang tercatat: `gpt-image-2` sempat balas **HTTP 503 "unable to verify api key —
try again shortly"** (verifikasi kunci pun ikut goyah, bukan cuma daftar model).
Bukti: `BUKTI-SPEK/BANDING_FOTO.jpg`.

**8) MENCARI APP YANG BENAR (bukan app lemah) — keluhan user "nggak sesuai gambar".** Katalog app diambil
lewat **POST** `/api/webapp/list` (GET → `PARAMS_INVALID`; bukan katalog kosong). Penyisiran 30 kata → **374
app unik**. Penyaring gratis sebelum bakar koin: `POST /api/workflow/export` → cari node berkelas
`RH_OpenAPI_*` (**app proxy = butuh saldo terpisah** ✗; terukur `RH_OpenAPI_SeedreamV5ProImageToImage` →
`Submit failed: Your balance is insufficient … [errorCode: 605]`, gagal SETELAH task dibuat = koin tetap
terbakar). Bentuk export ada di **level atas**, bukan di `data`.
**Diuji 17 Okt (±18:00):**
- ❌ `2075457737781235714` Seedream v5 Pro 换装 — proxy, saldo terpisah ✗
- ❌ `2075087723240714241` **Krea 2 Identity Edit** — LOKAL & identitas terjaga ✓ TAPI **salah alat**: keluarannya
  **KOLASE DUA ORANG** (foto user + cosplayer acuan berdampingan), bukan ganti baju. Sebab: **prompt bawaan
  app-nya** = *"Make an image of Girl in white pants and girl in black skirt best friend together in a bar"*
  → app itu dibuat untuk adegan dua orang. Biaya pelajaran 157 koin (1024x1024, 73 + 84).
  **Pelajaran: prompt bawaan app itu BOCORAN jujur fungsi app — baca dulu sebelum memilih.**
- ✅ DIPAKAI: `2075460030073237505` **FireRed 一键换衣服** — 16 node, lokal, **tanpa field prompt** (2 gambar
  saja: node 207 = image1 orang, 208 = image2 baju, urutan dibaca dari `LayerUtility: ImageReel`), cover
  app-nya = before/after **orang yang sama** ✓. Sedang diuji.
- Cadangan berikutnya: `1938438216678834178` Kontext Dual (150 → ImageConcanate, 153 → RMBG), `2001496602491645953`
  qwen outfit transfer (39 node), dan lapis pemulih wajah `2070874410734678017` **InstantID 换脸** (`CropFace`+`ApplyInstantID`).
**Alat baru permanen:** `tools/rh_app_run.py` (runner app generik: `--node 72:image=…`).

**9) SELESAI: APP GANTI BAJU YANG BENAR (FireRed) — DIPASANG KE BOT.** `2075460030073237505` **FireRed
一键换衣服**: 16 node, lokal (bayar koin), **tanpa field prompt** (2 slot gambar saja). Peta node dibaca dari
graf `LayerUtility: ImageReel`: **207 = image1 = ORANG**, **208 = image2 = BAJU/ACUAN**; cover app = before/
after orang yang SAMA.
**Hasil uji 2 acuan (17 Okt malam):**
- acuan **foto cosplayer (Nami)**: **1152x2064 (2,4 MP)**, **25 koin** — 1 orang ✓, wajah mirip karakter
  sheet + **kacamata tetap** ✓, SEMUA potongan acuan masuk (bikini teal-putih, jeans denim, sabuk stud +
  buckle, rambut oranye, **tato pinwheel**); jeruk (properti) tidak ikut.
- acuan **ilustrasi anime (princess-knight)**: **1152x2064**, **22 koin** — 1 orang ✓, wajah mirip +
  kacamata tetap ✓, potongan masuk: mini dress putih + trim gold, capelet, kerah tegak, **bros permata
  merah**, atasan bergaris, tights charcoal, **boots tan mid-calf** (dulu app lama menukarnya jadi sepatu
  hak ✗), **telinga elf**, twintails perak (depan masih hitam — hibrida identitas ✓); **tiara tidak ikut** ✗.
- Cacat konsisten: wajah agak mulus/"plastis", kacamata sedikit asimetris, jari tangan di pinggul menyatu,
  latar ruangan karakter sheet ikut terbawa.
**Perbandingan mesin:** app lama 760x1360 (1,0 MP) ~90 koin + prompt wajib; **FireRed 1152x2064 (2,4 MP)
22–25 koin tanpa prompt** → **2,3× lebih besar, ±3,6× lebih murah, wajah lebih mirip**.
**Pemasangan (commit menyusul):** `.env` `MOTIONBOT_OUTFIT_RH_APP=2075460030073237505` +
**`MOTIONBOT_OUTFIT_RH_NODES=207:image=orang,208:image=acuan`** — peta node kini **konfigurasi, bukan kode**,
jadi tukar app berikutnya cukup ganti `.env` (format `nodeId:field=peran`, peran ∈ orang/acuan/prompt;
app gaya lama bisa dipulihkan lewat `20:image=orang,21:image=orang,41:image=acuan,113:text=prompt`).
Bukti: `BUKTI-SPEK/BANDING_FIRERED_NAMI.jpg`, `BANDING_FIRERED_ANIME.jpg`.

**10) KOREKSI NAMA ACUAN (user, 17 Okt malam) — BELUM TUNTAS.** User menegur: *"plenger bukan frieren tolo,
nami"*. Yang terlihat di berkas (3× pembacaan penglihat, sama semua): **A** `cosplay_8886993492_1792216581.jpg`
= ilustrasi anime, **telinga runcing/elf, rambut perak panjang, dress putih trim emas, kerah tegak, capelet,
legging charcoal, boots coklat** → cocok dengan desain **Frieren**; **B** `cosplay_8886993492_1792225490.jpg`
= FOTO cosplayer, **rambut oranye gelombang, bikini garis teal-putih, jeans denim, sabuk stud + buckle,
tato pinwheel, jeruk** → **Nami**. User menyebut "bukan Frieren, Nami" — kemungkinan yang dimaksud: karakter
**milik user sendiri (disebut "arunika")** yang memakai kostum itu, atau penamaan yang berbeda dari sisi user.
**Jangan berdebat; label di kartu ini pakai "acuan A / acuan B" sampai user memutuskan namanya.** Nama karakter
TIDAK memengaruhi pipeline: app menyalin apa pun yang tampak di gambar acuan.
Bukti: `data/uji_firered/ACUAN_A_B.jpg` (A|B berdampingan).

**11) INSIDEN + PERBAIKAN: VALIDATOR "HANYA GAMBAR" MEMATIKAN JOB VIDEO (bug sendiri).** Saat membetulkan app
upscale yang mengembalikan ZIP (18:12), `rh.py` diberi validasi berbasis `PIL.Image.verify()` — itu **menolak
MP4** ✗ sehingga **job 66 (Generate Motion Control, 18:35, foto + video acuan FB 20 dtk, task
`2111413087620321282`) GAGAL 19:04** dengan *"semua keluaran task tidak bisa dibuka sebagai gambar"* ✗
(setelah task SUKSES di server). Biaya terbakar **701 koin** (11.216 → 10.515; ≈570 untuk job itu + 133 upscale HD).
**Perbaikan (commit `bb5281c`):** validator menerima **gambar DAN video** dari byte kepala (JPEG ffd8ff, PNG,
WEBP RIFF+WEBP, GIF, MP4/MOV ftyp@4, WEBM 1a45dfa3) + ukuran minimum; ZIP dibuka lalu divalidasi; prioritas
gambar→video→zip; teks/sampah tetap ditolak. Uji unit: JPEG ✓ MP4 ✓ ZIP ✗ .py ✗.
**Pelajaran penting:** bot **mengadopsi task lama** (`ADOPSI task lama <id> (bukan render ulang)`) → tidak ada
render kedua & tidak ada koin tambahan; kalau job lokal gagal padahal task sukses, **tarik hasil lewat
`task_id`** (kolom `jobs.task_id`) alih-alih render ulang. Sudah ditulis ke skill
`runninghub-ai-app-integration`.
**Status bot 19:13:** active (workers=2, poller Aulaa ✓), antrean 0, koin 10.515, job 66 `running` (menerima video ✓).

**UTANG KOIN KAMI (tracker: `data/utang_koin.json`).** Job 66 → **701 koin** kebakar karena bug kode kami
(validator hanya-gambar menolak MP4). Kredit user TIDAK terpotong (pembukuan bersih) → utang murni di sisi
koin RunningHub. **Dilunasi dari penghematan nyata**: FireRed ±65 koin/job tersimpan, app motion lebih murah
(sedang disisir), + bonus undangan RunningHub di layar referral bot. **Kalau video job 66 tidak sampai ke user,
kami render ulang atas biaya kami (±700 koin) tanpa diminta.**

**PENGAMAN BIAYA (kode, commit `bb5281c` + patch pengaman di `bot.py`).** Kalau task di server SUCCESS tapi
pemrosesan lokal gagal: bot **tidak pernah render ulang** — dia menarik ulang hasil task yang sama (0 koin),
dan kalau bot restart di tengah job dia **mengadopsi `jobs.task_id`** yang tersimpan. Aktif pada restart
berikutnya (restart ditunda selama ada job berjalan).

**TEMUAN BIAYA BESAR (17 Okt 19:2x, commit `e06de3f`).** Semua tier motion dipaksa `INSTANCE=plus`
(`MOTIONBOT_MC16/MC916/T10/T15/T20/FULL_INSTANCE=plus` — disetel 13 Okt untuk menghindari OOM mesin
default), padahal skill ini sendiri sudah mengukur instance `plus` menagih **2,4× lipat (96 vs 40 koin)**
untuk berkas hasil identik → satu render motion 20 dtk menembus **±700 koin** (bukan harga wajar).
Perbaikan: **percobaan pertama pakai instance DEFAULT**, percobaan ulang baru `plus` (keandalan tetap ada).
Proyeksi lunas utang 701 koin: **≤2 job motion** (bukti = delta `remainCoins` pada job motion berikutnya).

## 🆕 (16 Okt) FITUR 🎬 GENERATE VIDEO HIDUP + UJI MESIN KLING 3 PRO REPLICA

**1) Menu 🎬 Generate Video TIDAK LAGI PLACEHOLDER.** Alur: tekan menu → pilih karakter (atau foto baru)
→ tulis prompt gerakan → video. BEDA dari Motion Control: **tanpa video acuan**.
- Mesin: **Hailuo H3 (MiniMax H3) I2V Accelerated** app `2087081647066263554` (8.686x dipakai, sukses
  100%, rata-rata 322 dtk, 10 dtk video). Ganti mesin cukup ubah `.env` `MOTIONBOT_GV_APP/_NODES/_SET`.
- Biaya: `MOTIONBOT_GV_COST=3` credit (1 credit = Rp 1.000).
- `fill_nodes()` sekarang mendukung placeholder **`@prompt`** (dulu cuma @photo/@video/@ratio/@duration).
- Jalur video di `bot.py` ternyata SUDAH generik (digerakkan kunci model job) → tak perlu cabang baru.
- Diuji `tools/uji_gv.py` (Dispatcher aiogram asli, tanpa Telegram): **PASS** — menu merespons, foto
  tersimpan, job `gv` masuk antrean dengan prompt benar dan video acuan KOSONG.
- Commit `d31f05b`. Skrip uji **menimpa base aktif** saat menyimpan foto → base dipulihkan ke karakter
  #7 "Arunika · Kamar (Latar A)" 987 KB; skrip tes berikutnya harus simpan+pulihkan base.

**2) Uji mesin KLING MOTION CONTROL 3 PRO REPLICA** (`2101901146469191682`) dengan input job #54 PERSIS:
- **86 koin** (diukur dari selisih saldo 12.457 → 12.371) vs mesin sekarang **≈390 koin** → ±4,5x murah
- Tetapi resolusi **480x848** (mesin sekarang 720x1280) — dan klaim deskripsi app "Full HD 1080p"
  **TIDAK terbukti**. App hanya punya 2 field masukan → resolusi terkunci, tak bisa dinaikkan.
- Fakta visual: kacamata tetap ada di kedua video, rambut/pakaian/latar sama, rahang+dagu+hidung mesin
  baru lebih dekat ke foto input. Penilaian akhir = user.
- Skrip: `tools/uji_kling.py`, `tools/banding_kling.py` · bukti: `BUKTI-MOTION/out_kling.mp4` +
  `BUKTI-MOTION/BANDING_KLING.jpg` · rincian penuh: **`UJI-MESIN-KLING.md`**.

**3) PELAJARAN REALISME GAMBAR:** `GET /v1/models` = **katalog iklan, bukan ketersediaan**. Dari 6 model
yang diuji, 5 balas `404 unknown model` (`seedream-*`, `flux-*`, `nano-banana-*`, `gpt-image-2.5-*`) dan
`gpt-image-2` mati di batas 180 dtk (butuh >300 dtk). **Hanya 4 model gambar yang hidup**: `gpt-image-2`,
`gemini-3.0-pro-image`, `gemini-3.1-flash-image`, `gemini-2.5-flash-image`. Sudah dicatat di skill
`inferhub-image-models`.

**4) REALISME GAMBAR — SEBABNYA UKURAN, SUDAH DIPERBAIKI.** Mesin sama (gemini), foto & prompt sama:
diminta 1024x1536 → hasil 848x1264 (26 dtk, Rp 31); diminta 2160x3840 → hasil **3072x5504** (58 dtk,
Rp 60, berkas 17,7 MB). Panel 4K memperlihatkan tekstur kulit + helai rambut + pantulan lensa yang tidak
ada di 1,5 MP. `MOTIONBOT_IMAGE_SIZE` dinaikkan `1024x1536 → 2160x3840` (commit `ae27773`) — memakai
ukuran yang sudah terbukti di Ganti Baju. Margin 16,7x pada harga 1 credit = Rp 1.000. Batas Telegram
sudah aman (`bot.py:2564`: >9 MB → pratinjau 1600px + dokumen penuh).
**Mode gagal konten ada TIGA, jangan salah baca:** tolak cepat (`400` 1–4 dtk), **gantung** (timeout
menit padahal prompt netral 200 — ini yang terjadi pada prompt bikini di gemini), gangguan (`524`), dan
`429` "Credits exhausted" yang terbukti **transient** (30 dtk kemudian 200 lagi). Rincian + alat:
**`UJI-REALISME-DAN-BIAYA.md`**. Bug ditutup: Cosplay kini jatuh ke cadangan pada 429/500 (commit `3b7d791`).

## 🆕 RAMBUT HILANG di Motion Control — SUDAH DIPERBAIKI (15 Okt 2026)
Keluhan user: "hasil aneh, rambut tiba-tiba hilang".
**Temuan:** kerusakan ada di EKOR video (out_43: rambut panjang hilang mulai detik 14.0 → 15.1;
bahu/dada jadi kulit). Video acuan & foto sumber rambutnya utuh; dua video lain dari app yang sama
sehat → artefak AI App, bukan kode bot.
**Sebab:** AI App Pose Transfer (2083697864529678338) punya **13 field input**; bot cuma pernah
mengisi 2 (gambar + video). Default **node 265 "simulasi ekspresi" = 1.0** — dokumentasi app-nya
sendiri: *"wajah akan ikut meniru wajah video acuan"* → kepala/rambut ditulis ulang.
**Bukti uji (segmen gagal 12→15.1 dtk, foto & video sama):**
- T1 setelan lama → rambut rusak di 5.8 dtk, HILANG di ekor 6.7 dtk ❌
- T2 `265=0.2` → rambut panjang UTUH sampai ekor, kualitas lebih bersih ✅
**Perbaikan LIVE:** `MOTIONBOT_{T10,T15,T20,FULL,S1,FAST,HD}_SET=265:value:0.2` di `.env`.
Jalur baru: `MOTIONBOT_<KEY>_SET` (bisa banyak binding, dipisah `;`) = selalu DITAMBAHKAN, tidak
menggantikan CAP. Parser: `parse_caps()` di bot.py (uji: `tools/uji_cap.py`, 9 kasus lulus).
**Alat uji:** `tools/uji_rambut.py` (A/B setelan app), `tools/ukur_rambut*.py` (ukur rambut),
`tools/uji_rambut_e2e.py` (jalur produksi run_job), `tools/rh_app_inspect.py app <id>` (baca kontrak input).
**Sisa setelan yang BELUM dipakai** (bisa dinaikkan kualitas kalau perlu): 316/317 = 576×1024
(resolusi default terendah; bisa 720×1280), 264 fps=30, 300 batas frame=1200 (=40 dtk), 293 mode
pose=1, 266 getar=0.35, 271 saklar topeng=false, 348 mode keluaran=1.

## 🧑 PEMILIH KARAKTER di Ganti Baju & Ganti Pose (15 Okt 2026)
- Keluhan user: "nggak ada pilihan karakter yang gue punya" — dulu alur langsung memakai `base_<uid>.jpg`
  (karakter terakhir) tanpa memberi pilihan.
- Sekarang: tekan 👕 Ganti Baju / 🕺 Ganti Pose → keluar **tombol tiap karakter** (yang aktif diberi ✅,
  urut `last_used DESC`) + tombol **📸 Kirim foto karakter baru**. Pilih → `base_<uid>.jpg` diganti dari
  foto karakter itu (encode ulang JPEG ≤2160px) → langsung lanjut ke langkah kirim foto baju/pose.
- Callback baru: `ou:use:<id>` / `po:use:<id>` / `ou:new` / `po:new` (+ helper `_pakai_karakter`,
  `pick_char_kb(uid, prefix)`).
- **Fix penting:** `char_photo_path` sekarang menyelesaikan **path relatif ke folder bot**
  (`_path_ada`) — dulu karakter ber-path relatif bisa dianggap "file hilang" kalau cwd proses beda.
  Baris DB karakter #7 juga sudah diubah ke absolut.
- Bukti: `tools/uji_pilih_karakter.py` (Dispatcher asli + session stub) → pemilih muncul, base
  BERGANTI dan cocok dengan karakter terpilih, state pindah ke `Flow:outfit_photo`. PASS.
- Jangan tandai karakter aktif dengan membandingkan isi file — base selalu di-encode ulang sehingga
  byte-nya tidak pernah sama; pakai urutan `last_used`.

## ✂️ /start jadi SATU pesan (15 Okt 2026)
- Dulu: sambutan (4 baris) **+ pesan kedua** berisi saldo & daftar harga lengkap → user: "terlalu panjang".
- Sekarang: **satu pesan** (salam 3 baris + `💳 Saldo kamu: N credit`); daftar harga pindah ke tombol
  **💳 Saldo Credit** (`show_saldo`, satu tap dari menu).
- Bukti: harness `tools/uji_start.py` (Dispatcher asli + session stub, 0 request ke Telegram) →
  `jumlah pesan dikirim /start: 1`, 214 char. Commit `8f59e30`.

## 💰 HARGA BARU TERPASANG (14 Okt 2026) — 1 credit = Rp 1.000
- `.env`: `COST_10=3 · COST_15=5 · COST_20=6 · COST_FULL=18 · IMG_COST=1 · GEN_COST=1 ·
  REAL_COST_ADD=2 · PACKAGES=5:5000,11:10000,28:25000,57:50000`.
- Paket sekarang diatur lewat SATU baris env `MOTIONBOT_PACKAGES="kredit:harga,..."` (tidak perlu
  ubah kode lagi). Tombol tier di bot ikut otomatis dari `TIER_COST`.
- Uji E2E ulang setelah ganti harga: paket 5 credit/Rp 5.000 → poller mengkredit dalam ~4 dtk ✓.

### 🔒 PENGAMAN MODE LIVE (wajib, karena uang asli)
- **Klaim atomik** (`db.pay_credit_once`): `UPDATE payments … WHERE status='pending'` → poller dan
  tombol "Sudah Bayar" bisa jalan bersamaan tanpa dobel-credit. Diuji: percobaan kedua balik `None`
  dan saldo TIDAK bertambah.
- **Cek nominal**: kalau yang dibayar < harga order → TIDAK dikredit, admin dikabari.
- Cadangan manual tetap ada kalau API Aulaa mati.

### 🚦 STATUS LIVE AULAA
- Project Aulaa masih mode **sandbox** (transaksi balik `is_test=true`, QRIS tes `COM.TESTTEST`).
- Project ini **dipakai bersama bot Kree.AI** → begitu switch di-flip ke Live, KEDUA bot langsung
  pakai uang asli. (Riwayat: Kree.AI pernah 1 order live lunas Rp 10.000 — tes sendiri, 8 Okt.)
- Setelah switch ke Live: lakukan 1 transaksi nyata kecil (Rp 5.000) dari HP sendiri, lalu cek
  `journalctl -u kreeaimotion -f | grep topup` + tabel `payments`.

## PEMBAYARAN OTOMATIS AULAA (QRIS) — LIVE & TERUJI SANDBOX (14 Okt 2026)

- **Modul:** `tools/aulaa.py` (disalin dari bot Kree.AI) + tabel `payments` di `db.py`
  (`pay_create/pay_set/pay_get/pay_pending/pay_recent`) + poller tiap 6 dtk di `bot.py`.
- **Alur:** user ketuk 💰 Top Up → pilih paket → bot bikin order (`km<epoch><uid%100000>`) → Aulaa
  balikin invoice QRIS → bot kirim **gambar QR + tautan halaman bayar** + tombol `✅ Sudah Bayar` /
  `❌ Batalkan` → **poller** cek status tiap 6 dtk → credit masuk otomatis + user dikabari.
- **Cadangan:** kalau `AULAA_API_KEY` kosong, alur lama (QRIS statis + kirim bukti + admin approve)
  tetap jalan. Kredensial Aulaa sekarang diisi → jalur otomatis aktif.
- **Sandbox:** switch di dashboard Aulaa → transaksi balik `is_test=true`; QR-nya QRIS tes
  (`COM.TESTTEST`). Simulasi bayar: `GET/POST https://api.aulaa.co/payment-simulation`.
- **Bukti uji (`tools/uji_aulaa_sandbox.py`):** order Rp 5.000 → bayar disimulasikan →
  **poller bot sendiri mengkredit dalam ~4 detik** (log `topup LUNAS (via poller) … credit=+6.0
  saldo=106.0`), status DB `paid`, ledger `topup_aulaa km…` tercatat, saldo 100 → 106.
- **Metode aktif di project (14):** qris (min Rp 1.000), shopee_pay, linkaja, alfamart, indomaret,
  BCA/BNI/BRI/Mandiri/Permata/CIMB/Maybank/BNC/ATM Bersama VA.
- **⚠️ Catatan:** project Aulaa ini masih **sama** dengan bot Kree.AI. Pisahkan project kalau mau
  pembukuan terpisah.

## 💰 HARGA CREDIT — analisis lengkap di `HARGA-CREDIT.md`
- Biaya nyata: motion **25,95 koin/detik**; ganti baju App 41–44 koin; ganti pose App 47–48 koin;
  jalur Inferhub ±Rp 40–90 (0 koin).
- **Harga sekarang RUGI**: motion 10 dtk dijual 1 credit (Rp 455–833) tapi biayanya Rp 968.
- **Usulan:** 1 credit = Rp 1.000 → motion 10/15/20 dtk = 3/5/6 credit, motion maks 60 dtk = 18 credit,
  ganti baju & pose & gambar = 1 credit → margin 52–91%.
- Koin sebaiknya dibeli paket **Personal (Rp 3,73/koin)**, bukan Lite Plus (Rp 8,26).

## STATUS MODEL VIDEO INFERHUB (dicek 14 Okt 2026) — BELUM BISA DIPAKAI

- `/v1/models` memang mendaftar **±28 id model video** (Veo 3.1, Kling 2.1–3.0 + video-o-1/o-3,
  Seedance 1.0–2.5, Wan 2.6–3.0, Hailuo 03/2.3, LTXV 2.3 pro/fast, motion_2.0, flux-3-video) —
  tapi itu cuma **iklan katalog**, bukan ketersediaan.
- **Bukti 3 lapis bahwa video = NOL:** `GET /v1/videos` → `{"data":[]}`; halaman harga resmi →
  `Text 201 · Image 4 · Video 0`; semua panggilan `POST /v1/videos` → `404 unknown_model`, TERMASUK
  contoh dari docs mereka sendiri (`leo/veo-3.1-fast-generate-001`) dan semua prefix yang dicoba
  (bare, leo/, alias/, ali/, cc/, cb/, ocg/, grok/).
- **Jebakan:** submit tanpa prompt BUKAN tes validitas — router memvalidasi parameter lebih dulu,
  jadi model hidup & mati sama-sama balas `400 invalid_request: prompt is required`.
- **Keputusan:** video tetap di RunningHub (AI App otz). Alat pantau sudah dibuat:
  `tools/pantau_video_inferhub.py` (gratis, tanpa API key, baca halaman harga publik).
- **4 model gambar yang AKTIF** (semua sudah dipakai kecuali yang terakhir):
  gpt-image-2 ($0.136/$0.51), gemini-3.0-pro-image ($0.034/$2.04),
  **gemini-3.1-flash-image ($0.0085/$1.02 — murah, belum dipakai, kandidat cadangan ke-3)**,
  gemini-2.5-flash-image ($0.0051/$0.51).

## 🎬 MESIN ALTERNATIF: MiniMax H3 (14 Okt 2026) — lebih murah + motion control via video referensi
**Latar:** user minta *"coba bikin motion control pake minimax"* (memanfaatkan promo "MiniMax H3 gratis").

**⚠️ Promo "gratis" TIDAK berlaku di jalur kita.** Promo *"MiniMax H3 RH Enhanced — 1 bulan unlimited,
13 jam gratis/hari"* berlaku **di rhTV / RHSTORY** (produk aplikasi RunningHub), **bukan** API/workflow/AI App.
**Bukti empiris:** render 5 dtk jam **08:37 WIB** (di dalam jendela yang diklaim gratis) **tetap kena 82 koin**.
`accountStatus` → `apiType: NORMAL`.

**Mesin 1 — foto → gerak (i2v): workflow `2095423555109744641` "MiniMax H3 MAX Image-to-Video — AI photo to Motion"**
- 8 node, pakai node `RHMiniMaxH3VideoGen` (versi "RH Enhanced" milik RunningHub).
- Binding: node **1** `image` = foto · node **8** `prompt`, `aspect_ratio`, `width`, `height`, `duration_seconds`.
- Hasil uji (foto user, 5 dtk, 4 step turbo): **480×832 @24fps · 5,17 dtk · ADA AUDIO (AAC)** · 2,4 MB
- **Biaya 82 koin = 16,4 koin/detik** → **±38% lebih murah** dari mesin sekarang (otz 26,3 koin/detik),
  tapi resolusi & fps lebih rendah.

**Mesin 2 — MOTION CONTROL (gerak mengikuti video referensi): workflow `2085900381959593985`
"MiniMax H3 Reference Live Video RH Version _ Text Image Audio"**
- 20 node. Node kunci: `RHMiniMaxH3Ref2VAVideoReference` (**#9**) · `MiniMaxH3Ref2VATarget` (**#12**)
  · `RHMiniMaxH3Ref2VAEncode` (**#13**).
- Binding API: node **4** `image` (Picture 1) · node **6** `image` (Picture 2) ·
  node **8** `file` (video) + `keep_audio` + `trim_time` · node **12** `aspect_ratio`/`duration_seconds`/`width`/`height`
  · node **13** `prompt` (pakai penanda `<Picture 1>` / `<Picture 2>`).
- Pelajaran: MiniMax H3 RH Enhanced **memang multimodal** — referensi bisa **9 gambar + 3 video + 3 audio**
  → **motion control versi MiniMax ADA**, bukan cuma generasi.
- **Hasil uji ref2v (14 Okt 09:15):** ✅ video jadi — **1344×768 @24fps · 5,17 dtk · ada audio** ·
  render **±22 menit** (sampler 21 langkah) · **biaya 655 koin = ±127 koin/detik** → **±4,8× LEBIH MAHAL**
  dari mesin otz (26,3 koin/detik). ⚠️ Binding `aspect_ratio=9:16` **tidak dipakai** (hasil tetap landscape 1344×768)
  → kalau mau portrait, harus set `width`/`height` juga.
  Isi video: identitas user terjaga (rambut panjang + kacamata + dress merah), pose **berubah antar frame**
  (gerak terjadi), latar berubah jadi interior (gorden abu + sofa).
- 📌 **Kesimpulan biaya:** MiniMax i2v turbo (4 langkah) = **16,4 koin/detik (termurah)** · otz = 26,3 ·
  **MiniMax ref2v motion control = 127 koin/detik (termahal)**. Kalau mau motion control MiniMax yang murah,
  cari varian **accel/turbo**-nya (mis. `2087178020289708033` all-in-one acceleration) dan turunkan langkah sampler.

### Uji PORTRAIT + DURASI 10 DETIK (14 Okt 2026, 09:30–10:17)
Binding portrait **berhasil kalau `width`/`height` diisi eksplisit** (aspect_ratio saja tidak cukup).
| uji | hasil | biaya | waktu |
|---|---|---|---|
| i2v turbo, 480×832, 10 dtk (prompt ada push-in) | 480×832@24 · 10,1 dtk · audio | **92 koin** (9,2 k/dtk) | ±3 mnt |
| i2v turbo, 480×832, 10 dtk (**kamera statis**) | 480×832@24 · 10,1 dtk · audio | **42 koin** (4,2 k/dtk) | ±3 mnt |
| **ref2v motion control, 768×1344, 10 dtk** | **768×1344@24 · 10,1 dtk · audio** | **1.398 koin** (138 k/dtk) | **±57 mnt** |
- ⚠️ **Tagihan tidak linier**: i2v 5 dtk=82, i2v 10 dtk=92, i2v 10 dtk (v2)=42 → tampaknya dihitung dari
  **waktu GPU nyata**, bukan durasi video. Jadi **10 detik bisa lebih murah dari 5 detik**.
- ⚠️ Cacat i2v: framing masih sedikit mengetat di akhir; **warna dress bergeser** (merah→maroon), tint hijau
  di rambut, glow oranye di lengan. Ghosting berat hilang setelah prompt "static camera, no push-in".
- 💰 **Total eksperimen 14 Okt: 2.269 koin** (82+655+92+42+1.398) ≈ **Rp 12.200** (rentang Rp 8.500–18.750
  tergantung tier koin). Bonus: **+100 koin klaim harian** masuk otomatis. Sisa koin: **16.812**.
- 📄 Rincian harga koin: Lite Plus $71,9/thn→13.000 koin/bln (Rp 8,26/koin) · Personal $89,9/thn→36.000 koin/bln
  (**Rp 3,73/koin**) · Pro $139/thn→54.000 (Rp 3,85) · Pro Plus $236,9/thn→72.000 (Rp 4,91).

### 🔍 AKAR MASALAH "kacamata muncul telat + wajah berubah" (14 Okt, 12:40–13:10)
Keluhan user pada hasil MiniMax ref2v 10 dtk. Temuan dari catatan workflow sendiri:
- **"参考图不作为首帧"** (foto referensi **BUKAN** frame pertama) — rupa diambil dari foto, tapi frame awal
  dibangun dari VIDEO referensi → identitas (kacamata) baru "nyantol" di tengah sampling.
- Workflow ini aslinya untuk **DUA foto orang** (rantai: Image1 → Image2 → Video → Audio) + audio ref;
  kita mengisi foto yang sama ke dua slot = pemakaian di luar peruntukan.
- 📌 **Faktor dominan = DURASI**: klip 10 dtk drift; **klip 5 dtk dengan resep sama → kacamata muncul dari
  frame pertama, wajah konsisten, latar tidak berubah.** → **batasi klip ref2v ≤ 5–6 dtk** untuk identitas stabil.
- Portrait WAJIB set `width`/`height` eksplisit (node 12); `aspect_ratio` diabaikan.

| uji lanjutan | hasil | biaya | catatan |
|---|---|---|---|
| **otz (mesin live) portrait 10 dtk** | 576×1024@30 · 10,0 dtk · audio | **279 koin** (27,9 k/dtk) | kacamata ✓ wajah ✓ latar ✓ · ghosting ringan di tangan |
| **MiniMax ref2v portrait 5 dtk** (resep sama dgn landscape favorit user) | 768×1344@24 · 5,17 dtk · audio | **635 koin** (127 k/dtk) | identitas stabil ✓ · ghosting di tangan saat gerak cepat |
- Task: otz `2110229393807040513` · MiniMax portrait5s `2110230011737325569`.
- 💰 Biaya sesi lanjutan: **914 koin** (otz 279 + MiniMax 635) → sisa koin **15.898**.
- 🏆 **Verdict untuk produksi: `otz` menang** — 4,5× lebih murah per detik, 30fps, identitas stabil di 10 dtk.

### 🖼️ FITUR BARU: Generate Gambar (TEKS → gambar) via Inferhub — 14 Okt 2026
**Konsep:** user sekarang cukup KETIK PROMPT → gambar jadi. Tidak butuh RunningHub, **0 koin** (biaya lewat kredit gateway Inferhub).
- Modul baru: **`tools/txt2img.py`** (`generate(prompt, dest_dir) -> (Path, model)`, retry + model cadangan)
- Setelan `.env`: `MOTIONBOT_IMAGE_KEY` · `MOTIONBOT_IMAGE_BASE=https://api.inferhub.dev/v1` ·
  `MOTIONBOT_IMAGE_MODEL=gemini-3.0-pro-image` · `MOTIONBOT_IMAGE_FALLBACK=gpt-image-2` · `MOTIONBOT_IMAGE_SIZE=1024x1536` ·
  `MOTIONBOT_GEN_COST=0` (gratis sementara — harga final menyusul, cukup ubah .env)
- Alur bot: tombol **🖼️ Generate Gambar** → popup berisi **susunan prompt** + **contoh master karakter kucing oren Van cat**
  (mata heterochromia, pose realistis, background poskamling perumahan) → user ketik prompt → state `Flow.gen_prompt` →
  `asyncio.to_thread(T2I.generate)` → foto dikirim. Kalau user malah kirim FOTO di state itu, otomatis pindah ke jalur foto lama.
- Jalur lama (foto acuan: identitas/pakaian/latar/gaya, Qwen-Edit) tetap ada lewat tombol inline
  **“🖼️ Pakai foto sebagai acuan”** (`callback_data="gg:photo"`).
- **Model gambar yang TERBUKTI jalan di Inferhub `/v1/images/generations`:** `gemini-3.0-pro-image` (paling fotorealistis),
  `gemini-3.1-flash-image`, `gemini-2.5-flash-image` (nano banana), `gpt-image-2` (ukuran PERSIS sesuai `size`).
  Yang **404** (nama tak terdaftar di endpoint gambar): `gpt-image-1.5`, `gpt-image-2.5-flare`, `nano-banana-2`, `gemini-image-2`.
- Catatan: model Gemini mengikuti rasio tapi memakai resolusi internal (848×1264); `gpt-image-2` patuh `size` (1024×1536).
  Billing Inferhub **tidak bisa dicek via API** (endpoint billing 404) → cek dashboard mereka.
- Deploy: `systemctl restart kreeaimotion` (14 Okt) · handler terverifikasi: `img_start`, `gen_prompt_step`, `img_use_photo`.

### 👕 GANTI BAJU PINDAH MESIN → Inferhub (GPT utama, Gemini cadangan) — 14 Okt 2026
**Permintaan user:** alur seperti di ChatGPT — upload foto karakter (character sheet) + foto orang yang
memakai baju yang diinginkan → ketik `/transferoutfit` → wajah & proporsi tubuh tetap identik, baju jadi
sangat mirip foto kedua.
- **Endpoint Inferhub `/images/edits` menerima JSON** (BUKAN multipart; multipart dijawab
  `body must be JSON`) — gambar dikirim sebagai **data-URL base64** di field **`image: [url1, url2]`**.
  Bentuk ini TERBUKTI jalan untuk `gpt-image-2` (output 1024×1536) **dan** `gemini-3.0-pro-image` (848×1264).
- Modul baru: **`tools/imgedit.py`** — `edit(foto_utama, [foto_lain], prompt, dest_dir)`, mencoba 4 bentuk
  field (image/images × data-url/raw) dan otomatis pindah model kalau model utama gagal.
- `.env`: `MOTIONBOT_OUTFIT_ENGINE=inferhub` · `MOTIONBOT_OUTFIT_MODEL=gpt-image-2` ·
  `MOTIONBOT_OUTFIT_FALLBACK=gemini-3.0-pro-image`. Set `MOTIONBOT_OUTFIT_ENGINE=runninghub` untuk balik
  ke Qwen-Edit (kena koin).
- Prompt baru (Inggris, paling nurut): **`OUTFIT_PROMPT_EN`** — pertahankan wajah/identitas/kulit/rambut/
  kacamata/pose/proporsi + latar & cahaya; baju disalin hampir identik (desain, potongan, warna, bahan, motif, panjang).
- **Alur bot:** tombol 👕 Ganti Baju **atau** perintah **`/transferoutfit`**. Kalau belum ada `base_<uid>.jpg`,
  bot minta FOTO KARAKTER dulu (state `Flow.outfit_base`, disimpan jadi `base_<uid>.jpg`), baru minta foto baju.
- **UJI END-TO-END NYATA:** job #31 disisipkan ke DB → worker mengambilnya → **selesai 27 detik via gpt-image-2**
  (RunningHub lama ± 2 menit) · hasil 1024×1536 · **0 koin RunningHub** · gambar terkirim ke chat admin.
  Verifikasi: wajah sama ✓ · baju ikut acuan ✓ (catatan: celana panjang jadi celana pendek) · latar tetap ✓ · tanpa cacat.
- ⚠️ Kalau mau kesetiaan potongan baju lebih ketat, perkuat `OUTFIT_PROMPT_EN` (mis. sebut "long trousers, same length").

### ⚡ GANGGUAN ENDPOINT EDIT INFERHUB + cadangan otomatis (14 Okt 2026, ±1 jam)
- **Gejala:** `/images/edits` MATI total (gpt-image-2 & gemini: read timeout 100–200 dtk; sebagian balas
  `HTTP 502 upstream error`), padahal `/images/generations` di key yang SAMA sehat (±23 dtk). Job user #32
  nyangkut 36 menit karena ini.
- **Cadangan otomatis (sudah live):** Inferhub gagal → bot pindah sendiri ke RunningHub Qwen-Edit
  (`MOTIONBOT_OUTFIT_RH_FALLBACK=1`). Job #32 selesai lewat jalur ini (44 koin) dan gambar terkirim ke user.
- **Budget:** `MOTIONBOT_OUTFIT_BUDGET=180` detik; percobaan per model 100 detik; urutan percobaan
  MEMBOLAK-BALIK model (gpt → gemini → gpt → gemini) supaya model mati tidak menelan seluruh budget.
- **Pemutus arus:** `tools/imgedit.py::budget_efektif()` — setelah 2 kegagalan beruntun, budget dipangkas
  jadi 70 dtk selama 15 menit (biar tidak buang 3 menit tiap job saat gateway rusak).
- **JALUR /chat/completions TIDAK BISA dipakai ganti baju** (sudah diuji): Gemini di jalur itu nerima 2
  gambar & balas gambar (11–42 dtk), TAPI gambar PERTAMA dianggap kanvas — orang dulu → baju diabaikan;
  baju dulu → orangnya yang diganti (jadi ilustrasi/kartun). Prompt berlabel IMAGE 1/2 & urutan dibalik = tetap gagal.
- **Log per percobaan** ada di `/var/log/kreeaimotion.log` (`imgedit: gagal <model> / <bentuk> setelah N dtk`).

### 🏆 MESIN CADANGAN GANTI BAJU DIGANTI → AI App "Outfit Transfer + Pose + 4K" (14 Okt 2026)
Dua AI App dikirim user; hasil bedah + uji nyata dengan foto asli (2 berkas: standar + 4K):

**✅ App `2095689306085285890` — DIPAKAI (menang)**
- Isi: Qwen-Image-Edit **PLUS** FP8 + LoRA `consistence_edit_v2` / `qwen-edit-skin_1.1` / `edit_0928_lora`
  + segmentasi orang (YOLO `person_yolov8m-seg`) + **GroundingDINO SDPose** (transfer pose)
  + **SeedVR2 7B** upscale → **output 4K asli 2160×3840**.
- Node: `20` 人物图 (orang) · `21` 姿态图 (pose) · `41` 服装图 (baju) · `113` CR Text (perintah).
  ⚠️ **Baju = GAMBAR KETIGA**, bukan kedua → prompt Inferhub ("second image") TIDAK boleh dipakai di app ini;
  dipakai `OUTFIT_PROMPT_APP` (China+Inggris, menyebut 图片1/图3).
- **Biaya terukur: 40 koin dengan instance DEFAULT** (≈213 dtk) vs **96 koin kalau `instanceType: plus`**
  dengan berkas hasil IDENTIK → **jangan paksa plus** (kesalahan yang sempat kejadian di jalur worker).
- Perbandingan: 40 koin dapat 2 berkas termasuk 4K; Qwen-Edit biasa 44 koin hanya 1 berkas tanpa 4K.
- Kelebihan lain: wajah/konsistensi identitas lebih stabil (ada LoRA khusus) — dinilai dari uji panel.

**❌ App `2093156177407741953` (Seedream 5.0 Pro) — TIDAK BISA DIPAKAI**
- Gagal di node `RH_SeedreamV5ProImageToImage` (`RuntimeError`) dalam 10–31 dtk, **0 koin**,
  di semua tipe instance (`default`, `plus`, `ultra`) dan **bukan karena filter konten**
  (baju netral juga gagal). Rusak di sisi RunningHub, bukan di sisi kita.

**Rantai mesin ganti baju sekarang (live):**
`Inferhub GPT/Gemini (0 koin)` → gagal/timeout → `AI App 2095689306085285890 (40 koin, 4K)`.
Bot mengirim berkas standar sebagai FOTO + berkas 4K sebagai DOKUMEN.
Setelan: `MOTIONBOT_OUTFIT_RH_APP=2095689306085285890` (kosongkan = workflow Qwen-Edit biasa).
**Uji end-to-end job #33** (Inferhub gagal 180 dtk → app) → `state=done`, keluar 760×1352 (750 KB) + 2160×3840 (8,3 MB).

### 🕺 FITUR BARU: GANTI POSE + urutan mesin pintar (14 Okt 2026)
- **Tombol `🕺 Ganti Pose`** (+ perintah `/gantipose`) — alur sama seperti Ganti Baju:
  kalau belum ada `base_<uid>.jpg` minta foto karakter dulu (state `Flow.pose_base`), lalu minta foto pose
  (`Flow.pose_photo`) → job `model="pose"` (foto pose disimpan di kolom `jobs.photo2`).
- Dijalankan di AI App `2095689306085285890` dengan slot: **20 = orang · 21 = POSE acuan · 41 = foto orang
  sendiri** (biar baju ikut yang asli) + prompt `POSE_PROMPT_APP`. Pose TIDAK lewat Inferhub (model gambar
  di sana tidak bisa kontrol pose).
- **Pelajaran penting (hasil uji #35 vs #36):** foto acuan pose WAJIB **seluruh badan**. Uji #35 pakai frame
  selfie dari video FB (muka ketutup HP) → hasilnya wajah KEPOTONG dan pose cuma sebagian. Setelah ganti
  acuan bersih (dibuat lewat GPT Image/Inferhub generations) + prompt ditambah "keep framing, never crop the
  face" → **pose mengikuti acuan, wajah utuh, baju & latar tetap** (uji #36). Tips ini sudah ditulis di pesan bot.
- **Urutan mesin pintar** (`MOTIONBOT_OUTFIT_ORDER=auto`): coba jalur gratis (Inferhub) dulu, TAPI kalau
  endpoint itu baru gagal beruntun (`imgedit.sedang_rusak()`, 2 gagal dalam 15 menit) → **langsung** ke AI App
  supaya user tidak menunggu 3 menit sia-sia. Nilai lain: `app` (selalu AI App) / `inferhub` (selalu gratis dulu).
- **Biaya terukur:** ganti pose ≈ **40 koin** (instance default), ±4 menit, 2 berkas (760×1352 + 2160×3840 10,7 MB).
- **⚠️ PENTING — berkas 4K hanya ada kalau lewat AI App.** Mode `auto` sempat bikin user bingung
  ("file gedenya gak dikirim"): job #37 lewat jalur GRATIS Inferhub (endpoint edit sudah pulih sebagian —
  gpt-image-2 masih timeout, Gemini jalan) dan jalur itu hanya menghasilkan **1 gambar 848×1264 (±1 MB)**,
  jadi memang tidak ada berkas 4K. **Solusi: `MOTIONBOT_OUTFIT_ORDER=app`** (atas persetujuan user) →
  setiap ganti baju langsung ke AI App, selalu keluar 2 berkas termasuk 4K. Balik ke hemat: set `auto`.
- **Uji akhir job #38** (mode app): langsung ke AI App tanpa nunggu Inferhub → 825 KB + 8,7 MB (4K), terkirim
  berdua tanpa error (tidak ada log `gagal kirim berkas tambahan`).

### 🔑 PEMBALIKAN BESAR (14 Okt 2026, ±18:20): Inferhub BISA keluarkan 4K langsung
- **Probe `tools/imgedit.py` / `probe_ukuran_besar.py`:** `gpt-image-2` **mematuhi `size` PERSIS** —
  minta `2160x3840` → benar-benar **2160×3840 (4K, ±106 dtk, 7,2 MB)**; `gemini-3.0-pro-image` minta
  `2160x3840` → **3072×5504 (±125 dtk, 16,7 MB)**. Di jalur `/images/edits` pun ukuran 4K diterima.
  **Artinya 4K tidak perlu upscale dan tidak perlu koin** — cukup minta ukuran besar ke Inferhub.
- **ENV sekarang:** `MOTIONBOT_OUTFIT_SIZE=2160x3840`, `MOTIONBOT_OUTFIT_ORDER=auto` (gratis dulu; AI App
  hanya kalau Inferhub ngadat), `MOTIONBOT_OUTFIT_BUDGET=260` (4K butuh ±106 dtk per model).
- **Mutu:** hasil Inferhub **lebih setia ke baju acuan**; App 1 (Qwen-Edit PLUS) pernah **mengarang motif
  bunga daisy** yang tidak ada di foto acuan (job #39) → itu penyebab keluhan user "hasilnya aneh".
- **🐞 BUG NYATA yang ketemu (ini akar keluhan "file gedenya gak dikirim"):** `send_photo` Telegram
  DITOLAK untuk berkas > **10 MB** (`file of size 17149582 bytes is too big for a photo`) dan dulu ini
  membuat **seluruh job GAGAL** (`state=failed`) sehingga berkas besar tak pernah sampai. **Perbaikan:**
  bot sekarang **membuat pratinjau JPEG sendiri** (maks 1600 px, ±100 KB) untuk `send_photo`, lalu
  mengirim **berkas asli sebagai DOKUMEN** (semua berkas ≥3 MB; dilewati kalau >50 MB).
- **Uji akhir job #41** (mode auto, foto user): Inferhub → gemini 4K → `state=done`, 3072×5504 (16,7 MB),
  pratinjau 101 KB, **0 koin**, foto + dokumen terkirim. Hasil job #40 yang gagal juga dikirim ulang manual
  (msg 516 foto / 517 dokumen) sebagai bukti perbaikan.
  Biaya credit user tetap `MOTIONBOT_IMG_COST` (sama seperti fitur gambar lain).

**Peta 137 workflow MiniMax yang punya input video** → `scratch/minimax_video_input.json`.
Kandidat kuat lain: `2093273891489026050` (Ref-to-Video RH full-chain) · `2100492507649007617`
(Multi-Parameter, **3 video ref**) · `2089977406388338689` (1 foto + video ref) ·
`2087178020289708033` (all-in-one acceleration).
Skrip: `scratch/rh_cari_minimax.py`, `rh_bedah_minimax.py`, `rh_cari_minimax_video.py`, `uji_minimax.py`, `uji_motion_minimax.py`.

## 👕 FITUR BARU: "GANTI BAJU" (13 Okt 2026, 16:35) — LIVE
Tombol **`👕 Ganti Baju`** di menu bot: user kirim **foto baju** → keluar karakter user memakai baju itu,
sementara **wajah, tubuh, pose, dan background tetap**. Commit **`b3c3c78`**.

- **Mesin**: workflow **Qwen-Edit 2511 `2003539764081008641`** — 3 slot gambar:
  node **41** = gambar 1 (karakter) · node **79** = gambar 2 (**BAJU**) · node **81** = gambar 3 (background)
  · node **68** = prompt · node **82** = ukuran.
- `tools/imagegen.py`: `edit_image(..., photo2=, photo3=)` → slot 2 & 3 boleh beda dari slot 1
  (sebelumnya selalu diisi foto yang sama).
- DB: kolom baru **`jobs.photo2`** + migrasi idempoten di `db.py`; `new_job(photo2=)`.
- Foto base: **`data/base_<uid>.jpg`**; kalau belum ada → fallback foto terbaru user
  (`char_<uid>_*` lalu `photo_<uid>_*`). Helper `_base_photo(uid)` di `bot.py`.
- Prompt `OUTFIT_PROMPT`: jaga wajah/identitas/tubuh/pose/background + larangan pinggang-melar & kulit plastik.
- **Biaya nyata: 49 koin RunningHub per gambar (~Rp 216)** — jauh lebih murah dari motion (431 koin).
- Hasil uji (foto user + baju dari video): baju berubah ✓ · wajah sama ✓ · background sama ✓.
  ⚠️ Catatan jujur: Qwen **menggambar ulang seluruh gambar**, jadi pinggang/pinggul bisa tampak lebih
  ideal, kulit lebih halus, dan aksesori tipis (kalung) bisa hilang. Kalau mau background **piksel-identik**,
  jalurnya harus workflow try-on bermask (kandidat: `2011329691990368258` one-click outfit change 6.580×,
  `2078118953481940994` FireRed try-on 766×, `1874011612846624769` Leffa try-on 1.465×).

## 🎨 BASE + BACKGROUND (13 Okt 2026, 16:30)
Kelanjutan permintaan user: *"transfer baju udah mantep, background tolong bikinin aja biar agak mirip sama
video yang gue kirim, kedepannya gua cuma bakal ganti baju doang"* + *"kamar nggak harus 100% mirip,
justru lebih bagus agak beda tapi menarik"*.

- Vibe acuan (video FB): kamar cozy — dinding krem, lantai kayu + karpet, kasur seprai putih/abu,
  nightstand + lampu meja kuning hangat + diffuser.
- Bahan di `/root/.hermes/cache/scratch/vibes/`: `BG_strip.jpg` (strip kamar), `BAJU_ref.jpg` (baju).
- Dibuat: **2 base** (A: baju tetap · B: baju dari video) + **4 variasi background**
  (V1 Korea aesthetic · V2 jendela golden hour · V3 rak buku cozy · V4 jendela lampu kota malam).
- Skrip: `vibes/uji_gantibaju.py`, `vibes/uji_base_baru.py`, `vibes/uji_variasi_bg.py`.
- ⏳ **Menunggu user memilih base** → set jadi `data/base_8886993492.jpg` (supaya tombol Ganti Baju
  pakai base itu).

## 🥇 MESIN MOTION FINAL: AI App `otz` "Pose Transfer" (13 Okt 2026, 15:23) — LIVE
User memilih hasil uji #4 (file dibalas = md5 `b242bdf5a351ff0d5339650fde09bf3f`):
*"ini pakai mesin yang mana? mantep sih yang ini"* → mesin dipindah dari nightfunnels ke **AI App**.

**`webappId = 2083697864529678338`** · nama `动作迁移自用` / "Pose Transfer Personal Use"
- 7.843× dipakai · **sukses 97%** · ±690 dtk/run · `instanceType: plus` · tanpa password
- Output: **576×1024 @30fps**, durasi **mengikuti video referensi** (uji: 16,43 dtk)
- **Biaya nyata 431 koin/16,4 dtk ≈ 26,3 koin/dtk** (setara nightfunnels 25,9)
- ⚠️ **Keluarannya ZIP** (nama di dalam: `新V6_00001-audio.mp4`) **sudah ada audionya**

**Cara panggil**: `rh.run_app(2083697864529678338, nodes, instance="plus")`
→ `POST /task/openapi/ai-app/run` (jalur yang sama dengan Generate Gambar). Tidak pakai workflowId.
- Binding: **node `299` `image` = foto** · **node `275` `video` = video referensi**
- Field lain (opsional): 316/317 lebar-tinggi (576×1024), 264 fps (30), 300 batas frame (1200),
  293 mode pose (1), 265 ekspresi (1.0), 266 guncangan (0.35), 271 topeng (false), 356 prompt
- **Tidak ada field durasi** → durasi ditentukan oleh panjang video referensi (bot sudah memotongnya
  sesuai tier), jadi `_CAP` **dikosongkan**.

**Setelan .env** (backup: `.env.bak-13Oct-1525`):
`MOTIONBOT_{T10,T15,T20,FULL,MC16,S1,FAST,HD}_APP=2083697864529678338`,
`..._NODES=[["299","image","@photo"],["275","video","@video"]]`, `..._INSTANCE=plus`, `..._CAP=` (kosong).
`..._WF=2042526099766251522` (nightfunnels) **sengaja dibiarkan** sebagai cadangan — hapus baris `_APP`
saja untuk kembali ke nightfunnels.

**Perbaikan kode**: `rh.download()` sekarang otomatis **membongkar ZIP** (`_buka_zip_bila_perlu`)
dan mengambil file video terbesar di dalamnya — sebelumnya ZIP tersimpan sebagai `.mp4` dan
hasilnya rusak (`moov atom not found`).

### Ringkasan uji banding template (foto & video sama)
| template | hasil |
|---|---|
| **AI App `otz`** (2083697864529678338) | ✅ 576×1024@30fps · 431 koin · ada audio ← **DIPAKAI** |
| nightfunnels (2042526099766251522) | ✅ 544×960@30fps · 394 koin · cadangan |
| SCAIL SDPose Uni3C (2001253005766914050) | ❌ CRASH `OOM_KILLED` |
| CereLabs Motion Control (2080966668369932290) | ❌ "sukses tapi tak ada output" (66 koin hangus) |
| Wan2.2 Animate revolution (1969217356767653890) | ⏹ dibatalkan tapi **tetap ditagih 431 koin** |

**⚠️ PELAJARAN KEUANGAN (13 Okt 2026)**: `/task/openapi/cancel` **TIDAK mengembalikan koin** yang
sudah terpakai. Membatalkan task yang sedang berjalan hanya menghentikannya, tagihan tetap jalan
(bukti: D_wan22rev dibatalkan → tetap 431 koin). Jadi **jangan** membatalkan task untuk "hemat koin";
lebih baik biarkan selesai (hasilnya bisa dipakai) atau jangan dijalankan sejak awal.
Total uji banding 13 Okt: **21.009 → 20.118 = 891 koin** (A 394 + B 0 + C 66 + D 431).

## 🚀 MESIN MOTION SEBELUMNYA: nightfunnels (13 Okt 2026, 15:12) — dipakai ±11 menit
Keputusan user saat itu (memilih hasil uji banding `A_nightfunnels`, md5 `389400069db4d2409dda5bfd91b70d02`).

**Workflow baru: `2042526099766251522` — "Motion Control - nightfunnels.com"** (72 node)
- Mesin: **`Wan2_2-Animate-14B_fp8_scaled_e4m3fn_KJ_v2`** + `WanAnimate_relight_lora_fp16`
- Segmentasi `SeCVideoSegmentation` (SeC-4B-fp8) + deteksi pose/wajah `PoseAndFaceDetection`
  (vitpose_h + yolov10m.onnx) — otomatis, tanpa setelan manual
- Sampler hanya **3 langkah, cfg 1** (cepat) · keluaran **544×960 @30fps**
- Binding: **foto = node `391` (`image`)**, **video = node `392` (`video`)**
  · **durasi keluaran = node `341` (`value`, dalam DETIK)** ← dulu 15 (default pembuat)

**Setelan .env sekarang** (backup: `.env.bak-13Oct-1520`):
- `MOTIONBOT_{T10,T15,T20,FULL,MC16,S1,FAST,HD}_WF=2042526099766251522`
- `..._NODES=[["391","image","@photo"],["392","video","@video"]]` · `..._INSTANCE=plus`
- `..._CAP=341:value:{ref}` → **`{ref}` = durasi video referensi** (dihitung di `run_job`,
  dibatasi durasi tier). Tanpa ini video 16 dtk diminta 20 dtk → gerakan ujung membeku.
- `MOTIONBOT_MAX_FULL=30` (dulu 60): >30 dtk belum diuji, dan SCAIL sudah `OOM_KILLED`

**⚠️ BIAYA NAIK**: nightfunnels **394 koin / 15 dtk** vs workflow lama **162 koin / 20 dtk**
(≈ 2,4× lebih mahal). Harga credit ke user BELUM diubah (masih 1 / 1,5 / 2 / 4).

**Perbaikan bug**: `rh.run_workflow()` sekarang menangani `421 TASK_QUEUE_MAXED`
(menunggu & ulang) — sebelumnya langsung gagal; `run_app()` sudah punya sejak dulu.

**Hasil uji banding template (foto & video sama):**
| template | hasil |
|---|---|
| **nightfunnels** (2042526099766251522) | ✅ 544×960@30fps · 986 dtk · 394 koin ← **DIPAKAI** |
| SCAIL SDPose Uni3C (2001253005766914050) | ❌ CRASH `OOM_KILLED` (VRAM kurang, 0 koin) |
| CereLabs Motion Control (2080966668369932290) | ❌ "sukses tapi tak ada output" (66 koin hangus) |
| Wan2.2 Animate revolution (1969217356767653890) | ⏳ sedang diuji |
| AI App `otz` (2083697864529678338) | ⏳ sedang diuji |

## 🎬 WORKFLOW "VACE 14B Image-to-Video" — 盘古 (13 Okt 2026, link kedua dari user)
Sumber: `works-details/2074687679400341505` (penulis `盘古`, 2.400× dipakai, output **720×1280**).
`POST /api/creation/detail` → `contentType: WORKFLOW`, **`workflowId = 1922977171818598402`**
→ bisa dibedah & dijalankan sendiri (bukan app terkunci).

**INI BUKAN MOTION TRANSFER**: 74 node, input hanya **`LoadImage` node 210** —
**tidak ada `VHS_LoadVideo`** → foto → video (I2V), tidak bisa memakai video referensi.

**Kenapa hasilnya "realistis banget" — resepnya (patut ditiru):**
1. Mesin: `WanVideoModelLoader` **Wan2_1-T2V-14B_fp8_e4m3fn** + `WanVideoVACEModelSelect`
   **Wan2_1-VACE_module_14B_bf16** · `WanVideoVACEEncode` 832×480 · sampler 20 langkah cfg 6
2. Penajam kualitas: **`WanVideoEnhanceAVideo`** (penguat detail/gerak) + **`ColorMatch`** (mkl 0.9)
   + `WanVideoTeaCache` + `WanVideoSLG` ← kunci warna & detail tidak "plastik"
3. **Prompt otomatis**: 3× `RH_Captioner` + `RH_Prompter` + 2× `RH_Translator` + `JjkText`
4. **SUARA OTOMATIS**: `MMAudioModelLoader` (mmaudio_large_44k_v2) + `MMAudioFeatureUtilsLoader`
   (vae_44k + synchformer) + `CheckpointLoaderSimple` stable-audio-open-1.0 + `CLIPLoader` t5-base-google
   + `MMAudioSampler` (3, 40, 4.5) + `AudioCombine` → video keluar **dengan musik/ambience**
   (nama file contoh: `241-20_00001_p85-audio_*.mp4`)

**Kesimpulan peran:** link#1 (`otz`) = **motion transfer** (foto+video);
link#2 (`盘古`) = **foto→video + prompt otomatis + suara otomatis**. Dua fungsi berbeda, dua-duanya berguna.

## 💎 AI APP "POSE TRANSFER PERSONAL USE" — app motion transfer paling realistis (13 Okt 2026)
Sumber: halaman kreasi yang dikirim user `works-details/2107847068877430785` (penulis `otz`).
Kreasi itu **bukan workflow, tapi AI App**. Detail app ditemukan via `POST /api/webapp/detail {"webappId":…}`
(tanpa login pun jalan — cukup header Origin/Referer).

**`webappId = 2083697864529678338`** · nama `动作迁移自用` / "Pose Transfer Personal Use"
- **`useCount 7.843`** · 62 like · **250 koleksi** · **sukses 97%** · rata-rata **690 detik**
- `accessType 0` · `needPassword false` · `encrypted false` · app jalan di `instanceType: plus`
- Output contoh: **576×1024** · file `迁移_00001_p80-audio_nicnn_*.mp4`

**Cara panggil (SUDAH didukung kode kita)**: `rh.run_app(app_id, nodes, instance)`
→ `POST /task/openapi/ai-app/run` dengan `{apiKey, webappId, nodeInfoList, instanceType}`
(jalur sama seperti Generate Gambar / Qwen-Edit). **Tidak perlu workflowId** (`workflowId: null`).

**13 field masukan** (data mentah: `docs/apps/otz_motion_bindings.txt`, JSON: `docs/apps/otz_motion_*.json`):
| node | jenis | field | arti | default |
|---|---|---|---|---|
| **299** | LoadImage | `image` | **FOTO** | — |
| **275** | VHS_LoadVideo | `video` | **VIDEO referensi** | — |
| 316 | easy int | `value` | lebar | 576 |
| 317 | easy int | `value` | tinggi | 1024 |
| 264 | easy int | `value` | fps | 30 |
| 300 | easy int | `value` | batas frame | 1200 |
| 293 | ImpactSwitch | `select` | mode hitung pose (1) | 1 |
| 265 | easy float | `value` | simulasi ekspresi | 1.0 |
| 266 | easy float | `value` | amplitudo guncangan | 0.35 |
| 271 | easy boolean | `value` | saklar topeng | false |
| 356 | Text Multiline | `text` | prompt penguat | 最佳质量, photorealistic, 8k… |
| 348 | ImpactSwitch | `select` | mode keluaran | 1 |
| 357 | Text | `text` | node cadangan (tak terpakai) | — |

**Panduan parameter dari pembuatnya:**
- 1280×720 @30fps → **video ≤26 dtk** (disarankan <20 dtk) · 1024×576 → ≤45 dtk (<34) · 960×540 → ≤42 dtk
- **OOM bisa terjadi walau parameter sudah kecil** — kata pembuatnya: "jalankan ulang atau coba di jam lain,
  ini cuma gangguan RunningHub" (cocok dengan temuan OOM kita)
- Ekspresi: `0` = hampir tanpa perubahan wajah · `0.2` = halus (disarankan) · `1` = penuh (cepat)
- Mode hitung pose **3 jangan dipakai pemula**
- Ada opsi **video super-resolution** (2× resolusi, ~20–35 koin)

Cara menemukan app lain: `POST /api/creation/detail {"creationId":…}` → lihat `webappId`/`workflowId`,
lalu `POST /api/webapp/detail {"webappId":…}` untuk skema isian + statistik sukses.

## 0. ⭐ STATUS TERKINI — 13 Okt 2026, 10:10 WIB (BACA INI DULU; bagian di bawah = riwayat)

### 🔥 FIX OOM MOTION — instanceType tak terkirim (13 Okt 2026 14:25, LIVE)
- **Gejala**: job motion t20 **gagal** berulang (17/19/20) padahal job 18 sukses — input sama.
- **Akar masalah (dari RunningHub, bukan kira-kira)**: `POST /task/openapi/outputs` untuk task
  gagal → `data.failedReason = {exception_type: "torch.OutOfMemoryError", node_name: "WanVideoSampler"}`
  → **GPU kehabisan VRAM** di sampler Wan.
- **Sebab di kode kita**: `bot.run_job` memanggil `rh.run_workflow(wf_id, nodes)` **tanpa
  `instance=inst`** → setelan `MOTIONBOT_*_INSTANCE` (plus) **tidak pernah terkirim**; task jatuh
  ke mesin default yang padat. (Jalur `run_app` sudah mengirim, jalur workflow tidak.)
- **Perbaikan (commit `158b724`)**:
  1. `run_workflow(..., instance=inst)` — instance benar-benar dikirim.
  2. **Auto-retry**: `MOTIONBOT_JOB_RETRY=2` + jeda `MOTIONBOT_JOB_RETRY_WAIT=8` detik;
     user dikabari "🔁 percobaan N gagal, mencoba ulang otomatis…".
  3. `rh.failed_reason()` → pesan gagal menyebut sebab asli (mis. "GPU kehabisan memori").
  4. `rh.cancel()` → `/task/openapi/cancel` (buat buang task sebelum retry / saat salah kirim).
- **instanceType yang sah**: `plus`, `ultra` (balas `netWssUrl` + target host sendiri), `pro`
  (bisa balas `TASK_QUEUE_MAXED`).
- Backup: `bot.py.bak-13Oct-1341`. Service sudah direstart (14:28) dengan kode ini.

### ♾️ AKUN KITA (ADMIN) BEBAS CREDIT — 13 Okt 2026 13:50
- `bot.py`: helper **`is_unlim(uid)`** = `uid in S.admins or DBX.is_unlimited(uid)`.
  **Semua 9 titik** cek/potong credit (motion, gambar, refund) sudah pakai helper ini.
- Akun admin (`MOTIONBOT_ADMINS=8886993492`) **tidak pernah dipotong credit** —
  dan saldonya sudah di-seed **100 credit** sebagai cadangan kalau bypass dimatikan.
- Tampilan saldo admin: `♾️ Admin — bebas credit (tidak dipotong)`.
- **Credit tetap berlaku penuh untuk USER kita** nanti (bukan dihapus).
- **Uji nyata**: job motion admin → saldo **100 → 100 (potong 0)**; job user biasa →
  **12,5 → 11,5 (potong 1)** ✓.
- Cara isi saldo manual (kalau perlu): `/addcredits <uid> <jumlah>` (admin saja).

### 🧑 Karakter Saya — FOTO USER APA ADANYA (13 Okt 2026 13:45, LIVE)
- **Perubahan**: bikin karakter **TIDAK lagi render character sheet 3 view** lewat RunningHub.
  Foto yang dikirim user **langsung disimpan apa adanya** → dipakai sebagai sumber Motion Control.
  Efek: **instan (0,000 dtk; sebelumnya 63 dtk)**, **0 credit** (gerbang credit & teks biaya dicopot),
  wajah/proporsi **tidak mungkin berubah** karena tidak ada proses AI yang menyentuhnya.
- **Kode**: `_char_build_from` (tanpa RunningHub; `views={"front": foto user}`),
  `char_use` utamakan `photo_path` (foto asli; sheet lama jadi cadangan),
  `config.char_cost` default **0.0**. Commit kode **`9c9fdbe`**. Backup `bot.py.bak-13Oct-1341`.
- **Uji nyata**: kirim foto → state `char_name` + balasan foto; tombol 🧑 Pakai →
  salinan **md5 identik** dengan foto asli user (`71b52d5a…`), beda dari panel sheet (`2c525f07…`).
- `tools/sheet.py` + `MOTIONBOT_CHAR_WORKFLOW` kini **tidak dipakai bot** (tinggal CLI manual).

### ✅ CEK RUNNINGHUB — workflow motion TIDAK rusak (13 Okt 2026 13:40)
Export 6 workflow via `/api/workflow/export`; **binding node semuanya benar**:
`2106585458498420737` (t10/t15/t20/full/mc16/S1/FAST/HD) ✓ #1 LoadImage · #2 VHS_LoadVideo ·
`2013996160695930881` (mc916) ✓ #55 · #72 · `2074049787567292416` (PRO) ✓ #299 · #275 ·
`1973232104739835906` (Mode Realistis, belum di-wire) ✓ #91 · #114 ·
`2057856312750465025` (default LAMA di `tools/try_motion.py`) ada tapi **tak dipakai** ·
`2003539764081008641` (Generate Gambar) ✓ #68 TextEncodeQwen · #9 SaveImage.
→ Kalau alur motion terasa "beda dari default", sebabnya di **alur bot** (banyak fitur +
langkah pilih durasi dihapus + karakter), **bukan** di RunningHub.

### 🧠 9router — GATEWAY MODEL (13 Okt 2026, PERMANEN)
- **Apa**: gateway OpenAI-compatible yang bisa many-to-many model + fallback otomatis.
- **Service**: `9router` (systemd, `enabled`, RAM ±160 MB, dibatasi `MemoryMax=420M`).
  Port **20128** · hanya `127.0.0.1` · log `/var/log/9router.log` · data `~/.9router/db/data.sqlite`.
- **Klien**: kunci klien ada di tabel `apiKeys` DB itu (nama `kreeaimotion-bot`) —
  **JANGAN pernah tampilkan nilainya**. Base URL: `http://127.0.0.1:20128/v1`.
- **Provider terpasang**: node `openai-compatible-chat-429e8267-…` nama **Inferhub**
  (baseUrl `https://api.inferhub.dev/v1`) + 315 model kekspos sebagai `ih/<model-asli>`.
- **Combo `cerdas`** (kind chat, 5 model, urut): `ih/ali/qwen3.8-flash` → `ih/cb/gpt-5.6-luna`
  → `ih/ali/qwen3.8-max` → `ih/cb/gemini-3.1-pro` → `ih/ali/deepseek-v4.1-flash`.
  Panggil model `cerdas` = otomatis pindah model kalau ada yang mati/nolak.
- ⚠️ **WAJIB `"stream": false`** di body `/v1/chat/completions` — tanpa itu balasannya SSE
  dan `json.loads` gagal (ini pernah bikin promptcraft mentok 24 dtk).
- Login dashboard dimatikan lewat tabel `settings` (`requireLogin:false`) karena bind localhost.
- Nyalakan/matikan: `systemctl status|restart 9router`.

### 🖼️ Generate Gambar — ALUR + MUTU (13 Okt 2026, sudah LIVE)
Alur (pilihan user): **FOTO DULU** → menu minta prompt → user ketik atau tombol prompt acak →
🚀 Buat Gambar. Tampilan menu:
```
✍️ Sekarang kirim prompt-nya: ketik langsung di chat ini.

Contoh: identik wajah sama, kebaya merah, sawah pagi hari, half body 9:16,
photorealistic kulit nyata film

💡 Bahasa Inggris paling nurut — kalau bisa tulis promptnya dalam bahasa Inggris.

🎲 Prompt: <muncul di sini, otomatis berubah tiap tekan Ganti>

Saldo: 12 credit · 1 gambar = 1 credit
Hasil ±2 menit.
```
Tombol: **[🎲 Generate Prompt] → berubah jadi [🔄 Ganti]** + **[🚀 Buat Gambar]**.
- **Pilihan kelompok (Pakaian/Framing/Background/Vibe) DIHAPUS**; bank 24 prompt di
  `tools/imgmenu.py::RANDOM_PROMPTS` masih ada tapi hanya dipakai tombol acak.
- ⚠️ **PERUBAHAN 13 Okt 11:55 — PROMPT LANGSUNG KE RUNNINGHUB (default).**
  User menegur: *"kenapa kurang realistis, lu terlalu banyak bikin aturan dan nggak langsung kirim
  prompt ke runninghub"* — **BENAR**. Dulu `run_image_job` selalu memanggil
  `PC.build_final()` → prompt user dirapihkan + ditempeli aturan (kunci wajah, aturan sudut,
  aturan proporsi, pembersih teks) sebelum dikirim ✗.
  Sekarang ada saklar **`MOTIONBOT_IMG_RAW_PROMPT=1`** (default ON, di `config.py`) →
  `final = prompt user APA ADANYA`, **0 karakter tambahan**, lalu langsung ke node prompt RunningHub.
  Jalur rapihan masih ada tapi NONAKTIF (`=0` kalau mau dihidupkan); `promptcraft` kini hanya dipakai
  tombol 🎲 Generate Prompt (teks yang dilihat user).
  Satu-satunya yang masih diatur: **kanvas rasio** (kalau user menyebut 9:16 dll) — ini menyentuh
  GAMBAR, bukan teks prompt. Kalau foto masukan sudah 9:16, kanvas praktis tidak menambah apa pun.
  Kalau ternyata kanvas ini pun mengganggu keaslian, matikan dengan tidak menyebut rasio di prompt,
  atau kabari untuk dibuatkan saklar terpisah.
- **Prompt user dipahami dulu, lalu dirapihkan jadi Inggris 5 lapis** oleh
  `tools/promptcraft.py` lewat **9router** (`cerdas`) — **hasil rapihan TIDAK ditampilkan ke user**.
  Cadangan tanpa internet: kamus ID→EN berbasis token (jangan pakai `str.replace` berulang —
  dulu bikin kata rusak "tobaya"/"toep").
- ⚠️ **PERBAIKAN 13 Okt 11:30 — kunci identitas terlalu ketat (bug).**
  Dulu `promptcraft.IDENT` = *"Keep her face, **hair**, skin tone and identity exactly the same"* dan
  `SYS_PROMPT` nomor 1 = *"keep the same face/**hair**/body"* → bot **melarang** mesin mengubah rambut,
  jadi permintaan "ubah gaya rambut" / "foto dari samping" **selalu ditolak**.
  Sekarang: kunci **HANYA wajah** (`Keep the same face and facial features identical`) + 3 aturan baru:
  **ANGLE RULE** (sudut samping ditulis konkret: "profile view, turned 90 degrees"), **PROPORTION RULE**
  (bukan close-up kalau tidak diminta; kepala ±1/6 tinggi frame), **CLEAN RULE** (hapus teks UI/watermark —
  foto user sering screenshot aplikasi yang ada tulisan "MAIN VIEW (CLOSE UP)" dan dulu IKUT TERSALIN ke hasil).
  **Bukti uji nyata**: dari foto close-up DEPAN → keluar **profil 90° + rambut bob pendek** ✓ (koin −138).
- **Soal "kepala selalu kelihatan besar"**: BUKAN efek kunci rasio. Hasil ukur: hasil LAMA tanpa kunci
  = kepala **58%** tinggi frame ✗; hasil pakai kunci = **24%** ✓ (kunci justru memperbaiki).
  Penyebab sesungguhnya = **foto masukan user selalu close-up dada-ke-atas** (kepala 38%) sehingga
  komposisi itu diwarisi mesin. Solusi: minta *full body/wide shot* di prompt, atau kirim foto yang
  badannya kelihatan.
- **RASIO WAJIB IKUT PERMINTAAN USER.** Node size `#82` diabaikan mesin, jadi rasio dikunci dari
  sisi INPUT: `tools/imagegen.py::prep_canvas()` (kanvas 1080×1920, pinggir cermin+blur) →
  hasil 936×1672 = 9:16 pas. Terdeteksi dari prompt: `9:16 16:9 1:1 4:5 3:4 2:3 3:2 5:4 4:3`,
  plus kata vertical/portrait → 9:16, horizontal/landscape → 16:9, square/persegi → 1:1.
- Config `.env`: `MOTIONBOT_LLM_BASE=http://127.0.0.1:20128/v1`, `MOTIONBOT_LLM_KEY=<kunci klien 9router>`,
  `MOTIONBOT_LLM_MODELS=cerdas,ih/ali/qwen3.8-flash,ih/cb/gpt-5.6-luna,ih/ali/qwen3.8-max`.
- Biaya nyata satu gambar: ±50 koin RunningHub ≈ Rp 220 (job #8: 198 dtk, 49 koin).
- ⚠️ **Mesin JANGAN diubah tanpa perintah**: Qwen-Image-Edit 2511 `2003539764081008641`.
- ⚠️ **JANGAN pakai `pkill -f "9router …"`** — polanya cocok dengan shell pemanggil dan
  membunuh diri sendiri. Matikan lewat PID dari `ss -ltnp` atau `systemctl`.

### 🧩 Potong subjek / ganti latar (13 Okt 12:20 — alat lokal, 0 koin)
- `tools/bgswap.py` — potong subjek dari gambar → **PNG transparan** (`cutout`), lalu tempel ke latar
  apa pun: warna polos, gradient, atau foto (`composite`) + penyatu cahaya, rim light, dan bayangan.
- **PENTING**: `rembg 2.0.85` + `onnxruntime 1.31.0` sudah dipasang di `.venv` (venv jadi ±828 MB).
  Model di `/root/.rembg/models/u2net/u2net.onnx` (176 MB, diunduh sekali).
  **Kalau venv dibuat ulang, rembg+onnxruntime harus dipasang lagi**, kalau tidak `tools/bgswap.py` mati.
- Pakai `alpha_matting=True` untuk rambut — terbukti jauh lebih bersih (potongan biasa menyisakan
  halo putih + helaian rambut hilang). Biaya waktu: ±15 detik, RAM aman di server 1,9 GB.
- Skor jujur: potongan subjek **7/10** ✓; tempel ke latar warna polos bagus ✓; tempel ke **foto adegan
  ramai masih 4/10** ✗ (cahaya studio-dari-depan tidak cocok dengan latar seperti sunset) →
  untuk adegan realistis tetap pakai jalur mesin AI (RunningHub), bukan tempel.
- Belum dipasang sebagai tombol di bot (user belum minta).

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

### 🎁 Referral (SELESAI 12 Okt 2026) — anti-farming
- Bonus **2,5 : 2,5** (pengundang & yang diundang). Link `?start=ref_<id>` + menu **🎁 Kode Referral**.
- **5 lapis pengaman**: (1) `referrals.invitee_id` PRIMARY KEY → 1 akun = 1 bonus seumur hidup;
  (2) pengundang wajib user terdaftar + self-referral ditolak (dijaga di lapisan DB **dan** bot);
  (3) cap 10/hari & 30/30hari → kelebihan DITAHAN, tidak hilang; (4) bonus pengundang cair
  **setelah invitee selesai render pertama** (mode aman, `MOTIONBOT_REF_INVITER_AFTER_RENDER=1`);
  (5) gate channel komunitas (opsional, aktif setelah bot jadi ADMIN).
- Admin: `/refstats` · `/refbayar <invitee_id>`. Uji: `tools/ref_selftest.py` (21),
  `tools/ref_e2e.py` (11), `tools/ref_route.py` (8, lewat Dispatcher aiogram asli),
  `tools/ref_gate.py` (12, gate channel) = **52 lulus**.
- ✅ **Gate channel AKTIF (12 Okt 2026)**: `@kreeaimotionbot` sudah jadi **administrator** di
  `@KreeaCommunity` (nama tampilan channel = **Kreeativ Community**, 7 subscriber) — ditambahkan
  lewat otomasi GUI Telegram Desktop (xdotool+OCR, resep di skill `telegram-desktop-gui-automation`).
  Terverifikasi dari sisi Bot API: `get_chat_member` → bot `administrator`, user `creator`,
  non-member → BadRequest "member not found" (ditangkap kode = "belum join").
  `MOTIONBOT_CHANNEL=KreeaCommunity`.

### Pending / next
0. **Character sheet (hasil riset 12 Okt)** → baca `RISET-CHARACTER-SHEET.md` + `prompt-sheet-3view.txt`.
   Terbukti: workflow sheet publik jalan via API kita (50 & 56 koin, ±53 koin ≈ Rp 235), hasil 1344×768
   rapi. Arsitektur: sheet 3-view → potong per view → pilih otomatis sesuai framing video pemandu
   → kirim potongan (BUKAN sheet utuh) ke `LoadImage #55`. Sudah ada bukti di `bukti/`.
0b. **REALISME (bab 8 & 10 dokumen itu)** — sudah diuji di akun RH (24,1rb koin):
   - Upgrade kualitas TERBUKTI: bf16 + 720×1280 + 6 step = **+34% ketajaman**, biaya 1,61×
     (365 koin / 925 dtk vs 226 / 575). Caranya: override `#94 model`, `#84 width/height`, `#70 steps`.
   - **Modul baru `tools/iphone_look.py`** (sudah commit): naik-res 1080p + tajam + butir sensor +
     warna + vignette, preset ringan/standar/kuat, 0 koin, ±4,7× durasi klip. Ukur: +14–19% tajam,
     +1,88× butir.
   - **Telegram mengompres foto user** (terbukti: semua foto masuk 1280 px / ±95 KB; aslinya
     3000×4000) → bot HARUS menyuruh kirim foto sebagai **FILE/dokumen**.
   - Workflow "skin texture" RH = penghalus kulit (3–4/10), TIDAK bisa menciptakan pori.
   - `bg_images`/`mask`/`face_images` kita KOSONG (sebab latar belakang dihalusinasi); workflow
     publik `1973232104739835906` tersambung lengkap tapi output-nya `save_output=False` di dalam
     grup → tak bisa diambil lewat API. Perlu fork ke akun kita + pakai editor RH.
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

## KARAKTER SAYA (LIVE 12 Okt 2026)
- Menu **🧑 Karakter Saya** di bot: bikin sheet (cukup **foto biasa**, tak wajib FILE) → sheet 3-view
  **full-body** (depan·samping·belakang) + crop wajah dari foto ASLI → kasih nama → tersimpan.
- **Kenapa bisa "dibaca bot"**: sheet dipotong **deterministik** (bukan deteksi AI) → file per view
  disimpan di kolom `views_json`; `tools/sheet.py:pick_view()` yang menentukan file mana dipakai.
  Terbukti: potongan panel jatuh di ruang kosong antar figur (vision: "no character is split").
- Prompt penentu full-body ada di node **#97** (`prompt`) workflow `1962303327478464513`;
  tanpa prompt itu hasilnya kepotong di paha. Biaya 1× sheet ≈ 50 koin ≈ Rp 220 (~90 dtk).
- Crop wajah: **deteksi wajah OpenCV** (frontal+profil + verifikasi MATA untuk buang deteksi palsu di badan) dengan cadangan heuristik (foto badan penuh → wajah di bagian atas). Kotak dirapatkan 1,35× agar pori-pori terlihat.
- BUG yang sudah dibasmi (12 Okt): handler bukti-bayar `@router.message(F.photo)` tanpa `StateFilter(None)` didaftarkan paling awal & memanggil `step_photo()` untuk state APA PUN → foto di alur Karakter kebajak jadi alur motion. Sekarang filter ketiga handler foto saling eksklusif + ada jaring pengaman "mau dipakai untuk apa?".
- Di alur Generate, tombol **🧑 Pakai: <nama>** memakai view DEPAN & menyalin filenya ke work_dir
  (aman walau karakter dihapus) → lanjut seperti biasa (kirim video).
- Uji: `char_hub`/`char_new`/`char_step_name`/`char_pick_kb`/`char_use` semua lulus harness handler;
  8 handler karakter terdaftar; service `kreeaimotion` sudah restart.
- BELUM: mode Realistis belum di-wire ke worker (mesin `tools/realism.py` masih dipanggil manual).

## PROPORSI TUBUH (temuan 12 Okt 2026)
- **Masalah nyata**: prompt sheet lama menghasilkan figur **6,5–7 kepala** dengan kepala kegedean,
  kaki pendek, torso panjang, panggul lebar/bahu sempit (jurnal penilai visual).
- **Obatnya (TERBUKTI)**: tambahkan ke prompt — `natural adult human body proportions, about 7.5
  heads tall, correct leg-to-torso ratio, natural hip-to-waist ratio, realistic anatomy` dan ke
  negatif — `chibi, doll-like proportions, oversized head, short legs, long torso, deformed anatomy`.
  Hasil v3 vs v2 (1 run nyata, 50 koin): **~7,5 kepala**, kepala lebih kecil, kaki lebih panjang,
  bahu lebih seimbang.
- **v4 (final, terbukti)**: tambah `natural hip-to-waist ratio` → tetap 7,5 kepala, **pinggang tak
  lagi terjepit**, panggul lebih penuh, **tangan lebih rapat ke badan** (pose netral), sebaran skala
  antar-view turun 1,2% → **0,7%**. Penilai visual: "v4 decisively the better reference — v3's
  stylized waist/hip and floating arms can cause warping/morphing saat bergerak". KONFIG FINAL = v4.
- **Seberapa "digarap model"**: foto *selfie* (bukan seluruh badan) → bagian bawah tubuh **tidak ada
  di foto** → memang DIKARANG model. Karena itu tip di bot: foto seluruh badan (kepala–kaki) =
  proporsi lebih mirip aslinya. Ini informasi, bukan syarat (user tak mau ada gerbang FILE).
- **Skala antar-view sheet sudah konsisten** di v2/v3 (tinggi figur 730/729/721 & 738/734/729 px,
  sebaran ~1,2%) → tak perlu normalisasi panel.
- **Pengukur otomatis proporsi: JANGAN dipercaya.** Deteksi "garis bahu" dan "garis pisah kaki"
  dua-duanya salah pada figur ini (kaki rapat → pisah tak terdeteksi; bahu terdeteksi terlalu
  rendah). Oracle yang sahih = **penilai visual** (hitungan "berapa kepala"). Jangan bangun fitur
  dari siluet mentah tanpa verifikasi mata.
- Di tahap render, bentuk tubuh hasil lebih banyak mengikuti **video pemandu** (+ acuan karakter),
  jadi pilih video yang orangnya sepadan; rasio aspek acuan vs video juga berpengaruh.

## 🖼️ FITUR GENERATE GAMBAR — LIVE (12 Okt 2026)
**Alur**: tekan 🖼️ Generate Gambar → kirim FOTO (selfie/badan penuh, caption boleh jadi perintah) →
bot SELALU tampilkan menu pilihan → tekan 🚀 Buat Gambar → hasil di chat (±2 menit, 1 credit).
Semua pilihan OPSIONAL. Tombol: 🔄 Ganti foto · 🧹 Reset · ✍️ Tulis sendiri.

**Desain kelompok (5 opsi per kelompok — semua terkontrol, tidak tumpang tindih):**
| Kelompok | Opsi |
|---|---|
| 👗 Pakaian | 👔 Formal · 👕 Casual · 🧥 Tertutup · 💃 Seksi · 🎽 Sporty |
| 📐 Framing | 😊 Wajah · 👤 Half body · 🧍 Full body · 🪑 Duduk · 🚶 Berdiri |
| 🏝️ Background | 🏖️ Pantai · ☕ Kafe · 🏊 Kolam · 🌃 Kota malam · 📸 Studio |
| 🎨 Vibe | ☀️ Cerah · 🌅 Golden hour · 🎬 Sinematik · 💡 Studio · 🌙 Neon |
| ✍️ Tulis sendiri | teks bebas (ditambah sebagai "Additional request: …") |

**Mesin**: workflow RunningHub **2003539764081008641** "Qwen Image Edit 2511"
(27 node, 4 langkah Lightning, ±53 koin/133 detik). Override API:
`#41/#79/#81 LoadImage → image` (ketiganya diarahkan ke FOTO kita = edit 1 gambar),
`#68 TextEncodeQwenImageEditPlus → prompt`, `#82 EmptySD3LatentImage → width/height`.

⚠️ **JEBAKAN PENTING**: workflow ini punya 3 node SaveImage — `#9` = **foto hasil bersih**
(944×1664), `#100` = komposit "sebelum|sesudah", `#101` = upscale 4K yang **juga komposit**
(13 MB, 3779×4997). Bot **WAJIB ambil #9** (kode di tools/imagegen.py sudah memaksa nodeId
"9", bukan urutan pertama/terbesar). Salah ambil = user dikirimi gambar berdampingan.

**Kode**: `tools/imgmenu.py` (kelompok+perakit perintah), `tools/imagegen.py` (mesin),
`bot.py` (3 state: img_photo/img_sel/img_custom, handler `ig:*`, cabang `run_image_job`),
`db.py` kolom `jobs.prompt`, `config.py` `img_enabled/img_cost=1.0/img_workflow/img_timeout`.

**Mutu saat ini (dinilai visual)**: ganti baju/background/cahaya BERHASIL; identitas
dipertahankan tapi **kulit cenderung terlalu mulus** & kacamata agak melengkung → 7/10.
Skor sama untuk instruksi "gaun merah + pantai" (7/10). Ini batas model, bukan bug alur.
Sisa PR mutu: penajaman wajah (opsi pass kedua) atau tambah "natural skin texture, visible pores"
yang lebih kuat di prompt.

**Uji**: simulasi dispatcher 13/13 hijau (menu → foto → pilih → 🚀 → job+credit benar)
+ job #6 sungguhan lewat service → state=done → gambar terkirim (944×1664, 1,7 MB).

---

## MESIN MOTION CONTROL — DI BONGKAR (16 Okt 2026, dari keluhan wajah job #54)
Pertanyaan user: "job #54 pake mesin mana? mukanya nggak identik sama character sheet."

**MESIN:** RunningHub AI App `2083697864529678338` — **"Pose Transfer Personal Use"**
(instance `plus`, sukses 97%, rata-rata 676 dtk, sudah dipakai 8.173 kali).
Workflow di dalamnya: `2042526099766251522` ("Motion Control - nightfunnels.com", 72 node).

**Model asli di dalamnya (dari graf workflow):**
- `Wan22Animate/Wan2_2-Animate-14B_fp8_scaled_e4m3fn_KJ_v2.safetensors` → **Wan 2.2 Animate 14B**
- `WanAnimate_relight_lora_fp16` (kekuatan 1.5 — me-relight karakter ikut cahaya video)
- `clip_vision_h.safetensors` + `WanVideoClipVisionEncode` → pembaca identitas dari foto
- `PoseAndFaceDetection` (vitpose_h_wholebody + yolov10m) → deteksi pose **dan wajah**
- `SeCVideoSegmentation` (SeC-4B-fp8) → pemisah orang/latar

**13 field masukannya:** 299=image (foto), 275=video (acuan), **316=lebar, 317=tinggi**, 264=fps,
300=batas frame, 293=mode hitung pose, 265=ekspresi, 266=getar, 271=mask, 356=prompt, 348=mode output, 357=super-res.

**SEBAB WAJAH TIDAK IDENTIK (3 sebab, semua terukur):**
1. **Resolusi keluaran dibiarkan default app: 576x1024 = 0,59 MP.** App sendiri menyarankan
   1280x720 (0,92 MP). Wajah hanya dapat ~192x230 px → mustahil mirip sheet 858x1280.
2. **Foto masukan kena kompres Telegram:** 858x1280 tapi **hanya 82 KB**. Foto ini satu-satunya
   sumber identitas (lewat CLIP-Vision) → detail wajah sudah rusak sebelum masuk mesin.
3. **Model menggambar ulang seluruh frame** → rahang/hidung/mata bergeser. Atribut ikonik tetap
   (rambut pirang, kacamata kotak hitam, tanda berlian ungu ✓).

Catatan penting: node 265 = **0.2 sudah benar** (rekomendasi app). Kalau 1.0, wajah justru
**meniru wajah video acuan** → makin tidak identik.

**PERBAIKAN YANG DIPASANG (.env, tanpa ubah kode):**
`MOTIONBOT_T10/T15/T20_SET=265:value:0.2;316:value:720;317:value:1280`
→ 720x1280 rasionya **SAMA PERSIS** dengan 576x1024 (0,5625) jadi komposisi tidak berubah, +56% piksel.
`full` tetap 576x1024 karena acuannya sampai 30 dtk (720x1280 aman hanya ≤26 dtk).
Trade-off jujur: resolusi lebih besar = mesin lebih lama = **koin RunningHub lebih boros**.

**Saran untuk user (gratis, dampak besar):** kirim character sheet sebagai **FILE (bukan foto
terkompres)** dan pakai **crop setengah badan/wajah**, supaya wajahnya besar di gambar.

Bukti: `BUKTI-MOTION/BANDING_WAJAH.jpg`

### BUG: alur motion MENOLAK character sheet berbentuk FILE (16 Okt 2026) — SUDAH DIPERBAIKI
Gejala: user mengirim character sheet sebagai FILE → bot balas "Kirim FOTO ya (bukan teks)".
Sebab: handler `step_photo` (state `Flow.photo`, baris 680) hanya memeriksa `m.photo`.
Handler alur lain (cosplay `cosplay_base`, ganti baju `outfit_base`, `img_photo`) SUDAH menerima
dokumen — jadi hanya alur motion yang rusak. Ini penting karena FILE justru yang kita sarankan:
foto Telegram dikompres (job #54: 858x1280 tapi 82 KB).

Perbaikan: terima `m.document` dengan mime `image/*` (batas 20 MB), ekstensi dipertahankan
(.jpg/.jpeg/.png/.webp), balasan menyebut "(resolusi utuh — bagus untuk kemiripan wajah)".
Prompt durasi juga diubah: "💡 Kirim sebagai *FILE* (bukan foto) biar wajahnya lebih mirip".

Bukti uji `tools/uji_foto_file.py` (4 kasus, semua PASS):
- teks → ditolak, state tetap
- FILE PNG → diterima, tersimpan **84.957 byte = persis ukuran asli** (tanpa kompres), state → video
- FILE pdf → ditolak, state tetap
- FOTO Telegram → tetap diterima seperti dulu
