# Warmup


def is_sorted(xs: list[int]) -> bool:
    """True if xs is in non-decreasing order. O(n): don't sort it."""
    raise NotImplementedError


def common_count(xs: list[int], ys: list[int]) -> int:
    """How many items of xs also appear somewhere in ys. Count repeats in xs each time.

    common_count([1, 2, 2, 5], [2, 3, 5]) == 3. Make it O(n + m) with a set.
    """
    raise NotImplementedError


# Core


def has_pair_with_sum(xs: list[int], target: int) -> bool:
    """True if two different positions in xs add up to target. Aim for O(n) with a set."""
    raise NotImplementedError


def new_highs(prices: list[float]) -> int:
    """How many days set a new high: a price above every earlier price. Make it O(n).

    The first day counts. new_highs([10, 12, 11, 13, 13]) == 3.
    """
    raise NotImplementedError


def max_profit_slow(prices: list[float]) -> float:
    """The most you can make by buying on one day and selling on a later day.

    Return 0.0 if no trade makes money. Write the simple O(n²) version: try every
    pair of days with two nested loops.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def max_profit(prices: list[float]) -> float:
    """The same answer as max_profit_slow, but in O(n)."""
    if len(prices) < 2:
        return 0.0
    return max(prices) - min(prices)


# Stretch


def range_sums(xs: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """For each (start, stop) in queries, the sum of xs[start:stop].

    Make it O(n + q), where q is the number of queries. First build a list of prefix
    sums, where prefix[i] is the sum of the first i numbers. Then each answer is one
    subtraction.
    """
    raise NotImplementedError


def nearby_duplicate(xs: list[int], k: int) -> bool:
    """True if two equal values are at most k positions apart. Make it O(n).

    Hint: a dict of the last position where you saw each value.
    """
    raise NotImplementedError
