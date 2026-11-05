---
title: "L08: Code quality"
marimo-version: "0.25.2"
---

# L08: Code quality

**By the end of this lecture you can:**

- use ruff to find and fix style problems
- use ty to catch type errors before the code runs
- debug methodically, and with an AI, without just asking for the answer

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Code is read more often than it's written

Compare these two versions of the same function:

```python {.marimo}
def f(a, b):
    c = a * b / 100
    return a - c


def sale_price(price: float, discount_percent: float) -> float:
    discount = price * discount_percent / 100
    return price - discount


print(f(80, 25), sale_price(80, 25))
```

Good names, type hints, and small functions are what make code readable.

## 2. ruff: lint and format

```sh
uv run ruff check          # find problems: unused imports, undefined names...
uv run ruff check --fix    # fix the safe ones automatically
uv run ruff format         # consistent spacing and layout
```

## 3. ty: types

```sh
uv run ty check
```

```python
def sale_price(price: float, discount_percent: float) -> float: ...


sale_price("80", 25)  # ty: Argument of type `Literal["80"]` is not assignable to `float`
```

## 4. Debugging methodically

1. **Reproduce it:** find the smallest input that shows the bug.
2. **Compare:** what did you *expect*, and what *actually* happened?
3. **Narrow it down:** add `print(f"{x=}")` or use `breakpoint()`.
4. **Fix it, then add a test** so the bug can never come back.

```python {.marimo}
def absolute(x: float) -> float:
    if x > 0:
        return x
    return x  # bug: what should this line be?


print(f"{absolute(5)=}, {absolute(-5)=}")
```

## 5. Debugging with AI, the right way

| Weak prompt | Strong prompt |
|---|---|
| "fix my code" | "Here's my function, the input, what I expected, and what happened. Explain what's wrong without rewriting it." |
| pasting 200 lines | the smallest piece of code that reproduces the bug |

## AI activity

Take a function from homework 03 and ask an AI to review it for **readability only**. Run `ruff` and `ty` on it too. Compare the AI's suggestions with what the tools found.

**Exercises:** `l08_exercises.py`
