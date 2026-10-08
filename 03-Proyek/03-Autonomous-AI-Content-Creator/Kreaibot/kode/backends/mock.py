"""MockBackend — bikin video uji lokal pakai ffmpeg (buat dev tanpa biaya API)."""
from __future__ import annotations

import asyncio
import subprocess
import uuid
from pathlib import Path

from . import GenRequest, GenStatus


class MockBackend:
    name = "mock"

    def __init__(self, work_dir: str = ".", **_: object):
        self.work_dir = Path(work_dir)
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self._tasks: dict[str, GenRequest] = {}

    async def submit(self, req: GenRequest) -> str:
        tid = "mock-" + uuid.uuid4().hex[:12]
        self._tasks[tid] = req
        return tid

    async def poll(self, task_id: str) -> GenStatus:
        req = self._tasks.get(task_id)
        if not req:
            return GenStatus(state="failed", error="task tidak dikenal")
        out = req.out_path
        if out.exists():
            return GenStatus(state="done", progress=100, result_path=out, message="selesai (mock)")

        # video uji: 5 detik pakai testsrc2 (tanpa font/drawtext → tahan di server minimal)
        size = "720x1280" if req.ratio == "9:16" else ("1280x720" if req.ratio == "16:9" else "720x720")
        cmd = [
            "ffmpeg", "-y", "-f", "lavfi", "-i", f"testsrc2=size={size}:rate=24:duration=5",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out),
        ]
        try:
            await asyncio.to_thread(subprocess.run, cmd, check=True,
                                    capture_output=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"ffmpeg gagal: {e.stderr.decode()[-300:]}") from e
        except FileNotFoundError as e:
            raise RuntimeError("ffmpeg tidak terpasang di server") from e
        return GenStatus(state="done", progress=100, result_path=out, message="selesai (mock)")