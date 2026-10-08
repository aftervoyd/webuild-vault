# 🫀 Papan Hidup Agent

> Journal harian tiap agent Webuild. Bukti tim kita **tumbuh & belajar** tiap hari.
> Format tiap entri: `## YYYY-MM-DD — <NamaAgent>` lalu **Apa yang dikerjakan** + **Pelajaran**.

---

## 2026-10-07 — 🎛️ Orchestrator (pendirian sistem)
- **Dibangun:** struktur vault (08 folder), visi Webuild, Team Registry (5 divisi/13 agent), 4 proyek
- **Dihidupkan:** 2 Bot (`reposcout`, `newswatch`) dengan SOUL sendiri + Papan Kanban + journal ini
- **Integrasi:** GitHub (`gh`), DeepWiki MCP, Context7 MCP, Tailscale SSH, fallback provider
- **Pelajaran:** agent butuh 4 hal biar "hidup" → **identitas (SOUL)** + **ingatan** + **skill (belajar)** + **rutinitas (cron)** + **sosial (papan bersama)**

---

## 2026-10-07 — 🔍 RepoScout
- **Dikerjakan:** riset 5 repo terbaik Next.js (landing page modern & UI kit) buat WebBuilder → dicatat di [[06-Tim-Agent/RepoScout - Katalog Repo]] bagian "🌐 WebBuilder" (task t_05f9b201)
- **Temuan:** shadcn/ui (125k⭐) · Magic UI (22k⭐) · Cult UI (6,4k⭐) · Launch UI (862⭐ — Next 16/React 19/Tailwind 4, paling fresh) · ixartz Next.js Landing Starter (2,1k⭐) — **kelimanya MIT**. cruip open-react-template (4,7k⭐) populer tapi **GPL-3.0 + dilarang redistribusi template** → hati-hati jual ke klien.
- **Pelajaran:** `gh api "search/repositories?q=...&stars:>500&sort=stars&order=desc"` jauh lebih tajam dari `gh search repos`; cek lisensi **wajib** pakai `gh api repos/O/R --jq '.license.spdx_id'` — `gh repo view --json licenseInfo` bisa balikin `spdxId` kosong walau `name` "MIT License", kalau percaya gitu bisa salah simpul repo GPL jadi MIT.
- **Buat agen lain:** WebBuilder → mulai dari shadcn/ui (fondasi) + Launch UI (stack paling up-to-date); MotionAgent → Magic UI & Cult UI buat animasi landing biar nggak monoton.

---

## 2026-10-07 — 🏢 Orchestrator (Zonasi Divisi + Rancangan Ruangan)
- **Dibangun:** 5 zona divisi di kantor (Riset/Produksi/Kreatif/Distribusi/Bisnis) + label lantai (nama + jumlah agent)
- **Fitur baru:** `src/divisions.ts` (divisi, role→divisi, rencana pertumbuhan ruangan, trigger kapasitas)
- **Fix:** nama agent asli muncul di kantor (RepoScout, NewsWatch, WebBuilder, dst — sebelumnya "AI Eng", "Reviewer")
- **Temuan penting:** CSS multi-ruangan **sudah ada** di repo (sidebar + floor plan + pintu) — komponen React-nya tinggal dibikin
- **Rancangan:** ruangan tumbuh dari KEBUTUHAN (5 trigger objektif), bukan diborong di awal → [[03-Proyek/04-Virtual-Office-Visualisasi/Desain Ruangan & Divisi]]
- **Pelajaran:** agent kantor dapat role generik dari repo — harus dipetakan ke identitas tim kita sendiri biar gak jadi "Worker" anonim

## 2026-10-07 — 🏡 Orchestrator (Demo Desa Digital jadi!)
- **Dibangun:** Demo **"Desa Pamekaran"** — Astro 5 + Tailwind 4, **8 halaman**, 280 KB, build 1,5 detik
- **Halaman:** beranda · profil · **transparansi APBDes** · UMKM · layanan · berita · kontak · 404
- **Live:** http://100.115.213.21:8080/ (systemd `desa-pamekaran`, bind Tailscale only)
- **Pelajaran:** Astro jauh lebih ringan dari Next.js untuk VPS kecil (build <2 dtk, output statis) — cocok buat demo cepat
- **Tujuan:** bahan tawaran ke calon kepala desa (posisi "Demo Desa Digital")

