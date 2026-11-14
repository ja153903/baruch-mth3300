---
title: "L03: Strings"
marimo-version: "0.25.2"
---

# L03: Strings

**By the end of this lecture you can:**

- find the length of a string with `len`
- index and slice strings, including negative positions and steps
- use common string methods, and chain them together
- check for a piece of text with `in`
- build new strings with `+`, `*`, and `str()`
- explain why strings can't be changed in place

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L02)

**Predict** the output before you run it:

```python {.marimo}
_x = 7
_x += 3
_x = _x // 4
print(_x, 17 % 5, 2**3)
print(int("12") + 3, float(2), type(7 / 7))
```

## 1. Strings and `len`

A string is a sequence of characters: letters, digits, spaces, and punctuation. `len` counts them all.

```python {.marimo}
print(len("Baruch"), len("Baruch College"), len(""))
print("It's 9 o'clock", 'She said "hi"')
```

- The **empty string** has no characters, so its length is 0.
- Use double quotes around text that contains an apostrophe, and single quotes around text that contains double quotes.

## 2. Indexing

Positions start at **0**. Negative indexes count from the end.

```python {.marimo}
word = "Baruch"
print(word[0], word[1], word[-1], len(word))
```

| character | B | a | r | u | c | h |
|---|---|---|---|---|---|---|
| index | 0 | 1 | 2 | 3 | 4 | 5 |
| negative index | -6 | -5 | -4 | -3 | -2 | -1 |

### Common bug: one past the end

`word` has 6 characters, so its last index is 5, not 6:

```python {.marimo}
try:
    print(word[6])
except IndexError as err:
    print("IndexError:", err)
```

The last character is always `word[len(word) - 1]`, or more simply `word[-1]`.

## 3. Slicing

`s[start:stop:step]` includes `start` and stops **before** `stop`.

**Predict:**

```python {.marimo}
print(word[0:3])
print(word[2:])
print(word[:-1])
print(word[::-1])
```

Leave out `start` to begin at the start, and leave out `stop` to go to the end. A step of `-1` goes backwards.

**Predict** these too:

```python {.marimo}
_digits = "0123456789"
print(_digits[1::2])
print(_digits[::3])
print(_digits[7:2:-1])
print(_digits[5:100])
```

A slice never raises `IndexError`: a stop past the end just stops at the end. A handy fact: `s[a:b]` has `b - a` characters.

### Slicing fixed formats

Dates, codes, and tickers often have a fixed layout, so slices can take them apart:

```python {.marimo}
date = "2026-11-13"
year = date[:4]
month = date[5:7]
day = date[8:]
print(year, month, day)
```

## 4. Methods

A method is a function that belongs to a value: `value.method()`.

```python {.marimo}
name = "  ada LOVELACE  "
print(repr(name.strip()))
print(name.strip().title())
print(name.upper().count("A"))
print("ada" in name)
print("a,b,c".split(","))
print("-".join(["2026", "11", "05"]))
```

(`repr` shows a string with its quotes, so you can see the spaces.)

| Method | Gives back | Example | Result |
|---|---|---|---|
| `upper()`, `lower()` | all capitals, or no capitals | `"Hi".upper()` | `'HI'` |
| `title()` | each word capitalized | `"wall street".title()` | `'Wall Street'` |
| `strip()` | without spaces at either end | `"  hi  ".strip()` | `'hi'` |
| `replace(old, new)` | every `old` swapped for `new` | `"11/13/2026".replace("/", "-")` | `'11-13-2026'` |
| `count(t)` | how many times `t` appears | `"banana".count("a")` | `3` |
| `find(t)` | the index of the first `t`, or `-1` | `"banana".find("n")` | `2` |
| `startswith(t)`, `endswith(t)` | `True` or `False` | `"hw03.py".endswith(".py")` | `True` |
| `isdigit()` | `True` if every character is a digit | `"3300".isdigit()` | `True` |
| `split(sep)` | a list of the pieces | `"a,b,c".split(",")` | `['a', 'b', 'c']` |

A list holds several values in order. You'll learn lists properly in L11.

### Chaining

A method gives back a new value, so you can call another method on the result, or slice it:

```python {.marimo}
_quote = "AAPL:227.48"
_colon = _quote.find(":")
print(_colon, _quote[:_colon], _quote[_colon + 1 :])
```

## 5. Checking for text with `in`

`text in s` is `True` if `text` appears anywhere inside `s`. **Predict:**

```python {.marimo}
print("ruch" in "Baruch")
print("@" in "student.baruch.cuny.edu")
print("A" in "aapl")
```

`in` is case-sensitive. To ignore case, lowercase both sides first.

## 6. Building strings

`+` joins strings, and `*` repeats one. To join a number to a string, convert it with `str()` first:

```python {.marimo}
_ticker = "NVDA"
_shares = 25
print(_ticker + ": " + str(_shares) + " shares")
print("=" * 20)
```

In L04 you'll meet f-strings, an easier way to put numbers into text.

## 7. Strings are immutable

You can't change a character in place. Methods return a **new** string.

```python {.marimo}
city = "new york"
shouted = city.upper()
print(city, "->", shouted)
try:
    city[0] = "N"
except TypeError as err:
    print("TypeError:", err)
```

### Common bug: forgetting to keep the result

**Predict:**

```python {.marimo}
_ticker = "aapl"
_ticker.upper()
print(_ticker)
```

`upper()` made a new string, and nothing stored it. Write `_ticker = _ticker.upper()` to keep it.

## 8. A finance example: cleaning messy data

Data copied from a website or a spreadsheet is often messy: extra spaces, the wrong case, and dollar signs and commas inside numbers. Clean it before you use it:

```python {.marimo}
_ticker_raw = "  nvda "
_price_raw = "$1,450.25"
_ticker = _ticker_raw.strip().upper()
_price = float(_price_raw.replace("$", "").replace(",", ""))
print(_ticker, _price, _price * 2)
```

**Predict:** what goes wrong if you call `float("$1,450.25")` without cleaning it first?

## AI activity

Ask an AI: *"Give me five Python slicing puzzles on the string 'programming', without answers."*

Solve them on paper, check them in the REPL, and log which ones fooled you.

For each one that fooled you, ask the AI to explain the answer step by step. Then make up one more puzzle of the same kind and check it yourself.

## Exercises (40 minutes)

Open `l03_exercises.py`. Replace each `None` with an expression, and run `uv run pytest lectures/03-strings` as you go. Do them in order:

| Group | Variables |
|---|---|
| Warmup | `first_three`, `reversed_word` |
| Core | `country_code` / `check_digit`, `clean_ticker`, `iso_date`, `masked_card` |
| Fix the AI's code | `last_three` |
| Stretch | `middle_letter`, `word_count` |
