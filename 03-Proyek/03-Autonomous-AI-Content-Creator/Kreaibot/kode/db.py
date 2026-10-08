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
        self.conn.commit()

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
                   ref_photos: Iterable[str], prompt: str, ratio: str) -> int:
        import json
        cur = self.conn.execute(
            "INSERT INTO jobs (telegram_id, feature, cost, ref_photos, prompt, ratio, created_at, updated_at)"
            " VALUES (?,?,?,?,?,?,?,?)",
            (telegram_id, feature, cost, json.dumps(list(ref_photos)), prompt, ratio, _now(), _now()))
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