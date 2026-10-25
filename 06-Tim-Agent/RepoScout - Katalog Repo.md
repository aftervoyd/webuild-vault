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
| github.com/**cosscom/ui** *(dulu `cosscom/coss`)* | 10.720 | Design system resmi **Cal.com** (dulu Origin UI) — kualitas tinggi & sangat aktif, **tapi AGPL-3.0** → hati-hati kalau masuk produk tertutup. ⚠️ **URL diperbarui 2026-10-19:** repo `cosscom/coss` sekarang ⭐3 (kosong/dipakai ulang) — jangan pakai URL lama |
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

## 🧪 WebBuilder / OpsAgent — MUTU SITUS KLIEN: performa, aksesibilitas, pencarian, pratinjau sosial

> Riset **2026-10-18** — rotasi topik: **web dev, sudut yang belum ada: MENGUKUR & MENJAMIN MUTU situs** yang kita jual.
> Katalog sudah penuh alat *membuat* situs (template, komponen, token desain, aset, CMS/mutu), tapi **belum punya satu pun alat untuk membuktikan situs kita cepat, aksesibel, dan tak punya tautan mati**. Buat jualan ke desa/pemda, **angka lebih kuat daripada klaim "modern"** — situs desa dibuka dari HP murah & sinyal lemah.
> Semua lisensi dibaca dari **file lisensi asli** (bukan `spdx_id`).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Pagefind** | github.com/Pagefind/pagefind | **Pencarian statis tanpa server**: index dibuat saat build; pengunjung mengunduh hanya potongan index sesuai halaman (hemat kuota), multilingual (termasuk Indonesia), highlight, filter/faceted | Rust (WASM) + JS | ✅ **MIT** (`LICENSE`) | 5.519 (**16**) · 59 commit/60 hari · 88 kontributor | WebBuilder + OpsAgent | ✅ **PAKAI** — situs desa "banyak berita" jadi bisa dicari warga, **tanpa** Elasticsearch/Meilisearch di VPS |
| **astro-pagefind** | github.com/shishkin/astro-pagefind | Integrasi **Pagefind ↔ Astro** (index otomatis saat build + komponen siap pakai) | Astro | ✅ MIT | 567 (3) · push **2026-10-17** | WebBuilder | ✅ PAKAI — jalur "30 menit" masang pencarian di demo Desa Pamekaran |
| **Unlighthouse** | github.com/harlan-zw/unlighthouse | Jalankan **Lighthouse ke SELURUH halaman** situs sekaligus → dashboard + skor per halaman (bukan cuma 1 URL) | Node / Vue / Chromium | ✅ **MIT** | 4.903 (**27**) · 24 commit/60 hari | WebBuilder + OpsAgent | ✅ **PAKAI** (di PC user / sekali-jalan) — ⚠️ butuh Chromium → **jangan** jadi service di VPS 1,9 GB |
| **Lighthouse CI** | github.com/GoogleChrome/lighthouse-ci | Otomatiskan Lighthouse tiap commit/PR + **jaga ambang skor** (build gagal kalau performa turun) | Node (resmi Google) | ✅ Apache-2.0 | 7.113 (**79**) · push 2026-10-17 | OpsAgent + WebBuilder | ✅ PAKAI — pasang di repo situs klien (GitHub) → "skor tak boleh turun" |
| **lychee** | github.com/lycheeverse/lychee | **Pemeriksa tautan mati** super cepat (Rust, async): file lokal, situs live, atau Markdown | Rust (CLI + GitHub Action) | ✅ **MIT ATAU Apache-2.0** (dual: `LICENSE-MIT` + `LICENSE-APACHE`) | 4.017 (**14**) · 45 commit/60 hari · 100 kontributor | OpsAgent + WebBuilder | ✅ **PAKAI** — gerbang wajib sebelum serah-terima situs klien (tautan mati = malu di depan desa); sekalian buat **vault kita** (banyak tautan keluar) |
| **axe-core** | github.com/dequelabs/axe-core | **Mesin uji aksesibilitas** de-facto (dipakai Lighthouse/Playwright/Cypress), 100+ aturan WCAG | JS (npm; browser/Node) | ⚠️ **MPL-2.0** (bukan MIT — copyleft per-FILE) | 7.658 (**173**) · push 2026-10-15 | DesignerBot + WebBuilder | ✅ PAKAI — dipanggil via `axe-playwright` / `cypress-axe` untuk audit situs klien otomatis |
| **pa11y** | github.com/pa11y/pa11y | **CLI audit aksesibilitas** satu perintah (banyak URL, output JSON/HTML) | Node | ⚠️ **LGPL-3.0** | 4.577 (**215**) · push 2026-10-13 | WebBuilder + DesignerBot | ✅ PAKAI sebagai **alat terpisah** (CLI) — LGPL aman selama tak "dikaitkan" jadi library di produk tertutup kita |
| **Takumi** | github.com/kane50613/takumi | **Render gambar OG & PDF dari JSX/HTML/CSS TANPA headless browser** (Rust + binding JS/WASM) → 1200×630 PNG, WebP, animasi | Rust + JS/TS | ✅ **MIT atau Apache-2.0** (dual, README nyebut jelas) | 3.118 (**2**!) · **100 commit/60 hari** · 37 kontributor | WebBuilder + SocialAgent | ⚠️ **UJI DULU** — ⭐ tinggi tapi watchers **2** & muda (created 2025-06); repo ±**333 MB** (jangan full-clone). Unggulan: **tanpa Chromium** → bisa jalan di VPS kecil |
| **Satori** | github.com/vercel/satori | Library Vercel: HTML/CSS → **SVG** (bahan gambar OG), pasangan `resvg`/`sharp` | TypeScript | ⚠️ **MPL-2.0** | 14.098 (**78**) · push 2026-10-16 | WebBuilder | ✅ CADANGAN — paling matang, tapi butuh renderer tambahan & lebih berat; **Next.js sudah punya `next/og` (ImageResponse) bawaan** |
| **Squoosh** | github.com/GoogleChromeLabs/squoosh | Kompres gambar (WebP/AVIF) **di browser** — siapkan foto desa/UMKM sebelum upload | Web app (WASM) | ✅ Apache-2.0 | 26.035 (**251**) | DesignerBot + ContentWriter | ✅ PAKAI (manual, di PC user) — foto 5 MB → ~150 KB = situs ringan di kuota warga |
| **optimizt** | github.com/funbox/optimizt | CLI kompresi gambar (PNG/JPEG/SVG/WebP) | Node | ✅ MIT | 947 (21) · push **2023-10** | — | 🚫 **MATI** — jangan pakai (3 tahun tanpa update); pakai `sharp` (bawaan Astro) atau Squoosh |

### 🔎 Catatan mutu situs (jadikan "kartu mutu" = bahan jualan)
- 🧾 **Bikin "kartu mutu situs" 1 halaman per klien** — bukti, bukan klaim: skor **Lighthouse per halaman (Unlighthouse)** + **0 tautan mati (lychee)** + hasil **pa11y/axe** (aksesibilitas) + ukuran halaman + gambar OG tampil benar. Untuk penawaran ke desa/pemda ini pembeda murah: *"situs Bapak/Ibu kami uji dulu, ini hasilnya."*
- ⚙️ **Bagi beban VPS vs PC user:** semua yang butuh **Chromium** (Unlighthouse, pa11y, axe via browser, Lighthouse CI lokal) itu berat → jalankan **sekali-jalan di PC user / CI GitHub**, bukan service menetap di VPS (RAM ketat). Yang cocok menetap/berulang di VPS: **lychee** (Rust, ringan) & **Pagefind** (index dibuat saat build).
- 🖼️ **Gambar OG otomatis = situs klien ber-"brand" saat dibagikan di WhatsApp/FB** (kanal utama desa). Pilihan hemat RAM: **Takumi** (tanpa browser). Untuk situs Next.js: **`next/og` bawaan** — tak perlu repo tambahan.
- ⚖️ **Lagi-lagi `spdx_id` menyesatkan:** **Satori & axe-core = MPL-2.0** (bukan MIT), **pa11y = LGPL-3.0**, **lychee & Takumi = MIT *ATAU* Apache-2.0 (file lisensinya DUA)**. MPL/LGPL aman dipakai & dijual, **tapi copyleft tingkat file**: kalau **file berlisensi MPL itu kita ubah**, perubahannya wajib dibuka.

---

## 🔗 SocialAgent / SalesAgent — Link-in-bio & Tombol Bagikan (kartu digital UMKM)

> Riset **2026-10-18** — rotasi topik: **social media, sudut yang belum ada: halaman 1-link & tombol bagikan**.
> Katalog sudah punya *penjadwal posting* (Postiz dkk) tapi **belum punya** yang paling sering diminta UMKM: **satu halaman berisi semua tautan** (WA, IG, TikTok, katalog, Maps) — produk mikro yang bisa dijual cepat sekaligus **pintu masuk** ke paket situs.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **LittleLink** | github.com/sethcottle/littlelink | **Template link-in-bio DIY** (HTML/CSS, 100+ tombol merek siap pakai) — "linktree tanpa server", tinggal diedit | HTML / CSS | ✅ **MIT** (`LICENSE.md`) | 3.097 (25) · **0 commit/60 hari** (push 2026-07) | SocialAgent + WebBuilder | ✅ **PAKAI (ambil desain/CSS-nya)** — jalur terbaik: **generate halaman statis Astro sendiri** bergaya LittleLink (nol server, nol AGPL) |
| **LittleLink-Server** | github.com/timothystewart6/littlelink-server | Versi **berjalan**: satu halaman tautan dikonfigurasi dari **environment variable** (tema, avatar, tombol, analytics, health-check) | Next.js / React / TS | ✅ **MIT** (`LICENSE.md`) | 1.154 (12) · 9 commit/60 hari · **compose = 1 container** (`little-link`) | SocialAgent + OpsAgent | ✅ **PAKAI** kalau klien mau ganti tautan sendiri **tanpa** deploy ulang — 1 container ringan |
| **LinkStack** | github.com/LinkStackOrg/LinkStack | **Aplikasi link-in-bio penuh** (mirip Linktree): akun, tema, statistik klik, admin UI | PHP (Laravel) + Docker | ⚠️ **AGPL-3.0** | 3.907 (**31**) · push 2026-10-04 · 441 fork | SocialAgent | ⚠️ **HATI-HATI** — paling lengkap, **tapi AGPL**: kalau kita host & **modifikasi** untuk banyak klien, pengguna jaringan berhak atas kode modifikasinya; butuh PHP + DB di VPS |
| **react-share** | github.com/nygardk/react-share | Tombol bagikan siap pakai untuk React (WA, FB, X, Telegram, email…) + hitungan share | React / TS | ✅ MIT | 2.818 (13) · push 2026-10-12 | WebBuilder + SocialAgent | ✅ PAKAI kalau situsnya Next.js/React |
| **sharer.js** | github.com/ellisonleao/sharer.js | Tombol bagikan **vanilla JS tanpa dependency** (atribut `data-` di HTML) — pas buat Astro | JS (repo 916 KB) | ✅ MIT | 2.096 (48) · push 2026-10-14 | WebBuilder + SocialAgent | ✅ **PAKAI** — paling pas buat situs Astro kita (tanpa framework) |
| **Shareon** | github.com/kytta/shareon | Tombol bagikan **tanpa pelacakan**, bundle <8 KiB, logo resmi | JS / CSS | ✅ MIT | 478 (**2**) | WebBuilder | 🔸 CADANGAN — "ethical & no tracking" nyambung narasi **PDP-ready**, tapi kecil/pemakaian pribadi |
| **BioDrop (dulu LinkFree)** | github.com/EddieHubCommunity/BioDrop | Dulu link-in-bio **paling populer** di GitHub (profil + proyek + event) | Next.js | ✅ MIT | 5.680 (13) | — | 🚫 **JANGAN PAKAI — `archived=true`** (push terakhir **2024-07-01**) walau ⭐ tertinggi di kategori ini |
| **Singlelink** | github.com/singlelink-co/Singlelink | Alternatif Linktree (mono-repo TS) | TypeScript | ⚠️ GPL-3.0 | 585 (11) · push **2023-03** | — | 🚫 SKIP — stale 3 tahun + GPL |

### 🔎 Catatan link-in-bio & bagikan
- 🌟 **Kategori ini bukti lagi: repo ber-⭐ TERTINGGI justru sudah mati.** **BioDrop/LinkFree 5.680⭐ (MIT) = ARCHIVED** → jangan direkomendasi walau namanya paling dikenal; **LittleLink 3.097⭐ = 0 commit/60 hari** → ambil desainnya saja, jangan harap fitur baru. Cek `.archived` + commit 60 hari sebelum rekomendasi.
- 💡 **Cara paling hemat buat klien UMKM: halaman link-in-bio STATIS milik kita** (Astro 1 halaman, data per klien dari JSON) bergaya **LittleLink (MIT)** → nol server, nol AGPL, dan bisa jadi **pintu masuk**: link-in-bio murah → upsell situs + katalog + order WhatsApp. Pakai **LittleLink-Server (MIT, 1 container)** hanya kalau klien wajib bisa ubah tautan sendiri.
- ⚖️ **LinkStack = AGPL-3.0 → pikir dua kali jadi layanan ber-merek kita.** AGPL = copyleft untuk pemakaian **lewat jaringan**: kalau kita modifikasi & host untuk banyak klien, kode modifikasi wajib bisa diakses pengguna. Kalau tetap mau: pakai **apa adanya** (tanpa modifikasi) atau taruh di server klien.
- 📲 **Yang benar-benar dipakai warga/UMKM bukan tombol "bagikan ke X/Twitter", tapi WhatsApp.** Urutan pasang: (1) **WhatsApp** + (2) salin tautan, baru (3) IG/FB. Astro → **sharer.js (MIT)**; Next.js → **react-share (MIT)**.
- 🔍 **Query tajam:** **`linktree alternative in:name,description`** jauh lebih berguna daripada **`link in bio`** (yang terakhir isinya proyek pribadi kecil semua). Buat tombol bagikan: `social share buttons in:name,description` (`social share` saja = plugin WordPress).

---

## 🔀 OpsAgent / RepoScout — LLM Gateway: SATU PINTU ke banyak provider + failover

> Riset **2026-10-19** — rotasi topik: **agentic AI, sudut baru: infrastruktur LLM (gateway/failover)**.
> **Alasan langsung (bukan teoretis):** fallback provider Hermes kita berulang kali rusak — 15 Okt fallback **401** → semua cron gagal; 17 Okt OmoApicall **502**; 18 Okt **401 kunci dicabut**. Katalog sudah punya *proxy AI-native* (`Plano`) & *observability* (`Langfuse/Opik/Logfire`), **tapi belum punya gateway LLM** yang jadi **satu pintu failover + budget + kunci** — yang bisa melayani Hermes **dan** tool/agen lain sekaligus.
> Semua lisensi dibaca dari **file lisensi asli** dan dicek **rekursif** (bukan cuma root).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **LiteLLM** | github.com/BerriAI/litellm | **AI gateway OpenAI-compatible**: satu URL → 100+ provider; **Router retry + fallback antar-deployment**, load balancing, **virtual keys**, **spend tracking per user/proyek**, guardrails, admin UI, callback ke Langfuse/MLflow — dipakai sebagai **SDK Python** atau **server** | Python (SDK + Proxy Server) / Docker | ✅ **MIT** (inti) ⚠️ `enterprise/` = **BerriAI Enterprise License** (komersial; boleh dipakai untuk dev/testing, **produksi butuh langganan**) | 61.504 (**240**) · 100 commit/60d · 100+ kontributor · push 2026-10-18 | OpsAgent | ✅ **REKOMENDASI** — obat langsung masalah fallback kita; ⚠️ `docker-compose.yml` = `litellm` + `db`(Postgres) + `prometheus` (**db & prometheus opsional**); repo **2,5 GB** → jangan full clone |
| **Bifrost** | github.com/maximhq/bifrost | Gateway high-performance: 23+ provider, **automatic failover**, load balancing, semantic caching, **MCP gateway**; satu binary Go / `npx` / Docker | Go | ✅ **Apache-2.0** (`LICENSE`) + `THIRD_PARTY_NOTICES.md` | 8.916 (**35**) · 100 commit/60d · created 2025-03 | OpsAgent | ⚠️ PELAJARI — paling ringan & cepat, tapi rasio ⭐:watchers **255:1** (muda/hype) → uji dulu sebelum jadi satu-satunya pintu |
| **AxonHub** | github.com/looplj/axonhub | Gateway AI all-in-one (Go): "SDK apa pun, model apa pun", **failover bawaan**, log | Go / Docker | ✅ Apache-2.0 (`LICENSE` + `NOTICE`) | 5.367 (**13**) · 100 commit/60d | OpsAgent | ⚠️ CADANGAN — komunitas kecil (subs 13) |
| **Portkey Gateway** | github.com/Portkey-AI/gateway | AI gateway + guardrail, rute ke 1.600+ LLM | TypeScript | ✅ Apache-2.0 | 13.214 · push **2026-05-25** | OpsAgent | ⚠️ CADANGAN — **melambat ±5 bulan** |
| **new-api** | github.com/QuantumNous/new-api | "AI model hub" **multi-tenant**: agregasi & distribusi model + billing | Go | ⚠️ **AGPL-3.0** (`LICENSE` + `NOTICE` + `THIRD-PARTY-LICENSES.md`) | 50.174 (**166**) | OpsAgent | ⚠️ HATI-HATI — AGPL **menyala** kalau kita host untuk banyak klien |
| **Manifest LLM Gateway** | github.com/mnfst/llm-gateway | Gateway + observability untuk agen ("AI agents that don't break") | TypeScript | ✅ MIT (© MNFST, Inc 2026) | 7.589 (**29**) | OpsAgent | 🔸 CADANGAN |
| **RTK** (rust token killer) | github.com/rtk-ai/rtk | Kompresi output bash & trafik API biar agen hemat token (klaim 60–90%) | Rust | ⚠️ **root `LICENSE` = Apache-2.0, TAPI `engine/LICENSE` & `proxy/LICENSE` = BUSL-1.1** | 83.864 (**218**) · push 2026-10-17 · created 2026-01 | OpsAgent | 🚫 **BUKAN fondasi** — jebakan lisensi ke-11: bagian yang berguna (mesin kompresi) **BUSL-1.1**; pakai **Headroom (Apache-2.0)** yang sudah ada di katalog |

### 🔌 Tier "lokal" (fallback offline) — semua ✅ MIT, tapi bukan buat VPS kita
| Repo | ⭐ (subs) | Catatan |
|---|---|---|
| github.com/ollama/ollama | 183.741 (**1.020**) · MIT | Server model lokal paling gampang — **cocok di PC user (Windows)**, bukan VPS |
| github.com/ggml-org/llama.cpp | 131.625 (**868**) · MIT | Mesin inference C/C++ (fondasi banyak alat); bisa CPU-only |
| github.com/mudler/LocalAI | 49.621 (**299**) · MIT | OpenAI-compatible lokal (LLM/vision/voice/image) |
| github.com/mostlygeek/llama-swap | 6.009 (**24**) · MIT | **Tukar model otomatis** di server lokal OpenAI-compatible |

### 🔎 Catatan LLM gateway (kenapa ini penting sekarang)
- 🚑 **Masalah nyata tim kita bukan "kurang model", tapi "satu provider mati = semua cron mati".** Gateway (LiteLLM/Bifrost) memindahkan logika retry/fallback **keluar dari tiap aplikasi** → Hermes, skrip, dan agen lain cukup menunjuk **satu `base_url`**; ganti provider = ubah 1 config, bukan 6 tempat.
- 💾 **Hitung RAM dulu (pelajaran lama masih berlaku).** `LiteLLM` = proses Python (ratusan MB) + Postgres opsional; `Bifrost`/`AxonHub` (Go) jauh lebih ringan. VPS kita saat riset: **RAM 1.930 MB, available cuma 307 MB** → jalankan **tanpa Prometheus & tanpa Postgres** dulu (budget in-memory), atau tunggu **VPS khusus**.
- 🧊 **Jangan tergoda "LLM sendiri di VPS 2 GB"**: semua mesin lokal (ollama/llama.cpp/LocalAI) MIT, tapi model terkecil pun butuh RAM yang **tidak** kita punya (available 307 MB) → taruh di **PC user** kalau mau offline.
- 🧾 **Jebakan lisensi ke-11: SATU repo bisa punya BEBERAPA file lisensi di FOLDER berbeda.** `rtk-ai/rtk` lolos teliti kalau cuma baca root: API bilang **Apache-2.0**, root `LICENSE` = Apache-2.0 penuh — **padahal** `engine/LICENSE` & `proxy/LICENSE` = **BUSL-1.1** (gratis untuk produksi, **tapi dilarang** menawarkan RTK/turunannya ke pihak ketiga sebagai produk/jasa komersial). **Cara deteksi: `git/trees/<branch>?recursive=1 | grep -iE "LICEN|COPYING|TERMS"` — REKURSIF, bukan root saja** (di rtk muncul 3 file: root, `engine/`, `proxy/`).

---

## 📅 WebBuilder / SalesAgent — Booking & Jadwal (layanan desa & UMKM)

> Riset **2026-10-19** — rotasi topik kedua: **web dev, sudut baru: pemesanan/jadwal (booking)**.
> **Kebutuhan nyata:** layanan desa (antre surat/posyandu/konsultasi) & UMKM (salon, bengkel, klinik, rental, kafe) hampir selalu butuh **"pilih tanggal & jam"**. Katalog sudah punya formulir & analitik, **belum punya mesin jadwal**.
> Bonus temuan: **koreksi penting** — repo `calcom/cal.com` sudah **ganti nama & ganti lisensi** (lihat catatan 🚨).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Cal.diy** (Cal.com Community Edition) | github.com/calcom/cal.diy *(dulu `calcom/cal.com`)* | Infrastruktur penjadwalan paling lengkap: tipe event, ketersediaan, kalender, embed, API | Next.js / tRPC / Prisma / TS | ✅ **MIT 100%** — tanpa EE, **tanpa license key** | 49.138 (**222**) · 16 commit/60d · 15.371 fork · repo **1,1 GB** | WebBuilder | ⚠️ PELAJARI — lisensi paling bersih, **tapi** README-nya sendiri: *"strictly recommended for personal, non-production use"* + compose = **5 service** (`database`, `redis`, `calcom`, `calcom-api`, `studio`) → **bukan** untuk VPS 1,9 GB |
| **Easy!Appointments** | github.com/alextselegidis/easyappointments | Penjadwalan janji temu self-hosted: layanan, penyedia, jam kerja, notifikasi email, embed | PHP 8 + MySQL | ⚠️ **GPL-3.0** | 4.444 (**153**) · 1.577 fork · push 2026-10-16 | WebBuilder + SalesAgent | ✅ **REKOMENDASI buat VPS kita** — minimal **3 container** (`php-fpm` + `nginx` + `mysql`; compose dev menambah phpmyadmin/mailpit/baikal/openldap/swagger) → ringan & mapan (sejak 2014). GPL: **jual jasa OK**, jangan tanam kodenya ke produk tertutup |
| **Rallly** | github.com/lukevella/rallly | Penjadwalan **gaya polling** (Doodle): ajukan tanggal → peserta pilih → hasil | Next.js + Postgres | ⚠️ **AGPL-3.0** | 5.310 (**30**) · push 2026-10-18 · compose: `rallly_db` + `rallly_selfhosted` → **2 service** | SocialAgent | ✅ PAKAI (internal/koordinasi) — paling ringan; pas buat **rapat tim & koordinasi desa**; AGPL → jangan jadi layanan ber-brand kita |
| **Thunderbird Appointment** | github.com/thunderbird/appointment | Penjadwalan janji (undang orang memilih slot) — dari tim Mozilla/Thunderbird | Python | ⚠️ MPL-2.0 | 555 (**13**) · push 2026-10-16 | WebBuilder | 🔸 CADANGAN — organisasi besar, MPL = copyleft per-file |
| **Calnode** | github.com/Calnode/calnode | Alternatif Calendly **1 binary Go + SQLite**, API-first | Go | ✅ Apache-2.0 | 119 (**0**) · created 2026-06 · push 2026-10-18 | OpsAgent | ⚠️ UJI DULU — paling ringan & lisensi bersih, tapi komunitas **nol** |
| **Calrs** | github.com/olivierlambert/calrs | Penjadwalan self-host cepat — "seperti Cal.com, tapi Rust" | Rust | ⚠️ AGPL-3.0 | 319 (**4**) · created 2026-03 | OpsAgent | ⚠️ PANTAU — muda |
| **Someday** | github.com/rbbydotdev/someday | Pemilih ketersediaan (Calendly alternative) jalan di **Google Apps Script** → gratis di akun Google | GAS + React/TS | ✅ MIT (`LICENSE.md`; ⚠️ teksnya masih template `[year] [fullname]`) | 1.064 (**1**) · push 2026-07 | WebBuilder | 🔸 CADANGAN — nol server, tapi terikat ekosistem Google |
| **CloudMeet** | github.com/dennisklappe/CloudMeet | Calendly alternative di **Cloudflare free tier** (edge) | TS / Cloudflare | ✅ MIT | 549 (**1**) · push 2026-07 | WebBuilder | 🔸 CADANGAN — subs 1 + 3 bulan tanpa update |
| **django-appointment** | github.com/adamspd/django-appointment | App Django: manajemen jadwal/janji temu | Python / Django | ✅ Apache-2.0 | 281 (**2**) · push 2026-10-13 | WebBuilder | 🔸 CADANGAN — bahan kalau kita bikin modul jadwal sendiri |
| **openresto** | github.com/karanshukla/openresto | Booking meja restoran/kafe self-hosted | — | ✅ MIT | 98 (**1**) | SalesAgent | 🔸 niche (referensi) |

### 🚨 Koreksi katalog (WAJIB dicatat)
- **`calcom/cal.com` → `calcom/cal.diy`, dan lisensinya BERUBAH: AGPL-3.0 → MIT.** Repo lama (di catatan desain kita dulu disebut AGPL + punya `ee/`) sekarang **tidak punya folder `ee/` sama sekali**; file `LICENSE` = MIT; README: *"Cal.diy is the community-driven, fully open-source scheduling platform — a fork of Cal.com with all enterprise/commercial code removed… **100% MIT-licensed with no proprietary Enterprise Edition features**"*. Fitur EE (Teams, Organizations, Insights, Workflows, SSO/SAML) dibuang; yang komersial tetap di Cal.com. **Deteksi:** `gh api repos/calcom/cal.com` membalas `full_name = calcom/cal.diy` (rename, bukan repo baru).
- **`cosscom/coss` (design system Cal.com) juga berubah.** Entri lama kita (10.677⭐, AGPL-3.0) kini **salah URL**: `cosscom/coss` sekarang ⭐**3** (repo kosong/dipakai ulang), yang benar = **`github.com/cosscom/ui`** (10.720⭐, subs 33, **AGPL-3.0**, push 2026-10-18).

### 🔎 Catatan booking/scheduling
- 🔍 **Query `booking`/`scheduling` = BERISIK** (hotel, penerbangan, Gantt chart, Kubernetes scheduler). Yang tajam: **`calendly alternative in:name,description`**, **`appointment+scheduling+in:name,description`**, atau **nama proyek langsung** (`easyappointments`, `rallly`, `cal.com`). `self-hosted+booking+system` hanya menghasilkan proyek <100⭐.
- 💾 **Urutan dari paling ringan buat VPS kita:** **Rallly 2 service** → **Easy!Appointments 3 container (LAMP)** → Calnode 1 binary (komunitas 0) → **Cal.diy 5 service (berat)**. Jangan pasang Cal.diy di VPS 1,9 GB.
- ⚖️ **Lisensi kategori ini "campur":** Cal.diy = **MIT**, Easy!Appointments = **GPL-3.0**, Rallly/Calrs = **AGPL-3.0**, Thunderbird = **MPL-2.0**, Calnode/Someday/CloudMeet/django-appointment = **MIT/Apache**. Aturan tetap: MIT/Apache = bebas; **AGPL menyala saat kita host untuk banyak klien**; GPL = jual jasa boleh, salin kode ke produk tertutup jangan.
- 📄 **Kalimat README "for personal, non-production use" BUKAN batasan lisensi.** Cal.diy tetap **MIT** (boleh dipakai komersial secara hukum) — yang kita catat adalah **risiko kualitas/dukungan**, bukan larangan. Jangan campur "imbauan README" dengan "syarat LICENSE" (beda dengan kasus Dify/Open WebUI yang memang menaruh syarat **di dalam** lisensi).
- 🎯 **Buat Webuild:** kalau klien cuma butuh "pilih jadwal", **paling murah = halaman jadwal statis (Astro) + konfirmasi via WhatsApp/WAHA** — tanpa service tambahan di VPS. Naik ke **Easy!Appointments** kalau butuh multi-penyedia + notifikasi email; **Cal.diy** baru masuk hitungan setelah punya VPS khusus web.

---

## 🎙️ VoiceAgent / RepoScout — Suara Bahasa Indonesia TANPA GPU (pengumuman desa, audio WA, voice-over)

> Riset **2026-10-20** — rotasi topik: **TTS/voice**, sudut yang belum ada: katalog punya mesin suara **butuh GPU + cuma EN/ZH** (voice cloning, studio), **belum punya jalur "suara Indonesia, jalan di CPU, gratis"**.
> **Kebutuhan nyata:** (1) **voice-over Bahasa Indonesia** buat video promosi desa/UMKM tanpa bayar ElevenLabs, (2) **audio pengumuman** yang bisa dibroadcast ke WA grup warga, (3) **"mode baca"** di situs desa (aksesibilitas untuk warga lansia / rendah literasi).
> Semua angka & lisensi diverifikasi hari ini via `gh api` + **file lisensi asli** + `curl` ke HuggingFace. **Suara Indonesia gratis diverifikasi dengan menjalankan `edge-tts --list-voices | grep id-ID`** (bukan asumsi).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **sherpa-onnx** | github.com/k2-fsa/sherpa-onnx | Runtime **CPU-only tanpa GPU**: STT + **TTS** + diarisasi + pemisahan suara; menjalankan model VITS/**piper** (termasuk suara **Indonesia** `csukuangfj/vits-piper-id_ID-news_tts-medium` di HF) | C++ (+ binding Python/JS/Swift/Android) | ✅ **Apache-2.0** (`LICENSE`) | 15.383 (**123**) · **66 commit/60d** · 100 kontributor · push 2026-10-17 | VoiceAgent + OpsAgent | ✅ **REKOMENDASI** — inilah "mesin suara offline" buat kita: **pengganti resmi piper** (repo `rhasspy/piper` **ARCHIVED**, 11.301⭐) & jalan di CPU |
| **Kokoro-FastAPI** | github.com/remsky/Kokoro-FastAPI | Server **OpenAI-compatible `/v1/audio/speech`** untuk TTS: `docker run -p 8880:8880 ghcr.io/remsky/kokoro-fastapi-cpu:latest` (**1 container, CPU**) — bisa dicolok jadi provider TTS custom Hermes | Python / FastAPI / Docker | ✅ **Apache-2.0** (`LICENSE`) | 5.560 (**36**) · **60 commit/60d** · 53 kontributor · push 2026-10-14 | VoiceAgent + OpsAgent | ✅ **PAKAI** — paling praktis buat voice-over konten; ⚠️ **suara Kokoro = en/es/fr/hi/it/ja/pt/zh → TIDAK ada Bahasa Indonesia** (buat desa pakai jalur lain di bawah) |
| **edge-tts** | github.com/rany2/edge-tts | TTS **gratis** lewat layanan Edge Microsoft (tanpa API key) — **2 suara Indonesia terverifikasi**: `id-ID-ArdiNeural` (pria) & `id-ID-GadisNeural` (wanita) + `ms-MY-OsmanNeural`/`Yasmin` | Python (CLI + library) | ⚠️ **LGPL-3.0** | 12.330 (?) · 8 commit/60d · 22 kontributor | VoiceAgent + SocialAgent | ✅ **PAKAI (jalur tercepat hari ini)** — voice-over Indonesia & audio pengumuman WA **sekarang juga**; ⚠️ **butuh internet** (bukan offline) → jangan jadi satu-satunya jalur |
| **ArboTTS** | github.com/ARBO-TEAM/arboTTS | TTS **bilingual Indonesia + Inggris** super ringan: VITS/Kokoro/**Piperlite INT8** (1,55 MB buat ESP32), **inference CPU (klaim RTF 0,025x)**, **API REST kompatibel OpenAI**, demo **WASM jalan di browser (nol server)** | Python / ONNX / WASM | ✅ **MIT** (`LICENSE`, © ARBO-TEAM 2026) | **3** (**0**) · 34 commit/60d · **1 kontributor** · dibuat **2026-10-12** | VoiceAgent | ⚠️ **UJI DULU** — paling pas secara fitur (Indonesia + CPU + browser), **tapi** repo umur 8 hari, ⭐ 3, tim 1 orang, klaim besar → verifikasi kualitas audio dulu sebelum masuk produk klien |
| **kokoro-onnx** | github.com/thewh1teagle/kokoro-onnx | Kokoro-82M via **ONNX Runtime** (CPU) — TTS ringan tanpa PyTorch | Python / ONNX | ✅ **MIT** | 2.792 (18) · **1 commit/60d** · push 2026-09-01 | VoiceAgent | 🔸 CADANGAN — nyaris statis; pakai **Kokoro-FastAPI** kalau mau server |
| **hexgrad/kokoro** (model) | github.com/hexgrad/kokoro | Sumber model **Kokoro-82M** (bobot di HF: **apache-2.0** ✅) — kualitas terbaik di kelasnya (82 juta parameter) | JS/ONNX/model | ✅ Apache-2.0 (kode & bobot) | 9.494 (71) · **0 commit/60d** · push **2025-08-06** | VoiceAgent | ⚠️ **STAGNAN** (14 bulan tanpa commit) & **tanpa suara Indonesia** → pakai bobotnya saja, jangan harap fitur baru |

### 🇮🇩 Suara Indonesia offline (model, bukan kode) — cek lisensinya satu-satu
| Model (HuggingFace) | Catatan | Lisensi |
|---|---|---|
| `rhasspy/piper-voices/id/id_ID/news_tts/medium` | Satu-satunya suara piper Bahasa Indonesia (22,05 kHz, 1 pembicara) — jalan via **sherpa-onnx** | ⚠️ **TIDAK JELAS** — `MODEL_CARD` cuma bilang *"Dataset License: See URL"* (korpus Kaggle Indic TTS) |
| `csukuangfj/vits-piper-id_ID-news_tts-medium` | Salinan siap-pakai untuk sherpa-onnx (dikelola maintainer sherpa-onnx) | ⚠️ sama (turunan voice di atas) |
| `grandhigh/Chatterbox-TTS-Indonesian` | Finetune Chatterbox → Indonesia (±0,5B) — kualitas bagus | ⚠️ perlu **GPU/berat di CPU**; lisensi model harus dibaca di HF |
| `alkhrzmy/qwen3-tts-0.6b-indonesian` · `Wikidepia/indonesian-tts` | Finetune Qwen3-TTS 0,6B & Coqui lama (2022) | ⚠️ bobot besar (CPU lambat) / **Wikidepia = tanpa lisensi** → jangan dipakai komersial |

### 🔎 Catatan voice/TTS Indonesia (kenapa ini penting buat Webuild)
- 🎯 **Urutan paling realistis buat kita (VPS tanpa GPU, RAM ketat):** **edge-tts (id-ID-Ardi/Gadis, gratis, online)** buat mulai hari ini → **sherpa-onnx + voice id_ID** kalau butuh offline & stabil → **Kokoro-FastAPI** buat voice-over bahasa Inggris/pasar luar → **ArboTTS** tinggal diuji (dia satu-satunya yang janji "Indonesia + browser + CPU").
- 🖥️ **"Mode baca" situs desa = fitur murah yang langsung jadi bahan jualan:** tombol 🔊 di tiap artikel/kabar desa. Dua jalur: **(a) Web Speech API bawaan browser** (suara id-ID dari Android/iOS — nol kode baru, nol biaya) atau **(b) audio MP3 yang kita prasetel** pakai edge-tts/sherpa-onnx (kualitas konsisten, bisa diputar berkali-kali, hemat kuota warga). Untuk desa, (b) lebih tahan banting karena **Android murah sering tak punya suara id-ID terpasang**.
- 📻 **Audio pengumuman → WA grup warga** = paket "pengumuman suara" (MP3 dari edge-tts) yang bisa jadi layanan mikro tambahan untuk paket desa; sekalian jalan pintas buat warga yang malas baca teks panjang.
- ⚖️ **Jebakan lisensi ke-12 (baru): "SDK/model RESMI" ≠ berlisensi, dan MODEL SUARA punya lisensi PER-SUARA.** `xendit/xendit-node` (SDK resmi Xendit) **tak punya file LICENSE sama sekali**, sementara `xendit-php/go/python` = **MIT** — jadi satu keluarga SDK pun bisa beda. Untuk suara: lisensi **bukan** di repo piper, tapi di file **`MODEL_CARD` tiap voice** (piper id_ID = *"See URL"* / tidak jelas). **Kokoro = Apache-2.0 termasuk bobotnya** (aman) — tapi tak ada suara Indonesia.
- 🔍 **Query tajam kategori ini:** `text-to-speech in:name,description stars:>1500 pushed:>2025-06-01` (yang muncul: Handy, DeepSpeech, index-tts, sherpa-onnx…) · **`kokoro tts`** · untuk Indonesia **nama bahasa Indonesia jauh lebih berguna daripada kata umum**: `tts indonesian in:name,description` & `indonesian speech` (yang muncul malah dataset deteksi ujaran kebencian → saring manual). Cari **model** di HuggingFace, bukan GitHub (query `https://huggingface.co/api/models?search=indonesian%20tts`).
- 💡 **Keaktifan ≠ ⭐, lagi-lagi:** `hexgrad/kokoro` 9.494⭐ tapi **0 commit/60 hari**, `kokoro-onnx` 1 commit/60d, sementara `Kokoro-FastAPI` (⭐ lebih kecil) **60 commit/60d** → yang dipilih **Kokoro-FastAPI**.

---

## 💳 WebBuilder / SalesAgent — Checkout UMKM Indonesia: QRIS & pembayaran (tanpa biaya gateway)

> Riset **2026-10-20** — rotasi topik kedua: **web dev**, sudut yang belum ada: katalog punya *mesin toko* (Medusa/Saleor/openumkm) & *katalog statis + checkout WhatsApp*, **belum punya bagian yang paling ditanya UMKM: "uangnya masuk bagaimana?"**
> **Kebutuhan nyata:** untuk penjual kecil (warung, katering, olshop rumahan) **jangan** pasang gateway berbunga di VPS kecil — cukup **checkout WhatsApp + QRIS**. Yang dicari: library **QRIS statis → dinamis** (nominal otomatis) + SDK gateway resmi kalau klien naik kelas.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **QRIS Dinamis** | github.com/verssache/qris-dinamis | **Parse / validasi / generate QRIS**: ubah QRIS **statis merchant → dinamis** (nominal + biaya otomatis, NMID tetap) + CLI & API | TypeScript (Vite/React) | ✅ **MIT** (`LICENSE`, © 2020 QRIS Dinamis) | 521 (**1**) · **0 commit/60d** · 1 kontributor · push 2026-04-01 | WebBuilder + SalesAgent | ✅ **PAKAI (referensi utama)** — kode kecil & stabil, persis kebutuhan "warung punya QRIS sendiri"; ⚠️ tak dirawat 6 bulan & subs 1 → **salin logikanya**, jangan berharap fitur baru |
| **qris-static-dynamic-core** | github.com/nurafandito/qris-static-dynamic-core | Inti konversi QRIS statis→dinamis (parser, validator, converter) + 4 fork | TypeScript | ✅ **MIT** (`LICENSE`, © 2026 Nur Afandi) | 44 (**0**) · 1 commit/60d · push 2026-09-15 · repo **21 KB** | WebBuilder | ✅ **PAKAI** — alternatif lebih segar dari `qris-dinamis`, kode ringan (21 KB) buat dipelajari |
| **Midtrans SDK resmi** | github.com/Midtrans/midtrans-nodejs-client | SDK resmi Midtrans untuk **Node/Next.js** (Snap, QRIS, VA, e-wallet) — 422⭐ versi PHP, 142⭐ versi Go juga ada | JS/TS (juga PHP/Go) | ✅ **MIT** (`midtrans-nodejs-client`, `midtrans-php`, `midtrans-go`) | Node **220** (11) · **0 commit/60d** (push 2025-06) · PHP 422⭐ (push 2025-03) | WebBuilder + SalesAgent | ✅ **PAKAI** kalau klien mau gateway sungguhan — API stabil walau SDK melambat 16–19 bulan (⚠️ perhatikan update dependency) |
| **Xendit SDK resmi** | github.com/xendit/xendit-node | SDK resmi Xendit (Invoice, QRIS, VA, disbursement) untuk Node | TypeScript (juga PHP/Go/Python) | ⚠️ **xendit-node = TIDAK ADA file lisensi** (php/go/python = **MIT**) | Node 150 (21) · push 2025-10-01 | WebBuilder | ⚠️ **HATI-HATI** — repo resmi tapi **tanpa lisensi = all rights reserved**; untuk produksi klien pakai **jalur PHP/Go/Python (MIT)** atau **panggil REST API langsung** |
| **pakasir-sdk** | github.com/zeative/pakasir-sdk | Klien API **Pakasir** (gateway lokal ringan, fee kecil, QRIS) | Go | ✅ **MIT** | 24 (3) · push 2026-09-29 | SalesAgent | 🔸 CADANGAN — pihak ketiga tak resmi; cocok buat jualan kecil (digital/UMKM) |
| **ongkir-sdk** | github.com/cakfan/ongkir-sdk | SDK multi-penyedia **ongkos kirim Indonesia** (Biteship, Komship) | TypeScript | ✅ **MIT** | 3 (**0**) · push 2026-08-04 | WebBuilder | 🔸 CADANGAN — kecil/unofficial; kalau butuh: **panggil API RajaOngkir/Biteship langsung** dari Astro API route |
| **go-payment** | github.com/imrenagi/go-payment | Konektor pembayaran Midtrans + Xendit (Go) | Go | ✅ MIT | 406 (7) · push **2023-07** | — | 🚫 **USANG** (3 tahun) — pakai SDK resmi langsung |
| **rajaongkir (kavist)** | github.com/kavist/rajaongkir | Klien API RajaOngkir (PHP) | PHP | ✅ MIT | 131 (3) · push **2022-03** | — | 🚫 **USANG** — referensi saja |
| **gopay/goBiz mutation scrapers** | github.com/ahmadzakiyox/gopay-api-gateaway · github.com/rzkyyds/gobiz-payment-v2 | "Gateway" yang memantau **mutasi GoPay/GoBiz** (auto-konfirmasi pembayaran) | JS/TS | GoPay = tanpa lisensi · gobiz-v2 = MIT | 240 (?) · 34 | — | 🚫 **JANGAN** — menyalahi ToS GoPay/GoBiz & **risiko akun klien diblokir**; ini yang paling ditakutkan merchant |

### 🚨 Yang populer TAPI **tanpa lisensi** (jangan dipakai di produk klien)
| Repo | ⭐ | Masalah |
|---|---|---|
| github.com/idlanyor/qris-api | 78 | `license = NONE` (tidak ada file lisensi) — = *all rights reserved* |
| github.com/Adytm404/qris-dinamis-generator | 65 | tanpa lisensi, push Juli 2025 (web tool) |
| github.com/mmenghancurkan/dynaQRIS | 50 | tanpa lisensi (Python) |
| github.com/Wimboro/qris | 35 | tanpa lisensi |

### 🔎 Catatan checkout UMKM (penting & jujur)
- ✅ **Pola paling hemat buat penjual kecil (nol biaya bulanan):** situs/katalog statis → tombol **"Pesan via WhatsApp"** (pesan otomatis berisi barang+jumlah) → pembeli **scan QRIS** merchant. Kalau merchant sudah punya **QRIS statis**, kita bisa bikin **QRIS dinamis** dengan `qris-dinamis`/`qris-static-dynamic-core` (**MIT**) supaya nominal & pesanan tercatat otomatis — **tanpa MDR tambahan, tanpa daftar merchant baru**.
- ⚖️ **Kejujuran soal legalitas QRIS statis→dinamis:** sampai riset ini **tidak ada aturan Bank Indonesia yang secara eksplisit melarang atau mengizinkan** konversi QRIS statis→dinamis oleh pihak ketiga (yang berubah hanya tag 01/54/63; **NMID merchant tidak diubah** sehingga dana tetap masuk ke rekening merchant yang sama). Karena itu **jangan kita klaim "legal"**: tulis di kontrak/penawaran bahwa **merchant wajib mengonfirmasi ke akuirer/PJSP & bank-nya**; kalau bank melarang → pakai jalur gateway. Yang **jelas dilarang/haram**: meng-*scrape* mutasi GoPay/GoBiz akun klien (blokir akun + ToS).
- 🪜 **Tangga eskalasi pembayaran (dari murah ke mahal):** (1) **transfer/QRIS manual + konfirmasi WA** [nol kode, nol biaya] → (2) **QRIS dinamis otomatis** (`qris-dinamis` MIT) [nol biaya bulanan, ada catatan pesanan] → (3) **Pakasir** (gateway fee kecil, pihak ketiga) → (4) **Midtrans/Xendit SDK resmi** [klien serius: invoice, VA, e-wallet, refund otomatis] → (5) mesin toko penuh (**Medusa MIT**) hanya kalau butuh stok/varian/multi-penjual.
- 🧾 **Ini menjawab utang keputusan `t_2af5e946` (segmen toko UMKM, `ready` sejak 15 Okt):** untuk **mulai jualan sekarang** cukuplah (1)+(2) — **tidak butuh VPS khusus web & tidak butuh keputusan Xendit dulu**; Xendit/Midtrans ditunda sampai ada klien yang benar-benar minta checkout otomatis.
- 🔍 **Query tajam kategori ini:** **`qris in:name,description`** (+ filter `license:mit` atau cek file lisensi!), **`midtrans in:name,description`**, **`xendit in:name,description`**, `payment gateway indonesia` (hasilnya kecil-kecil & sebagian tanpa lisensi). ⚠️ Kata **`qris`** juga menarik **`qrisp`** (pemrograman kuantum), **`qri-io`** (data tooling), dan `rajaongkir` menarik proyek PHP lama → saring manual. **`rajaongkir`/`ongkir` = semua usang (2022–2023)** → untuk ongkir, panggil API langsung.

---

## 🔎 WebBuilder / ContentWriter / SalesAgent — SEO & Keterlihatan (Google + AI search/GEO) buat situs desa & UMKM

> Riset **2026-10-21** — rotasi topik: **web dev**, sudut yang belum ada: katalog punya "mutu situs" (performa, aksesibilitas, pencarian Pagefind, pratinjau sosial) & analitik, **belum punya SEO / keterlihatan** — padahal pertanyaan pertama calon klien desa: *"situsnya bisa muncul di Google nggak? kok warga masih nanya di WA?"*
> Sudut baru kedua: **GEO (Generative Engine Optimization)** — biar desa/UMKM **dikutip AI search** (ChatGPT/Perplexity/Gemini), bukan cuma diindeks Google. Belum ada pesaing lokal yang menawarkan ini.
> Semua ⭐/subs/lisensi diverifikasi via `gh api` + **baca file lisensi asli** (`curl raw.githubusercontent`), keaktifan = **commit 60 hari + kontributor**.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **OpenSEO** | github.com/every-app/open-seo | Alternatif open-source **Semrush/Ahrefs**: riset kata kunci, rank tracking, backlink, audit situs, **AI visibility**; punya **MCP server + agent skills** (README menyebut **Claude Code, OpenClaw, Hermes**) | TypeScript / Docker | ✅ **MIT** (`LICENSE`, © 2026 Ben Senescu) | 24.309 (**74**) · **100 commit/60d** · 20 kontributor · 3.274 fork · push 2026-10-20 · repo 30,7 MB | WebBuilder + ContentWriter + RepoScout | ✅ **PAKAI (internal)** — **1 container** (`compose.yaml` → `ghcr.io/every-app/open-seo:latest`, port `127.0.0.1:3001`); ⚠️ **wajib `DATAFORSEO_API_KEY` (API BERBAYAR pay-as-you-go)** = kode MIT **tapi datanya tidak gratis**; hosted resmi $10/bln → jangan bilang "gratis" ke klien |
| **Claude SEO** | github.com/AgriciDaniel/claude-seo | **Skill SEO paling lengkap**: 26 sub-skill + 19 sub-agen paralel — technical SEO, E-E-A-T, **Schema.org**, GEO/AI search, local SEO, e-commerce, i18n; tiap audit keluar **rencana aksi berprioritas + skor 0–100** | Python (Claude Code skill) | ✅ **MIT** (root **dan** tiap `skills/*/LICENSE.txt` + `extensions/*/LICENSE.txt` = MIT) | 19.469 (**163**) · **100 commit/60d** · 30 kontributor · push 2026-10-04 · repo 7,5 MB | ContentWriter + SalesAgent + RepoScout | ✅ **PELAJARI/ADAPTASI** — persis kebutuhan "kartu mutu situs" kita; ⚠️ format Claude Code (`~/.claude/skills/`, perintah `/seo`) → **perlu porting** ke skill Hermes |
| **geo-seo-claude** | github.com/zubair-trabzada/geo-seo-claude | Skill **GEO-first** (AI search optimization): biar situs **dikutip model AI** (ChatGPT/Perplexity/Gemini) — citability, entitas, kutipan sumber | Python (Claude Code skill) | ✅ **MIT** (`LICENSE`, © 2026 Zubair Trabzada) | 11.128 (**80**) · **60 commit/60d** · 25 kontributor · push 2026-10-20 · repo **353 KB** | ContentWriter + RepoScout | ✅ **PAKAI** (pelengkap) — teringan & paling khusus; tetap perlu porting skill |
| **llms.txt** | github.com/AnswerDotAI/llms-txt | Proposal file **`/llms.txt`** di root situs supaya **LLM paham isi situs** (peta konten versi ringkas buat model AI) — spec + notebook + contoh | Jupyter Notebook / Markdown | ✅ **Apache-2.0** | 2.665 (**42**) · push 2026-09-24 | WebBuilder + ContentWriter | ✅ **PAKAI** — pasang `llms.txt` di situs desa = **5 menit, nol biaya**, langsung jadi nilai jual "situs yang siap AI search" |
| **astro-paper v6.1.0** | github.com/satnaing/astro-paper | Starter **blog markdown** minimal, aksesibel & SEO-friendly (kabar desa, artikel UMKM) | **Astro 7 + Tailwind 4** | ✅ **MIT** | 5.138 (**24**) · push 2026-10-18 · 1.117 fork | WebBuilder | ✅ **PAKAI** — stack **sama** dengan kita; basis "kabar desa" yang ringan (bandingkan tema WordPress 2–4 MB) |
| **next-seo** | github.com/garmeeh/next-seo | Plugin SEO Next.js: meta tag, Open Graph, **JSON-LD** | TypeScript / Next.js | ✅ **MIT** | 8.529 (**29**) · push 2026-07-29 (≈3 bln) | WebBuilder | 🔸 CADANGAN — App Router sekarang punya **Metadata API bawaan**; hanya perlu kalau klien pakai Pages Router |
| **next-sitemap** | github.com/iamvishnusankar/next-sitemap | Generate `sitemap.xml` + `robots.txt` buat Next.js | TypeScript | ✅ **MIT** | 3.747 (**6**) · push 2026-05-13 | WebBuilder | 🔸 CADANGAN — untuk **Astro sudah ada `@astrojs/sitemap`** bawaan |
| **Publii** | github.com/GetPublii/Publii | CMS statis **desktop** (Windows) yang SEO- & privasi-focused: klien ngedit sendiri, output HTML statis, tanpa server | HTML/C++/Electron | ⚠️ **GPL-3.0** | 7.348 (**74**) · push 2026-10-19 | WebBuilder + OpsAgent | 🔸 CADANGAN — cocok buat klien yang tak mau bayar hosting dinamis; **GPL: jual jasa boleh, jangan tanam kodenya ke produk tertutup** |

### 🔎 Catatan SEO/GEO (penting buat jualan & prioritas PDP-ready)
- 🎯 **Urutan paling hemat buat Webuild (nol biaya dulu):** (1) **teknis dasar yang bisa kita tulis sendiri** — `sitemap.xml` + `robots.txt` + canonical + **JSON-LD `LocalBusiness`/`GovernmentOrganization`** + Open Graph + halaman per layanan (ini yang sebenarnya menentukan; semua bisa di Astro/Next); (2) **`llms.txt`** (5 menit) → situs siap AI search; (3) **audit berulang** pakai (adaptasi) **claude-seo / geo-seo-claude** → hasilkan "kartu mutu situs" bertema SEO; (4) **OpenSEO** baru kalau kita butuh **data** pangsa kata kunci/backlink — **ingat: butuh kunci DataForSEO berbayar**.
- 📌 **Halaman per-layanan > halaman profil desa.** Warga mencari *"syarat akta kelahiran desa X"*, *"jam layanan posyandu"* → satu URL per pertanyaan; ini yang bikin situs benar-benar berguna (dan sesudah 16 Jan 2027, halaman layanan juga wajib mencantumkan **dasar hukum + alur pengaduan**).
- 🆕 **GEO = sudut jualan yang belum ada pesaing lokalnya:** uji sendiri — tanya AI *"bagaimana cara mengurus surat pindah di Desa X?"*; kalau jawabannya "hubungi kantor desa", di situ peluangnya. Bukti ke klien: **kutipan AI**, bukan cuma *ranking* Google.
- ⚖️ **Pola "kode MIT + DATA dari API berbayar" (bukan jebakan, tapi wajib jujur):** OpenSEO README: *"Bring your own DataForSEO API key and pay only for what you use"* + hosted $10/bln → jangan pernah bilang "gratis tanpa biaya" ke klien; sebut sebagai **"biaya data per pemakaian"**.
- 🔁 **Skill pack Claude Code ≠ skill Hermes:** claude-seo & geo-seo-claude menyebut `~/.claude/skills/` + perintah `/seo` → **perlu porting** ke format skill Hermes (frontmatter `name`/`description`). **Nilai tertinggi tetap repo yang menyebut "Hermes" di README-nya** — hari ini: **OpenSEO** (MCP + skills, nol porting).
- 🔍 **Query tajam kategori ini:** `seo in:name,description stars:>1500 pushed:>2025-06-01 NOT+awesome` (memunculkan gelombang **skill SEO** baru 2026) · `sitemap generator in:name,description` · **`llms.txt in:name,description`** · atau nama proyek langsung (`open-seo`, `next-seo`, `next-sitemap`, `astro-paper`, `publii`). Kata `seo` saja (tanpa filter) menarik blog-spam & repositori kosong.
- 📈 **⭐ besar di kategori skill SEO = masih wajar** (bukan star-farm): `open-seo` 24,3k⭐ tapi **100 commit/60d + 20 kontributor**, `claude-seo` 19,5k⭐ / 163 subs / 30 kontributor, `geo-seo` 11,1k⭐ / 80 subs → **tulis "muda & hype-driven, uji dulu", bukan "star-farm"**; yang **paling dicurigai** justru repo lama ⭐ besar **tanpa commit** (lihat pelajaran `WOW.js` di seksi motion).

---

## 🎬 DesignerBot / WebBuilder / MotionAgent — Animasi & Motion buat situs ANTI-TEMPLATE (dan 2 jebakan lisensi baru)

> Riset **2026-10-21** — rotasi topik: **design/UI**, sudut yang belum ada: katalog punya *komponen beranimasi siap pakai* (Magic UI, Cult UI, animate-ui, tsParticles) & *video programmatic*, **belum punya lapisan mesin animasi** (yang dipilih saat butuh gerak halus, scroll effect, atau transisi antar halaman).
> **Kebutuhan nyata:** membuat situs klien terasa "mahal & tidak seperti theme beli" — tanpa mengorbankan syarat kita: **ringan (<300 KB), skor Lighthouse tinggi, aksesibel**.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Motion** (dulu *Framer Motion*) | github.com/motiondivision/motion | Mesin animasi standar de-facto untuk React/JS: spring, layout animation, gesture/drag, scroll-linked, exit animation | JS/TS (React, Vue, vanilla) | ✅ **MIT** | 34.393 (**126**) · **100 commit/60d** · 100 kontributor · push 2026-10-20 | WebBuilder + DesignerBot + MotionAgent | ✅ **PAKAI** (paling lengkap) — ⚠️ **repo 1,63 GB** (monorepo) → **jangan di-clone**, pasang lewat npm `motion` |
| **Lenis** | github.com/darkroomengineering/lenis | **Smooth scroll** sangat ringan (<4 KB) — efek "premium" yang paling kelihatan bedanya di situs jasa | JS/TS | ✅ **MIT** | 16.752 (**66**) · 7 commit/60d · push 2026-10-18 | WebBuilder + DesignerBot | ✅ **PAKAI** — ⚠️ **URL lama `studio-freight/lenis` sekarang 404** (pindah org; verifikasi ulang kalau baca catatan lama) |
| **AutoAnimate** | github.com/formkit/auto-animate | Animasi **otomatis satu baris**: list/accordion/DOM insert bergerak sendiri — **paling murah buat UMKM/desa** (tak perlu nulis keyframe) | JS/TS (framework-agnostic, ada wrapper React/Vue) | ✅ **MIT** | 13.935 (**33**) · ⚠️ **0 commit/60d** · push 2026-07-10 | WebBuilder | ✅ PAKAI — kode kecil & stabil; ⚠️ nyaris tanpa perawatan (anggap "selesai", cek kompatibilitas sendiri) |
| ⚠️ **GSAP** | github.com/greensock/GSAP | Toolkit animasi paling tua & paling kuat (timeline, ScrollTrigger, morph SVG) | JS | ⚠️ **BUKAN open source** — **repo TANPA file lisensi**; lisensinya di **halaman web vendor**: *"Standard No Charge GSAP License"* (Webflow) | 29.537 (**424**) · push 2026-04-13 (≈6 bln) | WebBuilder + MotionAgent | ⚠️ **HATI-HATI (jebakan ke-13)** — boleh **komersial & "klien bayar sekali ke kita" itu OK**, **TAPI** (a) dilarang kalau **end-user dikenakan biaya akses/penggunaan**, (b) ada **"Prohibited Uses"**: jangan dipakai di **tool builder animasi no-code** yang bersaing dengan Webflow → butuh lisensi Business Club. **Untuk situs klien: boleh. Untuk produk platform/langganan Webuild: jangan.** |
| 🚫 **WOW.js** | github.com/mattdelacdev/WOW *(dulu `matthieua/WOW`)* | Reveal CSS saat scroll — masih sering direkomendasikan blog "animasi scroll" | JS | 🚫 **TANPA file LICENSE — README menyatakan DUA lisensi: GPLv3 (open source) ATAU lisensi komersial berbayar** (uplabs) untuk kode proprietary | 9.891 (**277**) · **0 commit/60d** (push **2024-06**) | — | 🚫 **JANGAN dipakai** di situs klien (kode kita tertutup = butuh lisensi berbayar / wajib GPL-kan seluruh situs). **Jebakan ke-14** — alternatif MIT: AutoAnimate / Motion / CSS native |
| 🚫 **lax.js** | github.com/alexfoxy/lax.js | Animasi scroll ringan (<4 KB) | JS | ✅ MIT | 10.463 (**2**) · **ARCHIVED** (push 2025-05) | — | 🚫 **MATI** — jangan (arsip + watchers 2) |
| **Nol-JS (bawaan browser)** | MDN: *scroll-driven animations* + *View Transitions API*; Astro punya `<ClientRouter />`/View Transitions bawaan | `animation-timeline: view()` (reveal saat scroll), `@view-transition` (transisi antar halaman) | CSS + HTML | ✅ Gratis (standar web) | — | WebBuilder | ✅ **PAKAI** — nol dependency, nol bundle JS; **wajib pasang `@media (prefers-reduced-motion: reduce)`**. Ini pilihan default kita sebelum tambah library |

### 🔎 Catatan motion (prinsip kerja, bukan cuma daftar repo)
- 🎯 **Animasi = bumbu, bukan menu.** Urutan yang kita pakai: **(1) CSS native** (view transitions / scroll-driven, 0 KB) → **(2) AutoAnimate** (1 baris, untuk list/akordeon) → **(3) Motion** (kalau butuh gesture/spring/layout) → **(4) Lenis** (kalau klien minta "terasa mewah") → **jangan** GSAP/WOW untuk produk tertutup.
- ♿ **`prefers-reduced-motion` wajib** (klien desa/pemerintah = aksesibilitas) + animasi berlebih **menjatuhkan Core Web Vitals** → bertentangan dengan janji jualan kita "situs <300 KB". Sertakan di "kartu mutu situs": bundle JS total + skor Lighthouse.
- 🔍 **Query `scroll animation in:name,description stars:>1000` = JELEK** — hasilnya iOS/Android/Unity (`JazzHands`, `DiscreteScrollView`, `Gemini`, `FancyScrollView`, `ticker`, `hellocharts-android`), bukan web. Pakai **nama proyek langsung** (`motion`, `lenis`, `auto-animate`, `gsap`) atau kata spesifik: `view transitions`, `web animations`, `smooth scroll`.
- 📉 **⭐ besar ≠ hidup ≠ boleh dipakai:** kategori motion hari ini melahirkan **dua jebakan sekaligus** — `WOW.js` 9.891⭐ (GPL/berbayar, 0 commit/60d, & **repo hasil rename** dari `matthieua/WOW`) dan `lax.js` 10.463⭐ (MIT **tapi ARCHIVED**). Sementara yang ⭐ lebih kecil (`AutoAnimate` 13,9k) justru MIT penuh.
- 🧾 **Jebakan lisensi ke-13 (GSAP) — "gratis" versi vendor ≠ open source:** `greensock/GSAP` **tak punya file LICENSE sama sekali** (`spdx_id=null`) & README berteriak *"GSAP is FREE… 100% FREE, even for commercial use"*, padahal lisensinya **hanya ada di halaman web** (`gsap.com/standard-license`). Aturan: kalau repo **tanpa file lisensi** tapi README bilang "free" → **cari halaman lisensi vendor** dan baca **"Prohibited Uses"**-nya; jangan simpul MIT.
- 🧾 **Jebakan lisensi ke-14 (WOW.js) — "GPL ATAU bayar":** README-nya menawarkan **GPLv3** untuk proyek open source **atau beli lisensi komersial** supaya kode tetap proprietary → untuk jasa kita (situs klien tertutup) artinya **wajib beli** atau tinggalkan. Deteksi: repo ⭐ ribuan **tanpa file LICENSE** + README memuat kata *commercial license*.
- 🔀 **Pindah org ≠ selalu redirect:** `studio-freight/lenis` sekarang **404** (repo pindah ke `darkroomengineering/lenis`) — jadi **404 bisa berarti "pindah", bukan "hilang"**; verifikasi lewat pencarian nama baru sebelum membuang catatan lama.

---

## 🧩 DesignerBot / WebBuilder — POLA, TEKSTUR & DEKORASI (latar anti-template, slider, ikon pembayaran)

> Riset **2026-10-22** — rotasi topik: **design/UI**, sudut yang belum ada. Katalog punya **aset** (ikon/font/emoji, 10-17) & **alat token desain** (designlang/Dembrandt, 10-10), **belum punya lapisan POLA/LATAR/DEKORASI** — justru inilah yang bikin situs terasa "dibeli" (gradien ungu default, hero tanpa tekstur). Sekaligus menutup celah yang kita catat sendiri 17 Okt.
> Semua lisensi dibaca dari **file lisensi asli** (bukan `spdx_id`); dua di antaranya **berubah/tidak seperti dugaan** (lihat jebakan ke-15 & ke-16).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **css-doodle** | github.com/css-doodle/css-doodle | **Web component seni visual** (CSS generative): tulis 3 baris → pola/latar unik & tak bisa dibeli sebagai tema | JS / Web Component | ✅ **MIT** (`LICENSE`) | 6.067 (**48**) · **100 commit/60d** · push 2026-10-20 | DesignerBot + WebBuilder | ✅ **PAKAI** — bikin "signature pattern" per klien (mis. pola dari motif/logo desa), nol gambar berat |
| **Embla Carousel** | github.com/davidjerleke/embla-carousel | **Slider/carousel ringan & presisi** — vanilla / React / Vue / **Astro** | TypeScript (framework-agnostic) | ✅ **MIT** (`LICENSE`, © David Jerleke) | 8.455 (24) · 14 commit/60d · push 2026-10-17 | WebBuilder + DesignerBot | ✅ **PAKAI** — testimoni, galeri UMKM, sorotan potensi desa. Katalog sebelumnya **belum punya komponen slider** (⚠️ default branch `master`, bukan `main`) |
| **PatternCraft** | github.com/megh-bari/pattern-craft | **300+ latar pola & gradien** siap copy-paste (Tailwind/CSS) — dipakai lewat website-nya | Tailwind / CSS | ✅ **MIT** (`LICENSE`, © 2025 Megh Bari) | 3.088 (**10**) · 4 commit/60d · push 2026-09-02 · ⚠️ repo **166 MB** | DesignerBot + WebBuilder | ✅ **PAKAI** — **jangan clone**; salin snippet dari patterncraft.store |
| **DoodleCSS** | github.com/chr15m/DoodleCSS | Tema HTML/CSS **"hand-drawn"** (semua elemen terlihat digambar tangan) | CSS | ✅ **MIT** (`LICENSE`) | 1.211 (5) · push 2026-04-27 | DesignerBot | ✅ **PAKAI (niche)** — penangkal "kelihatan template" paling ekstrem; cocok UMKM kuliner/anak/agenda acara, **bukan** untuk situs pemerintah |
| **Open Doodles (React port)** | github.com/lunahq/react-open-doodles | Ilustrasi doodle (160+ elemen manusia/objek) sebagai komponen | React / SVG | ✅ **kode MIT** (`LICENSE`) + **seni = CC0** (opendoodles.com) | 81 (2) · push 2022-12 | DesignerBot + ContentWriter | ✅ **PAKAI** — **jalur ilustrasi paling aman** yang benar-benar ada di GitHub (kode MIT + aset CC0, tanpa share-alike) |
| **Payment icons (Aaron Fagan)** | github.com/aaronfagan/svg-credit-card-payment-icons | **80 ikon kartu/pembayaran, 6 gaya** (SVG) — buat halaman checkout | SVG / CSS | ✅ **Apache-2.0** (`LICENSE`) | 641 (8) · 234 fork · push 2026-04-28 | WebBuilder + SalesAgent | ✅ **PAKAI** — nyambung ke riset checkout QRIS (10-20): halaman bayar UMKM langsung terlihat "resmi". ⚠️ **logo merek = trademark pemiliknya** → jangan dibikin seolah endorse/kerja sama |
| **geopattern** | github.com/btmills/geopattern | **Pola SVG generatif dari sebuah string** (nama desa → pola identitas) | JS | ✅ MIT | 1.843 (35) · push **2021-05** | DesignerBot | 🔸 CADANGAN — kode kecil & selesai, tapi 5 tahun tanpa update |
| **svelte-svg-patterns** | github.com/catchspider2002/svelte-svg-patterns | Pembuat **pola seamless SVG** sebagai latar/header | Svelte / SVG | ✅ MIT | 747 (6) · push 2024-09 | DesignerBot | 🔸 CADANGAN |
| **Trianglify** | github.com/qrohlf/trianglify | Latar **seni segitiga generatif** (dulu populer banget) | JS | ⚠️ **GPL-3.0** | 10.084 (**161**) · push 2025-05 | — | ⚠️ **HATI-HATI** — GPL-3: dipakai di situs klien tertutup berisiko copyleft → pakai **css-doodle/geopattern (MIT)** sebagai gantinya |
| 🚫 **CSS.gg** | github.com/astrit/css.gg | 700+ ikon CSS/SVG (dulu alternatif ikon favorit) | CSS / SVG | 🚫 **BUKAN MIT LAGI sejak v2.1.2** — lisensi kustom: atribusi wajib + **dilarang bikin karya turunan** + **komersial butuh izin tertulis** | 10.058 (**109**) · push 2024-08 | — | 🚫 **JANGAN PAKAI di klien** (jebakan ke-15). Ganti: **Lucide (ISC) / Tabler (MIT)** yang sudah di katalog |
| ⚠️ **Mega Doodles Pack** | github.com/MariaLetta/mega-doodles-pack | 160+ elemen doodle vektor cantik (SVG/PNG) buat sosmed & presentasi | SVG / PNG | ⚠️ **CC BY-SA 4.0** (README) — repo **tanpa file lisensi** | 586 (14) · **push 2019** | — | ⚠️ **HINDARI untuk klien berbayar** — **share-alike**: turunannya wajib berlisensi sama (sekelas masalah OpenMoji). Ambil **Open Doodles (CC0)** |
| **alohe/avatars** | github.com/alohe/avatars | Kumpulan **foto avatar placeholder** siap pakai (CDN jsDelivr) | PNG | ✅ file `LICENCE` = MIT | 500 (2) · 2.018 KB · push 2026-09-21 | DesignerBot | ⚠️ PELAJARI — README **tidak menyebut sumber/kredit** gambar-nya & isinya mengacu ke gaya pihak ketiga (DiceBear dkk.) → untuk kepastian pakai **DiceBear** (sudah di katalog, lisensi per-gaya) |
| 🚫 pattern.css | github.com/bansal/pattern.css | Latar pola CSS-only (3.900⭐, sering direkomendasikan) | CSS | ⚠️ **README menulis "License: MIT" TAPI tanpa file LICENSE** | 3.923 (38) · **0 commit/60d** (push 2022) | — | 🔸 referensi saja — kalau nimbrung ke produk, catat dasar lisensinya dari README (pola jebakan ke-10: izin ada di luar file) |

### 🔎 Catatan pola/tekstur (cara pakai & pelajaran)
- 🎨 **Urutan hemat buat Webuild:** **(1) css-doodle / pola CSS/SVG kita sendiri** (0 KB gambar, bisa dibuat "milik klien") → **(2) PatternCraft** (snippet siap tempel kalau butuh cepat) → **(3) 1 ilustrasi Open Doodles (CC0)** sebagai penyeimbang teks → **(4) Embla** kalau ada galeri/testimoni. Latar **jangan** berupa gambar besar: pola CSS/SVG aman untuk kuota warga & skor Lighthouse.
- 🧾 **Jebakan lisensi ke-15 — lisensi bisa DIPERKETAT di versi baru (dan `spdx_id` tidak tahu).** `astrit/css.gg`: API bilang `NOASSERTION`; file `LICENSE.md` dibuka → *"The previous versions prior to **2.1.2** … are licensed under the MIT License. **This license applies from version 2.1.2**"*, dan isi lisensi baru itu: **Allowed Uses = personal, non-commercial**; *"Any commercial use requires explicit permission"*; larangan membuat karya turunan. **Cara deteksi: kalau file lisensi memuat frasa "previous versions … MIT" → versi baru BUKAN MIT.** (Beda dari Lucide/Simple Icons yang cuma salah baca `spdx_id`.)
- 🔍 **Query `illustrations`/`illustration` = tetap zonk** (dikonfirmasi 2×: hasilnya repo **skill AI pembuat ilustrasi** seperti `ian-xiaohei-illustrations` 12,7k⭐, `awesome-gpt-image-2`, atau proyek tak nyambung). **Kesimpulan jujur: katalog aset ilustrasi legal TIDAK ada di GitHub** — ada di situs masing-masing (opendoodles.com = CC0, unDraw = MIT-style); di GitHub hanya **port**-nya. Query yang berguna justru **nama proyek**: `open-doodles`, `pattern.css`, `css-doodle`, `DoodleCSS`, `embla-carousel`.
- 🖼️ **Halaman kredit tetap wajib** (aturan 17 Okt): setiap aset (pola, ikon, ilustrasi, avatar, logo pembayaran) dicatat di `/kredit` atau komentar CSS → atribusi CC BY / OFL / Apache terpenuhi, dan jadi bahan jualan "semua aset legal & bebas royalti".

---

## 📣 SocialAgent / ContentWriter — Penjadwal & AGEN SOSMED (jawaban untuk "kenapa Postiz belum ada di katalog")

> Riset **2026-10-22** — rotasi topik: **social media**, sudut yang belum ada. Katalog punya penjadwal **kecil** (brightbean/trypost/cogsend/Post4U, 10-08) & link-in-bio (10-18) — **belum punya dua pemain yang sebenarnya dipakai orang**: **Postiz** (terus disebut sebagai pembanding, tapi tak pernah dicatat) & **Mixpost**, plus **agen sosmed** yang menulis/menjadwalkan sendiri.
> Ini juga menutup celah: SocialAgent butuh **mesin**, bukan cuma tombol bagikan.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Postiz** | github.com/gitroomhq/postiz-app | Penjadwal sosmed "**agentic**" paling besar di GitHub: kalender, multi-platform, analitik, tim, approval | Next.js / NestJS / Prisma + Docker | ⚠️ **AGPL-3.0** (`LICENSE`, teks AGPL standar, tanpa syarat tambahan) | 37.537 (**137**) · **100 commit/60d** · **7.318 fork** · push 2026-10-21 | SocialAgent + OpsAgent | ⚠️ **PELAJARI (bukan di VPS ini)** — README-nya menampilkan **logo agen AI yang didukung: ChatGPT · Claude · Claude Code · Codex · Cursor · OpenClaw · + Hermes Agent** (`postiz.com/hermes`) → **integrasi nol-porting** ke tim kita. ⚠️ `docker-compose.yaml` = **9 service** (`postiz`, `postgres`, `redis`, `spotlight`, `temporal` + `elasticsearch` + `postgresql` + `admin-tools` + `ui`) → **berat**; ⚠️ AGPL menyala kalau kita host untuk banyak klien |
| **Mixpost** | github.com/inovector/mixpost | Penjadwal + **analitik engagement** self-host (kalender konten, akun tim, lintas platform) | Laravel / PHP + DB | ✅ **MIT** (`LICENSE.md`, © Inovector) — ⚠️ **tapi ini versi LITE dari "Mixpost Pro" yang komersial** | 3.845 (**34**) · 582 fork · push **2026-03-16** (≈7 bln, melambat) | SocialAgent | ✅ **REKOMENDASI (kalau butuh mesin sendiri)** — lisensi paling bersih di kategori ini & paling ringan; ⚠️ tanpa `docker-compose` (Laravel + DB + queue worker, dipasang manual di server klien) + baca batas Lite vs Pro |
| **Social Media Agent (LangChain)** | github.com/langchain-ai/social-media-agent | **Agen resmi LangChain**: ambil 1 URL → tulis draf post **X/LinkedIn** → **human-in-the-loop** (Slack: setuju/tolak/ubah) → jadwalkan via cron | TypeScript / **LangGraph** | ✅ **MIT** (`LICENSE`, © LangChain) | 2.926 (26) · **74 commit/60d** · push 2026-10-21 | SocialAgent + ContentWriter | ✅ **PELAJARI/PAKAI** — cetak biru "agen yang menulis & menjadwalkan sendiri"; ⚠️ butuh Supabase + Slack + kredensial X/LinkedIn |
| **YouTube Automation Agent** | github.com/darkzOGx/youtube-automation-agent | **Agen otonom channel YouTube ujung-ke-ujung**: riset tren → skrip → narasi → visual → **render MP4** → judul/deskripsi/tag → jadwal → belajar dari analytics + komentar; ada *Shorts Repurposing Studio* (1 video → 3 klip 9:16) | Node.js + FFmpeg (UI dashboard) | ✅ **MIT** (`LICENSE`) | 4.513 (**72**) · 16 commit/60d · push 2026-10-20 · repo 1,3 MB | MotionAgent + SocialAgent + ContentWriter | ✅ **PELAJARI** — paling dekat dengan "pabrik konten" tim kita; **jalan di mesin sendiri + API key sendiri**, ada **mode slideshow lokal (gratis)**; 8 provider teks / 5 penyedia video AI ⚠️ biaya kredit bisa naik → pakai default lokal dulu |
| **AI Marketing Suite (Claude)** | github.com/zubair-trabzada/ai-marketing-claude | 15 **skill marketing** (copywriting, email, SEO, riset kompetitor, analisis) dgn sub-agen paralel | Markdown (Claude Code skill) | ✅ **MIT** | 2.777 (**37**) · **0 commit/60d** (push **2026-03-02**) · repo 132 KB | ContentWriter + SalesAgent | ⚠️ **SNAPSHOT** — isi menarik (satu penulis dgn geo-seo-claude) tapi **tak dirawat sejak Maret** & format Claude Code → perlu porting; jangan jadi fondasi |
| **claude-youtube** | github.com/AgriciDaniel/claude-youtube | Skill Claude Code buat kreator YouTube (audit channel, SEO video, skrip) | Python skill | ✅ MIT | 504 (4) · push 2026-04-10 | ContentWriter | 🔸 CADANGAN (penulis sama dengan claude-seo) |
| **marketing-skills (hyperfx)** | github.com/hyperfx-ai/marketing-skills | Skill marketing buat agen (ads, sosmed, SEO, riset kompetitor) | Python | ✅ MIT | 108 (1) · 9 commit/60d | ContentWriter | 🔸 CADANGAN — kecil |
| **Apify MCP server** | github.com/apify/apify-mcp-server | **MCP** biar agen mengambil data sosmed/web/search (actor Apify) | TypeScript / MCP | perlu cek | 12.454 (?) | OpsAgent | 🔸 CADANGAN — nyaman untuk agen, **tapi platformnya berbayar** (kredit) |
| 🚫 OSINT akun orang | github.com/sherlock-project/sherlock · github.com/qeeqbox/social-analyzer | Melacak akun seseorang di ribuan jaringan | Python / JS | MIT | 94.660 · 24.347 | — | 🚫 **JANGAN** — kategori ini muncul tiap cari "social media"; tidak relevan (OSINT orang) & berisiko etis/legal |

### 🔎 Catatan penjadwal & agen sosmed
- 🧾 **Jebakan lisensi ke-16 (baru) — "repo MIT" ≠ "produknya gratis".** `inovector/mixpost` README: *"This repository contains the **Lite version of Mixpost Pro, a commercial product**… it's essential that **Lite version features remain distinct** from those in Mixpost Pro"* → file `LICENSE.md` benar-benar MIT, tapi ini hanya edisi dasar dari produk berbayar; jangan janji ke klien fitur yang ada di Pro, dan jangan "menambah fitur ala Pro" ke Lite-nya.
- 💾 **Hitung service, lagi-lagi menyelamatkan kita:** Postiz = **9 service** (Temporal + Elasticsearch itu berat) → **tidak mungkin** di VPS 1,9 GB. Pilihan realistis: **(a) Postiz versi hosted/cloud**, **(b) Mixpost Lite di server klien**, **(c) untuk kebutuhan internal cukup cron + API platform** (kita sudah punya skill `xurl` untuk X; WAHA untuk WA). Aturan lama tetap: penjadwal sosmed bukan kandidat self-host di VPS kita.
- 🤖 **Sinyal integrasi terkuat hari ini: README menampilkan LOGO agen AI yang didukung.** Postiz punya folder `.github/agents/` berisi `hermes-agent.svg` + tautan `postiz.com/hermes` (juga ChatGPT/Claude/Codex/Cursor/OpenClaw) → **ini penanda "nol porting"** yang lebih cepat ditemukan daripada membaca seluruh README. **Kebiasaan baru: `gh api repos/O/R/git/trees/HEAD?recursive=1 --jq '.tree[].path' | grep -i "agents/"`** saat menilai repo sosmed/otomasi.
- 📉 **Kategori "analitik sosmed self-host" hampir kosong & banyak yang mati:** `social media analytics in:name,description stars:>800` = **0 hasil**; `instagram analytics` → `jakim/ig-monitoring` **DISCONTINUED**, `ayrshare/social-media-api` (348⭐) = **API berbayar**, sisanya proyek <350⭐. Artinya: **jangan jual "analitik sosmed" ke klien** — cukup laporkan angka dari aplikasi platform + kunjungan web (Umami, sudah di katalog). Untuk YouTube ada `spacesdrive/twiligent` (81⭐) — kecil.
- 🎯 **Rekomendasi buat SocialAgent/ContentWriter:** (1) **mesin posting milik klien** → **Mixpost (MIT)** kalau klien mau punya sendiri, atau **Postiz cloud** kalau tidak mau urus server; (2) **menulis konten** → cetak biru **langchain/social-media-agent** (URL → draf → approval) yang bisa kita tiru pakai agen Hermes sendiri; (3) **skala konten video** → pelajari **youtube-automation-agent** (paling lengkap) & **openfilm** (sudah di katalog); (4) **jangan** masukkan penjadwal sosmed ke VPS produksi.

---

## 🧠 RepoScout + Orchestrator — MEMORI JANGKA PANJANG AGEN (ingatan yang bisa dibaca & diaudit)

> Riset **2026-10-23** (*run ulangan* — run terjadwal 06:00 gagal: `execute_code` timeout → Inferhub HTTP 400 *content-filter*, fallback OmoApicall **401**) — rotasi topik: **agentic AI**, sudut yang belum ada.
> Katalog sudah punya framework agen (10-08) & skills/MCP/kompresi konteks (10-12), **belum punya MEMORI**: cara 9 agen kita ingat pekerjaan kemarin tanpa menaruh semuanya di prompt.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **OpenViking** | github.com/volcengine/OpenViking | **"Context Database" buat agen**: satu *virtual filesystem* `viking://` untuk **pengetahuan + memori + skill** — agen navigasi pakai `ls/tree/read/write/grep/find`, tiap folder punya *summary* (L0–L2) biar agen baca ringkasan dulu; sesi di-*commit* → memori jadi **Markdown yang bisa dibaca & diedit** | Python + Rust (CLI `ov`) + Docker | ⚠️ **AGPL-3.0** (inti, `LICENSE`) — **tapi** `crates/ov_cli` & `examples/` = **Apache-2.0**, dan **plugin Hermes-nya MIT** (`examples/hermes-plugin/LICENSE`) | 40.600 (**113**) · **100 commit/60d** · 100 kontrib · 3.276 fork · rilis v0.5.1.1 (20 Okt) · created 2026-01 | RepoScout + Orchestrator + OpsAgent | ✅ **REKOMENDASI #1 — satu-satunya di katalog yang punya plugin memori Hermes RESMI.** ⭐ **Diverifikasi sendiri 23 Okt:** `hermes plugins search openviking` → *openviking · memory · community · v2.1.1 @ 9f150ece*, `hermes plugins info openviking` lengkap (Tools/Hooks: none) → **nol porting**: `hermes plugins install openviking --enable` + `hermes memory setup openviking`. Angka README mereka: LoCoMo **Hermes 33,38% → 82,86%** (token −34–91%, latensi −58–66%). Deploy = **2 service** (`openviking` + `caddy`) → paling ringan di kategori memori. ⚠️ **3 catatan jujur:** (a) **Quick Local** memasang server OpenViking 0.4.x dari PyPI + **llama-cpp-python + model embedding lokal** → **berat buat VPS 1,9 GB kita (zram penuh)** & servernya **tetap hidup** setelah Hermes keluar/plugin dilepas (`hermes openviking local stop`); (b) **privasi** — disklosur resmi: *conversation turns, tool results, dan edit `MEMORY.md`/`USER.md` dikirim ke server* → pikir dulu sebelum dipasang di profil yang pegang kredensial klien; (c) AGPL: self-host apa adanya aman, **jangan** jual versi modifikasi sebagai layanan tanpa membuka kode. Saran: uji di **PC user** atau tab VPS terpisah |
| **Hindsight** | github.com/vectorize-io/hindsight | Memori agen yang **BELAJAR**, bukan cuma mengingat riwayat: operasi `retain` / `recall` / `reflect`, *observations*, *mental models* & knowledge pages | Python + SDK Python/JS, **MCP server**, integrasi coding agent, bisa **embedded tanpa server** | ✅ **MIT** (`LICENSE`, © Vectorize AI; sub-lisensi integrasi juga MIT; ada Hindsight Cloud berbayar) | 52.740 (**107**) · 100 commit/60d · 100 kontrib · 6.212 fork · rilis v1.1.0 (21 Okt) · **created 2025-10-30** | RepoScout + Orchestrator | ⚠️ **PELAJARI (hype — uji dulu)** — klaim SOTA **LongMemEval** + paper arXiv; mode embedded menarik buat uji cepat. ⚠️ rasio **⭐:watchers = 493** (ambang kita ~300) & repo **825 MB** → jangan jadi fondasi tanpa uji; **belum ada integrasi Hermes** (0 sebutan) |
| **cognee** | github.com/topoteretes/cognee | Platform memori AI: **graph + vector** untuk memori jangka panjang persisten; ada `cognee-mcp` | Python (Docker) | ✅ **Apache-2.0** (`LICENSE`) | 32.677 (**103**) · 100 commit/60d · 3.406 fork · rilis v1.6.5 (16 Okt) · **created 2023-08 (paling matang)** | RepoScout + OpsAgent | ✅ **PELAJARI** — paling "dewasa" + ada MCP; ⚠️ `docker-compose` = `cognee` + `cognee-mcp` + `frontend` + **Neo4j + Postgres + Redis** (+ redisinsight) → **berat** → VPS khusus/PC, bukan VPS produksi kita |
| **ruflo** *(dulu Claude-Flow)* | github.com/ruvnet/ruflo | **Harness orkestrasi swarm multi-agent**: koordinasi banyak agen paralel, plugin tim AI | TypeScript / Node | ✅ **MIT** (`LICENSE`, © ruvnet) — ⚠️ sub-folder `ruflo/src/ruvocal/LICENSE` = Apache-2.0 (© Hugging Face) | 78.483 (**471**) · 100 commit/60d · 78 kontrib · rilis **v3.59.17** (22 Okt) · created 2025-06 | Orchestrator + OpsAgent | ⚠️ **PELAJARI (ambil polanya saja)** — watchers sehat (rasio 167) & 19 sebutan MCP, **tapi** ritme rilis ekstrem (v3.59) = permukaan API bergerak cepat → jangan jadi fondasi |
| **Agent-Skills-for-Context-Engineering** | github.com/muratcankoylan/Agent-Skills-for-Context-Engineering | Kumpulan **skill agen** soal rekayasa konteks: arsitektur multi-agent, sistem memori, pemadatan konteks | Markdown / Python (agent skills) | ✅ **MIT** | 18.190 (**104**) · push 2026-10-12 · created 2025-12 | RepoScout + semua agent | ✅ **PELAJARI/ADAPTASI** — bahan kurikulum skill tim; formatnya skill agen → gampang diadaptasi ke pola skill Hermes |
| **nanobot** | github.com/HKUDS/nanobot | Framework **agen personal ultra-ringan** self-host: jalan di browser/terminal/chat app, ingat preferensi, jadwalkan tugas | Python ≥3.11 / Docker (`nanobot-gateway` + `api` + `cli`) | ✅ **MIT** | 49.283 (**211**) · 100 commit/60d · 8.669 fork · rilis v0.3.5 (15 Sep) · created 2026-02 | OpsAgent + Orchestrator | ⚠️ **CADANGAN/referensi** — **repo cuma 79 MB** & docs ada **Bahasa Indonesia** (`nanobot.wiki/id`) → bagus buat **membandingkan arsitektur harness ringan** vs Hermes; ⚠️ dia **pesaing** Hermes → pelajari, jangan ditumpuk di VPS yang sama |

### 🔎 Catatan memori agen
- ⭐ **Temuan terbesar hari ini: memori Hermes sudah tersedia sebagai plugin di katalog resmi Hermes.** `hermes plugins search openviking` (dijalankan sendiri 23 Okt) → entri **`openviking`** (kategori *memory*, tier *community*, v2.1.1 pinned `9f150ece`), `hermes plugins info openviking` lengkap. *Cara menemukan kelas repo ini:* **grep `hermes` di SELURUH TREE, bukan cuma README** — OpenViking punya `docs/en/agent-integrations/05-hermes.md`, `examples/hermes-plugin/` (`plugin.yaml` + 20 file tes), `benchmark/locomo/hermes/`, dan logo `hermes-agent.png`.
- 🧾 **Jebakan lisensi ke-17 (baru) — lisensi karangan VENDOR dengan nama baru: "MSCL-1.0-GPL".** `directus/directus` (38.621⭐, subs 346, 92 commit/60d) `spdx=NOASSERTION`, dan file lisensinya bernama **`license`** (huruf kecil, **tanpa ekstensi**): *"Monospace Sustainable Core License, Version 1.0 — MSCL-1.0-GPL"* © **Monospace Inc. 2026** → keluarga **fair-code/BSL**: boleh apa pun **kecuali "Competing Use"**, **dilarang menembus/mematikan fungsi license key**, komersial terbatas (internal / pendidikan-riset non-komersial / jasa ke pemegang lisensi) → 🚫 **jangan dipakai buat jasa/produk Webuild.** Regex grep lisensi harus mencakup **huruf kecil & tanpa ekstensi** (`^(LICEN|COPYING|licen|copying)`).
- 💾 **Keluarga "External Deployment" = copyleft tersulut-hosting, sekelas AGPL.** `trailbaseio/trailbase` pakai **OSL-3.0**; §5 *External Deployment*: menyediakan karya **supaya bisa dipakai orang lain lewat jaringan** = **distribusi** → wajib buka kode. Untuk alat yang mau kita **host-kan ke klien**, cek kata **"External Deployment"/"network"** di file lisensi (AGPL, OSL-3.0, SSPL), bukan cuma nama lisensinya.
- 📊 **Kategori "memori agen" = sabuk ⭐ muda; patokan tetap rasio watchers.** Semua kandidat ⭐ 18k–78k tapi umur <1 tahun (kecuali cognee 2023) → ukur **rasio ⭐:subs** (Hindsight **493** ⚠️ · cognee 317 · nanobot 234 · ruflo **167** ✅) + **commit/60d** + **jumlah kontributor** + **ada/tidaknya rilis**. ⭐ tinggi + watchers puluhan + 0 rilis = uji dulu.
- 🤝 **`mem0` (66.774⭐, Apache-2.0) sudah ada di katalog sejak 8 Okt** (bagian "Proyek 2 & 3") → tidak diduplikasi. Yang baru hari ini: OpenViking (khusus Hermes), Hindsight, cognee, ruflo, nanobot.

---

## 🧰 WebBuilder / OpsAgent — BACKEND & DATA RINGAN buat SITUS KLIEN (BaaS "1 file", tanpa VPS berat)

> Riset **2026-10-23** — rotasi topik: **web dev**, sudut yang belum ada. Katalog punya CMS (10-12), analitik & formulir (10-14), hosting (10-14) — **belum punya "database + auth + API"**, padahal itu yang diminta klien begitu minta *"form-nya masuk ke admin"* / *"katalog UMKM"* / *"panel data desa"*, dan yang biasa dipakai (Supabase/Firebase) semuanya berat.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **PocketBase** | github.com/pocketbase/pocketbase | **Backend dalam 1 FILE** (Go): SQLite tertanam + **realtime subscriptions**, manajemen **file & user**, **dashboard admin**, API REST-ish; bisa dipakai sebagai **kerangka Go** buat logika sendiri | Go 1.27+ (1 binary, **tanpa docker-compose**) + SDK resmi JS & Dart | ✅ **MIT** (`LICENSE.md`, © Gani Georgiev) | 61.548 (**329**) · 57 commit/60d · 45 kontrib · rilis v0.40.5 (8 Okt) · repo 147 MB (binary ±30 MB) | WebBuilder + OpsAgent | ✅ **REKOMENDASI UTAMA** — **nol service tambahan** di VPS (1 proses + 1 file DB): pas untuk **formulir klien, katalog UMKM, panel data desa, & demo produk** — pengganti hemat dari Formbricks/Supabase (10–12 container). ⚠️ **pre-1.0 (v0.40)** — README sendiri: *"full backward compatibility is not guaranteed before v1.0.0"* → pakai untuk proyek yang kita kendalikan, jangan janji API stabil ke klien; taruh di belakang NPM (SSL) + backup rutin file DB; ⚠️ bukan pengganti Supabase jika butuh multi-tenant/role granular |
| **TrailBase** | github.com/trailbaseio/trailbase | Alternatif Firebase **1 executable** (Rust): API type-safe (REST + realtime), auth, admin UI, **sub-milidetik** | Rust (1 binary) + client Dart/Go/Swift/JS | ⚠️ **OSL-3.0** (`LICENSE`) — **ada klausul External Deployment (§5)** | 5.720 (**20**) · 100 commit/60d · 34 kontrib · rilis v0.35.2 (21 Okt) · created 2024-10 | WebBuilder + OpsAgent | ⚠️ **CADANGAN** — kekuatan: 1 executable & cepat (cocok VPS kecil); **tapi lisensinya paling "menyala"** kalau kita host untuk klien (wajib buka kode kalau dimodifikasi lalu di-*deploy* ke orang lain) → pakai **apa adanya** |
| **bknd** | github.com/bknd-io/bknd | Firebase/Supabase alternatif **ringan** yang bisa jalan **di dalam** Next.js/React Router (tanpa server terpisah) | TypeScript | ✅ **Apache-2.0** (`LICENSE.md`) | 3.776 (**16**) · **0 commit/60d** (push 2026-09-24; rilis terakhir Jan 2026) | WebBuilder | ⚠️ **SNAPSHOT/pantau** — idenya pas (BaaS nempel di app kita), tapi **berhenti bergerak 60 hari** → jangan jadi fondasi dulu |
| **Butterbase** | github.com/butterbase-ai/butterbase | BaaS open source: **Postgres + auth + storage + functions + AI gateway + MCP** | TypeScript | ✅ **Apache-2.0** (`LICENSE`, © NetGPT Inc.) | 3.030 (**113**) · 75 commit/60d · **6 kontrib** · belum ada rilis · created 2026-05 | WebBuilder + RepoScout | ⚠️ **UJI DULU** — rasio watchers bagus & 12 sebutan MCP, tapi **tim inti cuma 6 orang** & belum pernah rilis → menarik, belum terbukti |
| **nhost** | github.com/nhost/nhost | Alternatif Firebase lengkap: Postgres + **GraphQL (Hasura)** + storage + functions + dashboard | TypeScript / Docker | ✅ **MIT** (`LICENSE`) | 9.364 (**48**) · 100 commit/60d · rilis 20 Okt · **repo 940 MB** | OpsAgent | 🔸 **CADANGAN** — lengkap, tapi **berat** (banyak service + Postgres) → bukan buat VPS 1,9 GB; baru masuk kalau klien punya server sendiri |
| **SuperTokens** | github.com/supertokens/supertokens-core | **Autentikasi** mandiri (alternatif Auth0 / Firebase Auth): sesi, social login, MFA, self-host | Java (core) + SDK banyak bahasa | ⚠️ **Apache-2.0 inti + folder `ee/`** (lisensi terpisah: `ee/LICENSE.md`) | 15.333 (**88**) · 100 commit/60d | WebBuilder + OpsAgent | 🔸 **CADANGAN** — open-core: pakai inti Apache-2.0, **cek `ee/`** sebelum pakai fitur enterprise; alternatif termurah = login bawaan PocketBase |
| **Directus** | github.com/directus/directus | Headless CMS/data platform di atas DB apa pun | TypeScript / Vue | 🚫 **"MSCL-1.0-GPL" (Monospace Sustainable Core License) — fair-code, BUKAN open source** | 38.621 (**346**) | — | 🚫 **JANGAN** buat jasa/produk kita — lihat **jebakan lisensi ke-17** di catatan bawah |
| **sqlite-sync** | github.com/sqliteai/sqlite-sync | **Sinkronisasi offline-first (CRDT) untuk SQLite** — aplikasi desa/lapangan yang sering putus internet | C | ✅ **Apache-2.0** | 587 (**5**) · push 2026-10-22 | WebBuilder + OpsAgent | 🔸 **CADANGAN** — kecil tapi nyambung ke kebutuhan desa 3T (sinyal lemah; lihat berita Berau 20–23 Okt); uji dulu |

### 🔎 Catatan backend & data ringan
- 🎯 **Cara pakai urutannya:** **halaman statis (Astro) + WA/Sheets** → **PocketBase (1 binary)** → baru **Supabase/Postgres** kalau memang perlu skala. Ini menutup celah katalog: CMS (Decap/EmDash/Publii) untuk *konten*, analitik (Umami) untuk *angka*, tapi **database+auth+API** belum ada — PocketBase mengisi itu dengan biaya RAM nyaris nol.
- 💾 **Pelajaran "hitung service" bentuk baru: yang terbaik justru TIDAK punya `docker-compose`.** PocketBase = `./pocketbase serve` (1 proses + 1 file DB); TrailBase = 1 binary; sebaliknya nhost/Supabase = banyak container. **Penyaring pertama paling murah: `git/trees | grep -iE "docker-compose|Dockerfile"`** — repo tanpa compose belum tentu ribet, bisa jadi justru paling ringan.
- 🔍 **Query tajam kategori ini: `firebase alternative in:name,description`** (dapat PocketBase lewat endpoint langsung + trailbase/bknd/butterbase/nhost); **`backend as a service` (cuma 2 hasil) & `sqlite backend` (hasilnya library Key-Value/CLI Discord) = jelek.**
- 🧾 **Nama file lisensi bisa huruf kecil & tanpa ekstensi** (Directus: `license`) → grep `^(LICEN|COPYING|licen|copying)`. Dan **MIT tanpa judul tetap MIT** (`zhayujie/CowAgent`: file `LICENSE` cuma *"Copyright (c) 2022 zhayujie"* + teks MIT apa adanya, tanpa baris "MIT License") → jangan simpul "lisensi aneh" dari ketiadaan judul. Bonus **rename**: `zhayujie/chatgpt-on-wechat` (nama populer lama) sekarang = **`zhayujie/CowAgent`** (47.507⭐, subs 314) → verifikasi ulang URL lama sebelum dikutip.

---

## 🗺️ WebBuilder / SalesAgent — PETA & BASEMAP buat Situs Desa (peta potensi, batas wilayah, titik UMKM) — tanpa API key Google

> Riset **2026-10-24** — rotasi topik: **web dev**, sudut yang belum ada. Katalog sudah punya hampir semua lapisan situs klien (template, komponen, CMS, analitik, form, booking, pencarian, SEO/GEO, backend), **belum punya PETA** — padahal (a) situs desa hampir selalu diminta menampilkan **peta potensi / batas wilayah / sebaran UMKM**; (b) **Google Maps = API key + tagihan per pemuatan** → bertentangan dengan paket "situs desa murah"; (c) NewsWatch 23 Okt mencatat **pemkab diminta memetakan titik lemah sinyal (Berau)** → peta naik kelas jadi barang jualan ke pemda.
> Semua lisensi dibaca dari **file lisensi asli**; dua di antaranya **tidak seperti dugaan** (jebakan lisensi ke-19 + lisensi DATA peta/ODbL, lihat catatan).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **Leaflet** | github.com/Leaflet/Leaflet | Peta interaktif **paling ringan & paling tua yang masih hidup** (~42 KB gzip): marker, popup, layer, plugin segudang — jalan tanpa framework (pas buat Astro) | JS (vanilla) | ✅ **BSD-2-Clause** | 45.771 (**888** — subs paling sehat di kategori ini) · 81 commit/60d · 100 kontributor · push 2026-10-23 | WebBuilder | ✅ **REKOMENDASI #1 buat desa** — peta potensi/UMKM/lokasi kantor desa dengan biaya nyaris nol; ⚠️ rilis terakhir bertag `dev` (2025-09) tapi commit tetap deras |
| **OpenFreeMap** | github.com/hyperknot/openfreemap | **Hosting tile vektor GRATIS** buat peta gaya sendiri: instance publik **tanpa batas jumlah view/request, tanpa registrasi, tanpa API key, tanpa cookie** (dibiayai donasi); semua open-source, **tanpa model open-core** | Python (deploy script) + Ubuntu 24.04, Docker-free | ✅ **MIT** (`LICENSE.md`) — ⚠️ **data peta = OpenStreetMap → ODbL** | 6.262 (**39**) · 36 commit/60d · 9 kontributor · push 2026-10-23 | WebBuilder + OpsAgent | ✅ **PAKAI** — inilah jalan keluar "peta cantik tanpa tagihan Google"; pasangkan dengan **MapLibre**. ⚠️ jujur: **bukan SLA/komersial** (donasi) & self-host-nya butuh server + disk besar → bukan buat VPS 1,9 GB |
| **MapLibre GL JS** | github.com/maplibre/maplibre-gl-js | Mesin **peta vektor** open source (fork `mapbox-gl-js` v1.13): gaya kustom, rotasi/pitch, 3D — tanpa API key Mapbox | TypeScript | ✅ **BSD-3-Clause** (`LICENSE.txt`; API bilang **NOASSERTION**; di dalamnya ada kode pihak ketiga: mapbox-gl-js BSD-3, glfx.js MIT, d3-color BSD-3) | 11.927 (**104**) · 100 commit/60d · 100 kontributor · rilis **v6.15.0 (18 Okt)** | WebBuilder + DesignerBot | ✅ **PAKAI** — peta vektor "kelas mahal" buat situs desa wisata; ⚠️ repo **1,06 GB** → **jangan di-clone**, pakai npm |
| **Martin** | github.com/maplibre/martin | **Tile server 1 binary (Rust)**: PostGIS / MBTiles / **PMTiles** → endpoint tile siap pakai | Rust | ✅ **Apache-2.0** | 4.018 (**34**) · 100 commit/60d · rilis 22 Okt | OpsAgent | ✅ **PAKAI (kalau self-host)** — jalur paling hemat untuk menyajikan peta dari data sendiri (1 proses, bukan 5 container) |
| **PMTiles** | github.com/protomaps/PMTiles | **Format 1 file** untuk kumpulan tile peta → bisa ditaruh di **hosting statis/object storage**, tanpa tile server | TypeScript/JS/C++/Go/Python | ✅ **BSD-3-Clause** untuk implementasi referensi + **spec = public domain/CC0** ⚠️ **tileset sampel lisensinya sendiri-sendiri** (ada `REUSE.toml`) | 3.096 (**24**) · 5 commit/60d (pola "stabil/selesai") · 53 kontributor | OpsAgent + WebBuilder | ✅ **PAKAI** — cara paling murah self-host peta: satu file `.pmtiles` di CDN/R2, nol server |
| **Protomaps Basemaps** | github.com/protomaps/basemaps | **Gaya basemap siap pakai** untuk MapLibre + PMTiles (di-generate dari OSM) | Java/TS | ✅ kode **BSD-3** (`LICENSE.md`) **+** data `LICENSE_DATA.md`: **OSM/ODbL (share-alike + atribusi)**, Natural Earth | 766 (**15**) · push 2026-09-11 | DesignerBot + OpsAgent | ✅ **PAKAI** — pasangan wajib PMTiles; **baca `LICENSE_DATA.md`, bukan cuma `LICENSE.md`** |
| **Terra Draw** | github.com/JamesLMilner/terra-draw | Library **menggambar & mengedit geometri di peta** (dukung MapLibre, Leaflet, OpenLayers, Google) | TypeScript | ✅ **MIT** (`LICENSE`) | 1.120 (**9**) · 37 commit/60d · 46 kontributor · `terra-draw@1.38.0` (18 Okt) | WebBuilder | 🔸 CADANGAN — buat modul "tandai lokasi potensi/UMKM" di panel admin klien |
| **react-map-gl** | github.com/visgl/react-map-gl | API React resmi komunitas **vis.gl** untuk Mapbox **atau MapLibre** (`react-map-gl/maplibre`) | TypeScript / React | ✅ **MIT** (`LICENSE`; API bilang NOASSERTION) | 8.514 (**1.909**!) · 1.347 fork · push 2026-09-03 | WebBuilder | ✅ **PAKAI kalau stack React/Next** — pengganti aman `react-leaflet` (lihat catatan 🚨); subs 1.909 = paling dipercaya |
| ⚠️ **mapcn** | github.com/AnmolSaini16/mapcn | **Komponen peta gaya shadcn/ui** (MapLibre + Tailwind): tema terang/gelap, satu perintah setup | TypeScript / React | ✅ **MIT** (`LICENSE`) | 12.309 (**45** — rasio 274:1) · 718 fork · dibuat **2025-12-28** · 24 commit/60d · **3 kontributor** · masih v0.1.0 | WebBuilder + DesignerBot | ⚠️ **UJI DULU** — paling cepat menyatu dengan stack kita (shadcn), **tapi** muda + tim 3 orang; ⚠️ **basemap default = CARTO** (kuota komersial 1 juta tile/bulan, atribusi wajib, bisa butuh API key) → arahkan ke **OpenFreeMap/PMTiles** |
| **TileServer GL** | github.com/maptiler/tileserver-gl | Server tile **raster & vektor** + style GL, ada render sisi server | Node / Docker | ✅ **BSD-2-Clause** (`LICENSE.md`) | 2.911 (**62**) · 33 commit/60d · rilis **v5.7.0 (23 Okt)** | OpsAgent | 🔸 CADANGAN — alternatif Martin kalau mau ekosistem Node |
| **Headway** | github.com/headwaymaps/headway | **Stack peta self-host lengkap** (geocoding + routing + tile) dari OpenStreetMap | Rust / Docker | ✅ **Apache-2.0** | 3.009 (**15**) | OpsAgent | 🔸 CADANGAN — lengkap tapi **banyak service** (server sendiri, bukan VPS kita) |
| 🚫 **react-leaflet** | github.com/PaulLeCam/react-leaflet | Wrapper **React** untuk Leaflet (paling populer, 5.6k⭐) — **tapi lisensinya bukan open source** | TypeScript / React | 🚫 **Hippocratic License 2.1** (ethical source, **bukan OSI**; README sendiri: *"Hippocratic License"*) | 5.605 (**55**) · ⚠️ **0 commit/60d** · rilis terakhir **v5.0.0 (Des 2024)** | — | 🚫 **JANGAN dipakai buat klien** — lihat **jebakan lisensi ke-19**; ganti: **react-map-gl (MIT)** / **mapcn (MIT)** / Leaflet langsung |
| ⚠️ **uMap** | github.com/umap-project/umap | Bikin peta OSM + **embed** ke situs dalam beberapa menit (peta partisipatif warga) | JS / Django | ⚠️ **AGPL-3.0** (`LICENSE`) | 1.622 (**49**) · push 2026-10-22 | SocialAgent | ⚠️ **HATI-HATI** — AGPL menyala kalau kita **host & modifikasi untuk banyak klien**; pakai versi publiknya (umap.openstreetmap.fr) atau taruh di server klien |

### 🔎 Cadangan (lisensi BELUM kami verifikasi — jangan dipakai sebelum dicek)
| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/leaflet-extras/leaflet-providers | 2.391 | Konfigurasi puluhan penyedia tile gratis untuk Leaflet (berguna banget buat pemilihan basemap) → cek dulu syarat tiap penyedia |
| github.com/geoman-io/leaflet-geoman | 2.434 | Plugin menggambar/mengedit di Leaflet |
| github.com/maplibre/maputnik | 2.660 | Editor gaya visual untuk spesifikasi MapLibre (bikin gaya peta "milik klien") |
| github.com/hyperknot/openfreemap-styles | — | Repo **gaya** (styles) OpenFreeMap — dikembangkan terus, sumber gaya siap pakai |

### 🔎 Catatan peta & basemap (buat Webuilder & SalesAgent)
- 🎯 **Urutan paling hemat buat Webuild (nol API key, nol tagihan):** **(1) Leaflet (BSD-2) + tile publik** untuk peta ringan → **(2) MapLibre + OpenFreeMap (MIT, gratis tanpa batas)** kalau mau peta vektor yang terasa "mahal" → **(3) PMTiles di hosting statis / Martin (1 binary)** kalau mau data peta sendiri & lepas dari layanan pihak ketiga → **(4) mapcn/react-map-gl** kalau situsnya React/Next. **Jangan pakai Google Maps API** di paket desa: API key + tagihan per pemuatan = bertentangan dengan harga jual kita.
- 🧾 **Jebakan lisensi ke-19 (BARU) — `spdx=NOASSERTION` bisa berarti lisensi "ETHICAL SOURCE", bukan open core.** **`PaulLeCam/react-leaflet`** (5.605⭐, subs 55, wrapper React Leaflet paling populer) punya `LICENSE.md` yang **bukan MIT**: barisnya berbunyi *"Hippocratic License Version Number: 2.1"* (ethicalsource.dev), berisi bagian **"Compliance with Human Rights Principles and Human Rights Laws"**, **arbitrase Hague Rules**, dan **klausul indemnity**; README punya bagian *"License — Hippocratic License"*. **Bukan larangan komersial**, tetapi: (a) **bukan lisensi OSI** → banyak **pengadaan pemerintah/pemda mensyaratkan lisensi open source terdaftar OSI** (nyambung ke paket kita ke desa/pemda!); (b) lisensor bisa **mengakhiri lisensi sepihak** kalau menilai ada pelanggaran HAM; (c) wajib meneruskan lisensi + menandai perubahan. **Deteksi: grep kata `Hippocratic` / `ethicalsource` di file lisensi & README.** Riwayat file lisensi menunjukkan perubahan terakhir pada commit **`Release v3` (31 Okt 2020)** → **sejak v3 bukan MIT lagi** (v4.2.1 & v5.0.0 sama-sama Hippocratic). Gantinya: **react-map-gl (MIT)** / **mapcn (MIT)** / Leaflet vanilla (BSD-2).
- 🗺️ **Lisensi DATA peta ≠ lisensi KODE peta — ODbL.** Kode peta boleh BSD/MIT, **tapi data OpenStreetMap = ODbL**: (a) **atribusi "© OpenStreetMap" wajib terlihat** di peta yang kita kirim ke klien; (b) ODbL **share-alike untuk DATABASE TURUNAN** → kalau kita meng-*extract*/membangun database tile dari data OSM, database itu wajib berlisensi ODbL (gambar peta sebagai *Produced Work* cukup atribusi). Cara menemukannya: repo peta bisa punya **DUA file lisensi** — `LICENSE.md` (kode) + **`LICENSE_DATA.md`** (data) seperti **`protomaps/basemaps`**; dan `protomaps/PMTiles` bahkan menulis **spec = CC0, kode = BSD-3, tileset sampel = lisensi sendiri**. → **aturan lama "grep lisensi REKURSIF" berlaku juga untuk data.**
- 🔁 **Motif berulang ke-3: "kode MIT + layanan pihak ketiga berkuota/berbayar".** **mapcn** kode MIT dan **"zero config"**, tapi basemap default-nya **CARTO Basemaps** — README sendiri: komersial gratis **hanya sampai 1 juta tile request/bulan**, **atribusi CARTO + OSM wajib**, dan **API key** diperlukan untuk raster (bisa diperluas ke vektor). Sama polanya dengan `open-seo`→DataForSEO (21 Okt) & `Open-Generative-AI`→MuAPI (9 Okt). **Aturan: komponen peta "langsung jalan" → baca bagian basemap/provider/API key sebelum bilang "gratis" ke klien.**
- 🧾 **File lisensi bisa cuma PENUNJUK (bukan teks lisensi).** `containers/bubblewrap` (lihat seksi sandbox) punya file `LICENSE` **dan** `COPYING.LIB` yang isinya **7 byte: kata `COPYING`** — lisensi sebenarnya ada di file `COPYING` (**LGPL-2.1**). **Kalau file lisensi sangat pendek / isinya hanya nama file lain → ikuti rujukannya**, jangan simpul "tanpa lisensi" atau "lisensi tidak jelas".
- 📣 **Bahan jualan konkret (nyambung NewsWatch 23 Okt):** *"peta potensi desa + peta titik lemah sinyal (blank spot) — dibuat tanpa biaya langganan Google Maps, datanya dari OpenStreetMap, atribusi resmi kami cantumkan."* Ini melengkapi **template pitch kabupaten** yang sudah dicatat NewsWatch; sekaligus pembeda anti-template (gaya peta bisa dibuat "milik klien" via Maputnik/gaya OpenFreeMap).
- 🔍 **Query tajam kategori peta:** **`maplibre`**, **`leaflet in:name,description`**, **`protomaps`**, **`pmtiles`**, **`openfreemap`**, **`tile server`**, **`vector tiles`**. ⚠️ **`google+maps+alternative in:name,description` = ZONK** (hasilnya extension privasi, picker Android, repo 79⭐) — pelajaran `desa`/`booking` berlaku lagi: **pakai istilah teknis/nama proyek, bukan frasa "alternatif X"**.

