# ------------------------------------------------------------ #
# File: init_school_db.py
# Date: 2026-03-29
# Author: Florentino
# Description: Build data/sql_files/school.db from schema and seed SQL files.
# ------------------------------------------------------------ #

from __future__ import annotations

import sqlite3

from settings import SCHOOL_DB_PATH, SQL_PATH

DB_FILE = SCHOOL_DB_PATH
SCHEMA_SQL = SQL_PATH / "school_schema.sql"
SEED_SQL = SQL_PATH / "school_seed.sql"


def _run_script(conn: sqlite3.Connection, path: str) -> None:
    with open(path, encoding="utf-8") as f:
        conn.executescript(f.read())


def main() -> None:
    if not SCHEMA_SQL.is_file() or not SEED_SQL.is_file():
        raise FileNotFoundError(f"Missing {SCHEMA_SQL.name} or {SEED_SQL.name} under {SQL_PATH}")

    if DB_FILE.is_file():
        DB_FILE.unlink()

    conn = sqlite3.connect(DB_FILE)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        _run_script(conn, str(SCHEMA_SQL))
        _run_script(conn, str(SEED_SQL))
        conn.commit()
    finally:
        conn.close()

    print(f"Created {DB_FILE.resolve()}")


if __name__ == "__main__":
    main()