## 2026-10-07 — 🎮 Orchestrator (Webuild Office hidup)
- **Dibangun:** **Webuild Office** — visualisasi pixel-art agent (adaptasi `W17ant/Claude-Office`, MIT)
- **Jembatan:** `hooks.outbound` Hermes → `POST /hermes` → WebSocket → React
- **Karakter:** 12 profil tim dipetakan ke karakter (Orchestrator, RepoScout, NewsWatch, WebBuilder, dst)
- **Permanen:** systemd `webuild-office` (auto-start), bind **Tailscale only**
- **Akses:** http://100.115.213.21:3334/
- **Pelajaran:** Hermes punya **padanan hook Claude Code** (`hooks.outbound`) → repo Claude-spesifik bisa diadaptasi **tanpa Claude**

## 📋 Cara Nulis (buat semua agent)
```markdown
## YYYY-MM-DD — <NamaAgent>
- **Dikerjakan:** ...
- **Temuan:** ...
- **Pelajaran:** ... (kalau ada → langsung patch skill sendiri)
- **Buat agen lain:** ... (kalau ada)
```

---

## 🔗 Terkait
- [[06-Tim-Agent/Team Registry]]
- [[06-Tim-Agent/RepoScout - Katalog Repo]]

#papan-hidup #tim-agent #journal

## 2026-10-07 — Kantor multi-ruangan + obrolan kerjaan ASLI jadi

- **Obrolan sekarang nampilin kerjaan ASLI** (dari `tool_input`): "menjalankan terminal: npm run build",
  "menulis file: index.astro", "riset di web: next.js patterns". Sebelumnya cuma generik.
- **10 ruangan baru** (dibuat pakai `scripts/gen-rooms.py`, pixel-art day+night):
  Server Room, Meeting Room, Kitchen, Lobby, Wellness, Rooftop, Gym, Parking, Manager, CEO.
- **Sidebar navigasi + denah**: klik ruangan buat pindah; tombol Denah nampilin 11 ruangan
  sekaligus dengan jumlah agent per ruangan.
- **Kursi otomatis** di tiap spot duduk (meeting-seat/lounge/desk) → karakter kelihatan duduk.
- **Aturan ruangan (tumbuh dari kebutuhan)**: role spesialis punya ruangan sendiri
  (OpsAgent→Server Room, VoiceAgent→Meeting Room); sisanya kantor utama (zonasi 5 divisi tetap utuh);
  kalau kantor utama penuh (10 meja), agent baru melebar ke ruangan lain.
- **Rekonsiliasi roster tiap 12 detik**: kantor selalu sinkron dengan server, agent gak hilang.
- **Bug fix**: cerita palsu tadinya masih nyala di `?story=0` (`params.has()` true untuk nilai apa pun).
  Sekarang wajib `?story=1`.
- **Pelajaran teknis**: `assignSpot()` dulu cuma nerima spot `type === 'desk'`, jadi ruangan non-kantor
  (server-room=`standing`, meeting-room=`meeting-seat`) selalu gagal → agent jatuh ke kantor utama.
  Fix: tambah param `types` + fallback ke spot apa pun yang bebas.

### Lanjutan — art ruangan disejajarkan dengan titik kursi

Temuan: karakter berhenti di pintu, bukan di kursi. Ternyata **art ruangan tidak sejajar
dengan koordinat spot** di `rooms.ts` (meja digambar di bawah, sementara titik kursi di atas).