---

## 🧱 OpsAgent / RepoScout — SANDBOX EKSEKUSI KODE buat AGEN (jalankan kode pihak ketiga tanpa membahayakan server)

> Riset **2026-10-24** — rotasi topik: **agentic AI**, sudut yang belum ada. Katalog sudah punya kerangka agen, memori, MCP/skill, gateway LLM, observability, browser agent, RAG — **belum punya RUNTIME ISOLASI**: tempat menjalankan kode yang tidak kita percaya (skill pihak ketiga, kode hasil generate agen, scraper, otomasi klien).
> **Alasan nyata:** (a) tim kita berbasis **skill + execute_code** — dan **`execute_code` Hermes BUKAN sandbox** (kernel Python yang persisten di profil); (b) 13 Okt kita sudah mencatat risiko skill pihak ketiga (`aig-skill-scan`) tapi belum punya tempat "menahan" kodenya; (c) klien minta otomasi yang menjalankan skrip mereka.
> **Diverifikasi langsung di VPS ini:** `ls -l /dev/kvm` → **tidak ada**, `grep -cE 'vmx|svm' /proc/cpuinfo` → **0** → **microVM/Firecracker (kelas terkuat) TIDAK BISA jalan di VPS kita.** Ini yang menentukan urutan rekomendasi di bawah.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **gVisor** | github.com/google/gvisor | **Kernel aplikasi untuk container** (sandbox proses Google, dipakai Cloud Run): isolasi **tanpa perlu KVM** (platform `ptrace`; KVM opsional buat performa) | Go | ✅ **Apache-2.0** | 19.763 (**322** — sehat) · push 2026-10-23 · sejak 2018 | OpsAgent | ✅ **REKOMENDASI buat VPS kita** — satu-satunya jalur isolasi "keras" yang realistis di server tanpa `/dev/kvm`; jalankan wadah sekali-jalan, buang sesudahnya |
| **microsandbox** | github.com/superradcompany/microsandbox | **microVM lokal** untuk *untrusted workloads* (agen, kode user, plugin, scraper, CI): CLI `msb` + SDK | Rust (CLI + SDK), microVM | ✅ **Apache-2.0** | 8.784 (**26** — rasio 338 ⚠️) · 100 commit/60d · 72 kontributor · rilis **v0.7.9 (22 Okt)** · repo **987 MB** | OpsAgent | ⚠️ **PC/Linux bare-metal SAJA** — README *Requirements*: **Linux = KVM enabled** → **mustahil di VPS kita**; sangat pas di **PC user (Windows/macOS)** |
| **OpenSandbox** | github.com/opensandbox-group/OpenSandbox | **Runtime sandbox buat agen** (kode, command, file, browser, desktop) lewat API terpadu: Docker lokal → Kubernetes; **Firecracker 64 ms P50**; **kebijakan egress per-sandbox**; **Credential Vault** (agen pakai kredensial tanpa melihatnya); SDK Python/TS/Java/C#/Go + CLI `osb` + **MCP** | Python + K8s/Firecracker | ✅ **Apache-2.0** | 16.111 (**62**) · 100 commit/60d · 100 kontributor · `release-1.2.0-rc.2` (21 Okt) · dibuat 2025-12 · repo 113 MB | OpsAgent + RepoScout | ✅ **PELAJARI** — paling lengkap & aktif (badge OpenSSF Best Practices); ⚠️ mode cepatnya (Firecracker/K8s) **butuh KVM** → uji mode Docker dulu atau tunggu VPS khusus |
| **CubeSandbox** | github.com/TencentCloud/CubeSandbox | Sandbox agen **kilat & padat** (Tencent): isolasi **hardware-level**, startup puluhan ms, **API kompatibel E2B**, CNCF Landscape | Go (+ PyPI `cubesandbox`) | ✅ **Apache-2.0** (kecuali komponen pihak ketiga; API bilang **NOASSERTION**) | 13.024 (**61**) · 100 commit/60d · rilis v0.7.3 (12 Okt) · **dibuat 2026-04-10** | OpsAgent | ⚠️ **UJI DULU** — paling "siap produksi" secara klaim, tapi **muda** + hardware-level isolation = **butuh KVM** |
| **perplexityai/SPACE** | github.com/perplexityai/SPACE | "Sandboxed Platform for Agentic Code Execution" — sandbox **pluggable-runtime** (Perplexity) | Rust | ✅ **Apache-2.0** | 1.909 (**6**) · 100 commit/60d · **dibuat 2026-10-01 (3 minggu!)** | RepoScout | ⚠️ **PANTAU** — kualitas organisasi + ritme tinggi, tapi terlalu baru untuk jadi fondasi |
| **nsjail** | github.com/google/nsjail | **Isolasi proses ringan** (namespaces, seccomp, cgroup) — alat klasik buat menjalankan perintah tak dipercaya | C++ / Linux | ✅ **Apache-2.0** | 4.170 (**82**) · push 2026-10-02 | OpsAgent | ✅ **PAKAI (level praktis)** — tanpa KVM, tanpa container engine; pembungkus perintah agen |
| **bubblewrap** | github.com/containers/bubblewrap | **Sandbox unprivileged tingkat rendah** (dipakai Flatpak): batasi filesystem/namespace tanpa root | C | ⚠️ **LGPL-2.1** — teks aslinya di file **`COPYING`**; `LICENSE` & `COPYING.LIB` cuma **penunjuk 7 byte** | 9.177 (**62**) · push 2026-10-14 | OpsAgent | 🔸 CADANGAN — aman sebagai **alat terpisah** (LGPL), hati-hati kalau di-link jadi library ke produk tertutup |
| **Wasmer** | github.com/wasmerio/wasmer | **Runtime WebAssembly** (sandbox by design, ringan) — jalur paling hemat RAM untuk kode yang tak dipercaya | Rust | ✅ **MIT** | 21.188 (**194**) · push 2026-10-23 | OpsAgent | 🔸 CADANGAN — buat fungsi kecil/plugin (bukan lingkungan penuh); paling cocok VPS RAM-ketat |
| ⚠️ **agent-infra/sandbox** | github.com/agent-infra/sandbox | Sandbox **all-in-one**: browser + shell + file + MCP + VSCode dalam satu wadah | Python | ✅ **Apache-2.0** | 6.220 (**34**) · **5 commit/60d** (mandek sejak **14 Sep**) · rilis v1.11.0 (23 Jun) | OpsAgent | ⚠️ **SNAPSHOT** — konsepnya pas, tapi tidak bergerak 6 minggu → pantau |
| ⚠️ **SWE-ReX** | github.com/SWE-agent/SWE-ReX | Eksekusi kode tersandbox **lokal atau di cloud** (mesin di belakang SWE-agent), paralel masif | Python | ✅ **MIT** | 623 (**5**) · **0 commit/60d** · rilis terakhir v1.4.0 (Agt 2025) | RepoScout | ⚠️ **SNAPSHOT** — bagus buat membaca polanya, jangan fondasi |
| **abshkbh/arrakis** | github.com/abshkbh/arrakis | Sandbox code-execution agen **self-host yang bisa dikustom** (VM) | Go | ⚠️ **AGPL-3.0** | 890 (**9**) · push terakhir **2025-06-02** | — | 🚫 SKIP — AGPL + **setahun tanpa update** |

