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

## 🛒 WebBuilder / SalesAgent — Toko Online UMKM (e-commerce modern)

> Riset **2026-10-15** (run ulangan — run 06:00 gagal: fallback provider 401) — rotasi topik: **e-commerce / toko online** (belum ada sama sekali di katalog).
> **Kebutuhan nyata:** rencana bisnis Webuild menyebut **"toko UMKM lokal + kurir lokal"** — dan sampai sekarang katalog punya website, CMS, WhatsApp, analitik… **tapi belum punya mesin tokonya**. Semua lisensi diverifikasi dari file LICENSE asli.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (watchers) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Medusa** | github.com/medusajs/medusa | **Headless commerce backend** — produk, cart, order, multi-region, plugin; frontend-nya kita bikin sendiri | TypeScript / Node | ✅ **MIT (inti)** + `ENTERPRISE-LICENSE.md` (materials EE proprietary) | 36.748 (206) | WebBuilder + OpsAgent | ✅ **REKOMENDASI** — headless = pas prinsip anti-template (frontend Astro/Next milik kita, bukan tema toko) |
| **Saleor** | github.com/saleor/saleor | Headless commerce API **GraphQL** kelas enterprise | Python / Django | ✅ **BSD-3-Clause** | 23.440 (**362** — paling sehat di kategori) | WebBuilder | ✅ PAKAI — lisensi paling bersih & komunitas paling sehat; ⚠️ **storefront resminya lain lisensi** (lihat catatan) |
| **Vercel Commerce** | github.com/vercel/commerce | Storefront **Next.js App Router + Tailwind** resmi Vercel (template headless commerce) | TypeScript / Next.js | ✅ MIT | 14.304 (208) | WebBuilder | ✅ PAKAI — contoh storefront Next.js modern, bukan WooCommerce |
| **Bagisto** | github.com/bagisto/bagisto | eCommerce + **marketplace multi-vendor** (Laravel) | PHP / Laravel | ✅ MIT | 28.240 (181) | WebBuilder | ✅ CADANGAN — justru cocok kalau desa butuh **1 situs banyak penjual** (pasar UMKM desa) |
| **Spree** | github.com/spree/spree | Platform commerce DTC/B2B + marketplace | Ruby / Rails | ✅ BSD-3-Clause | 15.756 (85) | OpsAgent | ⚠️ CADANGAN — stack Ruby (asing buat tim) |
| **Sylius** | github.com/Sylius/Sylius | Headless commerce Symfony, multi-channel | PHP / Symfony | ✅ MIT | 8.557 (258) | WebBuilder | ⚠️ CADANGAN — kalau klien memang minta PHP |
| **astro-shopify** | github.com/thomasKn/astro-shopify | Starter storefront **Astro** ↔ Shopify Storefront API | Astro / Tailwind | ✅ MIT | 504 (9) | WebBuilder | ⚠️ CADANGAN — satu-satunya jalur **Astro↔commerce**; proyek kecil |
| **OpenUMKM** | github.com/openumkm/openumkm | eCommerce engine **khusus penjual kecil Indonesia**: checkout tamu/akun, **Xendit + transfer manual (upload bukti & review)**, ongkir **RajaOngkir/Komerce (8 kurir)** + metode kustom, admin + dashboard omzet, bilingual ID/EN, AI tulis deskripsi (OpenAI-compatible) | NestJS/Fastify + Postgres + EJS · Docker | ✅ MIT | 69 (**subs 1**) | SalesAgent + WebBuilder | ⚠️ **PELAJARI/PANTAU** — kebutuhannya **paling mirip kita** (Xendit + kurir lokal + klaim jalan di **1 vCPU/1GB RAM**) **tapi** proyek mini & **tak diupdate sejak 2026-06-05** → pakai sebagai **pola/referensi**, bukan fondasi |

### 🔎 Cadangan & jebakan toko online
| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/reactioncommerce/reaction | 12.397 | GPL-3.0 — README-nya sendiri bilang **"Project has been discontinued"** → **jangan dipakai**. |
| github.com/vendurehq/vendure | 8.517 | ⚠️ **BUKAN MIT walau `spdx=NOASSERTION`**: `LICENSE.md` = **GPLv3 (Community Edition)** atau **Vendure Commercial License (VCL)**. GPLv3 → hati-hati kalau dicampur produk tertutup. |
| github.com/medusajs/nextjs-starter-medusa | 2.789 | MIT **tapi `archived=true`** (push terakhir 2026-04-23) → starter resmi di repo itu sudah ditinggalkan walau **induknya super aktif**; ambil starter dari docs Medusa / `medusajs/b2b-starter-medusa`. |
| github.com/woocommerce/woocommerce · PrestaShop/PrestaShop | 10.550 (523) · 9.229 (444) | Raksasa yang **klien UMKM sudah kenal** & watchers besar — tapi berbasis **tema + plugin** (kelihatan generik) dan berat di VPS kecil → bertentangan dengan prinsip **anti-template**; pakai hanya kalau klien memang minta. |
| github.com/lunarphp/lunar · solidusio/solidus · itswadesh/svelte-commerce | 3.755 · 5.342 · 1.820 | Semua MIT/BSD (Laravel headless · Rails · SvelteKit storefront untuk 26 backend) → referensi kalau stack-nya cocok. |

