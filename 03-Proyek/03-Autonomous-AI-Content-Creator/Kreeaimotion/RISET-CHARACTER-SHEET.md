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

## 8. CATATAN OPERASIONAL

- Endpoint berguna: `POST /api/search/workflow` (param `search`), `POST /api/workflow/export`
  (param `workflowId`, tanpa login, wajib Referer/Origin), `/task/openapi/ai-app/run` (webappId),
  `/uc/openapi/accountStatus` (**cek saldo koin** — bisa dipakai bot buat alarm koin menipis).
- Niche "character consistency" di RH = **paling rame (2.121 workflow)** → bukan celah pasar,
  tapi **fitur bot** (UX + alur) tetap pembeda.
- Skill GUI: `telegram-desktop-gui-automation`.