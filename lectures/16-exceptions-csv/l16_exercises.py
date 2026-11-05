from pathlib import Path


def parse_int(text: str) -> int | None:
    """int(text), or None if text isn't a valid integer."""
    raise NotImplementedError


def read_prices(path: Path) -> dict[str, float]:
    """Read a CSV with columns ticker,price. Skip rows whose price isn't a number."""
    raise NotImplementedError