**Kesimpulan buat Webuilder/SalesAgent:**
1. **Model yang benar buat kita = headless**: mesin toko (**Medusa MIT** atau **Saleor BSD**) terpisah dari **frontend custom kita** (Astro/Next) → toko tetap *tidak kelihatan template*.
2. Untuk paket **"toko UMKM desa"** yang ringan, sering **tidak perlu** full commerce stack: **katalog statis (Astro) + checkout lewat WhatsApp/WAHA + bayar via Xendit/transfer** (pola **OpenUMKM**) jauh lebih murah & hemat RAM daripada menjalankan backend commerce.
3. **Jangan pasang stack commerce di VPS 1,9 GB ini** — commerce butuh Postgres + proses Node/Python terus-menerus; rencanakan **VPS khusus web** (lihat bagian PaaS 2026-10-14).

---

## 🕹️ OpsAgent / RepoScout — Browser Agent (agen yang benar-benar mengoperasikan web)

> Riset **2026-10-15** — rotasi topik kedua: **agentic AI, sudut baru: "computer-use / browser agent"**.
> Katalog sudah punya `playwright-mcp` (MCP browser), tapi belum ada **framework agen yang mengemudikan web** (isi form, klik, ambil data) — kemampuan yang persis dibutuhkan kalau agen kita harus bekerja di situs **desa/PSE yang tak punya API**, atau menguji situs klien.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (watchers) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **browser-use** | github.com/browser-use/browser-use | Framework Python: **agen LLM mengemudikan browser** seperti manusia (isi form, booking, ambil data) — sekarang **juga jadi MCP server** | Python | ✅ MIT | 117.993 (**481** — rasio ⭐:watchers **245:1**, sehat) | OpsAgent + RepoScout | ✅ **REKOMENDASI** — paling matang di kategori; bisa dicolok ke Hermes via MCP |
| **Stagehand** | github.com/browserbase/stagehand | **SDK browser agent (TypeScript)** di atas Playwright: primitif `act` / `extract` / `observe` / `agent` — gabung kode + bahasa manusia | TypeScript / Playwright | ✅ MIT | 25.669 (104) | WebBuilder + OpsAgent | ✅ PAKAI — dasar bagus buat **"agen QA"** yang menguji situs klien (sekamar dengan skill `dogfood`) |
| **Lightpanda** | github.com/lightpanda-io/browser | Headless browser **dibuat dari nol (Zig)** khusus agen/crawler — benchmark: **123 MB vs 2 GB RAM** & 9x lebih cepat dari Chrome (100 halaman); sudah jalan **JS via V8** | Zig (binary) / npm | ⚠️ **AGPL-3.0** | 36.500 (98) | OpsAgent | ✅ **PELAJARI / PAKAI INTERNAL** — kandidat **hemat RAM VPS** (kita ketat memori); AGPL → hati-hati kalau masuk produk yang dijual |
| **agent-browser** | github.com/vercel-labs/agent-browser | **CLI Rust** buat agen: `npm i -g agent-browser` lalu perintah buka/klik/ekstrak (unduh Chrome for Testing sendiri) | Rust / npm | ✅ Apache-2.0 | 43.983 (107) | OpsAgent | ⚠️ PELAJARI — dari Vercel Labs & commit aktif (66 commit/60 hari), tapi ⭐ 44k dalam 9 bulan → uji dulu |
| **Skyvern** | github.com/Skyvern-AI/skyvern | Otomasi workflow browser pakai LLM + **computer vision** (klaim tahan perubahan layout), ada UI | Python | ⚠️ AGPL-3.0 | 23.198 (101) | OpsAgent | ⚠️ CADANGAN — AGPL + butuh browser penuh (berat untuk VPS kita) |
| **Nanobrowser** | github.com/nanobrowser/nanobrowser | Ekstensi Chrome: beberapa agen AI bekerja di browser **punya user sendiri** (bring-your-own API key) | TypeScript | ✅ Apache-2.0 | 14.089 (70) | OpsAgent + user | ⚠️ CADANGAN — buat **PC user (Windows)**, bukan VPS |
| **Magentic-UI** | github.com/microsoft/magentic-ui | Prototipe Microsoft: agen bekerja lintas **browser + file lokal** (human-in-the-loop) | Python | ✅ MIT | 10.097 (71) | RepoScout | ⚠️ PANTAU — eksperimental |
| **Steel Browser** | github.com/steel-dev/steel-browser | "Browser API" open-source buat agen: self-host sesi browser siap pakai | TypeScript / Docker | ✅ Apache-2.0 | 7.805 (21) | OpsAgent | ⚠️ CADANGAN |

### 🔎 Catatan browser agent (2026: kategori paling "hype")
- ⚠️ **Kategori ini penuh repo 2026 yang ⭐-nya meledak dalam hitungan bulan**: `lexmount/moli` 18,4k⭐ (dibuat **2026-08-10**!), `h4ckf0r0day/obscura` 28,9k⭐, `jackwener/OpenCLI` 30,3k⭐, `citrolabs/ego-lite` 17,4k⭐, `jo-inc/camofox-browser` 11,6k⭐, `Leonxlnx/taste-skill` 96,4k⭐ — watchers cuma **30–296** sementara ⭐ puluhan ribu. **Bedanya dengan repo mati:** semuanya **aktif** (66–100+ commit/60 hari, 10–100 kontributor) → jadi sebut **"muda & hype-driven, uji dulu"**, **jangan** langsung cap star-farm. Cek cepat volume kerja nyata:
  ```bash
  gh api "repos/O/R/commits?since=2026-08-15&per_page=100" --jq 'length'
  gh api "repos/O/R/contributors?per_page=100&anon=1" --jq 'length'
  ```
