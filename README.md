# Data Science Python Environment

This repository is a local workspace for Python data science libraries and experiments.

## Structure

- `files/` - miscellaneous data files and scripts.
- `matplotlib/` - work related to Matplotlib visualization.
- `pandas/` - work related to Pandas data manipulation.

## Setup

1. Create and activate a Conda environment:
   ```bash
   conda create -n ds-env python=3.11 -y
   conda activate ds-env
   ```
2. Install dependencies (if any):
   ```bash
   conda install jupyter ipykernel
   ```
3. Add packages as needed, e.g.:
   ```bash
   pip install numpy pandas matplotlib seaborn
   ```

## Usage

- Launch Jupyter Lab / Notebook in the repo root:
  ```bash
  jupyter lab
  ```

## Contributing

- Keep code style consistent.
- Use branches for features and bug fixes.
- Test notebooks and scripts before committing.

## Environment variables

Use `.env` for local secrets and `.env.example` as a template to share required keys.
