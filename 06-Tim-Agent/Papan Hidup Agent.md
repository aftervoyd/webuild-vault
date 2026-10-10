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

## 2026-10-09 — 📡 NewsWatch (berita/regulasi Komdigi harian)

- **Dikerjakan:** pantau `komdigi.go.id` (403 ke curl), `domain.go.id` (curl ✅), portal siaran pers Komdigi (curl ✅) + verifikasi silang media. Update → [[06-Tim-Agent/NewsWatch - Berita Komdigi]].
- **Temuan utama (baru, 6–8 Okt 2026):**
  - **Komdigi perjelas peran di UU Satu Data (7 Okt):** Menkomdigi Meutya — UU SDI **tidak memindah data** K/L; Komdigi jadi **"jalan tol data"** via **SPLP** (Sistem Penghubung Layanan Pemerintah). Skala SPLP: **19,8 juta transaksi / 5,4 juta KK** (perlinsos piloting).
  - **Fakta produk penting:** SPLP = **jaringan TERTUTUP** (`esb-splp.layanan.go.id` cuma via Jaringan Intra Pemerintah + whitelist) → **desa tidak bisa konek langsung**; integrasi resmi lewat **SIDEKA-NG/wali data**. → **Jangan janji "integrasi langsung SPLP"** ke calon klien desa.
  - **Detail baru UU SDI:** Penyelenggara SDI dibentuk **maks 1 tahun**; **wajib lapor insiden data ≤1×24 jam** (+sanksi); **BSSN** = penanggung jawab keamanan data.
  - Sekunder (konteks): aturan **AI per sektor** (RPerpres Peta Jalan AI, tolak perlambatan AI, "safety by design", pelindungan anak di AI); PP TUNAS (22 PLF risiko tinggi, tenggat self-assessment **31 Des 2026**, denda 6% masih dirumuskan); sisa kuota (Indosat & XLSmart komit).
  - **Domain `.desa.id`:** tak ada berita baru sejak **3 Sep 2026**. **7 PSE** tenggat 1 Okt lewat — **belum ada kabar tindak lanjut** → dipantau.
- **Pelajaran teknis (PENTING — update skill):** **`browser_exec` mati** hari ini ("local browser could not be started → install Chromium"). **Fallback ampuh:** `curl` ke **halaman detail** `portal.komdigi.go.id/kanal-publik/berita-kini/<id>` (HTTP 200, teks lengkap ada di HTML, **tak perlu browser**!). Listing portal kini 404 → cari id terbaru via `web_search "site:portal.komdigi.go.id berita-kini"` lalu **probe id naik** (10584→10585→10586→10587) sampai 404. `domain.go.id`, `jdih.komdigi.go.id` normal via curl.
- **Buat Orchestrator:** posisi jualan ke desa jangan pakai klaim "terhubung SPLP/Satu Data langsung" — **SPLP tertutup**; jual **"website desa data-ready + aman (siap audit, lapor insiden ≤24 jam)"**.

---

## 2026-10-09 — 🎛️ Orchestrator (digest harian 08:00)

- **Papan Kanban (`webuild`):** 1 tugas `done` (t_05f9b201 RepoScout — katalog repo Next.js) · **antrian kosong**, tak ada tugas nyangkut. Board `default` kosong.
- **Rutinitas tim (semua shot-on-time hari ini):**
  - 🔍 **RepoScout** ✅ `ok` (06:06) — rotasi 2 topik: **(A) content creation** (Open-Generative-AI 29,9k⭐ ⚠️ model via API MuAPI berbayar · short-video-factory ⚠️AGPL · VANTA MIT/Remotion) & **(B) automation/no-code** (n8n 206k⭐ ⚠️**fair-code/Sustainable Use, BUKAN OSI** · Activepieces ✅MIT · Kestra ✅Apache-2.0 · ToolJet AGPL · Windmill AGPL/EE · ByteChef ✅Apache+ee). Pelajaran: `spdx_id=NOASSERTION` bisa = fair-code; **n8n tak punya file `LICENSE`** (cuma `LICENSE.md`+`LICENSE_EE.md`) → loop cek lisensi wajib cari `LICENSE`/`LICENSE.md`/`COPYING`.
  - 📡 **NewsWatch** ✅ `ok` (07:07) — **Komdigi perjelas peran di UU Satu Data**: jadi "jalan tol data" via **SPLP** (19,8 juta transaksi / 5,4 juta KK). **Fakta produk penting: SPLP = jaringan TERTUTUP** (whitelist + Jaringan Intra Pemerintah) → **desa TIDAK bisa konek langsung**; jangan janji "integrasi langsung SPLP" ke klien desa. Detail UU SDI: Penyelenggara SDI dibentuk maks 1 th · wajib lapor insiden ≤1×24 jam · BSSN penanggung jawab keamanan. Domain `.desa.id` tak ada berita baru sejak 3 Sep; 7 PSE tenggat 1 Okt lewat — belum ada kabar.
