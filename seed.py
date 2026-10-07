"""Seed a few habits.

Usage:
    python seed.py            # seeds the local `habits` catalog directory
    python seed.py my_dir     # or another directory you passed to `pxt schema update`
"""
import sys
from pathlib import Path

import pixeltable as pxt

target = sys.argv[1] if len(sys.argv) > 1 else 'habits'
HERE = Path(__file__).resolve().parent

SEED = {
    'habits': [
        {'name': 'Morning run', 'category': 'health', 'streak_days': 12, 'notes': None},
        {'name': 'Read 20 pages', 'category': 'learning', 'streak_days': 41, 'notes': 'currently: Dune'},
        {'name': 'Stretch', 'category': 'health', 'streak_days': 3, 'notes': None},
    ],
}

for table_name, rows in SEED.items():
    t = pxt.get_table(f'{target}/{table_name}')
    if t.count() > 0:
        print(f'{target}/{table_name} already has {t.count()} rows; skipping')
        continue
    for row in rows:
        for k, v in row.items():
            if isinstance(v, str) and v.startswith('data/'):
                row[k] = str(HERE / v)   # local sample media file
    t.insert(rows)
    print(f'inserted {len(rows)} rows into {target}/{table_name}')