### 🔎 Catatan sandbox agen (penting: saring lewat HARDWARE, bukan ⭐)
- 🖥️ **Penyaring pertama kelas "sandbox/agent runtime" = apakah butuh KVM.** Buktikan dulu, jangan percaya label "lightweight":
  ```bash
  ls -l /dev/kvm ; grep -cE 'vmx|svm' /proc/cpuinfo   # VPS kita: tidak ada file, hasil 0
  ```
  Hasil hari ini: **0 vmx/svm, tanpa `/dev/kvm`** → semua **microVM/Firecracker** (`microsandbox`, `CubeSandbox`, mode cepat `OpenSandbox`) **mustahil** di VPS ini. **Yang masih bisa:** **gVisor (ptrace)**, **nsjail/bubblewrap** (namespaces), **WASM (Wasmer)**, atau **container sekali-jalan** (Docker/rootless). Ini generalisasi aturan lama "hitung service dulu" → sekarang: **"cek dulu kebutuhan hypervisor/KVM"**, sama seperti kita menolak RAG 17-container.
- 📉 **Kategori ini penuh repo muda ber-⭐ puluhan ribu — ukur kerja nyata, bukan ⭐.** `OpenSandbox` 16,1k⭐ tapi **dibuat Des 2025**, `CubeSandbox` 13k⭐ **dibuat Apr 2026**, `microsandbox` (Okt 2024) subs cuma 26 (rasio **338**), `SPACE` dibuat **1 Okt 2026**. Yang ⭐-nya jauh lebih kecil tapi **matang & sehat**: **`google/gvisor`** (subs 322, sejak 2018). Bukti kerja: **commit/60d + kontributor + rilis** (ketiganya kuat untuk OpenSandbox/CubeSandbox/microsandbox → tulis *"muda, uji dulu"*, bukan star-farm).
- 🚨 **Jujur soal alat kita sendiri: `execute_code` Hermes BUKAN sandbox.** Kernel Python-nya **persisten per profil** (variabel & import bertahan antar panggilan) dan berjalan **dengan hak akses agen** → jangan pakai untuk **kode pihak ketiga / hasil generate LLM yang belum dibaca**. Untuk itu: bungkus dengan **nsjail/bubblewrap** atau jalankan di **container buang**; kalau butuh isolasi keras **tanpa KVM**, **gVisor**.
- 🔐 **Dua fitur yang paling relevan buat klien (bukan buat kita sendiri):** (a) **egress policy per-sandbox** (batasi ke mana sandbox boleh keluar — penting karena agen yang disusupi = pintu keluar data); (b) **Credential Vault** (OpenSandbox): agen memanggil layanan luar **tanpa pernah melihat kredensial** → pola yang benar untuk WAHA/API klien di masa depan.
- 💾 **Jangan pasang sandbox sebagai service menetap di VPS 1,9 GB** (saat riset: RAM available **606 MB**, 2 vCPU). Pola yang benar sama seperti browser agent (15 Okt): **jalankan sekali-jalan, lalu matikan**; atau taruh di **PC user** (microsandbox mendukung Windows/macOS, syarat Linux = KVM).
- 🔍 **Query tajam kategori ini:** **`agent sandbox in:name,description stars:>300`**, **`sandbox for AI agents in:name,description`**, `microsandbox`, `code execution sandbox agent in:name,description stars:>500`. ⚠️ **`e2b alternative in:name,description` = ZONK** (repo <900⭐, banyak proyek 0–4⭐) → **jangan pakai frasa "alternatif X"**; pakai istilah teknis (`microvm`, `firecracker`, `gvisor`, `code interpreter sandbox`).

