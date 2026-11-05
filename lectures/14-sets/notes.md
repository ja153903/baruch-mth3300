---
title: "L14: Sets, counting, midterm review"
marimo-version: "0.25.2"
---

# L14: Sets, counting, midterm review

**By the end of this lecture you can:**

- use sets for uniqueness and fast membership tests
- count things with `collections.Counter`
- pick the right data structure for a problem

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Sets

A set is an **unordered** collection with **no duplicates**.

```python {.marimo}
visits = ["AAPL", "MSFT", "AAPL", "NVDA", "MSFT"]
unique = set(visits)
print(unique, len(unique), "AAPL" in unique)
```

## 2. Set operations

```python {.marimo}
mine = {"AAPL", "MSFT", "NVDA"}
yours = {"MSFT", "TSLA"}
print(mine & yours, mine | yours, mine - yours)
```

## 3. `Counter`

```python {.marimo}
from collections import Counter

counts = Counter("mississippi")
print(counts, counts.most_common(2))
```

## 4. Choosing a data structure

| You need… | Use |
|---|---|
| an ordered sequence that can change | `list` |
| a fixed group of values | `tuple` |
| a lookup from key to value | `dict` |
| uniqueness, or fast `in` checks | `set` |
| counts | `Counter` |

## 5. Midterm review: predict the output

```python {.marimo}
review_data = [3, 1, 3, 2]
print(sorted(set(review_data)))
print({x: review_data.count(x) for x in review_data})
print(review_data[1:3], review_data[::-1])
print([x * 2 for x in review_data if x > 1])
```

## AI activity: make your own practice exam

Ask an AI: *"Write five 'predict the output' Python questions on lists, dicts, and sets for an intro course, with the answers hidden at the end."* Do them **without running the code**, then check yourself. Bring any you missed to office hours.

**Exercises:** `l14_exercises.py`
