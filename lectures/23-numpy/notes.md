---
title: "L23: NumPy and plotting"
marimo-version: "0.25.2"
---

# L23: NumPy and plotting

**By the end of this lecture you can:**

- add a library to a project with `uv add`
- do math on whole arrays at once, without loops
- make a labeled plot with matplotlib

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Adding libraries

```sh
uv add numpy matplotlib
```

This updates `pyproject.toml` and `uv.lock`, so anyone who clones your project gets exactly the same versions.

## 2. Arrays

```python {.marimo}
import numpy as np

prices = np.array([100.0, 102.0, 99.0, 105.0, 107.0])
print(prices * 2)  # works on every element: no loop needed
print(prices.mean(), prices.std(), prices.max())
print(prices[prices > 100])
```

## 3. Vectorized finance

```python {.marimo}
returns = prices[1:] / prices[:-1] - 1
growth = np.cumprod(1 + returns)
print(np.round(returns, 4))
print(f"total return: {growth[-1] - 1:.2%}")
```

**Predict:** what's the shape of `returns` compared with `prices`?

## 4. Speed

```python {.marimo}
import time

values = np.random.default_rng(0).random(1_000_000)
start = time.perf_counter()
loop_total = 0.0
for v in values:
    loop_total += v * v
loop_time = time.perf_counter() - start
start = time.perf_counter()
vector_total = float(values @ values)
vector_time = time.perf_counter() - start
print(
    f"loop {loop_time:.3f}s, numpy {vector_time:.5f}s, same answer: {np.isclose(loop_total, vector_total)}"
)
```

## 5. Plotting

```python {.marimo}
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(range(len(prices)), prices, marker="o")
ax.set_xlabel("Day")
ax.set_ylabel("Price ($)")
ax.set_title("A made-up stock")
ax
```

Every plot needs a title, axis labels, and units.

## 6. marimo notebooks

These notes are a **marimo** notebook. To run them interactively:

```sh
uv run marimo edit lectures/23-numpy/notes.md
```

## AI activity: start your final project

Describe your final-project idea to an AI, and ask it which NumPy functions would help. Before you use any of them, look it up in the official NumPy documentation and check that it does what the AI said.

**Exercises:** `l23_exercises.py`
