# Data Science Python Environment

This repository is a local workspace for Python data science libraries and experiments.

## Table of Contents

- [About](#about)
- [Repository layout](#repository-layout)
- [Clone the Repository](#clone-the-repository)
- [Download for Windows/Linux/macOS](#download-for-windowslinuxmacos)
- [Setup (Conda or pip)](#setup-conda-or-pip)
- [Usage](#usage)
- [Database configuration](#database-configuration)
- [Environment variables](#environment-variables)
- [How to Contribute](#how-to-contribute)
- [Branch and Pull Request Workflow](#branch-and-pull-request-workflow)

## About

This project contains Python scripts, sample data under `data/`, and experiments with libraries such as Pandas, Matplotlib, NumPy, and SQLAlchemy.

## Repository layout

| Path | Purpose |
|------|---------|
| `classes/` | Object-oriented Python examples |
| `data/csv`, `data/json`, `data/text` | Sample datasets for labs |
| `data/sql/` | SQLite schema, seed SQL, generated `school.db` (not committed) |
| `files/` | Small I/O scripts (`read_text.py`, `read_people.py`) |
| `matplotlib/`, `numpy/`, `pandas/` | Topic examples |
| `tests/` | Pytest tests |
| `database.py` | SQLAlchemy engine using `settings.DATABASE_URL` |
| `init_school_db.py` | Builds `data/sql/school.db` from SQL files |
| `settings.py` | Loads `.env` and resolves `DATABASE_URL` (SQLite or PostgreSQL) |
| `environment.yml` | Minimal Conda spec to recreate the lab environment |

## Clone the Repository

```bash
git clone https://github.com/florentz14/Labs_Py_Anaconda.git
cd Labs_Py_Anaconda
```

Update from remote:

```bash
git pull origin main
```

## Download for Windows/Linux/macOS

1. Install Git: [Windows](https://git-scm.com/download/win), [macOS](https://git-scm.com/download/mac), or on Debian/Ubuntu `sudo apt install git`, Fedora `sudo dnf install git`.
2. Clone (same command on all OS):

```bash
git clone https://github.com/florentz14/Labs_Py_Anaconda.git
cd Labs_Py_Anaconda
```

3. Optional: GitHub **Code → Download ZIP**, then extract.

## Setup (Conda or pip)

**Option A — from `environment.yml` (recommended):**

```bash
conda env create -f environment.yml
conda activate labs_py
```

**Option B — manual Conda env:**

```bash
conda create -n ds-env python=3.11 -y
conda activate ds-env
conda install -c conda-forge jupyter ipykernel sqlalchemy python-dotenv numpy pandas matplotlib seaborn pytest -y
pip install psycopg
```

`psycopg` is the PostgreSQL driver for SQLAlchemy URLs like `postgresql+psycopg://...` (already included in `environment.yml` via pip).

## Usage

1. Copy environment template and adjust values:

```bash
cp .env.example .env
```

2. Initialize the SQLite school database from schema + seed:

```bash
python init_school_db.py
```

This creates `data/sql/school.db` from:

- `data/sql/school_schema.sql`
- `data/sql/school_seed.sql`

3. Test the database connection:

```bash
python database.py
```

4. Example file readers (run from anywhere; paths are resolved from each script’s location):

```bash
python files/read_text.py
python files/read_people.py
```

5. Start Jupyter from the repository root:

```bash
jupyter lab
# or
jupyter notebook
```

## Database configuration

- **`settings.py`** loads `.env` via `python-dotenv` and sets **`DATABASE_URL`** for SQLAlchemy.
- **Priority:** if `DATABASE_URL` in `.env` is non-empty, it is used as-is (SQLite or PostgreSQL). If it is empty and `DB_BACKEND` is `postgresql` (or `postgres` / `pg`), the URL is built from `POSTGRES_*` variables.
- **Default** when `DATABASE_URL` is empty and backend is SQLite: absolute path to `data/sql/school.db`.
- **`init_school_db.py`** does not import `settings`; it writes SQLite files under `data/sql/` using paths relative to the repo root.
- **`database.py`** uses `create_engine(settings.DATABASE_URL, ...)`.
- Generated `*.db` files under `data/sql/` are ignored by `.gitignore`.

## Environment variables

Copy `.env.example` to `.env` and edit **`.env`** (never commit `.env`).

| Variable | Role |
|----------|------|
| `API_KEY`, `SECRET_KEY` | Optional app secrets |
| `DATABASE_URL` | SQLAlchemy URL; non-empty value wins over composed Postgres URL |
| `DB_BACKEND` | `sqlite` (default) or `postgresql` / `postgres` / `pg` when building URL from `POSTGRES_*` |
| `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` | Used when `DATABASE_URL` is empty and `DB_BACKEND` selects PostgreSQL |

Example PostgreSQL URL (driver **psycopg** v3):

```bash
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/labs_py
```

## How to Contribute

1. Fork the repository on GitHub.
2. Create a branch: `git checkout -b feature/my-new-feature`
3. Make changes, add tests, run local checks.
4. Commit: `git add .` and `git commit -m "Describe your change clearly."`
5. Push and open a PR: `git push origin feature/my-new-feature`

## Branch and Pull Request Workflow

- Default branch: `main`
- Use feature branches with clear names
- Rebase or merge `main` before opening a PR
- Describe changes and how you tested them
