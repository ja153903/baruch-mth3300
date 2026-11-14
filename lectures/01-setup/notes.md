---
title: "L01: Setup and your first program"
marimo-version: "0.25.2"
---

# L01: Setup and your first program

**By the end of this lecture you can:**

- move around folders in the terminal
- install Python with uv and run a program
- use the Python REPL as a calculator, and predict the order of operations
- give values names with variables, and join text with `+`
- save your work with git
- read the last line of an error message, and ask an AI to explain it

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. The terminal

The terminal is a text window where you type commands instead of clicking. In VS Code, open it with **View → Terminal**. On macOS you can also use the Terminal app; on Windows, PowerShell.

The terminal is always "in" one folder, called the **current directory**. Commands act on that folder.

```sh
pwd                 # print the current directory
ls                  # list the files here
mkdir mth3300       # make a new folder
cd mth3300          # move into it
cd ..               # move up one folder
```

These work on macOS, Linux, and PowerShell. Press **Tab** to autocomplete a file name and **↑** to repeat the last command.

**Try it:** make a folder for this course, `cd` into it, and run `pwd`. You'll save `hello.py` here in section 4.

## 2. Install uv

uv installs Python and every library this course needs. You never install Python by hand.

```sh
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then check that it works:

```sh
uv --version
uv run python --version   # downloads Python 3.15 the first time
```

## 3. The REPL

`uv run python` starts the **REPL** (Read–Eval–Print Loop). You type an expression and Python prints its value. Type `exit` to leave.

The `>>>` at the start of a line is the REPL's **prompt**: Python is waiting for you to type. Don't type the `>>>` yourself.

```text
>>> 2 + 3
5
>>> 7 / 2
3.5
```

These notes are a marimo notebook. Each gray box is a **cell** of Python code. Press its run button and the output appears below it. In a cell, `print` shows a value, like the REPL does.

**Predict:** what does each line below print?

```python {.marimo}
print(2 + 3 * 4)
print((2 + 3) * 4)
print(7 / 2)
```

### Arithmetic

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+`, `-` | add, subtract | `10 - 4` | `6` |
| `*` | multiply | `6 * 7` | `42` |
| `/` | divide | `7 / 2` | `3.5` |
| `**` | power | `2 ** 10` | `1024` |

`/` always gives a number with a decimal point, even when it divides evenly: `6 / 3` is `2.0`. Raising to the power `0.5` takes a square root.

### Order of operations

Python uses the order from math class: parentheses first, then `**`, then `*` and `/`, then `+` and `-`. Operators at the same level go left to right.

**Predict** each line before you run it:

```python {.marimo}
print(2 * 3**2)
print((2 * 3) ** 2)
print(10 - 4 - 3)
print(9**0.5)
```

### A finance example: growing money

$1,000 that earns 5% a year is multiplied by 1.05 each year. After 10 years, it has been multiplied by 1.05 ten times:

```python {.marimo}
print(1000 * 1.05**10)
```

### Common bug: missing parentheses

Someone writes the growth factor as `1 + 0.05` instead of `1.05`. **Predict** both lines:

```python {.marimo}
print(1000 * 1 + 0.05**10)
print(1000 * (1 + 0.05) ** 10)
```

In the first line, `**` goes first, so only `0.05` is raised to the 10th power. When you aren't sure what Python does first, add parentheses.

## 4. Your first program

A program is a file of instructions that Python runs from top to bottom. Save this as `hello.py` in your course folder, then run `uv run python hello.py`.

```python {.marimo}
course = "MTH 3300"
print("Hello,", course)
print("Python can do arithmetic:", 2**10)
```

- `print` can show several values at once. Separate them with commas, and it puts a space between them.
- A line that starts with `#` is a **comment**. Python skips it. Comments are notes for people.
- In a program, only `print` shows anything. A line like `2 + 3` computes 5 and throws it away. (The REPL is different: it prints every value for you.)

**Predict:** how many lines does this print, and what are they?

```python {.marimo}
# A receipt. Python skips this line.
print("Coffee", 4.5)
print("Bagel", 3.25)
2 + 2
print("Total", 4.5 + 3.25)
```

