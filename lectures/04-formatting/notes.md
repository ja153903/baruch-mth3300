---
title: "L04: Formatting, input/output, reading tracebacks"
marimo-version: "0.25.2"
---

# L04: Formatting, input/output, reading tracebacks

**By the end of this lecture you can:**

- format numbers with f-strings: decimal places, commas, percents, and signs
- line up columns with widths and alignment
- debug with `f"{x=}"`
- read input from the user and convert it
- read a traceback from the bottom up, and name the common kinds of error

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L03)

**Predict** the output before you run it:

```python {.marimo}
_s = "Wall Street"
print(_s[:4], _s[-6:], _s[::-1][:3])
print(_s.lower().count("l"), _s.find(" "), "St" in _s)
```

## 1. f-strings

Put an `f` before the quote, and any expression inside `{}` gets its value filled in.

```python {.marimo}
item = "coffee"
price = 4.5
qty = 3
print(f"{qty} x {item} = ${price * qty}")
```

Inside the braces you can put any expression: a variable, some arithmetic, or a method call. Compare the L03 way, with `+` and `str()`, to an f-string:

```python {.marimo}
_name = "ada"
_score = 92
print("Student " + _name.title() + " scored " + str(_score) + "%")
print(f"Student {_name.title()} scored {_score}%")
```

### Common bug: forgetting the `f`

**Predict:**

```python {.marimo}
_total = 42
print("Total: {_total}")
print(f"Total: {_total}")
```

Without the `f`, the braces are just characters in the string.

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

| Spec | Meaning | Example | Result |
|---|---|---|---|
| `.2f` | fixed point: exactly 2 digits after the decimal point | `f"{3.14159:.2f}"` | `3.14` |
| `,` | commas between thousands | `f"{1234567:,}"` | `1,234,567` |
| `.1%` | times 100, with 1 decimal place and a `%` sign | `f"{0.123:.1%}"` | `12.3%` |
| `+` | always show the sign | `f"{5:+}"` | `+5` |
| `<8`, `>8`, `^8` | left, right, or center in 8 characters | `f"{'hi':>8}"` | `'      hi'` |
| `05d` | a whole number, padded with zeros to 5 digits | `f"{42:05d}"` | `00042` |

To fill with a character other than a space, put it before `<`, `>`, or `^`: `f"{'hi':*^8}"` gives `***hi***`.

You can combine specs in one: `f"{x:>12,.2f}"` means right-aligned in 12 characters, with commas, and 2 decimal places.

**Predict** each line:

```python {.marimo}
print(f"{2 / 3:.3f}")
print(f"{98765.4321:,.2f}")
print(f"{-0.034:+.1%}")
print(f"[{'AAPL':^10}]")
```

## 3. A finance example: lining up columns

A width makes every value take up the same space. Unless you say otherwise, numbers go on the right and text on the left. **Predict:**

```python {.marimo}
print(f"[{42:6}]")
print(f"[{'42':6}]")
```

So columns line up:

```python {.marimo}
print(f"{'Ticker':<6} {'Shares':>6} {'Price':>8} {'Value':>10}")
print(f"{'AAPL':<6} {10:>6} {227.48:>8.2f} {10 * 227.48:>10,.2f}")
print(f"{'NVDA':<6} {125:>6} {145.1:>8.2f} {125 * 145.1:>10,.2f}")
```

Line up text on the left and numbers on the right, so the decimal points sit under each other. In L09, a loop will print a whole table like this for you.

## 4. Debugging with `=`

`f"{expr=}"` prints the expression *and* its value. This is the fastest way to check what a variable holds.

```python {.marimo}
subtotal = price * qty
print(f"{subtotal=}, {subtotal * 1.08875=:.2f}")
```

## 5. More control over `print`

`print` puts a space between values and starts a new line at the end. `sep` and `end` change those:

```python {.marimo}
print("2026", "11", "13", sep="-")
print("Loading", end="... ")
print("done")
```

## 6. Input

`input()` always returns a **string**, so convert it before doing math:

```python
age = int(input("Your age: "))
print(f"Next year you'll be {age + 1}")
```

(`input` doesn't run inside these notes. Try it in a `.py` file instead.)

### Common bug: forgetting to convert

**Predict:** the user types `3`. What does each one print?

```python {.marimo}
_typed = "3"  # pretend the user typed this
print(_typed * 2, int(_typed) * 2)
```

Text that looks like a number is still text. Here's what happens with other things a user might type:

```python {.marimo}
_typed = "3.5"  # pretend the user typed this
print(float(_typed) * 2)
try:
    print(int(_typed))
except ValueError as err:
    print("ValueError:", err)
```

A complete program that reads a number, converts it, and prints a formatted answer:

```python
miles = float(input("Miles: "))
print(f"{miles} miles is {miles * 1.609:.1f} km")
```

## 7. Reading a traceback

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

The error shows up on line 2, but the fix belongs on line 1, where `bill` was read: convert it with `float`. The line that crashes isn't always the line with the mistake.

The kinds of error you'll see most:

| Error | Usually means | Example |
|---|---|---|
| `SyntaxError` | Python can't read the line: a missing `)`, quote, or colon | `print("hi"` |
| `NameError` | a name Python doesn't know, often a typo | `prnit("hi")` |
| `TypeError` | an operation on the wrong type | `"Total: " + 5` |
| `ValueError` | the right type, but a value that doesn't work | `int("3.5")` |
| `ZeroDivisionError` | dividing by zero | `10 / 0` |
| `IndexError` | a position past the end | `"abc"[3]` |
| `AttributeError` | a method the value doesn't have | `"hi".uper()` |

**Quick check:** which error does each line raise? Predict, then check in the REPL.

- `int("twelve")`
- `"MTH" + 3300`
- `"Baruch"[10]`
- `round(3.7, 1`

## 8. Python suggests fixes for typos

Modern Python checks whether you misspelled a name, and says so on the last line:

```text
NameError: name 'prnit' is not defined. Did you mean: 'print'?
AttributeError: 'str' object has no attribute 'uper'. Did you mean '.upper' instead of '.uper'?
```

Read the suggestion before you ask anyone else, including an AI. It's a guess, so check that it's what you meant.

## AI activity

Write a three-line program that asks for a bill amount and prints a 20% tip, then run it. If it crashes, paste the traceback into an AI and ask it to explain each line of the traceback, **not** to fix your code.

Once it works, run it again and type `twenty` as the bill. Predict the last line of the traceback before you look. Was your prediction right?

## Exercises (40 minutes)

Open `l04_exercises.py`. Replace each `None` with an f-string, and run `uv run pytest lectures/04-formatting` as you go. Do them in order:

| Group | Variables |
|---|---|
| Warmup | `formatted_price`, `rate_text` |
| Core | `invoice_text`, `table_row`, `debug_text`, `change_text` |
| Fix the AI's code | `balance_text` |
| Stretch | `banner`, `scientific` |
