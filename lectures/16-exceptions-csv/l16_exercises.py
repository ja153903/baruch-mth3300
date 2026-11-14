import csv
from pathlib import Path

# Warmup


def parse_int(text: str) -> int | None:
    """int(text), or None if text isn't a valid integer."""
    raise NotImplementedError


def check_percent(x: float) -> float:
    """Return x if it's from 0 to 100, inclusive. Otherwise, raise ValueError.

    Put x in the error message, like "percent out of range: 120".
    """
    raise NotImplementedError


# Core


def read_prices(path: Path) -> dict[str, float]:
    """Read a CSV with columns ticker,price. Skip rows whose price isn't a number."""
    raise NotImplementedError


def parse_money(text: str) -> float:
    """Turn text like "$1,234.50" into 1234.5.

    Accountants write negative amounts in parentheses, so "(12.50)" means -12.5.
    Raise ValueError for text that isn't money, like "abc". (float already does that.)
    """
    raise NotImplementedError


def count_bad_rows(path: Path, column: str) -> int:
    """How many rows of a CSV file have a value in column that isn't a number."""
    raise NotImplementedError


def write_report(path: Path, totals: dict[str, float]) -> None:
    """Write totals as a CSV file with the header ticker,total.

    Write one row per ticker in alphabetical order, with each total to two decimal
    places. For {"MSFT": 2051.25, "AAPL": 1905.0}, the rows are AAPL,1905.00 and
    MSFT,2051.25.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def total_shares(path: Path) -> int:
    """The total of the shares column of a CSV file.

    Skip rows where shares isn't a whole number.
    """
    total = 0
    with open(path, newline="") as f:
        try:
            for row in csv.DictReader(f):
                total += int(row["shares"])
        except ValueError:
            pass
    return total


# Stretch


def read_trades(path: Path) -> list[tuple[str, int, float]]:
    """Read a CSV with columns ticker,shares,price into (ticker, shares, price) tuples.

    If a row has bad data, raise ValueError with that row's line number in the
    message, like "line 3: bad row". The header is line 1.
    """
    raise NotImplementedError
