# Program Referral Kreea.ai — Desain Anti-Farming

**Status: LIVE di bot** (`@kreeaibot`) sejak 8 Okt 2026 · tes: 40/40 selftest + 10/10 E2E referral

## Bonus
| Pihak | Bonus | Kapan cair |
|---|---|---|
| **Yang diundang** (invitee) | **2,5 Token** | setelah join channel komunitas |
| **Yang mengundang** (inviter) | **1,5 Token** | setelah invitee klaim (atau setelah invitee top up pertama, kalau mode aman aktif) |

Link undangan: `https://t.me/kreeaibot?start=ref_<telegram_id>`
(menu **👥 Referral** menampilkan link + statistik + tombol bagikan)

## 5 lapis anti-farming
1. **1 akun Telegram = 1 bonus invitee, seumur hidup.**
   DB: `referrals.invitee_id` UNIQUE. Klik link 2×, 10×, atau dari 10 pengundang berbeda → tetap 1× bayar.
2. **Wajib join channel komunitas** untuk klaim.
   Telegram = akun ber-nomor HP, jadi bikin 100 akun palsu butuh 100 nomor HP = mahal. Dicek asli via
   `getChatMember` (bot harus admin di channel).
3. **Cap per pengundang**: maksimum **10 bonus/hari** dan **30 bonus/30 hari** (default).
   Kalau kena cap, bonus **ditahan** (tidak hilang — `inviter_paid` tetap 0, bisa dibayar manual).
4. **Self-referral ditolak** (`inviter_id == invitee_id`) dan invitee lama/non-baru tidak diberi bonus.
5. **Mode aman opsional** (`KREAIBOT_REF_INVITER_AFTER_PURCHASE=1`): bonus pengundang baru cair
   setelah invitee **top up pertama** → farming jadi tidak berguna (harus bayar uang beneran).

## Konfigurasi (.env)
```
KREAIBOT_CHANNEL=              # username channel TANPA @ — kosong = gate join nonaktif
KREAIBOT_CHANNEL_TITLE=Kreativ Community
KREAIBOT_CHANNEL_LINK=https://t.me/kreativcommunity
KREAIBOT_REF_INVITEE=2.5
KREAIBOT_REF_INVITER=1.5
KREAIBOT_REF_MAX_DAY=10
KREAIBOT_REF_MAX_MONTH=30
KREAIBOT_REF_INVITER_AFTER_PURCHASE=0
```

## Yang perlu disiapkan di Telegram (manual, sekali)
1. Buat channel publik **Kreativ Community** (username mis. `@kreativcommunity`).
2. Tambahkan **@kreeaibot** sebagai **admin** channel (wajib, supaya bot bisa cek keanggotaan).
3. Isi `KREAIBOT_CHANNEL` di `.env` = username channel (tanpa `@`) → restart service.

## Alat admin
- `/refstats` — daftar pengundang teratas + jumlah undangan/cair (deteksi farming).
- Audit: tabel `referrals` + `ledger` (`reason='ref_bonus_invitee'` / `'ref_bonus_inviter'`).
- Revoke: `/take <id> <token>` (kurangi saldo) atau tandai `status='blocked'`.

## Uji
- `python3 selftest.py` — 12 tes referral (DB: duplikat, self-ref, cap, rekap).
- `python3 tools/ref_e2e.py` — 10 tes E2E memanggil handler asli `/start ref_<id>`
  (pakai DB terisolasi `/tmp/reftest.sqlite3`, DB produksi tidak tersentuh).