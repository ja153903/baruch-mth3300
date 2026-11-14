---
title: "L15: Files and paths"
marimo-version: "0.25.2"
---

# L15: Files and paths

**By the end of this lecture you can:**

- build file paths with `pathlib`, and take them apart
- read and write a whole text file at once
- read and write a file line by line with `with`
- choose the right mode: reading, `"w"`, or `"a"`
- process a file line by line: clean it, filter it, and total it
- list, copy, and move files

```python {.marimo hide_code="true"}
import marimo as mo
```

## 0. Warmup (from L14)

Welcome back from the midterm. **Predict** all three:

```python {.marimo}
_a = {1, 2, 3, 4}
_b = {3, 4, 5}
print(sorted(_a - _b), sorted(_a ^ _b), len(_a | _b))
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

A `Path` is only a name. Making one doesn't create a file, and it doesn't check that the file exists. **Predict** each line:

```python {.marimo}
_report = Path("data") / "2026" / "prices.csv"
print(_report)
print(_report.name, _report.stem, _report.suffix)
print(_report.parent)
print(_report.with_suffix(".txt"))
```

On Windows, these paths print with `\` instead of `/`. Your code stays the same.

### Common bug: the wrong working folder

`Path("data/prices.csv")` is a **relative** path. Python looks for it inside the folder you ran the program from, which `Path.cwd()` tells you. Run the same program from a different folder, and it can't find the file. In a script, `Path(__file__).parent / "prices.csv"` means "next to this script," wherever you run it from.

## 2. Writing and reading the whole file

```python {.marimo}
notes_file.write_text("first line\nsecond line\nthird line\n")
print(notes_file.read_text())
print(notes_file.exists())
```

`read_text` gives you one long string. `.splitlines()` turns it into a list of lines, without the newlines:

```python {.marimo}
_lines = notes_file.read_text().splitlines()
print(_lines, len(_lines))
```

Files store bytes, and an **encoding** says how text becomes bytes. Since Python 3.15, the default is UTF-8 on every operating system, so this code behaves the same on macOS, Windows, and Linux. L22 covers encodings in detail.

## 3. `with open(...)`: line by line

`with` closes the file for you, even if an error happens partway through.

```python {.marimo}
with open(notes_file) as f:
    for line_number, line in enumerate(f, start=1):
        print(line_number, line.rstrip("\n"))
```

**Predict:** why do we need `.rstrip("\n")`? What prints without it?

A loop over a file reads one line at a time, so it uses very little memory. It works even on a file bigger than your computer's memory.

## 4. Writing line by line

```python {.marimo}
log_file = workdir / "log.txt"
with open(log_file, "w") as out:
    for day in ["Mon", "Tue", "Wed"]:
        out.write(f"{day}: ok\n")
print(log_file.read_text())
```

Mode `"w"` **replaces** the file's contents, and `"a"` **appends** to it:

```python {.marimo}
with open(log_file, "a") as _out:
    _out.write("Thu: ok\n")
print(log_file.read_text())
```

### Common bug: forgetting the newline

**Predict:**

```python {.marimo}
_squashed = workdir / "squashed.txt"
with open(_squashed, "w") as _out:
    for _day in ["Mon", "Tue", "Wed"]:
        _out.write(_day)
print(_squashed.read_text())
```

`write` writes exactly what you give it. Unlike `print`, it doesn't add a newline at the end.

### Common bug: `"w"` empties the file right away

**Predict:** what's in the file at the end?

```python {.marimo}
_important = workdir / "important.txt"
_important.write_text("do not lose me\n")
with open(_important, "w") as _f:
    pass  # meant to read it, but opened it for writing
print(repr(_important.read_text()))
```

Opening a file with `"w"` empties it before you write anything. To read a file, open it with no mode at all.

## 5. A finance example: cleaning and totaling a file

Real files are messy, with blank lines and extra spaces. Clean each line with `.strip()`, and skip the lines that are empty.

```python {.marimo}
prices_file = workdir / "prices.txt"
prices_file.write_text("101.5\n  99.0\n\n103.25  \n98.0\n")

_total = 0.0
_count = 0
with open(prices_file) as _f:
    for _line in _f:
        _line = _line.strip()
        if _line != "":
            _total += float(_line)
            _count += 1
print(f"{_count} prices, average {_total / _count:.2f}")
```

**Predict:** what goes wrong without the `if`? L16 shows how to handle errors like that one.

## 6. Reading one file and writing another

Many programs read an input file and write a cleaned-up output file. One `with` can open both:

```python {.marimo}
_above = workdir / "above_100.txt"
with open(prices_file) as _src, open(_above, "w") as _dst:
    for _line in _src:
        _line = _line.strip()
        if _line != "" and float(_line) > 100:
            _dst.write(_line + "\n")
print(_above.read_text())
```

## 7. Listing files

```python {.marimo}
print(sorted(p.name for p in workdir.glob("*.txt")))
```

In `glob("*.txt")`, the `*` matches anything, so you get every name that ends in `.txt`.

## 8. Folders, copying, and moving

```python {.marimo}
_draft = workdir / "draft.md"
_draft.write_text("version 1\n")
_backup = _draft.copy(workdir / "draft.bak")
_archived = _backup.move(workdir / "archive.bak")
print(_draft.exists(), _backup.exists(), _archived.exists())
```

**Predict:** which of the three files exists at the end?

`copy` and `move` are new in Python 3.14. `mkdir` makes a folder. `parents=True` also makes any missing folders along the way, and `exist_ok=True` means "don't complain if it's already there."

```python {.marimo}
_folder = workdir / "2026" / "reports"
_folder.mkdir(parents=True, exist_ok=True)
(_folder / "q1.txt").write_text("Q1 report\n")
print(_folder.is_dir(), sorted(p.name for p in _folder.iterdir()))
```

## 9. Checking that a file exists

Reading a file that isn't there raises `FileNotFoundError`. For now, check first with `.exists()`. L16 shows a better way to handle errors.

```python {.marimo}
_missing = workdir / "nope.txt"
if _missing.exists():
    print(_missing.read_text())
else:
    print(f"{_missing.name} not found")
```

## AI activity: why `with`?

1. Ask an AI: *"What happens if my program crashes while a file is open without `with`?"* Then write a two-sentence explanation in your own words.
2. Ask it to rewrite this code with `with`:

   ```python
   out = open("log.txt", "w")
   out.write("Mon: ok\n")
   out.close()
   ```

3. Run both versions in the REPL from a scratch folder, and compare the files they write. Did the AI change anything besides adding `with`?

## Exercises (40 minutes)

Each exercise takes a `Path`. The tests make their files in a temporary folder with pytest's `tmp_path`, so they never touch your own files. Open `l15_exercises.py` and run `uv run pytest lectures/15-files` as you go. Do them in order:

| Group | Functions |
|---|---|
| Warmup | `write_lines`, `read_numbers` |
| Core | `longest_line`, `append_line`, `find_lines`, `filter_file` |
| Fix the AI's code | `save_prices` |
| Stretch | `backup`, `word_index` |
