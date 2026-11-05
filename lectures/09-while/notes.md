---
title: "L09: while loops"
marimo-version: "0.25.2"
---

# L09: `while` loops

**By the end of this lecture you can:**

- repeat code while a condition holds
- trace a loop by hand
- spot and fix infinite loops

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. The shape of a `while` loop

```python {.marimo}
countdown = 3
while countdown > 0:
    print(countdown)
    countdown = countdown - 1
print("liftoff")
```

Every loop needs three things: **initialize** a variable, **test** it, and **update** it. Forget the update and the loop runs forever. (Press Ctrl-C to stop it.)

## 2. Trace it by hand

**Predict:** what does `digits(3300)` return? Fill in a table with columns for `n` and `count` for each step.

```python {.marimo}
def digits(n: int) -> int:
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


print(digits(3300))
```

**Predict:** what about `digits(0)`? Is that the answer we want?

## 3. When you don't know how many steps it takes

How many years until money doubles at 7% a year?

```python {.marimo}
def years_to_double(rate: float) -> int:
    balance = 1.0
    years = 0
    while balance < 2:
        balance *= 1 + rate
        years += 1
    return years


print(years_to_double(0.07), "vs. the rule of 72:", 72 / 7)
```

## 4. `break`

```python {.marimo}
def first_divisor(n: int) -> int:
    d = 2
    while True:
        if n % d == 0:
            break
        d += 1
    return d


print(first_divisor(91), first_divisor(97))
```

## AI activity

Ask an AI: *"Give me a Python `while` loop with a subtle bug that makes it run forever. Don't tell me the bug."* Find the bug by tracing the loop by hand.

**Exercises:** `l09_exercises.py`
