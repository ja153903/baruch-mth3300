# Tools guide

These are the tools this course uses. You install uv, git, and VS Code yourself (see [`setup.md`](setup.md)). uv installs the rest for you.

| Tool | What it does | How you get it | First used |
|---|---|---|---|
| [The terminal](#the-terminal) | where you type commands | already on your computer | week 1 |
| [uv](#uv) | installs Python and runs everything | [`setup.md`](setup.md#1-uv-python-and-packages) | week 1 |
| [Python](#python) | runs your code | uv installs it | week 1 |
| [git and GitHub](#git-and-github) | saves snapshots and submits homework | [`setup.md`](setup.md#2-git) | week 1 |
| [VS Code](#vs-code) | where you write code | [`setup.md`](setup.md#3-editor-vs-code) | week 1 |
| [pytest](#pytest) | checks whether your code works | uv installs it | week 3 |
| [ruff](#ruff) | finds style problems and tidies code | uv installs it | week 4 |
| [ty](#ty) | finds type mistakes before you run | uv installs it | week 4 |
| [marimo](#marimo) | opens the interactive lecture notes | uv installs it (course repo only) | week 1 |

You never install Python, pytest, ruff, ty, or marimo by hand. Each homework folder lists them in its `pyproject.toml`, and the first `uv run` in that folder installs them.

## The terminal

The terminal is a window where you type commands instead of clicking. Use the one built into VS Code (*Terminal → New Terminal*). It opens in the folder you have open, which is almost always the folder you want.

A command only sees the folder you're in. Most "it doesn't work" problems come from being in the wrong folder.

| To… | macOS / Linux | Windows (PowerShell) |
|---|---|---|
| see which folder you're in | `pwd` | `pwd` |
| list the files here | `ls` | `ls` |
| go into a folder | `cd assignments` | `cd assignments` |
| go up one folder | `cd ..` | `cd ..` |
| stop a running program | **Ctrl+C** | **Ctrl+C** |
| repeat an earlier command | **↑** arrow | **↑** arrow |

```sh
$ pwd
/Users/sam/Documents/baruch-mth3300
$ ls
AGENTS.md  README.md  SYLLABUS.md  assignments  docs  exams  lectures  practice  project  pyproject.toml
```

If you see `SYLLABUS.md` and `assignments`, you're in the right place: the top of your course folder. In these docs, `$` stands for the prompt; don't type it.

## uv

uv installs the right Python version and every package a folder needs, then runs your command. **Put `uv run` in front of every Python tool command.** You never need to activate a virtual environment.

| Command | What it does |
|---|---|
| `uv run python` | start the Python REPL |
| `uv run python hello.py` | run a program |
| `uv run pytest assignments/01-basics` | run one homework's tests |
| `uv run ruff check` | check style |
| `uv run ty check` | check types |
| `uv sync` | install everything without running anything (handy after `git pull`) |
| `uv --version` | check that uv is installed |

The first `uv run` in a new folder downloads things and takes a few seconds. After that it starts instantly.

```sh
$ uv run python --version
Python 3.15.0
```

`uv run` creates a `.venv` folder next to `pyproject.toml`. That's where the packages live. Don't edit it or commit it; if something seems broken, delete `.venv` and run `uv sync`.

## Python

**The REPL** is for trying one line at a time. Type an expression, press Enter, and Python prints its value:

```text
$ uv run python
>>> 7 * 24 * 60 * 60
604800
>>> name = "Baruch"
>>> f"Hello, {name}!"
'Hello, Baruch!'
>>> 0.1 + 0.2
0.30000000000000004
>>> exit
```

**A program** is a `.py` file that runs top to bottom. Save this as `hello.py`:

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

Then run it:

```text
$ uv run python hello.py
What's your name? Sam
Hello, Sam!
```

When something goes wrong, Python prints a **traceback**. Read it from the bottom up: the last line says what went wrong, and the line above it says where. Lecture L4 covers tracebacks in detail.

## git and GitHub

git saves snapshots of your files, called **commits**. GitHub stores your commits online. Pushing your commits to GitHub is how you submit homework.

**The everyday loop** (run these in the homework folder):

```sh
git status                          # what changed since the last commit?
git add -A                          # include every change in the next snapshot
git commit -m "finish problem 2"    # take the snapshot, with a short message
git push                            # upload it to GitHub
```

```text
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   assignments/01-basics/hw01.py

no changes added to commit (use "git add" and/or "git commit -a")

$ git add -A
$ git commit -m "finish problem 2"
[main 3f2a9c1] finish problem 2
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push
```

Commit and push whenever you finish a piece of work, not only at the end. Your last push before the deadline is graded.

**Other useful commands:**

| Command | What it does |
|---|---|
| `git clone <url>` | download a repo to your computer (once, for your fork) |
| `git pull` | download new commits, like new lectures, after you click **Sync fork** on GitHub |
| `git log --oneline` | list your commits, newest first |
| `git diff` | show exactly what you changed since the last commit |
| `git restore assignments/01-basics/hw01.py` | throw away your uncommitted changes to that file (careful: this can't be undone) |

**Checking your work.** Run `uv run pytest assignments/01-basics` (with your homework's folder) before you push. That's the same check used for grading.

If `git push` asks for a password, see [Common problems in `setup.md`](setup.md#common-problems).

## VS Code

| To… | Do this |
|---|---|
| open the course | *File → Open Folder*, then pick your course folder, the one with `SYLLABUS.md` |
| open a terminal | *Terminal → New Terminal* |
| run any command by name | **Cmd+Shift+P** (macOS) or **Ctrl+Shift+P** (Windows), then type |
| see ruff and ty problems as you type | install the Ruff and ty extensions; problems get squiggly underlines and show in *View → Problems* |
| format the file | command palette → *Format Document* |
| commit without the terminal | the **Source Control** icon in the left sidebar |

VS Code uses the Python in `.venv` once you've run `uv run` at least once. If it picks the wrong one, use command palette → *Python: Select Interpreter* → `.venv`.

## pytest

Each homework comes with a `test_hwNN.py` file. Each `test_` function in it checks one thing your code should do. pytest runs them all and reports which pass. **Your homework is done when every test passes.** Don't edit the test file; grading uses the original.

Say `clock.py` has this function, which should turn `135` minutes into `"2h 15m"`:

```python
def to_text(minutes: int) -> str:
    return f"{minutes // 60}h {minutes // 60}m"
```

and `test_clock.py` checks it:

```python
from clock import to_text


def test_to_text():
    assert to_text(135) == "2h 15m"


def test_to_text_under_an_hour():
    assert to_text(45) == "0h 45m"
```

Run the tests:

```text
$ uv run pytest
...
    def test_to_text():
>       assert to_text(135) == "2h 15m"
E       AssertionError: assert '2h 2m' == '2h 15m'
E
E         - 2h 15m
E         + 2h 2m

test_clock.py:5: AssertionError
...
FAILED test_clock.py::test_to_text - AssertionError: assert '2h 2m' == '2h 15m'
FAILED test_clock.py::test_to_text_under_an_hour - AssertionError: assert '0h...
============================== 2 failed in 0.02s ===============================
```

How to read it: the `>` line is the check that failed. `'2h 2m' == '2h 15m'` means your code returned `'2h 2m'` but the test expected `'2h 15m'`. The minutes are wrong, so look at the minutes part: it should be `minutes % 60`. Fix it and run again:

```text
$ uv run pytest
test_clock.py ..                                                         [100%]
============================== 2 passed in 0.02s ===============================
```

Each `.` is a passing test and each `F` is a failing one.

| Command | What it does |
|---|---|
| `uv run pytest assignments/01-basics` | run one homework's tests |
| `uv run pytest -x` | stop at the first failure, so you can fix one thing at a time |
| `uv run pytest -k hour` | run only tests with `hour` in their name |
| `uv run pytest -q` | shorter output |
| `uv run pytest lectures/05-functions` | run one lecture's exercises |

## ruff

ruff reads your code without running it. `ruff check` finds likely mistakes, like an import you never use or a name you never defined. `ruff format` fixes spacing and layout so all code looks the same.

```python
# report.py
import math


def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)
```

```text
$ uv run ruff check
report.py:1:8: F401 [*] `math` imported but unused
Found 1 error.
[*] 1 fixable with `--fix`.

$ uv run ruff check --fix
Found 1 error (1 fixed, 0 remaining).
```

`report.py:1:8` means file `report.py`, line 1, column 8. `[*]` means ruff can fix it for you.

`ruff format` turns this:

<!-- fmt:off -->
```python
def total( prices:list[float] )->float:
    return sum( prices )
```
<!-- fmt:on -->

into this:

```python
def total(prices: list[float]) -> float:
    return sum(prices)
```

| Command | What it does |
|---|---|
| `uv run ruff check` | list problems |
| `uv run ruff check --fix` | fix the ones ruff can fix safely |
| `uv run ruff format` | reformat every file |
| `uv run ruff format --check` | say which files would change, without changing them |

To look up a rule like `F401`, search for it at [docs.astral.sh/ruff/rules](https://docs.astral.sh/ruff/rules/).

## ty

ty checks your type hints without running your code. It catches mistakes like putting a `float` where you promised an `int`. Lecture L6 introduces type hints.

```python
# report.py
def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


best: int = average([88, 92, 79])
```

```text
$ uv run ty check
error[invalid-assignment]: Object of type `float` is not assignable to `int`
 --> report.py:5:13
  |
5 | best: int = average([88, 92, 79])
  |       ---   ^^^^^^^^^^^^^^^^^^^^^ Incompatible value of type `float`
  |       |
  |       Declared type

Found 1 diagnostic
```

`average` returns a `float`, but `best` says it holds an `int`. Either `best` should be a `float`, or you meant to round. ty can't tell which; you decide.

| Command | What it does |
|---|---|
| `uv run ty check` | check every file in the folder |
| `uv run ty check report.py` | check one file |

**ruff and ty don't replace tests.** Code can pass both and still give the wrong answer. Run all three before you push:

```sh
uv run pytest assignments/01-basics && uv run ruff check assignments/01-basics && uv run ty check assignments/01-basics
```

## marimo

The lecture notes are marimo notebooks: text with Python cells you can edit and run. marimo comes installed with the course.

```sh
uv run marimo edit lectures/01-setup/notes.md
```

This opens the notes in your browser. Things to try:

- Change a number in a code cell and press **Shift+Enter** to run it. Every cell that uses that variable reruns too.
- Add a cell with the **+** button to try your own code.
- Stop marimo by pressing **Ctrl+C** in the terminal.

Your edits change your copy of the file. If `git pull` later refuses because of them, see step 2 of the [main README](../README.md#for-students-how-to-use-this-repo).

## Where to get more help

- uv: [docs.astral.sh/uv](https://docs.astral.sh/uv/)
- Python: [docs.python.org/3.15/tutorial](https://docs.python.org/3.15/tutorial/)
- pytest: [docs.pytest.org](https://docs.pytest.org/en/stable/getting-started.html)
- ruff: [docs.astral.sh/ruff](https://docs.astral.sh/ruff/)
- ty: [docs.astral.sh/ty](https://docs.astral.sh/ty/)
- marimo: [docs.marimo.io](https://docs.marimo.io/)
- git: [the git book, chapter 2](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

An AI tutor is good at explaining error output. Paste the error and the code it points to, and ask what it means. See [`using-ai.md`](using-ai.md).
