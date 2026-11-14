---
title: "L19: Big-O and profiling"
marimo-version: "0.25.2"
---

# L19: Big-O and profiling

**By the end of this lecture you can:**

- describe how running time grows with input size: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- find the Big-O of a function by reading its loops
- spot hidden loops, like `in` on a list
- measure running time instead of guessing
- use a profiler to find where time actually goes

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L18)

**Predict** both lines. Watch the words that have the same length.

```python {.marimo}
_words = ["kiwi", "fig", "apple", "date"]
print(sorted(_words, key=len))
print(sorted(_words, key=len, reverse=True))
```

## 1. Counting steps

Seconds depend on your computer. Instead, count the steps a function takes as the input size n grows:

```python {.marimo}
def steps_single(n: int) -> int:
    steps = 0
    for _ in range(n):
        steps += 1
    return steps


def steps_nested(n: int) -> int:
    steps = 0
    for _ in range(n):
        for _ in range(n):
            steps += 1
    return steps


def steps_halving(n: int) -> int:
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps
```

```python {.marimo}
for _n in [10, 100, 1000]:
    print(
        f"n = {_n:>4}: single {steps_single(_n):>4}, "
        f"nested {steps_nested(_n):>9,}, halving {steps_halving(_n)}"
    )
```

**Predict:** what happens to each count when n goes from 1,000 to 2,000?

## 2. Growth rates

| Big-O | Example | n = 1,000 | n = 1,000,000 |
|---|---|---|---|
| O(1) | `d[key]`, `x in a_set` | 1 | 1 |
| O(log n) | binary search | ~10 | ~20 |
| O(n) | linear search, `sum` | 1,000 | 1,000,000 |
| O(n log n) | `sorted` | ~10,000 | ~20,000,000 |
| O(n²) | comparing every pair | 1,000,000 | 10¹² |
| O(2ⁿ) | Tower of Hanoi (L17) | about 10³⁰¹ | a number with 301,030 digits |

Big-O keeps only the fastest-growing term, and it drops constant factors: 3n² + 5n + 2 is O(n²). For large n, the biggest term is all that matters:

```python {.marimo}
for _n in [10, 100, 1000, 10_000]:
    print(f"n = {_n:>6,}: 100n = {100 * _n:>9,}, n² = {_n * _n:>11,}")
```

**Predict:** for which values of n is 100n smaller than n²?

## 3. Reading Big-O from code

- One loop over the input: O(n).
- A loop inside a loop, both over the input: O(n²).
- A loop that halves what's left each time: O(log n).
- A few steps that don't depend on n: O(1).

**Predict** the Big-O of each function. For `num_digits`, n is the number itself.

```python {.marimo}
def first_item(xs: list[int]) -> int:
    return xs[0]


def zero_pairs(xs: list[int]) -> int:
    count = 0
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] + xs[j] == 0:
                count += 1
    return count


def num_digits(n: int) -> int:
    count = 1
    while n >= 10:
        n //= 10
        count += 1
    return count
```

### Common bug: the hidden loop

Some one-liners are loops in disguise. `x in a_list`, `a_list.count(x)`, `a_list.index(x)`, `a_list.remove(x)`, and `a_list.insert(0, x)` all walk through the list, so each one is O(n). Put one inside a loop, and the function becomes O(n²):

```python {.marimo}
def unique_slow(xs: list[int]) -> list[int]:
    result = []
    for x in xs:
        if x not in result:  # a hidden loop over result
            result.append(x)
    return result


def unique_fast(xs: list[int]) -> list[int]:
    seen: set[int] = set()
    result = []
    for x in xs:
        if x not in seen:  # O(1) on a set
            seen.add(x)
            result.append(x)
    return result


print(unique_slow([3, 1, 3, 2, 1]), unique_fast([3, 1, 3, 2, 1]))
```

## 4. Measure it

`timed(fn, *args)` calls `fn` with the arguments that come after it, and returns how many seconds that took.

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

Timings change from run to run and from computer to computer, so compare ratios, not exact numbers. This **doubling test** works for any function: double n, and divide the new time by the old one.

```python {.marimo}
_before = timed(has_duplicate_pairs, list(range(1000)))
_after = timed(has_duplicate_pairs, list(range(2000)))
print(f"2x the data took {_after / _before:.1f}x the time")
```

A ratio near 2 means O(n), and a ratio near 4 means O(n²).

## 5. `in` on a list vs. a set

