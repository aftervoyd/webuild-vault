---
project: KREE.AI (Kreaibot)
status: referensi teknis — node map workflow FL2VA
tanggal: 2026-10-08
---

# 🗺️ Node Map — MiniMax H3 FL2VA (workflow `2084116925483151361`)

Sumber: `runninghub.ai/post/2084116925483151361/aiDetail` — **"MiniMax H3 FL2VA first-last frame to Video"**
oleh Quhania (13 Aug 2026) · 4.133 views / 15 likes / 31 favorites · kualitas **open-source, ada metode hapus watermark**.

JSON mentah: `minimax-h3-fl2va.json` (di folder ini). Cara ambil ulang: buka halaman workflow → tombol **Download** (**tidak perlu login**).

## 🎛️ Node penting (yang di-bind ke API)

| Node ID | Class | Fungsi | Nilai contoh | Binding API |
|---|---|---|---|---|
| **4** | `LoadImage` | **Foto FRAME AWAL** | (nama file png) | `@photo1` |
| **6** | `LoadImage` | **Foto FRAME AKHIR** | (nama file png) | `@photo2` |
| **8** | `RHMiniMaxH3FL2VAEncode` | **PROMPT teks** (format per-segmen waktu) | "0-2s: medium wide shot… 2-5s: camera pushes to close-up…" | `@prompt` |
| **7** | `RHMiniMaxH3FL2VATarget` | **Rasio + durasi + resolusi** | `["4:3", 5, 832, 480]` | rasio/durasi |
| 5 | `RHMiniMaxH3FL2VAFirstFrameCondition` | saklar **"First / First+Last"** → 1 foto = first-frame saja, 2 foto = first+last | – | – |
| 12 | `CreateVideo` | fps + audio | `[24, 8]` | – |
| 13 | `SaveVideo` | nama file + format | `["minimax_h3/fl2va_first_last_frame","mp4","h264","auto"]` | – |
| 10 | `RHMiniMaxH3DualSigmaSampler` | sampler | `[42,"fixed",50,12,3,"off",true,0.12,2,4,4]` | – |
| 2 | `RHMiniMaxH3FL2VAModelLoader` | model DiT | `MiniMax-H3-FL2VA-int8_convrot.safetensors` | – |
| 1 | `RHMiniMaxH3FL2VATextEncoderLoader` | text encoder | `qwen3-vl-32b-int8_convrot.safetensors` | – |
| 3 | `RHMiniMaxH3FL2VAVAELoader | VAE video+audio | `MiniMax-H3-video_vae` + `MiniMax-H3-audio_vae` | – |
| 9/11 | `EmptyAVLatent` / `DecodeAV` | latent + decode **video DAN audio** | – | – |
| 14 | `MarkdownNote` | panduan + link material resmi | feishu wiki | – |

## 🔑 Pelajaran penting (buat kualitas & biaya)
1. **Prompt H3 = per-segmen waktu** (`0-2s: …`, `2-5s: …`) — bukan satu paragraf. PromptSmith sudah di-upgrade ke format ini.
2. **Output ada AUDIO** (bukan video bisu) — `EmptyAVLatent` + `DecodeAV` = "Decode Video + Audio". Ini keunggulan yang bisa dijual.
3. **Rasio & durasi diatur di node 7** (`Target`): `["4:3", 5, 832, 480]` = 4:3, 5 detik, 832×480. Untuk 9:16 → set `"9:16"` + `480×832`.
4. Node 5 fleksibel: **1 foto** (first-frame saja) atau **2 foto** (first + last) → satu workflow bisa dipakai untuk beberapa fitur.
5. Tombol **Download** di halaman workflow memberi JSON lengkap **tanpa login** → sumber intel terbaik (dipakai buat bikin node map ini).

## ✅ Status integrasi
- `RUNNINGHUB_WF_ALLINONE=2084116925483151361` (sudah diisi di `.env`).
- **Binding FINAL (terverifikasi jalan):**
  - node 4 `image` ← `@photo1` (frame awal)
  - node 6 `image` ← `@photo2` (frame akhir)
  - node **8 `prompt`** ← `@prompt` ⚠️ nama field-nya **`prompt`, BUKAN `text`** (kalau salah: error `803 NODE_INFO_MISMATCH ... field_not_found_in_node_inputs`)
- **Upload**: `POST /task/openapi/upload` (form: apiKey + fileType + file) → balikin `api/<sha256>.png`. Berhasil tanpa membership.
- **Create task**: `POST /task/openapi/create` (`apiKey` + `workflowId` + `nodeInfoList`) → balikin `data.taskId`.
- **Poll**: `POST /task/openapi/status` → `POST /task/openapi/outputs` (output = URL → harus diunduh).
- ⚠️ `POST /task/openapi/getWorkflowJson` **balikin code 404** untuk ID post komunitas → pakai tombol **Download** di halaman workflow sebagai gantinya.
- 🔎 Kalau ada error `field_not_found_in_node_inputs`: jalankan **`tools/rh_probe_fields.py`** (brute-force nama field kandidat sampai ketemu).

**Tes render pertama:** taskId `2108059227392602114` (2 foto frame awal/akhir, prompt gaya H3 2 segmen) — status: jalan di cloud.