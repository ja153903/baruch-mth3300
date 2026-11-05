# Homework 07: Dicts and sets

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw07.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

Implement each function in `hw07.py`:

1. `word_counts(text)`: how many times each word appears. Ignore case, and split on whitespace.
2. `unique_sorted(xs)`: the distinct values, smallest first (hint: a set).
3. `group_by_value(d)`: map each value to the list of keys that had it, in their original order.

## Find the bug

`most_common_word` was written by an AI, and it has a bug. Steps:

1. Read the function and predict what it returns for `"b a a"`.
2. Add a test to `test_hw07.py` that fails because of the bug.
3. Fix the function.
4. In `AI_LOG.md`, explain the bug in one or two sentences.

## Check your work

```sh
uv run pytest
```
