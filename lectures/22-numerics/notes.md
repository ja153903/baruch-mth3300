---
title: "L22: Numbers you can trust"
marimo-version: "0.25.2"
---

# L22: Numbers you can trust

**By the end of this lecture you can:**

- explain why `0.1 + 0.2 != 0.3`
- use `Decimal` for money and `Fraction` for exact math
- run a reproducible random simulation

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Floats are binary approximations

```python {.marimo}
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
```

`0.1` has no exact binary representation, just as 1/3 has no exact decimal one. **Never** compare floats with `==`. Use `math.isclose` instead.

```python {.marimo}
import math

print(math.isclose(0.1 + 0.2, 0.3))
print(sum([0.1] * 10), math.fsum([0.1] * 10))
```

## 2. `Decimal` for money

```python {.marimo}
from decimal import ROUND_HALF_UP, Decimal

subtotal = Decimal("19.99") * 3
tax_amount = (subtotal * Decimal("0.08875")).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)
print(subtotal, tax_amount, subtotal + tax_amount)
```

Always build a `Decimal` from a **string**. `Decimal(0.1)` carries over the float's error.

## 3. `Fraction` for exact rational math

```python {.marimo}
from fractions import Fraction

print(Fraction(1, 3) + Fraction(1, 6))
print(sum(Fraction(1, k) for k in range(1, 6)))
```

## 4. Simulation with `random`

Estimate the probability that two dice sum to 7, which is exactly 1/6:

```python {.marimo}
import random


def estimate_seven(trials: int, seed: int) -> float:
    rng = random.Random(seed)
    hits = sum(rng.randint(1, 6) + rng.randint(1, 6) == 7 for _ in range(trials))
    return hits / trials


for n in [100, 10_000, 1_000_000]:
    print(f"{n:>9,}: {estimate_seven(n, seed=3300):.4f}   (exact {1 / 6:.4f})")
```

**Seeds** make a simulation reproducible: the same seed always gives the same "random" numbers. The error shrinks roughly like 1/√n.

## AI activity

Ask an AI: *"Should a bank store balances as floats?"* Then test its claims with `Decimal` and `float` yourself. Did anything it said turn out to be wrong?

**Exercises:** `l22_exercises.py`
