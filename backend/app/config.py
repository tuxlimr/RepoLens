"""Environment config. No secrets hardcoded; everything optional for local MVP."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./repolens.db")
    github_token: str | None = os.getenv("GITHUB_TOKEN") or None
    openrouter_api_key: str | None = os.getenv("OPENROUTER_API_KEY") or None
    openrouter_model: str = os.getenv("OPENROUTER_MODEL", "openrouter/free")
    cors_origins: str = os.getenv("CORS_ORIGINS", "http://localhost:3000")
    max_files: int = int(os.getenv("MAX_FILES", "800"))
    max_file_bytes: int = int(os.getenv("MAX_FILE_BYTES", "200000"))
    max_total_bytes: int = int(os.getenv("MAX_TOTAL_BYTES", "8000000"))
    fresh_analysis_price_cents: int = int(os.getenv("FRESH_ANALYSIS_PRICE_CENTS", "900"))


settings = Settings()
