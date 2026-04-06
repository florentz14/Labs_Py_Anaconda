"""SQLAlchemy: carga `.env` y expone DATABASE_URL (SQLite o PostgreSQL)."""

from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import quote_plus

from dotenv import load_dotenv

_REPO_ROOT = Path(__file__).resolve().parent
load_dotenv(_REPO_ROOT / ".env")

_default_sqlite = _REPO_ROOT / "data" / "sql" / "school.db"


def _postgres_url_from_env() -> str:
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "")
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    db = os.environ.get("POSTGRES_DB", "postgres")
    u = quote_plus(user)
    p = quote_plus(password) if password else None
    auth = f"{u}:{p}@" if p is not None else f"{u}@"
    return f"postgresql+psycopg://{auth}{host}:{port}/{db}"


def _resolve_database_url() -> str:
    explicit = os.environ.get("DATABASE_URL", "").strip()
    if explicit:
        return explicit
    backend = os.environ.get("DB_BACKEND", "sqlite").lower()
    if backend in ("postgresql", "postgres", "pg"):
        return _postgres_url_from_env()
    return "sqlite:///" + _default_sqlite.resolve().as_posix()


DATABASE_URL = _resolve_database_url()

if __name__ == "__main__":
    print("DATABASE_URL =", DATABASE_URL)