Fix: semua prop digambar ulang mengikuti koordinat spot asli:
- meeting-room: meja oval dipindah ke pusat `(150,107)` = titik seat-1..4 (x 30%/70%, y 40%/55%)
- kitchen: meja makan ke `(150,146)` = lunch-1/lunch-2 (35%/65%); mesin kopi ke x 90 (coffee-spot)
- server-room: rak server di x 24/82/172/262 biar spot (35%/65%, y 60%) ada di depan rak
- lobby: meja resepsionis ke `(150,90)`; sofa panjang di x 44..118 = waiting-1/2
- gym: 2 treadmill pas di x 75 & 225 (gym-1/gym-2)
- nap-room: 3 sofa di x 75/150/225 (nap-1/2/3)
- rooftóp: kursi santai pas di roof-1/2/3
- manager-office & ceo-office: meja ke y 90 / y 101 (mgr-spot / ceo-spot)

Verifikasi: VoiceAgent jalan dari pintu (90,50) → sampai seat-1 (30,40) → state `working` dalam ~20 detik.
Semua 14 agent akhirnya `working` di ruangannya masing-masing.

---

## 2026-10-08 — 🔍 RepoScout (agentic AI + TTS/voice)

- **Dikerjakan:** rotasi 2 topik → **(A) agentic/autonomous AI** (isi section "Proyek 2 & 3" yang masih kosong) & **(B) TTS/voice** (section baru buat VoiceAgent). Dicatat di [[06-Tim-Agent/RepoScout - Katalog Repo]].
- **Temuan A (agent, 5 repo):** **mem0** (66,8k⭐, Apache-2.0 — memory layer = "ingatan" buat tim agent kita, paling langsung berguna) · **Langflow** (155,6k⭐, MIT — builder visual agen) · **Sim** (29,8k⭐, Apache-2.0, Next.js+Bun — panel orkestrasi, stack sama kayak kita) · **Ekko Studio** (11,3k⭐, dulu bernama **Hermes Studio / Hermes Web UI** — web console buat Hermes Agent; lisensi **BSL-1.1**, bukan open bebas) · agenticSeek (27,4k⭐, GPL-3.0).
- **Temuan B (voice, 6 repo):** **Voicebox** (56,6k⭐, MIT, Python + Qwen3-TTS/Whisper + Docker + MCP server = voice studio self-hosted) · **GPT-SoVITS** (62,5k⭐, MIT, cloning 1 menit data) · **RealtimeTTS** (4k⭐, MIT, TTS streaming) · **openai-edge-tts** (2,1k⭐, GPL-3.0, endpoint `/v1/audio/speech` gratis pakai edge-tts → bisa dicolok jadi provider TTS custom Hermes) · edge-tts (12,2k⭐, LGPLv3) · IndexTTS (24,3k⭐, lisensi bilibili).
- **Pelajaran (PENTING):** `license.spdx_id` = **`NOASSERTION`/`Other`** itu tanda lisensi campur/kustom — **wajib baca file LICENSE-nya langsung**. Buktinya hari ini: **edge-tts ternyata LGPLv3** (bukan MIT seperti dugaan), **IndexTTS pakai bilibili Model Use License** (kustom, belum tentu komersial), **Ekko Studio pakai BSL-1.1** (Business Source License). Kalau cuma lihat spdx_id = salah simpul.
- **Pelajaran (query):** hasil `search/repositories` didominasi **awesome-list** (star ratusan ribu) di posisi atas → tambah **`+NOT+awesome`** di query + `+pushed:>2025-06-01` biar hasilnya repo beneran & masih aktif.
- **Pelajaran (API):** di REST API field arsip itu **`.archived`**, bukan `.is_archived` (itu nama field GraphQL) — `gh api repos/O/R --jq .is_archived` bakal balikin `null` (kelihatan sehat padahal bisa jadi arsip).
- **Buat agen lain:** **VoiceAgent** → mulai dari Voicebox (paling lengkap, ada MCP) + openai-edge-tts (TTS gratis buat Hermes); **OpsAgent** → mem0 buat memori agent + review lisensi Ekko Studio (BSL) kalau mau bikin web console Hermes sendiri; **WebBuilder/MotionAgent** → Sim (Next.js) contoh panel agent yang rapi.

---

## 2026-10-08 — 📡 NewsWatch (run pertama)

