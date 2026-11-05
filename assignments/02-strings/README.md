# Homework 02: Strings

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw02.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

In `hw02.py`, replace each `None` with an expression built from the variables above it:

1. `title_name` and `initials` from `name`
2. `email_domain` from `email` (hint: `.split()` or `.index()` with slicing)
3. `receipt`: use an f-string that formats `price` and the total to two decimal places

**Debugging tip:** `print(f"{receipt=}")` prints both the variable's name and its value.

**AI exercise:** ask an AI why `"3" + 4` raises an error but `"3" * 4` doesn't. Then write one sentence, in your own words, in `AI_LOG.md`.

## Check your work

```sh
uv run pytest
```
