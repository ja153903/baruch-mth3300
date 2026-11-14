---
title: "L07: Booleans and conditionals"
marimo-version: "0.25.2"
---

# L07: Booleans and conditionals

**By the end of this lecture you can:**

- write comparisons and combine them with `and`, `or`, `not`
- choose between branches with `if`/`elif`/`else`
- predict which branch runs, and put conditions in the right order
- test the boundaries of every condition
- explain which values count as true and which as false
- pick between two values with a one-line conditional expression

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L06)

**Predict** the output before you run it:

```python {.marimo}
def _half(x: float) -> float:
    return x / 2


print(_half(7) == 3.5)
print(_half(7) == 3)
print(type(_half(8)))
```

## 1. Comparisons produce booleans

```python {.marimo}
print(3 < 5, 3 == 3.0, "a" < "b", 0.1 + 0.2 == 0.3)
```

Remember: `=` assigns a value, and `==` compares two values.

Strings compare in dictionary order, letter by letter, but every capital letter comes before every lowercase letter. **Predict:**

```python {.marimo}
print("apple" < "banana", "Zebra" < "apple", "10" < "9")
```

### Common bug: comparing numbers stored as text

`"10" < "9"` is `True`, because strings compare one character at a time, and `"1"` comes before `"9"`. Convert text to numbers before you compare them: `int("10") < int("9")` is `False`.

## 2. Combining conditions

**Predict:**

```python {.marimo}
temp = 72
print(temp > 60 and temp < 80)
print(60 < temp < 80)  # Python lets you chain comparisons
print(not temp > 100)
print(temp < 0 or temp > 100)
```

| `a` | `b` | `a and b` | `a or b` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

`and` is true only when both sides are. `or` is true when at least one side is. `not` flips `True` and `False`.

`and` stops as soon as it knows the answer: if the left side is `False`, Python never looks at the right side. That can protect you from an error:

```python {.marimo}
_shares = 0
print(_shares != 0 and 1000 / _shares > 10)
```

## 3. `if` / `elif` / `else`

A plain `if` runs its indented block only when the condition is true:

```python {.marimo}
_cash = 40
_price = 55
if _price > _cash:
    print("Not enough cash")
print("Done")
```

The indented line belongs to the `if`. `print("Done")` isn't indented, so it runs either way.

Python checks the conditions top to bottom and runs **only the first** branch that's true.

```python {.marimo}
def letter(score: float) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C or below"


print(letter(95), letter(85), letter(42))
```

**Predict:** what goes wrong if you swap the `>= 90` and `>= 80` checks?

### Common bug: conditions in the wrong order

```python {.marimo}
def letter_swapped(score: float) -> str:
    if score >= 80:
        return "B"
    elif score >= 90:
        return "A"
    else:
        return "C or below"


print(letter_swapped(95))
```

95 is also at least 80, so the first branch wins, and the `>= 90` branch can never run. Put the strictest condition first.

## 4. `if` versus `elif`

**Predict:** how many lines does each cell print?

```python {.marimo}
_x = 15
if _x > 10:
    print("more than 10")
if _x > 5:
    print("more than 5")
```

```python {.marimo}
_x = 15
if _x > 10:
    print("more than 10")
elif _x > 5:
    print("more than 5")
```

Two separate `if`s are checked separately. An `elif` is checked only when every condition above it was false.

## 5. Returning a boolean

A comparison is already `True` or `False`, so a function can return it directly. Days are numbered 0 for Monday through 6 for Sunday:

```python {.marimo}
def is_weekend(day: int) -> bool:
    return day >= 5


print(is_weekend(2), is_weekend(6))
```

You could write `if day >= 5: return True` and `else: return False`, but that's four lines for the same thing.

## 6. Nested conditions

An `if` can go inside another `if`. Members always ship free; everyone else ships free on orders of $50 or more:

```python {.marimo}
def shipping(total: float, is_member: bool) -> float:
    if is_member:
        return 0.0
    else:
        if total >= 50:
            return 0.0
        else:
            return 5.99


print(shipping(20, True), shipping(60, False), shipping(20, False))
```

The same rule fits in one condition: `if is_member or total >= 50: return 0.0`. When you can flatten nested `if`s with `and` or `or`, the code is usually easier to read.

## 7. Truthiness

In an `if`, a few values count as false: `0`, `0.0`, the empty string, and `None`. Everything else counts as true. (Empty lists and dicts, which you'll meet later, count as false too.) `bool()` shows how a value counts:

```python {.marimo}
print(bool(0), bool(7), bool(0.0), bool(-2.5))
print(bool(""), bool("hi"), bool(" "), bool("0"))
```

A common use is checking whether the user typed anything:

```python {.marimo}
_typed = ""  # pretend the user pressed Enter without typing
if _typed:
    print("Hello,", _typed)
else:
    print("You didn't type anything")
```

## 8. Conditional expressions

`a if condition else b` gives `a` when the condition is true, and `b` otherwise. It picks between two values in one line:

```python {.marimo}
_change = -3.2
_arrow = "up" if _change > 0 else "down"
print(f"The stock is {_arrow} {abs(_change)}%")
```

Use it for a simple choice between two values. For anything longer, a full `if` is easier to read.

## 9. A finance example: tax brackets

```python {.marimo}
def tax(income: float) -> float:
    if income <= 10_000:
        return 0.0
    elif income <= 50_000:
        return (income - 10_000) * 0.10
    else:
        return 4_000 + (income - 50_000) * 0.20


print(tax(5_000), tax(30_000), tax(80_000))
```

**Predict** the tax on each side of both boundaries, then run:

```python {.marimo}
print(tax(10_000), tax(10_001), tax(50_000), tax(50_001))
```

Every `<=` or `<` is a decision about what happens exactly on the boundary. Test the number right on it, and one on each side.

## AI activity

Ask an AI to write `tax` for you, then test it at **exactly** 10,000 and 50,000. Did it handle the boundaries the way the spec says? Log what you found.

Then ask it why it chose `<` or `<=` at each boundary. Does its explanation match what its code does?

## Exercises (40 minutes)

Open `l07_exercises.py` and run `uv run pytest lectures/07-conditionals` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `is_even`, `max_of_three` |
| Core | `trade_allowed`, `commission`, `price_signal`, `quadrant` |
| Fix the AI's code | `late_fee` |
| Stretch | `median_of_three`, `count_real_roots` |
