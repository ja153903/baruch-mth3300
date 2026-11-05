# Setup guide

You need three things: **uv**, **git**, and an **editor**. Plan for about 20 minutes.

## 1. uv (Python and packages)

**macOS / Linux:**

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** (PowerShell, *not* Command Prompt):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Close and reopen your terminal**, then check that it worked:

```sh
uv --version
uv run python --version     # should print Python 3.15.x
```

## 2. git

- **macOS:** run `git --version`. If git isn't installed, macOS offers to install the developer tools; accept.
- **Windows:** install [Git for Windows](https://git-scm.com/download/win) with the default options.
- **Linux:** `sudo apt install git` (or your distribution's equivalent)

Then tell git who you are:

```sh
git config --global user.name "Your Name"
git config --global user.email "you@baruchmail.cuny.edu"
```

## 3. Editor: VS Code

Install [VS Code](https://code.visualstudio.com/), then these extensions:

- **Python** (Microsoft)
- **Ruff** (Astral)
- **ty** (Astral)
- **marimo** (optional, for lecture notes)

Open a homework folder with *File → Open Folder*. VS Code finds `.venv` automatically after your first `uv run`.

## 4. Check everything

Clone homework 01, then run:

```sh
uv run pytest
```

You should see the tests **fail**, because you haven't written anything yet. That means your setup works.

## Common problems

| Symptom | Fix |
|---|---|
| `uv: command not found` | Close and reopen the terminal. If that doesn't help, re-run the installer. |
| Windows: "running scripts is disabled" | Use the `-ExecutionPolicy ByPass` command above, exactly as written |
| `UnicodeDecodeError` reading a file | You're on an old Python. Run `uv run python --version`; this course needs 3.15. |
| VS Code shows the wrong Python | Command palette → *Python: Select Interpreter* → choose `.venv` |
