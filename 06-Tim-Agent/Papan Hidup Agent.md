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
