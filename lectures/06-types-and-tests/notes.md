---
title: "L06: Type hints and tests"
marimo-version: "0.25.2"
---

# L06: Type hints and tests

**By the end of this lecture you can:**

- annotate a function's parameters and return type, and say what hints do and don't do
- read and write a pytest test, and read pytest's report when a test fails
- compare floats in a test with `math.isclose`
- choose test cases: a normal case, edge cases, and both sides of a boundary
- use tests to decide whether code works, whoever wrote it

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L05)

**Predict** the output before you run it. How many lines does it print?

```python {.marimo}
def _triple(x):
    return x * 3


def _show_triple(x):
    print(x * 3)


_a = _triple(2)
_b = _show_triple(2)
print(_a, _b)
```

## 1. Type hints

Hints document what a function expects and returns. Python doesn't enforce them at runtime, but a type checker such as **ty** checks them before you run anything.

```python {.marimo}
def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / height_m**2


print(f"{bmi(70, 1.75):.1f}")
```

Common hints: `int`, `float`, `str`, `bool`, `list[int]`, `dict[str, float]`, `int | None`.

- `weight_kg: float` says the parameter should be a `float`. An `int` is fine wherever a `float` is expected.
- `-> float` says what the function returns. A function that only prints returns nothing, so write `-> None`.

### Hints don't stop the code from running

**Predict:**

```python {.marimo}
def double(x: int) -> int:
    return x * 2


print(double(21), double("ha"))
```

Python ran `double("ha")` without complaint, because `*` works on strings too. Hints are for people and for tools like ty, which would flag that call (section 7).

## 2. Tests are code that checks code

```python {.marimo}
def test_bmi():
    assert round(bmi(70, 1.75), 1) == 22.9
    assert bmi(100, 2) == 25


test_bmi()
print("test_bmi passed")
```

`assert condition` does nothing if the condition is true, and raises `AssertionError` if it's false.

A condition is usually a comparison. Each one is either `True` or `False`:

| `==` | `!=` | `<` | `<=` | `>` | `>=` |
|---|---|---|---|---|---|
| equal | not equal | less than | at most | greater than | at least |

(L07 does much more with these.) Here's an assert that fails:

```python {.marimo}
try:
    assert bmi(70, 1.75) == 22.9
except AssertionError:
    print("AssertionError: bmi(70, 1.75) is really", bmi(70, 1.75))
```

That's why `test_bmi` rounds before it compares.

## 3. Comparing floats: `math.isclose`

Floats are stored with about 16 significant digits, so two calculations that should agree can differ in the last digit. In tests, compare floats with `math.isclose` instead of `==`:

```python {.marimo}
import math

print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))
print(math.isclose(bmi(70, 1.75), 22.857142857142858))
```

`math.isclose(a, b)` is `True` when `a` and `b` agree to about 9 significant digits.

## 4. pytest

pytest finds every file named `test_*.py`, runs every function named `test_*` in it, and reports what passed.

```sh
uv run pytest                 # run everything
uv run pytest -x              # stop at the first failure
uv run pytest -k average      # only tests with "average" in the name
```

Suppose `cube` returns `x * 3` by mistake. pytest reports:

```text
__________________________________ test_cube ___________________________________

    def test_cube():
>       assert cube(3) == 27
E       assert 9 == 27
E        +  where 9 = cube(3)

test_geometry.py:5: AssertionError
```

Read it like a traceback:

- `>` marks the line that failed.
- The `E` lines show the actual values: `cube(3)` returned `9`, but the test wanted `27`.
- The last line gives the file and the line number.

A function that still says `raise NotImplementedError` fails its test with that error. That just means "not written yet".

## 5. What to test

- **A normal case:** `bmi(70, 1.75)`
- **An edge case:** zero, negatives, an empty list, the boundary of an `if`
- **A case you got wrong before:** every bug you fix becomes a test

### A finance example: testing compound growth

