# MTH 3300 Syllabus: Programming in Python

> Draft. TODO before publishing: instructor and contact info, meeting times, and Baruch's required statements (academic integrity, accessibility, attendance).

## Course design

1. **Students learn to code by writing code, and learn to use AI by using it on purpose.** Every assignment states which AI tier applies.
2. **Grades come mostly from in-person work.** Homework is practice with a light weight. Quizzes, exams, and project defenses carry most of the grade.
3. **Tests decide whether code works.** Every homework comes with pytest tests, whoever wrote the code.
4. **Modern tools from day one:** Python 3.15, uv, ruff, ty, pytest, and git.

## AI policy

| Tier | Meaning | Used for |
|---|---|---|
| **No AI** | Closed book, in person | Quizzes, midterm, final exam |
| **AI as tutor** | AI may explain and give hints, but may not write the solution | Homework 1–9 |
| **AI as pair programmer** | AI may write code, but you must understand and defend every line | Homework 10–13, AI build session, final project |

- **Log your AI use.** For every homework, record your AI sessions in `AI_LOG.md`: what you asked, and what you changed afterwards. Logged AI use is never penalized. Unlogged use is an academic integrity issue.
- **Possible sanctions.** Using AI beyond what a tier allows, or not logging it, is handled under the CUNY Policy on Academic Integrity. Possible sanctions include a zero on the work, a lower course grade, and a report to the college's academic integrity officer.
- **Free tools only.** Nothing in this course requires a paid AI subscription. GitHub Copilot in VS Code, free through the GitHub Student Developer Pack, is the course default. OpenCode's free models are the backup, and CUNY Copilot is the option for anything private. See [`docs/using-ai.md`](docs/using-ai.md).
- **Each assignment folder has AI instructions.** The `AGENTS.md` and `CLAUDE.md` files tell AI coding tools how to help at that assignment's tier.

## Schedule

There are 23 lectures over 14 weeks, with two meetings a week. The other five meetings are the midterm, two project workshops, and two demo days.

Each lecture meeting is about an hour of lecture, followed by about 40 minutes of programming on that lecture's exercises.

| Wk | Meeting | Modern Python / tooling | Homework assigned | AI tier |
|---|---|---|---|---|
| 1 | **L1** Setup and your first program | uv, the 3.15 REPL, git | `01-basics` | Tutor |
| 1 | **L2** Values, types, expressions | | | Tutor |
| 2 | **L3** Strings | | `02-strings` | Tutor |
| 2 | **L4** Formatting, input/output, reading tracebacks | f-strings, `f"{x=}"`, "Did you mean" errors | | Tutor |
| 3 | **L5** Functions | `def` | `03-functions` | Tutor |
| 3 | **L6** Type hints and tests | pytest | | Tutor |
| 4 | **L7** Booleans and conditionals | | `04-conditionals` | Tutor |
| 4 | **L8** `while` loops | | | Tutor |
| 5 | **L9** `for` loops and accumulation | `range`, `enumerate`, `random` | `05-loops` | Tutor |
| 5 | **L10** Loop patterns and debugging | `breakpoint()` | | Tutor |
| 6 | **L11** Lists and slicing | | `06-lists` | Tutor |
| 6 | **L12** Tuples and comprehensions | `zip(strict=True)`, `pairwise`, `batched`, ruff | | Tutor |
| 7 | **L13** Dicts | `frozendict` | `07-dicts` | Tutor |
| 7 | **L14** Sets, counting, midterm review | `collections.Counter` | | Tutor |
| 8 | **Midterm** | | | No AI |
| 8 | **L15** Files and paths | `pathlib`, `with`, UTF-8 by default | | Tutor |
| 9 | **L16** Exceptions and CSV | `try`/`except`, `except A, B`, `csv` | `09-files` | Tutor |
| 9 | **L17** Recursion | | | Tutor |
| 10 | **L18** Searching and sorting | | `10-algorithms` | Pair programmer |
| 10 | **L19** Big-O and profiling | `profiling.tracing`, `profiling.sampling` | | Pair programmer |
| 11 | **L20** Classes and objects | `class`, `@dataclass`, `copy.replace`, `@override` | `11-dataclasses` | Pair programmer |
| 11 | **L21** Modern Python | `match`, `StrEnum`, `type` aliases, t-strings | | Pair programmer |
| 12 | **L22** How data is represented | `ord`/`chr`, UTF-8, `decimal` | `12-representation` | Pair programmer |
| 12 | **L23** Building with AI | | | Pair programmer |
| 13 | Project workshop + AI build session | | `13-testing` | Pair programmer |
| 13 | Project workshop | | | Pair programmer |
| 14 | Project demos and oral defenses | | | Pair programmer |
| 14 | Project demos and oral defenses | | | Pair programmer |
| 15 | **Final exam** | | | No AI |