- 🚫 **Hindari yang menjual "stealth / bypass anti-bot"** (`camofox-browser` — klaim tembus Cloudflare, `obscura`) buat pekerjaan klien: risiko etis + legal + aturan platform; kebutuhan kita (situs desa/PSE, uji situs sendiri) tidak butuh itu.
- 💾 **RAM = pertimbangan pertama kita**: browser agen apa pun butuh Chromium/Chrome (~2 GB kalau banyak tab). Urutan hemat: **Lightpanda** (123 MB) → `agent-browser`/Stagehand (Chrome headless per-sesi, matikan setelah selesai) → **browser-use** (paling fleksibel, tapi paling berat). Jalankan sebagai tugas sekali-jalan, **bukan** service yang menetap di VPS.

---

## 🏛️ WebBuilder / SalesAgent — Ekosistem Digital Desa Indonesia (SID, data wilayah, naik kelas ke kabupaten)

> Riset **2026-10-16** — rotasi topik: **web dev/pemerintah, sudut yang belum pernah disentuh: apa yang SUDAH dipakai desa Indonesia**. Katalog sudah penuh alat "modern" (Astro, CMS, e-commerce), tapi belum pernah mencatat **pemain de-facto di lapangan**: kalau kita jual "desa digital", kita harus tahu desa sudah jalan pakai apa.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (watchers) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **OpenSID** | github.com/OpenSID/OpenSID | **SID de-facto nasional** (1.197 fork!) — administrasi desa, surat, penduduk, statistik, web desa. Dikelola **Perkumpulan Desa Digital Terbuka** (opendesa.id) | PHP 8.1 (CodeIgniter 3 + Illuminate 10, HMVC `Modules/`) | ⚠️ **GPL-3.0-or-later** (spdx `NOASSERTION`, tapi `LICENSE` = GPLv3 & `composer.json` bilang GPL-3.0-or-later) | 1.229 (110) | WebBuilder + SalesAgent | ⚠️ **PELAJARI WAJIB** — jangan lawan, **jangan salin kodenya** (lihat catatan) |
| **OpenKab** | github.com/OpenSID/OpenKab | **Dasbor tingkat KABUPATEN**: menarik data dari **database gabungan OpenSID** → statistik desa, penduduk, kesehatan, pendidikan; ada **SSO** ke panel admin OpenSID | PHP/Blade (Laravel) | ✅ **GPL-3.0** | 16 (8) — push **2026-10-15** (aktif) | WebBuilder + SalesAgent | ✅ **PELAJARI** — ini **persis jalur "naik kelas ke kabupaten"** versi mereka |
| **SIDeGa** | github.com/desagarut/sidega-master | SID tingkat kabupaten (**Garut**) — pengelolaan data desa se-kabupaten | PHP | ✅ GPL-3.0 | 104 (1) · push 2026-09-07 | SalesAgent | ⚠️ REFERENSI kompetitor — single-maintainer (forks 1) |
| **cahyadsn/wilayah** | github.com/cahyadsn/wilayah | **Data kode wilayah Indonesia (Kepmendagri)** — provinsi→desa + aplikasi/API + changelog update | SQL / PHP | ✅ **MIT** | 1.325 (50) · push **2026-10-14** | WebBuilder + OpsAgent | ✅ **PAKAI** — buat dropdown alamat, validasi kode desa, isian form klien |
| **laravolt/indonesia** | github.com/laravolt/indonesia | Package Laravel: data Provinsi/Kabupaten/Kecamatan/Desa | PHP (Laravel) | perlu cek file | 679 (?) | WebBuilder | 🔸 CADANGAN — hanya kalau proyek Laravel |
| **edwardsamuel/Wilayah-Administratif-Indonesia** | github.com/edwardsamuel/Wilayah-Administratif-Indonesia | Data wilayah lengkap (Python) | Python | perlu cek | 960 | OpsAgent | 🔸 CADANGAN data |
| **emsifa/api-wilayah-indonesia** | github.com/emsifa/api-wilayah-indonesia | REST API wilayah populer (kini ada `SKILL.md`, `cli/`, `web/`) | TypeScript | ❌ **TANPA file lisensi apa pun** | 755 (5) · push 2026-10-11 | — | 🚫 **JANGAN PAKAI** — tanpa LICENSE = *all rights reserved* (lihat pelajaran) |
| **sqllite-api-wilayah-indonesia** | github.com/maftuh23/sqllite-api-wilayah-indonesia | **Database SQLite wilayah Indonesia (BPS)** siap pakai + API 1 container | Dockerfile / SQLite | ✅ MIT | 328 (2) · push 2025-08 (agak idle) | OpsAgent | 🔸 CADANGAN — paling ringan kalau butuh self-host |
| **wilayah-indonesia-api** | github.com/edopandoyo/wilayah-indonesia-api | REST API + batas GeoJSON wilayah (MinIO) | TypeScript | ❌ tanpa lisensi | 82 (0) · dibuat **2026-08-03** | — | 🚫 SKIP — tanpa lisensi + terlalu muda |
| **cosmo** (tema OpenSID) | github.com/dikisiswanto/cosmo | Tema web OpenSID minimalis | CSS | ✅ MIT | 58 (1) · push 2022 | DesignerBot | ⚠️ **ARCHIVED** — contoh ekosistem tema OpenSID yang ditinggalkan |
| **tema-natra** | github.com/OpenSID/tema-natra | Tema resmi OpenSID | Blade | ❌ tanpa file lisensi | 29 (12) | DesignerBot | 🔸 hanya referensi struktur tema |
| **simdesa** | github.com/pandigresik/simdesa | SID surat-menyurat + kependudukan (dulu populer, 91 fork) | PHP | ❌ tanpa lisensi | 61 (15) · push **2015** | — | 🚫 MATI — legacy, jangan disarankan |

