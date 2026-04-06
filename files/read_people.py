#-------------------------------------------------
# file_name: read_people.py
# author: Florentino
# date: 2026-04-05
# description: Read people.csv and print each row
#-------------------------------------------------

import csv
from pathlib import Path

_root = Path(__file__).resolve().parents[1]
file_path = _root / "data" / "csv" / "people.csv"

with open(file_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
