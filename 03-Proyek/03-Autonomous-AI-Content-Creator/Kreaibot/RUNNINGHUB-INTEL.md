# RunningHub — Intel Akun & Program Earning (dipanen 8 Okt 2026)

## Akun (login BERHASIL via Hermes vault)
| | |
|---|---|
| Nama | **Nimara Official** |
| User ID | `2108050207926067202` |
| Email | marketing.nimara@gmail.com |
| Member | **Personal**, aktif s/d **8 Nov 2026** (sisa 31 hari) |
| **Saldo koin** | **35.694 RH Coins** (36.000 − 269 render 15s − 70 render 5s) |
| Invite code | **`baaxhjzz`** |
| Login | via Hermes vault (`vault_5e4871dcae31`) — password terenkripsi, TIDAK pernah masuk chat |

## 💰 Jalur earning yang ditemukan

### 1. Program Invite RunningHub (aktif, bisa langsung)
- Undang 1 user baru = **500 RH Coins** untuk pengundang **dan** 500 untuk yang diundang
- Link: `https://www.runninghub.ai?inviteCode=baaxhjzz`
- Reward berlaku **372 hari**
- Batas user reguler: **5.000 RH Coins/hari** dari invite
- 🔥 **Mitra promosi (promo partner) TIDAK ADA BATAS** → ada jalur "ajukan diri jadi mitra promosi RH"
- Nilai: 500 koin ≈ Rp2.230 (kurs Rp4,46/koin)

### 2. Creator Growth Program (创作者成长计划) — "Jadi Super Kreator"
3 tingkatan: **Pioneer (先锋) → Benchmark (标杆) → Super (超级)**
- **Pioneer**: dapat **starter compute credits** + s.d. **¥1.000/bulan** kredit komputasi + **pengembalian penuh kredit kanvas** untuk workflow publik yang masuk "pilihan kanvas"
- **Benchmark**: reward per-view + **tugas terbatas (cash floor + reward view)**
- **Super**: reward view + **insentif viral** (tertinggi) + benefit membership
- Masuk jalur: undangan resmi / referral (kini hanya via internal Super) / **pendaftaran mandiri** (ada form resmi)
- Aturan lengkap: https://kcnfnpfw2khn.feishu.cn/wiki/WrcLwqPj0iwE1bkeYdacw3xlnWe

### 3. Kontes AIGC (Chinese Nebula Awards)
- **Global AIGC Feature Film Competition** — hadiah utama s.d. **USD 150.000 cash**
- 3 studio: Sci-Fi / Glimmer / Brand Studio
- ⏰ **Deadline pendaftaran + teaser 2 menit: 9 Okt 2026**
- Tahap 2: film final min. 15 menit, deadline **3 Nov 2026**; pengumuman finalis 12–13 Okt

### 4. ~~Free window untuk member~~ → ⚠️ **KOREKSI 14 OKT 2026: TIDAK BERLAKU BUAT KITA**
- Promo *"13 jam/hari gratis"* itu **spesifik model MiniMax H3 RH Enhanced** — **bukan** workflow/AI App kita.
- Bukti: uji Qwen di "jam gratis" tetap kena **632 koin**; render kita selalu memakai koin.
- Tarif nyata: Qwen-Edit ±50 koin/gambar · motion ±26 koin/detik (16,4 dtk ≈ 431 koin).
- 👉 **Hitung koin dulu sebelum render.** Tidak ada jam yang lebih murah.

## ⚠️ Catatan teknis
- Login dari IP VPS (datacenter Tencent, beda negara): login pertama sempat **drop session** dalam ~1 menit; percobaan kedua **stabil** (bertahan > 40s + navigasi). Kalau drop berulang → pindah ke **proxy residensial** + profil browser persisten.
- Jangan pernah pindahkan password ke repo/vault Obsidian (keduanya push ke GitHub).
- Vault Hermes: `/root/.hermes/vault/vault.json.enc` (terenkripsi) + `vault.key` (mode 600).

## Alat yang dibuat
- `tools/rh_search_app.py` — cari AI App RunningHub pakai API key (tanpa login). Catatan: endpoint `/openapi/v2/aiapp/list` **tidak mendukung keyword** (total selalu 70.508), jadi pencarian app spesifik harus lewat halaman web/Canvas.