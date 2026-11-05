# Homework 12: Numbers you can trust

**AI policy: AI as pair programmer.** You may have an AI write code with you, but you must be able to explain every line; you'll be asked to in class. Record each AI session in `AI_LOG.md`.

## Warm-up

In the REPL (`uv run python`), run `0.1 + 0.2 == 0.3`. In `AI_LOG.md`, explain in your own words why the result is `False`, and why that matters for money.

## Tasks

Implement each function in `hw12.py`:

1. `total_price(prices)`: the exact total of prices given as strings, like `"19.99"`. Use `Decimal`.
2. `harmonic(n)`: `1 + 1/2 + ... + 1/n` as an exact `Fraction`.
3. `estimate_pi(samples, seed)`: estimate π with a Monte Carlo simulation. Pick random points in the unit square, and count the fraction that land inside the quarter circle. Use `random.Random(seed)` so that the same seed always gives the same answer.

**Check the AI:** ask your AI how accurate `estimate_pi(100_000)` should be. Then run it with 10 different seeds and see whether its answer holds up.

## Check your work

```sh
uv run pytest
```
