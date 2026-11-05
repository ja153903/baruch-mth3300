---
title: "L17: Recursion"
marimo-version: "0.25.2"
---

# L17: Recursion

**By the end of this lecture you can:**

- write a recursive function with a base case and a recursive case
- trace recursive calls
- recognize when recursion fits a problem naturally

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. A function that calls itself

```python {.marimo}
def factorial(n: int) -> int:
    if n == 0:  # base case: stop here
        return 1
    return n * factorial(n - 1)  # recursive case: a smaller problem


print(factorial(5))
```

Every recursive function needs:

1. a **base case** that answers directly, and
2. a **recursive case** that moves *toward* the base case.

## 2. Tracing the calls

```python {.marimo}
def traced_factorial(n: int, depth: int = 0) -> int:
    print("  " * depth + f"factorial({n})")
    if n == 0:
        return 1
    return n * traced_factorial(n - 1, depth + 1)


print(traced_factorial(3))
```

## 3. Recursion on strings and lists

```python {.marimo}
def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


def total(xs: list[int]) -> int:
    if not xs:
        return 0
    return xs[0] + total(xs[1:])


print(is_palindrome("racecar"), is_palindrome("baruch"), total([1, 2, 3, 4]))
```

## 4. When recursion goes wrong

With no base case, or one you never reach, Python stops after about 1000 nested calls:

```python {.marimo}
def broken(n: int) -> int:
    return broken(n - 1)


try:
    broken(5)
except RecursionError as err:
    print("RecursionError:", err)
```

## 5. Problems that are naturally recursive

```python {.marimo}
def gcd(a: int, b: int) -> int:
    """Euclid's algorithm, from about 300 BC."""
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(3300, 1210))
```

## AI activity

Ask an AI to trace `gcd(3300, 1210)` step by step. Then trace it yourself on paper. Does the AI's trace match yours exactly?

**Exercises:** `l17_exercises.py`