```python {.marimo}
big_list = list(range(1_000_000))
big_set = set(big_list)
print(f"list: {timed(lambda: 999_999 in big_list):.6f}s")
print(f"set:  {timed(lambda: 999_999 in big_set):.6f}s")
```

Dict lookups are O(1) too. That's why the counting pattern from L13 stays fast on huge inputs.

## 6. A finance example: reconciling trades

Your records and your broker's should list the same trade IDs. Which of yours are missing from the broker's list? Here are a slow way and a fast way:

```python {.marimo}
def missing_slow(ours: list[int], theirs: list[int]) -> list[int]:
    return [t for t in ours if t not in theirs]


def missing_fast(ours: list[int], theirs: list[int]) -> list[int]:
    theirs_set = set(theirs)
    return [t for t in ours if t not in theirs_set]
```

```python {.marimo}
_ours = list(range(5_000))
_theirs = [t for t in _ours if t % 500 != 7]
for _name, _find in [("slow", missing_slow), ("fast", missing_fast)]:
    _start = time.perf_counter()
    _missing = _find(_ours, _theirs)
    _seconds = time.perf_counter() - _start
    print(f"{_name}: {len(_missing)} missing in {_seconds:.4f}s")
```

**Predict:** if both lists grow 10 times longer, about how much slower does each version get?

## 7. Profiling: where does the time go?

A real program has many functions, and you can't time each one by hand. A **profiler** times all of them at once.

Python 3.15 ships with two profilers. The **tracing profiler** records every function call, and it works on every computer:

```sh
uv run python -m profiling.tracing slow_program.py
```

You can also run it from Python code. Here it profiles a report that calls three helper functions:

```python {.marimo}
import profiling.tracing
import pstats


def load_prices(n: int) -> list[int]:
    return [(i * 7919) % 1000 for i in range(n)]


def distinct_prices(prices: list[int]) -> list[int]:
    return unique_slow(prices)


def average(prices: list[int]) -> float:
    return sum(prices) / len(prices)


def report(n: int) -> None:
    prices = load_prices(n)
    print(len(distinct_prices(prices)), "distinct prices, average", average(prices))
```

```python {.marimo}
_profiler = profiling.tracing.Profile()
_profiler.runcall(report, 50_000)
pstats.Stats(_profiler).strip_dirs().sort_stats("cumulative").print_stats(6)
```

`ncalls` is how many times each function ran. `tottime` is the time spent inside the function itself, and `cumtime` adds the time spent in the functions it called. Which function would you speed up first?

The **sampling profiler** checks what your program is doing thousands of times a second, and reports which functions it was in. It slows your program down much less, and it can draw a flame graph that you open in a browser. The widest bars are where the time goes.

```sh
uv run python -m profiling.sampling run slow_program.py
uv run python -m profiling.sampling run --flamegraph -o profile.html slow_program.py
```

On macOS, the sampling profiler may stop with a permission error. If it does, use the tracing profiler instead. To try the commands yourself, save `unique_slow` and the four functions above in `slow_program.py`, with `report(50_000)` at the bottom.

Optimize the part the profiler points to, not the part you *think* is slow.

## 8. Big-O of common operations

| Operation | Big-O |
|---|---|
| `xs[i]`, `xs.append(x)`, `xs.pop()` | O(1) |
| `x in xs`, `xs.index(x)`, `xs.insert(0, x)`, `xs.pop(0)` | O(n) |
| `x in s` for a set, `d[k]` for a dict | O(1) |
| `sorted(xs)`, `xs.sort()` | O(n log n) |
| `xs[a:b]`, `xs.copy()` | O(size of the copy) |

**Question:** `total(xs)` from L17 slices `xs[1:]` in every call. It looks like one pass through the list. What is its Big-O really?

## AI activity: check the speedup

Ask an AI to make `has_duplicate_pairs` faster. **Before** you run its version, predict the speedup at n = 2,000. Then measure it. How close was your prediction? How close was the AI's claim?

Then ask it for the Big-O of its version, and check that claim with the doubling test from section 4.

## Exercises (40 minutes)

Several tests use big inputs, so a slow solution takes seconds instead of milliseconds. Open `l19_exercises.py` and run `uv run pytest lectures/19-big-o` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `is_sorted`, `common_count` |
| Core | `has_pair_with_sum`, `new_highs`, `max_profit_slow` |
| Fix the AI's code | `max_profit` |
| Stretch | `range_sums`, `nearby_duplicate` |
