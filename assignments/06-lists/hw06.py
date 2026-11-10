# Daily closing prices for a made-up stock. PRICES[0] is day 0.
PRICES: list[float] = [
    100.00, 98.46, 98.01, 98.87, 97.69, 96.12, 96.06, 92.07, 94.37, 95.87,
    97.04, 97.33, 98.97, 100.60, 100.63, 99.20, 98.07, 97.87, 96.01, 96.93,
    98.60, 96.00, 97.71, 96.67, 96.27, 95.64, 94.39, 93.23, 93.18, 90.72,
    92.28, 89.56, 89.33, 89.46, 87.36, 86.43, 85.23, 83.30, 81.58, 84.42,
    86.54, 86.00, 86.66, 87.53, 88.73, 90.22, 90.95, 88.93, 90.15, 86.47,
    87.26, 86.55, 85.43, 87.15, 85.46, 87.95, 87.46, 88.54, 88.34, 87.62,
    91.81, 95.56, 96.13, 96.96, 96.50, 98.80, 102.05, 105.68, 104.76, 104.29,
    101.20, 101.16, 101.41, 98.83, 96.22, 98.24, 97.61, 98.74, 98.84, 97.66,
    98.10, 99.28, 99.52, 98.63, 98.67, 99.52, 100.26, 103.39, 104.12, 105.00,
]  # fmt: skip

# Part 2: fill this in BEFORE you implement signals. Add at least 5 cases, worked out
# by hand, as (prices, short, long, expected_signals).
# For example: ([3, 2, 1, 2, 3, 4, 3, 2, 1], 1, 3, [(3, "buy"), (6, "sell")])
SIGNAL_CASES: list[tuple[list[float], int, int, list[tuple[int, str]]]] = []


# Part 1: building blocks


def running_total(xs: list[float]) -> list[float]:
    """Each element is the sum of everything in xs up to and including that position."""
    raise NotImplementedError


def moving_average(xs: list[float], k: int) -> list[float]:
    """The average of every window of k consecutive elements.

    Returns [] if k is bigger than the list.
    moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    """
    raise NotImplementedError


def daily_changes(prices: list[float]) -> list[float]:
    """Each day's price minus the previous day's. The result is one element shorter.

    Write this as a list comprehension, using zip(..., strict=True).
    daily_changes([10, 12, 11]) == [2, -1]
    """
    raise NotImplementedError


# Part 2: signals and backtesting


def signals(prices: list[float], short: int, long: int) -> list[tuple[int, str]]:
    """The (day, action) pairs where the two moving averages cross, in day order.

    short < long. On day d, the short average covers the short prices ending at day d,
    and the long average covers the long prices ending at day d. The first day with
    both averages is day long - 1. It can never have a signal, because it has no
    previous day to compare with.

    - "buy" on day d: short <= long on day d - 1, and short > long on day d.
    - "sell" on day d: short >= long on day d - 1, and short < long on day d.

    Use moving_average. Be careful: its two results have different lengths.
    signals([3, 2, 1, 2, 3, 4, 3, 2, 1], 1, 3) == [(3, "buy"), (6, "sell")]
    """
    raise NotImplementedError


def backtest(
    prices: list[float], trades: list[tuple[int, str]], cash: float, fee: float = 0.0
) -> float:
    """The value of the account after following trades, starting with only cash.

    Go through trades in order. Each one is a (day, action) pair like signals returns.
    - "buy": if you hold no shares, spend all your cash at that day's price. Fractions
      of a share are allowed. If you already hold shares, ignore the trade.
    - "sell": if you hold shares, sell them all at that day's price. If you hold none,
      ignore the trade.

    The result is your cash plus the value of any shares at the last price in prices.
    Leave fee alone until part 3.
    """
    raise NotImplementedError


def best_windows(
    prices: list[float], shorts: list[int], longs: list[int], cash: float
) -> tuple[int, int, float]:
    """The (short, long, final_value) of the most profitable pair of windows.

    Try every short in shorts with every long in longs, skipping pairs where
    short >= long. You can assume at least one pair is valid. If pairs tie, keep the
    one you found first, looping through shorts on the outside and longs on the inside.
    """
    raise NotImplementedError
