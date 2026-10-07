# 🎮 Proyek 04 — Virtual Office Visualisasi

> **Status:** 🟢 **PROTOTIPE JALAN** (7 Okt 2026) · **Divisi:** Produk AI
> **Nama internal:** *Webuild Office*

---

## 💡 Ide

Orang bisa **lihat agent AI mereka bekerja secara visual** (kayak game) + kirim perintah dari tampilan itu — lewat website kita, setting sesimpel mungkin.

**Jadi produk:** bukan cuma internal Webuild, tapi **ditawarkan ke orang lain** yang mau visualisasi agent AI mereka.

## ✅ Yang sudah dibangun (v1)

Diadaptasi dari **`W17ant/Claude-Office`** (MIT) — pixel-art office yang memvisualisasikan agent real-time.

**Kunci: GAK BUTUH CLAUDE.** Claude Code cuma sumber event-nya. Hermes punya padanan persis:
> `hooks.outbound` (outbound webhook) → POST tiap aktivitas ke server kita.

### Arsitektur

```
[Hermes agent / bot]
      ↓  hooks.outbound: post_tool_call, on_session_start/end, subagent_start/stop
      ↓  POST http://100.115.213.21:3334/hermes
[Office Server  (Express + ws + node:sqlite)]  ← systemd: webuild-office
      ↓  WebSocket broadcast
[Frontend React + Vite  (pixel-art office)]
      ↓
   🖥️ Browser (via Tailscale)
```

### Akses

```
http://100.115.213.21:3334/
```
> ⚠️ **Cuma lewat Tailscale** (bind ke interface Tailscale — privat, **nggak kebuka ke internet**).

### Pemetaan agent → karakter

| Profil Hermes | Karakter | Role |
|---|---|---|
| `default` | **Orchestrator** | boss |
| `reposcout` | RepoScout | ai-engineer |
| `newswatch` | NewsWatch | code-reviewer |
| `webbuilder` | WebBuilder | frontend-developer |
| `designer` | DesignerBot | frontend-developer |
| `motion` | MotionAgent | employee-3 |
| `voice` | VoiceAgent | prompt-engineer |
| `social` | SocialAgent | employee-2 |
| `content` | ContentWriter | employee-1 |
| `ops` | OpsAgent | devops-engineer |
| `sales` | SalesAgent | general-purpose |
| `trend` | TrendScout | employee-1 |

*(tambah baris di `PROFILE_TO_AGENT`, `server/index.js`)*

## 📁 Lokasi file

| Item | Path |
|---|---|
| App | `/root/webuild-office/` |
| Server | `server/index.js` (endpoint `/hermes`, `/event`, `/roster`) |
| Frontend | `src/` → build ke `dist/` |
| Sprites | `public/sprites/` + `dist/sprites/` |
| Config bos | `office.config.json` |
| Service | `/etc/systemd/system/webuild-office.service` |
| Log | `/var/log/webuild-office.log` |
| Token auth | `~/.agent-office/auth-token` |

## 🔧 Perintah

```bash
systemctl status webuild-office     # cek
systemctl restart webuild-office    # restart
cd /root/webuild-office && npm run build   # rebuild frontend kalau src diubah
hermes hooks list                   # cek webhook Hermes
```

## ⚠️ Prinsip Keamanan (WAJIB)

Pelajaran dari VPS lama (ke-lockout port 22):
- ✅ Bind **cuma ke IP Tailscale** — nggak buka ke internet
- ✅ **NGGAK** sentuh SSH/UFW/iptables/port 22
- ✅ systemd **user-level app**, bukan perubahan network-level
- Ikuti [[08-Infrastruktur/Prosedur Pemulihan Akses]]

## 🔧 Perbaikan dari repo asli (catatan teknis)

1. `better-sqlite3` → **`node:sqlite`** (bawaan Node 26, gak perlu compile — VPS gak ada g++)
2. Electron dibuang (VPS headless → cukup web)
3. URL di frontend: hardcode `localhost:3334` → **`window.location`** (same-origin)
4. Server **serve frontend** sendiri (`dist/`) → 1 port
5. `vite build target: esnext` (butuh top-level await)
6. Tambah endpoint **`/hermes`** = jembatan webhook Hermes → gerakan agent

## 📋 Todo lanjutan
- [ ] Sprite kustom Webuild (sekarang masih sprite The Office bawaan repo)
- [ ] Panel chat → sambung ke Papan Hidup Agent
- [ ] Mode 3D / ruangan bertema Webuild
- [ ] Packaging "setting simpel" buat pengguna luar (produk)

## 🔗 Terkait
- [[03-Proyek/04-Virtual-Office-Visualisasi/README|Proyek 04]]
- [[06-Tim-Agent/Team Registry]] · [[06-Tim-Agent/Papan Hidup Agent]]
- [[08-Infrastruktur/VPS Manifest]]

#proyek #virtual-office #ai #selesai #webuild-office