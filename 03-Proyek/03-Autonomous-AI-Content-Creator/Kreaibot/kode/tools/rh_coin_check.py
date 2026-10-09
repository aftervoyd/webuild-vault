#!/usr/bin/env python3
"""Cek saldo RH Coins + wallet RunningHub, catat riwayat, dan deteksi klaim harian.

Dipakai oleh cron harian. Tanpa argumen: cetak ringkas + simpan ke rh_coins.csv.
Jalankan:  python3 tools/rh_coin_check.py
"""
from __future__ import annotations

import csv
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV = ROOT / ".env"
LOG = ROOT / "work" / "rh_coins.csv"


def read_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV.exists():
        for line in ENV.read_text().splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def account_status(base: str, key: str) -> dict:
    url = base.rstrip("/") + "/uc/openapi/accountStatus"
    req = urllib.request.Request(
        url, data=json.dumps({"apiKey": key}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())


def main() -> int:
    env = read_env()
    base = env.get("RUNNINGHUB_BASE", "")
    key = env.get("RUNNINGHUB_API_KEY", "")
    if not base or not key:
        print("❌ RUNNINGHUB_BASE / RUNNINGHUB_API_KEY kosong di .env")
        return 1
    try:
        js = account_status(base, key)
    except Exception as e:  # noqa: BLE001
        print(f"❌ gagal panggil RunningHub: {e}")
        return 2
    d = js.get("data") or {}
    coins = d.get("remainCoins", "?")
    money = d.get("remainMoney", "?")
    tasks = d.get("currentTaskCounts", "?")

    # deteksi kenaikan vs baris terakhir
    prev = None
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if LOG.exists():
        rows = list(csv.reader(LOG.read_text().splitlines()))
        for r in reversed(rows[1:]):
            try:
                prev = float(r[1]); break
            except (IndexError, ValueError):
                continue
    delta = ""
    try:
        delta = f"  (Δ {float(coins) - prev:+.0f} vs cek terakhir)" if prev is not None else ""
    except (TypeError, ValueError):
        pass

    stamp = time.strftime("%Y-%m-%d %H:%M")
    print(f"💰 RH Coins: {coins}{delta} · wallet ${money} · tugas jalan: {tasks}  [{stamp}]")

    new = not LOG.exists()
    with LOG.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["waktu", "koin", "wallet_usd", "tugas"])
        w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), coins, money, tasks])
    return 0


if __name__ == "__main__":
    sys.exit(main())