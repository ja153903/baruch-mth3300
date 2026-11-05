---
title: "L23: Building with AI"
marimo-version: "0.25.2"
---

# L23: Building with AI: spec, tests, generate, review

**By the end of this lecture you can:**

- write a spec precise enough that two people (or an AI) would build the same thing
- write tests from the spec *before* you see any code
- judge AI-written code with tests, a review checklist, and measurement
- check a fast version against a slow, obviously correct one on random inputs

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup

An AI wrote this to find the average of a list. **Predict** the output for each call, including any errors:

```python {.marimo}
def average(xs: list[float]) -> float:
    return sum(xs) / len(xs)


print(average([1, 2, 3, 4]))
try:
    print(average([]))
except ZeroDivisionError as error:
    print("crashed:", error)
```

Is crashing on `[]` a bug? You can't tell without a **spec**. The spec decides what correct means, not the code.

## 1. The loop

From now on, you'll build code with AI in this order:

1. **Spec:** what goes in, what comes out, and what happens on edge cases and bad input.
2. **Tests:** written from the spec, *before* any code exists.
3. **Generate:** ask the AI for code that meets the spec.
4. **Review:** read every line. Can you explain it? Does it use things that really exist?
5. **Run and measure:** run the tests, and check any claim (about speed, for example) yourself.

Why tests *before* code? Once you've read code that looks right, you start testing what it does instead of what it *should* do.

## 2. Writing a spec

A vague request: *"write a function that checks for leap years."* A spec:

```python
def is_leap(year: int) -> bool:
    """True if year is a leap year in the Gregorian calendar.

    A year is a leap year if it is divisible by 4, except that years divisible
    by 100 are not, except that years divisible by 400 are.

    is_leap(2024) == True     # divisible by 4
    is_leap(2023) == False
    is_leap(1900) == False    # divisible by 100
    is_leap(2000) == True     # divisible by 400
    """
```

A good spec has: **types**, **the rule**, **examples**, and **edge cases**. Each example covers a different branch of the rule.

## 3. Tests from the spec

A check function takes any candidate implementation and returns what went wrong. That way we can test several candidates against the same spec.

```python {.marimo}
from collections.abc import Callable


def check_is_leap(is_leap: Callable[[int], bool]) -> list[str]:
    failures = []
    for year, expected in [
        (2024, True),
        (2023, False),
        (1900, False),
        (2000, True),
        (2100, False),
    ]:
        if is_leap(year) != expected:
            failures.append(f"is_leap({year}) should be {expected}")
    return failures
```

## 4. Three candidates

Suppose three AI chats gave us three answers. All of them look reasonable. **Before you run the cell**, read each one and predict which checks it fails.

```python {.marimo}
def candidate_a(year: int) -> bool:
    return year % 4 == 0


def candidate_b(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0


def candidate_c(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


for _name, _candidate in [("A", candidate_a), ("B", candidate_b), ("C", candidate_c)]:
    _failures = check_is_leap(_candidate)
    print(_name, "passes" if not _failures else _failures)
```

A test that only checked 2024 and 2023 would pass all three. **Tests are only as good as their edge cases.**

## 5. Ambiguous specs

Ask an AI for `second_largest(xs)`. What should `second_largest([5, 5, 3])` return: `5` or `3`? The request didn't say, so the AI guessed. Here are two reasonable answers:

```python {.marimo}
def second_largest_by_position(xs: list[int]) -> int:
    return sorted(xs)[-2]


def second_largest_distinct(xs: list[int]) -> int:
    return sorted(set(xs))[-2]


print(second_largest_by_position([5, 5, 3]), second_largest_distinct([5, 5, 3]))
```

Neither one is wrong. The **spec** was incomplete. When an AI's answer surprises you, check whether your spec actually said what you meant.

**Quick check:** what does each version do with `[7]`? Add a line to the spec that decides it.

## 6. Reviewing code

Tests catch wrong answers. A review catches what tests miss. For every piece of AI code, ask:

- **Can I explain every line?** If not, ask until you can, or don't use it.
- **Does everything it calls exist?** AI tools sometimes invent functions that sound right.
- **Does it handle the edge cases the spec names?** An empty list, zero, a negative number, bad input.
- **Does it use only what I need?** A 40-line answer to a 5-line problem is a warning sign.

Checking whether a function exists takes one line:

```python {.marimo}
import statistics

print(hasattr(statistics, "fmean"), hasattr(statistics, "weighted_average"))
```

`statistics.fmean` is real. `statistics.weighted_average` is the kind of name an AI might make up.

## 7. Measure claims

AI tools often say things like "this version is much faster." Don't argue; measure it, the way we did in L19.

```python {.marimo}
import time


def count_common_lists(a: list[int], b: list[int]) -> int:
    return len([x for x in a if x in b])


def count_common_sets(a: list[int], b: list[int]) -> int:
    b_set = set(b)
    return len([x for x in a if x in b_set])


_a = list(range(0, 6000, 2))
_b = list(range(0, 6000, 3))
for _fn in [count_common_lists, count_common_sets]:
    _start = time.perf_counter()
    _result = _fn(_a, _b)
    print(f"{_fn.__name__}: {_result} in {time.perf_counter() - _start:.4f}s")
```

Both give the same answer. Checking that the answers match matters as much as the timing: a fast wrong answer is worthless.

## 8. Slow and obviously correct vs. fast and clever

When an AI gives you a clever, fast version, write (or ask for) the slowest version you're **sure** is correct. Then compare them on many random inputs. If they ever disagree, at least one of them is wrong, and you have a failing input to study.

```python {.marimo}
import random


def max_gap_slow(xs: list[int]) -> int:
    """The largest difference between any two values: obviously correct, O(n²)."""
    best = 0
    for x in xs:
        for y in xs:
            best = max(best, x - y)
    return best


def max_gap_fast(xs: list[int]) -> int:
    """The same thing in O(n), as an AI might write it. Is it right?"""
    return max(xs) - min(xs) if len(xs) > 1 else xs[0]


def find_disagreement(trials: int, seed: int) -> list[int] | None:
    rng = random.Random(seed)
    for _ in range(trials):
        xs = [rng.randint(-10, 10) for _ in range(rng.randint(1, 6))]
        if max_gap_slow(xs) != max_gap_fast(xs):
            return xs
    return None


print(find_disagreement(1000, seed=3300))
```

The random search found an input where the two disagree. **Which one is wrong, and why?** Fix it, and rerun the search.

## 9. Log it

Every one of these steps is worth a line in `AI_LOG.md`: what you asked, what it gave you, and what your tests or measurements showed. "My tests caught the AI's bug on 1900" is exactly the kind of entry that shows you're in charge of the code.

## AI activity: the full loop, live

As a class, pick a spec from the list below. Write the tests **first**, together. Then ask an AI for the code, run the tests, and review it with the checklist from section 6.

- `is_palindrome(text)`, ignoring case, spaces, and punctuation
- `clamp(x, low, high)`, which raises `ValueError` if `low > high`
- `parse_time("2:05 PM")`, which returns minutes after midnight

## Exercises (40 minutes)

The AI tier for this lecture is **pair programmer**. You may use AI for the implementations, but write the `check_` functions yourself: they're how you know the AI's code is right.

Open `l23_exercises.py` and run `uv run pytest lectures/23-building-with-ai` as you go:

| Group | Functions |
|---|---|
| Implement from the spec | `median`, `normalize_spaces` |
| Write the checks | `check_median`, `check_normalize_spaces` |
| Slow vs. fast | `count_pairs_slow`, `count_pairs_fast`, `agree` |
| Fix the AI's code | `word_counts` |
