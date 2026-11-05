---
title: "L05: Functions"
marimo-version: "0.25.2"
---

# L05: Functions

**By the end of this lecture you can:**

- define a function with parameters and a return value
- explain the difference between `print` and `return`
- explain why a variable inside a function isn't visible outside it

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Defining and calling

```python {.marimo}
def area_of_rectangle(width, height):
    return width * height


print(area_of_rectangle(3, 4))
print(area_of_rectangle(2.5, 2) + 1)
```

`width` and `height` are **parameters**. The values `3` and `4` are **arguments**.

## 2. `print` is not `return`

**Predict** what this prints:

```python {.marimo}
def shout(text):
    print(text.upper())


answer = shout("hi")
print(answer)
```

A function without `return` gives back `None`. `print` shows a value to a *person*; `return` hands it back to the *code* that called the function.

## 3. Default arguments and keyword arguments

```python {.marimo}
def compound(principal, rate=0.05, years=1):
    return principal * (1 + rate) ** years


print(compound(1000))
print(compound(1000, years=10))
```

## 4. Scope

Variables created inside a function are **local**: they disappear when the function returns.

```python {.marimo}
def make_total():
    _subtotal = 10
    return _subtotal * 2


print(make_total())
```

(The `_` prefix is a marimo convention for names that stay private to one cell. In a normal `.py` file, you'd write `subtotal`.)

## 5. Functions call functions

```python {.marimo}
def square(x):
    return x * x


def hypotenuse(a, b):
    return (square(a) + square(b)) ** 0.5


print(hypotenuse(3, 4))
```

## AI activity

Write `hypotenuse` yourself without looking. Then ask an AI: *"What are three inputs that might break this function?"* Try each input. Is the AI right?

**Exercises:** `l05_exercises.py`
