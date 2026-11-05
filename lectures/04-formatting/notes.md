---
title: "L04: Formatting, input/output, reading tracebacks"
marimo-version: "0.25.2"
---

# L04: Formatting, input/output, reading tracebacks

**By the end of this lecture you can:**

- format numbers with f-strings
- read input from the user and convert it
- read a traceback from the bottom up

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. f-strings

Put an `f` before the quote, and any expression inside `{}` gets its value filled in.

```python {.marimo}
item = "coffee"
price = 4.5
qty = 3
print(f"{qty} x {item} = ${price * qty}")
```

## 2. Format specs

Add `:spec` after the expression to control how it looks.

```python {.marimo}
balance = 1234567.891
rate = 0.0725
print(f"{balance:,.2f}")  # thousands separators, 2 decimal places
print(f"{rate:.2%}")  # as a percentage
print(f"{'left':<10}|{'right':>10}|")
print(f"{42:05d}")  # pad with zeros
```

## 3. Debugging with `=`

`f"{expr=}"` prints the expression *and* its value. This is the fastest way to check what a variable holds.

```python {.marimo}
subtotal = price * qty
print(f"{subtotal=}, {subtotal * 1.08875=:.2f}")
```

## 4. Input

`input()` always returns a **string**, so convert it before doing math:

```python
age = int(input("Your age: "))
print(f"Next year you'll be {age + 1}")
```

(`input` doesn't run inside these notes. Try it in a `.py` file instead.)

## 5. Reading a traceback

```text
Traceback (most recent call last):
  File "tip.py", line 2, in <module>
    tip = bill * 0.2
          ~~~~~^~~~~
TypeError: can't multiply sequence by non-int of type 'float'
```

Read it **bottom up**:

1. **Last line:** what kind of error, and why.
2. **The line above it:** which line of your code, with `~~~^~~~` pointing at the exact part.
3. **Ask yourself:** what type does `bill` hold? (It's a string, straight from `input`.)

## AI activity

Write a three-line program that asks for a bill amount and prints a 20% tip, then run it. If it crashes, paste the traceback into an AI and ask it to explain each line of the traceback, **not** to fix your code.

**Exercises:** `l04_exercises.py`
