# 🔍 RepoScout — Katalog Repo Berguna

> Hasil riset repo GitHub yang berguna buat proyek Webuild.
> Cara kerja ada di skill `reposcout`. **Update tiap RepoScout jalan.**

---

## 📋 Format

`| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik (agent) | Status |`

---

## 🎮 Proyek 4 — Virtual Office / Visualisasi Agent

| Nama | URL | Fungsi | Stack | Pemilik |
|---|---|---|---|---|
| **pixtuoid** | github.com/IvanWng97/pixtuoid | Terminal pixel-art office buat AI coding agent | Rust | MotionAgent/WebBuilder |
| **agent-office** | github.com/harishkotra/agent-office | Agent AI jalan ke meja, kolaborasi, hire intern | TypeScript | WebBuilder |
| **Claude-Office** | github.com/W17ant/Claude-Office | Pixel-art virtual office, visualisasi agent real-time | TypeScript | WebBuilder |
| **opencode-visualiser** | github.com/psinetron/opencode-visualiser | Log terminal AI → 2D pixel office | HTML | WebBuilder |
| **AgentFleet** | github.com/DBell-workshop/AgentFleet | Pixel-art RPG workspace multi-agent | Python | WebBuilder |
| **agent-monitor** | github.com/ruiqili2/agent-monitor | Dashboard visualisasi + monitoring agent | TypeScript | OpsAgent |
| **claw3d** | github.com/dacoburchenson/claw3d | 3D AI agent office visualization | TypeScript | MotionAgent |

## 📱 SocialAgent — Auto-Posting Sosmed

| Nama | URL | Fungsi | Stack | Pemilik |
|---|---|---|---|---|
| **brightbean-studio** | github.com/brightbeanxyz/brightbean-studio | Platform manajemen sosmed self-hosted | Python | SocialAgent |
| **trypost** | github.com/trypostit/trypost | Sosmed scheduling open-source | PHP | SocialAgent |
| **Free-AI-Social-Media-Scheduler** | github.com/Anil-matcha/Free-AI-Social-Media-Scheduler | Alternatif Postiz self-hosted | JavaScript | SocialAgent |
| **cogsend** | github.com/deepakness/cogsend | Scheduler self-hosted, publish ke banyak platform | TypeScript | SocialAgent |
| **Post4U** | github.com/ShadowSlayer03/Post4U-Schedule-Social-Media-Posts | Auto-jadwal & posting | Python | SocialAgent |

## 🤖 Proyek 2 & 3 — Agentic / Autonomous AI

> Riset 2026-10-08 — **5 repo terbaik: framework/builder agen + memori agen**.
> Prioritas buat kita: yang **menambah kemampuan tim agent Webuild** (memori, orkestrasi, builder), bukan framework yang cuma dipakai nulis agen dari nol.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **mem0** | github.com/mem0ai/mem0 | **Memory layer buat agen** — memori jangka panjang yang persisten (unify memory + RAG), drop-in buat agen & app | Python / API + SDK | Apache-2.0 ✅ | 66.774 | RepoScout + OpsAgent | ✅ REKOMENDASI — paling langsung nambah "ingatan" tim agent |
| **Langflow** | github.com/langflow-ai/langflow | Builder visual agen & workflow AI (drag-drop), deploy jadi API | Python / React Flow | MIT ✅ | 155.569 | OpsAgent + RepoScout | ✅ PAKAI (prototipe cepat alur agen) |
| **Sim** | github.com/simstudioai/sim | Workspace kolaboratif buat build/deploy/monitor agen & workflow (100k+ builder) | TypeScript / Bun / Next.js / Turborepo | Apache-2.0 ✅ | 29.790 | OpsAgent + WebBuilder | ✅ PAKAI — stack sama (Next.js), cocok jadi panel orkestrasi |
| **Ekko Studio** (dulu *Hermes Studio / Hermes Web UI*) | github.com/EKKOLearnAI/ekko-studio | Web console + desktop buat **Hermes Agent** & multi-agent: chat, voice, file, device, workflow visual | TypeScript / Vue3 / npm | ⚠️ **BSL-1.1** | 11.320 | OpsAgent + WebBuilder | ⚠️ PELAJARI — paling nyambung ke Hermes kita, tapi **Business Source License**: cek batasan produksi komersial + Change Date sebelum dipakai |
| **agenticSeek** | github.com/Fosowl/agenticSeek | "Manus AI lokal" — agen otonom yang mikir, browsing, & ngoding tanpa API berbayar | Python | ⚠️ GPL-3.0 | 27.446 | RepoScout | ⚠️ CADANGAN — GPL-3.0 (hati-hati kalau produk kita nyampur kodenya) |

### 🔎 Catatan lisensi (hati-hati)
| Repo | Catatan |
|---|---|
| `license.spdx_id` bisa balikin **`NOASSERTION` / `Other`** walau repo aktif — artinya lisensi campur/kustom. **Wajib baca file LICENSE** (`gh api repos/O/R/contents/LICENSE --jq .content \| base64 -d`). Contoh nyata 2026-10-08: edge-tts ternyata **LGPLv3** (bukan MIT), index-tts pakai **bilibili Model Use License**, ekko-studio pakai **BSL-1.1**. |

## 🧠 RepoScout + OpsAgent — Agent Skills, MCP & Context (infrastruktur tim agent)

> Riset **2026-10-12** — rotasi topik: **agentic AI lanjutan → ekosistem AGENT SKILLS + MCP + kompresi konteks** (katalog sudah punya framework agen & memori, tapi belum punya skill/MCP/context).
> Kenapa penting: cara kerja tim kita = **skill-based** (skill `reposcout`, `newswatch`, dst). Repo skill yang **nyebut Hermes Agent** langsung bisa dipakai — bukan cuma dibaca.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Superpowers** | github.com/obra/superpowers | **Framework metodologi + set skill komposabel** buat coding agent: paksa alur *spec → rencana → subagent-driven TDD → review*, disiplin YAGNI/DRY | Shell / Markdown — plugin buat Claude Code, Codex, Gemini CLI, **Hermes Agent** (ada bagian khusus di README) | MIT ✅ | 297.655 | Orchestrator + semua agent | ✅ **REKOMENDASI** — paling nyambung dgn pola skill kita; pelajari metodologinya buat bikin skill tim sendiri |
| **Headroom** | github.com/headroomlabs-ai/headroom | **Layer kompresi konteks buat agen**: kompres output tool/log/file/RAG **sebelum** masuk LLM (contoh README: 55.957 → 24.340 token, baris penting utuh) — ada PyPI + npm + MCP | Python | Apache-2.0 ✅ | 75.065 | OpsAgent + semua agent | ✅ **PAKAI** — hemat token & hemat RAM VPS (kita ketat memori); cek dulu akurasinya di prompt kita |
| **codebase-memory-mcp** | github.com/DeusData/codebase-memory-mcp | **MCP code intelligence**: index repo (162 bahasa, tree-sitter + Hybrid LSP) → knowledge graph fungsi/kelas/route + 17 tool MCP; klaim **10× lebih hemat token** & 2,1× lebih sedikit tool call vs baca file satu-satu | C (native, **tanpa runtime/API key**) | MIT ✅ | 46.369 | WebBuilder + RepoScout + OpsAgent | ✅ PAKAI — bikin agen "paham" repo klien tanpa baca file satu-satu (ada preprint arXiv:2603.27277) |
| **Graphify** | github.com/Graphify-Labs/graphify | Ubah **codebase + docs + skema SQL + config + PDF** → knowledge graph yang bisa di-query agen | Python | Apache-2.0 ✅ | 125.538 | RepoScout + OpsAgent | ✅ PAKAI — pelengkap codebase-memory-mcp (kita banyak PDF dokumen desa) |
| **FastMCP** | github.com/PrefectHQ/fastmcp | Cara **Pythonic bikin MCP server & client** (standar de-facto) | Python | Apache-2.0 ✅ | 28.043 | OpsAgent | ✅ PAKAI — jalur kita sendiri buat expose layanan Webuild (vault, kanban, desa) sebagai MCP |
| **Figma-Context-MCP** | github.com/GLips/Figma-Context-MCP | MCP server kirim **info layout Figma** ke agent coding (REST API Figma resmi) | TypeScript / MCP | MIT ✅ | 15.970 | DesignerBot | ✅ PAKAI — pasangan/alternatif `figma-mcp-bridge` (yang itu tanpa limit API lewat plugin desktop) |
| **Playwright MCP** | github.com/microsoft/playwright-mcp | MCP server browser Microsoft — buka halaman, ambil struktur, klik | TypeScript / Playwright | Apache-2.0 ✅ | 38.028 | OpsAgent + RepoScout | ✅ PAKAI — alternatif resmi buat `browser_exec` kalau perlu di dalam agen lain |
| **ECC** | github.com/affaan-m/ECC | "Agent harness performance optimization": skills + instincts + memory + security + research | JavaScript (plugin Claude Code + npm `ecc-universal`) | MIT ✅ | 277.165 | OpsAgent + Orchestrator | ⚠️ PELAJARI — banyak ide bagus (instincts/security) tapi ⭐ sangat tinggi, watchers 1.376 → cek dulu isinya sebelum dipasang |
| **Skills (mattpocock)** | github.com/mattpocock/skills | Skill engineering kecil & komposabel ("bukan vibe coding"), update otomatis via `skills.sh` | Shell / Markdown | MIT ✅ | 286.097 | Semua agent | ⚠️ CADANGAN — bahan perbandingan gaya nulis skill |

