---
title: "L12: Tuples and comprehensions"
marimo-version: "0.25.2"
---

# L12: Tuples and comprehensions

**By the end of this lecture you can:**

- use tuples and unpacking
- walk through two lists together with `zip`
- write list comprehensions, including Python 3.15's unpacking form
- walk through neighbors and chunks with `itertools`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Tuples are lists that can't change

```python {.marimo}
point = (3, 4)
x, y = point  # unpacking
print(x, y)
quotient, remainder = divmod(17, 5)
print(quotient, remainder)
```

Use a tuple for a fixed group of related values, like a coordinate, or a function that returns two results.

## 2. `zip`

```python {.marimo}
tickers = ["AAPL", "MSFT", "NVDA"]
shares = [10, 5, 8]
for ticker, n in zip(tickers, shares, strict=True):
    print(ticker, n)
```

`strict=True` raises an error if the lists have different lengths, instead of silently dropping the extras.

## 3. List comprehensions

`[expression for item in iterable if condition]`

```python {.marimo}
squares = [k * k for k in range(1, 6)]
evens = [k for k in range(10) if k % 2 == 0]
lengths = [len(t) for t in tickers]
print(squares, evens, lengths)
```

**Predict:**

```python {.marimo}
print([c.upper() for c in "hey" if c != "e"])
```

## 4. New in Python 3.15: unpacking in comprehensions

```python {.marimo}
rows = [[1, 2], [3], [4, 5, 6]]
print([*row for row in rows])  # flattens the list of lists
```

Before 3.15, you had to write `[x for row in rows for x in row]`.

## 5. Dict and set comprehensions

```python {.marimo}
print({t: n for t, n in zip(tickers, shares)})
print({len(t) for t in tickers})
```

## 6. Neighbors and chunks with `itertools`

`pairwise` gives each item with the one after it, which is exactly what a period return needs:

```python {.marimo}
from itertools import batched, pairwise

_prices = [100.0, 110.0, 99.0]
print([round(b / a - 1, 3) for a, b in pairwise(_prices)])
```

`batched` splits a sequence into tuples of a fixed size.

**Predict:** three tickers, in batches of two. What's in the last batch?

```python {.marimo}
print(list(batched(tickers, 2)))
```

## AI activity

Write `[x for row in rows for x in row]` and `[*row for row in rows]` side by side. Ask an AI which is clearer and why. Do you agree?

**Exercises:** `l12_exercises.py`
