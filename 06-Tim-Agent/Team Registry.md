# 🤖 Tim Agent — Team Registry

> Peta resmi tim agent AI Webuild. **Orchestrator:** Hermes.
> Prinsip: agent = pekerja spesialis; user = pengambil keputusan.

---

## 🏢 Struktur: 5 Divisi

### 🎨 Divisi KREATIF — bikin aset
| Agent | Tugas | Tool/Integrasi | Status |
|---|---|---|---|
| **DesignerBot** | Visual & mockup desain | Figma MCP | ⚪ Rencana |
| **MotionAgent** | Motion graphics, animasi, video pendek | Remotion / Manim / FFmpeg | ⚪ Rencana |
| **VoiceAgent** | TTS **Indonesia + Sunda + Jawa**, narasi, dubbing | Meta MMS TTS (open-source, gratis) | ⚪ Rencana |
| **ContentWriter** | Teks & konten multi-segmen | vault, web | ⚪ Rencana |

### 📱 Divisi DISTRIBUSI — sebar konten
| Agent | Tugas | Tool/Integrasi | Status |
|---|---|---|---|
| **SocialAgent** | Posting harian penuh: TikTok, IG, Threads | **Buffer** (skrg) → Postiz (nanti) | ⚪ Rencana |
| **WebPublisher** | Blog, SEO, update website klien | git, CMS | ⚪ Rencana |

### 🔍 Divisi RISET — cari info
| Agent | Tugas | Tool/Integrasi | Status |
|---|---|---|---|
| **RepoScout** | Cari repo GitHub berguna (AI, agentic, design, content, web) | `gh` CLI + DeepWiki MCP | ⚪ Rencana |
| **TrendScout** | Tren teknologi & desain | web search | ⚪ Rencana |
| **NewsWatch** | Monitor berita & regulasi **Komdigi** | cron + scraping | ⚪ Rencana |

### 🏗️ Divisi PRODUKSI — bikin produk klien
| Agent | Tugas | Tool/Integrasi | Status |
|---|---|---|---|
| **WebBuilder** | Bangun website modern anti-template | Next.js, Tailwind, git, VPS | ⚪ Rencana |
| **OpsAgent** | Deploy, monitoring, maintenance | cron, VPS, nginx | ⚪ Rencana |

### 📊 Divisi BISNIS — jualan & koordinasi
| Agent | Tugas | Tool/Integrasi | Status |
|---|---|---|---|
| **SalesAgent** | Proposal & penawaran | vault, PDF | ⚪ Rencana |
| **Orchestrator** | Koordinasi semua agent | delegate, cron, vault | 🟢 Aktif |

---

## 🔌 Integrasi

| Integrasi | Buat apa | Status |
|---|---|---|
| **GitHub** (`gh` CLI) | Repo, issue, PR | ⚪ Belum dipasang |
| **DeepWiki** (MCP) | Tanya jawab repo GitHub publik | ⚪ Belum dipasang |
| **Figma** (MCP) | Design canvas | ⚪ Belum dipasang |
| **Context7** (MCP) | Dokumentasi library terbaru | ⚪ Belum dipasang |
| **Buffer** (MCP) | Auto-posting sosmed | ⚪ Belum dipasang |

---

## 📋 SOP — Alur Kerja Agent

**Alur standar (1 tugas):**
```
User kasih goal
   ↓
Orchestrator pecah jadi sub-task
   ↓
Delegate ke agent spesialis
   ↓
Agent kerjain (riset/bikin/eksekusi)
   ↓
Orchestrator verifikasi hasil
   ↓
Simpan ke vault + lapor ke user
```

**Aturan:**
1. Tiap agent punya 1 domain jelas — nggak tumpang tindih
2. Hasil kerja selalu masuk vault (biar terekam)
3. Pelajaran baru → disimpen jadi *skill* (biar makin pinter)
4. User = pengambil keputusan akhir

**Dua tipe agent:**
- **Ephemeral** (sementara) — buat tugas sekali jalan
- **Persisten** (tetap) — punya jadwal otomatis (mis. NewsWatch harian)

---

## 🔗 Terkait
- [[01-Bisnis/Webuild - Visi & Roadmap]]
- [[README|Vault Index]]

#tim-agent #fondasi #sop