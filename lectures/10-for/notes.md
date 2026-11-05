---
title: "L10: for loops and accumulation"
marimo-version: "0.25.2"
---

# L10: `for` loops and accumulation

**By the end of this lecture you can:**

- loop over a range, a string, or a list
- use the accumulator pattern
- use `enumerate` instead of index arithmetic

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. `for` loops over a sequence

```python {.marimo}
for letter in "abc":
    print(letter)
```

## 2. `range`

**Predict** each one before you run:

```python {.marimo}
print(list(range(5)))
print(list(range(2, 6)))
print(list(range(10, 0, -3)))
```

## 3. The accumulator pattern

Start with an identity value (`0` for sums, `1` for products, `""` or `[]` for building things up), then update it on every step.

```python {.marimo}
def sum_of_squares(n: int) -> int:
    total = 0
    for k in range(1, n + 1):
        total += k * k
    return total


print(sum_of_squares(10), "formula:", 10 * 11 * 21 // 6)
```

## 4. Counting

```python {.marimo}
def count_vowels(text: str) -> int:
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


print(count_vowels("Baruch College"))
```

## 5. `enumerate`: the index and the value together

```python {.marimo}
tickers = ["AAPL", "MSFT", "NVDA"]
for position, ticker in enumerate(tickers, start=1):
    print(f"{position}. {ticker}")
```

## 6. `for` or `while`?

- Use **`for`** when you know what you're looping over.
- Use **`while`** when you're looping *until* something happens.

## AI activity

Write `sum_of_squares` with a `for` loop. Then ask an AI for a one-line version. Do you understand the one-liner well enough to explain it to a classmate? If not, ask the AI to walk you through it.

**Exercises:** `l10_exercises.py`