### 🔎 Catatan ekosistem desa (PENTING buat strategi jualan)
- 🏛️ **Desa Indonesia sudah punya "standar de-facto": OpenSID.** 1.229⭐ + **1.197 fork** + 110 watchers + forum/komunitas (opendesa.id) → **jangan jual "SID baru"**, itu perang di kandang orang. Posisi yang benar buat Webuild: **lapisan modern di atas data desa** (web publik Astro yang cepat + peta/potensi desa + katalog UMKM + transparansi anggaran) **atau** integrasi (pola **OpenKab**: baca **database gabungan** + SSO). Tanya tiap klien desa: *"sudah pakai OpenSID versi apa?"* — jawabannya mengubah penawaran kita total.
- ⚖️ **OpenSID = GPL-3.0 → ada efek copyleft.** Kita **boleh** memakai/memodifikasi/menjual *jasa* di atasnya, tapi **modifikasi kode OpenSID harus tetap dibuka (GPL-3)**. Jadi **jangan menyalin kode OpenSID ke produk komersial tertutup** kita (web builder/paket berlangganan). Aman: (a) pakai OpenSID apa adanya sebagai aplikasi desa, (b) bikin **frontend/alat terpisah milik kita** yang membaca data yang boleh diakses (API/DB/ekspor), (c) jual jasa instalasi+pendampingan+kustomisasi (GPL memperbolehkan jual jasa).
- 💰 **Model OpenSID = "open core dengan jendela tunda"**, bukan open source murni: repo GPL-3, tapi ada **"Versi Publik (UMUM)" vs "Versi Premium"** — fitur premium masuk publik **ditunda 6 bulan**, dan **beberapa fitur tidak akan pernah** dirilis publik. **Fakta lapangan: rilis publik terakhir `v2607.0.1` = 24 Juli 2026 (≈12 minggu lalu)** → jalur aktif mereka ada di `OpenSID/premium`. Artinya: jangan janji ke klien "OpenSID selalu selangkah dengan versi premium".
- 💾 **Ukuran repo OpenSID ≈ 250 MB** (`size=256287` KB) → jangan clone ke dalam vault; kalau perlu uji, ke `/root/repos/` (disk kita 22 GB free, tapi VPS RAM-ketat).
- ❌ **"Ada di GitHub" ≠ open source.** `emsifa/api-wilayah-indonesia` (755⭐, aktif) **tidak punya file LICENSE sama sekali** → hukumnya *all rights reserved*: dilarang dipakai di produk komersial walau populer. Mitra aman yang berlisensi jelas = **cahyadsn/wilayah (MIT, 1.325⭐)**.
- 🔍 **Query `desa` = jebakan bahasa (substring!).** GitHub search mencocokkan **potongan kata**, jadi `desa` menarik repo **Portugis Brasil/Sepanyol**: `desafio`/`desafios` (= "tantangan", mis. `backend-br/desafios` 2.712⭐, `PicPay/picpay-desafio-backend` 2.306⭐) dan `desarrollo`. Query yang benar buat tema desa: **`opensid`**, **`sistem+informasi+desa`**, **`aplikasi+desa`**, **`pemerintah+desa`**, atau **`kelurahan`** — plus `+NOT+desafio+NOT+desafios+NOT+desarrollo` kalau tetap pakai kata `desa`.

---

## 🎬 MotionAgent — Video Programmatic & Editing (konten pemasaran klien)

