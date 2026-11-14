# Setup guide

You need **uv**, **git**, an **editor**, and a **GitHub account** with Copilot. Plan for about 30 minutes, plus a few days' wait for GitHub to verify you're a student.

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

VS Code finds `.venv` automatically after your first `uv run`.

## 4. GitHub and Copilot

1. Make a GitHub account at [github.com/signup](https://github.com/signup) if you don't have one.
2. Apply for the [GitHub Student Developer Pack](https://education.github.com/pack) with your `@baruchmail.cuny.edu` email. **Do this in week 1**: verification can take a few days. Once you're approved, you get Copilot Student for free.
3. In VS Code, install the **GitHub Copilot Chat** extension and sign in with the same GitHub account.

Until you're approved, Copilot's free plan works for everything in weeks 1–4.

## 5. Get your copy of the course

You'll do all your work in your own copy of the course repo, called a **fork**. "Cloning" then downloads your fork to your computer.

1. Go to [github.com/ja153903/baruch-mth3300](https://github.com/ja153903/baruch-mth3300) and click **Fork**, then **Create fork**. You now have your own copy at `https://github.com/YOUR-USERNAME/baruch-mth3300`.
2. Submit that link to your instructor. That's how your homework gets graded.
3. In VS Code, open the command palette (**Cmd+Shift+P** on macOS, **Ctrl+Shift+P** on Windows), type **Git: Clone**, and press Enter.
4. Choose **Clone from GitHub**, sign in if VS Code asks, and pick `YOUR-USERNAME/baruch-mth3300`. Make sure it's **your** fork, not the original.
5. Pick a folder to save it in, like Documents. When VS Code asks, click **Open**.

Always open this whole folder in VS Code, not a single homework folder inside it. Your AI tools read their instructions from the top of the folder.

## 6. Check everything

In VS Code, open a terminal with *Terminal → New Terminal*. It opens inside your course folder. Run:

```sh
uv run pytest assignments/01-basics
```

You should see the tests **fail**, because you haven't written anything yet. That means your setup works.

Use VS Code's terminal for git commands all semester. It stays signed in to GitHub, so `git push` works without a password.

## Common problems

| Symptom | Fix |
|---|---|
| `uv: command not found` | Close and reopen the terminal. If that doesn't help, re-run the installer. |
| Windows: "running scripts is disabled" | Use the `-ExecutionPolicy ByPass` command above, exactly as written |
| `UnicodeDecodeError` reading a file | You're on an old Python. Run `uv run python --version`; this course needs 3.15. |
| `git push` asks for a password, or says authentication failed | Push from VS Code's terminal, not a separate one. If it still fails, click the account icon in VS Code's bottom-left corner and sign in to GitHub. |
| `uv run pytest` says no tests ran | You're in the wrong folder. Use *File → Open Folder* to open your course folder (the one with `SYLLABUS.md`), then open a new terminal. |
| `git push` says permission denied | You cloned the original repo instead of your fork. Clone your fork (step 5) and copy your work over. |
| VS Code shows the wrong Python | Command palette → *Python: Select Interpreter* → choose `.venv` |

## Next

[`tools.md`](tools.md) shows how to use each tool day to day, with examples: the terminal, uv, Python, git, VS Code, pytest, ruff, ty, and marimo.
