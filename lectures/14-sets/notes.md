---
title: "L14: Sets, counting, midterm review"
marimo-version: "0.25.2"
---

# L14: Sets, counting, midterm review

**By the end of this lecture you can:**

- use sets for uniqueness and fast membership tests
- combine sets with `&`, `|`, `-`, and `^`
- count things with `collections.Counter`
- pick the right data structure for a problem
- trace, debug, and write short functions by hand, as on the midterm

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L13)

**Predict** the dict and its length:

```python {.marimo}
_counts = {}
for _ch in "banana":
    _counts[_ch] = _counts.get(_ch, 0) + 1
print(_counts, len(_counts))
```

## 1. Sets

A set is an **unordered** collection with **no duplicates**.

```python {.marimo}
visits = ["AAPL", "MSFT", "AAPL", "NVDA", "MSFT"]
unique = set(visits)
print(unique, len(unique), "AAPL" in unique)
```

Your set may print in a different order from your neighbor's. A set has no order, so you can't index it: `unique[0]` is an error. Use `sorted(unique)` when you need an order.

```python {.marimo}
_seen = {3, 1}
_seen.add(4)
_seen.add(1)  # already there, so nothing changes
_seen.discard(3)
print(sorted(_seen), len(_seen))
```

`.remove(x)` raises a `KeyError` if `x` isn't in the set. `.discard(x)` doesn't.

### Common bug: `{}` is an empty dict

**Predict:**

```python {.marimo}
print(type({}), type(set()), type({1, 2}))
```

Write `set()` for an empty set.

## 2. Set operations

```python {.marimo}
mine = {"AAPL", "MSFT", "NVDA"}
yours = {"MSFT", "TSLA"}
print(mine & yours, mine | yours, mine - yours)
```

| Operator | Name | Gives the items… |
|---|---|---|
| `a & b` | intersection | in both |
| `a \| b` | union | in either one |
| `a - b` | difference | in `a` but not in `b` |
| `a ^ b` | symmetric difference | in exactly one of them |
| `a <= b` | subset | `True` if everything in `a` is also in `b` |

**Predict** each line. The `sorted` calls make the order the same for everyone.

```python {.marimo}
print(sorted(mine ^ yours))
print({"MSFT"} <= mine, mine <= yours)
print(sorted(set("hello") & set("world")))
```

## 3. The "seen" pattern

To spot the first repeat, or to keep only the first copy of each item, keep a set of everything you've seen so far:

```python {.marimo}
def first_repeat(tickers: list[str]) -> str | None:
    seen: set[str] = set()
    for t in tickers:
        if t in seen:
            return t
        seen.add(t)
    return None


print(first_repeat(visits), first_repeat(["AAPL", "MSFT"]))
```

`t in seen` is fast on a set, however big the set gets. On a list, Python checks the items one at a time. L19 measures the difference.

## 4. Set comprehensions

Curly braces around a single expression build a set:

```python {.marimo}
_tickers = ["AAPL", "MSFT", "NVDA", "GOOG"]
print({len(t) for t in _tickers})
print(sorted({t[0] for t in _tickers}))
```

## 5. `Counter`

```python {.marimo}
from collections import Counter

counts = Counter("mississippi")
print(counts, counts.most_common(2))
```

A `Counter` is a dict that does the counting pattern from L13 in one line. A missing key counts as 0, instead of raising a `KeyError`:

```python {.marimo}
_by_ticker = Counter(["AAPL", "MSFT", "AAPL", "NVDA", "AAPL", "MSFT"])
print(_by_ticker["AAPL"], _by_ticker["TSLA"])
_by_ticker["TSLA"] += 1
print(_by_ticker.most_common(1), sum(_by_ticker.values()))
```

### A simulation: rolling two dice

With `random` from L09, a `Counter` shows the shape of a distribution. A sum of 7 is the most likely, with probability 6/36, and 2 and 12 are the least likely, with 1/36 each.

