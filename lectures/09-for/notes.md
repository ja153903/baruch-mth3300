---
title: "L09: for loops and a first look at lists"
marimo-version: "0.25.2"
---

# L09: `for` loops and a first look at lists

**By the end of this lecture you can:**

- make a list, index it, and loop over it
- loop over a string, a list, or a `range`
- avoid off-by-one errors with `range`
- use the accumulator pattern to sum, count, and build up results
- use `enumerate` instead of index arithmetic
- run a small, reproducible random simulation
- choose between `for` and `while`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L08)

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

**Predict:** what is the value of `_letter` after the loop below finishes?

```python {.marimo}
for _letter in "Baruch":
    pass
print(_letter)
```

## 2. A first look at lists

A **list** holds several values in order, inside square brackets, separated by commas. Indexing works the same way as for strings (L03): the first item is at 0, and `-1` is the last.

```python {.marimo}
prices = [19.99, 5.25, 102.00]
print(prices[0], prices[-1], len(prices))
print(sum(prices), max(prices), min(prices))
```

A `for` loop takes each item of a list in turn, just as it takes each character of a string:

```python {.marimo}
for _price in prices:
    print(f"${_price:>8.2f}")
```

To build a list, start with an empty list, `[]`, and `append` an item each time through the loop:

```python {.marimo}
_digits = []
for _ch in "a1b22c3":
    if _ch.isdigit():
        _digits.append(int(_ch))
print(_digits, sum(_digits))
```

- `list(...)` turns a sequence into a list, so you can see all its items at once: `list("abc")` is `['a', 'b', 'c']`.
- A parameter that takes a list of whole numbers has the type hint `list[int]` (L06).

That's all you need for now. L11 covers slicing, changing a list in place, and the surprises that come with it.

## 3. `range`

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

## 4. The accumulator pattern

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

## 5. Counting with a condition

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

## 6. A finance example: a growth table

Accumulators and f-strings together. The balance is the accumulator.

```python {.marimo}
def print_growth(principal: float, rate: float, years: int) -> None:
    balance = principal
    for year in range(1, years + 1):
        balance *= 1 + rate
        print(f"Year {year:>2}: ${balance:>10,.2f}")


print_growth(1000, 0.07, 10)
```

**Question:** why is this a `for` loop, when `years_to_double` in L08 was a `while` loop?

## 7. `enumerate`: the index and the value together

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

## 8. Loops inside loops

**Predict:** how many lines does this print?

```python {.marimo}
for _row in range(1, 4):
    _line = ""
    for _col in range(1, 4):
        _line += f"{_row * _col:>4}"
    print(_line)
```

The inner loop runs completely for **each** step of the outer loop: 3 × 3 = 9 products. L10 does much more with loops inside loops.

## 9. Simulation with `random`

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

## 10. `for` or `while`?

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

Open `l09_exercises.py` and run `uv run pytest lectures/09-for` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `count_multiples`, `product` |
| Core | `factorial`, `digit_sum`, `remove_vowels`, `alternating_sum` |
| Fix the AI's code | `count_evens` |
| Stretch | `is_prime`, `seven_frequency` |
