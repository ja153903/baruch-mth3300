# Practice final

**No AI, no notes, no computer.** Cumulative, but weighted toward L15–L23. Give yourself 110 minutes. 100 points.

## Part A: predict the output (5 points each)

```python
# A1
def g(n):
    if n <= 1:
        return n
    return g(n - 1) + g(n - 2)


print([g(k) for k in range(7)])


# A2
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

# A3
try:
    print(int("3.5"))
except ValueError:
    print("bad")
finally:
    print("done")

# A4
print(0.1 * 3 == 0.3, round(0.1 * 3, 10) == 0.3)


# A5
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

## Part B: find the bug (10 points each)

```python
# B1: should return the sum of the digits of n, for n >= 0
def digit_sum(n):
    if n < 10:
        return 0
    return n % 10 + digit_sum(n // 10)


# B2: should return the index of target in the sorted list xs, or -1
def binary_search(xs, target):
    lo, hi = 0, len(xs) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if xs[mid] == target:
            return mid
        if xs[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# B3: lines come from a file. Should return the average of the lines that
# are numbers, skipping the rest. Assume at least one line is a number.
def average(lines):
    total = 0.0
    count = 0
    for line in lines:
        count += 1
        try:
            total += float(line)
        except ValueError:
            pass
    return total / count
```

For each one: give an input that shows the bug, write the fixed code, and write one `assert` that fails on the buggy code and passes on your fix. For B2, also give the Big-O of the fixed version.

## Part C: write code (15 points each)

Graded on correct logic and handling the example. Small syntax slips, like a missing colon, don't cost points.

**C1.** Write a recursive `count_down(n: int) -> list[int]`. For example, `count_down(3)` is `[3, 2, 1, 0]`. How many calls does `count_down(n)` make in total?

**C2.** Write a class `Account` by hand (no `@dataclass`). `Account(owner, balance=0.0)` stores both values, and `withdraw(amount)` raises `ValueError` if `amount` is more than the balance. Then write a subclass `OverdraftAccount` whose `withdraw` allows the balance to go down to `-100`.

**C3.** Write `total_by_ticker(path) -> dict[str, float]` for a CSV with columns `ticker,shares,price`. It returns the total value (shares × price) for each ticker, and skips rows with bad numbers. What's its Big-O in the number of rows?

<details>
<summary>Answers</summary>

- **A1:** `[0, 1, 1, 2, 3, 5, 8]`
- **A2:** `empty one: 7 pair: 5 other`. (`"hi"` doesn't match `(a, b)`, because sequence patterns never match strings.)
- **A3:** `bad`, then `done`
- **A4:** `False True`
- **A5:** `short 8 TSLA True False`. (`b` and `a` are the same object, and a class without `__eq__` is only equal to itself.)
- **B1:** the base case returns 0 instead of `n`, so the first digit is lost: `digit_sum(123)` gives 5. Fix: `return n`. Assert: `assert digit_sum(123) == 6`
- **B2:** `lo < hi` stops before checking the last remaining item, so `binary_search([5], 5)` gives -1. Fix: `while lo <= hi:`. Assert: `assert binary_search([5], 5) == 0`. Big-O: O(log n).
- **B3:** `count += 1` runs for bad lines too, so `["2", "abc", "4"]` gives 2.0. Fix: move `count += 1` into the `try`, after the `float` line. Assert: `assert average(["2", "abc", "4"]) == 3.0`
- **C1:** `count_down(n)` makes n + 1 calls.
- **C3:** O(n), one pass over the rows.
</details>
