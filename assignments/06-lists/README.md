# Homework 06: Testing a trading rule

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw06.py` or fill in `SIGNAL_CASES`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

You'll build a small program that tests a real trading rule, the moving-average crossover, on a made-up stock. Then you'll decide whether you'd trust it. Each part builds on the one before, so start early and work in order. Your commit history shows the order.

None of your functions may change a list passed in.

## Part 1: building blocks

Implement `running_total`, `moving_average`, and `daily_changes` in `hw06.py`. Commit.

## Part 2: the rule, tests first

1. **Tests first.** Read the docstring for `signals`. Before you implement it, fill in `SIGNAL_CASES` with at least 5 cases worked out by hand. Include a case with no signals, one with both a buy and a sell, one with `short` bigger than 1, one with at least three signals, and one where the two averages are equal on the day before a signal. One case can cover more than one of these. Commit.
2. **Build.** Implement `signals`, then `backtest`, then `best_windows`. Reuse your earlier functions instead of repeating their logic: `best_windows` should call both `signals` and `backtest`.
3. **Run.** `uv run pytest`. Besides checking your functions, the tests run **buggy versions** of `signals`, and check that at least one of your `SIGNAL_CASES` catches each one. If a buggy version gets through, add a case that catches it. Commit.

## Part 3: a change request

Your client now wants a trading fee. Change `backtest` so that `fee` works:

- Each buy or sell that actually happens costs `fee`. Ignored trades cost nothing.
- A buy spends `fee` first, then puts the rest of the cash into shares. If your cash is less than or equal to `fee`, skip the buy.
- A sell gives you the sale amount minus `fee`.

**The spec has a gap:** it doesn't say what happens if the sale amount is smaller than `fee`. Decide what your code should do, and explain your rule and your reason in a comment. The tests don't check this. Commit.

## Part 4: would you trust it?

In the REPL (`uv run python`), find the best windows on the first 60 days, then try them on the 30 days after that:

```python
from hw06 import PRICES, backtest, best_windows, signals

early = PRICES[:60]
later = PRICES[60:]
best_windows(early, [2, 3, 5], [8, 10, 15], 1000)
```

Under a heading `## Analysis` in `AI_LOG.md`, record:

1. The best windows on `early`, and their final value. Compare that with buying on day 0 and holding: `backtest(early, [(0, "buy")], 1000)`.
2. How the **same windows** do on `later`, compared with buying and holding on `later`.
3. How the results on `later` change with `fee=2`.
4. In 3–5 sentences of your own: would you trade this rule with real money? Use your numbers.

**AI exercise:** once all tests pass, ask an AI to review `signals` and to critique your answer to question 4. In `AI_LOG.md`, list each point it made and whether you accepted it, with one sentence explaining why. Pick one factual claim it made about your code and check it by running the code.

## Check your work

```sh
uv run pytest
```

All tests passing means your code works. It doesn't mean you're done: parts 3 and 4 include writing that the tests can't check.
