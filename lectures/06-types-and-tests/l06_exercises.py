# Warmup


def clamp(x: float, lo: float, hi: float) -> float:
    """Return x, limited to the range [lo, hi]."""
    raise NotImplementedError


def is_passing(score: float) -> bool:
    """A score of 60 or more passes."""
    raise NotImplementedError


# Core


def shift_hours(start: int, end: int) -> int:
    """Hours worked on a shift from hour `start` to hour `end`, on a 24-hour clock.

    shift_hours(9, 17) == 8. A shift can run past midnight:
    shift_hours(22, 6) == 8. Hint: %.
    """
    raise NotImplementedError


def quarter(month: int) -> int:
    """The quarter of the year (1 to 4) that a month (1 to 12) is in.

    quarter(1) == 1, quarter(3) == 1, and quarter(4) == 2. Hint: //.
    """
    raise NotImplementedError


def break_even_units(fixed_cost: float, price: float, unit_cost: float) -> int:
    """How many units you must sell to cover fixed_cost.

    Each unit earns price - unit_cost. You can't sell part of a unit, so round up:
    break_even_units(1000, 15, 5) == 100.
    Add `import math` at the top of this file, and use math.ceil.
    """
    raise NotImplementedError


def cagr(start: float, end: float, years: float) -> float:
    """The compound annual growth rate: the yearly rate r that grows start into end.

    That means start * (1 + r) ** years == end. cagr(100, 121, 2) is 0.1 (10% a year).
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def average_rating(total_stars: int, num_reviews: int) -> float:
    """The average star rating, rounded to one decimal place."""
    return round(total_stars // num_reviews, 1)


# Stretch


def round_up_to(x: float, step: float) -> float:
    """x rounded up to the next multiple of step: round_up_to(1234, 100) == 1300.

    A number that's already a multiple stays the same: round_up_to(1200, 100) == 1200.
    """
    raise NotImplementedError


def continuous_growth(principal: float, rate: float, years: float) -> float:
    """principal grown at `rate` a year for `years` years, compounded continuously.

    The formula is principal * e ** (rate * years). Use math.exp(x), which is e ** x.
    """
    raise NotImplementedError
