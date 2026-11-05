---
title: "L13: Dicts"
marimo-version: "0.25.2"
---

# L13: Dicts

**By the end of this lecture you can:**

- store and look up key–value pairs
- loop over a dict's keys, values, and items
- use `.get` and the counting pattern

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Key → value

```python {.marimo}
portfolio = {"AAPL": 10, "MSFT": 5}
portfolio["NVDA"] = 8  # add a key
portfolio["AAPL"] += 2  # update a value
print(portfolio, portfolio["MSFT"], "TSLA" in portfolio)
```

Keys must be **immutable**: strings, numbers, or tuples. Looking up a missing key raises `KeyError`.

## 2. `.get` with a default

```python {.marimo}
menu = {"coffee": 3.0, "bagel": 2.5}
print(menu.get("coffee"), menu.get("tea"), menu.get("tea", 0.0))
```

## 3. Looping

```python {.marimo}
for ticker, n in portfolio.items():
    print(f"{ticker:>5}: {n}")
print(list(portfolio.keys()), sum(portfolio.values()))
```

## 4. The counting pattern

```python {.marimo}
def letter_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


print(letter_counts("mississippi"))
```

## 5. Combining two dicts

```python {.marimo}
prices = {"AAPL": 190.5, "MSFT": 410.25, "NVDA": 120.0}
value = sum(n * prices[t] for t, n in portfolio.items())
print(f"Portfolio value: ${value:,.2f}")
```

## AI activity

Ask an AI: *"Why can't a list be a dict key in Python?"* Then try `{[1, 2]: "x"}` yourself and read the error. Does the error match the AI's explanation?

**Exercises:** `l13_exercises.py`