---

## 🍪 WebBuilder / SalesAgent — KEPATUHAN PRIVASI SITUS KLIEN (banner izin + embed sadar-privasi → paket "PDP-ready")

> Riset **2026-10-26** — rotasi topik: **web dev + kepatuhan**. Katalog sudah punya analitik klien (Umami) & formulir, tapi **`grep consent` = 0** → kelas **persetujuan/privasi** belum ada sama sekali.
> **Kebutuhan nyata:** prioritas #1 tim = paket **"situs desa PDP-ready"** (UU PDP 27/2022 + PP 33/2026 berlaku **16 Jan 2027**). Setiap situs klien yang memasang **embed pihak ketiga** (YouTube, Google Maps, feed IG/FB, widget chat, tombol share) menaruh **cookie pihak ketiga** di perangkat warga → butuh **izin + kontrol**, dan kalau ditanya pemda/Satgas PDP kita harus bisa **menunjukkan buktinya**.
> **Prinsip kita (anti-template + hemat):** situs statis Astro + **analitik tanpa cookie (Umami)** + **embed facade** → sebagian besar situs desa **tidak butuh cookie apa pun**. Banner izin baru wajib begitu ada layanan non-esensial (GA4/Ads, YouTube, Maps Google, chat pihak ketiga).

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **tarteaucitron.js** | github.com/AmauriC/tarteaucitron.js | **Manajer persetujuan (CMP) vanilla JS**: banner izin, panel preferensi **per-layanan**, **pemblokiran skrip sampai izin diberikan**, **placeholder untuk konten tertunda**, dukungan **Google Consent Mode v2** / Bing / Piano | JavaScript (tanpa dependency, tanpa server) | ✅ **MIT** (`LICENSE`, © 2014 AmauriC) | 1.058 (**34**) · **26 commit/60d** · 100 kontributor · push 2026-10-15 · repo **2,2 MB** | WebBuilder + SalesAgent | ✅ **REKOMENDASI** — paling lengkap fiturnya & masih dirawat; ⚠️ ada **layanan Pro berbayar** (deteksi otomatis + dashboard + statistik izin) di tarteaucitron.io → **library-nya tetap MIT**, Pro cuma tambahan |
| **vanilla-cookieconsent** | github.com/orestbida/cookieconsent | Banner izin cookie **paling populer** (v3.1.0, ~10 KB): kategori izin, mode opt-in, tombol ganti preferensi, API bersih, tanpa server | JavaScript (vanilla) | ✅ **MIT** | 5.718 (**63**) · 508 fork · ⚠️ **0 commit/60d** · rilis terakhir **v3.1.0 (4 Feb 2025)** | WebBuilder | ✅ **PAKAI (stabil/selesai)** — paling pas buat situs **Astro statis** (tempel 1 script); jujur: hampir **20 bulan tanpa rilis/commit** → anggap "selesai", uji sendiri di browser tahun ini |
| ⚠️ **c15t** | github.com/c15t/c15t | CMP modern buat **React/Next.js/Vue**: komponen banner + registry, **rekaman persetujuan & riwayat audit**, integrasi tag manager & 30+ analitik (GA4, Umami, PostHog, Matomo…) | TypeScript (monorepo) | ✅ **Apache-2.0** (`LICENSE.md`) | 2.004 (**subs 4** ⚠️ rasio **501**) · 100 commit/60d · 30 kontributor · rilis 2026-10-23 · repo 57 MB | WebBuilder | ⚠️ **UJI DULU** — paling menyatu dengan Next.js & punya **bukti persetujuan** (nilai tinggi kalau diaudit); tapi **rasio ⭐:watchers ekstrem**, dan backend: **self-host `@c15t/backend` (Postgres/MySQL/SQLite)** **atau** **hosted gratis "Inth"** → **motif ke-4 "kode bebas + backend hosted pihak ketiga"** |
| ⚠️ **Klaro** | github.com/kiprotect/klaro | CMP open source (agensi Jerman KIProtect): teks & terjemahan siap pakai, Consent Mode, mudah di-embed | JavaScript | ✅ **BSD-3-Clause** (`LICENSE`, © 2019-2020 KIProtect GmbH; **API bilang NOASSERTION** → jebakan spdx lagi) | 1.522 (**31**) · ⚠️ **0 commit/60d** · push terakhir **2025-03-27** · **tanpa rilis** | — | ⚠️ **PANTAU (MANDEK 7 bulan)** — lisensi & terjemahan bagus, tapi jangan jadikan fondasi baru |
| **lite-youtube-embed** | github.com/paulirish/lite-youtube-embed | **Facade YouTube**: tampil thumbnail dulu, **iframe YouTube baru dimuat setelah diklik** → **nol cookie pihak ketiga** sampai warga memilih, halaman jauh lebih ringan | HTML/JS (web component) | ✅ **Apache-2.0** (`LICENSE`, © 2019 Paul Irish; API bilang **NOASSERTION**) | 6.352 (**56**) · 299 fork · ⚠️ **0 commit/60d** · push terakhir **2025-11-10** | WebBuilder + DesignerBot | ✅ **PAKAI** — inilah cara "pakai video YouTube tanpa kena urusan cookie"; komponen kecil = "selesai" itu wajar |
| **lite-youtube** (web component) | github.com/justinribeiro/lite-youtube | Versi **custom element** dari pola facade (tanpa framework, `<lite-youtube>`), dukungan shadow DOM | TypeScript (Lit) | ✅ **MIT** | 1.375 (**11**) · push 2026-04-21 | WebBuilder | ✅ **PAKAI** — alternatif kalau mau elemen HTML sendiri, bukan `div`+JS |
| **react-lite-youtube-embed** | github.com/ibrahimcesar/react-lite-youtube-embed | Facade YouTube untuk **React/Next** (SSR-friendly) | TypeScript / React | ✅ **MIT** | 382 (**1**) · push 2026-10-19 · sejak 2019 | WebBuilder | 🔸 CADANGAN — buat situs Next.js klien |

