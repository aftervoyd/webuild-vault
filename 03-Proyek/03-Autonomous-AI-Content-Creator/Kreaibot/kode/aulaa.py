"""Klien Aulaa (payment gateway QRIS / VA / e-wallet) untuk Kreaibot.

Dokumentasi: https://aulaa.co/dokumentasi
Base URL   : https://api.aulaa.co/v1        (HTTPS, JSON, Bearer token)
Auth       : header `Authorization: Bearer pgw_id_...`
Model      : server-to-server; status pembayaran dicek lewat GET /v1/payments/{id}
             (webhook opsional — kita pakai polling supaya server tidak perlu publik)
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import aiohttp

log = logging.getLogger("kreaibot.aulaa")


class AulaaError(RuntimeError):
    def __init__(self, msg: str, status: int = 0, payload: dict | None = None):
        super().__init__(msg)
        self.status = status
        self.payload = payload or {}


@dataclass
class Payment:
    id: str
    order_id: str
    status: str
    amount: int
    method: str
    number: str          # string QRIS (di-render jadi QR) / nomor VA
    expired_at: str
    is_test: bool
    raw: dict

    @property
    def paid(self) -> bool:
        return self.status in ("paid", "settled", "success")

    @property
    def dead(self) -> bool:
        return self.status in ("expired", "cancelled", "canceled", "failed")


class Aulaa:
    def __init__(self, api_key: str, base: str = "https://api.aulaa.co/v1",
                 pay_base: str = "https://payment.aulaa.co", timeout: int = 30):
        self.key = (api_key or "").strip()
        self.base = base.rstrip("/")
        self.pay_base = pay_base.rstrip("/")
        self.timeout = timeout

    # ---------- internal ----------
    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.key}", "Content-Type": "application/json",
                "Accept": "application/json"}

    async def _req(self, method: str, path: str, payload: dict | None = None) -> dict:
        url = f"{self.base}{path}"
        to = aiohttp.ClientTimeout(total=self.timeout)
        async with aiohttp.ClientSession(timeout=to) as s:
            async with s.request(method, url, json=payload, headers=self._headers()) as r:
                txt = await r.text()
                try:
                    data: Any = json.loads(txt) if txt else {}
                except Exception:
                    data = {"_raw": txt[:400]}
                if r.status >= 400:
                    msg = ""
                    if isinstance(data, dict):
                        msg = str(data.get("error") or data.get("message") or data.get("msg") or "")
                        if not msg:
                            msg = str(data.get("errors") or txt[:200])
                    raise AulaaError(f"HTTP {r.status}: {msg}", status=r.status,
                                     payload=data if isinstance(data, dict) else {})
                return data if isinstance(data, dict) else {"_raw": data}

    # ---------- API ----------
    async def methods(self) -> list[dict]:
        d = await self._req("GET", "/payments/methods")
        return list(d.get("methods") or [])

    async def create(self, order_id: str, amount: int, method: str | None = "qris",
                     redirect_url: str | None = None) -> Payment:
        body: dict[str, Any] = {"order_id": order_id, "amount": int(amount)}
        if method:
            body["payment_method"] = method
        if redirect_url:
            body["redirect_url"] = redirect_url
        try:
            d = await self._req("POST", "/payments", body)
        except AulaaError as e:
            # order_id sudah pernah dibuat (409) → lanjutkan sesi lama, jangan buat baru
            pid = _extract_id(e.payload) or _extract_id(str(e))
            if e.status == 409 and pid:
                log.info("order_id %s sudah ada → ambil status payment %s", order_id, pid)
                return await self.get(pid)
            raise
        return _to_payment(d)

    async def get(self, pid: str) -> Payment:
        d = await self._req("GET", f"/payments/{pid}")
        return _to_payment(d.get("data") if isinstance(d.get("data"), dict) else d)

    async def cancel(self, pid: str) -> dict:
        return await self._req("POST", f"/payments/{pid}/cancel")

    # ---------- UX ----------
    def pay_url(self, pid: str) -> str:
        """Halaman pembayaran terhosting (pembeli bisa pilih metode sendiri)."""
        return f"{self.pay_base}/pay/{pid}"

    @staticmethod
    def qr_png(payload: str, out: str | Path, scale: int = 9) -> Path:
        """Render string QRIS jadi PNG (paket `segno`, murni Python, tanpa dependensi)."""
        import segno
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        segno.make(payload, error="m").save(str(out), scale=scale, border=3,
                                            dark="#0B1220", light="#FFFFFF")
        return out


def _extract_id(payload: Any) -> str | None:
    """Cari UUID payment di berbagai bentuk respons (termasuk pesan error 409)."""
    import re
    txt = payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False)
    m = re.search(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", txt or "")
    return m.group(0) if m else None


def _to_payment(d: dict) -> Payment:
    return Payment(
        id=str(d.get("id") or d.get("payment_id") or ""),
        order_id=str(d.get("order_id") or ""),
        status=str(d.get("status") or "pending").lower(),
        amount=int(d.get("amount") or 0),
        method=str(d.get("payment_method") or ""),
        number=str(d.get("payment_number") or d.get("payment_code") or d.get("qr_string") or ""),
        expired_at=str(d.get("expired_at") or ""),
        is_test=bool(d.get("is_test")),
        raw=d,
    )


def make_client(settings) -> "Aulaa | None":
    """Bikin klien kalau kredensial Aulaa sudah diisi di .env."""
    if not getattr(settings, "aulaa_api_key", ""):
        return None
    return Aulaa(settings.aulaa_api_key, settings.aulaa_base, settings.aulaa_pay_base)