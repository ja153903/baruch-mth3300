---
title: "L10: Loop patterns and debugging"
marimo-version: "0.25.2"
---

# L10: Loop patterns and debugging

**By the end of this lecture you can:**

- recognize four loop patterns: count, add up, search, and best so far
- write and trace loops inside loops
- spot the most common loop bugs: returning too early and resetting inside the loop
- debug methodically: reproduce, compare, narrow down, then fix and test
- ask an AI about a bug in a way that helps you learn
- write your first skill, which tells your AI how to help you trace a loop

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L09)

**Predict** the output before you run it:

```python {.marimo}
_total = 0
for _k in range(1, 6):
    if _k % 2 == 1:
        _total += _k
print(_total)
```

## 1. Four loop patterns

Most loops you'll write in this course follow one of four patterns. Learn to spot them, and a new problem starts to look like an old one.

| Pattern | Start with | Inside the loop | Example |
|---|---|---|---|
| **count** | `count = 0` | `count += 1` when the item matches | how many vowels |
| **add up** | `total = 0` | `total += item` | the sum of the digits |
| **search** | nothing | `return` as soon as you find it | is there a space? |
| **best so far** | the first item, or a safe starting value | replace it when you see a better one | the largest digit |

Here are count and add up together:

```python {.marimo}
def vowels_and_digits(text: str) -> str:
    vowels = 0
    digit_total = 0
    for ch in text:
        if ch.lower() in "aeiou":
            vowels += 1
        if ch.isdigit():
            digit_total += int(ch)
    return f"{vowels} vowels, digits add up to {digit_total}"


print(vowels_and_digits("MTH 3300 at Baruch"))
```

### Search: stop as soon as you know

```python {.marimo}
def has_digit(text: str) -> bool:
    for ch in text:
        if ch.isdigit():
            return True
    return False


print(has_digit("Room 12"), has_digit("Lexington"))
```

`return True` happens the moment a digit turns up. `return False` sits **after** the loop, because you only know there's no digit once you've checked every character.

### Common bug: returning too early

**Predict:** what does this print?

```python {.marimo}
def has_digit_wrong(text: str) -> bool:
    for ch in text:
        if ch.isdigit():
            return True
        else:
            return False
    return False


print(has_digit_wrong("Room 12"), has_digit_wrong("12 Room"))
```

The `else: return False` runs on the very first character, so the loop never gets past it. Ask yourself: can I decide the answer **now**, or only after the whole loop?

### Best so far

Which order size gives the most profit? Each item sells for $12, and making `units` items costs `100 + units**2 / 4` dollars:

```python {.marimo}
def profit(units: int) -> float:
    return 12 * units - (100 + units**2 / 4)


best_units = 1
for _units in range(1, 51):
    if profit(_units) > profit(best_units):
        best_units = _units
print(best_units, profit(best_units))
```

Start "best" with a value that's really possible, here `1`. If you start the best profit at 0 and every profit is negative, the loop never finds anything better, and you get the wrong answer.

## 2. Loops inside loops

The inner loop runs all the way through for **each** step of the outer loop.

**Predict:** how many lines does this print, and what's on them?

```python {.marimo}
for _row in range(1, 4):
    for _col in range(1, 3):
        print(_row, _col)
```

3 steps of the outer loop × 2 steps of the inner loop = 6 lines.

### Tracing a nested loop

When you trace a nested loop by hand, give each loop variable its own column. The inner variable starts over every time the outer one moves:

| `_row` | `_col` | printed |
|---|---|---|
| 1 | 1 | `1 1` |
| 1 | 2 | `1 2` |
| 2 | 1 | `2 1` |
| 2 | 2 | `2 2` |
| 3 | 1 | `3 1` |
| 3 | 2 | `3 2` |

### Pairs: start the inner loop after the outer one

How many ways can you pick two different stocks from five? If the inner loop starts at `_a + 1`, each pair shows up once, and no stock gets paired with itself:

```python {.marimo}
_pairs = 0
for _a in range(1, 6):
    for _b in range(_a + 1, 6):
        _pairs += 1
print(_pairs, "and the formula 5 × 4 / 2 gives", 5 * 4 // 2)
```

**Predict:** what would `_pairs` be if the inner loop were `range(1, 6)` instead?

### Building a picture, one row at a time

```python {.marimo}
def triangle(n: int) -> str:
    rows = ""
    for row in range(1, n + 1):
        line = ""
        for _ in range(row):
            line += "*"
        rows += line + "\n"
    return rows


print(triangle(4))
```

### Common bug: resetting in the wrong place

`line = ""` sits **inside** the outer loop, so each row starts empty. **Predict:** what does this version print?

