"""Kreaibot — lapisan data (SQLite): user, ledger token, job, voucher."""
from __future__ import annotations

import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    username    TEXT,
    name        TEXT,
    tokens      REAL NOT NULL DEFAULT 0,
    referred_by INTEGER,
    created_at  INTEGER NOT NULL,
    banned      INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS ledger (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    delta       REAL NOT NULL,
    reason      TEXT NOT NULL,
    ref         TEXT,
    created_at  INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS jobs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    feature     TEXT NOT NULL,
    cost        REAL NOT NULL,
    status      TEXT NOT NULL DEFAULT 'queued',   -- queued|running|done|failed|refunded
    task_id     TEXT,
    ref_photos  TEXT,                              -- JSON list file_id
    prompt      TEXT,
    brief       TEXT,
    style       TEXT,
    ratio       TEXT,
    duration    INTEGER,
    result_path TEXT,
    error       TEXT,
    created_at  INTEGER NOT NULL,
    updated_at  INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS vouchers (
    code        TEXT PRIMARY KEY,
    tokens      REAL NOT NULL,
    max_uses    INTEGER NOT NULL DEFAULT 1,
    used        INTEGER NOT NULL DEFAULT 0,
    created_at  INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS referrals (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    inviter_id   INTEGER NOT NULL,
    invitee_id   INTEGER NOT NULL UNIQUE,          -- 1 akun hanya bisa jadi invitee SEKALI seumur hidup
    status       TEXT NOT NULL DEFAULT 'pending',  -- pending | paid | blocked
    invitee_paid INTEGER NOT NULL DEFAULT 0,
    inviter_paid INTEGER NOT NULL DEFAULT 0,
    created_at   INTEGER NOT NULL,
    paid_at      INTEGER
);
CREATE INDEX IF NOT EXISTS idx_ref_inviter ON referrals(inviter_id, status);
CREATE TABLE IF NOT EXISTS payments (
    order_id    TEXT PRIMARY KEY,                    -- order unik kita (idempotensi Aulaa)
    payment_id  TEXT,                                -- id invoice Aulaa
    telegram_id INTEGER NOT NULL,
    amount      INTEGER NOT NULL,                    -- rupiah
    tokens      REAL NOT NULL,                       -- token yg didapat kalau lunas
    status      TEXT NOT NULL DEFAULT 'pending',     -- pending|paid|expired|error
    is_test     INTEGER NOT NULL DEFAULT 0,          -- 1 = transaksi sandbox
    invoice     TEXT,                                -- string QRIS / nomor VA
    note        TEXT,
    created_at  INTEGER NOT NULL,
    paid_at     INTEGER
);
CREATE INDEX IF NOT EXISTS idx_pay_status ON payments(status, created_at);
CREATE TABLE IF NOT EXISTS characters (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    name        TEXT NOT NULL,                      -- nama pilihan user (bebas)
    name_lower  TEXT NOT NULL,                      -- untuk pencocokan case-insensitive
    kind        TEXT NOT NULL DEFAULT 'char',       -- 'char' = karakter · 'produk' = produk (UGC)
    file_id     TEXT NOT NULL,                      -- foto master (file_id Telegram)
    note        TEXT,                               -- catatan pengingat (opsional)
    uses        INTEGER NOT NULL DEFAULT 0,
    created_at  INTEGER NOT NULL,
    UNIQUE(telegram_id, kind, name_lower)           -- 1 user tidak boleh punya 2 nama kembar (per jenis)
);
CREATE INDEX IF NOT EXISTS idx_chars_user ON characters(telegram_id, created_at);
"""


def _now() -> int:
    return int(time.time())


class Database:
    def __init__(self, path: str | Path):
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.executescript(SCHEMA)
        # migrasi ringan: SQLite tak punya "ADD COLUMN IF NOT EXISTS"
        for _sql in ("ALTER TABLE payments ADD COLUMN msg_id INTEGER",   # pesan QR → bisa di-edit jadi LUNAS
                     "ALTER TABLE payments ADD COLUMN chat_id INTEGER",
                     "ALTER TABLE characters ADD COLUMN kind TEXT NOT NULL DEFAULT 'char'"):
            try:
                self.conn.execute(_sql)
            except sqlite3.OperationalError:      # kolom sudah ada
                pass
        self.conn.commit()
        self._migrate()
        self.conn.commit()

    def _migrate(self) -> None:
        """Tambah kolom baru ke DB lama tanpa menghapus data."""
        cols = {r["name"] for r in self.conn.execute("PRAGMA table_info(jobs)")}
        for name, ddl in (("brief", "TEXT"), ("style", "TEXT"), ("duration", "INTEGER")):
            if name not in cols:
                self.conn.execute(f"ALTER TABLE jobs ADD COLUMN {name} {ddl}")

    # ---------- user ----------
    def ensure_user(self, telegram_id: int, username: str = "", name: str = "",
                    signup_bonus: float = 0.0, referred_by: int | None = None) -> sqlite3.Row:
        row = self.get_user(telegram_id)
        if row:
            return row
        self.conn.execute(
            "INSERT INTO users (telegram_id, username, name, tokens, referred_by, created_at)"
            " VALUES (?,?,?,?,?,?)",
            (telegram_id, username or "", name or "", 0.0, referred_by, _now()),
        )
        if signup_bonus:
            self.ledger_add(telegram_id, signup_bonus, "signup_bonus")
        self.conn.commit()
        return self.get_user(telegram_id)  # type: ignore[return-value]

    def get_user(self, telegram_id: int) -> sqlite3.Row | None:
        cur = self.conn.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
        return cur.fetchone()

    def all_users(self) -> list[sqlite3.Row]:
        return list(self.conn.execute("SELECT * FROM users ORDER BY created_at DESC"))

    # ---------- token ----------
    def ledger_add(self, telegram_id: int, delta: float, reason: str, ref: str | None = None) -> float:
        self.conn.execute(
            "UPDATE users SET tokens = tokens + ? WHERE telegram_id=?", (delta, telegram_id))
        self.conn.execute(
            "INSERT INTO ledger (telegram_id, delta, reason, ref, created_at) VALUES (?,?,?,?,?)",
            (telegram_id, delta, reason, ref, _now()))
        self.conn.commit()
        row = self.get_user(telegram_id)
        return float(row["tokens"]) if row else 0.0

    def balance(self, telegram_id: int) -> float:
        row = self.get_user(telegram_id)
        return float(row["tokens"]) if row else 0.0

    def ledger(self, telegram_id: int, limit: int = 10) -> list[sqlite3.Row]:
        return list(self.conn.execute(
            "SELECT * FROM ledger WHERE telegram_id=? ORDER BY id DESC LIMIT ?", (telegram_id, limit)))

    # ---------- job ----------
    def create_job(self, telegram_id: int, feature: str, cost: float,
                   ref_photos: Iterable[str], prompt: str, ratio: str,
                   brief: str = "", style: str = "", duration: int = 0) -> int:
        import json
        cur = self.conn.execute(
            "INSERT INTO jobs (telegram_id, feature, cost, ref_photos, prompt, brief, style, ratio, duration, created_at, updated_at)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (telegram_id, feature, cost, json.dumps(list(ref_photos)), prompt, brief, style,
             ratio, int(duration or 0), _now(), _now()))
        self.conn.commit()
        return int(cur.lastrowid)

    def set_job(self, job_id: int, **fields: Any) -> None:
        if not fields:
            return
        fields["updated_at"] = _now()
        cols = ", ".join(f"{k}=?" for k in fields)
        self.conn.execute(f"UPDATE jobs SET {cols} WHERE id=?", (*fields.values(), job_id))
        self.conn.commit()

    def get_job(self, job_id: int) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()

    def pending_jobs(self) -> list[sqlite3.Row]:
        return list(self.conn.execute(
            "SELECT * FROM jobs WHERE status IN ('queued','running') ORDER BY id"))

    def running_jobs(self) -> list[sqlite3.Row]:
        """Job yang sudah disubmit ke backend tapi belum tuntas.

        Dipakai saat startup: service yang direstart kehilangan loop poll-nya, jadi
        render yang sudah jalan (dan sudah dibayar) harus disambung lagi.
        """
        return list(self.conn.execute(
            "SELECT * FROM jobs WHERE status='running' AND task_id IS NOT NULL "
            "AND task_id<>'' ORDER BY id"))

    # ---------- referral (anti-farming) ----------
    def ref_register(self, inviter_id: int, invitee_id: int) -> bool:
        """Catat invitee (1 akun = 1 kali seumur hidup). False kalau tidak valid/duplikat."""
        if inviter_id <= 0 or inviter_id == invitee_id:
            return False
        if self.conn.execute("SELECT 1 FROM referrals WHERE invitee_id=?", (invitee_id,)).fetchone():
            return False
        self.conn.execute(
            "INSERT INTO referrals (inviter_id, invitee_id, created_at) VALUES (?,?,?)",
            (inviter_id, invitee_id, _now()))
        self.conn.execute("UPDATE users SET referred_by=? WHERE telegram_id=?", (inviter_id, invitee_id))
        self.conn.commit()
        return True

    def ref_get(self, invitee_id: int) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM referrals WHERE invitee_id=?", (invitee_id,)).fetchone()

    def ref_mark(self, invitee_id: int, **f: Any) -> None:
        allowed = {"invitee_paid", "inviter_paid", "status"}
        f = {k: v for k, v in f.items() if k in allowed}
        if not f:
            return
        if f.get("invitee_paid") or f.get("status") == "paid":
            f["paid_at"] = _now()
        cols = ", ".join(f"{k}=?" for k in f)
        self.conn.execute(f"UPDATE referrals SET {cols} WHERE invitee_id=?", (*f.values(), invitee_id))
        self.conn.commit()

    def ref_count_since(self, inviter_id: int, since_ts: int) -> int:
        return int(self.conn.execute(
            "SELECT COUNT(*) n FROM referrals WHERE inviter_id=? AND status='paid' AND created_at>=?",
            (inviter_id, since_ts)).fetchone()["n"])

    def ref_summary(self, inviter_id: int) -> dict[str, Any]:
        c = self.conn
        total = c.execute("SELECT COUNT(*) n FROM referrals WHERE inviter_id=?",
                          (inviter_id,)).fetchone()["n"]
        paid = c.execute("SELECT COUNT(*) n FROM referrals WHERE inviter_id=? AND status='paid'",
                         (inviter_id,)).fetchone()["n"]
        earned = c.execute("SELECT COALESCE(SUM(delta),0) s FROM ledger"
                           " WHERE telegram_id=? AND reason='ref_bonus_inviter'",
                           (inviter_id,)).fetchone()["s"]
        return {"total": int(total), "paid": int(paid), "earned": float(earned)}

    def ref_top(self, limit: int = 10) -> list[sqlite3.Row]:
        return list(self.conn.execute(
            "SELECT inviter_id, COUNT(*) total, SUM(status='paid') paid,"
            " SUM(inviter_paid) paid_inviter FROM referrals"
            " GROUP BY inviter_id ORDER BY total DESC LIMIT ?", (limit,)))

    def ref_pending_inviter(self, invitee_id: int) -> int | None:
        r = self.ref_get(invitee_id)
        if r and r["invitee_paid"] and not r["inviter_paid"]:
            return int(r["inviter_id"])
        return None

    # ---------- pembayaran Aulaa (QRIS) ----------
    def pay_create(self, order_id: str, telegram_id: int, amount: int, tokens: float) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO payments (order_id, telegram_id, amount, tokens, status, created_at)"
            " VALUES (?,?,?,?,'pending',?)",
            (order_id, telegram_id, int(amount), float(tokens), _now()))
        self.conn.commit()

    def pay_set(self, order_id: str, **f: Any) -> None:
        allowed = {"payment_id", "status", "is_test", "invoice", "note", "paid_at", "msg_id", "chat_id"}
        f = {k: v for k, v in f.items() if k in allowed}
        if not f:
            return
        if f.get("status") == "paid":
            f["paid_at"] = _now()
        cols = ", ".join(f"{k}=?" for k in f)
        self.conn.execute(f"UPDATE payments SET {cols} WHERE order_id=?", (*f.values(), order_id))
        self.conn.commit()

    def pay_get(self, order_id: str) -> sqlite3.Row | None:
        return self.conn.execute("SELECT * FROM payments WHERE order_id=?", (order_id,)).fetchone()

    def pay_pending(self, limit: int = 20) -> list[sqlite3.Row]:
        return list(self.conn.execute(
            "SELECT * FROM payments WHERE status='pending' ORDER BY created_at LIMIT ?", (limit,)))

    def pay_mark_paid(self, order_id: str) -> sqlite3.Row | None:
        self.pay_set(order_id, status="paid")
        return self.pay_get(order_id)

    def pay_recent(self, telegram_id: int, limit: int = 5) -> list[sqlite3.Row]:
        return list(self.conn.execute(
            "SELECT * FROM payments WHERE telegram_id=? ORDER BY created_at DESC LIMIT ?",
            (telegram_id, limit)))

    def stats(self) -> dict[str, Any]:
        c = self.conn
        return {
            "users": c.execute("SELECT COUNT(*) n FROM users").fetchone()["n"],
            "jobs": c.execute("SELECT COUNT(*) n FROM jobs").fetchone()["n"],
            "done": c.execute("SELECT COUNT(*) n FROM jobs WHERE status='done'").fetchone()["n"],
            "queued": c.execute("SELECT COUNT(*) n FROM jobs WHERE status='queued'").fetchone()["n"],
            "tokens_spent": c.execute("SELECT COALESCE(SUM(-delta),0) s FROM ledger WHERE delta<0").fetchone()["s"],
        }

    def top_balance(self, limit: int = 10) -> list[sqlite3.Row]:
        return list(self.conn.execute(
            "SELECT telegram_id, tokens FROM users ORDER BY tokens DESC LIMIT ?", (limit,)))

    # ---------------- KARAKTER SAYA (master character sheet) ----------------
    # Ide: user simpan 1 foto master (character sheet) + kasih NAMA sendiri.
    # Nanti di fitur apa pun user tinggal sebut namanya → bot pakai karakter itu
    # secara identik (foto yang SAMA → hasil konsisten antar render).

    def char_save(self, telegram_id: int, name: str, file_id: str,
                  note: str = "", kind: str = "char") -> int | None:
        """Simpan karakter baru. None kalau nama sudah dipakai (biar tidak kembar)."""
        nm = " ".join(str(name or "").split())[:40]
        if not nm or not file_id:
            return None
        try:
            cur = self.conn.execute(
                "INSERT INTO characters (telegram_id, kind, name, name_lower, file_id, note, created_at)"
                " VALUES (?,?,?,?,?,?,?)",
                (telegram_id, kind, nm, nm.lower(), file_id, (note or "")[:120], _now()))
            self.conn.commit()
            return int(cur.lastrowid)
        except sqlite3.IntegrityError:            # nama sudah ada
            return None

    def char_list(self, telegram_id: int, limit: int = 30,
                  kind: str | None = None) -> list[sqlite3.Row]:
        if kind:
            return list(self.conn.execute(
                "SELECT * FROM characters WHERE telegram_id=? AND kind=?"
                " ORDER BY uses DESC, created_at DESC LIMIT ?", (telegram_id, kind, limit)))
        return list(self.conn.execute(
            "SELECT * FROM characters WHERE telegram_id=? ORDER BY uses DESC, created_at DESC LIMIT ?",
            (telegram_id, limit)))

    def char_count(self, telegram_id: int, kind: str | None = None) -> int:
        if kind:
            return int(self.conn.execute(
                "SELECT COUNT(*) n FROM characters WHERE telegram_id=? AND kind=?",
                (telegram_id, kind)).fetchone()["n"])
        return int(self.conn.execute(
            "SELECT COUNT(*) n FROM characters WHERE telegram_id=?", (telegram_id,)).fetchone()["n"])

    def char_get(self, telegram_id: int, name_or_id) -> sqlite3.Row | None:
        """Ambil karakter dari NAMA (case-insensitive) atau dari id numerik."""
        s = str(name_or_id or "").strip()
        if not s:
            return None
        if s.isdigit():
            r = self.conn.execute("SELECT * FROM characters WHERE telegram_id=? AND id=?",
                                  (telegram_id, int(s))).fetchone()
            if r:
                return r
        return self.conn.execute(
            "SELECT * FROM characters WHERE telegram_id=? AND name_lower=? "
            "ORDER BY (kind='char') DESC LIMIT 1",
            (telegram_id, s.lower())).fetchone()

    def char_find_in_text(self, telegram_id: int, text: str,
                          kind: str | None = None) -> sqlite3.Row | None:
        """Cari nama karakter yang DISEBUT di dalam teks bebas user.

        Dipakai supaya user cukup menulis 'bikin video si rina jalan di pantai'
        → bot otomatis memakai character sheet bernama 'si rina'.
        Nama terpanjang dicek lebih dulu (agar 'rina cantik' menang atas 'rina').
        """
        t = f" {(text or '').lower()} "
        if not t.strip():
            return None
        for r in sorted(self.char_list(telegram_id, kind=kind), key=lambda x: -len(x["name_lower"])):
            if f" {r['name_lower']} " in t or f" {r['name_lower']}," in t:
                return r
        return None

    def char_delete(self, telegram_id: int, cid: int) -> bool:
        cur = self.conn.execute("DELETE FROM characters WHERE telegram_id=? AND id=?",
                                (telegram_id, int(cid)))
        self.conn.commit()
        return cur.rowcount > 0

    def char_rename(self, telegram_id: int, cid: int, new_name: str) -> bool:
        nm = " ".join(str(new_name or "").split())[:40]
        if not nm:
            return False
        try:
            cur = self.conn.execute(
                "UPDATE characters SET name=?, name_lower=? WHERE telegram_id=? AND id=?",
                (nm, nm.lower(), telegram_id, int(cid)))
            self.conn.commit()
            return cur.rowcount > 0
        except sqlite3.IntegrityError:
            return False

    def char_bump(self, cid: int) -> None:
        self.conn.execute("UPDATE characters SET uses=uses+1 WHERE id=?", (int(cid),))
        self.conn.commit()