### 🎨 Skill-pack siap pakai (desain & marketing)

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Hallmark** | github.com/Nutlope/hallmark | **Skill anti-AI-slop** (dibuat Together AI): pilih *macrostructure*, 21 tema, 4 perintah — `build` · `audit` (skor kode existing) · `redesign` · `study` (ekstrak **DNA desain** dari URL/screenshot → `design.md`, menolak pixel-clone) + 57 gate "slop test" | CSS / Markdown (Claude Code, Cursor, Codex) | MIT ✅ | 29.909 | DesignerBot + WebBuilder | ✅ **PELAJARI/ADAPTASI** — persis prinsip **ANTI-TEMPLATE** Webuild; ⚠️ muda (created 2026-04) & push terakhir 2026-08-06 |
| **Marketingskills** | github.com/coreyhaines31/marketingskills | Skill marketing buat agen: CRO, copywriting, SEO, analytics | JavaScript / Markdown | MIT ✅ | 54.194 | ContentWriter + SalesAgent | ✅ PAKAI — bahan jualan & konten desa/UMKM |
| **Archify** | github.com/tt-a1i/archify | Ide/rencana/codebase → **diagram interaktif** (agent skill) | JavaScript | MIT ✅ | 82.028 | ContentWriter + WebBuilder | ✅ PAKAI — bikin diagram penjelasan buat klien (non-teknis) |

