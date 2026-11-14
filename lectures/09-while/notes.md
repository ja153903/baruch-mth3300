---
title: "L09: while loops"
marimo-version: "0.25.2"
---

# L09: `while` loops

**By the end of this lecture you can:**

- repeat code while a condition holds
- set up a loop: initialize, test, and update
- trace a loop by hand with a table
- count and add things up inside a loop
- take a number apart, digit by digit, with `%` and `//`
- spot and fix infinite loops and off-by-one errors
- stop a loop early with `break`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L08)

**Find the bug.** Teenagers are 13 to 19 years old. What does this print, and what should it print?

```python {.marimo}
def _is_teen(age: int) -> bool:
    return 13 < age < 19


print(_is_teen(13), _is_teen(15), _is_teen(19))
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

Python checks the condition before each pass through the body, including the first one. If the condition is false from the start, the body never runs at all.

**Predict:** how many times can you halve 100 before it drops below 1?

```python {.marimo}
_n = 100
_halvings = 0
while _n >= 1:
    _n = _n / 2
    _halvings += 1
print(_halvings, _n)
```

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

| step | `n` | `count` | `n > 0`? |
|---|---|---|---|
| start | 3300 | 0 | yes |
| 1 | | | |
| 2 | | | |

Keep adding rows until the test says no. The last row holds the answer.

**Predict:** what about `digits(0)`? Is that the answer we want?

## 3. Taking a number apart

`n % 10` is the last digit of `n`, and `n // 10` is `n` without its last digit. Together, they take a number apart one digit at a time, starting from the right:

```python {.marimo}
_n = 2026
while _n > 0:
    print(_n % 10, _n // 10)
    _n = _n // 10
```

## 4. Adding things up

A loop can keep a running total. Here is 1 + 2 + ... + 10:

```python {.marimo}
_k = 1
_total = 0
while _k <= 10:
    _total += _k
    _k += 1
print(_total, "and the formula n(n + 1)/2 gives", 10 * 11 // 2)
```

`_total` starts at 0, and each pass adds one more number to it. `_k` counts from 1 up to 10.

### Common bug: off by one

**Predict:** this was meant to add up 1 + 2 + 3 + 4 + 5. What does it print?

```python {.marimo}
_k = 1
_total = 0
while _k < 5:
    _total += _k
    _k += 1
print(_total)
```

`< 5` stops before 5 gets added. Check the last pass of every loop: does the body run when `_k` is 5? Choosing between `<` and `<=` is the most common loop bug there is.

## 5. When you don't know how many steps it takes

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

This is where `while` shines. You can't know ahead of time how many years it takes, so you loop *until* the goal is reached.

## 6. A finance example: paying off a credit card

You owe $5,000 on a card that charges 24% a year, which is 2% a month. You pay $200 a month. How many months until it's paid off?

```python {.marimo}
def months_to_pay_off(balance: float, annual_rate: float, payment: float) -> int:
    months = 0
    while balance > 0:
        balance = balance * (1 + annual_rate / 12) - payment
        months += 1
    return months


print(months_to_pay_off(5_000, 0.24, 200))
```

**Predict:** does paying $300 a month instead cut the time by a third, by more, or by less?

```python {.marimo}
print(months_to_pay_off(5_000, 0.24, 300))
```

**Predict:** what happens with a payment of $100? Work it out before you run anything. (Hint: what's 2% of $5,000?)

### Common bug: the loop that never ends

A loop runs forever when its condition never becomes false. Usually the update is missing, or it moves the wrong way. Sometimes it jumps right past the stopping point:

```python
# Don't run this: n goes 10, 7, 4, 1, -2, ... and never equals 0.
n = 10
while n != 0:
    n -= 3
```

Fix it with `while n > 0`. If a loop seems stuck, press **Ctrl-C** to stop it. Then put `print(f"{n=}")` inside the loop to watch what happens.

## 7. Walking through a string

An index that counts up lets a `while` loop visit each character of a string:

```python {.marimo}
_word = "Baruch"
_i = 0
while _i < len(_word):
    print(_i, _word[_i])
    _i += 1
```

The test is `_i < len(_word)`, not `<=`, because the last index is `len(_word) - 1`. In L10, the `for` loop will do this with less to get wrong.

## 8. `break`

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

`while True` loops forever on purpose, and `break` is the way out. Use it when the place to stop is easiest to check in the middle of the body.

**Predict:** why does `first_divisor(97)` return 97?

## 9. Asking until the input is valid

You can't know how many tries a user needs to type a whole number, so `input` and `while` go together:

```python
shares = input("How many shares? ")
while not shares.isdigit():
    shares = input("Please type a whole number: ")
print(f"Buying {int(shares)} shares")
```

## AI activity

Ask an AI: *"Give me a Python `while` loop with a subtle bug that makes it run forever. Don't tell me the bug."* Find the bug by tracing the loop by hand.

Write your trace as a table, like the one in section 2. Then fix the loop, and ask the AI whether your fix is right. If you disagree, run your version and check.

## Exercises (40 minutes)

Open `l09_exercises.py` and run `uv run pytest lectures/09-while` as you go. If the tests seem stuck, one of your loops never ends: press Ctrl-C and trace it. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `count_digits`, `years_to_reach` |
| Core | `sum_of_odds`, `reverse_number`, `next_power_of_two`, `gcd` |
| Fix the AI's code | `first_space` |
| Stretch | `newton_sqrt`, `payoff_months` |