- **Dikerjakan:** pasang rutinitas harian pantau Komdigi → catat di [[06-Tim-Agent/NewsWatch - Berita Komdigi]]. Cek `komdigi.go.id`, `domain.go.id`, `portal.komdigi.go.id`.
- **Temuan utama (semua terverifikasi sumber resmi):**
  - **UU Satu Data Indonesia SAH** (6 Okt 2026, Siaran Pers 200/HM-KKD/10/2026) — **20 bab / 141 pasal**; naik dari Perpres 39/2019 jadi UU. Atur **Data Dasar Nasional**, standar+metadata, katalog data, **interoperabilitas**, keamanan/PDP, pemanfaatan **AI**, transfer data ke luar negeri. Orkestrasi **Bappenas**, Komdigi di interoperabilitas+infrastruktur.
  - **Komdigi investigasi jual-beli data pribadi ilegal** (2 Okt 2026) — koordinasi Polri+BSSN, blokir situs; dasar **UU 27/2022 PDP**.
  - **Sisa kuota**: implementasi operator belum optimal (3 Okt 2026) — dampak rendah.
  - **Domain**: tak ada berita baru di `domain.go.id` sejak **3 Sep 2026**. Aturan kunci 2026: domain `.desa.id` **>35 hari nunggak → landing page**, **>1 th → dihapus**; **22.862 domain** aktif, ~47% kedaluwarsa >2 th.
- **Dampak ke Webuild (bisnis):** peluang jual **"website desa siap Satu Data"** (data rapi, siap integrasi SID/SIDEKA-NG/Siskeudes) + **paket penertiban domain `.desa.id`** (banyak domain "hidup tapi nunggak").
- **Pelajaran teknis (PENTING):** `www.komdigi.go.id` **balas 403 ke curl** (WAF) → **pakai browser** (`browser_exec`) berhasil; halaman berita = **Next.js client-render** jadi teks artikel baru muncul setelah navigasi+wait (kadang perlu reload 1x). `web_extract` di profil ini **search-only (DDG)** → nggak bisa ambil isi URL, wajib browser. `domain.go.id` normal via curl.

---

## 2026-10-08 — 🎛️ Orchestrator (digest harian 08:00)

- **Papan Kanban (`webuild`):** 1 tugas `done` (t_05f9b201 RepoScout — katalog repo Next.js) · **antrian kosong**, tak ada tugas nyangkut.
- **Rutinitas tim (semua shot-on-time hari ini):**
  - 🔍 **RepoScout** ✅ `ok` (06:02) — riset **agentic AI** (mem0 66,8k⭐ Apache-2.0 · Langflow MIT · Sim Apache-2.0/Next.js · Ekko Studio ⚠️BSL-1.1 · agenticSeek ⚠️GPL-3.0) + **TTS/voice** (Voicebox MIT+ MCP · GPT-SoVITS · RealtimeTTS · openai-edge-tts GPL · IndexTTS ⚠️lisensi bilibili). Pelajaran: **`license.spdx_id = NOASSERTION` = wajib baca file LICENSE** (dua kali salah simpul).
  - 📡 **NewsWatch** ✅ `ok` (07:04) — **UU Satu Data Indonesia SAH** (141 pasal) + Komdigi tindak jual-beli data pribadi (UU PDP) + domain `.desa.id` (>35 hari nunggak → landing page).
- **Kesehatan VPS:** uptime 1d 20j · load 0.44/0.58/0.59 (sehat) · **disk 32%** (26G free) · **RAM 1,9 GB → cuma ~108 MB free, swap kepakai 1,0 GB** ⚠️ (agak ketat) · gateway `gateway run` hidup 18 jam (pid 482358) · service `webuild-office` · `desa-pamekaran` (8080) · `desa-redesign` (8085) · `desa-mobile` (8086) **semua active**, bind **Tailscale-only**. SSH port 22 normal.
- **Butuh keputusan user:**
  1. **Aplikasi mobile Desa Digital Pamekaran** — statusnya "menunggu referensi page-per-page dari user". Perlu kirim contoh/link halaman mana yang mau ditiru sebelum lanjut polish.
  2. **Pivot jualan ke "website desa siap Satu Data"** (dari temuan NewsWatch) — perlu keputusan apakah paket & materi tawaran ke calon kades diubah sekarang.
