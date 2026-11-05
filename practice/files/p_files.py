from pathlib import Path


def word_count(path: Path) -> int:
    """The number of whitespace-separated words in a text file."""
    raise NotImplementedError


def tail(path: Path, n: int) -> list[str]:
    """The last n lines of the file, without newlines."""
    raise NotImplementedError


def average_by(path: Path, key_column: str, value_column: str) -> dict[str, float]:
    """Read a CSV with a header row and average value_column for each distinct key_column value."""
    raise NotImplementedError
