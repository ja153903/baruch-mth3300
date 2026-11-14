from dataclasses import dataclass
from enum import StrEnum
from string.templatelib import Template


class Grade(StrEnum):
    PASS = "pass"
    FAIL = "fail"
    INCOMPLETE = "incomplete"


# Warmup


def counts_toward_gpa(grade: Grade) -> bool:
    """Use match: PASS and FAIL count, INCOMPLETE doesn't."""
    raise NotImplementedError


def last[T](items: list[T]) -> T | None:
    """The last item, or None if the list is empty."""
    raise NotImplementedError


# Core


def describe(value: object) -> str:
    """Use match:
    - an empty list           -> "empty"
    - a list of one element   -> "one item"
    - any other list          -> "many items"
    - a 2-tuple (x, y)        -> "point at x, y", for example "point at 3, 4"
    - anything else           -> "unknown"
    """
    raise NotImplementedError


def calculate(expr: tuple) -> float:
    """expr is ("add", a, b), ("mul", a, b), or ("neg", a). Raise ValueError otherwise."""
    raise NotImplementedError


def parse_grade(text: str) -> Grade:
    """Turn text like "pass", " PASS ", or "Fail" into a Grade.
    Raise ValueError for anything else. (Hint: Grade("pass") already does half the work.)
    """
    raise NotImplementedError


@dataclass
class Buy:
    ticker: str
    shares: int
    price: float


@dataclass
class Sell:
    ticker: str
    shares: int
    price: float


@dataclass
class Dividend:
    ticker: str
    amount: float


def cash_change(event: Buy | Sell | Dividend) -> float:
    """How an event changes your cash. Use match with class patterns.

    A Buy spends shares * price, a Sell brings in shares * price, and a Dividend
    brings in its amount. cash_change(Buy("AAPL", 10, 190.5)) == -1905.0
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


@dataclass
class Order:
    ticker: str
    shares: int


@dataclass
class LimitOrder(Order):
    limit: float


def describe_order(order: Order) -> str:
    """Describe an order: "buy 10 AAPL at market" for an Order, and
    "buy 10 AAPL at 185.0 or less" for a LimitOrder with a limit of 185.0.
    """
    match order:
        case Order(ticker=t, shares=n):
            return f"buy {n} {t} at market"
        case LimitOrder(ticker=t, shares=n, limit=p):
            return f"buy {n} {t} at {p} or less"


# Stretch


def money(template: Template) -> str:
    """Build the string, but format every float value as dollars, like $1,234.50.
    Other values are converted with str().

    Hint: `for part in template` gives a str for each piece of text, and an
    Interpolation (from string.templatelib) for each {...}. Its .value is the value.
    """
    raise NotImplementedError
