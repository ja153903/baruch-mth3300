---
title: "L11: Lists and slicing"
marimo-version: "0.25.2"
---

# L11: Lists and slicing

**By the end of this lecture you can:**

- create, index, slice, and change lists
- explain the difference between **changing** a list and **making a new** one
- explain aliasing

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Lists hold sequences of values

```python {.marimo}
prices = [101.5, 99.0, 103.25, 98.75]
print(prices[0], prices[-1], prices[1:3], len(prices))
print(max(prices), min(prices), sum(prices) / len(prices))
```

## 2. Lists are mutable

Unlike strings, lists **can** change in place.

```python {.marimo}
watchlist = ["AAPL", "MSFT"]
watchlist.append("NVDA")
watchlist[0] = "GOOG"
watchlist.remove("MSFT")
print(watchlist)
```

## 3. Changing a list vs. making a new one

```python {.marimo}
nums = [3, 1, 2]
print(sorted(nums), nums)  # sorted() returns a NEW list
nums.sort()  # .sort() changes nums and returns None
print(nums)
```

## 4. Aliasing

**Predict:** what does this print?

```python {.marimo}
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

`b = a` doesn't copy the list. It gives the **same list** a second name. To copy it, write `a.copy()` or `a[:]`.

```python {.marimo}
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(original, copied)
```

## 5. Building a list with a loop

```python {.marimo}
def above(xs: list[float], threshold: float) -> list[float]:
    result = []
    for x in xs:
        if x > threshold:
            result.append(x)
    return result


print(above(prices, 100))
```

## AI activity

Ask an AI to explain aliasing with a diagram. Then draw your own diagram for the "Predict" cell above, and compare the two.

**Exercises:** `l11_exercises.py`
