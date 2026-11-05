# Homework 01: Values and expressions

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw01.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Setup

1. Install [uv](https://docs.astral.sh/uv/).
2. In this folder, run `uv run pytest`. The first run installs Python 3.15 and pytest for you. Every test should fail, because you haven't written anything yet.

## Tasks

Open `hw01.py` and replace each `None` with an expression that computes the answer:

1. `seconds_in_a_week`
2. `average_score`: the average of `score1`, `score2`, and `score3`
3. `hypotenuse`: of a right triangle with legs 3 and 4
4. `full_boxes` and `leftover_eggs`: 100 eggs packed in boxes of 12

**Try it:** start the REPL with `uv run python`, and test each expression there before you put it in the file.

**AI exercise:** before you run `7 // 2`, `-7 // 2`, and `7 % -2`, write down what you predict they'll print. Then run them, and ask an AI to explain any you got wrong. Log it.

## Check your work

```sh
uv run pytest
```
