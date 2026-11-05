# Homework 04: Conditionals

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw04.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

Implement each function in `hw04.py`:

1. `letter_grade(score)`: `"A"` for 90 and up, `"B"` for 80 and up, `"C"` for 70 and up, `"D"` for 60 and up, otherwise `"F"`.
2. `sign(x)`: `-1`, `0`, or `1`.
3. `is_triangle(a, b, c)`: `True` if three side lengths make a real triangle. That means every side is positive, and every pair of sides adds up to more than the third.

## Code quality

Run these and fix what they report:

```sh
uv run ruff check
uv run ty check
```

**AI exercise:** break a type hint on purpose, for example by returning `"A"` from `sign`. Run `ty check`, then ask an AI to explain the error message in plain English.

## Check your work

```sh
uv run pytest
```