### 🔎 Catatan agent-skills / MCP
- **Rasio ⭐ vs watchers wajib dicek di kategori ini.** Skill-pack viral muda bisa ⭐ ratusan ribu dengan watchers kecil: `Graphify` 125.538⭐/397 subs, `Archify` 82.028⭐/227, `Hallmark` 29.909⭐/**61** — bandingkan proyek sehat (`FastMCP` 28.043⭐/124). **Yang watchers-nya belasan** → jangan jadi fondasi, cukup referensi.
- **Hasil `search/repositories` bisa balikin `subscribers_count: null`** walau detail repo punya nilainya → selalu ambil dari endpoint detail `repos/O/R`, jangan dari hasil search.
- **Repo skill untuk agen = kategori tersendiri sekarang.** Query tajam: `agent+skills+in:name,description+NOT+awesome`, `claude+skills`, `+pushed:>2025-06-01`. Nilai tertinggi = yang README-nya **menyebut Hermes Agent** (Superpowers) → nol porting.

## 🌐 WebBuilder — Web Modern / Desa

> Riset 2026-10-07 (task t_05f9b201) — **5 repo terbaik: template/komponen Next.js (landing page modern & UI kit)**.
> Prinsip Webuild = modern & ANTI-TEMPLATE → prioritas: **komponen yang masuk ke repo kita (copy-paste/shadcn registry)**, bukan theme jadi yang kelihatan generik.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **shadcn/ui** | github.com/shadcn-ui/ui | UI kit fondasi — komponen aksesibel, source-nya di-copy ke repo kita (bukan dependency) → gampang dikustom biar nggak template | React 19 / Next.js / Tailwind / Radix & Base UI | MIT ✅ | 125.223 | WebBuilder + DesignerBot | ✅ REKOMENDASI UTAMA (dipakai semua proyek) |
| **Magic UI** | github.com/magicuidesign/magicui | Library komponen **beranimasi** buat landing page (bento grid, marquee, particle, shimmer) — copy-paste via shadcn CLI → landing langsung berasa "mahal" | Next.js / React / Tailwind / Framer Motion | MIT ✅ | 22.484 | WebBuilder + MotionAgent | ✅ PAKAI (bahan hero/animasi landing) |
| **Cult UI** | github.com/nolly-studio/cult-ui | 150+ komponen animasi shadcn registry (dynamic island, shift card, texture) — CLI nyalin source ke project, jadi kode milik kita | Next.js / React 19 / Tailwind / Motion | MIT ✅ | 6.364 | WebBuilder + MotionAgent | ✅ PAKAI (varian desain anti-monoton) — ⚠️ repo ±222 MB (monorepo), jangan full clone |
| **Launch UI** | github.com/launch-ui/launch-ui | Landing page kit copy-paste (section hero/fitur/harga/FAQ) — **stack paling fresh** dari semua kandidat | Next.js 16 / React 19 / Tailwind 4 / TypeScript | MIT ✅ | 862 | WebBuilder | ✅ PAKAI (paling up-to-date, `isTemplate=true`) |
| **Next.js Landing Page Starter (ixartz)** | github.com/ixartz/Next-JS-Landing-Page-Starter-Template | Starter landing page lengkap: dark mode, ganti warna/tema, SEO, i18n — tinggal ganti konten | Next.js 14 / React 18 / Tailwind 3.4 / TS 5 | MIT ✅ | 2.140 | WebBuilder | ⚠️ CADANGAN — stack agak ketinggalan (Tailwind 3, Next 14), update terakhir 2026-01 |

### 🔎 Cadangan & yang perlu hati-hati

| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/cruip/open-react-template | 4.707 | Kualitas bagus, tapi **lisensi GPL-3.0 + dilarang redistribusi/resell template** → boleh dipakai buat klien, jangan dijual ulang sebagai template. Banyak dipakai orang = kelihatan template. |
| github.com/cruip/tailwind-landing-page-template | 4.510 | Sama seperti di atas (GPL-3.0, no redistribusi). |
| github.com/vercel/next-forge | 7.670 | Template Turborepo production-grade (Clerk, Stripe, PostHog) — MIT, `isTemplate=true`. Lebih ke fondasi SaaS, bukan landing page. |
| github.com/imskyleen/animate-ui | 4.365 | Komponen animasi bagus, **tapi lisensi "Other/NOASSERTION"** → wajib baca LICENSE.md sebelum dipakai komersial. |
| github.com/nobruf/shadcn-landing-page | 1.290 | MIT, template landing shadcn+Tailwind — **stale** (push terakhir 2025-01). |

**Kesimpulan buat Webuilder:** pakai **shadcn/ui sebagai fondasi**, tambah **Magic UI + Cult UI + Launch UI** sebagai sumber komponen/section animasi → hasilnya modern dan tidak kelihatan "theme beli". Hindari menyerahkan template cruip apa adanya (lisensi + terlalu umum).

## 🎨 DesignerBot / WebBuilder — Design & UI/UX (desain, token, Figma)

> Riset **2026-10-10** — rotasi topik: **design/UI-UX** (belum ada di katalog).
> Prinsip Webuild = **ANTI-TEMPLATE** → yang paling berharga di sini: alat yang **membaca design system situs referensi → jadi token milik kita sendiri** (bukan nyalin template jadi).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **design-extract** (`designlang`) | github.com/Manavarya09/design-extract | Headless browser baca design system situs LIVE lewat DOM → 17+ file: **DTCG tokens, Tailwind config, shadcn theme, Figma variables, motion tokens**, prompt-pack siap-tempel (v0/Lovable/Cursor) + grade/report card, drift-check | Node / JS (`npx designlang <url>`) | MIT ✅ | 4.194 | DesignerBot + WebBuilder | ✅ REKOMENDASI — senjata anti-template: "rasa" desain referensi → token resmi kita |
| **Dembrandt** | github.com/dembrandt/dembrandt | URL → **W3C design tokens (DTCG)** satu perintah: warna, tipografi, spacing, border, shadow, motion, komponen + `--shadcn`, `--dtcg`, `--wcag`, `--design-md` (buat agen); bisa **dienforce di CI** | TypeScript / Node 18+ / Playwright | MIT ✅ | 3.620 | DesignerBot | ✅ PAKAI — token paling rapi + guard CI |
| **Design DNA** | github.com/zanwei/design-dna | **Agent skill**: ekstrak & terapkan identitas visual jadi JSON "Design DNA" 3 dimensi (tokens · gaya kualitatif · efek Canvas/WebGL/3D) dari screenshot/URL → generate UI | Agent skill (`npx skills add`) | MIT ✅ | 1.923 | DesignerBot + RepoScout | ✅ PAKAI — formatnya skill agen, gampang diadaptasi ke pola skill Hermes |
| **Designer Skills Pack** | github.com/Owl-Listener/designer-skills | 273 skill + 76 command / 33 plugin: riset desain, design system, UX strategy, UI, interaksi, prototyping, critique + koleksi khusus **"AI product design"** (UX buat agen) | Markdown (Claude Code / Gemini CLI plugin) | MIT ✅ | 2.865 | DesignerBot | ✅ PELAJARI/ADAPTASI — bahan kurikulum desain buat tim |
| **UX/UI Agent Skills (XIAS)** | github.com/plugin87/ux-ui-agent-skills | Kit "senior design architect": DTCG tokens, **138 design system**, 52 gate objektif, WCAG 2.2 AA→AAA, 16 adapter framework | Markdown + HTML statis | MIT ✅ | 1.560 | DesignerBot + WebBuilder | ✅ PAKAI — rujukan gate kualitas & aksesibilitas |
| **Figma MCP Bridge** | github.com/gethopp/figma-mcp-bridge | Plugin Figma + **MCP server** → streaming data dokumen Figma ke agen **tanpa kena limit API Figma** (free cuma 6 request/BULAN) | TypeScript / MCP / `npx` | MIT ✅ (file `LICENSE.md`) | 725 | DesignerBot + OpsAgent | ✅ PAKAI — jembatan Figma→agent; butuh **Figma desktop app** (user Windows ✅) |

### 🔎 Cadangan & referensi desain

| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/cosscom/coss | 10.677 | Design system resmi **Cal.com** (dulu Origin UI) — kualitas tinggi & sangat aktif, **tapi AGPL-3.0** → hati-hati kalau masuk produk tertutup |
| github.com/radix-ui/primitives · mui/base-ui · chakra-ui/ark · unovue/reka-ui | 19.375 · 11.107 · 5.409 · 6.859 | Semua **MIT** — komponen "unstyled" (fondasi shadcn/ui). **reka-ui = versi Vue**, ark = React/Vue/Solid. Pakai kalau mau primitif sendiri |
| github.com/tsparticles/tsparticles | 8.991 | MIT — partikel/confetti/efek background buat landing (MotionAgent) |

## 🚀 WebBuilder — Astro (stack utama kita)

> Riset **2026-10-10** — stack Webuild = **Next.js/Astro + Tailwind**, tapi katalog baru isi Next.js. Demo "Desa Pamekaran" kita pakai **Astro 5** → Astro dapat bagiannya.
> Catatan: semua kandidat di bawah sudah **Astro 7 + Tailwind 4** (2016-10 = versi terkini), jadi demo kita perlu rencana upgrade.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **AstroWind** | github.com/arthelokyo/astrowind *(dulu `onwidget/astrowind` — cuma rename org, repo sama)* | Theme Astro **paling banyak ⭐ & fork 2022–2025**: landing + blog, skor **Lighthouse 100 semua**, ada Docker + nginx + `AGENTS.md`/`CLAUDE.md` (siap-dipakai agen) | Astro 7 / Tailwind 4 / TS 5.9 | MIT ✅ (`LICENSE.md`) | 6.027 | WebBuilder | ✅ REKOMENDASI — basis landing desa/UMKM, sekelas stack kita |
| **ScrewFast** | github.com/mearashadowfax/ScrewFast | Template bisnis lengkap dalam 1 repo: landing + blog + halaman produk + **docs site** (Starlight) + view-transition | Astro 7 / Tailwind 4 / Preline UI | MIT ✅ | 1.420 | WebBuilder + ContentWriter | ✅ PAKAI — kalau klien butuh sekaligus website + dokumentasi |
| **Accessible Astro Starter** | github.com/incluud/accessible-astro-starter | Starter fokus **SEO + aksesibilitas WCAG 2.2 AA** (ada juga package komponen aksesibel terpisah) | Astro 7 / Tailwind 4 | MIT ✅ | 1.187 | WebBuilder + DesignerBot | ✅ PAKAI — situs desa/pemerintah wajib aksesibel → ini rujukannya |
| **Starwind UI** | github.com/starwind-ui/starwind-ui | Komponen UI shadcn-style **portabel**: satu set jalan di **Astro, React, Vue, Svelte** (mono-repo: `packages/astro|react|vue|svelte|cli|runtime`) — di-copy ke repo kita | Astro / TS / Tailwind | MIT ✅ | 744 | WebBuilder | ✅ PAKAI — 1 set komponen buat **dua stack** kita (Astro + Next) |
| **Fulldev UI** | github.com/fulldotdev/ui | Komponen + **block shadcn-compatible khusus Astro**, vanilla Astro (tanpa framework JS), content-first (section, tiles) | Astro 7 / Tailwind 4 / TS 6 | MIT ✅ (file `LICENCE`) | 610 | WebBuilder | ✅ PAKAI — push 2026-10-09 (paling fresh dari semua kandidat) |
| **Bearnie** | github.com/michael-andreuzza/bearnie | Komponen aksesibel Astro + Tailwind, source **di-copy ke project** biar jadi milik kita (docs: bearnie.dev) | Astro 7 / Tailwind 4 / MDX | MIT ✅ | 354 | WebBuilder + DesignerBot | ✅ PAKAI — bahan varian desain non-monoton |

### 🔎 Cadangan (web/Astro)

| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/surjithctly/astroship | 1.982 | Populer & aktif (push 2026-10-05) **tapi GPL-3.0** + disponsori Web3Templates → hindari buat produk yang dijual |
| github.com/saicaca/fuwari · CuteLeaf/Firefly · RyanFitzgerald/devportfolio | 5.073 · 2.282 · 4.984 | Semua **MIT** — tema blog/blog & portfolio; Firefly paling aktif (push 2026-10-09). Bagus jadi **referensi desain**, bukan fondasi |

**Kesimpulan buat Webuilder:** (1) kumpulkan *token* dari situs referensi pakai **designlang/Dembrandt** (bukan jiplak template) → jaga prinsip anti-template; (2) fondasi Astro pakai **AstroWind**, komponen dari **Starwind UI + Fulldev UI + Bearnie**, jamin aksesibilitas pakai **Accessible Astro Starter**.

## 🎙️ VoiceAgent — TTS / Voice / Audio

> Riset 2026-10-08 — **6 repo terbaik: TTS, voice cloning & voice studio self-hosted**.
> Konteks VPS kita: **tanpa GPU** → utamakan yang ringan/CPU atau yang bisa dicolok sebagai API gratis.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Voicebox** | github.com/jamiepine/voicebox | **Voice studio AI open-source**: clone suara, generate speech, dikte ke app apa pun — full voice I/O lokal | Python / Qwen3-TTS / Whisper / CUDA+MLX / Docker + MCP server | MIT ✅ | 56.590 | VoiceAgent | ✅ REKOMENDASI UTAMA (ada `docker-compose.yml` + MCP → gampang dihubungkan ke agent) |
| **GPT-SoVITS** | github.com/RVC-Boss/GPT-SoVITS | Voice cloning few-shot — 1 menit data suara cukup buat bikin TTS baru | Python | MIT ✅ | 62.476 | VoiceAgent | ✅ PAKAI (kalau butuh suara kustom klien/desa) — butuh GPU biar nyaman |
| **RealtimeTTS** | github.com/KoljaB/RealtimeTTS | TTS **streaming realtime** (teks→suara kayak lagi ngomong) — buat balasan suara live | Python | MIT ✅ | 4.038 | VoiceAgent | ✅ PAKAI (basis voice assistant realtime) |
| **openai-edge-tts** | github.com/travisvn/openai-edge-tts | Endpoint **`/v1/audio/speech` kompatibel OpenAI** pakai edge-tts (GRATIS) — bisa dicolok jadi provider TTS custom Hermes | Python / FastAPI / Docker | ⚠️ GPL-3.0 | 2.120 | VoiceAgent + OpsAgent | ✅ PAKAI SELF-HOST (gratis, tanpa API key) — GPL aman buat internal, hati-hati kalau distribusi ulang |
| **edge-tts** | github.com/rany2/edge-tts | Pakai layanan TTS Microsoft Edge dari Python — tanpa Edge/Windows/API key | Python (CLI + lib) | ⚠️ **LGPLv3** (+MIT 1 file) | 12.186 | VoiceAgent | ✅ referensi/backup — **catatan: Hermes sudah punya provider TTS `edge` bawaan**, jadi ini buat keperluan luar Hermes |
| **IndexTTS** | github.com/index-tts/index-tts | Zero-shot TTS industrial-grade, controllable (emosi/durasi), cross-lingual | Python / PyTorch | ⚠️ **bilibili Model Use License** | 24.345 | VoiceAgent | ⚠️ PELAJARI lisensinya dulu (kustom, belum tentu bebas komersial) sebelum dipakai |

### 🎤 Tambahan **2026-10-12** — STT & Voice Agent realtime (sisi "mendengar", belum ada di katalog)

> Rotasi topik TTS/voice, tapi **sudut baru**: katalog 2026-10-08 cuma isi *pembuat* suara (TTS/clone). Yang belum ada: **pengenal suara (STT)** & **rangkaian percakapan realtime** (voice agent).
> Konteks VPS: **tanpa GPU** → menang yang jalan di CPU/offline.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **sherpa-onnx** | github.com/k2-fsa/sherpa-onnx | Toolkit **offline/on-device**: STT, TTS, speaker diarization, VAD, language ID, speech enhancement — **tanpa internet & tanpa GPU**, binding Python/JS/Android/iOS/Windows/Linux, jalan di web (WASM) | C++ / ONNX Runtime | Apache-2.0 ✅ | 15.224 | VoiceAgent + OpsAgent | ✅ **REKOMENDASI** — paling cocok VPS kita (CPU, offline, gratis); sekaligus **pengganti piper** (runtime piper ada di dalamnya) |
| **Pipecat** | github.com/pipecat-ai/pipecat | Framework Python buat **voice & multimodal agent realtime**: rangkai STT + LLM + TTS, transport audio/video, multi-agent handoff | Python | BSD-2-Clause ✅ | 16.365 | VoiceAgent + OpsAgent | ✅ PAKAI — basis "agen suara" layanan desa/UMKM (aktif: push 2026-10-11) |
| **LiveKit Agents** | github.com/livekit/agents | Framework realtime voice AI agent di atas **WebRTC** (ada versi JS: `agents-js`) | Python / TypeScript | Apache-2.0 ✅ | 14.697 | VoiceAgent | ✅ PAKAI — kalau butuh jalur telepon/WebRTC, bukan cuma file audio |
| **Moonshine** | github.com/moonshine-ai/moonshine | STT **latensi sangat rendah** + intent recognition + TTS, dirancang buat voice agent | C++ / Python | ⚠️ **MIT + pengecualian per-model** | 11.212 | VoiceAgent | ⚠️ BACA LISENSI DULU — **model legacy non-streaming non-Inggris** (Arab, Jepang, Korea, Mandarin, Spanyol, Ukraina, Vietnam) = **Moonshine Community License (NON-KOMERSIAL)**; model TTS/G2P ikut lisensi pihak ketiga |
| **Handy** | github.com/cjpais/Handy | Aplikasi desktop **STT offline** (dikte ke app apa pun), bisa diperluas | Rust | MIT ✅ | 33.537 | VoiceAgent (buat user) | ⚠️ CADANGAN — butuh desktop/GUI (PC user Windows ✅), bukan service di VPS |

### 🔎 Cadangan & catatan voice/STT
| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/rhasspy/piper | 11.297 | TTS lokal cepat — **ARCHIVED** (push terakhir 2025-08-26) → **jangan dipakai**; ambil runtime piper dari **sherpa-onnx** |
| github.com/coqui-ai/TTS | 46.107 | **MPL-2.0**, tapi melambat (push terakhir 2024-08) → legacy |
| github.com/PaddlePaddle/PaddleSpeech | 12.695 | **Apache-2.0**, ASR + TTS + streaming (push 2026-08) — toolkit besar, berat buat VPS kita |
| github.com/streamcoreai/streamcore-server | 234 | Server voice agent realtime (Go, WebRTC/WHIP, barge-in) — kecil & belum teruji, cuma referensi |

**Kesimpulan buat VoiceAgent:** (1) **bikin suara** → GPT-SoVITS / Voicebox (riset 10-08); (2) **dengar suara** → **sherpa-onnx** (offline, CPU, gratis) atau **Moonshine** (latensi rendah, cek lisensi); (3) **rangka jadi percakapan** → **Pipecat** / **LiveKit Agents**. Jalur WhatsApp-desa: pesan suara masuk → STT sherpa-onnx → agen → TTS → balas via WAHA.

---

## ✍️ ContentWriter / SocialAgent — Content Creation (konten & video AI)

> Riset **2026-10-09** — rotasi topik: **content creation** (belum ada di katalog).
> Konteks VPS **tanpa GPU** + tim butuh bikin konten promosi (video pendek, caption, copy) buat Webuild & klien desa/UMKM.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Open-Generative-AI** | github.com/Anil-matcha/Open-Generative-AI | Studio AI image+video "open-source", 600+ model (14 studio), tanpa filter | JS / Next.js | MIT ✅ | 29.887 | SocialAgent + MotionAgent | ⚠️ PELAJARI — kodenya MIT, **tapi model-nya lewat API MuAPI berbayar** (bukan lokal); value tergantung langganan |
| **short-video-factory** | github.com/YILS-LIN/short-video-factory | Desktop app: prompt + storyboard → video pendek marketing **otomatis** (AI copy + TTS + auto-edit + subtitle + batch) | TypeScript / Electron | ⚠️ AGPL-3.0 | 5.566 | SocialAgent + ContentWriter | ✅ PAKAI INTERNAL — pas buat bulk konten UMKM; hati-hati AGPL kalau distribusi |
| **VANTA** | github.com/itsjwill/vanta | **AI video engine berbasis Remotion (React/TS)**: voice cloning (GPT-SoVITS), avatar talking-head, caption animasi (WhisperX), T2V, music gen, 100+ transisi GPU | TypeScript / React / Remotion | MIT ✅ | 134 | MotionAgent + VoiceAgent | ✅ PAKAI — render programatik, **stack kita (React/TS)**; bintang kecil tapi integrasi terdokumentasi |
| **OpenChatCut** | github.com/0xsline/OpenChatCut | Video editor AI conversational, local-first, multi-track timeline | TypeScript | ⚠️ AGPL-3.0 | 2.201 | MotionAgent | ⚠️ PANTAU — repo baru (created 2026-07) |
| **ai-video-editor** | github.com/MartinDelophy/ai-video-editor | Editor video local-first; **manusia & AI agent edit timeline yang sama** | JavaScript | MIT ✅ | 905 | MotionAgent | ⚠️ PANTAU — konsep pas buat agent, repo masih muda |
| **CartCut** | github.com/cartesiancs/cartcut | Video editor desktop fokus **motion effects**, animasi, sound mixing, ekstensi library | TypeScript | MIT ✅ | 797 | MotionAgent | ⚠️ PANTAU |

### 🔎 Catatan (content)
- **Hati-hati "open-source" palsu:** repo bisa berlisensi MIT tapi fungsinya **front-end ke API berbayar** (contoh: Open-Generative-AI → **MuAPI**, white-label $49/mo). Baca README, cari kata *"powered by / API key / subscription"*.
- **Waspada star-farm:** topik niche (AI video editor) banyak repo **created 2026 dengan bintang tinggi mendadak** & nama mirip-mirip (cartcut, OpenChatCut, WeftCut) → cek `created_at` + rasio fork/⭐ + commit asli sebelum dipakai.

## ⚙️ OpsAgent — Automation / No-Code

> Riset **2026-10-09** — rotasi topik: **automation / no-code**.
> Kegunaan: otomatisasi kerja tim (posting, sync, backup) + builder buat klien. **Perhatian lisensi** — banyak "open-source" di sini sebenarnya *fair-code*.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **n8n** | github.com/n8n-io/n8n | Platform automation workflow visual + AI native (400+ integrasi) — standar de-facto | TypeScript / Node | ⚠️ **Sustainable Use License** (fair-code) + EE Enterprise | 206.729 | OpsAgent | ⚠️ PAKAI INTERNAL — **BUKAN open source OSI**: dilarang jual ulang/host jadi layanan; file `.ee.` butuh lisensi Enterprise |
| **Activepieces** | github.com/activepieces/activepieces | Alternatif Zapier open-source (TypeScript), self-host, AI-first | TypeScript | ✅ **MIT** (base) + dir `ee/` | 24.956 | OpsAgent | ✅ REKOMENDASI — inti MIT, paling aman buat dipakai/dijual; fitur EE terpisah |
| **Kestra** | github.com/kestra-io/kestra | Orchestrator workflow event-driven (YAML deklaratif), skala besar | Java / YAML | ✅ **Apache-2.0** | 29.427 | OpsAgent | ✅ PAKAI — lisensi paling bersih, cocok orkestrasi jadwal/backup |
| **ToolJet** | github.com/ToolJet/ToolJet | No-code/low-code builder internal tool & dashboard (drag-drop, konek DB/API) | JavaScript / React | ⚠️ AGPL-3.0 | 41.051 | OpsAgent + WebBuilder | ⚠️ PELAJARI — bagus buat panel internal klien, tapi AGPL |
| **Windmill** | github.com/windmill-labs/windmill | Developer platform: script → workflow → UI otomatis (Rust, cepat) | Rust / TypeScript | ⚠️ mix **AGPL-3.0 + Apache-2.0** + EE | 18.140 | OpsAgent | ⚠️ PELAJARI lisensi per-file sebelum dipakai |
| **ByteChef** | github.com/bytechefhq/bytechef | Automation + AI agent self-host, bisa di-embed ke SaaS | Java | ✅ **Apache-2.0** (base) + dir `ee/` | 1.016 | OpsAgent | ✅ CADANGAN — Apache-2.0, alternatif n8n yang boleh dijual |

### 🔎 Catatan lisensi automation (PENTING)
- Banyak platform "open source" automation sebenarnya **fair-code / Sustainable Use License** (n8n, LiveContext) → boleh self-host & modifikasi, **tapi dilarang menjual ulang sebagai layanan / hapus branding**.
- Pola umum: **inti berlisensi bebas (MIT/Apache) + folder Enterprise (`ee/`, `.ee.`) proprietary** → cek folder `ee` dulu. Contoh: Activepieces (MIT+ee), ByteChef (Apache+ee), Windmill (AGPL/Apache+ee).

---

## 🗂️ WebBuilder / ContentWriter — CMS buat Klien (editor konten desa & UMKM)

> Riset **2026-10-11** — rotasi topik: **CMS / editor konten** (belum ada di katalog).
> **Kebutuhan nyata:** demo "Desa Pamekaran" itu **Astro statis** → staf desa (non-teknis) tidak bisa nulis berita/pengumuman sendiri. Ini gap paling menghambat kalau mau dijual sebagai produk.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Sveltia CMS** | github.com/sveltia/sveltia-cms | Git-based headless CMS — **penerus resmi Netlify/Decap CMS**: editor konten modern, i18n, jalan sebagai SPA dari CDN (**tanpa backend/server**), kompatibel Astro/Hugo/Eleventy | JavaScript / Svelte / GitHub API | MIT ✅ (file `LICENSE.txt`) | 2.938 | WebBuilder + ContentWriter | ✅ **REKOMENDASI UTAMA** — (1) konten tetap di repo (aman + gratis), (2) **punya Agent Skill resmi + `llms.txt`** → agen kita bisa ngedit konten langsung, (3) sudah dipakai instansi pemerintah AS (argumen jual ke desa/pemda) |
| **Pages CMS** | github.com/hunvreus/pagescms | CMS open-source **buat repo GitHub**: connect repo → editor konten/media commit langsung; tersedia versi **HOSTED gratis** di app.pagescms.org | TypeScript / Next.js / GitHub App | MIT ✅ | 4.078 | WebBuilder + ContentWriter | ✅ **PAKAI** — paling sedikit ribet (staf desa tak perlu install apa pun); ⚠️ ritme rilis santai (commit terakhir 2026-06-08) |
| **EmDash** | github.com/emdash-cms/emdash | CMS full-stack TypeScript **berbasis Astro** — ambil ide WordPress (admin UX, ekosistem plugin) tapi plugin diisolasi di **Cloudflare Worker sandbox**; jalan di Cloudflare (D1+R2+Workers) atau Node+SQLite. Ada template Blog/Marketing/Portfolio | TypeScript / Astro / Workers | MIT ✅ (© **Cloudflare Inc.**) | 13.555 | WebBuilder | ✅ **PELAJARI** — paling \"satu atap\" & stack kita (Astro); ⚠️ repo **muda** (created 2026-04) + 350 open issues → API masih bergerak cepat, jangan jadikan fondasi produksi dulu |
| **TinaCMS** | github.com/tinacms/tinacms | CMS **visual** (edit langsung di halaman, real-time) buat Markdown/MDX — klien \"ngedit sambil lihat hasilnya\" | TypeScript / React | Apache-2.0 ✅ | 13.825 | WebBuilder + ContentWriter | ✅ PAKAI — opsi kalau klien rewel soal \"harus lihat tampilan saat ngedit\" |
| **StudioCMS** | github.com/withstudiocms/studiocms | CMS headless **native Astro** (model SSR) — bukan output statis | TypeScript / Astro | MIT ✅ | 840 | WebBuilder | ⚠️ CADANGAN — mono-repo besar (±800 MB) & tim kecil; cocok kalau butuh CMS dinamis penuh |
| **Decap CMS** | github.com/decaporg/decap-cms | CMS Git-based kanonik (dulu Netlify CMS) buat static site generator | JavaScript / React | MIT ✅ | 19.424 | WebBuilder | ⚠️ CADANGAN — paling banyak dipakai, tapi ritme melambat (commit 2026-09-22, 609 open issues) → **pakai Sveltia sebagai versi modernnya** |
| **Payload** | github.com/payloadcms/payload | CMS/backend full-stack Next.js (admin + REST/GraphQL + auth + upload) — kalau situs butuh database & role | TypeScript / Next.js | MIT ✅ (file `LICENSE.md`) | 45.176 | WebBuilder | ✅ PAKAI (kalau klien butuh lebih dari blog) — lebih berat dari kebutuhan desa biasa |

### 🔎 Cadangan & catatan CMS
| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/strapi/strapi | 73.291 | **MIT Expat untuk Community Edition**, folder `ee/` = Enterprise (lisensi terpisah). Berat (butuh server + DB) → *overkill* buat situs desa statis. |
| github.com/danielcgilibert/blog-template (\"Openblog\") | 1.018 | Template blog Astro bagus **tapi GPL-3.0** → hati-hati kalau dipakai produk tertutup. |
| github.com/StaticJsCMS/static-cms | 589 | MIT **tapi ARCHIVED** (`archived=true`, push terakhir 2024-09) → **jangan dipakai** (pernah jadi penerus Decap, kini ditinggalkan; pendahulu Sveltia). |
| github.com/sitepins/sitepins · pageel/pageel-cms | 185 · 61 | Git-based CMS & CMS native Astro, proyek kecil/belum teruji → cuma referensi. |

**Kesimpulan buat Webuilder:** pakai **Sveltia CMS** (konten di Git, tanpa server) sebagai standar semua situs desa/UMKM — atau **Pages CMS hosted** kalau klien mau nol-setup. Simpan **EmDash** sebagai kandidat "desa digital generasi 2" (Astro + admin + database) begitu stabil.

## 💬 SocialAgent / OpsAgent / SalesAgent — WhatsApp & Messaging

> Riset **2026-10-11** — rotasi topik: **WhatsApp / messaging** (belum ada di katalog; katalog baru isi auto-posting sosmed).
> **Alasan strategis:** di desa & UMKM, **WhatsApp = kanal nomor satu** (pengumuman, layanan, order, keluhan). Website desa tanpa jalur WA = belum selesai.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **WAHA** | github.com/devlikeapro/waha | **WhatsApp HTTP API (REST)** siap pakai — Docker 1 perintah, ada dashboard + Swagger, multi-engine (WEBJS/NOWEB) | TypeScript / Docker | Apache-2.0 ✅ (inti) | 7.576 | OpsAgent | ✅ **REKOMENDASI** — cara tercepat nyalain WA jadi API; ⚠️ fitur lanjut (multi-sesi dsb) ada di image **WAHA Plus BERBAYAR** → cek dulu sebelum janji fitur |
| **Baileys** | github.com/WhiskeySockets/Baileys | Library **inti** WhatsApp Web (socket multi-device) buat bikin bot/API sendiri | TypeScript / JavaScript | MIT ✅ | 11.297 | OpsAgent + SocialAgent | ✅ PAKAI (fondasi; dipakai WAHA/Evolution di bawah) — ⚠️ cara tak resmi → pakai **nomor khusus**, jangan nomor klien, hindari spam |
| **Chatwoot** | github.com/chatwoot/chatwoot | **Meja layanan omni-channel** (live chat web, email, WA, IG) — alternatif Intercom, self-host | Ruby on Rails / Next.js | ✅ MIT (inti) + dir `enterprise/` lisensi terpisah | 37.688 | **SalesAgent** + SocialAgent | ✅ PAKAI — \"helpdesk desa/UMKM\": semua kanal masuk 1 inbox, ada agen/assignee |
| **Evolution API** | github.com/evolution-foundation/evolution-api | WhatsApp integration API open-source (paling populer buat bot & CRM di ID/BR) | TypeScript | ⚠️ **Apache-2.0 + SYARAT TAMBAHAN** | 9.820 | OpsAgent | ⚠️ PELAJARI — bukan Apache murni: (a) **dilarang hapus logo/copyright** di frontend, (b) **WAJIB tampilkan notifikasi** "memakai Evolution API" kalau dipakai di sistem lain (termasuk closed-source) |
| **DeskcommCRM** | github.com/melgarafael/DeskcommCRM | CRM + agen AI self-hosted, WA via WAHA, multi-tenant, RAG, MCP | TypeScript / Next.js / Supabase | MIT ✅ | 4.522 | SalesAgent | ⚠️ PANTAU — repo muda (created 2026-04) & **watchers cuma 23** vs 4.522⭐; rilis mingguan + 100+ kontributor (kelihatan asli) tapi jangan jadi fondasi dulu |

### 🔎 Catatan WhatsApp (PENTING)
- **Jangan pakai bot grup hasil fork-forkan.** Query `whatsapp bot` didominasi repo \"**X-MD**\" (`mruniquehacker/Knightbot-MD` 8.126⭐, `MalvinTechInfo/MALVIN-XD`, `mrfrankofcc/SUBZERO-MD`, `lyfe00011/levanter`/`whatsapp-bot`, `Ainz-devs/OVL-MD-V2`) — bot grup fitur ribuan, kualitas/asal tak jelas, dan sering minta user \"pairing nomor\" sendiri (risiko nomor diblokir). **Cari library/API-nya** (`baileys`/`waha`/`evolution`), bukan bot jadi.
- **Lisensi \"standar + syarat tambahan\" bisa lolos dari `spdx_id`.** Evolution API terbaca `NOASSERTION`, dan file LICENSE-nya memang **Apache-2.0 dengan 2 syarat tambahan** (notifikasi + larangan hapus logo) → baca **15 baris pertama** file LICENSE, bukan cuma baris pertama. Untuk produk yang mau dijual, wajib patuhi syarat itu.
- **Semua jalur WA tak resmi (Baileys/WAHA/Evolution) berbagi risiko sama:** nomor bisa diblokir Meta. Aturan internal: **nomor khusus**, volume wajar, tak ada spam/blast massal; untuk kebutuhan resmi/volume besar → **WhatsApp Cloud API resmi**.
- **Sambungan ke tim:** WAHA/Evolution → OpsAgent (infra + webhook) · Chatwoot/Deskcomm → SalesAgent (prospek & layanan) · pesan otomatis/pengumuman → SocialAgent. Otomatisasi lanjut bisa lewat **Activepieces (MIT)** / **n8n (internal saja)** dari [[06-Tim-Agent/RepoScout - Katalog Repo]] bagian OpsAgent.

---

## 🛠️ OpsAgent / Orchestrator — Observability, Eval & Keamanan Agen

> Riset **2026-10-13** — rotasi topik: **agentic AI, sudut baru: memantau & mengamankan agen** (katalog sudah punya framework/builder/memori/skill/MCP, tapi belum ada cara lihat *jejak, biaya, dan kesalahan* tiap run agen kita, apalagi mengaudit skill pihak ketiga).
> Kenapa penting sekarang: tim kita jalan dari cron per profil + gateway + fallback provider — kalau ada run gagal/diam-diam boros, **tidak ada yang kelihatan**.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **AI-Infra-Guard (A.I.G)** | github.com/Tencent/AI-Infra-Guard | Platform **AI red teaming** (Tencent Zhuque Lab): **`skill-scan`** audit keamanan skill agen (taksonomi T01–T09, verdict `malicious`/`suspicious`/`normal`, output SARIF), **`mcp-scan`**, `agent-scan`, pustaka **2000+ CVE** komponen AI (LangFlow, n8n, vLLM, MLflow…), jailbreak eval (Many-Shot/PAIR/GOAT) | Python (`pip install aig-skill-scan`) | Apache-2.0 ✅ | 6.836 | OpsAgent + RepoScout | ✅ **REKOMENDASI** — wajib dipakai tiap mau pasang **skill-pack pihak ketiga** (selama ini kita ambil skill dari repo viral tanpa audit) |
| **Plano** | github.com/katanemo/plano | **Proxy/data-plane AI-native** (dibangun di atas Envoy oleh kontributor intinya): routing orkestrasi multi-agen, **smart LLM routing + fallback provider** (endpoint OpenAI-compatible `base_url`), guardrail filter, **OTel traces/metrics** — "What you don't write: intent classifiers, routing logic, model fallbacks, provider adapters, tracing instrumentation" | Rust / Envoy / YAML | Apache-2.0 ✅ (tanpa folder `ee/`) | 7.084 | OpsAgent | ✅ **PAKAI** — paling relevan buat kita: **pusatkan fallback provider (Inferhub→OmoApicall) + guardrail + tracing di satu tempat**; ⚠️ repo muda (created 2024-07), pantau stabilitas |
| **Langfuse** | github.com/langfuse/langfuse | Observability + eval agen: trace LLM/agen, prompt management, dataset, LLM-as-judge, biaya | TypeScript / Next.js | MIT Expat (inti) + dir `ee/` proprietary | 35.713 | OpsAgent | ✅ PAKAI — tapi ⚠️ **self-host BERAT**: `docker-compose.yml` = web + worker + **ClickHouse + MinIO + Redis + Postgres** (6 service) → **jangan self-host di VPS kita** (RAM ketat); pakai versi cloud dulu |
| **Opik** | github.com/comet-ml/opik | Observability + eval LLM/RAG/agent (Comet): trace, LLM-judge, dataset; SDK Python/TS + dukungan OpenTelemetry | Python | Apache-2.0 ✅ | 22.533 | OpsAgent | ⚠️ CADANGAN — fungsinya lengkap, tapi **self-host compose = 15 service** (MySQL, ClickHouse, Redis, MinIO, ZooKeeper, Jaeger, otel-collector) → paling berat dari semua kandidat, bukan buat VPS kita |
| **Logfire** | github.com/pydantic/logfire | Observability AI **paling ringan**: SDK **OpenTelemetry** buat trace LLM/agen (tim Pydantic) | Python | MIT ✅ | 4.513 | OpsAgent | ✅ PAKAI — jalur paling hemat RAM: cukup kirim OTel dari proses Python, tanpa container besar; ⚠️ watchers cuma 17 |
| **MLflow** | github.com/mlflow/mlflow | Platform AI engineering (tracking eksperimen, eval LLM/agen, model registry) — standar industri | Python | Apache-2.0 ✅ | 28.353 | RepoScout | ⚠️ CADANGAN — sehat (watchers 327), tapi condong ke eksperimen ML → overkill buat memantau cron tim |

### 🔎 Catatan observability / keamanan agen
- **Kategori "observability/eval agen" = kategori berat container.** Ukur dulu sebelum janji self-host:
  ```bash
  gh api "repos/O/R/contents/docker-compose.yml" --jq '.content' | tr -d '\n' | base64 -d | grep -E "^  [a-z0-9_-]+:"
  ```
  Hasil nyata: **Langfuse 6 service**, **Opik 15 service** (MySQL+ClickHouse+MinIO+ZooKeeper+Jaeger). VPS kita (available ~272 MB) **tidak mungkin** menjalankannya → mulai dari **SDK OTel ringan (Logfire)** atau SaaS gratis.
- **LICENSE gaya "open core" makin sering pemiliknya bukan nama repo:** file LICENSE Langfuse berbunyi *"Copyright (c) 2023-2026 **ClickHouse, Inc.**"* dengan aturan `ee/` (akuisisi) — **baca 15 baris pertama**, jangan kaget/anggap repo berpindah.
- **Keamanan skill = risiko nyata buat tim skill-based.** Sebelum `skill_view`/instal skill dari repo luar, jalankan **`aig-skill-scan`** (verdict + SARIF); khususnya skill yang menyuruh jalankan shell/curl.

## 📧 SalesAgent / ContentWriter — Email & Newsletter (prospek desa & UMKM)

> Riset **2026-10-13** — rotasi topik: **email/newsletter self-hosted** (belum ada di katalog; yang ada baru sosmed + WhatsApp).
> **Kebutuhan nyata:** kirim **penawaran/proposal ke calon kepala desa & UMKM** secara rapi + terukur (bukan blast dari Gmail), dan **newsletter** desa buat warga.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **listmonk** | github.com/knadh/listmonk | Manajer **newsletter & mailing list** self-hosted: kampanye, list/segment, template, bounce, API — **satu binary Go** + PostgreSQL | Go / Vue / PostgreSQL | ⚠️ AGPL-3.0 | 23.765 | SalesAgent + OpsAgent | ✅ **REKOMENDASI** — paling matang & aktif (push 2026-10-12, watchers 147); kirim lewat **SMTP relay luar**, bukan langsung dari VPS |
| **Sendportal** | github.com/mettle/sendportal | **Email marketing** self-hosted: kampanye, subscriber, template (Laravel) | PHP / Laravel 13 / MySQL | ✅ **MIT** | 2.176 | SalesAgent | ✅ **PAKAI — lisensi paling bersih** buat yang mau dijual; baru upgrade Laravel 13 (push 2026-10-12) |
| **Ghost** | github.com/TryGhost/Ghost | Publishing + **newsletter + membership** satu atap (blog desa + kirim berita ke warga) | TypeScript / Node | ✅ MIT (© Ghost Foundation) | 55.523 | ContentWriter + WebBuilder | ✅ PAKAI — watchers **1.015** (paling sehat dari semua kandidat); cocok kalau klien mau blog + email langganan sekaligus |
| **BillionMail** | github.com/Billionmail/BillionMail | **Mail server penuh + newsletter/marketing** self-host (Postfix+Dovecot dibundel, panel web) | Go / Docker | ⚠️ AGPL-3.0 | 15.896 | OpsAgent | ⚠️ PANTAU — push terakhir **2026-06** (melambat); butuh DNS/PTR + port 25 → berat & rawan masuk spam |
| **Keila** | github.com/pentacent/keila | Alat newsletter open source (kampanye, list, form pendaftaran) | Elixir / PostgreSQL | ⚠️ AGPL-3.0 | 2.233 | SalesAgent | ⚠️ CADANGAN — watchers 16 + stack Elixir (asing buat tim kita) |
| **Notifuse** | github.com/Notifuse/notifuse | Newsletter + email marketing + email transaksional, ada MCP | Go / MySQL | ⚠️ **BSL-1.1 mulai v40** (v39.x selamanya AGPL) | 2.245 | SalesAgent | ⚠️ PELAJARI — **bukan open source lagi**: 6 fitur digerbang lisensi key (workspace >3, permission granular, SES tenant, SSO, template multibahasa, audit log). Mau bebas? pakai **v39.x (AGPL-3.0)** |
| **Cerberus** | github.com/emailmonday/Cerberus | Pola **template email HTML responsif** yang aman di Outlook/Gmail (template, bukan server) | HTML / CSS | ✅ MIT | 5.139 | ContentWriter + DesignerBot | ✅ PAKAI — bahan bikin template email kampanye desa/UMKM yang tidak berantakan di email client |

### 🔎 Catatan email/newsletter
- **JANGAN kirim email massal langsung dari VPS.** Deliverability ditentukan **PTR + SPF/DKIM/DMARC + reputasi IP**, dan port 25 sering diblokir penyedia VPS. Pola yang benar: **aplikasi di VPS (listmonk / Sendportal) + pengiriman via relay luar** (Amazon SES / Brevo / Resend — ada kuota gratis).
- **Lisensi bisa berubah per VERSI, bukan cuma per repo:** Notifuse pindah **AGPL-3.0 → BSL-1.1 mulai v40** (v39.x permanen AGPL) dan punya file terpisah **`LICENSING.md`** → baca `LICENSING.md`, bukan cuma `LICENSE`.
- **Sambungan ke tim:** kampanye ke calon kades/UMKM → **SalesAgent**; newsletter & isi berita desa → **ContentWriter**; desain template → DesignerBot; relay/DNS/domain → **OpsAgent**.

---

## 🚀 OpsAgent / WebBuilder — Deploy & Hosting Banyak Situs (self-hosted PaaS)

> Riset **2026-10-14** — rotasi topik **web dev/infra**, sudut baru: **cara menaruh BANYAK situs klien di satu server** (katalog sudah punya framework & CMS-nya, belum punya cara *men-deploy*-nya).
> **Kebutuhan nyata:** setiap klien desa/UMKM butuh domain + SSL + deploy sendiri. Ini yang paling cepat jadi beban operasional kalau dikerjakan manual satu-satu.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Coolify** | github.com/coollabsio/coolify | **PaaS self-hosted** (alternatif Vercel/Heroku/Netlify): panel web, deploy dari Git/Docker, kelola domain + SSL + database, aplikasi & service | PHP (Laravel) / Docker | Apache-2.0 ✅ (cuma `LICENSE`, tanpa folder `ee/`) | 62.948 (subs 195) | OpsAgent | ✅ **REKOMENDASI** — standar de-facto; cocok jadi \"panel hosting klien\" begitu kita punya VPS khusus web |
| **Dokploy** | github.com/Dokploy/dokploy | PaaS self-hosted (alternatif Vercel/Netlify/Heroku) — UI modern, Docker Compose, database, multi-server; ada versi cloud berbayar (opsional) | TypeScript / Docker | ✅ **Apache-2.0** (inti) + dir `/proprietary` | 37.779 (subs 113) | OpsAgent | ✅ PAKAI — inti bebas; baca folder `/proprietary` buat tahu fitur yang digerbang |
| **Dokku** | github.com/dokku/dokku | PaaS minimalis \"git push → jalan\" di atas Docker (paling ringan, tanpa panel berat) | Go / Docker | ✅ **MIT** | 32.179 (subs **340** — paling sehat) | OpsAgent | ✅ PAKAI — kalau mau hemat RAM: tanpa UI, cukup CLI + plugin |
| **Kamal** | github.com/basecamp/kamal | Deploy aplikasi container ke server apa pun **tanpa panel** (dari Basecamp): YAML + SSH, zero-downtime, proxy bawaan | Ruby / Docker | ✅ **MIT** | 14.646 (subs 98) | OpsAgent | ✅ PAKAI — jalur \"tanpa dashboard\", dokumentasi paling jelas |
| **CapRover** | github.com/caprover/caprover | PaaS (Docker + nginx otomatis) — \"Heroku on steroids\", sudah lama jalan | TypeScript / Docker | ✅ **Apache-2.0** (© BigZee Ventures LLC — file `LICENSE`) | 15.185 (subs 144) | OpsAgent | ⚠️ CADANGAN — masih aktif (push 2026-10-13) tapi UI/ritme lebih lambat dari Coolify/Dokploy |
| **Nginx Proxy Manager** | github.com/NginxProxyManager/nginx-proxy-manager | Panel **domain + reverse proxy + SSL Let's Encrypt** (klik, bukan edit config) | TypeScript / nginx / Docker | ✅ **MIT** | 34.395 (subs 227) | OpsAgent | ✅ **PAKAI SEKARANG** — paling langsung berguna: semua domain klien + sertifikat auto di satu UI |
| **Uptime Kuma** | github.com/louislam/uptime-kuma | **Monitoring uptime** situs/layanan + notifikasi (Telegram/WA/email), halaman status publik | JavaScript / Socket.io | ✅ **MIT** | 92.413 (subs 322) | OpsAgent + SalesAgent | ✅ **PAKAI** — bukti ke klien bahwa situsnya dipantau; notifikasi bisa masuk ke Telegram tim |
| **ZaneOps** | github.com/zane-ops/zane-ops | PaaS self-hosted (Django + React) untuk app, database, **situs statis** | Python / Docker | Apache-2.0 ✅ | 1.387 | OpsAgent | ⚠️ PANTAU (subs 30) |
| **SwiftWave** | github.com/swiftwave-org/swiftwave | PaaS ringan untuk VPS kecil (Go) — klaim hemat resource | Go / Docker | Apache-2.0 ✅ | 907 | OpsAgent | ⚠️ CADANGAN |

### 🔎 Catatan deploy/hosting
- **VPS kita (1,9 GB RAM, available ~375 MB) BUKAN tempat PaaS ini.** Coolify/Dokploy dirancang untuk server tersendiri (2 GB+ per instance) — memasangnya di server yang sekarang menjalankan 6 service + swap 1,5 GB kepakai = bunuh diri. **Urutan yang benar:** (1) sekarang pakai **NPM (domain+SSL)** + **Uptime Kuma (monitor)** + deploy manual per service; (2) begitu volume klien naik → **VPS khusus web** + Coolify/Dokploy; (3) kalau klien punya server sendiri → Dokku/Kamal (paling hemat).
- **Pola \"open-core\" juga ada di sini** dan semuanya terbaca `NOASSERTION` di API: **Dokploy** = Apache-2.0 + dir `/proprietary` · **PostHog** = MIT Expat + `ee/` · **Formbricks** = AGPL + `apps/web/modules/ee` · **OpnForm** = AGPL + `api/app/Enterprise`. **Baca header file LICENSE-nya** (bukan cuma spdx_id) → ini yang menentukan boleh-dijual atau tidak.

---

## 📊 SalesAgent / OpsAgent — Analitik Web & Formulir Klien (lead capture)

> Riset **2026-10-14** — rotasi topik kedua: **analitik & formulir** (belum ada di katalog).
> **Kebutuhan nyata:** (1) klien desa/UMKM mau tahu \"berapa orang buka situs saya\" **tanpa iklan Google**; (2) situs statis kita butuh **formulir kontak/pendaftaran** yang datanya masuk ke kita (lead sales) — bukan cuma tombol WhatsApp.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Umami** | github.com/umami-software/umami | Analitik web **privacy-first tanpa cookie** — traffic, campaign, behavior, conversion, revenue | TypeScript / Next.js | ✅ **MIT** | 39.350 (subs 139) | OpsAgent + SalesAgent | ✅ **REKOMENDASI** — compose cuma **2 service (app + Postgres)** → paling ringan buat VPS kita; ada versi cloud |
| **Plausible CE** | github.com/plausible/community-edition *(aplikasinya: `plausible/analytics` 29.391⭐ AGPL-3.0)* | Analitik privacy-first versi **self-hosted community** (ringan, satu halaman dashboard) | Elixir → Docker | ✅ **MIT** (repo CE) | 2.896 | OpsAgent | ✅ PAKAI — **3 service: app + Postgres + ClickHouse** (2 mesin DB → lebih berat dari Umami; jangan digabung di server klien kecil) |
| **Matomo** | github.com/matomo-org/matomo | Analitik web **paling lengkap** (eks-GitHub Piwik): laporan detail, goal, funnel, heatmap via plugin | PHP / MySQL | ⚠️ GPL-3.0 | 21.951 (subs **394** — paling sehat) | OpsAgent | ✅ PAKAI kalau klien minta laporan \"seperti Google Analytics\" — butuh PHP 8.1 + MySQL 8/MariaDB 10.6 |
| **PostHog** | github.com/PostHog/posthog | Platform product-analytics + session replay + feature flag + eksperimen (all-in-one) | Python / TS | ⚠️ MIT Expat (inti) + dir `ee/` | 40.262 (subs 143) | OpsAgent | ⚠️ CADANGAN — **jauh lebih berat** dari kebutuhan situs desa/UMKM; pakai versi cloud kalau butuh |
| **Formbricks** | github.com/formbricks/formbricks | **Form builder + survey + feedback** (alternatif Qualtrics/Typeform), ada targeting in-app & link publik | TypeScript / Next.js | ⚠️ **AGPLv3** (inti) + `apps/web/modules/ee` | 13.094 (subs 47) | SalesAgent + ContentWriter | ⚠️ PELAJARI — fitur bagus, **tapi self-host berat**: compose resmi (`docker/docker-compose.yml`) berisi **postgres + redis + spicedb + authzed (4 container izin) + migrate + hub** → **>12 container** |
| **OpnForm** | github.com/OpnForm/OpnForm *(URL lama `JhumanJ/OpnForm` = repo sama)* | Form builder open-source (drag-drop + logic), respons rapi | PHP (Laravel) / Vue / Nuxt | ⚠️ **AGPLv3** (inti) + dir `api/app/Enterprise` | 3.829 (subs 24) | SalesAgent | ⚠️ PELAJARI — **7 service** (api, api-worker, api-scheduler, ui, redis, db, ingress); AGPL → hati-hati kalau di-embed ke produk tertutup |
| **LimeSurvey** | github.com/LimeSurvey/LimeSurvey | Platform **survei/kuesioner** mapan (logika, kuota, token, laporan) | PHP / MySQL | ✅ **GPL-2.0** | 3.761 (subs 129) | SalesAgent + ContentWriter | ✅ CADANGAN — kalau kebutuhannya **survei serius** (mis. survei kepuasan warga), bukan formulir kontak |

### 🔎 Cadangan & jebakan formulir/analitik
| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/ohmyform/ohmyform | 2.889 | **ARCHIVED** (`archived=true`, push terakhir 2024-10) → sering muncul di daftar \"alternatif Typeform\", **jangan dipakai**. |
| github.com/quillforms/quillforms | 622 | **Plugin WordPress** (LGPL-3.0) — cuma relevan kalau klien pakai WP; stack kita Astro/Next → tidak berguna. |
| github.com/Luigigreco/gitforms | 164 | Ide cerdas (**kirim formulir → jadi GitHub Issue + email otomatis**, gratis tanpa DB) **TAPI lisensi = CC BY-NC-SA 4.0 (NON-KOMERSIAL)** → **dilarang** dipakai untuk jasa berbayar kita. |
| github.com/Swetrix/swetrix · betterlytics/betterlytics | 1.204 · 178 | Analitik privacy-first yang lebih baru (Swetrix AGPL-3.0 subs **6**, Betterlytics ada session replay) → referensi saja, komunitas terlalu kecil. |

**Kesimpulan:** (1) **Umami (MIT, 2 service)** = default analitik semua situs klien — ringan, tanpa cookie, gampang dijual sebagai \"statistik desa tanpa iklan\"; (2) formulir: **jangan** self-host Formbricks di VPS ini (12+ container) — untuk kebutuhan kita cukup **form → endpoint kita/WAHA + catat di vault**, atau OpnForm kalau nanti ada VPS khusus; (3) **hosting:** sekarang **NPM + Uptime Kuma**, nanti **Coolify/Dokploy** di VPS khusus web.

---

## 🔗 Terkait
- [[06-Tim-Agent/Team Registry]]
- [[03-Proyek/04-Virtual-Office-Visualisasi/README|Proyek 04 — Virtual Office]]

#reposcout #github #katalog