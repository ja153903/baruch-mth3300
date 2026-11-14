# Practice final

**No AI, no notes, no computer.** Cumulative, but weighted toward L15–L23. Give yourself 110 minutes.

## Part A: predict the output (4 points each)

```python
# A1
def g(n):
    if n <= 1:
        return n
    return g(n - 1) + g(n - 2)


print([g(k) for k in range(7)])

# A2
from dataclasses import dataclass


@dataclass
class P:
    x: int
    y: int = 0


print(P(1), P(1) == P(1, 0))


# A3
def classify(v):
    match v:
        case []:
            return "empty"
        case [x]:
            return f"one: {x}"
        case (a, b):
            return f"pair: {a + b}"
        case _:
            return "other"


print(classify([]), classify([7]), classify((2, 3)), classify("hi"))

# A4
try:
    print(int("3.5"))
except ValueError:
    print("bad")
finally:
    print("done")

# A5
print(0.1 * 3 == 0.3, round(0.1 * 3, 10) == 0.3)


# A6
class Position:
    def __init__(self, ticker, shares):
        self.ticker = ticker
        self.shares = shares

    def describe(self):
        return f"{self.shares} {self.ticker}"


class ShortPosition(Position):
    def describe(self):
        return "short " + super().describe()


a = ShortPosition("TSLA", 5)
b = a
b.shares = 8
print(a.describe(), isinstance(a, Position), a == ShortPosition("TSLA", 8))
```

## Part B: complexity (5 points each)

What's the Big-O running time of each, in terms of `n = len(xs)`?

1. `x in xs`, when `xs` is a list
2. `x in s`, when `s` is a set
3. Binary search on a sorted list
4. Two nested loops over `xs`
5. `sorted(xs)`

## Part C: write code (15 points each)

**C1.** Write a recursive `count_down(n: int) -> list[int]`. For example, `count_down(3)` is `[3, 2, 1, 0]`.

**C2.** Write a class `Account` by hand (no `@dataclass`). `Account(owner, balance=0.0)` stores both values, and `withdraw(amount)` raises `ValueError` if `amount` is more than the balance. Then write a subclass `OverdraftAccount` whose `withdraw` allows the balance to go down to `-100`.

**C3.** Write `total_by_ticker(path) -> dict[str, float]` for a CSV with columns `ticker,shares,price`. It returns the total value (shares × price) for each ticker, and skips rows with bad numbers.

<details>
<summary>Answers</summary>

- **A1:** `[0, 1, 1, 2, 3, 5, 8]`
- **A2:** `P(x=1, y=0) True`
- **A3:** `empty one: 7 pair: 5 other`. (`"hi"` doesn't match `(a, b)`, because sequence patterns never match strings.)
- **A4:** `bad`, then `done`
- **A5:** `False True`
- **A6:** `short 8 TSLA True False`. (`b` and `a` are the same object, and a class without `__eq__` is only equal to itself.)
- **B:** O(n), O(1) on average, O(log n), O(n²), O(n log n)
</details>
