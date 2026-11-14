---
title: "L18: Searching and sorting"
marimo-version: "0.25.2"
---

# L18: Searching and sorting

**By the end of this lecture you can:**

- implement linear search, and count its steps
- explain binary search, and why it needs sorted data
- implement selection sort, and trace it by hand
- describe how insertion sort and merge sort work
- sort by a key with `sorted(..., key=...)`
- explain why sorted data makes searching faster

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L17)

**Predict** what this prints. Trace the calls on paper first.

```python {.marimo}
def _mystery(n: int) -> str:
    if n < 2:
        return str(n)
    return _mystery(n // 2) + str(n % 2)


print(_mystery(6))
```

## 1. Linear search

Check every element in turn. It works on any list.

```python {.marimo}
def linear_search(xs: list[int], target: int) -> int:
    for i, x in enumerate(xs):
        if x == target:
            return i
    return -1


print(linear_search([7, 3, 9, 1], 9), linear_search([7, 3, 9, 1], 4))
```

In the worst case, when the target is last or missing, linear search checks all n items.

### Common bug: using `-1` as an index

`-1` means "not found" here, but `xs[-1]` is a real item: the last one. Check for `-1` before you use the result.

```python {.marimo}
_xs = [7, 3, 9, 1]
_i = linear_search(_xs, 4)
print(_xs[_i])  # 4 isn't in the list, but this still prints something
if _i == -1:
    print("not found")
```

## 2. Binary search

This needs a **sorted** list. Each step throws away half of what's left, like looking up a word in a dictionary.

Play "guess my number" from 1 to 100. Each answer of "higher" or "lower" halves the range, so 7 guesses are always enough.

```python {.marimo}
def binary_search_steps(xs: list[int], target: int) -> int:
    lo, hi, steps = 0, len(xs) - 1, 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if xs[mid] == target:
            break
        if xs[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return steps


million = list(range(1_000_000))
print("binary search steps for 1,000,000 items:", binary_search_steps(million, 765_432))
```

**Predict:** about how many steps would a linear search need for the same target?

Each step halves the range, so n items take at most about log₂(n) steps:

```python {.marimo}
for _n in [100, 1_000, 1_000_000, 1_000_000_000]:
    _steps = 0
    _left = _n
    while _left > 0:
        _left //= 2
        _steps += 1
    print(f"{_n:>13,} items: at most {_steps} steps")
```

### Common bug: binary search on unsorted data

Python's `bisect` module does binary search for you. `bisect_left(xs, x)` gives the position where `x` is, or where it would go. On unsorted data, it gives a wrong answer, with no error:

```python {.marimo}
from bisect import bisect_left

_sorted = [1, 3, 7, 9]
_unsorted = [7, 3, 9, 1]
print(bisect_left(_sorted, 7), _sorted[bisect_left(_sorted, 7)])
print(bisect_left(_unsorted, 7), _unsorted[bisect_left(_unsorted, 7)])
```

## 3. Selection sort

Repeatedly find the smallest remaining element and move it to the front. **Predict** what the list looks like after pass 3, then run it.

```python {.marimo}
def selection_sort(xs: list[int]) -> list[int]:
    result = xs.copy()
    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
        print(f"pass {i + 1}: {result}")
    return result


print(selection_sort([5, 2, 9, 1, 5, 6]))
```

The swap line uses tuple unpacking from L12. How much work is it? Pass 1 compares n − 1 pairs, pass 2 compares n − 2, and so on, for n(n − 1)/2 comparisons in all, whatever the input. For 1,000 items, that's 499,500.

## 4. Insertion sort: a hand of cards

Pick up cards one at a time. Slide each new card left, past the bigger ones, until it's in place. The cards on the left are always sorted. Trace `[5, 2, 9, 1]`:

| Step | Insert | Sorted so far |
|---|---|---|
| start | 5 | `[5]` |
| 1 | 2 | `[2, 5]` |
| 2 | 9 | `[2, 5, 9]` |
| 3 | 1 | `[1, 2, 5, 9]` |

When the list is already almost sorted, each card moves only a step or two, so insertion sort is fast. You'll write it in the exercises.

## 5. Merge sort: the idea

