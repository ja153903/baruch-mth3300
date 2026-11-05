---
title: "L20: Dataclasses"
marimo-version: "0.25.2"
---

# L20: Dataclasses

**By the end of this lecture you can:**

- define a class with `@dataclass`
- add methods that use `self`
- choose between mutable and frozen objects

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Why classes?

A tuple like `("AAPL", 10, 190.5)` doesn't tell you what each value means. A class gives every field a name and a type.

```python {.marimo}
from dataclasses import dataclass, field


@dataclass
class Position:
    ticker: str
    shares: int
    price: float

    def value(self) -> float:
        return self.shares * self.price


pos = Position("AAPL", 10, 190.5)
print(pos, pos.ticker, pos.value())
```

`@dataclass` writes `__init__`, `__repr__`, and `__eq__` for you.

## 2. Methods and `self`

`self` is the object the method was called on. `pos.value()` is shorthand for `Position.value(pos)`.

```python {.marimo}
@dataclass
class Portfolio:
    positions: list[Position] = field(default_factory=list)

    def add(self, position: Position) -> None:
        self.positions.append(position)

    def total(self) -> float:
        return sum(p.value() for p in self.positions)


book = Portfolio()
book.add(Position("AAPL", 10, 190.5))
book.add(Position("MSFT", 5, 410.25))
print(f"{book.total():,.2f}")
```

**Predict:** why `field(default_factory=list)` instead of `= []`? (Hint: aliasing, L11.)

## 3. Frozen dataclasses

```python {.marimo}
@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


origin = Point(0, 0)
print(origin.distance_to(Point(3, 4)), Point(1, 2) == Point(1, 2))
```

Frozen objects can't be changed after they're created, so they can be dict keys and set members.

Notice that `other: Point` refers to the class *inside its own body*. Since Python 3.14, annotations are evaluated lazily, so this just works.

## AI activity

Describe a `BankAccount` in plain English (fields and rules) and ask an AI to turn it into a dataclass. Check whether it enforced **every** rule you wrote. Log any it missed.

**Exercises:** `l20_exercises.py`
