---
title: "L08: Code quality"
marimo-version: "0.25.2"
---

# L08: Code quality

**By the end of this lecture you can:**

- choose clear names, and replace magic numbers with named constants
- write comments that explain *why*, not *what*
- use ruff to find and fix style problems
- use ty to catch type errors before the code runs
- debug methodically, and with an AI, without just asking for the answer
- write a skill that tells your AI how to review code

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L07)

**Predict** the output before you run it:

```python {.marimo}
def _bucket(x: int) -> str:
    if x > 10:
        return "big"
    elif x > 5:
        return "medium"
    return "small"


print(_bucket(10), _bucket(11), _bucket(5))
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

| What | Style | Example |
|---|---|---|
| variables and functions | lowercase words joined by `_` | `sale_price`, `discount_percent` |
| constants: values that never change | all capitals | `NYC_SALES_TAX` |
| booleans | a yes-or-no question | `is_member`, `has_discount` |

Single letters are fine in math formulas (`x`, `n`) and in very short code. Everywhere else, say what the value is.

**Try it:** what does `g` compute? Rename the function and its parameters so nobody has to guess.

```python {.marimo}
def g(a, b, c):
    return a * (1 + b) ** c


print(g(1000, 0.05, 10))
```

## 2. Named constants instead of magic numbers

A **magic number** is a number in the code with no explanation. Is `1.08875` a tax, a fee, or a typo? Give it a name instead:

```python {.marimo}
NYC_SALES_TAX = 0.08875
STUDENT_DISCOUNT = 0.10


def checkout_total(price: float, is_student: bool) -> float:
    if is_student:
        price = price * (1 - STUDENT_DISCOUNT)
    return round(price * (1 + NYC_SALES_TAX), 2)


print(checkout_total(80, False), checkout_total(80, True))
```

When the tax rate changes, you change one line. And a typo in a name gets caught:

```python {.marimo}
try:
    print(80 * (1 + NYC_SALE_TAX))
except NameError as err:
    print("NameError:", err)
```

A typo in a number, like `0.0875` instead of `0.08875`, gives no error at all, just a wrong answer that looks fine.

## 3. Comments and docstrings

A docstring says **what** a function does. A comment says **why** the code does something that might surprise a reader. Don't repeat the code in English:

```python
count = count + 1  # add 1 to count: says nothing new
trading_days = 252  # not 365: markets close on weekends and holidays
```

```python {.marimo}
def annual_to_daily(rate: float) -> float:
    """The daily rate that compounds to `rate` over one year of trading."""
    return (1 + rate) ** (1 / 252) - 1  # 252 trading days, not 365


print(f"{annual_to_daily(0.10):.4%}")
```

## 4. ruff: lint and format

```sh
uv run ruff check          # find problems: unused imports, undefined names...
uv run ruff check --fix    # fix the safe ones automatically
uv run ruff format         # consistent spacing and layout
```

For example, here is a messy `tip.py`:

```text
import math


def tip(bill,rate = 0.2):
    total=bill*rate
    return bill*rate
```

`uv run ruff check` finds two problems (output shortened):

```text
F401 [*] `math` imported but unused
 --> tip.py:1:8
F841 Local variable `total` is assigned to but never used
 --> tip.py:5:5
Found 2 errors.
```

`[*]` means `ruff check --fix` can fix it for you. `uv run ruff format` fixes the spacing: `def tip(bill, rate=0.2):` and `total = bill * rate`. Unused names often point at a real bug: here, the author computed `total` and then forgot to use it.

## 5. ty: types

```sh
uv run ty check
```

```python
def sale_price(price: float, discount_percent: float) -> float: ...


sale_price("80", 25)  # ty: Expected `float`, found `Literal["80"]`
```

ruff and ty only check what the code *looks like*. They can't tell whether `sale_price` gives the right answer. That's what tests are for.

## 6. Debugging methodically

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

### A worked example

A classmate's `percent_change` gives the wrong answer:

```python {.marimo}
def percent_change(old: float, new: float) -> float:
    change = new - old
    return change / new * 100


