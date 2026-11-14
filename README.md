# MTH 3300

Course materials for MTH 3300 at Baruch College, written for Python 3.15.

| Folder | What's in it |
|---|---|
| [`SYLLABUS.md`](SYLLABUS.md) | the schedule, AI policy, and grading |
| [`lectures/`](lectures) | 23 lectures: marimo notes and in-class exercises |
| [`assignments/`](assignments) | weekly homework, done in your fork of this repo |
| [`practice/`](practice) | ungraded practice problems for exam prep |
| [`project/`](project) | the final project spec, options, and rubric |
| [`exams/`](exams) | practice midterm and final |
| [`docs/`](docs) | student guides: setup, tools, using AI |

## For students: how to use this repo

You'll work in your own copy of this repo all semester: lectures, exercises, homework, and the skills and tools you build for your AI.

**1. Set up once.** Follow [`docs/setup.md`](docs/setup.md) to install uv, git, and VS Code, and to make your own copy (a **fork**) of this repo. [`docs/tools.md`](docs/tools.md) shows how to use each tool, with examples. Then, in VS Code's terminal:

```sh
uv sync
```

Open the whole `mth3300` folder in VS Code, run every command from inside it, and always run Python tools through `uv run`. You never need to activate anything.

**2. Get new material before each class.** New lectures and homework appear during the semester. On your fork's GitHub page, click **Sync fork → Update branch**. Then, in VS Code's terminal:

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

**5. Do the homework.** Each week's homework is in `assignments/`. Follow its `README.md`, and check your work with its tests:

```sh
uv run pytest assignments/01-basics
```

To submit, commit and push to your fork:

```sh
git add -A
git commit -m "finish problem 2"
git push
```

Push as often as you like. Your last push before the deadline is graded, using the original tests.

**6. Prepare for exams.** Work through [`practice/`](practice) and [`exams/`](exams) without AI first. Exam answers are hidden in collapsed sections; try each problem before you open them.

**Rules:** don't delete or edit any `AGENTS.md` or `CLAUDE.md` file that came with the course, and don't edit test files. The `AGENTS.md` files tell AI tools which [AI tier](docs/using-ai.md) applies. Log your AI use in each homework's `AI_LOG.md`.

## For instructors

Repo conventions, for both people and AI tools, are in [`AGENTS.md`](AGENTS.md).
