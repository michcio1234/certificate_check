import csv
from pathlib import Path

from typing import List, Dict

CSV_PATH = Path(__file__).parent / "data" / "attendees.csv"


def read_csv(path: str | Path) -> List[tuple]:
    with open(path) as fh:
        reader = csv.reader(fh)
        next(reader)  # skip header row
        rows = list(reader)
    return rows


def make_registry(rows: List[tuple]) -> Dict[str, str]:
    res = {}
    for row in rows:
        if row[1] in res:
            raise ValueError(f"Duplicated code {row[1]}.")
        res[row[1]] = row[0]
    return res


class CodeNotFound(Exception):
    pass


def check_attendee(code: str) -> str:
    try:
        return REGISTRY[code]
    except KeyError:
        raise CodeNotFound


REGISTRY = make_registry(read_csv(CSV_PATH))