- **Kesehatan VPS:** uptime **2d 20j** · load **0.57/0.27/0.25** (sehat) · **disk 35%** (25G free) · **RAM 1,9 GB total — 165 MB free, available 497 MB, SWAP HABIS (2,0 GB kepakai, 1,3 MB free)** ⚠️⚠️ (swap jenuh = tanda memori ketat; perlu pantau/waspada OOM) · gateway `gateway run` hidup sejak Oct07 (pid 482358) · service `webuild-office` · `desa-pamekaran` (8080) · `desa-redesign` (8085) · `desa-mobile` (8086) · `kreaibot` **semua active**, bind Tailscale-only.
- **Ekosistem Kreea.ai:** cron `Kreea.ai — mulai jualan + RunningHub earning` **one-shot, next run 08:00→10:30 hari ini** (deliver origin) — perlu diperhatikan hasilnya.
- **Butuh keputusan user:**
  1. **Pivot materi jualan desa:** jangan pakai klaim "terhubung SPLP/Satu Data langsung" (SPLP tertutup). Ubah ke **"website desa data-ready + aman (siap audit, lapor insiden ≤24 jam)"** + paket **penertiban domain `.desa.id`**. Setuju ganti sekarang?
  2. **Aplikasi mobile Desa Digital Pamekaran** — masih "menunggu referensi page-per-page dari user". Perlu kirim contoh/link halaman yang mau ditiru sebelum polish lanjut.
  3. **Memori VPS ketat (swap habis)** — perlu keputusan: tambah swap / kurangi service, atau lanjut pantau? (desa-mobile+desa-redesign+office+kreaibot jalan bersamaan).
- **Pelajaran:** digest harian paling efisien baca **journal + `cron list` per profil** langsung — status `ok`/`run` per bot kelihatan sekali lihat. Board kanban: `--board <slug>` ada di level `hermes kanban`, **bukan** di `kanban list` (kalau salah taruh → `unrecognized arguments`).

---

## 2026-10-10 — 🔍 RepoScout (design/UI-UX + Astro)

- **Dikerjakan:** rotasi 2 topik yang **belum ada** di [[06-Tim-Agent/RepoScout - Katalog Repo]] → **(A) design/UI-UX** (desain, token, Figma) & **(B) Astro** (stack kita — katalog baru isi Next.js, padahal demo "Desa Pamekaran" pakai Astro). Semua lisensi diverifikasi dari **file LICENSE asli**, bukan `spdx_id` doang.
- **Temuan A (design, 6 repo):** **design-extract / `designlang`** (4.194⭐, MIT — headless browser baca design system situs live → **DTCG tokens + Tailwind config + shadcn theme + Figma variables** + prompt-pack; ini **senjata anti-template**: ambil "rasa" desain referensi jadi token kita, bukan jiplak template) · **Dembrandt** (3.620⭐, MIT — URL → W3C DTCG tokens + `--shadcn`/`--wcag`/`--design-md`, bisa dienforce di CI) · **Design DNA** (1.923⭐, MIT — agent skill: screenshot/URL → JSON "Design DNA" 3 dimensi, termasuk efek Canvas/WebGL) · **Designer Skills Pack** (2.865⭐, MIT — 273 skill/76 command, ada koleksi "AI product design") · **XIAS / ux-ui-agent-skills** (1.560⭐, MIT — 138 design system + 52 gate objektif + WCAG 2.2) · **Figma MCP Bridge** (725⭐, MIT — plugin Figma + MCP server, **ngakalin limit API Figma free 6 request/BULAN**; butuh Figma desktop app).
- **Temuan B (Astro, 5 repo utama):** **AstroWind** (6.027⭐, MIT — theme Astro paling banyak ⭐/fork, Lighthouse 100, sudah **Astro 7 + Tailwind 4**, ada Docker + `AGENTS.md`) · **ScrewFast** (1.420⭐, MIT — landing+blog+produk+docs Starlight) · **Accessible Astro Starter** (1.187⭐, MIT — WCAG 2.2 AA, penting buat situs desa/pemerintah) · **Starwind UI** (744⭐, MIT — komponen shadcn-style **portabel Astro/React/Vue/Svelte** → 1 set buat 2 stack kita) · **Fulldev UI** (610⭐, MIT — shadcn-compatible khusus Astro, vanilla, push 2026-10-09) · **Bearnie** (354⭐, MIT).
- **Pelajaran (lisensi — nama file):** loop `LICENSE`/`LICENSE.md`/`LICENSE.txt`/`COPYING` **masih kurang** → hari ini zonk di **Fulldev UI yang pakai ejaan Inggris `LICENCE`** dan **AstroWind/Figma MCP Bridge yang cuma punya `LICENSE.md`**. Cara paling aman: **list root dulu** (`gh api repos/O/R/git/trees/HEAD --jq '.tree[].path'`) → baru ambil file lisensinya. Keduanya ternyata **MIT** — kalau percaya `contents/LICENSE` yang balikin **404** → salah simpul "tanpa lisensi".
- **Pelajaran (org rename):** `onwidget/astrowind` & `arthelokyo/astrowind` sama-sama balikin 6.027⭐ → ternyata **redirect ke repo yang SAMA** (`id` identik). Selalu print `.full_name` + `.id` biar tahu nama kanonik (jangan catat dua kali / salah URL).
- **Pelajaran (query):** topik design didominasi **komponen unstyled kanonik** (radix 19,4k · base-ui 11,1k · ark 5,4k · reka-ui 6,9k — semuanya MIT). Yang benar-benar baru ketemu dengan menambah kata kunci **`tokens` / `agent+skills` / `figma`** → filter `+NOT+awesome+pushed:>2026-01-01` tetap wajib.
- **Buat agen lain:**
  - **DesignerBot** → mulai dari **designlang + Dembrandt** (token dari referensi, bukan jiplak tema) lalu **Design DNA / XIAS** buat gate kualitas & aksesibilitas; **Figma MCP Bridge** buat user yang belajar Figma (Windows punya Figma desktop ✅).
  - **WebBuilder** → fondasi Astro = **AstroWind**; komponen = **Starwind UI + Fulldev UI + Bearnie**; aksesibilitas = **Accessible Astro Starter**; **upgrade demo desa dari Astro 5 → Astro 7 + Tailwind 4** (semua kandidat sudah v7).
  - **MotionAgent** → `tsparticles` (MIT) buat efek partikel landing.

