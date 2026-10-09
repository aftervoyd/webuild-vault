"""Storage FSM berbasis SQLite — sesi user TIDAK hilang saat bot di-restart.

MASALAH NYATA (9 Okt 16:13): user memilih fitur di menu, lalu bot di-restart (deploy). aiogram
menyimpan state FSM di RAM (MemoryStorage) → semua sesi hilang → user kirim foto →
"Update is not handled" → **bot diem total** (user merasa bot rusak).

Dengan storage ini, pilih fitur → kirim foto → prompt tetap nyambung walau bot baru restart.
"""
from __future__ import annotations

import asyncio
import json
import sqlite3
import time
from pathlib import Path

from aiogram.fsm.state import State
from aiogram.fsm.storage.base import BaseStorage, StorageKey

_SCHEMA = """CREATE TABLE IF NOT EXISTS fsm (
    k       TEXT PRIMARY KEY,
    state   TEXT,
    data    TEXT,
    updated INTEGER NOT NULL
);"""


class SQLiteStorage(BaseStorage):
    """State FSM di file SQLite (aman restart, tanpa Redis)."""

    def __init__(self, path: str | Path, ttl_days: int = 30) -> None:
        self.path = str(path)
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path) as c:
            c.execute(_SCHEMA)
            c.execute("DELETE FROM fsm WHERE updated < ?",
                      (int(time.time()) - ttl_days * 86400,))     # bersihkan sesi basi

    # ---------- kunci ----------
    @staticmethod
    def _key(key: StorageKey) -> str:
        return ":".join(str(x) for x in (key.bot_id, key.chat_id, key.user_id,
                                         getattr(key, "thread_id", None) or 0,
                                         getattr(key, "destiny", "default")))

    # ---------- operasi sinkron (dijalankan di thread) ----------
    def _set_state(self, k: str, state: str | None) -> None:
        with sqlite3.connect(self.path) as c:
            c.execute("INSERT INTO fsm (k, state, updated) VALUES (?,?,?) "
                      "ON CONFLICT(k) DO UPDATE SET state=excluded.state, updated=excluded.updated",
                      (k, state, int(time.time())))

    def _get_state(self, k: str) -> str | None:
        with sqlite3.connect(self.path) as c:
            r = c.execute("SELECT state FROM fsm WHERE k=?", (k,)).fetchone()
        return r[0] if r else None

    def _set_data(self, k: str, data: dict) -> None:
        js = json.dumps(data, ensure_ascii=False, default=str)
        with sqlite3.connect(self.path) as c:
            c.execute("INSERT INTO fsm (k, data, updated) VALUES (?,?,?) "
                      "ON CONFLICT(k) DO UPDATE SET data=excluded.data, updated=excluded.updated",
                      (k, js, int(time.time())))

    def _get_data(self, k: str) -> dict:
        with sqlite3.connect(self.path) as c:
            r = c.execute("SELECT data FROM fsm WHERE k=?", (k,)).fetchone()
        if not r or not r[0]:
            return {}
        try:
            return json.loads(r[0])
        except Exception:                                   # noqa: BLE001
            return {}

    # ---------- kontrak BaseStorage ----------
    async def set_state(self, key: StorageKey, state=None) -> None:
        st = None
        if isinstance(state, State):
            st = state.state
        elif state:
            st = str(state)
        async with _LOCK:
            await asyncio.to_thread(self._set_state, self._key(key), st)

    async def get_state(self, key: StorageKey) -> str | None:
        async with _LOCK:
            return await asyncio.to_thread(self._get_state, self._key(key))

    async def set_data(self, key: StorageKey, data: dict) -> None:
        async with _LOCK:
            await asyncio.to_thread(self._set_data, self._key(key), dict(data))

    async def get_data(self, key: StorageKey) -> dict:
        async with _LOCK:
            return await asyncio.to_thread(self._get_data, self._key(key))

    async def close(self) -> None:
        return None


_LOCK = asyncio.Lock()