from pathlib import Path


def count_lines(path: Path) -> int:
    raise NotImplementedError


def column_total(path: Path, column: str) -> float:
    raise NotImplementedError


def safe_divide(a: float, b: float) -> float | None:
    raise NotImplementedError