Homework is due the week after it's assigned. Each one has an AI exercise as well as the coding tasks, which build up how students work with AI:

- **Weeks 1–4, AI explains:** asking about errors, concepts, and wrong predictions, and reading the `AGENTS.md` instructions your AI follows.
- **Weeks 5–9, AI debugs and reviews:** trying first, then asking, and judging AI suggestions. You write your first **skills** (L10, L12, L14, L16).
- **Weeks 10–13, AI pair-programs:** writing a spec, building with AI, and verifying its claims. You give your AI tools with an **MCP server** (L20) and put the pieces together into your own workflow (L23).

Everything you build for your AI uses open formats (`AGENTS.md`, Agent Skills, and MCP), so it works in Copilot, OpenCode, Codex, and Claude Code.

## Grading

| Component | Weight | AI tier |
|---|---|---|
| Homework (12 assignments, autograded with pytest) | 10% | Tutor or pair programmer |
| In-class quizzes | 25% | No AI |
| Midterm | 20% | No AI |
| AI build session | 5% | Pair programmer |
| Final project, including the oral defense | 15% | Pair programmer |
| Final exam | 25% | No AI |

### Quizzes

Most classes start with a 10-minute quiz on the previous lecture: no AI, no notes. Each quiz has three questions:

1. **Tracing:** read a short piece of code and say what it prints or returns.
2. **Debugging:** find the bug in a short piece of code and fix it.
3. **Programming:** write a short function by hand, such as turning `135` minutes into `"2h 15m"`. Small syntax slips, like a missing colon, don't cost points.

Your lowest three quiz scores are dropped.

### Midterm and final exam

Both exams are on paper, with no AI, no notes, and no computer. They have the same three parts as the quizzes, with more questions:

| Part | Midterm (75 min, L01–L14) | Final (110 min, cumulative, weighted toward L15–L23) |
|---|---|---|
| **Tracing:** say what the code prints | 30 points | 25 points |
| **Debugging:** give an input that shows the bug, fix it, and write an `assert` that catches it | 30 points | 30 points |
| **Programming:** write functions or classes by hand | 40 points | 45 points |

Some final exam questions also ask for the Big-O of the code. As on quizzes, small syntax slips don't cost points. [`exams/`](exams) has a practice midterm and final in this format.

### AI build session

In week 13 (workshop 1), you get a small programming task at the start of class and 40 minutes to build it with AI as a pair programmer. Submit two things: your code, and the full transcript of your AI conversations.

- **Code (half):** run against tests you don't see. They check rules from the task that are easy to miss if you don't read it carefully.
- **Transcript (half):** shows how you worked. Did you give the AI a clear spec or examples before asking for code? Did you test what it wrote? Did you catch its mistakes, or push back instead of taking the first answer?

Working code with a transcript that's just "solve this" scores about half.

## Setup

Install [uv](https://docs.astral.sh/uv/) and fork this repo (see [`docs/setup.md`](docs/setup.md)). In your course folder, `uv run pytest` installs Python 3.15 and everything else that's needed. Students never need to install Python by hand or activate a virtual environment.
