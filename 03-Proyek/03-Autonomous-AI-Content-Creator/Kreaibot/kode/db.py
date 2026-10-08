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
        self._migrate()
        self.conn.commit()

    def _migrate(self) -> None:
        """Tambah kolom baru ke DB lama tanpa menghapus data."""
        cols = {r["name"] for r in self.conn.execute("PRAGMA table_info(jobs)")}
        for name, ddl in (("brief", "TEXT"), ("style", "TEXT")):
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
                   brief: str = "", style: str = "") -> int:
        import json
        cur = self.conn.execute(
            "INSERT INTO jobs (telegram_id, feature, cost, ref_photos, prompt, brief, style, ratio, created_at, updated_at)"
            " VALUES (?,?,?,?,?,?,?,?,?,?)",
            (telegram_id, feature, cost, json.dumps(list(ref_photos)), prompt, brief, style, ratio, _now(), _now()))
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