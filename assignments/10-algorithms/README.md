# Homework 10: Algorithms

**AI policy: AI as pair programmer.** You may have an AI write code with you, but you must be able to explain every line; you'll be asked to in class. Record each AI session in `AI_LOG.md`.

## Tasks

Implement each function in `hw10.py`:

1. `binary_search(xs, target)`: the index of `target` in the sorted list `xs`, or `-1` if it's not there. It must run in O(log n): no `in`, `.index()`, or scanning the whole list.
2. `merge_sort(xs)`: a new sorted list, built recursively. Don't change `xs` or call `sorted`.
3. `fib(n)`: the nth Fibonacci number, where `fib(0) == 0` and `fib(1) == 1`.

## Measure, don't guess

1. Write `fib` recursively in the simplest way you can, then profile it:
   ```sh
   uv run python -m profiling.sampling run hw10.py
   ```
2. Ask your AI how to make it faster. Before you accept the suggestion, predict how much faster it will be.
3. Profile it again. In `AI_LOG.md`, compare what you predicted with what you measured.

## Check your work

```sh
uv run pytest
```
