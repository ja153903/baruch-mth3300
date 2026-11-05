---
title: "L19: Big-O and profiling"
marimo-version: "0.25.2"
---

# L19: Big-O and profiling

**By the end of this lecture you can:**

- describe how running time grows with input size: O(1), O(log n), O(n), O(n²)
- measure running time instead of guessing
- use a profiler to find where time actually goes

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Growth rates

| Big-O | Example | n = 1,000 | n = 1,000,000 |
|---|---|---|---|
| O(1) | `d[key]`, `x in a_set` | 1 | 1 |
| O(log n) | binary search | ~10 | ~20 |
| O(n) | linear search, `sum` | 1,000 | 1,000,000 |
| O(n log n) | `sorted` | ~10,000 | ~20,000,000 |
| O(n²) | comparing every pair | 1,000,000 | 10¹² |

## 2. Measure it

```python {.marimo}
import time


def timed(fn, *args):
    start = time.perf_counter()
    fn(*args)
    return time.perf_counter() - start


def has_duplicate_pairs(xs: list[int]) -> bool:  # O(n²)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return True
    return False


def has_duplicate_set(xs: list[int]) -> bool:  # O(n)
    return len(set(xs)) != len(xs)


for size in [500, 1000, 2000]:
    data = list(range(size))
    print(
        f"n={size:>5}: pairs {timed(has_duplicate_pairs, data):.4f}s, set {timed(has_duplicate_set, data):.6f}s"
    )
```

**Predict:** when n doubles, what should happen to each time?

## 3. `in` on a list vs. a set

```python {.marimo}
big_list = list(range(1_000_000))
big_set = set(big_list)
print(f"list: {timed(lambda: 999_999 in big_list):.6f}s")
print(f"set:  {timed(lambda: 999_999 in big_set):.6f}s")
```

## 4. Profiling: where does the time go?

Python 3.15 ships with a **sampling profiler**. It checks what your program is doing thousands of times a second, and reports which functions it was in.

```sh
uv run python -m profiling.sampling run slow_program.py
```

Optimize the part the profiler points to, not the part you *think* is slow.

## AI activity

Ask an AI to make `has_duplicate_pairs` faster. **Before** you run its version, predict the speedup at n = 2,000. Then measure it. How close was your prediction? How close was the AI's claim?

**Exercises:** `l19_exercises.py`