### 🔎 Cadangan & catatan kepatuhan privasi (untuk SalesAgent & WebBuilder)

| Repo | ⭐ | Catatan |
|---|---|---|
| github.com/nisrulz/app-privacy-policy-generator | 4.882 | Generator **kebijakan privasi + syarat penggunaan** (1 halaman HTML, jalan offline) — ⚠️ **AGPL-3.0**, dan orientasinya **aplikasi mobile/app store**, bukan website → boleh dipakai sebagai **alat internal** untuk bahan draf, **jangan** salin kodenya ke produk klien |
| github.com/umami-software/umami *(sudah di katalog)* | 39.350 | Analitik **tanpa cookie** (MIT, 2 service) → **inilah alasan sebagian situs kita tidak butuh banner izin sama sekali** |
| github.com/Leaflet/Leaflet *(sudah di katalog)* | 45.771 | Peta **tanpa cookie** (BSD-2, atribusi "© OpenStreetMap") → pengganti Google Maps yang biasanya jadi sumber cookie pihak ketiga |

- 🧠 **Urutan keputusan yang benar (bukan "semua situs pasang banner"):** **(1) buang dulu sumber cookie-nya** — pakai **Umami** (tanpa cookie) alih-alih GA4, **Leaflet+OSM** alih-alih Google Maps, **lite-youtube-embed** alih-alih iframe mentah, **share tombol sendiri/statis** alih-alih widget pihak ketiga; **(2) kalau tetap ada layanan non-esensial** → pasang **tarteaucitron.js** (MIT) atau **vanilla-cookieconsent** (MIT) sebagai banner + **catat layanan yang dimuat setelah izin**; **(3) kalau klien butuh bukti persetujuan/audit** (atau Next.js + butuh dashboard) → pertimbangkan **c15t** (Apache-2.0, ada rekaman izin; backend self-host *atau* hosted).
- 🇮🇩 **Bahasa jualan yang jujur & tidak menakut-nakuti:** *"Situs desa Bapak/Ibu kami rancang supaya **tidak menaruh cookie iklan** — statistik pengunjung tetap ada, tapi tanpa melacak warga; kalau ada video YouTube, videonya dimuat hanya setelah warga klik. Ini yang diminta UU PDP (berlaku 16 Jan 2027)."* Ini pembeda nyata vs vendor tema WordPress yang menempel GA4 + pixel Facebook + Google Maps dalam sekali pasang.
- ⚠️ **Jangan klaim "bebas cookie" tanpa memeriksa:** (a) embed Google Maps/YouTube/IG masih memasang cookie **dari domain mereka**; (b) banyak tema/template populer sudah menyelipkan GA4 + pixel + Google Fonts → **cek juga Google Fonts** (pakai **font self-host**, sudah tercatat di katalog); (c) Consent Mode v2 hanya relevan kalau klien pakai GA4/Google Ads — **bukan** kewajiban umum.
- 🔍 **Query tajam:** **`cookie+consent+manager+in:name,description+stars:>200`** ✅ (hasil bersih) · **nama proyek langsung**: `tarteaucitron`, `cookieconsent`, `klaro`, `c15t`, `lite-youtube`. ⚠️ **`consent management platform in:name,description` = BERISIK** (isinya extension *penolak* consent seperti `MathRobin/Never-Consent` + repo tak nyambung); ⚠️ **`click-to-load in:name,description` = ZONK total** (yang muncul `ComfyUI-MultiGPU`, config OpenWrt, pelacak akun X) → pakai **nama proyek komponennya**.
- ⚠️ **Jebakan spdx berulang:** **paulirish/lite-youtube-embed = Apache-2.0** dan **klaro = BSD-3-Clause**, dua-duanya dilaporkan **`NOASSERTION`** oleh API → tetap **baca file lisensinya** (aturan lama, terbukti lagi hari ini).

