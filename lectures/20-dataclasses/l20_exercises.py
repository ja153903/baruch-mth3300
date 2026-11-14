from dataclasses import dataclass, field
from typing import override

# Warmup


class Tally:
    """A click counter. Write this class by hand: no @dataclass."""

    def __init__(self) -> None:
        """Start the count at 0."""
        raise NotImplementedError

    def click(self) -> None:
        """Add 1 to the count."""
        raise NotImplementedError

    def total(self) -> int:
        raise NotImplementedError

    def reset(self) -> None:
        """Set the count back to 0."""
        raise NotImplementedError


@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def scale(self, factor: float) -> None:
        """Multiply both sides by factor, changing this rectangle."""
        raise NotImplementedError


# Core


@dataclass(frozen=True)
class Bond:
    face_value: float
    coupon_rate: float  # 0.05 means 5% a year

    def annual_coupon(self) -> float:
        """The interest the bond pays each year: face_value times coupon_rate."""
        raise NotImplementedError

    def with_rate(self, rate: float) -> Bond:
        """A new Bond with a different coupon_rate. A frozen Bond can't change itself.

        Use copy.replace.
        """
        raise NotImplementedError


class Gradebook:
    """Write this class by hand: no @dataclass."""

    def __init__(self, course: str) -> None:
        """Store the course name, and start with an empty list of scores."""
        raise NotImplementedError

    def add(self, score: float) -> None:
        """Add a score. Raise ValueError unless 0 <= score <= 100."""
        raise NotImplementedError

    def average(self) -> float:
        """The mean score. Raise ValueError if there are no scores yet."""
        raise NotImplementedError

    def __repr__(self) -> str:
        """For example: Gradebook('MTH 3300', 3 scores)"""
        raise NotImplementedError


class CurvedGradebook(Gradebook):
    def __init__(self, course: str, curve: float) -> None:
        """Run Gradebook's __init__ with super(), then store the curve."""
        raise NotImplementedError

    @override
    def average(self) -> float:
        """Gradebook's average plus the curve, but never more than 100."""
        raise NotImplementedError


@dataclass
class CartItem:
    name: str
    price: float
    quantity: int = 1


@dataclass
class Cart:
    items: list[CartItem] = field(default_factory=list)

    def add(self, name: str, price: float, quantity: int = 1) -> None:
        """Add a CartItem to items."""
        raise NotImplementedError

    def total(self) -> float:
        """The sum of price times quantity, over all the items."""
        raise NotImplementedError

    def count(self) -> int:
        """How many things are in the cart: 2 bagels and 1 coffee make 3."""
        raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


class Watchlist:
    """A named list of tickers. Adding to a Watchlist never changes the list you made it from."""

    def __init__(self, name: str, tickers: list[str]) -> None:
        self.name = name
        self.tickers = tickers

    def add(self, ticker: str) -> None:
        """Add a ticker, in upper case."""
        self.tickers.append(ticker.upper())


# Stretch


@dataclass(frozen=True)
class Money:
    """An amount of money, stored as a whole number of cents, so it's exact."""

    cents: int

    def dollars(self) -> str:
        """Money(123456).dollars() == "$1,234.56", and Money(5).dollars() == "$0.05"."""
        raise NotImplementedError

    def __add__(self, other: Money) -> Money:
        """Python calls this for a + b. Money(150) + Money(275) == Money(425)."""
        raise NotImplementedError

    def split(self, n: int) -> list[Money]:
        """Split into n parts that differ by at most one cent, bigger parts first.

        Money(100).split(3) == [Money(34), Money(33), Money(33)]
        """
        raise NotImplementedError
