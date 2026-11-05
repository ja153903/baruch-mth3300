# Homework 13: Tests first, then build with AI

**AI policy: AI as pair programmer.** You may have an AI write code with you, but you must be able to explain every line; you'll be asked to in class. Record each AI session in `AI_LOG.md`.

This homework practices the loop from L23: **spec, tests, generate, review.** The tests you write are graded on whether they catch bugs.

## Tasks

Work in this order. Your commit history shows the order, and you'll be asked about it.

1. **Tests first.** Read the specs in `hw13.py`. Before writing any implementation, fill in `TEST_CASES` with at least 8 `(number, numeral)` pairs, worked out by hand. Choose them to cover every rule. Commit.
2. **Build.** Implement `to_roman` and `from_roman`, with or without AI. Review the code with the checklist from L23.
3. **Run.** `uv run pytest`. Besides checking your functions, the tests run a set of **buggy versions** of `to_roman`, and check that at least one of your `TEST_CASES` catches each one. If a buggy version gets through, add a case that catches it, and work out what the bug must be.

**AI exercise:** ask an AI to suggest 8 test cases for `to_roman`, *without* showing it your own. Put its cases in `TEST_CASES` instead of yours and run the tests. Which buggy versions got past the AI's cases? Log what you found, then go back to your own cases (or the best of both).

## Check your work

```sh
uv run pytest
```
