from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        raise NotImplementedError


@dataclass
class Account:
    owner: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        raise NotImplementedError


def area(shape: tuple) -> float:
    raise NotImplementedError
