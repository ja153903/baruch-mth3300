# Oral defense question bank

7 minutes per student. Open their repo, and point at specific lines. The aim is to find out whether they **understand** their code, not whether they wrote every character of it.

## Always ask

1. Walk me through what happens, line by line, when I run `uv run python main.py` with this input.
2. Pick a test. What does it check, and what bug would make it fail?
3. Show me one AI suggestion you **rejected**. Why did you reject it?

## Point-at-a-line questions

- Why is this a `dict` (or `list`, `set`, dataclass) rather than something else?
- What happens if this list is empty? If this file doesn't exist? If this number is negative?
- What's the Big-O of this function? How would it handle 1,000,000 rows?
- What does this `except` catch, and what would happen without it?
- Why `Decimal` here, and not `float`? (or the other way round)
- Change this line so that it does *X*. (a small live change: run it, run the tests)

## Red flags (probe further)

- They can describe *what* a block of code does, but not *why* it's written that way
- They can't find where a feature lives in their own code
- Their spec, their code, and their tests disagree with one another, and they can't explain why

## Scoring (40 points; see `project/rubric.md`)

- **36–40:** fluent answers, including about changes they'd make
- **28–35:** solid, with gaps in one area
- **20–27:** understands the main flow but not the details
- **Below 20:** can't explain the core. **Cap the project total at 50.**