> Riset **2026-10-16** — rotasi topik kedua: **content creation, sudut baru: membuat & mengedit video secara programatik** (katalog punya "video AI" sebatas generator, belum ada **mesin video berbasis kode** — yang paling cocok buat tim agent karena bisa ditulis/di-render otomatis tanpa editor manual).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (watchers) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Remotion** | github.com/remotion-dev/remotion | **Bikin video pakai React** — komposisi video = komponen TS, render MP4 lewat CLI/SSR. Standar de-facto video programatik | TypeScript / React | ⚠️ **Lisensi DUA TINGKAT**: gratis (termasuk komersial) untuk **individu & perusahaan ≤3 karyawan**; di atas itu wajib **Company License** (remotion.pro) | 64.384 (189) · 100+ commit/60 hari | MotionAgent | ✅ **PAKAI** — Webuild masih kecil → legal; **catat ambang 3 karyawan** |
| **Motion Canvas** | github.com/motion-canvas/motion-canvas | Animasikan & render video dengan kode TS (editor visual + preview realtime) — pengganti bebas Remotion | TypeScript | ✅ **MIT penuh** (tanpa batas ukuran perusahaan) | 19.345 (91) · push 2026-07-02 | MotionAgent | 🔸 **CADANGAN UTAMA** — pilih ini kalau tak mau repot lisensi; keaktifan melambat |
| **Revideo** | github.com/midrender/revideo | **API programmatic** untuk membuat video (fork/diturunkan dari Motion Canvas, siap dipanggil dari skrip/agen) | TypeScript | ✅ MIT | 4.111 (17) · push 2026-07-15 | MotionAgent | 🔸 CADANGAN — ⚠️ org **ganti nama**: `redotvideo` → **`midrender`** |
| **Graphite** | github.com/GraphiteEditor/Graphite | Aplikasi **desain 2D/vektor + motion** berbasis node (alternatif Illustrator/After Effects, gratis) | Rust (desktop/web) | ✅ **MIT + Apache-2.0** (dual) | 27.622 (133) · push 2026-10-15 | DesignerBot + MotionAgent | ✅ **PAKAI di PC user** — bukan untuk VPS (aplikasi desktop, berat) |
| **openfilm** | github.com/openfilm/openfilm | **"AI video agent"**: agen coding menulis film sebagai halaman web (`film.html`, `frame(t)`), lalu diedit di **Studio** (browser, timeline). `npx skills add openfilm/openfilm` = skill agen | TypeScript / Node 22 + ffmpeg + Chromium (~100 MB) | ✅ MIT | 407 (7) · dibuat **2026-10-04** | MotionAgent | ⚠️ **UJI DULU** — konsepnya paling pas dengan tim kita, tapi repo baru 12 hari |
| **anything2explainer** | github.com/Vincentwei1021/anything2explainer | **Skill Claude Code/Codex**: topik → **video explainer** motion-graphics + TTS + subtitle (pakai Remotion, ada protokol multi-agen) | TypeScript / Remotion | ❌ **PolyForm Noncommercial 1.0.0** — komersial perlu izin penulis | 2.523 (8) · dibuat 2026-09-08 | MotionAgent | 🚫 **NON-KOMERSIAL** — boleh dipelajari metodenya, **jangan dipakai untuk klien berbayar** |
| **motionity** | github.com/alyssaxuu/motionity | Editor motion graphics berbasis web (animasi keyframe di kanvas) | JavaScript | ✅ MIT | 4.122 (31) · push **2022** | MotionAgent | ⚠️ DORMANT — referensi UI saja |
| **mojs** | github.com/mojs/mojs | Toolbelt motion graphics untuk web (animasi mikro di situs klien) | CoffeeScript/JS | ✅ MIT | 18.816 (?) | WebBuilder | 🔸 CADANGAN — animasi web ringan, bukan video |
| **astrofox** | github.com/astrofox-io/astrofox | Motion graphics dari **audio** (visualizer musik) | TypeScript | perlu cek | 2.003 | MotionAgent | 🔸 CADANGAN niche |
| **TiXL** | github.com/tixl3d/tixl | Alat **motion graphics realtime** (node graph, Windows) | C# | perlu cek | 5.145 | MotionAgent | 🔸 CADANGAN — desktop Windows |
| **Klaster "AI video editor" 2026** | `0xsline/OpenChatCut` · `cartesiancs/cartcut` · `WeftCut/WeftCut` | Editor video ber-agen (timeline multi-track, edit lewat chat/teks) | TypeScript | ⚠️ OpenChatCut **AGPL-3.0**; cartcut & WeftCut **MIT** | 2.393 (8) · 814 (6) · 224 (7) | MotionAgent | ⚠️ **UJI DULU** — watchers 6–8 → muda/hype; jangan fondasi |

### 🔎 Catatan video programmatic
- 🧭 **Buat konten pemasaran klien, urutannya jelas**: butuh video yang bisa di-render ulang otomatis tiap ganti teks/harga → **Remotion (React)**; tak mau terikat lisensi berjenjang → **Motion Canvas / Revideo (MIT)**; mau agen yang menyutradarai sendiri → **openfilm** (paling baru, pantau). Untuk desain grafis/motion statis di PC user → **Graphite**.
- 💾 **Render video = kerja berat (CPU + disk besar)**. Jangan jadikan Remotion/renderer sebagai *service* menetap di VPS 1,9 GB; **jalankan sekali-jalan** (atau di PC user), lalu simpan hasilnya sebagai file.
- 🎯 **Untuk "video desa/UMKM" jangan mulai dari video generatif** (biaya API, hasil tak stabil). Yang paling cepat berguna: **slideshow/template Remotion dari data desa** (statistik, potensi, agenda) + **voice-over TTS** (VoiceAgent) → bisa dibikin sekali, dipakai berkali-kali.

---

## 📚 RepoScout / OpsAgent — RAG: tanya-jawab DOKUMEN (dokumen desa, proposal, regulasi)

