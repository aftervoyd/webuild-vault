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
- `RUNNINGHUB_WF_ALLINONE=2084116925483151361` (sudah diisi di `.env.example`).
- Binding awal: node 4 `image` ← @photo1, node 6 `image` ← @photo2, node 8 `text` ← @prompt.
- **Nama field node 7 & 8 belum 100% pasti** → wajib dicek dengan `tools/rh_inspect.py <workflowId>` begitu API key ada (endpoint "Get Workflow JSON"), biar binding gak nebak.