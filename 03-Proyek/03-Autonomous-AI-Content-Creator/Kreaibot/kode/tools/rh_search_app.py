#!/usr/bin/env python3
"""Cari AI Application di RunningHub pakai API KEY saja (tanpa login web).

Pakai: .venv/bin/python tools/rh_search_app.py "minimax h3"
       .venv/bin/python tools/rh_search_app.py --host https://www.runninghub.ai "h3 reference"
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dotenv import load_dotenv  # type: ignore  # noqa: E402

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
KEY = os.getenv("RUNNINGHUB_API_KEY", "")
PATH_LIST = "/openapi/v2/aiapp/list"


def call(host: str, payload: dict) -> dict:
    url = f"{host}{PATH_LIST}"
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(payload, f)
        tmp = f.name
    try:
        out = subprocess.run(
            ["curl", "-sS", "--max-time", "40", "-X", "POST", url,
             "-H", f"Authorization: Bearer {KEY}",
             "-H", "Content-Type: application/json",
             "-d", f"@{tmp}"],
            capture_output=True, text=True).stdout
    finally:
        os.unlink(tmp)
    try:
        return json.loads(out)
    except Exception:
        return {"_raw": out[:400]}


def app_id(rec: dict) -> str:
    """ID app ada di dalam invokeExample (…/run/ai-app/<id>), bukan field terpisah."""
    import re
    ex = str(rec.get("invokeExample") or "")
    m = re.search(r"/ai-app/(\d+)", ex)
    if m:
        return m.group(1)
    for k in ("id", "webappId", "appId", "app_id"):
        if rec.get(k):
            return str(rec[k])
    return ""


def main() -> int:
    args = [a for a in sys.argv[1:]]
    host = "https://www.runninghub.ai"
    if "--host" in args:
        i = args.index("--host")
        host = args[i + 1]
        del args[i:i + 2]
    kw = " ".join(args).strip().lower()

    if not KEY:
        print("❌ RUNNINGHUB_API_KEY kosong di .env")
        return 2

    records: list[dict] = []
    for page in (1, 2, 3):
        for payload in ({"current": page, "size": 50, "sort": "RECOMMEND"},
                        {"current": page, "size": 50, "sort": "HOTTEST", "days": 30}):
            r = call(host, payload)
            data = r.get("data") or {}
            recs = data.get("records") or data.get("list") or []
            records += recs
            if not recs:
                print(f"   (host={host} page={page} → {r.get('code')} {str(r.get('msg'))[:70]} "
                      f"keys={list(data)[:5] if isinstance(data, dict) else '-'})")
    # dedupe
    seen, uniq = set(), []
    for r in records:
        rid = app_id(r)
        if rid and rid not in seen:
            seen.add(rid)
            uniq.append(r)
    print(f"total app terbaca: {len(uniq)} (host={host})")

    def blob(r: dict) -> str:
        return " ".join(str(r.get(k, "")) for k in
                        ("name", "title", "appName", "description", "remark", "tags", "webappName")).lower()

    hits = [r for r in uniq if kw and all(w in blob(r) for w in kw.split())] if kw else uniq[:12]
    print(f"cocok '{kw}': {len(hits)}\n")
    for r in hits[:12]:
        print("──", r.get("name") or r.get("title") or r.get("appName"),
              "| id:", r.get("id") or r.get("webappId") or r.get("appId"))
        ex = r.get("invokeExample") or r.get("invoke_example") or ""
        if ex:
            print("   contoh panggil:", str(ex)[:300].replace("\n", " "))
        for k in ("description", "remark", "tags"):
            if r.get(k):
                print(f"   {k}: {str(r[k])[:160]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())