```python {.marimo}
def grow(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate) ** years


def test_grow():
    assert math.isclose(grow(1000, 0.10, 2), 1210)  # a normal case
    assert grow(1000, 0.10, 0) == 1000  # edge: no time passes
    assert grow(1000, 0, 5) == 1000  # edge: no interest
    assert grow(0, 0.10, 5) == 0  # edge: nothing invested


test_grow()
print("test_grow passed")
```

Each edge case catches a different mistake. If someone wrote `principal * (1 + rate) * years`, the `years=0` test would fail.

But edge cases alone aren't enough. **Predict:** this version uses simple interest by mistake. Which of the four checks catch it?

```python {.marimo}
def grow_wrong(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate * years)


print(math.isclose(grow_wrong(1000, 0.10, 2), 1210))
print(grow_wrong(1000, 0.10, 0) == 1000)
print(grow_wrong(1000, 0, 5) == 1000)
print(grow_wrong(0, 0.10, 5) == 0)
```

### Common bug: off at the boundary

For a boundary, test the value right on it and a value just past it. `is_passing(60)` and `is_passing(59.9)` together check that a score of exactly 60 passes. **Predict:** orders of $100 or more get a discount. Which call shows the bug?

```python {.marimo}
def gets_discount(total: float) -> bool:
    """Orders of $100 or more get a discount."""
    return total > 100


print(gets_discount(150), gets_discount(50), gets_discount(100))
```

Tests at 150 and 50 pass. Only the test at exactly 100 finds the bug.

## 6. Predict which tests would fail

**Predict:** which lines print `False`? Each `False` would be a failing `assert`.

```python {.marimo}
def net_price(price: float, discount: float) -> float:
    return price - price * discount


print(net_price(100, 0.2) == 80)
print(net_price(100, 0) == 100)
print(net_price(19.99, 0.3) == 13.993)
print(math.isclose(net_price(19.99, 0.3), 13.993))
```

### Common bug: a test that expects the wrong answer

A test is only as good as the answer it expects. If you work out the expected value with the same code you're testing, the test can't catch anything. Work it out by hand, or from the spec.

## 7. Type checking with ty

```sh
uv run ty check
```

If you call `bmi("70", 1.75)`, ty reports the mistake **before** the program runs:

```text
error[invalid-argument-type]: Argument to function `bmi` is incorrect
 --> health.py:5:11
  |
5 | print(bmi("70", 1.75))
  |           ^^^^ Expected `float`, found `Literal["70"]`
```

ty checks every call against the hints, including calls that only run on rare inputs, which a test might miss.

## 8. Tests decide, whoever wrote the code

Code from a classmate, from an AI, or from you last week: you decide whether it works by testing it. Write the tests from the docstring, before you read the code. Then you're testing what the code *should* do, not what it happens to do.

Here, the tests come from the docstring: its example, then two edge cases worked out by hand.

```python {.marimo}
def percent_of(part: float, whole: float) -> float:
    """What percent part is of whole: percent_of(25, 200) == 12.5."""
    return part / whole * 100


assert percent_of(25, 200) == 12.5
assert percent_of(0, 50) == 0
assert percent_of(50, 50) == 100
print("all three tests pass")
```

## AI activity

Write a function `clamp(x, lo, hi)`. Then ask an AI: *"Suggest edge-case tests for this function. Don't change the function."* Add the tests you agree with, and log any you rejected and why.

Check each suggested test by hand before you add it. Does any of them expect the wrong answer?

## Exercises (40 minutes)

Open `l06_exercises.py` and run `uv run pytest lectures/06-types-and-tests` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `clamp`, `is_passing` |
| Core | `shift_hours`, `quarter`, `break_even_units`, `cagr` |
| Fix the AI's code | `average_rating` |
| Stretch | `round_up_to`, `continuous_growth` |

When you're done, add one more test of your own for each function in `test_l06_exercises.py`.
