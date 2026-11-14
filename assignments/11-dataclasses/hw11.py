from dataclasses import dataclass
from typing import override


class Account:
    """Write this class by hand: no @dataclass."""

    # The attributes that __init__ sets:
    owner: str
    balance: float

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


class SavingsAccount(Account):
    rate: float

    def __init__(self, owner: str, balance: float = 0.0, rate: float = 0.02) -> None:
        raise NotImplementedError

    @override
    def withdraw(self, amount: float) -> None:
        raise NotImplementedError

    def add_interest(self) -> None:
        raise NotImplementedError


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        raise NotImplementedError

    def moved(self, dx: float, dy: float) -> Point:
        raise NotImplementedError


@dataclass
class Circle:
    radius: float


@dataclass
class Rectangle:
    width: float
    height: float


@dataclass
class Triangle:
    base: float
    height: float


type Shape = Circle | Rectangle | Triangle


def area(shape: Shape) -> float:
    raise NotImplementedError
