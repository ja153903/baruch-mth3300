---
title: "L15: Files and paths"
marimo-version: "0.25.2"
---

# L15: Files and paths

**By the end of this lecture you can:**

- build file paths with `pathlib`
- read and write text files safely with `with`
- process a file line by line

```python {.marimo hide_code="true"}
import marimo as mo
```

## 1. Paths

`pathlib.Path` builds paths that work on macOS, Windows, and Linux alike. Use `/` to join path parts.

```python {.marimo}
import tempfile
from pathlib import Path

workdir = Path(tempfile.mkdtemp())  # a scratch folder for this lecture
notes_file = workdir / "notes.txt"
print(notes_file.name, notes_file.suffix, notes_file.parent == workdir)
```

## 2. Writing and reading the whole file

```python {.marimo}
notes_file.write_text("first line\nsecond line\nthird line\n")
print(notes_file.read_text())
print(notes_file.exists())
```

## 3. `with open(...)`: line by line

`with` closes the file for you, even if an error happens partway through.

```python {.marimo}
with open(notes_file) as f:
    for line_number, line in enumerate(f, start=1):
        print(line_number, line.rstrip("\n"))
```

**Predict:** why do we need `.rstrip("\n")`? What prints without it?

## 4. Writing line by line

```python {.marimo}
log_file = workdir / "log.txt"
with open(log_file, "w") as out:
    for day in ["Mon", "Tue", "Wed"]:
        out.write(f"{day}: ok\n")
print(log_file.read_text())
```

Mode `"w"` **replaces** the file's contents, and `"a"` **appends** to it.

## 5. Listing files

```python {.marimo}
print(sorted(p.name for p in workdir.glob("*.txt")))
```

## AI activity

Ask an AI: *"What happens if my program crashes while a file is open without `with`?"* Then write a two-sentence explanation in your own words.

**Exercises:** `l15_exercises.py`
