---
title: "L02: Values, types, expressions"
marimo-version: "0.25.2"
---

# L02: Values, types, expressions

**By the end of this lecture you can:**

- name Python's basic types: `int`, `float`, `str`, `bool`
- predict the result of arithmetic, including `//`, `%`, and `**`
- apply the order of operations, and use parentheses when in doubt
- store values in variables, update them, and convert between types
- round numbers, and use `abs`, `min`, and `max`

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L01)

**Predict** the output before you run it:

```python {.marimo}
print(1 + 2 * 3, (1 + 2) * 3)
print("MTH" + "3300")
print("MTH", "3300")
```

## 1. Every value has a type

```python {.marimo}
print(type(42), type(3.5), type("42"), type(True))
```

| Type | What it holds | Examples |
|---|---|---|
| `int` | whole numbers | `42`, `-7`, `0` |
| `float` | numbers with a decimal point | `3.5`, `2.0`, `-0.25` |
| `str` | text | `"42"`, `"Baruch"` |
| `bool` | yes or no | `True`, `False` |

`42` and `"42"` look alike, but one is a number and the other is text. The type decides what an operator does. **Predict:**

```python {.marimo}
print(42 + 8)
print("42" + "8")
print("42" * 3)
print(type(6 / 3))
```

`*` on a string and an `int` repeats the string.

## 2. Arithmetic

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+ - *` | the usual | `7 * 3` | `21` |
| `/` | division, always a `float` | `6 / 3` | `2.0` |
| `//` | floor division | `7 // 2` | `3` |
| `%` | remainder | `7 % 2` | `1` |
| `**` | power | `2 ** 10` | `1024` |

**Predict** before you run:

```python {.marimo}
print(17 // 5, 17 % 5)
print(-17 // 5, -17 % 5)
print(2**0.5)
```

`//` rounds **down**, toward negative infinity, not toward zero. That's why `-17 // 5` is `-4`.

### What `%` is good for

- `n % 2` is `0` when `n` is even and `1` when it's odd.
- Clock arithmetic: 10 hours after 9 o'clock is `(9 + 10) % 12`, which is 7 o'clock.

```python {.marimo}
print(3300 % 2, 3301 % 2)
print((9 + 10) % 12)
```

## 3. Order of operations

From first to last:

1. parentheses `( )`
2. `**`
3. a minus sign in front of a number, like `-x`
4. `*`, `/`, `//`, `%`
5. `+`, `-`

Operators at the same level go left to right, except `**`, which goes right to left. **Predict:**

```python {.marimo}
print((-2) ** 2)
print(2**3**2)
print(100 / 10 * 2)
```

**Try it in the REPL:** predict `-2 ** 2` first, then type it in. The `**` happens before the minus sign, so Python reads it as `-(2 ** 2)`. When in doubt, add parentheses. They cost nothing and show what you meant.

## 4. Variables

A variable is a name that refers to a value. `=` means "make this name refer to this value"; it is not the `=` of algebra.

```python {.marimo}
total_cents = 1234
dollars = total_cents // 100
cents = total_cents % 100
print(dollars, cents)
```

Rules for names:

- letters, digits, and underscores, with no digit at the start: `rate2` works, `2rate` doesn't
- case matters: `Rate` and `rate` are different variables
- use lowercase words joined by underscores: `interest_rate`, not `interestrate` or `x`
- don't reuse a name Python already has, like `print` or `type`

**Predict:** what does this print?

```python {.marimo}
_width = 3
_height = 4
_area = _width * _height
_width = 10
print(_area)
```

`_area` got its value when that line ran. Changing `_width` afterwards doesn't go back and change `_area`.

## 5. Updating a variable

A variable can get a new value that depends on its old one. Python works out the right side first, using the old value, and then stores the result.

**Predict:**

```python {.marimo}
_balance = 1000
_balance = _balance * 1.05
_balance += 100  # short for _balance = _balance + 100
_balance -= 50
print(_balance)
```

`+=`, `-=`, `*=`, and `/=` are shortcuts: `x += 1` means `x = x + 1`.

### Common bug: computing a value and throwing it away

```python {.marimo}
_price = 100
_price * 0.9  # works out 90.0, then throws it away
print(_price)
```

To keep a result, store it: `_price = _price * 0.9`.

## 6. Converting types

```python {.marimo}
print(int("42") + 1)
print(float("3.5") * 2)
print(str(42) + "!")
print(int(3.99))  # truncates; it doesn't round
```

`int()` and `float()` turn text into numbers, and `str()` turns a number into text. You'll need this all the time: anything a user types is text, even when it looks like a number.

### Common bug: `int` of text with a decimal point

```python {.marimo}
try:
    print(int("3.5"))
except ValueError as err:
    print("ValueError:", err)
```

`int` only reads text that's a whole number. Use `float("3.5")` instead, or `int(float("3.5"))` if you want to drop the decimals.

## 7. Rounding and other built-in functions

Python has functions for common jobs built in. You call a function by writing its name and putting the values it needs in parentheses.

```python {.marimo}
print(round(3.14159, 2))
print(round(7.6))
print(abs(-250))
print(min(3, 9, 4), max(3, 9, 4))
```

- `round(x)` gives the nearest whole number, as an `int`. `round(x, 2)` rounds to 2 decimal places.
- `int(x)` doesn't round: it cuts off everything after the decimal point.
- `abs` gives the distance from zero: how big a gain or loss is, whatever its sign.

## 8. A finance example: buying shares

You have $1,000, and one share costs $37.50. How many whole shares can you buy, and how much cash is left over?

```python {.marimo}
cash = 1000
share_price = 37.50
shares = cash // share_price
leftover = cash % share_price
print(shares, leftover)
```

**Predict:** why is `shares` the `float` `26.0`, and not the `int` `26`?

When an operation mixes an `int` and a `float`, the result is a `float`. Write `int(shares)` to get `26`.

## 9. Integers never overflow

Python integers can be as large as your memory allows. That's unusual among programming languages, and handy in math.

```python {.marimo}
print(2**200)
```

### Writing big and small numbers

```python {.marimo}
print(1_000_000 + 1)
print(6.02e23, 2.5e-3)
```

- Underscores in a number are only there to help you read it: `1_000_000` is one million.
- `e` means "times ten to the power": `2.5e-3` is 2.5 × 10⁻³.

Floats are different from integers: they can't grow forever, and they aren't always exact. The AI activity shows you one surprise.

## AI activity: predict, then explain

Write down your prediction for each of these, then run them:

`0.1 + 0.2`, `round(2.5)`, `round(3.5)`, `10 / 3 * 3`.

For each one you got wrong, ask an AI *why*. You'll meet the full story in L22.

## Exercises (40 minutes)

Open `l02_exercises.py`. Replace each `None` with an expression, and run `uv run pytest lectures/02-values` as you go. Do them in order:

| Group | Variables |
|---|---|
| Warmup | `fahrenheit`, `last_digit` |
| Core | `hundreds_digit`, `order_total`, `price_range`, `quarters` / `dimes` / `nickels` / `pennies` |
| Fix the AI's code | `price_in_cents` |
| Stretch | `nickel_price`, `future_weekday` |
