# 🖥️ VPS Manifest — Server Webuild

> Peta lengkap server tempat Webuild dikembangkan. **Update tiap ada perubahan infra.**
> Aturan aman lengkap ada di skill `webuild-server`.

---

## 🧭 Identitas Server

| Item | Nilai |
|---|---|
| **Provider** | Tencent Cloud |
| **OS** | Ubuntu (kernel 7.0.0-30-generic) |
| **CPU** | 2 core |
| **RAM** | ~1.9 GB (+ 2 GB swap) |
| **Disk** | 39 GB (terpakai ~25%) |
| **Tailscale IP** | `100.115.213.21` (vm-0-17-ubuntu) |
| **SSH** | port **22** (default) |
| **Firewall UFW** | **inactive** ✅ |

---

## 🔑 Akses — 2 Jalur (biar nggak ke-lockout)

| Jalur | Cara | Catatan |
|---|---|---|
| **SSH publik** | `ssh root@<IP-publik>` port 22 | Jalur utama |
| **Tailscale SSH** ✅ | `ssh root@100.115.213.21` | **Cadangan** — jalan walau port 22 diblok |
| **PC user** | Tailscale `100.110.88.8` (Windows `desktop-t6ia4sj`) | — |
| **Terakhir** | Tencent Cloud Console → **VNC** | Nggak bisa dikunci |

---

## 📦 Yang Terpasang / Jalan

- **Hermes Agent** — gateway Telegram (config di `/root/.hermes`)
- **Vault Obsidian Webuild** — `/root/Documents/Webuild` (git → GitHub `aftervoyd/webuild-vault`)
- **Tailscale** — mesh VPN (server + PC)
- *(rencana)* **Virtual Office web app** → [[03-Proyek/04-Virtual-Office-Visualisasi/README|Proyek 4]]

---

## 🔌 Port Terpakai

| Port | Service |
|---|---|
| `22` | SSH |
| `53` | systemd-resolved (DNS lokal) |
| acak | Tailscale (wireguard) |

---

## ⚙️ Config Penting

| Setting | Nilai |
|---|---|
| Model utama | Inferhub — `ali/deepseek-v4.1-flash` |
| Fallback provider | OmoApicall — `deepseek-v4-flash` (otomatis kalau utama error) |
| Backup config | `/root/.hermes/config.yaml.bak.*` |

---

## 🔗 Terkait
- [[08-Infrastruktur/Prosedur Pemulihan Akses|Prosedur Pemulihan Akses]]
- [[06-Tim-Agent/Team Registry]]
- [[README|Vault Index]]

#infrastruktur #vps