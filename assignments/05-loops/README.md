# Homework 05: Loops

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw05.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

Implement each function in `hw05.py` with a loop. Don't use `math.factorial` or `**`.

1. `factorial(n)`: `n! = 1 × 2 × ... × n`, where `0! = 1`.
2. `collatz_steps(n)`: the number of steps to reach 1. At each step, if `n` is even, halve it; otherwise replace it with `3n + 1`.
3. `compound_balance(principal, rate, years)`: the account balance after `years` years of interest compounded once a year.

**Try on your own first.** Spend at least 15 minutes on a bug before you ask an AI about it. When you do ask, paste in your code and the full traceback, and log what you'd already tried.

## Check your work

```sh
uv run pytest
```
