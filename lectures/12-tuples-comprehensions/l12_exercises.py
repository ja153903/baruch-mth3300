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
