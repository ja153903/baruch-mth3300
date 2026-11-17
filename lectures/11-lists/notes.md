---
title: "L11: Lists and slicing"
marimo-version: "0.25.2"
---

# L11: Lists and slicing

**By the end of this lecture you can:**

- create, index, and slice lists
- change a list in place with `append`, `insert`, `pop`, and `remove`
- explain the difference between **changing** a list and **making a new** one
- explain aliasing, and copy a list when you need to
- build a new list with a loop
- store a table as a list of lists

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L10)

**Predict** the output before you run it. Which values of `_k` does the loop see?

```python {.marimo}
_count = 0
for _k in range(1, 20, 3):
    if _k % 2 == 0:
        _count += 1
print(_count)
```

## 1. Lists hold sequences of values

A list keeps values in order. Write it with square brackets, and put commas between the items. Many functions you already know work on lists.

```python {.marimo}
prices = [101.5, 99.0, 103.25, 98.75]
print(prices[0], prices[-1], prices[1:3], len(prices))
print(max(prices), min(prices), sum(prices) / len(prices))
```

A list can be empty, `[]`, and it can hold values of any type. Usually all the items have the same type, and the type hint says which one: `list[float]`, `list[str]`.

## 2. Indexing and slicing

Lists follow the same rules as strings (L03). Positions start at 0, negative indexes count from the end, and a slice stops **before** its stop.

**Predict** each line:

```python {.marimo}
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days[1:4])
print(days[-2:])
print(days[::2])
print(days[::-1])
```

An index past the end is an error. A slice past the end just stops early. `in` checks whether a value is in the list, and `.index` finds its position.

```python {.marimo}
print(days[3:100], days[7:9])
print("Wed" in days, "Sat" in days, days.index("Wed"))
```

Try `days[7]` in the REPL and read the error message.

## 3. Lists are mutable

Unlike strings, lists **can** change in place.

```python {.marimo}
watchlist = ["AAPL", "MSFT"]
watchlist.append("NVDA")
watchlist[0] = "GOOG"
watchlist.remove("MSFT")
print(watchlist)
```

| Method | What it does |
|---|---|
| `xs.append(x)` | adds `x` at the end |
| `xs.insert(i, x)` | adds `x` at position `i` |
| `xs.pop()` | removes the last item and returns it |
| `xs.pop(i)` | removes the item at position `i` and returns it |
| `xs.remove(x)` | removes the first copy of `x` |
| `xs.extend(ys)` | adds every item of `ys` at the end |

**Predict:**

```python {.marimo}
_queue = ["a", "b", "c"]
_queue.insert(0, "z")
_last = _queue.pop()
_first = _queue.pop(0)
print(_queue, _last, _first)
```

### Common bug: `append` vs. `extend`

```python {.marimo}
_a = [1, 2]
_a.append([3, 4])
_b = [1, 2]
_b.extend([3, 4])
print(_a, len(_a))
print(_b, len(_b))
```

`append` always adds **one** item, even when that item is a whole list.

## 4. Changing a list vs. making a new one

```python {.marimo}
nums = [3, 1, 2]
print(sorted(nums), nums)  # sorted() returns a NEW list
nums.sort()  # .sort() changes nums and returns None
print(nums)
```

Both take `reverse=True` to sort from largest to smallest. `+` and slicing make new lists too, so the original stays the same:

```python {.marimo}
_scores = [88, 92, 75]
_longer = _scores + [100]
_top_two = sorted(_scores, reverse=True)[:2]
print(_scores, _longer, _top_two)
```

### Common bug: saving the result of `.sort()`

**Predict:**

```python {.marimo}
_grades = [88, 92, 75]
_grades = _grades.sort()
print(_grades)
```

A method that changes a list returns `None`. Either call `xs.sort()` on its own line, or write `xs = sorted(xs)`.

## 5. Aliasing

**Predict:** what does this print?

```python {.marimo}
a = [1, 2, 3]
b = a
b.append(4)
print(a, a is b)
```

