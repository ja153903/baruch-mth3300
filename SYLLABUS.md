# MTH 3300 Syllabus: Programming in Python

> Draft. TODO before publishing: instructor and contact info, meeting times, and Baruch's required statements (academic integrity, accessibility, attendance).

## Course design

1. **Students learn to code by writing code, and learn to use AI by using it on purpose.** Every assignment states which AI tier applies.
2. **Grades come mostly from in-person work.** Homework is practice with a light weight. Exams, live coding, and project defenses carry most of the grade.
3. **Tests decide whether code works.** Every homework comes with pytest tests, whoever wrote the code.
4. **Modern tools from day one:** Python 3.15, uv, ruff, ty, pytest, and git.

## AI policy

| Tier | Meaning | Used for |
|---|---|---|
| **No AI** | Closed book, in person | Quizzes, midterm, final exam, live coding |
| **AI as tutor** | AI may explain and give hints, but may not write the solution | Homework 1–9 |
| **AI as pair programmer** | AI may write code, but you must understand and defend every line | Homework 10–13, final project |

- **Log your AI use.** For every homework, record your AI sessions in `AI_LOG.md`: what you asked, and what you changed afterwards. Logged AI use is never penalized. Unlogged use is an academic integrity issue.
- **Free tools only.** Nothing in this course requires a paid AI subscription.
- **Each assignment folder has AI instructions.** The `AGENTS.md` and `CLAUDE.md` files tell AI coding tools how to help at that assignment's tier.

## Schedule

There are 23 lectures over 14 weeks, with two meetings a week. The other five meetings are the midterm, two project workshops, and two demo days.

| Wk | Lectures | Modern Python / tooling | Homework assigned | AI tier |
|---|---|---|---|---|
| 1 | **L1** Setup and your first program · **L2** Values, types, expressions | uv, the 3.15 REPL, git | `01-basics` | Tutor |
| 2 | **L3** Strings · **L4** Formatting, input/output, reading tracebacks | f-strings, `f"{x=}"` | `02-strings` | Tutor |
| 3 | **L5** Functions · **L6** Type hints and tests | `def`, pytest | `03-functions` | Tutor |
| 4 | **L7** Booleans and conditionals · **L8** Code quality | ruff, ty | `04-conditionals` | Tutor |
| 5 | **L9** `while` loops · **L10** `for` loops and accumulation | `range`, `enumerate` | `05-loops` | Tutor |
| 6 | **L11** Lists and slicing · **L12** Tuples and comprehensions | `zip(strict=True)` | `06-lists` | Tutor |
| 7 | **L13** Dicts · **L14** Sets, counting, midterm review | `collections.Counter` | `07-dicts` | Tutor |
| 8 | **Midterm** · **L15** Files and paths | `pathlib`, `with` | | No AI (midterm) |
| 9 | **L16** Exceptions and CSV · **L17** Recursion | `try`/`except`, `csv` | `09-files` | Tutor |
| 10 | **L18** Searching and sorting · **L19** Big-O and profiling | `profiling.sampling` | `10-algorithms` | Pair programmer |
| 11 | **L20** Dataclasses · **L21** Pattern matching and modeling | `@dataclass`, `match` | `11-dataclasses` | Pair programmer |
| 12 | **L22** Numbers you can trust · **L23** NumPy and plotting | `decimal`, `fractions`, `random`, `uv add`, marimo | `12-numerics` | Pair programmer |
| 13 | Project workshop · Project workshop | | `13-numpy` | Pair programmer |
| 14 | Project demos and oral defenses · Project demos and oral defenses | | | Pair programmer |
| 15 | **Final exam** | | | No AI |

Homework is due the week after it's assigned. Each one has an AI exercise as well as the coding tasks, which build up how students work with AI:

- **Weeks 1–4, AI explains:** asking about errors, concepts, and wrong predictions.
- **Weeks 5–9, AI debugs and reviews:** trying first, then asking, and judging AI suggestions.
- **Weeks 10–13, AI pair-programs:** writing a spec, building with AI, measuring and verifying its claims.

## Grading

| Component | Weight | AI tier |
|---|---|---|
| Homework (12 assignments, autograded with pytest) | 20% | Tutor or pair programmer |
| In-class quizzes and live coding | 15% | No AI |
| Midterm | 20% | No AI |
| Final project, including the oral defense | 20% | Pair programmer |
| Final exam | 25% | No AI |

## Setup

Install [uv](https://docs.astral.sh/uv/). In any homework folder, `uv run pytest` installs Python 3.15 and everything else that's needed. Students never need to install Python by hand or activate a virtual environment.