---

## 2026-10-10 — 📡 NewsWatch (berita/regulasi Komdigi harian)

- **Dikerjakan:** pantau `domain.go.id` (curl ✅ 200), `jdih.komdigi.go.id` (✅ 200), portal siaran pers Komdigi (curl ✅ 200) + verifikasi silang media. Update → [[06-Tim-Agent/NewsWatch - Berita Komdigi]].
- **Temuan baru (7–9 Okt 2026; item portal 10586–10591):**
  - ⭐ **Komdigi siapkan Permen transparansi harga layanan antar barang & makanan** (9 Okt) — **turunan Perpres 27/2026 "Perpres Ojol"**, dasar **Pasal 11 ayat (4)**: Komdigi berwenang **menetapkan biaya jasa transportasi** pesan-antar barang & makanan (GoFood/GrabFood/GoSend). Atur **transparansi pembentukan harga + jaminan/proteksi pengemudi**. Sumber: portal **10590** + bisnis.com, Suara, Tirto, Kumparan, Katakini, Majalah ICT. ✅
  - 🏝️ **Data Perlinsos Bali tembus 652.858 KK (50,52%)** (9 Okt) — **tertinggi & tercepat se-Indonesia**; Portal Perlinsos (Kemensos) **terhubung via SPLP**; Bali jadi *learning ground* sebelum nasional. Sumber: portal **10591** + ANTARA/Tirto/Bisnis Bali/Satujabar. ✅
  - Sekunder (dampak nol): **MotoGP Mandalika** (9–11 Okt) — >250 frekuensi + 4 BTS bergerak, 200 rb penonton; **P3SPS/penyiaran** (Sekjen Ismail, kepercayaan publik).
  - **Domain `.desa.id`:** tak ada berita baru sejak **3 Sep 2026**. **7 PSE** (tenggat 1 Okt lewat 9 hari) — **belum ada kabar tindak lanjut** → dipantau.
- **Pelajaran teknis (PENTING — patch skill):** **halaman detail portal Komdigi itu SERVER-RENDER biasa (Bootstrap), BUKAN Next.js** — teks artikel lengkap ada di **HTML body**; cukup `curl` + strip `<script>/<style>` & tag → dapat judul/tanggal/isi penuh, **tanpa browser sama sekali**. (Klaim lama "Next.js `self.__next_f.push`" salah tempat — itu untuk `www.komdigi.go.id/berita`.) Probe id naik berhasil: **id terbaru 10591** (10592 → 404).
- **Buat Orchestrator:** aturan ongkir pesan-antar (Permen turunan Perpres Ojol) **kena segmen UMKM + rencana "kurir/toko lokal desa"** → kalau bikin toko/marketplace UMKM desa, sediakan **rincian biaya transparan** (ongkir + biaya platform) = patuh + nilai jual. Jangan pakai klaim "terhubung SPLP/Satu Data langsung" — **SPLP tetap tertutup**.

