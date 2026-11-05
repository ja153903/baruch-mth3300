---
title: "L01: Setup and your first program"
marimo-version: "0.25.2"
---

# L01: Setup and your first program

**By the end of this lecture you can:**

- install Python with uv and run a program
- use the Python REPL as a calculator
- save your work with git
- ask an AI to explain an error message

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Install uv

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

## 2. The REPL

`uv run python` starts the **REPL** (Read–Eval–Print Loop). You type an expression and Python prints its value. Type `exit` to leave.

**Predict:** what does each line below print?

```python {.marimo}
print(2 + 3 * 4)
print((2 + 3) * 4)
print(7 / 2)
```

## 3. Your first program

A program is a file of instructions that Python runs from top to bottom. Save this as `hello.py`, then run `uv run python hello.py`.

```python {.marimo}
course = "MTH 3300"
print("Hello,", course)
print("Python can do arithmetic:", 2**10)
```

## 4. Saving your work with git

git records snapshots of your files. You'll use four commands all semester:

```sh
git clone <url>          # copy an assignment repo to your computer
git add hw01.py          # choose what goes into the snapshot
git commit -m "Finish task 1"
git push                 # upload it; this is how you submit
```

## 5. When things go wrong

Errors are normal. Python tells you **where** the error happened and **what kind** it is. Read the *last line* first.

```python {.marimo}
try:
    print("Total: " + 5)
except TypeError as err:
    print("TypeError:", err)
```

## AI activity: your first conversation

1. In the REPL, run `print("Total: " + 5)` and copy the full error.
2. Ask an AI: *"I'm a beginner. Explain this Python error in plain English, but don't fix my code: …"*
3. Fix it yourself. Write one sentence in your own words about what went wrong.

**Exercises:** open `l01_exercises.py`, then run `uv run pytest lectures/01-setup`.
