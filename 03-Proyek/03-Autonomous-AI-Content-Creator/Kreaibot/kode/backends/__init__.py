"""Interface backend generate + factory.

Semua backend punya kontrak yang sama, jadi kalau nanti mau pindah dari
RunningHub ke fal.ai / MiniMax / GPU sendiri, cukup tambah adapter baru.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol


@dataclass
class GenRequest:
    job_id: int
    feature_key: str
    workflow: str
    photos: list[Path] = field(default_factory=list)
    video_in: Path | None = None
    prompt: str = ""
    ratio: str = "9:16"
    duration: int = 5
    out_path: Path = Path("out.mp4")


@dataclass
class GenStatus:
    state: str                      # queued | running | done | failed
    progress: int = 0               # 0..100
    message: str = ""
    result_path: Path | None = None
    error: str = ""


class Backend(Protocol):
    name: str

    async def submit(self, req: GenRequest) -> str: ...
    async def poll(self, task_id: str) -> GenStatus: ...


def make_backend(kind: str, **kw):
    kind = (kind or "mock").lower()
    if kind == "runninghub":
        from .runninghub import RunningHubBackend
        return RunningHubBackend(**kw)
    if kind == "fal":
        from .fal import FalBackend
        return FalBackend(**kw)
    from .mock import MockBackend
    return MockBackend(**kw)