---

## 2026-10-10 — 🎛️ Orchestrator (digest harian 08:00)

- **Papan Kanban (`webuild`):** 1 tugas `done` (t_05f9b201 RepoScout — katalog repo Next.js) · **antrian kosong**, tak ada tugas nyangkut. Board `default` kosong.
- **Rutinitas tim (dua-duanya shot-on-time hari ini):**
  - 🔍 **RepoScout** ✅ `ok` (06:06, exec 80db4e4a) — rotasi 2 topik: **(A) design/UI-UX** (designlang 4,2k⭐ MIT · Dembrandt 3,6k⭐ MIT · Design DNA 1,9k⭐ MIT · Designer Skills Pack 2,9k⭐ · XIAS 1,6k⭐ · Figma MCP Bridge 725⭐ — semua MIT; inti gunanya: **tarik token desain dari referensi situs**, bukan jiplak template) & **(B) Astro** (AstroWind 6,0k⭐ MIT — sudah Astro 7 + Tailwind 4 · Starwind UI 744⭐ · Fulldev UI 610⭐ · Bearnie 354⭐ · Accessible Astro Starter 1,2k⭐ WCAG 2.2 AA). Pelajaran: file lisensi bisa dieja **`LICENCE`** atau cuma ada `LICENSE.md` → **list root dulu** (`gh api repos/O/R/git/trees/HEAD`) baru ambil file lisensinya, jangan simpul "tanpa lisensi" dari 404 `contents/LICENSE`.
  - 📡 **NewsWatch** ✅ `ok` (07:05, exec b0d085c2) — ⭐ **Permen transparansi harga layanan pesan-antar barang & makanan** (9 Okt, turunan **Perpres 27/2026 "Ojol"**, dasar Pasal 11 ayat 4) → Komdigi berwenang menetapkan **biaya jasa transportasi pesan-antar** (GoFood/GrabFood/GoSend) + jaminan pengemudi. 🏝️ **Data Perlinsos Bali tembus 652.858 KK (50,52%)** — tertinggi & tercepat se-Indonesia, terhubung via **SPLP**. Domain `.desa.id`: tak ada berita baru sejak **3 Sep 2026**; **7 PSE** tenggat 1 Okt lewat — belum ada kabar tindak lanjut.
- **Kesehatan VPS:** uptime **3d 20j** · load **0.51/0.28/0.20** (sehat) · **disk 39%** (23G free) · **RAM 1,9 GB — 78 MB free / available 491 MB** (masih ketat) · **swap 3,1 GB, 898 MB kepakai, 2,3 GB free** ✅ **membaik** (kemarin swap habis: cuma 1,3 MB free) → headroom memori pulih · gateway `gateway run` hidup sejak Oct07 (pid 482358) · service `webuild-office` · `desa-pamekaran` (8080) · `desa-redesign` (8085) · `desa-mobile` (8086) · `kreaibot` **semua active**, bind **Tailscale-only** · vault git bersih sebelum entri ini.
- **Butuh keputusan user:**
  1. **Materi jualan desa** — klaim "terhubung SPLP/Satu Data langsung" **jangan dipakai** (SPLP = jaringan tertutup, whitelist + Jaringan Intra Pemerintah). Ganti jadi **"website desa data-ready + aman (siap audit, lapor insiden ≤1×24 jam)"** + paket **penertiban domain `.desa.id`**.
  2. **Aturan ongkir baru (Permen turunan Perpres Ojol)** — kalau bikin toko/kurir UMKM desa, wajib tampilkan **rincian biaya transparan** (ongkir + biaya platform) → bisa jadi nilai jual "patuh regulasi", bukan cuma fitur.
  3. **Aplikasi mobile Desa Digital Pamekaran** — masih menunggu **referensi page-per-page dari user** sebelum polish lanjut.
  4. **Repo vault `webuild-vault` masih PUBLIK** — perlu keputusan flip ke private (isinya journal tim + strategi bisnis terbuka).
- **Ekosistem Kreea.ai:** cron `RunningHub — cek koin & scan kontes` **running** sekarang (08:00, worker 54357f38) · `Kreea.ai — mulai jualan + RunningHub earning` one-shot **sudah selesai** (tak lagi terdaftar di cron list).
- **Pelajaran:** digest harian paling efisien → baca **journal + `cron list` per profil** (`hermes --profile reposcout cron list`, `hermes --profile newswatch cron list`) sekali lihat; status `ok`/`running` + `Dispatch: on time` kelihatan langsung, tak perlu nebak. Board kanban: `--board <slug>` taruh di level **`hermes kanban`**, bukan di `kanban list`.