`b = a` doesn't copy the list. It gives the **same list** a second name, and `is` checks for exactly that. To copy a list, write `a.copy()` or `a[:]`.

```python {.marimo}
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(original, copied, original is copied)
```

### Functions get the same list, not a copy

When you pass a list to a function, the function can change the caller's list:

```python {.marimo}
def charge_fee(balances: list[float], fee: float) -> None:
    for i in range(len(balances)):
        balances[i] -= fee


accounts = [100.0, 250.0, 40.0]
charge_fee(accounts, 5.0)
print(accounts)
```

That's fine when changing the list is the function's whole job, and its name says so. Otherwise, a function should leave its arguments alone. When an exercise says "Don't change xs", build and return a new list.

### Common bug: changing the loop variable

**Predict:** does this double every holding?

```python {.marimo}
_shares = [10, 20, 30]
for _n in _shares:
    _n = _n * 2
print(_shares)
```

`_n` is a name for each item in turn. Giving `_n` a new value doesn't change the list. To change the list, assign to a position, as `charge_fee` does with `balances[i]`.

## 6. Building a new list with a loop

The accumulator pattern from L09 works for lists too: start with `[]`, and `append` inside the loop.

```python {.marimo}
def above(xs: list[float], threshold: float) -> list[float]:
    result = []
    for x in xs:
        if x > threshold:
            result.append(x)
    return result


print(above(prices, 100))
```

## 7. A finance example: parallel lists

Two lists of the same length can describe one portfolio. `shares[i]` goes with `share_prices[i]`.

```python {.marimo}
tickers = ["AAPL", "MSFT", "NVDA"]
shares = [10, 5, 8]
share_prices = [190.50, 410.25, 120.00]

_values = []
for _i in range(len(tickers)):
    _values.append(shares[_i] * share_prices[_i])
    print(f"{tickers[_i]:<5} {_values[_i]:>9,.2f}")
print(f"Total {sum(_values):>9,.2f}")
```

**Question:** what goes wrong if `shares` is one item shorter than `tickers`? L12 shows a safer way to walk through two lists together.

## 8. Lists of lists

A table is a list of rows, and each row is a list. `table[r][c]` is row `r`, column `c`.

```python {.marimo}
quiz_scores = [
    [90, 85, 77],  # Ada
    [60, 75, 88],  # Alan
]
print(quiz_scores[1], quiz_scores[0][2], len(quiz_scores), len(quiz_scores[0]))
for _row in quiz_scores:
    print(f"{sum(_row) / len(_row):.1f}")
```

### Common bug: `[[0] * 3] * 2`

`*` repeats a list. **Predict:**

```python {.marimo}
_grid = [[0] * 3] * 2
_grid[0][0] = 99
print(_grid)
```

Both rows are the **same list**: aliasing again. Build each row separately instead:

```python {.marimo}
_grid = []
for _r in range(2):
    _grid.append([0] * 3)
_grid[0][0] = 99
print(_grid)
```

## 9. Strings and lists

`split` turns a string into a list of strings, and `join` turns a list of strings back into one string (L03). Convert each piece when you need numbers:

```python {.marimo}
_line = "190.50,410.25,120.00"
_pieces = _line.split(",")
_numbers = []
for _piece in _pieces:
    _numbers.append(float(_piece))
print(_pieces, sum(_numbers))
print(" | ".join(_pieces))
```

## AI activity: draw the boxes

1. Ask an AI to explain aliasing with a diagram. Then draw your own diagram for the **Predict** cell in section 5, and compare the two.
2. Ask it why both rows changed in `[[0] * 3] * 2`. Check its answer in the REPL with `grid[0] is grid[1]`.
3. If its diagram and yours disagree, which one matches what Python printed?

## Exercises (40 minutes)

Open `l11_exercises.py` and run `uv run pytest lectures/11-lists` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `last_n`, `price_range` |
| Core | `rotate`, `remove_all`, `apply_split`, `column` |
| Fix the AI's code | `top_three` |
| Stretch | `max_drawdown`, `transpose` |
