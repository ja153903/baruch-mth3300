---
title: "L07: Booleans and conditionals"
marimo-version: "0.25.2"
---

# L07: Booleans and conditionals

**By the end of this lecture you can:**

- write comparisons and combine them with `and`, `or`, `not`
- choose between branches with `if`/`elif`/`else`
- predict which branch runs

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Comparisons produce booleans

```python {.marimo}
print(3 < 5, 3 == 3.0, "a" < "b", 0.1 + 0.2 == 0.3)
```

Remember: `=` assigns a value, and `==` compares two values.

## 2. Combining conditions

**Predict:**

```python {.marimo}
temp = 72
print(temp > 60 and temp < 80)
print(60 < temp < 80)  # Python lets you chain comparisons
print(not temp > 100)
print(temp < 0 or temp > 100)
```

## 3. `if` / `elif` / `else`

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

## 4. Truthiness

In an `if`, empty values count as false: `0`, `0.0`, `""`, `[]`, `{}`, `None`.

```python {.marimo}
for value in [0, 7, "", "hi", [], [0]]:
    print(repr(value), "->", "truthy" if value else "falsy")
```

## 5. A finance example: tax brackets

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

## AI activity

Ask an AI to write `tax` for you, then test it at **exactly** 10,000 and 50,000. Did it handle the boundaries the way the spec says? Log what you found.

**Exercises:** `l07_exercises.py`
