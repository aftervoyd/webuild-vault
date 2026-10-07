# 🎮 Proyek 04 — Virtual Office Visualisasi

> **Status:** ⚪ RENCANA (ide bagus — dikerjakan nanti) · **Divisi:** Produk AI

---

## 💡 Ide

Orang bisa **lihat agentic AI mereka bekerja secara visual** (kayak game) + **kirim perintah** dari tampilan itu, lewat website kita — **setting sesimpel mungkin**.

**Jadi produk:** bukan cuma buat internal Webuild, tapi **ditawarkan ke orang lain** yang mau visualisasi agent AI mereka.

## 🔍 Tool referensi (hasil riset)

| Tool | Catatan |
|---|---|
| ⭐ **myvirtualoffice.ai** | **Support Hermes agents!** — paling relevan |
| **pixel-agents** | Pixel office di browser — cocok akses remote |
| **harishkotra/agent-office** | Tim pixel-art, agent saling kasih tugas (lokal/Ollama) |
| **CLAW3D** | Versi 3D |
| **AgentGUI** | Desktop, drag-and-assign tugas |

## ⚠️ Prinsip Keamanan (WAJIB)

Pelajaran dari VPS lama (ke-lockout port 22):
- Virtual office = **cuma viewer web** — **NGGAK BOLEH** sentuh SSH/UFW/port 22
- Cukup jalankan di **1 port web** (mis. 3000/8080)
- Akses lewat **Tailscale** atau nginx — jangan buka akses baru yang berisiko
- Ikuti prosedur di [[08-Infrastruktur/Prosedur Pemulihan Akses]]

## 📋 Todo (nanti)
- [ ] Pilih tool (mulai dari myvirtualoffice.ai / pixel-agents)
- [ ] Test di VPS di port terpisah
- [ ] Bikin alur "setting simpel" buat pengguna luar
- [ ] Packaging jadi produk

## 🔗 Terkait
- [[01-Bisnis/Webuild - Visi & Roadmap]]
- [[08-Infrastruktur/VPS Manifest]]

#proyek #virtual-office #ai #rencana