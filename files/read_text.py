#-------------------------------------------------
# file_name: read_text.py
# author: Florentino
# date: 2026-04-05
# description: Read a text file and print its content
#-------------------------------------------------

from pathlib import Path

# Raíz del repo: funciona aunque ejecutes el script con ruta absoluta (no depende del cwd).
_root = Path(__file__).resolve().parents[1]
file_path = _root / "data" / "text" / "sample.txt"

# Read a text file and print its content
with open(file_path, 'r') as file:
    content = file.read()
    print(content)