> Riset **2026-10-17** — rotasi topik: **agentic AI, sudut baru: RAG (tanya-jawab atas dokumen)**.
> Katalog sudah punya *memori codebase* (`codebase-memory-mcp`) & *knowledge graph* (`Graphify`), tapi **belum punya mesin RAG buat DOKUMEN** — padahal tim kita kebanjiran PDF (dokumen desa, proposal ke kades, regulasi Komdigi/LKPP). Kebutuhannya konkret: *"tanya dokumen apa pun → dijawab, plus ada sitasi halaman"*.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **haiku.rag** | github.com/ggozad/haiku.rag | **Agentic RAG tanpa server**: database **LanceDB tertanam** (tanpa server DB & tanpa API key), ingest PDF/office/HTML/MD/gambar pakai **Docling** (heading, tabel, provenance halaman tersimpan), pencarian **hybrid vector+full-text** + reranking opsional, **jawaban bersitasi nomor halaman + heading**, cek sitasi dengan menggambar chunk di gambar halaman, bisa jalankan **Python sandbox** atas dokumen (hitung/agregasi), ada **MCP server** + CLI + TUI + Python API + service ingester (filesystem/HTTP/S3/WebDAV, antrean SQLite/Postgres) | Python 3.12 / LanceDB / Pydantic AI / Docling | ✅ **MIT** | 629 (**7**) | RepoScout + OpsAgent + ContentWriter | ✅ **REKOMENDASI** — paling cocok VPS kita (nol container, nol API key); aktif: **100 commit/60 hari**, 13 kontributor |
| **AnythingLLM** | github.com/Mintplex-Labs/anything-llm | **All-in-one "ChatGPT privat"**: chat dengan dokumen, agen bawaan, multi-user + permission, vector DB & pipeline dokumen, **agent builder no-code (Agent Flows)**, **MCP-compatible**, **Scheduled Tasks** (cron), **chat widget yang bisa ditempel di situs klien** (versi Docker), desktop app Win/Mac/Linux | JavaScript / Node + React | ✅ **MIT** (`LICENSE`; ada `TERMS_SELF_HOSTED.md` = privasi/telemetri, **bukan** pembatas lisensi; **tanpa** folder `ee/`) | 67.210 (**418**) | OpsAgent + SalesAgent | ✅ **REKOMENDASI (Docker)** — `docker/docker-compose.yml` = **1 service saja**; bisa jadi "tanya dokumen desa" + widget FAQ di situs desa |
| **RAGFlow** | github.com/infiniflow/ragflow | RAG kelas enterprise: parsing dokumen dalam (layout/tabel), knowledge graph, agent, UI lengkap | Go / Python + Docker | ✅ Apache-2.0 | 92.335 (**362**) | OpsAgent | ⚠️ **PELAJARI (bukan di VPS ini)** — `docker/docker-compose-base.yml` = **17 service** (Elasticsearch/OpenSearch, MySQL, MinIO, Redis/kvrocks, NATS, ClickHouse, Jaeger, sandbox-executor…) |
| **Dify** | github.com/langgenius/dify | Platform agentic workflow + RAG pipeline + UI builder | Python / TypeScript + Docker | ⚠️ **"modified Apache 2.0"** (lihat catatan) | 158.664 (**841**) | OpsAgent | ⚠️ **INTERNAL SAJA / HATI-HATI JUAL-LAYANAN** — compose (api, worker, web, db_postgres, redis, sandbox, plugin_daemon, ssrf_proxy, nginx, weaviate) berat untuk VPS 1,9 GB |
| **FastGPT** | github.com/labring/FastGPT | Platform knowledge base + orkestrasi alur AI (UI + API) | TypeScript + Docker | ⚠️ **"FastGPT Open Source License"** (Apache + syarat sama spt Dify) | 29.842 (**152**) | OpsAgent | ⚠️ CADANGAN — **14 service** di `deploy/dev/docker-compose.yml` |
| **Open WebUI** | github.com/open-webui/open-webui | Front-end chat LLM paling populer (mirip ChatGPT), bisa RAG dokumen, multi-user | Python / Svelte | ⚠️ **"Open WebUI License"** (BSD-3 gaya + **klausul branding**, lihat catatan) | 155.919 (**678**) | OpsAgent | ⚠️ PELAJARI — compose cuma **2 service** (ollama + open-webui) & cepat dipasang, **tapi** jangan dipakai sebagai front-end ber-label kita untuk klien banyak user |
| **Kotaemon** | github.com/Cinnamon/kotaemon | RAG berbasis UI buat chat dengan dokumen (ada riset GraphRAG, multi-user, hybrid) | Python / Gradio | ✅ Apache-2.0 | 25.808 (**130**) | RepoScout | ⚠️ PANTAU — fungsinya pas, **tapi melambat**: push terakhir **2026-07-14** (±3 bulan) |
| **localGPT** | github.com/PromtEngineer/localGPT | Chat dengan dokumen **100% lokal/offline** (data tak keluar mesin) | Python / LangChain | ✅ MIT | 22.194 (**180**) | RepoScout | ✅ CADANGAN — repo kecil (6 MB), bagus buat eksperimen cepat di PC user/VPS |
| **nashsu/llm_wiki** | github.com/nashsu/llm_wiki | App desktop: dokumen → **wiki terorganisir** yang bisa dijelajah & ditanya (nyambung dgn skill `llm-wiki` kita) | TypeScript / Electron | ⚠️ **GPL-3.0** (API bilang `NOASSERTION`!) | 20.709 (**88**) | RepoScout | ⚠️ PELAJARI metodenya — **jangan salin kodenya** ke produk tertutup kita (GPL) |
| **Fess** | github.com/codelibs/fess | **Search server** self-hosted (di atas OpenSearch): crawl web & file → pencarian situs/internal | Java / OpenSearch | ✅ Apache-2.0 | 1.141 (**58**) | OpsAgent | 🔸 CADANGAN — jalur "pencarian isi situs desa", tapi Java + OpenSearch = berat |

### 🔎 Catatan RAG (PENTING: hitung service dulu, jangan janji self-host)
- 💾 **Urutan dari paling ringan** (hasil hitung nyata dari file compose): **haiku.rag** = **0 container** (LanceDB tertanam) → **AnythingLLM** = **1 service** → **Open WebUI** = 2 → **Dify** ≈ 10 core → **FastGPT** = 14 → **RAGFlow** = **17** (Elasticsearch + MySQL + MinIO + Redis + NATS + ClickHouse + Jaeger). VPS kita (1,9 GB, available ~200–330 MB) **hanya realistis untuk 2 yang pertama**.
- ⚖️ **Jebakan lisensi ke-9 — "modified Apache 2.0" (fair-code versi platform AI).** **Dify** & **FastGPT** menulis di baris pertama LICENSE: Apache-2.0 **+ syarat**: (a) **dilarang menjalankan sebagai multi-tenant** (1 workspace = 1 tenant) tanpa lisensi komersial tertulis, (b) **dilarang menghapus/mengubah LOGO & copyright di frontend** (`web/`). Jadi kode boleh dipakai, **tapi jangan dijual sebagai layanan ber-label sendiri**.
- ⚖️ **Jebakan lisensi ke-10 — lisensi buatan sendiri dengan AMBANG PENGGUNA.** **Open WebUI** pakai "Open WebUI License": klausul 4 **melarang** menghapus/mengubah branding "Open WebUI" **kecuali** (i) total end-user **≤50 orang dalam 30 hari bergulir**, (ii) ada izin tertulis, atau (iii) punya lisensi enterprise. Untuk klien desa (puluhan user) masih aman, **tapi** jangan jadikan front-end bertanda Webuild untuk ratusan user.
- 📄 **File terms terpisah ≠ pembatas lisensi.** **AnythingLLM** punya `TERMS_SELF_HOSTED.md` — isinya **privasi/telemetri & no-warranty** dan **menegaskan inti = MIT**. Baca dulu, tapi jangan salah klasifikasi seperti `LICENSE_EE.md` / `LICENSING.md` (yang itu memang gerbang komersial).
- 🧩 **GPL masih bisa sembunyi di balik `NOASSERTION`**: `nashsu/llm_wiki` API-nya `NOASSERTION`, file LICENSE = **GPL-3.0**.

