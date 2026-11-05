from pathlib import Path


def write_lines(path: Path, lines: list[str]) -> None:
    """Write each string on its own line."""
    raise NotImplementedError


def longest_line(path: Path) -> str:
    """The longest line in the file, without its newline. Return "" for an empty file."""
    raise NotImplementedError