```python {.marimo}
import random

random.seed(3300)
_sums = Counter(random.randint(1, 6) + random.randint(1, 6) for _ in range(36_000))
for _total in range(2, 13):
    print(f"{_total:>2} {_sums[_total]:>5} {'#' * (_sums[_total] // 200)}")
```

## 6. Choosing a data structure

| You need… | Use |
|---|---|
| an ordered sequence that can change | `list` |
| a fixed group of values | `tuple` |
| a lookup from key to value | `dict` |
| uniqueness, or fast `in` checks | `set` |
| counts | `Counter` |

**Which would you use?**

- the closing prices for the last 30 days, in order
- whether a ticker is on a "do not trade" list
- each employee's salary, looked up by name
- a (latitude, longitude) pair
- how many times each word appears in a report

## 7. Midterm review: predict the output

The midterm is like the quizzes: tracing, debugging, and writing code by hand, with no AI and no notes. **Predict** each cell before you run it.

```python {.marimo}
review_data = [3, 1, 3, 2]
print(sorted(set(review_data)))
print({x: review_data.count(x) for x in review_data})
print(review_data[1:3], review_data[::-1])
print([x * 2 for x in review_data if x > 1])
```

```python {.marimo}
def _shout(word: str, times: int = 2) -> str:
    return (word.upper() + "!") * times


_word = "Baruch"
print(_word[1:4], _word[-1], len(_word))
print(_shout("hi"), _shout("go", 3))
_total = 0
for _i in range(1, 10, 2):
    _total += _i
print(_total)
```

```python {.marimo}
_xs = [1, 2, 3]
_ys = _xs
_ys = _ys + [4]
_xs.append(5)
print(_xs, _ys)

_n = 100
_steps = 0
while _n > 1:
    _n //= 3
    _steps += 1
print(_n, _steps)
```

## 8. Midterm review: find the bug

Each function has one bug. For each one, find an input that shows the bug, and the one-line change that fixes it.

```python {.marimo}
def largest(xs: list[int]) -> int:
    """The largest number in xs, which is not empty."""
    best = 0
    for x in xs:
        if x > best:
            best = x
    return best


def exclaim(text: str) -> str:
    """text in capital letters, with an exclamation mark at the end."""
    text.upper()
    return text + "!"


print(largest([3, 9, 4]), largest([-5, -2, -8]))
print(exclaim("buy"))
```

## 9. Midterm review: write it by hand

Write each function on paper first. Then type it in and test it. On paper, the logic matters most: on the quizzes, small syntax slips like a missing colon don't cost points.

1. `count_vowels(text)`: how many vowels are in `text`.
2. `evens(xs)`: a new list of the even numbers in `xs`, in order. Write it once with a loop and once with a comprehension.
3. `as_hours(minutes)`: turns `135` into `"2h 15m"`.
4. `total_by_ticker(trades)`: from a list of `(ticker, shares)` tuples, a dict of the total shares for each ticker.

For more practice, try `exams/practice-midterm.md` and the problems in `practice/`.

## AI activity: a skill for practice exams

Turn your exam prep into a skill you can reuse before every exam.

1. Create a `practice-quiz` skill in `.agents/skills/` and `.github/skills/`. Its instructions should tell the AI to write five "predict the output" questions on the topics you name, using only features from this course, with the answers hidden until you ask for them.
2. Write the description carefully. It's the only part the AI reads before deciding whether to use the skill. Try *"quiz me on dicts"* and *"give me practice problems on sets"*. If the skill doesn't load for one of them, add those words to the description.
3. Do the questions **without running the code**, then check yourself. Bring any you missed to office hours.
4. Run `uv run pytest lectures/10-loop-patterns` to check the skill's format.

## Exercises (40 minutes)

Open `l14_exercises.py` and run `uv run pytest lectures/14-sets` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `has_duplicates`, `missing_numbers` |
| Core | `common_elements`, `jaccard`, `most_traded`, `duplicates` |
| Fix the AI's code | `unique_in_order` |
| Stretch | `can_spell` |
