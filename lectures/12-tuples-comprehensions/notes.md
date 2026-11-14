---
title: "L12: Tuples and comprehensions"
marimo-version: "0.25.2"
---

# L12: Tuples and comprehensions

**By the end of this lecture you can:**

- use tuples, unpacking, and swapping
- return more than one value from a function
- walk through two lists together with `zip`
- write list comprehensions, including Python 3.15's unpacking form
- walk through neighbors and chunks with `itertools`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L11)

**Predict** all three lists before you run it:

```python {.marimo}
_a = [3, 1, 2]
_b = _a
_c = _a[:]
_b.append(4)
_c.sort()
print(_a, _b, _c)
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

Indexing, slicing, `len`, and `in` work on tuples just like on lists. Changing an item doesn't: try `point[0] = 5` in the REPL.

### Common bug: the one-item tuple

The comma makes a tuple, not the parentheses. **Predict:**

```python {.marimo}
print(type((5)), type((5,)), type((5, 6)))
print(len(("AAPL")), len(("AAPL",)))
```

`("AAPL")` is just the string `"AAPL"`, so a loop over it would give you four letters instead of one ticker.

## 2. Unpacking and swapping

Unpacking gives a name to each item. The number of names must match the number of items, except that a `*` name collects whatever is left over, as a list.

```python {.marimo}
_low, _high = 3, 7
_low, _high = _high, _low  # swap, with no extra variable
print(_low, _high)
_first, *_rest = [10, 20, 30, 40]
print(_first, _rest)
```

`enumerate` gives tuples too. That's why `for i, x in enumerate(xs)` works:

```python {.marimo}
print(list(enumerate(["AAPL", "MSFT"])))
```

## 3. Returning more than one value

A function can return a tuple, and the caller unpacks it:

```python {.marimo}
def high_low(prices: list[float]) -> tuple[float, float]:
    return max(prices), min(prices)


week = [101.5, 99.0, 103.25, 98.75, 100.0]
high, low = high_low(week)
print(f"high {high}, low {low}, range {high - low}")
```

The type hint `tuple[float, float]` means "a tuple of exactly two floats."

## 4. Tuples as records

A list of tuples works like a small table, with one tuple per row. Unpack each row in the `for` line:

```python {.marimo}
trades = [("AAPL", 10, 190.50), ("MSFT", 5, 410.25), ("NVDA", 8, 120.00)]
for _ticker, _shares, _price in trades:
    print(f"{_ticker:<5} {_shares:>3} x {_price:>6.2f} = {_shares * _price:>8,.2f}")
```

Tuples compare item by item from the left, like words in a dictionary. **Predict:**

```python {.marimo}
print(sorted([("MSFT", 5), ("AAPL", 10), ("AAPL", 2)]))
print((1, 99) < (2, 0))
```

## 5. `zip`

```python {.marimo}
tickers = ["AAPL", "MSFT", "NVDA"]
shares = [10, 5, 8]
for ticker, n in zip(tickers, shares, strict=True):
    print(ticker, n)
```

`zip` pairs up the first items, then the second items, and so on. Compare it with the index loop in L11: no `range(len(...))`, and no `[i]` to get wrong.

### Common bug: lists of different lengths

**Predict:** how many pairs?

```python {.marimo}
print(list(zip(["AAPL", "MSFT", "NVDA"], [10, 5])))
```

Plain `zip` stops at the end of the shorter list, and it **silently drops** the rest. NVDA disappears without an error. With `strict=True`, `zip` raises a `ValueError` instead, so you find the bug right away. Use it whenever the lists should have the same length.

## 6. List comprehensions

`[expression for item in iterable if condition]`

```python {.marimo}
squares = [k * k for k in range(1, 6)]
evens = [k for k in range(10) if k % 2 == 0]
lengths = [len(t) for t in tickers]
print(squares, evens, lengths)
```

A comprehension is a short way to write the "build a new list" loop from L11. These two do the same thing:

```python {.marimo}
_prices = [101.5, 99.0, 103.25, 98.75]

_high_loop = []
for _p in _prices:
    if _p > 100:
        _high_loop.append(_p)

_high_comp = [p for p in _prices if p > 100]
print(_high_loop, _high_comp)
```

**Predict:**

```python {.marimo}
print([c.upper() for c in "hey" if c != "e"])
```

Comprehensions work with `zip` and unpacking. Inside `sum`, `max`, or `min`, you can even leave out the brackets:

```python {.marimo}
values = [n * p for n, p in zip(shares, [190.50, 410.25, 120.00], strict=True)]
print(values, sum(values))
print(sum(k * k for k in range(1, 11)))
```

A comprehension builds one list. If your loop prints, stops early with `return`, or keeps a running value like a balance, write a normal loop. The same syntax also builds dicts and sets, which you'll meet in L13 and L14.

## 7. New in Python 3.15: unpacking in comprehensions

```python {.marimo}
rows = [[1, 2], [3], [4, 5, 6]]
print([*row for row in rows])  # flattens the list of lists
```

Before 3.15, you had to write `[x for row in rows for x in row]`.

## 8. Neighbors and chunks with `itertools`

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

## 9. A finance example: the best day

Put the pieces together: `pairwise` for the returns, `enumerate` for the day numbers, and tuple comparison to find the best day. `:+.1%` shows a number as a percent with a sign.

```python {.marimo}
_closes = [100.0, 104.0, 101.4, 106.47, 105.0]
_returns = [b / a - 1 for a, b in pairwise(_closes)]
print([f"{r:+.1%}" for r in _returns])
_best_return, _best_day = max((r, day) for day, r in enumerate(_returns, start=1))
print(f"Best: day {_best_day}, {_best_return:+.1%}")
```

**Question:** `max` compares the tuples `(r, day)`. Why does that find the best return? What would `max((day, r) ...)` find instead?

## AI activity: which is clearer?

1. Write `[x for row in rows for x in row]` and `[*row for row in rows]` side by side. Ask an AI which is clearer and why. Do you agree?
2. The unpacking form is new in Python 3.15, so the AI may not know it. If it says the second version is a syntax error, run it, and show the AI the result.
3. Ask it to rewrite the index loop from L11, section 7, with `zip`. Check that both versions print the same total.

## Exercises (40 minutes)

Open `l12_exercises.py` and run `uv run pytest lectures/12-tuples-comprehensions` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `min_max`, `squares_of_evens` |
| Core | `pairwise_sums`, `flatten`, `period_returns`, `in_batches` |
| Fix the AI's code | `total_value` |
| Stretch | `longest_streak`, `best_performers` |
