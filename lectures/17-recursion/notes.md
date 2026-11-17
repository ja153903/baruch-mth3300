---
title: "L17: Recursion"
marimo-version: "0.25.2"
---

# L17: Recursion

**By the end of this lecture you can:**

- write a recursive function with a base case and a recursive case
- trace recursive calls, and explain the call stack
- write recursive functions on numbers, strings, and lists
- solve problems that are naturally recursive, like nested lists and the Tower of Hanoi
- spot a missing base case, a missing `return`, and recursion that goes too deep

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L16)

**Predict** the total:

```python {.marimo}
_total = 0
for _text in ["10", "x", "5", "2.5"]:
    try:
        _total += int(_text)
    except ValueError:
        _total -= 1
print(_total)
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

It works like a proof by induction. If the base case is right, and each step is right whenever the smaller case is right, then every case is right.

## 2. Tracing the calls

```python {.marimo}
def traced_factorial(n: int, depth: int = 0) -> int:
    print("  " * depth + f"factorial({n})")
    if n == 0:
        return 1
    return n * traced_factorial(n - 1, depth + 1)


print(traced_factorial(3))
```

Each call waits for the call below it to finish. Python keeps the waiting calls on the **call stack**. **Predict** the order of the lines:

```python {.marimo}
def countdown(n: int) -> None:
    if n == 0:
        print("liftoff")
        return
    print("down", n)
    countdown(n - 1)
    print("back in", n)


countdown(3)
```

The lines after the recursive call run on the way back up, in reverse order.

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

The pattern: handle the first item yourself, and let the recursive call handle the rest, `xs[1:]`. The empty list is the base case.

**Predict:** how many calls does `total([1, 2, 3, 4])` make, counting the first one?

## 4. A finance example: compound interest

"This year's balance is last year's balance times (1 + rate)." That sentence is already a recursive definition:

```python {.marimo}
def balance(principal: float, rate: float, years: int) -> float:
    if years == 0:
        return principal
    return balance(principal, rate, years - 1) * (1 + rate)


print(f"{balance(1000, 0.07, 10):,.2f}")
```

It matches year 10 of the growth table in L09, which used a loop.

## 5. Recursion that branches: the Tower of Hanoi

Move a stack of n disks from peg A to peg C, one disk at a time, and never put a bigger disk on a smaller one. The recursive idea: move the top n − 1 disks out of the way to B, move the biggest disk to C, then move the n − 1 disks from B on top of it.

```python {.marimo}
def hanoi(n: int, start: str, end: str, spare: str) -> None:
    if n == 0:
        return
    hanoi(n - 1, start, spare, end)
    print(f"move disk {n} from {start} to {end}")
    hanoi(n - 1, spare, end, start)


hanoi(3, "A", "C", "B")
```

**Predict:** how many moves does it take for 4 disks?

Each extra disk doubles the work, plus one move: moves(n) = 2 · moves(n − 1) + 1, and moves(0) = 0.

```python {.marimo}
def hanoi_moves(n: int) -> int:
    if n == 0:
        return 0
    return 2 * hanoi_moves(n - 1) + 1


print([hanoi_moves(n) for n in range(1, 11)])
print(f"{hanoi_moves(64):,}")
```

The pattern is 2ⁿ − 1, which you can prove by induction. At one move per second, 64 disks take about 585 billion years.

## 6. Nested data

Recursion fits data that contains smaller copies of itself. A fund of funds holds stocks, and also other funds, which can hold more funds. `isinstance(h, list)` checks whether `h` is a list:

```python {.marimo}
def nested_total(holdings: list) -> float:
    result = 0.0
    for h in holdings:
        if isinstance(h, list):
            result += nested_total(h)  # a fund inside the fund
        else:
            result += h
    return result


fund = [100.0, [50.0, 25.0], [[10.0], 5.0]]
print(nested_total(fund))
```

A plain loop can't do this by itself, because you don't know in advance how deep the nesting goes.

## 7. When recursion goes wrong

With no base case, or one you never reach, Python stops after about 1000 nested calls:

```python {.marimo}
def broken(n: int) -> int:
    return broken(n - 1)


try:
    broken(5)
except RecursionError as err:
    print("RecursionError:", err)
```

The limit applies to correct functions too. **Predict:** does `total` work on a list of 5,000 numbers?

```python {.marimo}
import sys

print(sys.getrecursionlimit())
try:
    total(list(range(5000)))
except RecursionError:
    print("too deep for recursion")
print(sum(range(5000)))
```

### Common bug: a base case you never reach

```python {.marimo}
def factorial_v2(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial_v2(n - 1)


print(factorial_v2(5))
```

**Predict:** `factorial_v2(5)` works. What does `factorial_v2(0)` do? Trace the first few calls.

### Common bug: forgetting to `return`

```python
def total_v2(xs: list[int]) -> int:
    if not xs:
        return 0
    xs[0] + total_v2(xs[1:])  # computes the answer, then throws it away
```

**Predict, then try it in the REPL:** what does `total_v2([1, 2, 3])` do? Run `uv run ty check` on it too: ty catches this bug before you run anything.

## 8. Problems that are naturally recursive

```python {.marimo}
def gcd(a: int, b: int) -> int:
    """Euclid's algorithm, from about 300 BC."""
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(3300, 1210))
```

Why does it stop? `a % b` is always smaller than `b`, so the second number shrinks with every call until it reaches 0.

## 9. Recursion or a loop?

- Anything you can write with recursion, you can also write with a loop.
- Use recursion when the problem is recursive: nested data, branching like the Tower of Hanoi, and "divide and conquer," like merge sort in L18.
- Use a loop for a simple walk through a long list. It's faster, and it never hits the depth limit.

## AI activity: check the trace

1. Ask an AI to trace `gcd(3300, 1210)` step by step. Then trace it yourself on paper. Does the AI's trace match yours exactly?
2. Ask it to list the moves for `hanoi(3, "A", "C", "B")`, and compare them with the output above. Long traces are easy to get wrong. Did it get every move right?

## Exercises (40 minutes)

Write every function recursively, even when a loop would be easier. Open `l17_exercises.py` and run `uv run pytest lectures/17-recursion` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `digit_sum`, `countdown_list` |
| Core | `power`, `reverse`, `count_char`, `max_value` |
| Fix the AI's code | `count_digits` |
| Stretch | `fast_power`, `subsets` |
