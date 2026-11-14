# Warmup


def is_even(n: int) -> bool:
    raise NotImplementedError


def max_of_three(a: float, b: float, c: float) -> float:
    """Don't use the built-in max()."""
    raise NotImplementedError


# Core


def trade_allowed(cash: float, price: float, shares: int) -> bool:
    """True if you can buy `shares` shares at `price` each with `cash`.

    You must buy at least one share. trade_allowed(1000, 37.5, 26) is True.
    """
    raise NotImplementedError


def commission(trade_value: float) -> float:
    """The broker's fee for a trade:

    - under $1,000: a flat $5.00
    - from $1,000 up to and including $10,000: 1% of the trade value
    - over $10,000: 0.5% of the trade value
    """
    raise NotImplementedError


def price_signal(price: float, average: float) -> str:
    """A trading signal: "buy" if price is more than 5% below average,
    "sell" if it's more than 5% above average, and "hold" otherwise.

    price_signal(90, 100) == "buy"
    """
    raise NotImplementedError


def quadrant(x: float, y: float) -> int:
    """The quadrant (1 to 4) that the point (x, y) is in, or 0 if it's on an axis.

    Quadrant 1 has x > 0 and y > 0. Quadrants 2, 3, and 4 follow counterclockwise.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def late_fee(days_late: int) -> float:
    """A credit card late fee: 0.0 if paid on time, 25.0 if 1 to 30 days late,
    and 40.0 if more than 30 days late."""
    if days_late > 0:
        return 25.0
    elif days_late > 30:
        return 40.0
    else:
        return 0.0


# Stretch


def median_of_three(a: float, b: float, c: float) -> float:
    """The middle value of three numbers. Don't use sorted(), min(), or max()."""
    raise NotImplementedError


def count_real_roots(a: float, b: float, c: float) -> int:
    """How many real solutions a*x**2 + b*x + c = 0 has. a is never 0.

    Hint: look at the discriminant, b**2 - 4*a*c.
    """
    raise NotImplementedError
