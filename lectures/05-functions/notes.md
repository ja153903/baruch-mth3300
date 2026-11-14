---
title: "L05: Functions"
marimo-version: "0.25.2"
---

# L05: Functions

**By the end of this lecture you can:**

- define a function with parameters and a return value
- trace what happens, step by step, when a function is called
- explain the difference between `print` and `return`
- use default arguments and keyword arguments
- explain why a variable inside a function isn't visible outside it
- build functions out of other functions, including ones from the `math` module
- read and write a docstring

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L04)

**Predict** the output before you run it:

```python {.marimo}
_price = 1234.5
_rate = 0.0412
print(f"{_price:>10,.2f}|{_rate:.1%}|{7:03d}")
print(f"{_price=}")
```

## 1. Defining and calling

```python {.marimo}
def area_of_rectangle(width, height):
    return width * height


print(area_of_rectangle(3, 4))
print(area_of_rectangle(2.5, 2) + 1)
```

`width` and `height` are **parameters**. The values `3` and `4` are **arguments**.

The parts of a definition:

- `def`, the function's name, its parameters in parentheses, and a colon
- the **body**: the lines indented under it, by 4 spaces each
- `return`, which sends a value back to the code that called the function

Defining a function doesn't run it. The body runs each time you **call** the function.

## 2. Tracing a call

When you call a function, Python:

1. works out the value of each argument,
2. gives each parameter the value of its argument,
3. runs the body until it reaches `return`,
4. puts the returned value where the call was.

**Predict:**

```python {.marimo}
def double(x):
    return x * 2


print(double(double(3)) + double(1))
```

Work from the inside out: `double(3)` is 6, so `double(double(3))` is `double(6)`.

`return` also ends the function. Any lines after a `return` never run.

## 3. `print` is not `return`

**Predict** what this prints:

```python {.marimo}
def shout(text):
    print(text.upper())


answer = shout("hi")
print(answer)
```

A function without `return` gives back `None`. `print` shows a value to a *person*; `return` hands it back to the *code* that called the function.

### Common bug: printing instead of returning

```python {.marimo}
def tip_amount(bill):
    print(bill * 0.2)


try:
    _total = 50 + tip_amount(50)
except TypeError as err:
    print("TypeError:", err)
```

`10.0` appears on the screen, so the function looks right. But it gave back `None`, and `50 + None` is an error. If other code needs the value, `return` it.

## 4. Default arguments and keyword arguments

```python {.marimo}
def compound(principal, rate=0.05, years=1):
    return principal * (1 + rate) ** years


print(compound(1000))
print(compound(1000, years=10))
```

- A **default** value is used when the call leaves that argument out.
- A **keyword argument** names its parameter, as in `years=10`. Keyword arguments can come in any order, and they make a call easier to read.
- Parameters with defaults must come after the ones without.

**Predict** each line:

```python {.marimo}
print(f"{compound(1000, 0.07, 10):,.2f}")
print(f"{compound(years=10, principal=1000, rate=0.07):,.2f}")
print(f"{compound(1000, years=10):,.2f}")
```

## 5. Scope

Variables created inside a function are **local**: they disappear when the function returns.

```python {.marimo}
def make_total():
    _subtotal = 10
    return _subtotal * 2


print(make_total())
```

(The `_` prefix is a marimo convention for names that stay private to one cell. In a normal `.py` file, you'd write `subtotal`.)

**Predict:** does the function change `rate`?

```python {.marimo}
rate = 0.05


def raise_rate():
    rate = 0.10
    return rate


print(raise_rate(), rate)
```

The `rate` inside `raise_rate` is a new, local variable that happens to have the same name. That's a good thing: you can understand a function by reading only its parameters and its body.

## 6. Functions call functions

```python {.marimo}
def square(x):
    return x * x


def hypotenuse(a, b):
    return (square(a) + square(b)) ** 0.5


print(hypotenuse(3, 4))
```

Small functions that each do one job are easier to write, test, and fix than one big function.

## 7. The `math` module

Python comes with **modules**: collections of ready-made functions. `import math` loads the math module. Then write `math.` before each name in it:

```python {.marimo}
import math

print(math.sqrt(2), math.pi)
print(math.floor(7.8), math.ceil(7.2))
```

`math.floor` rounds down and `math.ceil` rounds up. If paying off a loan takes 7.2 months of payments, you make payments for 8 months.

A finance example: how much a stock's price swings is called its **volatility**. Over a longer time, volatility grows with the square root of the time. A stock that moves about 1% a day moves about 1% × √252 over a year of 252 trading days:

```python {.marimo}
def annual_volatility(daily_volatility):
    return daily_volatility * math.sqrt(252)


print(f"{annual_volatility(0.01):.2%}")
```

## 8. A finance example: a mortgage payment

A **docstring** is a string on the first line of a function's body. It says what the function does. Every function in the exercises has one: it's the spec, so read it first.

```python {.marimo}
def monthly_payment(principal, annual_rate, years):
    """The monthly payment on a loan that's paid off in equal monthly payments."""
    r = annual_rate / 12
    n = years * 12
    return principal * r / (1 - (1 + r) ** -n)


print(f"${monthly_payment(300_000, 0.065, 30):,.2f}")
```

The local variables `r` and `n` give names to the monthly rate and the number of payments, so the formula is easier to check.

**Predict:** what happens to the payment if you borrow twice as much? What if you pay it off in 15 years instead of 30?

```python {.marimo}
print(f"${monthly_payment(600_000, 0.065, 30):,.2f}")
print(f"${monthly_payment(300_000, 0.065, 15):,.2f}")
```

## 9. Common bugs with functions

- **Forgetting the parentheses.** `print(monthly_payment)` doesn't call the function. It prints the function itself, something like `<function monthly_payment at 0x104a3c2c0>`.
- **Forgetting to indent the body.** Python stops before running anything:

```text
IndentationError: expected an indented block after function definition on line 1
```

- **Calling a function before its `def` has run.** In a file, define functions near the top, and call them below.

## AI activity

Write `hypotenuse` yourself without looking. Then ask an AI: *"What are three inputs that might break this function?"* Try each input. Is the AI right?

Before you run each input, write down what you think will happen. Did any of them surprise you?

## Exercises (40 minutes)

Open `l05_exercises.py` and run `uv run pytest lectures/05-functions` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `cube`, `average` |
| Core | `sales_tax`, `name_tag`, `distance`, `shares_affordable` |
| Fix the AI's code | `rent_share` |
| Stretch | `leftover_cash`, `doubling_time` |