- **Pelajaran:** digest harian paling efisien kalau baca **journal + `cron list` per profil** langsung — status `ok`/`running` per bot kelihatan sekali lihat, tak perlu nebak.

---

## 2026-10-09 — 🔍 RepoScout (content creation + automation/no-code)

- **Dikerjakan:** rotasi 2 topik baru → **(A) content creation** & **(B) automation/no-code** (dua section yang belum ada di [[06-Tim-Agent/RepoScout - Katalog Repo]]). Semua lisensi diverifikasi dari file LICENSE asli.
- **Temuan A (content, 6 repo):** **Open-Generative-AI** (29.887⭐, MIT — studio image/video 600+ model, **tapi model-nya lewat API MuAPI berbayar**, bukan lokal) · **short-video-factory** (5.566⭐, ⚠️AGPL-3.0 — desktop: prompt+storyboard → video pendek marketing otomatis: copy+TTS+auto-edit+subtitle) · **VANTA** (134⭐, MIT — AI video engine berbasis **Remotion/React-TS**, voice cloning+avatar+caption animasi, integrasi ke 40+ repo) · OpenChatCut (2.201⭐ AGPL) · ai-video-editor (905⭐ MIT) · CartCut (797⭐ MIT).
- **Temuan B (automation, 6 repo):** **n8n** (206.729⭐ — **⚠️Sustainable Use License/fair-code, BUKAN open source OSI**, file `.ee.` butuh lisensi Enterprise; dilarang jual ulang jadi layanan) · **Activepieces** (24.956⭐, ✅**MIT** base + dir `ee/` — alternatif Zapier paling aman dijual) · **Kestra** (29.427⭐, ✅Apache-2.0 — lisensi paling bersih, orchestrator YAML) · ToolJet (41.051⭐ AGPL — no-code internal tool) · Windmill (18.140⭐ AGPL/Apache+EE) · ByteChef (1.016⭐ ✅Apache-2.0+ee).
- **Pelajaran (lisensi — LANJUTAN):** `license.spdx_id = NOASSERTION` **bisa berarti fair-code / "Sustainable Use License"** (bukan lisensi bebas) — ketemu di **n8n** & **LiveContext**. Ciri: README bilang *"fair-code"*, ada file `LICENSE_EE.md`, folder `ee/` atau nama file `.ee.`. **n8n bahkan tidak punya file `LICENSE`** — hanya `LICENSE.md` + `LICENSE_EE.md` → loop cek lisensi **wajib** nyari `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` (kalau cuma cek `LICENSE` = zonk/keliru simpul open-source).
- **Pelajaran (pola lisensi baru):** makin umum **"inti MIT/Apache + folder Enterprise `ee/` proprietary"** (Activepieces, ByteChef, Windmill) → repo kelihatan NOASSERTION tapi intinya bebas; **cek folder `ee/`** buat tahu fitur mana yang berbayar, jangan buang repo-nya langsung.
- **Pelajaran ("open-source" palsu):** repo berlisensi MIT bisa jadi **front-end ke API berbayar** (Open-Generative-AI → MuAPI white-label $49/mo, "no GPU" krn model di server mereka). Baca README, cari *powered by / API key / subscription* → lisensi kode ≠ gratis dipakai.
- **Pelajaran (star-farm):** topik niche (AI video editor) banyak repo **created 2026, bintang tinggi mendadak, nama kembar** (cartcut / OpenChatCut / WeftCut) → cek `created_at` + rasio `forks/stars` sebelum rekomendasi; jangan tergiur angka ⭐ doang.
- **Buat agen lain:** **SocialAgent/ContentWriter** → short-video-factory (bulk konten UMKM, internal) + Open-Generative-AI (kalau mau langganan MuAPI); **MotionAgent/VoiceAgent** → VANTA (Remotion = stack kita, render video programatik dari React/TS); **OpsAgent** → pakai **Activepieces (MIT)** atau **Kestra (Apache-2.0)** buat otomatisasi tim — **HINDARI n8n buat produk yang mau dijual** (fair-code melarang).

---
