---
title: "L03: Strings"
marimo-version: "0.25.2"
---

# L03: Strings

**By the end of this lecture you can:**

- index and slice strings
- use common string methods
- explain why strings can't be changed in place

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Indexing

Positions start at **0**. Negative indexes count from the end.

```python {.marimo}
word = "Baruch"
print(word[0], word[1], word[-1], len(word))
```

## 2. Slicing

`s[start:stop:step]` includes `start` and stops **before** `stop`.

**Predict:**

```python {.marimo}
print(word[0:3])
print(word[2:])
print(word[:-1])
print(word[::-1])
```

## 3. Methods

A method is a function that belongs to a value: `value.method()`.

```python {.marimo}
name = "  ada LOVELACE  "
print(repr(name.strip()))
print(name.strip().title())
print(name.upper().count("A"))
print("ada" in name)
print("a,b,c".split(","))
print("-".join(["2026", "11", "05"]))
```

## 4. Strings are immutable

You can't change a character in place. Methods return a **new** string.

```python {.marimo}
city = "new york"
shouted = city.upper()
print(city, "->", shouted)
try:
    city[0] = "N"
except TypeError as err:
    print("TypeError:", err)
```

## AI activity

Ask an AI: *"Give me five Python slicing puzzles on the string 'programming', without answers."*
Solve them on paper, check them in the REPL, and log which ones fooled you.

**Exercises:** `l03_exercises.py`
