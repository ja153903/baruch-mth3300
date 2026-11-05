# Homework 03: Functions

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw03.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

Implement each function in `hw03.py`:

1. `circle_area(r)`: return the area of a circle with radius `r`. Use `math.pi`.
2. `is_leap_year(year)`: return `True` if `year` is a leap year. A year is a leap year if it's divisible by 4, except years divisible by 100, unless they're also divisible by 400.
3. `digit_sum(n)`: return the sum of the digits of a non-negative integer `n`. For example, `digit_sum(3300) == 6`.

## Check your work

```sh
uv run pytest
```

All tests passing means you're done.
