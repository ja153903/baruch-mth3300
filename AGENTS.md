# MTH 3300 course materials

Instructor repo for an intro Python course at Baruch College. Students are beginners, mostly math and finance majors. The week-by-week plan (23 lectures, AI tiers, grading) is in `SYLLABUS.md`.

## Layout

- `lectures/NN-topic/`: one folder per lecture, L01–L23.
  - `notes.md` is a marimo notebook in Markdown format. Code cells are fenced ```` ```python {.marimo} ````, and each file needs one `import marimo as mo` cell. A variable can be defined in only one cell; use an `_` prefix for cell-local names. Notes that write files must use a temp directory.
  - `lNN_exercises.py` and `test_lNN_exercises.py`: in-class exercises.
- `assignments/NN-name/`: the homework for week NN (none for exam weeks). Each one becomes its own student repo, so it must stand alone, with its own `pyproject.toml`, `uv.lock`, `.python-version`, `AI_LOG.md`, and `.github/workflows/autograde.yml`. It contains:
  - `README.md`: the problem statement and AI policy
  - `hwNN.py`: the starter code, with `raise NotImplementedError` stubs
  - `test_hwNN.py`: pytest tests that define "done"
  - `AGENTS.md` and `CLAUDE.md`: **student-facing AI instructions**, in tutor mode for weeks 1–9 and pair-programmer mode for weeks 10–13. They tell the student's AI how to behave and do NOT apply to you when you are editing this repo as the instructor.
  - To add an assignment, copy an existing folder with the same AI tier, rename `hwNN` throughout, and run `uv lock` inside it.
- `practice/<topic>/`: ungraded problems (`p_<topic>.py` and its tests) for exam prep.
- `project/`: the final project spec, options, and rubric.
- `exams/`: student-facing practice exams, with answers in `<details>` blocks.
- `docs/`: student guides (setup, using AI).
- `instructor/`: quizzes, live-coding prompts, and oral-defense questions. **Gitignored; never commit or publish it.**
- Solutions never go in this repo.

## Conventions

- Python 3.15. Use modern syntax: `list[int]`, `X | None`, f-strings, `match`, dataclasses, `pathlib`.
- Every module name must be unique across the repo (`hw01.py`, `l05_exercises.py`, `p_lists.py`), so pytest can collect everything in one run.
- Write code students can read at that point in the course: only use features that `SYLLABUS.md` has covered by then.
- Weeks 1–2 (and lectures L01–L04) come before functions, so their starters are module-level variables that tests check directly.
- Check every "predict the output" answer by running it.

## Commands

```sh
uv run pytest assignments/03-functions   # starters fail until implemented; that's expected
uv run pytest --collect-only -q          # check that every test imports
uv run ruff check && uv run ruff format --check
uv run ty check
uv run marimo check lectures/*/notes.md
uv run marimo edit lectures/01-setup/notes.md
```
