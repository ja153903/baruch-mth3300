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

## For students: how to use this repo

This repo holds lectures, practice, and exams. **Homework is not here**; each assignment is a separate repo (see step 5).

**1. Set up once.** Follow [`docs/setup.md`](docs/setup.md) to install uv, git, and VS Code. Then:

```sh
git clone https://github.com/ja153903/baruch-mth3300.git mth3300
cd mth3300
uv sync
```

Run every command from inside the `mth3300` folder, and always through `uv run`. You never need to activate anything.

**2. Get new material before each class.** New lectures appear during the semester:

```sh
git pull
```

If git refuses because you changed some files, save your work in a commit first, then pull again:

```sh
git add -A
git commit -m "my work"
git pull
```

**3. Read the lecture notes.** They're interactive notebooks:

```sh
uv run marimo edit lectures/01-setup/notes.md
```

**4. Do the in-class exercises.** Edit `lNN_exercises.py` in the lecture's folder, then run its tests:

```sh
uv run pytest lectures/01-setup
```

Failing tests are normal until you finish. A test passes when your code is done.

**5. Do the homework in its own repo.** Each week your instructor will tell you how to get that week's homework repo. Clone it, and follow its `README.md`. To submit, commit and push:

```sh
git add -A
git commit -m "finish problem 2"
git push
```

Push as often as you like; your last push before the deadline is graded. Every push reruns the tests on GitHub; look at the **Actions** tab to see the result.

**6. Prepare for exams.** Work through [`practice/`](practice) and [`exams/`](exams) without AI first. Exam answers are hidden in collapsed sections; try each problem before you open them.

**Rules:** don't delete the `AGENTS.md` and `CLAUDE.md` files in your homework; they tell AI tools which [AI tier](docs/using-ai.md) applies. Log your AI use in `AI_LOG.md`.

## For instructors

Repo conventions, for both people and AI tools, are in [`AGENTS.md`](AGENTS.md).
