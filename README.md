# MTH 3300

Course materials for MTH 3300 at Baruch College, written for Python 3.15.

| Folder | What's in it |
|---|---|
| [`SYLLABUS.md`](SYLLABUS.md) | the schedule, AI policy, and grading |
| [`lectures/`](lectures) | 23 lectures: marimo notes and in-class exercises |
| [`assignments/`](assignments) | weekly homework; each folder becomes a student repo |
| [`practice/`](practice) | ungraded practice problems for exam prep |
| [`project/`](project) | the final project spec, options, and rubric |
| [`exams/`](exams) | practice midterm and final |
| [`docs/`](docs) | student guides: setup, using AI |

## Setup

Install [uv](https://docs.astral.sh/uv/), then run `uv sync`. Run everything through `uv run`; you don't need to activate anything.

```sh
uv run marimo edit lectures/01-setup/notes.md   # open lecture notes
uv run pytest practice/strings                  # run some tests
```

Repo conventions, for both people and AI tools, are in [`AGENTS.md`](AGENTS.md).
