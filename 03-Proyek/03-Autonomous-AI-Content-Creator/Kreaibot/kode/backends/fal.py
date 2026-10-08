"""fal.ai adapter (opsional) — alternatif RunningHub untuk model seperti MiniMax/Hailuo, LTX, dll."""
from __future__ import annotations

import asyncio
import os
from pathlib import Path

import aiohttp

from . import GenRequest, GenStatus

QUEUE = "https://queue.fal.run"


class FalBackend:
    name = "fal"

    def __init__(self, api_key: str = "", work_dir: str = ".", **_: object):
        self.api_key = api_key or os.getenv("FAL_KEY", "")
        self.work_dir = Path(work_dir)

    def _model(self, feature_key: str) -> str:
        # contoh: FAL_MODEL_ALLINONE=minimax/hailuo-03/image-to-video
        return os.getenv(f"FAL_MODEL_{feature_key.upper()}", "")

    @property
    def _headers(self) -> dict:
        return {"Authorization": f"Key {self.api_key}", "Content-Type": "application/json"}

    async def submit(self, req: GenRequest) -> str:
        model = self._model(req.feature_key)
        if not model:
            raise RuntimeError(f"FAL_MODEL_{req.feature_key.upper()} belum diisi")
        payload = {"prompt": req.prompt, "aspect_ratio": req.ratio}
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=120)) as s:
            async with s.post(f"{QUEUE}/{model}", json=payload, headers=self._headers) as r:
                js = await r.json(content_type=None)
        return str(js.get("request_id", ""))

    async def poll(self, task_id: str) -> GenStatus:
        # status endpoint butuh model; gunakan prefix yang sama saat submit lewat penyimpanan sederhana
        return GenStatus(state="running", progress=50,
                         message="polling fal.ai (isi FAL_MODEL_* & sesuaikan poll)")