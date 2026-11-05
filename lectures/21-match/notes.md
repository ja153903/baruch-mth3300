---
title: "L21: Pattern matching and modeling"
marimo-version: "0.25.2"
---

# L21: Pattern matching and modeling

**By the end of this lecture you can:**

- use `match`/`case` to branch on the *shape* of data
- destructure tuples and dataclasses in patterns
- model a small problem with dataclasses plus `match`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. `match` on values

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

## 2. `match` on shapes

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

## 3. `match` on dataclasses

```python {.marimo}
from dataclasses import dataclass


@dataclass
class Circle:
    r: float


@dataclass
class Rect:
    w: float
    h: float


def area(shape: Circle | Rect) -> float:
    match shape:
        case Circle(r=r):
            return 3.14159 * r * r
        case Rect(w=w, h=h):
            return w * h


print(area(Circle(1)), area(Rect(2, 3)))
```

## 4. Modeling: put it together

1. **Nouns** become dataclasses: `Account`, `Transaction`.
2. **Kinds of things** become separate classes, or tagged tuples.
3. **Behavior that depends on the kind** becomes a `match`.

## AI activity

Write a 4-sentence spec for a vending machine (its commands and rules). Ask an AI to implement it with `match`. Write three tests from **your spec**, not from its code. Do they pass?

**Exercises:** `l21_exercises.py`
