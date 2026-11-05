---
title: "L06: Type hints and tests"
marimo-version: "0.25.2"
---

# L06: Type hints and tests

**By the end of this lecture you can:**

- annotate a function's parameters and return type
- read and write a pytest test
- use tests to decide whether code works, whoever wrote it

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Type hints

Hints document what a function expects and returns. Python doesn't enforce them at runtime, but a type checker such as **ty** checks them before you run anything.

```python {.marimo}
def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / height_m**2


print(f"{bmi(70, 1.75):.1f}")
```

Common hints: `int`, `float`, `str`, `bool`, `list[int]`, `dict[str, float]`, `int | None`.

## 2. Tests are code that checks code

```python {.marimo}
def test_bmi():
    assert round(bmi(70, 1.75), 1) == 22.9
    assert bmi(100, 2) == 25


test_bmi()
print("test_bmi passed")
```

`assert condition` does nothing if the condition is true, and raises `AssertionError` if it's false.

## 3. pytest

pytest finds every file named `test_*.py`, runs every function named `test_*` in it, and reports what passed.

```sh
uv run pytest                 # run everything
uv run pytest -x              # stop at the first failure
uv run pytest -k average      # only tests with "average" in the name
```

## 4. What to test

- **A normal case:** `bmi(70, 1.75)`
- **An edge case:** zero, negatives, an empty list, the boundary of an `if`
- **A case you got wrong before:** every bug you fix becomes a test

## 5. Type checking with ty

```sh
uv run ty check
```

If you call `bmi("70", 1.75)`, ty reports the mistake **before** the program runs.

## AI activity

Write a function `clamp(x, lo, hi)`. Then ask an AI: *"Suggest edge-case tests for this function. Don't change the function."* Add the tests you agree with, and log any you rejected and why.

**Exercises:** `l06_exercises.py`
