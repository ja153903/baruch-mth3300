# Homework 13: NumPy

**AI policy: AI as pair programmer.** You may have an AI write code with you, but you must be able to explain every line; you'll be asked to in class. Record each AI session in `AI_LOG.md`.

## Tasks

Implement each function in `hw13.py` with no Python loops: use NumPy operations on whole arrays.

1. `daily_returns(prices)`: the percentage change from each day to the next, as a decimal. For example, `[100, 110]` gives `[0.10]`.
2. `zscore(a)`: shift and scale `a` so that it has mean 0 and standard deviation 1.
3. `portfolio_return(weights, returns)`: the weighted sum of the returns, as a Python `float`.

## Optional: plot it

```sh
uv add matplotlib
```

Plot `daily_returns` for a stock price series you make up. Ask your AI to help you label the axes.

## Check your work

```sh
uv run pytest
```
