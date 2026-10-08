#!/usr/bin/env python3
"""Pulihkan job yang nyangkut: render sudah jadi di backend, tapi video belum terkirim.

Kasus nyata: service direstart saat render masih jalan → poll terputus → user tidak
pernah menerima video (padahal koin/koin RunningHub sudah terpakai).

Pakai: .venv/bin/python tools/deliver_job.py <job_id>
"""
from __future__ import annotations

import asyncio
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv                       # noqa: E402

load_dotenv(ROOT / ".env")

import catalog                                       # noqa: E402
import db as dbmod                                   # noqa: E402
from aiogram import Bot                              # noqa: E402
from aiogram.client.default import DefaultBotProperties  # noqa: E402
from aiogram.enums import ParseMode                  # noqa: E402
from aiogram.types import FSInputFile                # noqa: E402
from backends import make_backend                    # noqa: E402
from config import settings                          # noqa: E402

db = dbmod.Database(settings.db_path)                # type: ignore[attr-defined]


async def main() -> int:
    job_id = int(sys.argv[1])
    job = db.get_job(job_id)
    if not job:
        print(f"❌ job {job_id} tidak ada di DB")
        return 1
    if job["status"] != "running":
        print(f"ℹ️ job {job_id} status='{job['status']}' — hanya 'running' yang perlu dipulihkan")
        return 0
    task_id = job["task_id"] or ""
    if not task_id or task_id.startswith("mock"):
        print(f"❌ job {job_id} tidak punya taskId nyata ({task_id!r})")
        return 1

    f = catalog.get(job["feature"])
    out = Path(settings.work_dir) / f"job_{job_id}" / "hasil.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)
    be = make_backend(settings.backend, api_key=settings.runninghub_api_key,
                      base=settings.runninghub_base, work_dir=settings.work_dir)
    bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    print(f"▶️ pulihkan job {job_id} · task {task_id} · fitur {job['feature']}")
    try:
        t0 = time.time()
        while True:
            st = await be.poll(task_id)
            el = int(time.time() - t0)
            print(f"   t+{el:4d}s {st.state} · {(st.message or st.error)[:90]}", flush=True)
            if st.state in ("done", "failed"):
                break
            if el > 2700:
                print("   ⏰ melewati 45 menit — hentikan")
                return 1
            await asyncio.sleep(settings.poll_interval)
        if st.state == "failed":
            db.set_job(job_id, status="failed", error=str(st.error)[:400])
            if f:
                db.ledger_add(job["telegram_id"], f.cost, "refund", ref=str(job_id))
            await bot.send_message(int(job["telegram_id"]),
                                   f"❌ Render job <code>{job_id}</code> gagal & Token dikembalikan.")
            print("   ↩️ refund + kabari user")
            return 2
        rp = str(st.result_path or "")
        if rp.startswith("http"):
            urllib.request.urlretrieve(rp, out)
        result = out if out.exists() else Path(rp)
        db.set_job(job_id, status="done", result_path=str(result))
        await bot.send_video(int(job["telegram_id"]), FSInputFile(result),
                             caption=(f"✨ <b>{f.label if f else job['feature']}</b> selesai tanpa watermark!\n"
                                      f"🆔 Job <code>{job_id}</code> (dipulihkan otomatis)"),
                             parse_mode=ParseMode.HTML)
        print(f"   ✅ terkirim ke {job['telegram_id']} · {result} ({result.stat().st_size} byte)")
        return 0
    finally:
        await bot.session.close()


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))