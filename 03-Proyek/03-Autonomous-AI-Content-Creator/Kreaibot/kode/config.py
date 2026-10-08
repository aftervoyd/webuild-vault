"""Kreaibot — konfigurasi terpusat (semua dari environment / .env)."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:  # dotenv opsional
    pass

BASE_DIR = Path(__file__).resolve().parent


def _env(key: str, default: str = "") -> str:
    return (os.getenv(key) or default).strip()


def _env_int(key: str, default: int) -> int:
    try:
        return int(_env(key, str(default)))
    except ValueError:
        return default


def _env_float(key: str, default: float) -> float:
    try:
        return float(_env(key, str(default)))
    except ValueError:
        return default


def _env_bool(key: str, default: bool = False) -> bool:
    return _env(key, "1" if default else "0").lower() in ("1", "true", "yes", "on")


@dataclass
class Settings:
    # === Telegram ===
    bot_token: str = _env("KREAIBOT_TOKEN")
    admin_ids: list[int] = field(default_factory=lambda: [
        int(x) for x in _env("KREAIBOT_ADMIN_IDS", "8886993492").replace(" ", "").split(",") if x
    ])
    bot_name: str = _env("KREAIBOT_NAME", "Kreaibot")

    # === Ekonomi token ===
    tokens_per_10k: int = _env_int("KREAIBOT_TOKENS_PER_10K", 10)   # Rp10.000 = 10 token
    harga_per_10k: int = _env_int("KREAIBOT_HARGA_10K", 10_000)
    signup_bonus: int = _env_int("KREAIBOT_SIGNUP_BONUS", 1)

    # === Backend generate (pluggable) ===
    backend: str = _env("KREAIBOT_BACKEND", "mock")                 # mock | runninghub | fal | minimax
    runninghub_api_key: str = _env("RUNNINGHUB_API_KEY")
    runninghub_base: str = _env("RUNNINGHUB_BASE", "https://www.runninghub.ai")
    fal_key: str = _env("FAL_KEY")
    minimax_key: str = _env("MINIMAX_API_KEY")

    # === Pembayaran QRIS (stub) ===
    payment_provider: str = _env("KREAIBOT_PAYMENT", "manual")      # manual | midtrans | xendit | mayar
    pay_info: str = _env(
        "KREAIBOT_PAY_INFO",
        "💳 QRIS / transfer ke admin — tulis detail pembayaran di .env (KREAIBOT_PAY_INFO)")
    midtrans_server_key: str = _env("MIDTRANS_SERVER_KEY")
    xendit_secret_key: str = _env("XENDIT_SECRET_KEY")
    aulaa_api_key: str = _env("AULAA_API_KEY")
    aulaa_base: str = _env("AULAA_BASE", "https://api.aulaa.co/v1")
    aulaa_pay_base: str = _env("AULAA_PAY_BASE", "https://payment.aulaa.co")
    aulaa_project_id: str = _env("AULAA_PROJECT_ID")
    aulaa_webhook_secret: str = _env("AULAA_WEBHOOK_SECRET")
    aulaa_method: str = _env("AULAA_METHOD", "qris")       # qris | bca_va | ... (kosong = pembeli pilih sendiri)
    aulaa_redirect: str = _env("AULAA_REDIRECT", "")       # URL setelah pembayaran berhasil (opsional)

    # === Referral & channel komunitas (anti-farming) ===
    channel: str = _env("KREAIBOT_CHANNEL")                  # username channel TANPA @ (kosong = gate nonaktif)
    channel_title: str = _env("KREAIBOT_CHANNEL_TITLE", "Kreativ Community")
    channel_link: str = _env("KREAIBOT_CHANNEL_LINK", "https://t.me/kreativcommunity")
    ref_invitee: float = _env_float("KREAIBOT_REF_INVITEE", 2.5)
    ref_inviter: float = _env_float("KREAIBOT_REF_INVITER", 1.5)
    ref_max_day: int = _env_int("KREAIBOT_REF_MAX_DAY", 10)
    ref_max_month: int = _env_int("KREAIBOT_REF_MAX_MONTH", 30)
    ref_inviter_after_purchase: bool = _env_bool("KREAIBOT_REF_INVITER_AFTER_PURCHASE", False)

    # === PromptSmith (perakit prompt UGC) ===
    # Kalau diisi, prompt dirapikan lagi oleh LLM. Kosong → pakai template offline (tetap jalan).
    promptsmith_base: str = _env("PROMPTSMITH_BASE_URL")
    promptsmith_key: str = _env("PROMPTSMITH_API_KEY")
    promptsmith_model: str = _env("PROMPTSMITH_MODEL")

    # === Storage / sistem ===
    db_path: str = _env("KREAIBOT_DB", str(BASE_DIR / "kreaibot.sqlite3"))
    work_dir: str = _env("KREAIBOT_WORK", str(BASE_DIR / "work"))
    concurrency: int = _env_int("KREAIBOT_CONCURRENCY", 3)
    poll_interval: int = _env_int("KREAIBOT_POLL_INTERVAL", 5)
    job_timeout: int = _env_int("KREAIBOT_JOB_TIMEOUT", 900)

    def ensure_dirs(self) -> None:
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)

    def validate(self) -> list[str]:
        errs: list[str] = []
        if not self.bot_token:
            errs.append("KREAIBOT_TOKEN belum diisi (dari @BotFather)")
        if self.backend == "runninghub" and not self.runninghub_api_key:
            errs.append("BACKEND=runninghub tapi RUNNINGHUB_API_KEY kosong")
        if self.backend == "fal" and not self.fal_key:
            errs.append("BACKEND=fal tapi FAL_KEY kosong")
        return errs


settings = Settings()