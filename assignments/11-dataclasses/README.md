# Homework 11: Modeling data

**AI policy: AI as pair programmer.** You may have an AI write code with you, but you must be able to explain every line; you'll be asked to in class. Record each AI session in `AI_LOG.md`.

## Tasks

Complete `hw11.py`:

1. `Point.distance_to(other)`: the straight-line distance between two points.
2. `Account.deposit(amount)` and `Account.withdraw(amount)`: raise `ValueError` if the amount isn't positive, or if a withdrawal is more than the balance. A rejected transaction must leave the balance unchanged.
3. `area(shape)`: use `match` on tuples like `("circle", r)`, `("rectangle", w, h)` and `("triangle", base, height)`. Raise `ValueError` for any other shape.

**Spec first.** Before you open an AI chat, write 3–5 sentences in `AI_LOG.md` describing how `Account` should behave. Give your AI that spec. Then note anywhere its code didn't match your spec.

**Notice:** `other: Point` works inside the `Point` class without quotes. Since Python 3.14, annotations aren't evaluated until they're needed.

## Check your work

```sh
uv run pytest
```
