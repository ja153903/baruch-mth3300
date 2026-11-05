# Live-coding sessions

These count toward the 15% "quizzes and live coding" grade. A student solves a short problem **in front of you**, with no AI, thinking out loud. Grade the **process**, not just whether it's finished.

**Format:** 10 minutes, a blank `.py` file, the REPL allowed, no AI or internet.

**Rubric (10 points):** restates the problem (2) · tries a small example first (2) · working code (3) · tests or checks an edge case (2) · explains a bug they hit (1)

| Round | After | Prompts (pick one per student) |
|---|---|---|
| 1 | L06 | `celsius_to_f(c)` · `is_leap_year(y)` · `hours_to_hms(seconds) -> str` |
| 2 | L12 | `count_negatives(xs)` · `reverse_words(s)` · `index_of_max(xs)` without `max` |
| 3 | L19 | `char_counts(s) -> dict` · `has_duplicates(xs)` in O(n) · recursive `sum_list(xs)` |
| 4 | L22 | dataclass `Temperature` with `to_f()` · `parse_prices(lines) -> dict` that skips bad rows · `match` on `("add", a, b)` commands |

**Follow-ups to ask:** "What happens with an empty input?" · "What's the Big-O?" · "How would you test that?"
