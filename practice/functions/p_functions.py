import math


def celsius_to_fahrenheit(celsius: float) -> float:
    """F = C × 9/5 + 32: celsius_to_fahrenheit(100) == 212."""
    raise NotImplementedError


def tip_amount(bill: float, rate: float = 0.18) -> float:
    """The tip on bill, rounded to cents. The rate is 18% unless the caller gives another."""
    raise NotImplementedError


def boxes_needed(items: int, per_box: int) -> int:
    """How many boxes it takes to pack every item: boxes_needed(100, 12) == 9. Hint: math.ceil."""
    raise NotImplementedError


def seconds_to_hms(seconds: int) -> str:
    """seconds as "H:MM:SS": seconds_to_hms(3723) == "1:02:03". Hint: // and %, and :02 in an f-string."""
    raise NotImplementedError


def format_price(amount: float) -> str:
    """amount with a dollar sign, commas, and two decimals: format_price(1234.5) == "$1,234.50"."""
    raise NotImplementedError


def mask_card(number: str) -> str:
    """Hide all but the last four digits: mask_card("4111222233334444") == "**** 4444"."""
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it with the tests, then fix it.


def circle_circumference(radius: float) -> float:
    """The distance around a circle: 2πr."""
    return 2 * math.pi * radius**2
