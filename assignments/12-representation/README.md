# Homework 12: How data is represented

**AI policy: AI as pair programmer.** You may have an AI write code with you, but you must be able to explain every line; you'll be asked to in class. Record each AI session in `AI_LOG.md`.

## Warm-up

In the REPL (`uv run python`), run `0.1 + 0.2 == 0.3` and `float(2**53) == float(2**53 + 1)`. In `AI_LOG.md`, explain in your own words why each result is what it is.

## Tasks

Implement each function in `hw12.py`. Don't use `int(s, base)`, `bin()`, or `format()`: the point is to do the conversions yourself.

1. `from_base(digits, base)`: the value of a string of digits in a base from 2 to 16. The digits after 9 are `a` to `f`, in either case, so `from_base("ff", 16) == 255`. Raise `ValueError` for a digit that isn't valid in that base.
2. `to_twos_complement(n, bits)`: the `bits`-bit two's complement pattern of `n`, as a string of `0`s and `1`s, so `to_twos_complement(-1, 8) == "11111111"`. Raise `ValueError` if `n` doesn't fit in that many bits.
3. `caesar(text, shift)`: shift each letter `shift` places through the alphabet, wrapping from `z` back to `a`, and keep upper and lower case. Leave everything else unchanged. Use `ord` and `chr`.
4. `total_price(prices)`: the exact total of prices given as strings, like `"19.99"`. Use `Decimal`.

**Check the AI:** ask your AI for the 8-bit two's complement pattern of -100, and how it got it. Check its answer with your function, and by hand with the rule from L22. Log what you found.

## Check your work

```sh
uv run pytest
```
