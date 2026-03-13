"""Environment-backed application settings."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_version: str
    app_env: str
    api_prefix: str
    host: str
    port: int
    log_level: str
    default_realm: str
    default_origin_host: str
    default_origin_realm: str


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings(
        app_name=os.getenv("APP_NAME", "VoIP Diameter Simulator"),
        app_version=os.getenv("APP_VERSION", "0.1.0"),
        app_env=os.getenv("APP_ENV", "development"),
        api_prefix=os.getenv("API_PREFIX", "/api/v1"),
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", "8001")),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        default_realm=os.getenv("DEFAULT_REALM", "ims.local"),
        default_origin_host=os.getenv("DEFAULT_ORIGIN_HOST", "simulator.ims.local"),
        default_origin_realm=os.getenv("DEFAULT_ORIGIN_REALM", "ims.local"),
    )