print(percent_change(100, 150), "expected 50.0")
```

1. **Reproduce:** `percent_change(100, 150)` should be 50.0.
2. **Compare:** it gives 33.3, which is 50 out of 150, not 50 out of 100.
3. **Narrow it down:** print each piece.

```python {.marimo}
_old = 100
_new = 150
_change = _new - _old
print(f"{_change=}, {_change / _new=}, {_change / _old=}")
```

4. **Fix it, then add a test:** divide by `old`, and keep the tests.

```python {.marimo}
def percent_change_fixed(old: float, new: float) -> float:
    change = new - old
    return change / old * 100


assert percent_change_fixed(100, 150) == 50
assert percent_change_fixed(80, 60) == -25
print("tests pass")
```

### `breakpoint()`

Put `breakpoint()` on a line of a `.py` file and run it. Python pauses there. Type a variable's name to see its value, `n` to run the next line, `c` to continue, and `q` to quit. (It doesn't work inside these notes.)

### Common bug: clean code can still be wrong

```python {.marimo}
def is_adult(age: int) -> bool:
    """True for anyone 18 or older."""
    return age > 18


print(is_adult(30), is_adult(18))
```

ruff and ty are both happy with this function. Only a test at the boundary, 18, finds the bug.

## 7. Debugging with AI, the right way

| Weak prompt | Strong prompt |
|---|---|
| "fix my code" | "Here's my function, the input, what I expected, and what happened. Explain what's wrong without rewriting it." |
| pasting 200 lines | the smallest piece of code that reproduces the bug |

Give the AI three things: the code, the full traceback (or the input and the wrong output), and what you expected. Then ask it to explain, not to fix:

```text
percent_change(old, new) should give the percent change from old to new.
percent_change(100, 150) returns 33.33, but I expected 50.0. Here is the code: ...
Explain what's wrong, but don't rewrite the function.
```

## AI activity: write your first skill

A **skill** is a folder with a `SKILL.md` file: a short name, a description of when to use it, and instructions. Your AI reads every skill's description and loads the full instructions only when a task matches. The format is an open standard, so the same file works in Copilot, OpenCode, Codex, and Claude Code. Look at `.github/skills/explain-error/SKILL.md` for an example.

Write a skill that reviews code for readability without rewriting it:

1. Create `.agents/skills/readability-review/SKILL.md`:

   ```markdown
   ---
   name: readability-review
   description: Reviews Python code for readability (names, comments, long functions) without rewriting it. Use when a student asks for a code review or asks whether their code is clear.
   ---

   # Readability review

   1. Run `uv run ruff check` and `uv run ty check` on the file and report what they find.
   2. Point out at most three readability problems: unclear names, missing type hints, or functions doing too much.
   3. For each one, explain why it hurts readability. Don't rewrite the code; the student fixes it.
   ```

2. Copy the folder to `.github/skills/readability-review/`. OpenCode reads `.agents/skills/` and Copilot reads `.github/skills/`, so keep the two copies the same.
3. Check the format: `uv run pytest lectures/08-code-quality`. The name must be lowercase with hyphens and match the folder name.
4. In Copilot Chat, ask: *"Review hw03.py for readability."* Did it use your skill? Compare its suggestions with what ruff and ty found on their own.
5. Change one instruction (for example, "at most two problems") and ask again. The answer should change.

## Exercises (40 minutes)

Open `l08_exercises.py` and run `uv run pytest lectures/08-code-quality` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `absolute`, `ticket_price` |
| Core | `is_valid_ticker`, `next_business_day`, `grade_points`, `parking_fee` |
| Fix the AI's code | `with_tax` |
| Stretch | `minutes_late` |

Use clear names and named constants as you go, then run `uv run ruff check` and `uv run ty check` on your file.
