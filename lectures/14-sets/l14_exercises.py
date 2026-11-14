# Warmup


def has_duplicates(xs: list[int]) -> bool:
    """True if some value appears more than once in xs."""
    raise NotImplementedError


def missing_numbers(xs: list[int], n: int) -> list[int]:
    """The numbers from 1 to n that aren't in xs, smallest first.

    missing_numbers([4, 1, 2], 5) == [3, 5]
    """
    raise NotImplementedError


# Core


def common_elements(xs: list[int], ys: list[int]) -> list[int]:
    """The values that appear in both lists, sorted, without duplicates."""
    raise NotImplementedError


def jaccard(a: set[str], b: set[str]) -> float:
    """How similar two sets are: the size of a & b divided by the size of a | b.

    jaccard({"AAPL", "MSFT"}, {"MSFT", "NVDA"}) == 1 / 3.
    Two empty sets count as the same, so their similarity is 1.0.
    """
    raise NotImplementedError


def most_traded(tickers: list[str], k: int) -> list[str]:
    """The k tickers that appear most often, most common first. Use Counter.

    If two tickers tie, the one that appears first in tickers comes first.
    """
    raise NotImplementedError


def duplicates(xs: list[int]) -> list[int]:
    """The values that appear more than once, sorted. duplicates([3, 1, 3, 2, 1, 3]) == [1, 3]."""
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def unique_in_order(xs: list[int]) -> list[int]:
    """xs without duplicates, keeping the first copy of each value, in order.

    unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    """
    return list(set(xs))


# Stretch


def can_spell(word: str, tiles: str) -> bool:
    """True if you can spell word with the letter tiles, using each tile at most once.

    can_spell("pass", "sapsx") is True, but can_spell("pass", "pas") is False.
    """
    raise NotImplementedError
