---
title: "L16: Exceptions and CSV"
marimo-version: "0.25.2"
---

# L16: Exceptions and CSV

**By the end of this lecture you can:**

- catch specific exceptions with `try`/`except`
- raise exceptions with helpful messages
- read and write CSV files

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Catching exceptions

```python {.marimo}
def parse_amount(text: str) -> float | None:
    try:
        return float(text.replace("$", "").replace(",", ""))
    except ValueError:
        return None


print(parse_amount("$1,234.50"), parse_amount("abc"))
```

Catch the **specific** exception you expect. A bare `except:` also hides real bugs.

## 2. Catching more than one kind

Since Python 3.14, you don't need parentheses around several exception types:

```python {.marimo}
def safe_ratio(a: str, b: str) -> float | None:
    try:
        return float(a) / float(b)
    except ValueError, ZeroDivisionError:
        return None


print(safe_ratio("6", "3"), safe_ratio("6", "0"), safe_ratio("x", "3"))
```

## 3. Raising exceptions

```python {.marimo}
def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise ValueError(f"insufficient funds: balance {balance}, requested {amount}")
    return balance - amount


try:
    withdraw(50, 80)
except ValueError as err:
    print("Error:", err)
```

## 4. CSV files

```python {.marimo}
import csv
import tempfile
from pathlib import Path

trades = Path(tempfile.mkdtemp()) / "trades.csv"
trades.write_text("ticker,shares,price\nAAPL,10,190.50\nMSFT,5,410.25\nBAD,x,1\n")

with open(trades, newline="") as f:
    for row in csv.DictReader(f):
        try:
            print(row["ticker"], int(row["shares"]) * float(row["price"]))
        except ValueError:
            print(row["ticker"], "skipped: bad data")
```

`csv.DictReader` turns each row into a dict keyed by the header. Every value arrives as a **string**.

## 5. Writing CSV

```python {.marimo}
summary = trades.with_name("summary.csv")
with open(summary, "w", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["ticker", "value"])
    writer.writerow(["AAPL", 1905.0])
print(summary.read_text())
```

## AI activity

Give an AI a CSV row with a missing value, and ask it to write code that handles it. Then test its code on three bad rows you make up yourself. Did it handle all three?

**Exercises:** `l16_exercises.py`
