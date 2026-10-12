# RISET: CHARACTER SHEET untuk Kreeaimotion
> 12 Okt 2026 · **semua angka di sini = hasil uji nyata di akun RunningHub kita**, bukan tebakan

---

## 0. JAWABAN SINGKAT (cara terbaik)

**Sheet 3-view (depan / samping / belakang) dibuat SEKALI, lalu setiap render memakai
POTONGAN view yang cocok — bukan menyodorkan sheet utuh sebagai gambar referensi.**

Kenapa bukan sheet utuh? Karena Wan Animate memakai **SATU** gambar sebagai *identity anchor*,
dan pipeline kita sendiri **memotong area WAJAH** dari gambar itu (`FaceMaskFromPoseKeypoints`)
sebelum masuk conditioning. Kalau yang dikirim sheet 3-panel, crop wajahnya kacau → hasil
justru lebih buruk daripada kirim 1 foto bagus.

Jadi fungsi sheet = **indeks sudut pandang + penyeragaman** (background bersih, pose netral,
cahaya konsisten, skala terkunci), **bukan** gambar referensi untuk ditebar mentah.

---

## 1. BUKTI UJI (2 run nyata, akun RH kita)

| # | Input | Workflow | Hasil | Waktu | Biaya |
|---|---|---|---|---|---|
| 1 | gambar bawaan workflow | `1962303327478464513` — Qwen-Image-Edit **Q8_0 GGUF** + Lightning 8-step | sheet **1344×768**, 3 view sejajar (depan/samping/belakang), background bersih, tanpa cacat besar | 56 dtk | **50 koin** |
| 2 | **foto kita sendiri** (upload → override `nodeId 96`) | sama | sheet 1344×768, **karakter tetap sama**, 3 view, sejajar | 144 dtk | **56 koin** |

- Rata-rata **±53 koin ≈ Rp 235** per sheet (asumsi 36.000 koin = Rp 160rb → Rp 4,4/koin).
- Saldo koin: **24.737** (turun 106 untuk 2 uji).
- ✅ **TEMUAN PENTING: workflow PUBLIK bisa dijalankan lewat API kita, cuma bermodal `workflowId`.**
  Tidak perlu menyalin dulu ke akun. Artinya kita bebas memakai workflow bagus milik orang lain.
- Verifikasi visual (vision): uji#1 → 3 view sejajar, head-top & garis kaki sejajar, background
  bersih, cacat minor cuma pose lengan di view belakang. Uji#2 → karakter hasil **konsisten**
  dengan input (badge helm & tali tas sedikit beda antar view).

---

## 2. KENYATAAN TEKNIS DARI WORKFLOW KITA SENDIRI

`wf/2013996160695930881.json` (46 node, workflow inti Kreeaimotion):

- Model: `Wan22Animate/Wan2_2-Animate-14B_fp8_scaled_e4m3fn_KJ_v2.safetensors`
- LoRA saat ini: `WanAnimate_relight_lora_fp16.safetensors` (relight)
- Jalur referensi: **`LoadImage #55`** → `ImageResizeKJv2` → `ImageCropByMaskAndResize` +
  `FaceMaskFromPoseKeypoints` → `ImageConcatMulti` ×2 → **`WanVideoClipVisionEncode` ×2** →
  `WanVideoAnimateEmbeds`