**Kesimpulan buat tim:** (1) **pemahaman dokumen desa** → JANGAN mulai dari platform besar; mulai **`haiku.rag`** (MIT, embedded, ada MCP → bisa dicolok ke agen kita) untuk uji cepat "tanya APBDes/proposal"; (2) kalau butuh **UI untuk klien/desa** → **AnythingLLM** (MIT, 1 container, ada widget embed); (3) **jangan** pasang RAGFlow/Dify/FastGPT di VPS ini; (4) nada jualan yang benar: *"FAQ & tanya-jawab dokumen desa, jalan di server sendiri, data tidak ke luar"* — sejalan dengan paket **"situs desa PDP-ready"**.

---

## 🎨 DesignerBot / ContentWriter / SocialAgent — Bahan baku visual BEBAS (ikon, emoji, avatar, font)

> Riset **2026-10-17** — rotasi topik kedua: **design/UI, sudut yang belum ada**. Katalog sudah penuh **ALAT** desain (`designlang`, `Dembrandt`, shadcn, Magic UI), tapi belum pernah mencatat **BAHAN-nya**: aset visual legal buat dipakai di situs klien. Ini pengungkit anti-template paling murah: ganti font + set ikon + ilustrasi, situs langsung tidak terasa "theme beli".
> Semua lisensi diverifikasi dari **file lisensi asli** (bukan `spdx_id`), termasuk file yang mudah terlewat (`LICENSE-GRAPHICS`).

| Nama | URL | Fungsi | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|
| **Lucide** | github.com/lucide-icons/lucide | Toolkit ikon stroke konsisten (dipakai ekosistem shadcn), tree-shakeable, banyak framework | ✅ **ISC** (API bilang `NOASSERTION`!) | 25.082 (60) | DesignerBot + WebBuilder | ✅ **PAKAI** — default ikon UI Webuild |
| **Tabler Icons** | github.com/tabler/tabler-icons | **6.200+ ikon** SVG konsisten (outline & filled) | ✅ MIT | 22.342 (110) | DesignerBot + WebBuilder | ✅ PAKAI — set besar buat ikon fitur/layanan desa |
| **Iconify** | github.com/iconify/iconify | **Satu API/komponen → 243 set ikon** (runtime, SVG on-demand) | ✅ MIT (**framework**) ⚠️ **lisensi per-SET** | 6.366 (24) | WebBuilder + DesignerBot | ✅ PAKAI — **tapi pilih set berlisensi MIT/Apache** (lihat catatan) |
| **Iconoir** | github.com/iconoir-icons/iconoir | Set ikon konsisten (1.500+), React/TS siap pakai | ✅ MIT | 4.584 (28) | DesignerBot | 🔸 CADANGAN |
| **Heroicons** | github.com/tailwindlabs/heroicons | Ikon resmi Tailwind Labs (outline/solid/mini/micro) | ✅ MIT | 23.870 (166) | WebBuilder | ⚠️ CADANGAN — push terakhir 2026-05 (melambat, tapi stabil) |
| **Simple Icons** | github.com/simple-icons/simple-icons | **3.000+ logo merek** (buat tautan sosmed/footer klien) | ✅ **CC0-1.0** (merek tetap milik pemiliknya — jangan seolah endorse) | 26.022 (178) | WebBuilder + SocialAgent | ✅ PAKAI |
| **Material Symbols** | github.com/google/material-design-icons | Set ikon raksasa Google (Material Symbols, variable font) | ✅ Apache-2.0 | 54.120 (**1.800**) | DesignerBot | ✅ CADANGAN — kalau butuh ikon "familiar" & sangat banyak |
| **pqoqubbw/icons** | github.com/pqoqubbw/icons | **Ikon beranimasi** siap tempel (React + motion) — micro-interaction landing | ✅ MIT | 8.214 (**14**) | DesignerBot + MotionAgent | ✅ PAKAI — bikin landing terasa "mahal" tanpa video |
| **Meteocons** | github.com/basmilius/meteocons | Ikon **cuaca** beranimasi tangan (juga buat widget data desa) | ✅ MIT | 1.672 (25) | MotionAgent | 🔸 CADANGAN |
| **react-useanimations / animateicons** | github.com/useAnimations/react-useanimations · github.com/Avijit07x/animateicons | Koleksi ikon beranimasi React (menu, loading, social) | ✅ MIT (keduanya) | 1.248 (10) · 1.261 (5) | WebBuilder | 🔸 CADANGAN |
| **Fontsource** | github.com/fontsource/fontsource | **Self-host font open source lewat npm** (tanpa CDN Google) — variable font, i18n | ✅ MIT (**paketnya**) ⚠️ **font-nya lisensi sendiri** | 6.205 (18) | WebBuilder + DesignerBot | ✅ **PAKAI** — ganti font = cara #1 bikin situs tidak kelihatan template |
| **google-webfonts-helper** | github.com/majodev/google-webfonts-helper | Ambil font Google → **woff/woff2 + CSS siap self-host** (tanpa request ke Google) | ✅ MIT | 13.073 (103) | WebBuilder + OpsAgent | ✅ PAKAI — bonus privasi (sejalan paket "PDP-ready") |
| **Subfont** | github.com/Munter/subfont | **Subsetting font agresif** sesuai teks yang benar-benar dipakai + preload | ✅ MIT | 1.636 (12) | OpsAgent + WebBuilder | ✅ PAKAI — situs desa lebih cepat (font sering jadi beban terberat) |
| **Fluent Emoji** | github.com/microsoft/fluentui-emoji | Set emoji resmi Microsoft (3D/flat) buat konten & ikon | ✅ MIT | 10.166 (65) | SocialAgent + ContentWriter | ✅ PAKAI — emoji legal buat konten sosmed |
| **Noto Emoji** | github.com/googlefonts/noto-emoji | Emoji Noto Google (juga **monokrom**, cocok jadi ikon) | ✅ OFL-1.1 | 5.074 (**119**) | ContentWriter | ✅ CADANGAN |
| **DiceBear** | github.com/dicebear/dicebear | **Generator avatar** (banyak gaya) — buat profil UMKM/warga tanpa upload foto | ✅ MIT (**kode**) ⚠️ **gaya = lisensi masing-masing** | 9.870 (34) | WebBuilder + DesignerBot | ✅ PAKAI — cek `/licenses` per gaya (banyak minta atribusi) |
| **OpenMoji** | github.com/hfg-gmuend/openmoji | Set emoji open source (garis, konsisten) | ⚠️ **CC-BY-SA-4.0** (atribusi **+ share-alike**) | 4.564 (45) | — | 🚫 **HATI-HATI** — buat klien berbayar pakai **Fluent Emoji (MIT)** |
| **Twemoji** | github.com/jdecked/twemoji | Emoji Twitter (dipakai luas) | ⚠️ **kode MIT, GRAFIS CC-BY 4.0** (`LICENSE-GRAPHICS`) | 1.881 (21) | — | ⚠️ atribusi wajib kalau dipakai |