---

## 💾 OpsAgent / WebBuilder — BACKUP & RESTORE TERUJI (situs klien, database, vault — bukan sekadar "ada backup")

> Riset **2026-10-26** — rotasi topik: **web dev / operasi**. Katalog punya deploy (NPM/Coolify), monitor (Uptime Kuma), analitik — tapi **`grep restic|kopia|borg` = 0** → kelas **backup** belum ada, padahal ini yang paling sering dijanjikan ke klien desa/pemda.
> **Alasan nyata:** (a) klien pemerintah menanyakan **"kalau server mati, data kami di mana?"**; (b) **bukti dari tim sendiri** — RepoScout **gagal total 25 Okt** (content filter provider + fallback mati) → katalog hari itu **kosong**; kemampuan memulihkan keadaan itu inti operasi; (c) banyak situs kita = **file statis + sedikit data** → pola backup-nya jauh lebih sederhana daripada yang dijual vendor.

| Nama | URL | Fungsi | Stack | Lisensi | ⭐ (subs) | Pemilik | Status |
|---|---|---|---|---|---|---|---|
| **restic** | github.com/restic/restic | **Program backup fondasi** (dedup + enkripsi + snapshot): backend **S3/R2/SFTP/local**, `restore`/`check`/`forget --prune`, 1 binary | Go | ✅ **BSD-2-Clause** (`LICENSE`, © 2014 Alexander Neumann) | 36.799 (**233** — paling sehat di kategori) · 41 commit/60d · 100 kontributor · rilis **v0.19.1 (5 Jul 2026)** | OpsAgent | ✅ **REKOMENDASI** — pasang sebagai **cron sekali-jalan** (bukan service menetap) di VPS RAM-ketat; simpan snapshot **di luar VPS** (R2/S3) |
| **kopia** | github.com/kopia/kopia | Backup **lintas platform** dengan **kebijakan retensi**, snapshot filesystem, mount/restore, UI; bisa juga jadi backend dedup | Go | ✅ **Apache-2.0** | 14.429 (**58**) · 88 commit/60d · 100 kontributor · rilis v0.23.1 (16 Jun 2026) | OpsAgent | ✅ **PAKAI** — alternatif restic kalau mau **kebijakan retensi berlapis** bawaan (mirip GFS) tanpa skrip sendiri |
| **gobackup** | github.com/gobackup/gobackup | **CLI backup database + file → cloud** terjadwal dari 1 file YAML: MySQL/PostgreSQL/**Redis/MongoDB** + folder → S3/Cloudflare R2/B2/WebDAV/FTP | Go (**1 binary, repo 686 KB**) | ✅ **MIT** (`LICENSE`, © 2017 Jason Lee) | 3.082 (**27**) · ⚠️ **0 commit/60d** · rilis **v3.1.1 (6 Jul 2026)** | OpsAgent | ✅ **PAKAI (stabil)** — paling ringan buat "dump DB → R2" di server kecil; jujur: rilis terakhir Jul 2026 → anggap stabil, uji restore sendiri |
| **litestream** | github.com/benbjohnson/litestream | **Replikasi berkelanjutan SQLite** ke S3/R2 (RPO detik, bukan jam) + restore | Go | ✅ **Apache-2.0** | 14.529 (**82**) · 43 commit/60d · rilis v0.5.17 (31 Agt 2026) | OpsAgent | ✅ **REKOMENDASI (khusus SQLite)** — pasangan wajib **PocketBase** ("panel data 1 file" yang sudah kita catat): panel klien aman tanpa DB server |
| **databasus** | github.com/databasus/databasus | Manajer backup **PostgreSQL** self-host: **Point-In-Time Recovery (RPO/RTO rendah)**, **verifikasi restore otomatis**, retensi **GFS** (hourly→yearly), enkripsi AES-256-GCM, notifikasi Telegram/Slack, storage S3/R2/Drive/FTP/SFTP | TypeScript (**1 container**, image `databasus/databasus:latest` + 1 volume) | ✅ **Apache-2.0** | 9.188 (**38**) · 100 commit/60d · 38 kontributor · rilis 24 Okt 2026 · dibuat Jun 2025 · repo **206 MB** | OpsAgent | ⚠️ **UJI DULU** — fiturnya kelas enterprise (PITR + *restore verification* = "backup terbukti"); ⚠️ **PostgreSQL saja** & masih muda |
| **databasement** | github.com/David-Crty/databasement | **Panel web backup database** (Postgres/MySQL/MariaDB/MSSQL/SQLite?) — jadwalkan, jalankan, restore dari UI | PHP / Laravel | ✅ **MIT** | 2.572 (**18**) · 100 commit/60d · 14 kontributor · rilis harian (25 Okt) · **dibuat 14 Nov 2025** | OpsAgent | ⚠️ **UJI DULU** — lisensi paling bersih (MIT) & UI rapi, tapi repo **sangat muda** (<1 tahun) |
| **Portabase** | github.com/Portabase/portabase | Alat **backup & restore database** self-host (PostgreSQL, MySQL, MSSQL, MariaDB) | TypeScript | ✅ **Apache-2.0** | 1.854 (**8**) · 100 commit/60d · 28 kontributor | OpsAgent | 🔸 CADANGAN — kandidat ketiga kalau databasement/databasus tidak cocok |
| **zerobyte** | github.com/nicotsx/zerobyte | **UI web + orkestrator di atas restic** (jadwal, retensi, restore dari browser) — "backup automation for self-hosters" | TypeScript (compose prod **1 service**) | ⚠️ **AGPL-3.0** (+ `LICENSES/BSD-2-Clause-Restic.txt`, ada `NOTICES.md`) | 7.073 (**17** ⚠️ rasio 416) · 93 commit/60d · 29 kontributor · rilis 21 Okt 2026 · dibuat **Agu 2025** | OpsAgent | ⚠️ **HATI-HATI** — UI-nya enak, tapi **AGPL menyala kalau kita host & modifikasi untuk banyak klien**; untuk internal sendiri = aman |
| **Backrest** | github.com/garethgeorge/backrest | **Web UI + scheduler untuk restic** (yang paling dikenal) | TypeScript | ⚠️ **GPL-3.0** | 7.737 (**17**) · ⚠️ **0 commit/60d** · rilis terakhir **12 Jul 2026** | OpsAgent | ⚠️ **PANTAU (mandek ±3 bulan)** — dulu pilihan populer; sekarang `<zerobyte>` lebih aktif |
| **docker-volume-backup** | github.com/offen/docker-volume-backup | Backup **volume Docker** (label-based) → S3/WebDAV/Azure/Dropbox/SFTP/local, otomatis terjadwal | Go (container pendamping) | ✅ **MPL-2.0** | 4.059 (**12**) · 38 commit/60d · 45 kontributor · rilis 22 Okt 2026 | OpsAgent | 🔸 CADANGAN — paling gampang untuk **volume service** (mis. data Umami/listmonk); MPL = copyleft tingkat file, aman sebagai alat terpisah |

### 🔎 Catatan backup (urutan kerja & aturan jujur)

- 🎯 **Urutan backup Webuild (dari yang paling murah):** **(1) kode & dokumen → git + vault (sudah jalan)** tapi **git bukan backup** (repo bisa dihapus/di-rewrite/corrupt) → tambahkan **arsip `.tar.gz`/snapshot ke R2**; **(2) situs statis klien** = repo + output build → arsipkan **seluruh project + `dist/`** per rilis; **(3) data dinamis** = **PocketBase/SQLite → litestream** (RPO detik) *atau* snapshot file + restic; **Postgres (Umami/listmonk) → `pg_dump` terjadwal (gobackup)** atau **databasus** kalau mau PITR + verifikasi restore; **(4) konfigurasi server** = `/etc/nginx` + compose + `.env` (rahasia disimpan terenkripsi di **password manager user**, bukan di dalam server yang di-backup).
- 🧪 **Aturan #1: backup yang belum pernah di-restore = belum terbukti.** Tulis **prosedur restore 1 halaman** per klien, dan **uji restore tiap kuartal** (PocketBase & Postgres) — sekaligus bahan jualan: *"kami pernah menguji pemulihan data Bapak/Ibu, ini hasilnya"* (nada sama seperti "kartu mutu situs").
- 🌍 **Simpan salinan DI LUAR VPS.** Server yang di-backup **tidak boleh** jadi satu-satunya tempat snapshot (VPS kita RAM-ketat & single point of failure) → backend **Cloudflare R2/S3/Backblaze** dengan **enkripsi bawaan restic/kopia** (kunci enkripsi jangan ikut di server itu).
- 🪶 **Jangan pasang semuanya di VPS 1,9 GB.** Yang cukup: **restic (cron) + gobackup atau litestream** = 2 alat CLI tanpa service menetap. UI seperti **zerobyte / Backrest / databasus / databasement** = **1 container** tapi tambahan RAM → pasang kalau ada VPS khusus, atau jalankan di **PC user** untuk memantau snapshot R2.
- 🔍 **Query tajam:** **`backup+tool+in:name,description+stars:>1000+pushed:>2025-06-01`** ✅ · **`database+backup+in:name,description+stars:>500+pushed:>2025-06-01`** ✅ · nama proyek langsung (`restic`, `kopia`, `litestream`, `gobackup`). ⚠️ **`restic+in:name,description` = BERISIK** (yang muncul `gin`, `svelte`, `json-server`, `insomnia` — kata "REST" menyeret framework API) → **selalu tambah `+backup` atau `language:go`**; ini contoh ke-4 jebakan substring (`desa`→`desafio`, `booking`→hotel, `qris`→`qrisp`).
- ⚠️ **Keaktifan ≠ ⭐ (terbukti lagi):** **Backrest** (7.737⭐) **0 commit/60d** mandek 3 bulan, **gobackup** (3.082⭐) juga 0 commit/60d tapi **stabil & MIT**, sementara **restic** (36,8k⭐, subs 233) tetap jadi fondasi. Urutan cek: `.archived` → commit/60d → rilis terakhir → subs → ⭐.

---

## 🔗 Terkait
- [[06-Tim-Agent/Team Registry]]
- [[03-Proyek/04-Virtual-Office-Visualisasi/README|Proyek 04 — Virtual Office]]

#reposcout #github #katalog