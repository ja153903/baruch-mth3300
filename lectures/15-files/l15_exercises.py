from pathlib import Path

# Warmup


def write_lines(path: Path, lines: list[str]) -> None:
    """Write each string on its own line."""
    raise NotImplementedError


def read_numbers(path: Path) -> list[float]:
    """The numbers in a file with one number per line, as floats.

    Lines may have spaces around the number. Skip blank lines.
    """
    raise NotImplementedError


# Core


def longest_line(path: Path) -> str:
    """The longest line in the file, without its newline. Return "" for an empty file."""
    raise NotImplementedError


def append_line(path: Path, line: str) -> None:
    """Add line and a newline to the end of the file. Create the file if it doesn't exist."""
    raise NotImplementedError


def find_lines(path: Path, word: str) -> list[int]:
    """The line numbers, starting at 1, of every line that contains word, ignoring case.

    Use enumerate.
    """
    raise NotImplementedError


def filter_file(src: Path, dst: Path, threshold: float) -> int:
    """Copy the numbers in src that are above threshold to dst, one per line.

    src has one number per line, and no blank lines. Write each number you keep
    exactly as it appears in src. Return how many numbers you wrote.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def save_prices(path: Path, prices: list[float]) -> None:
    """Write each price on its own line, with two decimal places: 1.5 becomes 1.50."""
    for price in prices:
        with open(path, "w") as f:
            f.write(f"{price:.2f}\n")


# Stretch


def backup(folder: Path) -> int:
    """Copy every .txt file in folder into a subfolder named backup. Return how many.

    Create the backup folder if it doesn't exist yet. Hint: Path.mkdir and Path.copy.
    """
    raise NotImplementedError


def word_index(path: Path) -> dict[str, list[int]]:
    """Map each word in the file, in lower case, to the numbers of the lines it's on.

    Lines are numbered from 1. List each line once per word, even if the word appears
    on it twice. For a file with the lines "Buy AAPL" and "sell aapl", the result is
    {"buy": [1], "aapl": [1, 2], "sell": [2]}.
    """
    raise NotImplementedError
