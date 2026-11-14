# Warmup


def min_max(xs: list[int]) -> tuple[int, int]:
    """The smallest and largest values, as a tuple. min_max([3, 9, 1]) == (1, 9).

    xs has at least one item.
    """
    raise NotImplementedError


def squares_of_evens(xs: list[int]) -> list[int]:
    """The square of every even number in xs, in order. Use a comprehension.

    squares_of_evens([1, 2, 3, 4]) == [4, 16]
    """
    raise NotImplementedError


# Core


def pairwise_sums(xs: list[int], ys: list[int]) -> list[int]:
    """[xs[0]+ys[0], xs[1]+ys[1], ...]. Raise ValueError if the lengths differ (hint: zip strict)."""
    raise NotImplementedError


def flatten(rows: list[list[int]]) -> list[int]:
    """Join a list of lists into one list. Use a comprehension."""
    raise NotImplementedError


def period_returns(prices: list[float]) -> list[float]:
    """The return from each price to the next: later / earlier - 1. Use itertools.pairwise."""
    raise NotImplementedError


def in_batches(tickers: list[str], size: int) -> list[list[str]]:
    """Split tickers into lists of length size; the last may be shorter. Use itertools.batched."""
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def total_value(shares: list[int], prices: list[float]) -> float:
    """The value of a portfolio: the sum of shares[i] * prices[i].

    Raise ValueError if the lists have different lengths.
    """
    return sum(n * p for n, p in zip(shares, prices))


# Stretch


def longest_streak(prices: list[float]) -> int:
    """The most days in a row that the price went up. Use itertools.pairwise.

    longest_streak([1, 2, 3, 2, 3, 4, 5]) == 3, for the three rises from 2 to 5.
    A price that stays the same isn't a rise.
    """
    raise NotImplementedError


def best_performers(tickers: list[str], returns: list[float], n: int) -> list[str]:
    """The n tickers with the highest returns, best first.

    best_performers(["A", "B", "C"], [0.05, 0.12, -0.02], 2) == ["B", "A"]
    Hint: sort (return, ticker) tuples.
    """
    raise NotImplementedError
