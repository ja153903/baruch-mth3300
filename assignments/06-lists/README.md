# Homework 06: Lists

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw06.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

Implement each function in `hw06.py`. None of them may change the list passed in.

1. `running_total(xs)`: each element is the sum of everything up to and including that position.
2. `evens(xs)`: only the even numbers. Write this one as a list comprehension.
3. `moving_average(xs, k)`: the average of every window of `k` consecutive elements (hint: slicing). If `k` is bigger than the list, return `[]`.

**AI exercise:** once all tests pass, ask an AI to review your `hw06.py`. In `AI_LOG.md`, list each suggestion it made and whether you accepted it, with one sentence explaining why.

## Check your work

```sh
uv run pytest
```
