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

| Nama | URL | Fungsi | Stack | Pemilik |
|---|---|---|---|---|
| *(menunggu riset lanjutan)* | | | | |

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

---

## 🔗 Terkait
- [[06-Tim-Agent/Team Registry]]
- [[03-Proyek/04-Virtual-Office-Visualisasi/README|Proyek 04 — Virtual Office]]

#reposcout #github #katalog