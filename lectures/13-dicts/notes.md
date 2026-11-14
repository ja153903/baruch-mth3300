---
title: "L13: Dicts"
marimo-version: "0.25.2"
---

# L13: Dicts

**By the end of this lecture you can:**

- store and look up key–value pairs
- add, change, and remove entries
- loop over a dict's keys, values, and items
- use `.get` with a default, and the counting pattern
- group values into lists inside a dict
- build dicts with comprehensions
- use a `frozendict` as a key

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L12)

**Predict** both values before you run it:

```python {.marimo}
_pairs = list(zip("abc", [1, 2, 3], strict=True))
print(_pairs[1], [n * 2 for _, n in _pairs])
```

## 1. Key → value

With two parallel lists, finding MSFT's price means searching for its position first:

```python {.marimo}
_tickers = ["AAPL", "MSFT", "NVDA"]
_prices = [190.5, 410.25, 120.0]
print(_prices[_tickers.index("MSFT")])
```

A **dict** stores each value under a **key**, so you can look it up directly:

```python {.marimo}
portfolio = {"AAPL": 10, "MSFT": 5}
portfolio["NVDA"] = 8  # add a key
portfolio["AAPL"] += 2  # update a value
print(portfolio, portfolio["MSFT"], "TSLA" in portfolio)
```

Keys must be **immutable**: strings, numbers, tuples, or the `frozendict` in section 9. Each key appears only once, and `in` checks the keys, not the values. Looking up a missing key raises `KeyError`.

## 2. `.get` with a default

```python {.marimo}
menu = {"coffee": 3.0, "bagel": 2.5}
print(menu.get("coffee"), menu.get("tea"), menu.get("tea", 0.0))
```

Use `d[key]` when the key must be there, so that a missing key is a loud error. Use `.get(key, default)` when a missing key is normal.

## 3. Adding, changing, and removing

**Predict:**

```python {.marimo}
_stock = {"apples": 5, "pears": 2}
_stock["apples"] = 7
_stock["plums"] = 1
del _stock["pears"]
print(_stock, len(_stock))
```

Assigning to a key that already exists **replaces** its value. Dicts remember the order their keys were added, so changing `"apples"` doesn't move it. `.pop(key)` removes a key like `del` does, and also returns its value.

## 4. Looping

```python {.marimo}
for ticker, n in portfolio.items():
    print(f"{ticker:>5}: {n}")
print(list(portfolio.keys()), sum(portfolio.values()))
```

A plain `for key in d` loops over the keys. `.items()` gives `(key, value)` tuples, which you unpack just like in L12.

### Common bug: deleting keys while you loop

Deleting from a dict while you loop over it raises `RuntimeError: dictionary changed size during iteration`. Loop over a copy of the keys, `list(d)`, instead:

```python {.marimo}
_holdings = {"AAPL": 12, "MSFT": 0, "NVDA": 8, "TSLA": 0}
for _t in list(_holdings):
    if _holdings[_t] == 0:
        del _holdings[_t]
print(_holdings)
```

Section 8 shows a shorter way: build a new dict that leaves those keys out.

## 5. The counting pattern

```python {.marimo}
def letter_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


print(letter_counts("mississippi"))
```

The first time you see `ch`, `counts.get(ch, 0)` is 0, so you never get a `KeyError`. An empty dict gives ty no clue about its types, so the hint `dict[str, int]` tells it.

### Common bug: setting instead of adding

**Predict:**

```python {.marimo}
_votes = {}
for _side in ["buy", "sell", "buy", "buy"]:
    _votes[_side] = 1
print(_votes)
```

Each vote **replaces** the count with 1. Like the accumulator bug in L10, the fix is to build on the old value.

## 6. A finance example: valuing a portfolio

Two dicts with the same keys work together. Here, one holds shares and the other holds prices:

```python {.marimo}
prices = {"AAPL": 190.5, "MSFT": 410.25, "NVDA": 120.0}
value = sum(n * prices[t] for t, n in portfolio.items())
print(f"Portfolio value: ${value:,.2f}")
```

Each position's weight is its value divided by the total:

```python {.marimo}
for _t, _n in portfolio.items():
    _position = _n * prices[_t]
    print(f"{_t:<5} {_position:>9,.2f} {_position / value:>7.1%}")
```

**Question:** what happens if you hold a ticker that's missing from `prices`? Which would you rather have: an error, or a value of 0?

## 7. Grouping: a dict of lists

Sometimes a key needs several values. Make each value a list, and start a new list the first time you see a key:

```python {.marimo}
trade_log = [("AAPL", 10), ("MSFT", 5), ("AAPL", -4), ("NVDA", 8), ("MSFT", 5)]

by_ticker: dict[str, list[int]] = {}
for _t, _shares in trade_log:
    if _t not in by_ticker:
        by_ticker[_t] = []
    by_ticker[_t].append(_shares)
print(by_ticker)
```

### Dicts inside dicts

A value can even be another dict. Data from websites and APIs often looks like this, with one record per key:

```python {.marimo}
book = {
    "AAPL": {"shares": 10, "price": 190.5},
    "MSFT": {"shares": 5, "price": 410.25},
}
print(book["MSFT"]["price"])
for _t, _info in book.items():
    print(_t, _info["shares"] * _info["price"])
```

**Predict:** what does `book["AAPL"]["shares"]` give? What about `book["shares"]`?

## 8. Dict comprehensions

`{key: value for item in iterable if condition}` builds a dict, just as a list comprehension builds a list.

```python {.marimo}
_names = ["AAPL", "MSFT", "NVDA"]
_counts = [10, 5, 8]
print({t: c for t, c in zip(_names, _counts, strict=True)})
print({t: sum(s) for t, s in by_ticker.items()})
print({t: p for t, p in prices.items() if p > 150})
```

The second line turns the trade log into net positions: you bought 10 AAPL and sold 4, so you hold 6.

## 9. New in Python 3.15: `frozendict`

A `frozendict` is a dict that can't change after it's created. Because it can't change, it can be a key in another dict.

```python {.marimo}
_weights = frozendict(tech=0.6, energy=0.4)
_labels = {_weights: "aggressive"}
print(_labels[frozendict(energy=0.4, tech=0.6)])
```

**Predict:** the two `frozendict`s above list their keys in different orders, yet the lookup works. Why?

**Predict, then try it in the REPL:** does this work? Read the error if it doesn't.

```python
{frozendict(a=[1, 2]): "x"}
```

## AI activity: check the explanation

1. Ask an AI: *"Why can't a list be a dict key in Python?"* Then try `{[1, 2]: "x"}` yourself and read the error. Does the error match the AI's explanation?
2. `frozendict` is new in Python 3.15, so many AIs haven't heard of it. Ask yours how to use a dict as a key in another dict. Does it suggest `frozendict`, or an older workaround? Run whatever it suggests, and log the answer.

## Exercises (40 minutes)

Open `l13_exercises.py` and run `uv run pytest lectures/13-dicts` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `tickers_above`, `order_total` |
| Core | `letter_frequencies`, `net_positions`, `apply_splits` |
| Fix the AI's code | `first_trade_day` |
| Stretch | `count_allocations`, `top_holding` |
