# Homework 09: Files and errors

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw09.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

Implement each function in `hw09.py`:

1. `count_lines(path)`: the number of lines in a text file. Open it with `with`.
2. `column_total(path, column)`: the sum of one numeric column in a CSV file with a header row. Use `csv.DictReader`.
3. `safe_divide(a, b)`: `a / b`, or `None` if `b` is zero. Use `try`/`except`; don't check `b == 0`.

**Try it:** the tests create temporary files with pytest's `tmp_path`. Read `test_hw09.py` to see how.

**AI exercise:** once all tests pass, predict what your `column_total` does if a cell in the column is blank, and if the column name doesn't exist. Then ask an AI what your function does in those two cases, and test both on a small CSV file of your own. In `AI_LOG.md`, record your prediction, the AI's answer, and what actually happened.

## Check your work

```sh
uv run pytest
```
