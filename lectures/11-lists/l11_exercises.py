# Warmup


def last_n(xs: list[int], n: int) -> list[int]:
    """The last n items of xs, as a new list. last_n([1, 2, 3, 4], 2) == [3, 4].

    last_n(xs, 0) == [], and if n is bigger than the list, return all of it.
    """
    raise NotImplementedError


def price_range(prices: list[float]) -> float:
    """The highest price minus the lowest. prices has at least one price.

    price_range([101.5, 99.0, 103.25]) == 4.25
    """
    raise NotImplementedError


# Core


def rotate(xs: list[int], k: int) -> list[int]:
    """A new list with the first k elements moved to the end. rotate([1,2,3,4], 1) == [2,3,4,1]."""
    raise NotImplementedError


def remove_all(xs: list[int], value: int) -> list[int]:
    """A new list without any copies of value. Don't change xs."""
    raise NotImplementedError


def apply_split(shares: list[int], ratio: int) -> None:
    """A stock split multiplies every holding by ratio. Change shares in place.

    Return nothing. If xs == [10, 5], then after apply_split(xs, 2), xs == [20, 10].
    """
    raise NotImplementedError


def column(table: list[list[int]], j: int) -> list[int]:
    """Item j of every row, as a new list. column([[1, 2], [3, 4]], 1) == [2, 4]."""
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def top_three(scores: list[int]) -> list[int]:
    """The three highest scores, highest first. Don't change scores."""
    scores.sort(reverse=True)
    return scores[:3]


# Stretch


def max_drawdown(prices: list[float]) -> float:
    """The biggest drop from a peak to a later price, as a fraction of the peak.

    For [100, 120, 90, 130, 117], the biggest drop is from 120 to 90: 30 / 120 == 0.25.
    If prices never fall, the drawdown is 0.0. prices has at least one price.

    Hint: keep track of the highest price so far.
    """
    raise NotImplementedError


def transpose(table: list[list[int]]) -> list[list[int]]:
    """Rows become columns. transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]].

    table has at least one row, and every row has the same length.
    """
    raise NotImplementedError