1. Split the list in half.
2. Sort each half (recursively).
3. **Merge** the two sorted halves, by repeatedly taking the smaller front element.

```text
[5, 2, 9, 1, 5, 6]
[5, 2, 9]   [1, 5, 6]      split, again and again, down to lists of one
[2, 5, 9]   [1, 5, 6]      merge the pieces back together
[1, 2, 5, 5, 6, 9]         merge the two halves
```

To merge `[2, 5, 9]` and `[1, 5, 6]` by hand, compare the fronts. 1 < 2, so take 1. Then 2 < 5, so take 2. Keep going until one list is empty, then copy the rest of the other.

The list splits in half about log₂(n) times, and each level of merging touches all n items. So merge sort takes about n · log₂(n) steps. You'll build it in homework 10.

## 6. Sorting in practice

`key=` tells `sorted` what to compare. It takes a function, calls it on each item, and sorts by the results:

```python {.marimo}
people = [("Ada", 36), ("Alan", 41), ("Grace", 85)]


def age(person: tuple[str, int]) -> int:
    return person[1]


print(sorted(people, key=age, reverse=True))
print(sorted(people, key=lambda p: p[1], reverse=True))
```

A `lambda` is a small function with no name: `lambda p: p[1]` does the same thing as `age`. Use it for one-line keys. `min` and `max` take `key=` too:

```python {.marimo}
print(max(people, key=age), min(people, key=lambda p: len(p[0])))
```

Python's built-in `sorted` uses **Timsort**, a hybrid of merge sort and insertion sort. Use it in real code. Write your own sorts only to learn how they work.

### Ties keep their order

Python's sort is **stable**: items that compare equal stay in their original order. **Predict:**

```python {.marimo}
_trades = [("MSFT", 5), ("AAPL", 10), ("NVDA", 5), ("TSLA", 10)]
print(sorted(_trades, key=lambda t: t[1]))
```

### Common bug: sorting numbers stored as strings

Data from a CSV file arrives as strings (L16). **Predict:**

```python {.marimo}
_prices = ["10.50", "9.99", "100.00"]
print(sorted(_prices))
print(sorted(_prices, key=float))
```

Strings compare one character at a time, so `"100.00"` comes before `"9.99"`, however long the number is.

## 7. A finance example: ranking a portfolio

```python {.marimo}
_holdings = {"AAPL": 2286.0, "MSFT": 2051.25, "NVDA": 960.0, "TSLA": 2051.25}
_ranked = sorted(_holdings.items(), key=lambda item: item[1], reverse=True)
for _rank, (_ticker, _value) in enumerate(_ranked, start=1):
    print(f"{_rank}. {_ticker:<5} {_value:>9,.2f}")
```

**Question:** MSFT and TSLA tie. Why does MSFT come first? How would you break ties alphabetically on purpose?

## 8. Why sorted data pays off

Sorting costs about n · log₂(n) steps, once. After that, every search takes about log₂(n) steps instead of n.

| n | one linear search | one binary search | sorting once |
|---|---|---|---|
| 1,000 | 1,000 | 10 | about 10,000 |
| 1,000,000 | 1,000,000 | 20 | about 20,000,000 |

If you'll search a big list many times, sort it first. And sort it with a fast sort: compare the comparisons selection sort needs with merge sort's n · log₂(n).

```python {.marimo}
import math

for _n in [1_000, 1_000_000]:
    _selection = _n * (_n - 1) // 2
    _merge = round(_n * math.log2(_n))
    print(f"n = {_n:>9,}: selection {_selection:>15,}, merge {_merge:>11,}")
```

L19 makes this kind of counting precise.

## AI activity: check each step

1. Ask an AI to visualize binary search on `[1, 3, 5, 7, 9, 11, 13]` for target `11`, step by step. Check each step against `binary_search_steps`.
2. Ask it what happens when the list isn't sorted. Then test its answer with `bisect_left` on a list of your own.

## Exercises (40 minutes)

Open `l18_exercises.py` and run `uv run pytest lectures/18-search-sort` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `count_occurrences`, `last_index` |
| Core | `insertion_sort`, `sort_by_value`, `count_inversions`, `closest` |
| Fix the AI's code | `bubble_sort` |
| Stretch | `two_sum_sorted` |
