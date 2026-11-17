# Homework 03: Functions

**AI policy: AI as tutor.** You may ask an AI to explain concepts, error messages, and hints. You may not have it write the code in `hw03.py`. Record each AI conversation in `AI_LOG.md`: what you asked, and what you changed afterwards.

## Tasks

Implement each function in `hw03.py`:

1. `circle_area(r)`: return the area of a circle with radius `r`. Use `math.pi`.
2. `split_bill(total, people, tip_rate=0.18)`: return what each person pays when `people` split `total` plus a tip, rounded to cents. For example, `split_bill(100, 4) == 29.5`, and `split_bill(100, 4, tip_rate=0.2) == 30.0`.
3. `sum_of_three_digits(n)`: return the sum of the digits of a three-digit number. For example, `sum_of_three_digits(472) == 13`. Hint: `//` and `%` from L02.

**AI exercise:** before you run this code, write down exactly what you predict it will print:

```python
def double(x):
    print(x * 2)


result = double(4)
print(result)
```

Then run it, and ask an AI to explain anything you got wrong. In `AI_LOG.md`, write one sentence, in your own words, about the difference between `print` and `return`.

## Check your work

```sh
uv run pytest
```

All tests passing means you're done.
