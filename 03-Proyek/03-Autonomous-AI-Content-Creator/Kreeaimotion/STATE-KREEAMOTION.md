# KREE.AI MOTION — KARTU PROYEK (STATE)

> **BACA FILE INI PERTAMA** di setiap sesi baru (termasuk setelah `/new`).
> Diperbarui tiap milestone + langsung di-commit/push. Ini yang menjaga konteks antar-sesi.
> ⚠️ TIDAK BOLEH memuat rahasia — hanya LOKASI kredensial.

---

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
