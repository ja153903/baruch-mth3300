---
title: "L02: Values, types, expressions"
marimo-version: "0.25.2"
---

# L02: Values, types, expressions

**By the end of this lecture you can:**

- name Python's basic types: `int`, `float`, `str`, `bool`
- predict the result of arithmetic, including `//`, `%`, and `**`
- store values in variables and convert between types

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Every value has a type

```python {.marimo}
print(type(42), type(3.5), type("42"), type(True))
```

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

## 3. Variables

A variable is a name that refers to a value. `=` means "make this name refer to this value"; it is not the `=` of algebra.

```python {.marimo}
total_cents = 1234
dollars = total_cents // 100
cents = total_cents % 100
print(dollars, cents)
```

## 4. Converting types

```python {.marimo}
print(int("42") + 1)
print(float("3.5") * 2)
print(str(42) + "!")
print(int(3.99))  # truncates; it doesn't round
```

## 5. Integers never overflow

Python integers can be as large as your memory allows. That's unusual among programming languages, and handy in math.

```python {.marimo}
print(2**200)
```

## AI activity: predict, then explain

Write down your prediction for each of these, then run them:
`0.1 + 0.2`, `round(2.5)`, `round(3.5)`, `10 / 3 * 3`.
For each one you got wrong, ask an AI *why*. You'll meet the full story in L22.

**Exercises:** `l02_exercises.py`
