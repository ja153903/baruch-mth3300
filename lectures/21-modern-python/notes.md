---
title: "L21: Modern Python"
marimo-version: "0.25.2"
---

# L21: Modern Python

**By the end of this lecture you can:**

- use `match`/`case` to branch on the *shape* of data
- give a fixed set of choices names with `StrEnum`
- name a type with `type`, and write a generic function
- explain how a t-string differs from an f-string

```python {.marimo hide_code="true"}
import marimo as mo
```

A new version of Python comes out every October. You've already used many features from 3.10 onward:

| Feature | Version | Where you saw it |
|---|---|---|
| `X \| None` in type hints | 3.10 | L6 |
| Better error messages ("Did you mean…") | 3.10–3.13 | L4 |
| `zip(strict=True)`, `itertools.batched` | 3.10, 3.12 | L12 |
| `except A, B` without parentheses | 3.14 | L16 |
| Lazy annotations, `copy.replace` | 3.14, 3.13 | L20 |

This lecture covers the rest worth knowing. A lot of AI-written code still uses older styles, so it helps to recognize the modern way.

## 1. `match` (3.10)

### On values

```python {.marimo}
def http_message(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 503:
            return "Server error"
        case _:
            return "Unknown"


print(http_message(200), http_message(503), http_message(418))
```

### On shapes

A pattern can pull values out of the data while it matches.

```python {.marimo}
def run(command: tuple, balance: float) -> float:
    match command:
        case ("deposit", amount):
            return balance + amount
        case ("withdraw", amount) if amount <= balance:
            return balance - amount
        case ("withdraw", _):
            raise ValueError("insufficient funds")
        case ("interest", rate):
            return balance * (1 + rate)
        case _:
            raise ValueError(f"unknown command: {command}")


demo_balance = 100.0
for cmd in [("deposit", 50), ("withdraw", 30), ("interest", 0.1)]:
    demo_balance = run(cmd, demo_balance)
print(demo_balance)
```

### On classes

`match` works with dataclasses too, and that's where it shines. Each kind of thing gets its own class, and one `match` handles them all.

```python {.marimo}
from dataclasses import dataclass


@dataclass
class Deposit:
    amount: float


@dataclass
class Withdrawal:
    amount: float


@dataclass
class Fee:
    amount: float
    reason: str


def apply(balance: float, txn: Deposit | Withdrawal | Fee) -> float:
    match txn:
        case Deposit(amount=a):
            return balance + a
        case Withdrawal(amount=a) if a <= balance:
            return balance - a
        case Withdrawal():
            raise ValueError("insufficient funds")
        case Fee(amount=a):
            return balance - a


_balance = 100.0
for _txn in [Deposit(50), Withdrawal(30), Fee(2.5, "wire")]:
    _balance = apply(_balance, _txn)
print(_balance)
```

`Deposit(amount=a)` means "is this a `Deposit`? If so, call its `amount` `a`." `Withdrawal()` with no fields just checks the type.

## 2. `StrEnum` (3.11)

Strings like `"buy"` and `"sell"` are easy to mistype, and a typo fails silently: `side == "biy"` is just `False`. An **enum** gives a fixed set of choices names that Python checks.

```python {.marimo}
from enum import StrEnum


class Side(StrEnum):
    BUY = "buy"
    SELL = "sell"


def signed(side: Side, shares: int) -> int:
    match side:
        case Side.BUY:
            return shares
        case Side.SELL:
            return -shares


print(signed(Side.SELL, 10), Side("buy") is Side.BUY, Side.BUY == "buy", list(Side))
```

- `Side.BIY` is an `AttributeError`, and ty flags it before you run anything.
- `Side("buy")` turns text from a file or `input()` into a `Side`. `Side("hold")` raises `ValueError`.
- A `StrEnum` member *is* a string, so `Side.BUY == "buy"` is `True`, and it prints and writes to CSV as `buy`.

## 3. `type` aliases and generics (3.12)

A `type` statement gives a long type a short, meaningful name:

```python {.marimo}
type Transaction = Deposit | Withdrawal | Fee
type Prices = dict[str, float]


def total_fees(txns: list[Transaction]) -> float:
    return sum(t.amount for t in txns if isinstance(t, Fee))


print(total_fees([Deposit(10), Fee(1.5, "wire"), Fee(0.5, "atm")]))
```

A **generic** function works for any type, and the type hint says how its input and output relate. `[T]` after the name introduces a type variable:

```python {.marimo}
def first[T](items: list[T]) -> T:
    return items[0]


print(first([3, 1, 2]), first(["AAPL", "MSFT"]))
```

ty knows that `first([3, 1, 2])` is an `int` and `first(["AAPL"])` is a `str`. If the hint were `list[object] -> object`, it would know neither.

You'll see the older spelling in AI code and in libraries written before 2023. It means the same thing:

```python
from typing import TypeVar, Optional, Union

T = TypeVar("T")


def first(items: list[T]) -> T: ...  # now: def first[T](items: list[T]) -> T


x: Optional[int]  # now: x: int | None
y: Union[int, str]  # now: y: int | str
```

## 4. Template strings (3.14)

An f-string becomes text immediately. A **t-string** keeps the pieces apart, so the code that receives it decides how to put them together.

```python {.marimo}
stock = "AAPL"
close = 190.5
tmpl = t"{stock} closed at {close}"

print(type(tmpl).__name__)
print(tmpl.strings)
print(tmpl.values)
for _part in tmpl.interpolations:
    print(_part.expression, "=", _part.value)
```

Why would you want that? A function that receives the pieces can treat the *values* differently from the *text*. A database library can escape values so that a user's input can't run as SQL. A web library can escape HTML. A report function can format every number as money. Iterating over a template gives each piece in order: a `str` for the text, and an `Interpolation` for each `{...}`.

## AI activity: modern or legacy?

AI models learned from years of older Python, so they often write the old style.

1. Ask your AI: *"Write a Python function that returns the largest item in a list of any type, or None if the list is empty."*
2. Check the answer for `TypeVar`, `Optional`, `Union`, or `List` from `typing`. Those are signs of older code.
3. Ask it to rewrite the function for Python 3.15, using only built-in types and the 3.12 generic syntax. Run `uv run ty check` on both versions.
4. Log which version it gave first, and whether the rewrite still passes your tests.

## Exercises (40 minutes)

Open `l21_exercises.py` and run `uv run pytest lectures/21-modern-python` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `counts_toward_gpa`, `last` |
| Core | `describe`, `calculate`, `parse_grade`, `cash_change` |
| Fix the AI's code | `describe_order` |
| Stretch | `money` |
