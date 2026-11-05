---
title: "L10: for loops and accumulation"
marimo-version: "0.25.2"
---

# L10: `for` loops and accumulation

**By the end of this lecture you can:**

- loop over a string, a list, or a `range`
- avoid off-by-one errors with `range`
- use the accumulator pattern to sum, count, and build up results
- use `enumerate` instead of index arithmetic
- run a small, reproducible random simulation
- choose between `for` and `while`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L09)

**Predict** the output before you run it. How many times does the loop body run?

```python {.marimo}
_n = 5
_steps = 0
while _n != 1:
    if _n % 2 == 0:
        _n = _n // 2
    else:
        _n = 3 * _n + 1
    _steps += 1
print(_steps)
```

## 1. `for` loops over a sequence

A `while` loop needs you to initialize, test, and update a counter. A `for` loop does all three for you: it takes each item in turn.

```python {.marimo}
for _letter in "abc":
    print(_letter)
```

The same loop written with `while`. Count the places you could make a mistake:

```python {.marimo}
_word = "abc"
_i = 0
while _i < len(_word):
    print(_word[_i])
    _i += 1
```

A `for` loop works on any sequence, including a list:

```python {.marimo}
for _price in [19.99, 5.25, 102.00]:
    print(f"${_price:>8.2f}")
```

**Predict:** what is the value of `_letter` after the loop below finishes?

```python {.marimo}
for _letter in "Baruch":
    pass
print(_letter)
```

## 2. `range`

`range(stop)`, `range(start, stop)`, and `range(start, stop, step)`. The **stop is never included**.

**Predict** each one before you run:

```python {.marimo}
print(list(range(5)))
print(list(range(2, 6)))
print(list(range(10, 0, -3)))
print(list(range(5, 5)))
```

### Off-by-one errors

To loop over 1 to n *inclusive*, the stop must be `n + 1`. This is the most common loop bug in the course.

```python {.marimo}
_n = 4
print("range(1, n):    ", list(range(1, _n)))
print("range(1, n + 1):", list(range(1, _n + 1)))
```

**Quick check:** write the `range` that produces each of these:

- `0, 1, 2, ..., 9`
- `1, 3, 5, 7, 9`
- `10, 9, 8, ..., 1`

## 3. The accumulator pattern

1. **Before** the loop: start with an identity value (`0` for sums, `1` for products, `""` for strings).
2. **Inside** the loop: update it with each item.
3. **After** the loop: use or return it.

```python {.marimo}
def sum_of_squares(n: int) -> int:
    total = 0
    for k in range(1, n + 1):
        total += k * k
    return total


print(sum_of_squares(10), "formula:", 10 * 11 * 21 // 6)
```

Strings work the same way. **Predict** what this returns:

```python {.marimo}
def mystery(text: str) -> str:
    result = ""
    for ch in text:
        result = ch + result
    return result


print(mystery("loop"))
```

### Common bug: resetting the accumulator inside the loop

```python {.marimo}
def broken_sum(n: int) -> int:
    for k in range(1, n + 1):
        total = 0
        total += k
    return total


print(broken_sum(10), "but we wanted", 55)
```

**Trace it:** what is `total` after each step? Move one line to fix it.

## 4. Counting with a condition

Counting is accumulating `1` each time a condition is true.

```python {.marimo}
def count_vowels(text: str) -> int:
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


print(count_vowels("Baruch College"))
```

### Returning early

When you find what you're looking for, `return` stops the loop and the function immediately.

```python {.marimo}
def has_digit(text: str) -> bool:
    for ch in text:
        if ch.isdigit():
            return True
    return False


print(has_digit("MTH3300"), has_digit("Python"))
```

**Predict:** what goes wrong if you put `return False` *inside* the loop, as an `else`?

## 5. A finance example: a growth table

Accumulators and f-strings together. The balance is the accumulator.

```python {.marimo}
def print_growth(principal: float, rate: float, years: int) -> None:
    balance = principal
    for year in range(1, years + 1):
        balance *= 1 + rate
        print(f"Year {year:>2}: ${balance:>10,.2f}")


print_growth(1000, 0.07, 10)
```

**Question:** why is this a `for` loop, when `years_to_double` in L09 was a `while` loop?

## 6. `enumerate`: the index and the value together

```python {.marimo}
tickers = ["AAPL", "MSFT", "NVDA"]
for _position, _ticker in enumerate(tickers, start=1):
    print(f"{_position}. {_ticker}")
```

Without `enumerate`, you track the index yourself. It works, but there is more to get wrong:

```python {.marimo}
_position = 1
for _ticker in tickers:
    print(f"{_position}. {_ticker}")
    _position += 1
```

## 7. Loops inside loops

**Predict:** how many lines does this print?

```python {.marimo}
for _row in range(1, 4):
    _line = ""
    for _col in range(1, 4):
        _line += f"{_row * _col:>4}"
    print(_line)
```

The inner loop runs completely for **each** step of the outer loop: 3 × 3 = 9 products.

## 8. Simulation with `random`

You can estimate a probability by trying something many times and counting. What fraction of rolls of two dice sum to 7? (The exact answer is 1/6 ≈ 0.1667.)

```python {.marimo}
import random


def estimate_seven(trials: int) -> float:
    hits = 0
    for _ in range(trials):
        if random.randint(1, 6) + random.randint(1, 6) == 7:
            hits += 1
    return hits / trials


random.seed(3300)
for _trials in [10, 100, 10_000, 1_000_000]:
    print(f"{_trials:>9,} trials: {estimate_seven(_trials):.4f}")
```

- `_` is the name for a loop variable you don't use.
- `random.seed(3300)` makes the "random" numbers the same on every run, so your results are reproducible.
- More trials means a closer estimate.

## 9. `for` or `while`?

- Use **`for`** when you know what you're looping over: the characters, the items, or the numbers 1 to n.
- Use **`while`** when you're looping *until* something happens, and you can't know in advance how many steps that takes.

## AI activity: write the test that catches it

An AI was asked for "a function that adds up the numbers from 1 to n." It wrote:

```python {.marimo}
def sum_to(n: int) -> int:
    total = 0
    for k in range(n):
        total += k
    return total
```

1. **Before running anything,** write down what `sum_to(3)` should return, and what this code actually returns.
2. Write one `assert` that would catch the bug.
3. Run it below, and fix the code.

```python {.marimo}
print("sum_to(3) =", sum_to(3), "expected", 1 + 2 + 3)
```

Then ask an AI for a one-line version of `sum_of_squares`. Could you explain it to a classmate? If not, ask the AI to walk you through it, and log the conversation.

## Exercises (40 minutes)

Open `l10_exercises.py` and run `uv run pytest lectures/10-for` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `count_multiples`, `product` |
| Core | `factorial`, `digit_sum`, `remove_vowels`, `alternating_sum` |
| Fix the AI's code | `count_evens` |
| Stretch | `is_prime`, `seven_frequency` |
