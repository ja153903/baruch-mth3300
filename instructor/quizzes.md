# Lecture quizzes

Each quiz is 3 questions, for the first 5 minutes of the *next* class. No AI. Answers are in brackets.

| L | Questions |
|---|---|
| 01 | 1. What command runs `hello.py`? [`uv run python hello.py`] 2. What does `print(2 + 3 * 4)` show? [14] 3. Which git command uploads your commits? [`git push`] |
| 02 | 1. `7 // 2` and `7 % 2`? [3, 1] 2. `type(6 / 3)`? [`float`] 3. `int(3.99)`? [3] |
| 03 | 1. `"Baruch"[1:4]`? [`aru`] 2. `"Baruch"[-1]`? [`h`] 3. Why does `s[0] = "X"` fail? [strings are immutable] |
| 04 | 1. `f"{3.14159:.2f}"`? [`3.14`] 2. What type does `input()` return? [`str`] 3. Which line of a traceback do you read first? [the last line] |
| 05 | 1. What does a function without `return` give back? [`None`] 2. Parameter vs. argument? [the name in the definition vs. the value passed in] 3. `def f(x=2): return x * 3`; `f()`? [6] |
| 06 | 1. What does `assert False` raise? [`AssertionError`] 2. Which files does pytest collect? [`test_*.py`] 3. Does Python enforce type hints at runtime? [no] |
| 07 | 1. `0.1 + 0.2 == 0.3`? [False] 2. `bool([])`? [False] 3. `1 < 2 < 3 > 2`? [True] |
| 08 | 1. Which tool formats code? [`ruff format`] 2. What does `f"{x=}"` print when `x = 5`? [`x=5`] 3. One step you take after fixing a bug? [add a test] |
| 09 | 1. The three parts of a loop? [initialize, test, update] 2. How many times does `while n > 0: n //= 10` run for `n = 500`? [3] 3. What does `break` do? [exits the innermost loop] |
| 10 | 1. `list(range(1, 10, 3))`? [`[1, 4, 7]`] 2. The identity value for a product? [1] 3. What does `enumerate` give you? [(index, value) pairs] |
| 11 | 1. `a = [1]; b = a; b.append(2); a`? [`[1, 2]`] 2. What does `sorted(x)` return, compared with `x.sort()`? [a new list vs. None] 3. Copy a list? [`a.copy()` or `a[:]`] |
| 12 | 1. `x, y = (3, 4)`; `y`? [4] 2. `[c for c in "abc" if c != "b"]`? [`['a', 'c']`] 3. What does `zip(..., strict=True)` add? [an error if the lengths differ] |
| 13 | 1. `{"a": 1}.get("b", 0)`? [0] 2. What happens when you index a missing key? [`KeyError`] 3. Can a list be a dict key? [no; it's mutable, so it can't be hashed] |
| 14 | 1. `{1, 2} & {2, 3}`? [`{2}`] 2. `len(set("banana"))`? [3] 3. Which structure for fast `in` checks? [a set] |
| 15 | 1. What does `with` guarantee? [the file gets closed] 2. Mode `"w"` vs. `"a"`? [overwrite vs. append] 3. `Path("a") / "b.txt"`? [the path `a/b.txt`] |
| 16 | 1. `int("4.5")` raises what? [`ValueError`] 2. What type is every value from `csv.DictReader`? [`str`] 3. Why avoid a bare `except:`? [it hides real bugs] |
| 17 | 1. The two parts of every recursive function? [a base case and a recursive case] 2. What happens with no base case? [`RecursionError`] 3. `gcd(12, 8)`? [4] |
| 18 | 1. What does binary search require? [a sorted list] 2. About how many steps for a million items? [~20] 3. What algorithm does Python's `sorted` use? [Timsort] |
| 19 | 1. Big-O of `x in a_set`? [O(1)] 2. Doubling n for an O(n²) algorithm multiplies the time by? [4] 3. Profile or guess? [profile] |
| 20 | 1. Three methods `@dataclass` writes for you? [`__init__`, `__repr__`, `__eq__`] 2. Why `default_factory=list`? [so instances don't share one list] 3. What does `frozen=True` prevent? [changing fields] |
| 21 | 1. What does `case _:` match? [anything] 2. `match (1, 2): case (a, b): a + b`? [3] 3. Can you add an `if` condition to a case? [yes, a guard] |
| 22 | 1. Build a `Decimal` from a string or a float? [a string] 2. `Fraction(1, 3) + Fraction(1, 6)`? [`1/2`] 3. Why set a seed? [reproducible results] |
| 23 | 1. `np.array([1, 2]) * 2`? [`[2 4]`] 2. Which command adds a library? [`uv add`] 3. Three things every plot needs? [a title and two axis labels] |
