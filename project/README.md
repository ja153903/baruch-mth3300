# Final project

**Weight:** 20% of your grade · **AI policy: AI as pair programmer** · **Work alone**

You'll build a small but real Python program, using AI as a pair programmer, and then **defend it orally**: you'll explain any line of your code we point to. The defense is where most of the grade comes from.

## Timeline

| When | Milestone | What you submit |
|---|---|---|
| Week 12 (L23) | Choose an idea | A one-paragraph proposal: which option, and what it will do |
| Week 13, workshop 1 | Spec | `SPEC.md`: inputs, outputs, 3–5 example cases, and what's out of scope |
| Week 13, workshop 2 | Working core | The main feature works, with at least 5 passing tests |
| Week 14 | Demo and defense | The final repo, a 3-minute demo, and a 7-minute oral defense |

## Requirements

Your repo must have:

- [ ] a `pyproject.toml` and `uv.lock`, so that `uv run` works on a fresh clone
- [ ] at least one `@dataclass`
- [ ] at least 10 meaningful pytest tests, all passing with `uv run pytest`
- [ ] no problems reported by `uv run ruff check` or `uv run ty check`
- [ ] a `README.md` explaining what it does and how to run it
- [ ] a `SPEC.md`, written **before** you wrote any code
- [ ] an `AI_LOG.md` with your significant AI sessions: what you asked, what you accepted, and what you rejected and why

## Options

Pick one from [`options.md`](options.md), or propose your own in week 12. Your own idea needs approval.

## Grading

See [`rubric.md`](rubric.md).