- Video pemandu: `VHS_LoadVideo` (#72) → `DWPreprocessor` (pose) 
- **Konsekuensi:** referensi = 1 orang, dan ada tahap ekstraksi mask wajah → sheet multi-panel
  tidak boleh dikirim mentah (lihat §0).

---

## 3. ARSITEKTUR YANG DIREKOMENDASIKAN

### Tahap 1 — bikin sheet (sekali per karakter)
- Input: 1–5 foto dari user → unggah ke RH (`/openapi/v2/media/upload/binary`)
- **Workflow A (cepat & murah):** `1962303327478464513`
  Qwen-Image-Edit Q8_0 GGUF + `Qwen-Image-Edit-Lightning-8steps` · latent 1344×768 ·
  KSampler 8 step cfg 1 · prompt bawaan: *"create with this character a character sheet
  turnaround, front view, side view and back view"* → **50 koin / ±1 menit**
- **Workflow B (kualitas terbaik):** `2093154602467319810`
  `qwen_image_edit_2511_bf16` + LoRA **`Three-view drawing_qwen_image_edit_2511`** +
  Lightning-4steps · **3 sampler (4/6/8 step)** = 3 varian sekali jalan
  → pakai **prompt profesional** (lihat `prompt-sheet-3view.txt`, 1.231 karakter):
  menegakkan kanvas/kamera/skala sama, tinggi kepala sejajar, telapak kaki sejajar,
  proporsi sama, background putih murni
- Output: sheet 1344×768 → **POTONG jadi 3 sel 448×768** + 1 crop wajah (simpan semua)

### Tahap 2 — pilih view saat render (otomatis)
Deteksi framing video pemandu (rasio tinggi orang di frame dari pose keypoints):

| Video pemandu | View sheet yang dipakai |
|---|---|
| close-up / bicara | crop wajah (atau view depan) |
| medium / full-body menghadap kamera | **depan** |
| profil / jalan menyamping | **samping** |
| membelakangi kamera | **belakang** |

→ kirim potongan itu ke **`LoadImage #55`**. Hasil: identitas konsisten **dan** sudut cocok.

### Tahap 3 — tuning konsistensi
Resep LoRA dari workflow publik terbukti (`1973232104739835906`, "Wan2.2 animate Change
character or background V1.1", 137 node, `wan2.2_animate_14B_bf16` + sageattn):

| LoRA | Strength | Fungsi |
|---|---|---|
| `lightx2v_elite_it2v_animate_face.safetensors` | **1,0–1,2** | konsistensi wajah + akselerasi (lightx2v sudah built-in) |
| `WAN22_MoCap_fullbodyCOPY_ED.safetensors` | **0,35–0,5** | condong ke karakter **gambar referensi** (kunci "pakai karakter saya") |
| `WAN22_MoCap_fullbodyCOPY_ED.safetensors` | 0,7–1,0 | condong ke karakter **video pemandu** |
| `Wan2.2-Fun-A14B-InP-Fusion-Elite` | 0,65 | detail/tekstur |
| `FullDynamic_Ultimate_Fusion_Elite` | 0,7 | dinamika |

- **Batas durasi (penting):** penulis workflow itu mengukur konsistensi mulai luntur
  di **±10 detik**, dan menyarankan **≤20 dtk, maksimal 30 dtk**. Di atas itu degradasi tak terduga.
  → tier **`full`** kita (sampai 60 dtk) sebaiknya **dipecah per segmen** lalu disambung,
  atau diturunkan capnya.
- Prompt hygiene: deskriptor gaya/cahaya harus sama di setiap klip.

---

## 4. YANG JANGAN DILAKUKAN

1. ❌ Kirim sheet utuh (3 panel) sebagai referensi — crop wajah kacau, bisa muncul dobel/ghosting.
2. ❌ Render >30 detik sekali jalan dengan 1 referensi — konsistensi luntur.
3. ❌ Gabung 2 karakter dalam 1 gambar referensi.
4. ❌ Pakai foto input resolusi rendah / wajah <150 px — sheet-nya ikut jelek.
5. ❌ Campur view yang salah (video duduk dekat kamera tapi dikasih view belakang full-body).

---

## 5. UX BOT + MODEL DATA

Menu baru **🧑 Karakter Saya**:
- **➕ Buat karakter** → kirim 1–5 foto → bot bikin sheet → tampilkan → "simpan & beri nama"
- **🎬 Pakai karakter** → pilih nama → kirim video/link pemandu → render
- **🗑️ Kelola** (ganti nama / hapus) — batas **3 karakter** per user (mode normal)

```sql
CREATE TABLE IF NOT EXISTS characters (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id     INTEGER NOT NULL,
  name        TEXT    NOT NULL,
  sheet_path  TEXT,              -- sheet penuh 1344×768
  views_json  TEXT,              -- {"front": "...", "side": "...", "back": "...", "face": "..."}
  thumb_path  TEXT,              -- thumbnail buat tombol/menu
  created_at  INTEGER,
  last_used   INTEGER DEFAULT 0
);
-- + kolom baru: jobs.character_id INTEGER DEFAULT 0
```

**Harga:** bikin sheet = **1 credit** (biaya asli ±53 koin ≈ Rp 235) · render motion **tidak berubah**.

---

## 6. RENCANA EKSEKUSI (urut)

1. **Uji workflow B** (`2093154602467319810`, 2511 + LoRA + prompt profesional) → banding kualitas
   vs A → pilih yang dipakai produksi (3 varian per run = pilihan lebih baik, biaya ±3×)
2. **Potong otomatis** sheet → 3 sel + crop wajah + thumbnail
3. **Pemilih view otomatis** dari pose video pemandu
4. **Tabel `characters` + handler bot** (alur 3 langkah di §5)
5. **LoRA konsistensi** (`lightx2v_elite_it2v_animate_face` @1,1 + `WAN22_MoCap_fullbodyCOPY_ED` @0,4)
   → uji A/B: kualitas naik? kecepatan turun berapa?
6. **Cap durasi `full`** ≤20–30 dtk atau mode segmen

## 7. UPGRADE LANJUTAN (kalau dibutuhkan)

- **Multi-referensi:** workflow publik `2053304622248407042` ("Wan2.2 Animate Ultimate Plus V5",
  212 node, **7 × LoadImage**) → kirim 3 view sekaligus, plus "multi-proportion pose alignment".
  Catatan: pakai node custom `WanAnimatePlus`, jadi ekspos-parameter lewat API terbatas.
- **Sequential frame reference:** buat loop netral 5–10 frame dari sheet (image→video) lalu
  pakai loop itu sebagai anchor — lebih tahan untuk klip panjang / banyak klip.
- LoRA per karakter (latih khusus) — mahal & lama, belum layak sekarang.

---

## 8. REALISME: tekstur kulit + video rasa iPhone (riset lanjutan, 12 Okt)

### 8.1 Temuan pahit yang harus diketahui
Dua workflow "skin texture" terpopuler di RH diuji nyata:
(`2108844379510251521` *Skin Texture King* dan `2102285699730214913` *De-AI Look* — **29 koin**, 72 dtk):

- Hasilnya kulit **malah makin mulus**, bukan berpori. Prompt internalnya justru:
  *"dry skin, clean skin"* dan *"脸部干净轻微修图不要任何雀斑污点伤痕"*
  (= wajah bersih, retouch ringan, **tanpa jerawat/bercak/pori**) → itu estetika *beauty* pasar CN.
- Penilaian mata (vision) pada hasil: **3/10** (De-AI) dan **4/10** (SeedVR2) untuk realisme.
- 🔴 **Kesimpulan: kelas workflow ini TIDAK BISA menciptakan pori-pori dari gambar AI.**
  SeedVR2 (36 koin, 88 dtk) = **pemulih**, bukan pencipta detail.

### 8.2 Aturan realism yang benar
1. **Pori-pori hanya bisa berasal dari FOTO ASLI.** Kalau sumbernya foto asli, detailnya sudah ada —
   tugas pipeline = **jangan menghapusnya** (hindari pass yang "menghaluskan").
2. ⚠️ **Telegram mengompres foto** (sisi panjang ≤1280 px + re-encode JPEG) → pori-pori **hilang sebelum
   sampai ke bot**. → **Bot WAJIB menyuruh user kirim foto sebagai FILE/dokumen**, bukan foto biasa.
   Gratis, efeknya besar.
3. **Resolusi render = penghambat utama.** Output sekarang 464×832 → wajah ±200 px → pori mustahil ada.
   Node `WanVideoAnimateEmbeds` kita = **(512, 912)** → bisa dinaikkan ke **720×1280** (≈2× piksel,
   ≈2× koin & waktu). Wajib untuk mode realistis.
4. Model & step: naikkan dari `fp8_scaled` ke **bf16** + step sampler **6–8** (sekarang 4) + LoRA
   `lightx2v_elite_it2v_animate_face` @1,1 & `WAN22_MoCap_fullbodyCOPY_ED` @0,4.
5. **Rasa "kamera iPhone" itu urusan POST-PROCESS (ffmpeg lokal), bukan model.** Lihat 9.3.

### 8.3 Rantai iPhone-look — SUDAH DIUJI & DIUKUR (lokal, 0 koin)
```
minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1   # 30fps halus (default iPhone)
scale=928:1664:flags=lanczos                                          # 2× resolusi
unsharp=5:5:0.9:5:5:0.0                                               # ketajaman komputasional
eq=contrast=1.05:saturation=1.05                                      # warna
noise=alls=6:allf=t+u                                                 # BUTIR SENSOR (kunci!)
vignette=PI/5.5                                                       # karakter lensa
```
Hasil ukur (frame identik, skala identik, base = naik-res saja):

| Metrik | naik-res saja | + iPhone-look | Delta |
|---|---|---|---|
| Ketajaman (energi tepi) | 18,16 | **20,78** | **+14%** |
| Derau temporal / butir sensor | 1,39 | **2,62** | **+88% (1,88×)** |

Waktu proses di VPS: ≈**4,7× durasi klip** (klip 20 dtk ≈ 95 dtk) — jalan di VPS, **tidak pakai koin**.
Catatan: `fps=30` tanpa interpolasi = frame kembar (gerakan tetap patah-patah) → **wajib `minterpolate`**
kalau mau rasa video HP asli. Tambahkan butir **SETELAH** interpolasi (kalau sebelum, butir ikut dihaluskan).

### 8.4 Arsitektur mode **"Realistis"** (rekomendasi)

| # | Tahap | Alat | Biaya |
|---|---|---|---|
| 1 | Foto asli dikirim sebagai **file** | user | Rp 0 |
| 2 | Sheet + crop wajah resolusi tinggi | Qwen-Image-Edit 2511 + LoRA 3-view (workflow `2093154602467319810`) | ±50 koin |
| 3 | Render Wan Animate **720×1280**, model bf16, step 6–8, + LoRA wajah/konsistensi | RunningHub | ±2× koin tarif normal |
| 4 | Pemulih detail video/gambar | SeedVR2 (`1962513607676309506`) | ±36 koin |
| 5 | **iPhone-look** | ffmpeg di VPS | Rp 0 |
| | | **Tambahan** | **±86 koin ≈ Rp 380** |

→ Jual sebagai **tier premium** (+1 s.d. +1,5 credit dari tarif normal). Tier normal tetap seperti sekarang.

### 8.5 Jangan tertipu
- Jangan janji "pori-pori dari AI" — yang bisa dijual: **mempertahankan** detail foto asli + resolusi
  tinggi + kamera-look. Kalau user kirim foto hasil AI / foto terkompres, hasilnya tetap plastik.
- Jangan pakai pass "beauty/clean skin" untuk mode realistis (itu justru menghapus tekstur).

---

## 10. LATAR BELAKANG ASLI (bg_images) — temuan & tembok, 12 Okt

**Hipotesis:** model kita menghalusinasi ulang SELURUH ruangan (cermin nggak memantulkan orangnya,
ubin palsu, LED mekar palsu). Kalau `bg_images` diisi frame video asli, latar tetap footage asli
(noise sensor asli, pantulan asli) — ini kunci rasa "rekaman HP".

**Fakta node kita (`#84 WanVideoAnimateEmbeds`):** `bg_images`, `mask`, `face_images`,
`start_ref_image` **KOSONG**; `colormatch` = `disabled`; `pose_strength` 1.1, `face_strength` 1.

**Workflow publik yang SUDAH tersambung lengkap:** `1973232104739835906` ("Change char/bg V1.1",
137 node) — `ref_images` ← #225, `pose_images` ← #226 (`DrawViTPose`), `face_images` ← #227
(`PoseAndFaceDetection`), **`bg_images` ← #228 (`DrawMaskOnImage` ← `BlockifyMask` ← SAM2 +
GroundingDINO #59 prompt `'dancer'`)**, `mask` ← #229.

**Uji nyata:** dijalankan via API kita dengan override `#91 image` (foto kita), `#114 video`
(video pemandu), `#114 frame_load_cap=81`, `#59 prompt='person'` → **SUCCESS 379 dtk, 150 koin**,
tapi `/task/openapi/outputs` balik **`data: []`** (kosong).

**Sebabnya ketemu:** semua node output workflow itu (`#239`, `#284`, `#301 VHS_VideoCombine`)
punya `save_output = False`, jadi RH tidak menandai ada output. Percobaan menyalakan lewat
`nodeInfo` **DITOLAK**: `NODE_INFO_MISMATCH(nodeId=284, reason=node_not_found_in_workflow)` —
node di dalam grup/loop tidak bisa dialamatkan lewat API.

**Tembok lain:** ambil hasil lewat web RH juga mentok — `/api/task/detail`, `/api/openapi/task/detail`,
`/api/task/taskDetail` semua `403 TOKEN_MISSION` walau sudah login (cookie + token `Rh-Comfy-Auth`
di localStorage tidak cukup); `/workspace` dan `/ai-apps` halaman SPA kosong saat dibaca headless;
endpoint daftar AI App (`/api/search/webapp`, `/api/search/aiApp`, dst) **404**;
`/api/aiapp/list` ada tapi `403`.

**Kesimpulan praktis:** workflow publik yang butuh node output di dalam grup **tidak bisa dipakai
bot lewat API** (hasilnya tak terambil). Untuk memakai ide `bg_images`, harus **punya workflow
sendiri** yang: (a) `bg_images` + `mask` tersambung dari video asli, dan (b) node output di level
atas dengan `save_output=True`. → Perlu **fork/replikasi workflow itu ke akun kita lalu ubah lewat
editor RH**, bukan sekadar nodeInfo.

**Alternatif yang tidak butuh fork:** komposit lokal — segmentasi orang (bisa via workflow RH murah)
+ tempel karakter AI ke atas frame video asli pakai ffmpeg (risiko: tepi rambut kasar).

---

## 9. CATATAN OPERASIONAL

- Endpoint berguna: `POST /api/search/workflow` (param `search`), `POST /api/workflow/export`
  (param `workflowId`, tanpa login, wajib Referer/Origin), `/task/openapi/ai-app/run` (webappId),
  `/uc/openapi/accountStatus` (**cek saldo koin** — bisa dipakai bot buat alarm koin menipis).
- Niche "character consistency" di RH = **paling rame (2.121 workflow)** → bukan celah pasar,
  tapi **fitur bot** (UX + alur) tetap pembeda.
- Skill GUI: `telegram-desktop-gui-automation`.

## KANDIDAT "METODE TERBAIK" — hasil survei katalog RunningHub (12 Okt 2026)
Disurvei saat riset proporsi diparkir. Belum ada yang diuji; ini daftar bahan mentah.
Semua ID = workflow RunningHub (cek grafiknya lewat /api/workflow/export sebelum dipakai).

**A. TURNAROUND / MULTI-VIEW (pengganti langsung sheet sekarang = 1962303327478464513)**
- `2071975841445269506` Three views Qwen2511 High consistency  ← kandidat TERKUAT (keluarga
  Qwen-Edit-2511 yang sama dengan sheet kita, tapi sudah versi "high consistency")
- `2098329707967168513` Multi-Angle Workflow | Qwen Image Edit Consistent Multi-View
- `2072999837630767104` Generate multi-view character images — Consistent character kit
- `2067830775218786305` Three views (four views)

**B. 3D / MESH — paling anti-drift proporsi (foto → mesh → render beberapa sudut)**
- `2074612521968955394` Hunyuan3D Multi-view generates glb model
- `2069669394275454978` Hunyuan3D 2.0 Multi-view Model Generation (Texture version)
- `2003825166566236162` TRELLIS.2 (Microsoft, open-source)
- `2060178512773992449` Image to 3D Model [Plus Mode] (Pixal3D)
Catatan: jalur ini menjamin proporsi & siluet KONSISTEN antar sudut (mesh = satu benda yang
sama), tapi butuh langkah render mesh → gambar, dan hasil "3D-ish" harus diuji dulu.

**C. FRONTIER IMAGE (konsistensi identitas paling jago menurut reputasi umum)**
- `2097867666316185602` nano banana2 & pro create package mold
- `2096806165706498049` Nano Banana generates models (masked version)

**D. POSE / CONTROL — mengunci proporsi (bukan menyerahkan ke model)**
- `1996350694477152257` Create Z image Controlnet union pose/depth/sketch/redraw four-in-one
- `1996144706801352706` Z Controlnet pose control
- `2108557946895474690` Pose Control 4K | Outfit Transfer Posture Workflow
- `2001253005766914050` SCAIL SDPose Uni3C Action (transfer aksi/pose)

**E. IDENTITY (jaga muka antar view)**
- `1846037353528705026` Multi-angle consistent realistic characters_PuLiD  ← paling relevan
- `1978028146278674434` IPAdapter face swapping
- `1930521704227880961` IPAdapter Face Refinement Real Person to 3D

**Urutan uji yang disarankan kalau riset dilanjutkan:**
1. `2071975841445269506` (paling murah: ganti mesin saja, alur bot tak berubah)
2. `2098329707967168513` atau `2072999837630767104` (bandingkan konsistensi antar-view)
3. Jalur mesh Hunyuan3D (kalau 1 & 2 masih meleset proporsinya)