```python {.marimo}
def triangle_wrong(n: int) -> str:
    rows = ""
    line = ""
    for row in range(1, n + 1):
        for _ in range(row):
            line += "*"
        rows += line + "\n"
    return rows


print(triangle_wrong(4))
```

Line 1 has one star. Line 2 still has the old star, plus two more. Ask of every variable: should it start over each time, or keep building? That tells you which loop it belongs above.

## 3. Debugging methodically

Guessing and changing things at random makes bugs worse. Work through four steps instead:

1. **Reproduce it:** find the smallest input that shows the bug.
2. **Compare:** what did you *expect*, and what *actually* happened?
3. **Narrow it down:** put `print(f"{x=}")` inside the loop to watch the values change.
4. **Fix it, then add a test,** so the bug can never come back.

### A worked example

A classmate's `digit_sum` gives the wrong answer:

```python {.marimo}
def digit_sum(n: int) -> int:
    while n > 0:
        total = 0
        total += n % 10
        n = n // 10
    return total


print(digit_sum(3300), "expected 6")
```

1. **Reproduce:** `digit_sum(3300)` should be 6. Does a smaller input show it too? `digit_sum(12)` should be 3.
2. **Compare:** `digit_sum(3300)` gives 3, which is only the first digit.
3. **Narrow it down:** print the values on every pass.

```python {.marimo}
_n = 12
while _n > 0:
    _total = 0
    _total += _n % 10
    _n = _n // 10
    print(f"{_n=}, {_total=}")
```

`_total` never gets above one digit. It goes back to 0 on every pass, because `total = 0` is inside the loop.

4. **Fix it, then add a test:** move `total = 0` above the loop, and keep the tests.

```python {.marimo}
def digit_sum_fixed(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


assert digit_sum_fixed(3300) == 6
assert digit_sum_fixed(12) == 3
assert digit_sum_fixed(0) == 0
print("tests pass")
```

### `breakpoint()`

Put `breakpoint()` on a line of a `.py` file and run it. Python pauses there. Type a variable's name to see its value, `n` to run the next line, `c` to continue, and `q` to quit. (It doesn't work inside these notes.)

## 4. Debugging with AI, the right way

| Weak prompt | Strong prompt |
|---|---|
| "fix my code" | "Here's my function, the input, what I expected, and what happened. Explain what's wrong without rewriting it." |
| pasting 200 lines | the smallest piece of code that reproduces the bug |

Give the AI three things: the code, the full traceback (or the input and the wrong output), and what you expected. Then ask it to explain, not to fix:

```text
digit_sum(n) should add up the digits of n.
digit_sum(12) returns 1, but I expected 3. Here is the code: ...
Explain what's wrong, but don't rewrite the function.
```

## AI activity: write your first skill

A **skill** is a folder with a `SKILL.md` file: a short name, a description of when to use it, and instructions. Your AI reads every skill's description and loads the full instructions only when a task matches. The format is an open standard, so the same file works in Copilot, OpenCode, Codex, and Claude Code. Look at `.github/skills/explain-error/SKILL.md` for an example.

Write a skill that helps you trace a loop, instead of fixing it for you:

1. Create `.agents/skills/trace-loop/SKILL.md`:

   ```markdown
   ---
   name: trace-loop
   description: Helps a student trace a Python loop by hand, one row at a time, without fixing their code. Use when a student asks why a loop gives the wrong answer, runs forever, or is off by one.
   ---

   # Trace a loop

   1. Ask the student for one small input that shows the problem, if they haven't given one.
   2. Draw a trace table with one column per variable that changes in the loop. Fill in only the first row.
   3. Ask the student to fill in the next row. Check it, then ask for the next one.
   4. When the table shows where the values go wrong, ask the student which line caused it. Don't rewrite the code.
   ```

2. Copy the folder to `.github/skills/trace-loop/`. OpenCode reads `.agents/skills/` and Copilot reads `.github/skills/`, so keep the two copies the same.
3. Check the format: `uv run pytest lectures/10-loop-patterns`. The name must be lowercase with hyphens and match the folder name.
4. In Copilot Chat, paste in `triangle_wrong` from section 2 and ask: *"Why does this print too many stars?"* Did it use your skill?
5. Change one instruction (for example, "fill in the first two rows") and ask again. The answer should change.

## Exercises (40 minutes)

Open `l10_exercises.py` and run `uv run pytest lectures/10-loop-patterns` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `largest_digit`, `staircase` |
| Core | `count_pairs`, `times_table`, `has_repeat`, `count_primes` |
| Fix the AI's code | `all_even_digits` |
| Stretch | `longest_run`, `count_triples` |

When a test fails, trace the loop with a table before you change anything.