## 5. Variables: names for values

A **variable** is a name for a value. `=` stores the value on the right under the name on the left. After that, you can use the name anywhere you'd use the value.

```python {.marimo}
rent = 1450
groceries = 400
metrocard = 132
monthly_total = rent + groceries + metrocard
print("Per month:", monthly_total)
print("Per year:", monthly_total * 12)
```

Names can use letters, digits, and underscores, but can't start with a digit. Use lowercase words joined by underscores, like `monthly_total`, so the name says what the value is.

Some cells use names that start with an underscore, like `_price`. That's a marimo convention for a name used in only one cell. In your own `.py` files, just write `price`.

**Predict:**

```python {.marimo}
_price = 20
_quantity = 3
print(_price * _quantity, _price + _quantity)
```

## 6. Text: strings

Text in quotes is a **string**. Single and double quotes both work: `'hi'` and `"hi"` are the same string. `+` joins two strings into one.

**Predict:**

```python {.marimo}
print("3" + "4")
print(3 + 4)
print("ha" + "ha" + "ha")
```

`+` means one thing for numbers and another for text. The quotes decide which one you get.

### Common bug: forgetting the space

`+` joins strings exactly as they are. It never adds a space for you:

```python {.marimo}
school = "Baruch"
print(school + "College")
print(school + " College")
```

## 7. Saving your work with git

git records snapshots of your files. You'll use four commands all semester:

```sh
git clone <url>          # copy your fork of the course to your computer (once)
git add hw01.py          # choose what goes into the snapshot
git commit -m "Finish task 1"
git push                 # upload it; this is how you submit
```

A **commit** is a snapshot plus a message that says what changed. Commit whenever something works, so you can always get back to it. Write messages that say what you did, like "Finish task 2", not "stuff".

To check what you've changed since your last commit, run:

```sh
git status
```

## 8. When things go wrong

Errors are normal. Python tells you **where** the error happened and **what kind** it is. Read the *last line* first.

```python {.marimo}
try:
    print("Total: " + 5)
except TypeError as err:
    print("TypeError:", err)
```

(`try` and `except` let these notes show an error without stopping. You'll learn how they work in L16.)

`+` can't join a string and a number. For now, print them with a comma instead: `print("Total:", 5)`.

Here are the last lines of two more errors you'll see this week:

```text
NameError: name 'cuorse' is not defined. Did you mean: 'course'?
SyntaxError: '(' was never closed
```

- A **NameError** means Python doesn't know that name. Usually it's a typo, or a variable you haven't created yet.
- A **SyntaxError** means Python couldn't read the line at all, often because of a missing `)` or quote. Python doesn't run any of the file until you fix it.

## AI activity: your first conversation

Your AI reads instructions before it answers you. Open `AGENTS.md` at the top of your course folder. It's plain text that every coding AI reads: Copilot, OpenCode, Codex, and Claude Code all pick it up. It tells your AI to act as a tutor on homework 1–9.

1. Open Copilot Chat in VS Code and pick **Ask** mode. Ask it: *"What instructions are you following in this folder?"* Does its answer match `AGENTS.md`?
2. In the REPL, run `print("Total: " + 5)` and copy the full error.
3. Paste the error into Copilot Chat and ask: *"Explain this error."* The course comes with a **skill** called `explain-error` (in `.github/skills/`) that tells the AI how to explain errors without fixing your code. Watch for it in the answer.
4. Fix the code yourself. Write one sentence in your own words about what went wrong.

You'll write your own skills starting in L08.

## Exercises (40 minutes)

Open `l01_exercises.py`. Replace each `None` with an expression, and run `uv run pytest lectures/01-setup` as you go. Do them in order:

| Group | Variables |
|---|---|
| Warmup | `greeting`, `minutes_in_a_day` |
| Core | `file_path`, `total_with_tax`, `percent_change`, `grains_on_last_square` |
| Fix the AI's code | `midpoint` |
| Stretch | `larger_root`, `monthly_balance` |
