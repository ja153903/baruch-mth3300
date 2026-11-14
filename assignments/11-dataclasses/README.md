# Homework 11: Classes and modeling

**AI policy: AI as pair programmer.** You may have an AI write code with you, but you must be able to explain every line; you'll be asked to in class. Record each AI session in `AI_LOG.md`.

## Tasks

Complete `hw11.py`:

1. **`Account`, written by hand (no `@dataclass`).**
   - `Account(owner, balance=0.0)` stores both values as attributes.
   - `deposit(amount)` and `withdraw(amount)` raise `ValueError` if the amount isn't positive, or if a withdrawal is more than the balance. A rejected transaction must leave the balance unchanged.
   - `repr(Account("Ada", 70))` is `Account('Ada', 70.00)`.
2. **`SavingsAccount`, a subclass of `Account`.**
   - `SavingsAccount(owner, balance=0.0, rate=0.02)` uses `super().__init__` for the owner and balance, and stores `rate`.
   - `add_interest()` adds `balance * rate` to the balance.
   - `withdraw` allows at most 3 withdrawals; the 4th raises `ValueError`. It must still follow every `Account` rule, so call `super().withdraw`. A rejected withdrawal doesn't count toward the 3.
3. **`Point`, a frozen dataclass.**
   - `distance_to(other)` is the straight-line distance between two points.
   - `moved(dx, dy)` returns a *new* point shifted by `dx` and `dy`. Use `copy.replace`.
4. **`area(shape)`.** Use `match` on the `Circle`, `Rectangle`, and `Triangle` dataclasses. Raise `ValueError` for anything else.

**Spec first.** Before you open an AI chat, write 3–5 sentences in `AI_LOG.md` describing how `SavingsAccount` should behave, including what happens when a withdrawal is rejected. Give your AI that spec. Then note anywhere its code didn't match your spec.

**Notice:**
- `other: Point` works inside the `Point` class without quotes. Since Python 3.14, annotations aren't evaluated until they're needed.
- `type Shape = Circle | Rectangle | Triangle` gives the union a name (L21).

## Check your work

```sh
uv run pytest
```
