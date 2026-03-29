# Data Science Python Environment

This repository is a local workspace for Python data science libraries and experiments.

## Table of Contents

- [About](#about)
- [Clone the Repository](#clone-the-repository)
- [Download for Windows/Linux/macOS](#download-for-windowslinuxmacos)
- [Setup (Conda)](#setup-conda)
- [Usage](#usage)
- [How to Contribute](#how-to-contribute)
- [Branch and Pull Request Workflow](#branch-and-pull-request-workflow)
- [Environment Variables](#environment-variables)

## About

This project contains Python scripts, data files, and experiments focusing on data science tools like Pandas, Matplotlib, and more.

## Clone the Repository

Open a terminal or shell and run:

```bash
git clone https://github.com/florentz14/Labs_Py_Anaconda.git
cd Labs_Py_Anaconda
```

If you already have the repo and want to update from remote:

```bash
git pull origin main
```

## Download for Windows/Linux/macOS

1. Install Git:
   - Windows: https://git-scm.com/download/win
   - macOS: `brew install git` or https://git-scm.com/download/mac
   - Linux: `sudo apt-get install git` (Debian/Ubuntu) or `sudo dnf install git` (Fedora)

2. Clone the repository (same command for all OS):

```bash
git clone https://github.com/florentz14/Labs_Py_Anaconda.git
cd Labs_Py_Anaconda
```

3. Optional: download as ZIP via GitHub UI
   - Visit: https://github.com/florentz14/Labs_Py_Anaconda
   - Click "Code" > "Download ZIP"
   - Extract the archive to your local folder

## Setup (Conda)

Create and activate a Conda environment:

```bash
conda create -n ds-env python=3.11 -y
conda activate ds-env
```

Install base dependencies:

```bash
conda install jupyter ipykernel -y
```

Install additional libraries:

```bash
pip install numpy pandas matplotlib seaborn
```

## Usage

Launch Jupyter Lab or Notebook from repository root:

```bash
jupyter lab
# or
jupyter notebook
```

Open and run notebooks or scripts in the appropriate folders:

- `matplotlib/` : visualization examples
- `pandas/` : data manipulation examples
- `files/` : miscellaneous input/output data files

## How to Contribute

1. Fork the repository on GitHub.
2. Create a local branch:

```bash
git checkout -b feature/my-new-feature
```

3. Make changes, add tests, and run local checks.
4. Stage and commit changes:

```bash
git add .
git commit -m "Add feature: ..."
```

5. Push and open a pull request:

```bash
git push origin feature/my-new-feature
```

6. In GitHub, create a PR against `main`.

## Branch and Pull Request Workflow

- Main branch: `main`
- Use feature branches and meaningful names
- Rebase/merge main before PR creation
- Include description + testing steps

## Environment Variables

Use `.env` for local secrets and `.env.example` as a template:

- copy `.env.example` to `.env`
- set values in `.env`

**Note**: Do not commit sensitive values to version control.