### 🔎 Catatan aset visual (jebakan lisensi ke-8: **lisensi paket ≠ lisensi ISI paket**)
- 🧩 **Repo "katalog aset" harus dicek PER-ITEM.** **Iconify** (framework MIT) mendistribusikan **243 set**: **112 MIT · 52 CC BY 4.0 (wajib atribusi) · 31 Apache-2.0 · 13 OFL · 6 CC BY-SA · 4 GPL · 6 CC0 · 4 ISC** — contoh nyata: set **`solar` = CC BY 4.0**. Cara cek cepat:
  ```bash
  curl -s https://api.iconify.design/collections | python3 -c "import sys,json,collections;d=json.load(sys.stdin);print(len(d));print(collections.Counter((v.get('license') or {}).get('title') for v in d.values()).most_common(8))"
  ```
- 🔤 **Fontsource: paketnya MIT, font-nya tidak.** README-nya sendiri berbunyi: *"Always make sure to read the license for each font you use. Most of the fonts in the collection use the SIL Open Font License, v1.1. Some fonts use the Apache 2 license. The Ubuntu fonts use the Ubuntu Font License v1.0."* → tiap font dicek di `README.md` paketnya. **Ini juga berlaku untuk Google Fonts** (helper-nya MIT, font-nya tetap berlisensi sendiri).
- 🧑🎨 **DiceBear: kode MIT, gaya avatar bergantung pembuatnya** (README: *"The avatar styles are the work of their respective creators and carry their own licenses… many only ask for attribution"*) — banyak gaya populer **CC BY 4.0**.
- 🎨 **Emoji: dua lapis lisensi.** **Twemoji** = kode MIT **+ grafis CC-BY 4.0** (file `LICENSE-GRAPHICS` terpisah!). **OpenMoji** = **CC-BY-SA-4.0** → **share-alike**: turunannya harus berbagi dengan lisensi sama → hindari untuk aset komersial klien; pilih **Fluent Emoji (MIT)** / **Noto Emoji (OFL)**.
- ✅ **ISC & CC0 itu bebas, tapi API-nya bisa bilang `NOASSERTION`** — **Lucide = ISC**, **Simple Icons = CC0-1.0** → jangan simpul "lisensi tak jelas" lalu buang repo-nya.
- 📋 **Praktik aman sekali bikin:** tiap situs klien diberi halaman **`/kredit`** (atau komentar di CSS) yang menyebut aset + lisensinya → atribusi CC BY / OFL / CC0 terpenuhi, urusan legal beres sejak awal. Ini juga argumen jualan ("semua aset legal & bebas royalti").
- 🔍 **Query aset: pakai kata kategori, bukan kata "library".** Yang tajam: `icons+in:name,description+stars:>3000+NOT+awesome`, `animated+icons`, `fonts+self-host`, `emoji+in:name,description`. **`illustration(s)` = zonk** (hasilnya repo *AI illustration skill*, bukan katalog aset) → untuk ilustrasi/pattern, cari **nama proyek langsung** (mis. `openpeeps`, `humaaans`) atau situs katalognya.

---

## 🔗 Terkait
- [[06-Tim-Agent/Team Registry]]
- [[03-Proyek/04-Virtual-Office-Visualisasi/README|Proyek 04 — Virtual Office]]

#reposcout #github #katalog