---
title: "L16: Exceptions and CSV"
marimo-version: "0.25.2"
---

# L16: Exceptions and CSV

**By the end of this lecture you can:**

- name common exceptions, and read what went wrong
- catch specific exceptions with `try`/`except`
- explain why catching too much hides bugs
- raise exceptions with helpful messages
- read and write CSV files with `csv`
- skip bad rows in messy data, and count them

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L15)

**Predict** both values before you run it:

```python {.marimo}
_text = "AAPL\n  MSFT \n\nNVDA\n"
_lines = _text.splitlines()
print(len(_lines), [s.strip() for s in _lines if s.strip() != ""])
```

## 1. When something goes wrong

When Python can't do what you asked, it **raises an exception**. If nothing catches it, the program stops and prints a traceback. The last line of the traceback names the exception:

| Exception | One way to cause it |
|---|---|
| `ValueError` | `int("12.5")` |
| `ZeroDivisionError` | `1 / 0` |
| `KeyError` | `{"a": 1}["b"]` |
| `IndexError` | `[1, 2][5]` |
| `TypeError` | `"3" + 4` |
| `FileNotFoundError` | `Path("nope.txt").read_text()` |

`try`/`except` catches an exception, so the program can carry on. **Predict** which letters print:

```python {.marimo}
try:
    print("A")
    _x = int("oops")
    print("B")
except ValueError:
    print("C")
print("D")
```

As soon as `int("oops")` fails, Python jumps to the matching `except`. The rest of the `try` block never runs. Add `as err` to get the exception itself, with its message:

```python {.marimo}
try:
    int("12.5")
except ValueError as err:
    print("ValueError:", err)
```

## 2. Catching exceptions

```python {.marimo}
def parse_amount(text: str) -> float | None:
    try:
        return float(text.replace("$", "").replace(",", ""))
    except ValueError:
        return None


print(parse_amount("$1,234.50"), parse_amount("abc"))
```

Catch the **specific** exception you expect. A bare `except:` also hides real bugs. Keep the `try` block small, too: put only the line that can fail inside it.

## 3. Catching more than one kind

Since Python 3.14, you don't need parentheses around several exception types:

```python {.marimo}
def safe_ratio(a: str, b: str) -> float | None:
    try:
        return float(a) / float(b)
    except ValueError, ZeroDivisionError:
        return None


print(safe_ratio("6", "3"), safe_ratio("6", "0"), safe_ratio("x", "3"))
```

## 4. Common bug: catching too much

**Predict:** what does this print? Is it right?

```python {.marimo}
_row = {"ticker": "AAPL", "price": "190.5"}
try:
    _price = float(_row["Price"])  # typo: the key is "price"
except Exception:
    _price = 0.0
print(_price)
```

`except Exception` catches almost **every** kind of error, including the `KeyError` from the typo. The program runs, quietly gives a wrong answer, and nothing tells you why. With `except ValueError`, the `KeyError` would stop the program and point straight at the typo.

## 5. Raising exceptions

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

Raise an exception when your function gets input it can't handle, and put the bad value in the message. Return `None` only when "no answer" is a normal result, as with `parse_amount("abc")`.

## 6. CSV files

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

`csv.DictReader` turns each row into a dict keyed by the header. Every value arrives as a **string**. Open CSV files with an empty `newline`, as in the code above, because the `csv` module handles line endings itself.

### Why not `split(",")`?

A value can contain a comma, as long as it's in quotes. **Predict:**

```python {.marimo}
_line = '"Lovelace, Ada",100'
print(_line.split(","))
print(list(csv.reader([_line])))
```

`csv.reader` gives each row as a plain list of strings, with no header.

## 7. A missing file

L15 checked `.exists()` before reading. With `try`, you just read the file, and handle the error if it isn't there:

```python {.marimo}
try:
    trades.with_name("missing.csv").read_text()
except FileNotFoundError as err:
    print("No such file:", Path(err.filename).name)
```

## 8. Writing CSV

```python {.marimo}
summary = trades.with_name("summary.csv")
with open(summary, "w", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["ticker", "value"])
    writer.writerow(["AAPL", 1905.0])
print(summary.read_text())
```

`csv.writer` adds quotes around any value that needs them, so a name like `Lovelace, Ada` comes back in one piece.

## 9. A finance example: clean, total, and report

Put it together: read the trades, skip the bad rows but count them, total the value for each ticker, and write a report. The `try` lives in a small helper, so it surrounds only the code that can fail.

```python {.marimo}
def row_value(row: dict[str, str]) -> float | None:
    try:
        return int(row["shares"]) * float(row["price"])
    except ValueError:
        return None


def summarize_trades(src: Path, dst: Path) -> int:
    """Write each ticker's total value to dst. Return how many rows were skipped."""
    totals: dict[str, float] = {}
    skipped = 0
    with open(src, newline="") as f:
        for row in csv.DictReader(f):
            value = row_value(row)
            if value is None:
                skipped += 1
            else:
                totals[row["ticker"]] = totals.get(row["ticker"], 0.0) + value
    with open(dst, "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["ticker", "total"])
        for ticker in sorted(totals):
            writer.writerow([ticker, f"{totals[ticker]:.2f}"])
    return skipped
```

**Predict:** which rows get skipped, and what is AAPL's total?

```python {.marimo}
_messy = trades.with_name("messy.csv")
_messy.write_text(
    "ticker,shares,price\n"
    "AAPL,10,190.50\n"
    "MSFT,5,410.25\n"
    "AAPL,-4,195.00\n"
    "NVDA,,120\n"
    "TSLA,3,n/a\n"
)
_report = trades.with_name("report.csv")
print("skipped:", summarize_trades(_messy, _report))
print(_report.read_text())
```

## AI activity: a skill that runs your code

Skills can include scripts. The AI runs your script instead of guessing, so the answer comes from your code, not from the model.

1. Write `scripts/check_csv.py` inside a new `csv-check` skill folder (`.agents/skills/csv-check/`). It takes a CSV path, reads it with `csv.DictReader`, and prints the line number and the problem for every row with a missing or non-numeric `price`. Use `try`/`except ValueError`.
2. Write `SKILL.md`. Its instructions tell the AI to run `uv run python .agents/skills/csv-check/scripts/check_csv.py <file>` and explain the results, not to read the CSV itself.
3. Copy the whole folder, script included, to `.github/skills/csv-check/`, and run `uv run pytest lectures/10-loop-patterns`.
4. Make a CSV with three bad rows of your own. Ask your AI: *"Is prices.csv clean?"* Did it run your script? Did it report all three rows?

## Exercises (40 minutes)

The file exercises take a `Path`, and their tests make CSV files in a temporary folder with pytest's `tmp_path`. Open `l16_exercises.py` and run `uv run pytest lectures/16-exceptions-csv` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `parse_int`, `check_percent` |
| Core | `read_prices`, `parse_money`, `count_bad_rows`, `write_report` |
| Fix the AI's code | `total_shares` |
| Stretch | `read_trades` |
