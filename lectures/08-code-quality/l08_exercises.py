# Warmup


def absolute(x: float) -> float:
    """This has a bug. Find it with the tests, then fix it."""
    if x > 0:
        return x
    return x


def ticket_price(age: int) -> float:
    """Children under 12 pay 8.00, seniors 65 and over pay 9.00, and everyone else pays 14.00."""
    raise NotImplementedError


# Core


def is_valid_ticker(symbol: str) -> bool:
    """True if symbol is 1 to 5 letters, all capitals.

    "AAPL" is valid; "aapl", "GOOGLE", and "BRK.B" aren't.
    Hint: the string methods isalpha() and isupper().
    """
    raise NotImplementedError


def next_business_day(day: int) -> int:
    """The weekday after `day`. Days are numbered 0 = Monday to 6 = Sunday.

    After Friday, Saturday, or Sunday comes Monday: next_business_day(4) == 0.
    """
    raise NotImplementedError


def grade_points(letter: str) -> float:
    """The grade points for a letter grade.

    A = 4.0, B = 3.0, C = 2.0, D = 1.0, and anything else 0.0.
    Accept lowercase too: grade_points("b") == 3.0.
    """
    raise NotImplementedError


def parking_fee(hours: float) -> float:
    """Parking costs $5.00 for the first hour, then $3.00 for each extra hour
    or part of an hour, up to at most $20.00. hours is always more than 0.

    parking_fee(2.5) == 11.0: $5.00, plus $3.00 for each of 2 extra (started) hours.
    Use a named constant for each dollar amount. Hint: math.ceil.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def with_tax(price: float) -> float:
    """price plus New York City sales tax of 8.875%, rounded to cents."""
    return round(price * 1.0875, 2)


# Stretch


def minutes_late(scheduled: str, actual: str) -> int:
    """How many minutes late a train was, or 0 if it wasn't late.

    The times are "HH:MM" strings from the same day:
    minutes_late("08:15", "08:42") == 27 and minutes_late("09:00", "08:55") == 0
    """
    raise NotImplementedError
