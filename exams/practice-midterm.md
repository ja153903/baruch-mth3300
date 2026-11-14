# Practice midterm

**No AI, no notes, no computer.** Covers L01–L14. Give yourself 75 minutes. 100 points.

## Part A: predict the output (5 points each)

```python
# A1
print(17 // 5, 17 % 5, -17 // 5)

# A2
s = "Baruch College"
print(s[2:6], s[-3:], s[::4])

# A3
a = [1, 2, 3]
b = a
b.append(4)
c = a.copy()
c.append(5)
print(a, b, c)


# A4
def f(x):
    x = x * 2
    print(x)


y = f(3)
print(y)

# A5
d = {"a": 1, "b": 2}
d["a"] += 10
print(d.get("c", 0), sorted(d.items()))

# A6
print([n * n for n in range(6) if n % 2 == 1])
```

## Part B: find the bug (10 points each)

```python
# B1: should return True if every number is positive
def all_positive(xs):
    for x in xs:
        if x > 0:
            return True
    return False


# B2: should count the vowels in text
def count_vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiou":
            count + 1
    return count


# B3: should map each word to how many times it appears
def word_counts(words):
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        counts[w] = 1
    return counts
```

For each one: give an input that shows the bug, write the fixed code, and write one `assert` that fails on the buggy code and passes on your fix.

## Part C: write code (20 points each)

Graded on correct logic and handling the example. Small syntax slips, like a missing colon, don't cost points.

**C1.** Write `running_max(xs: list[int]) -> list[int]`, which returns the largest value seen so far at each position. For example, `running_max([3, 1, 4, 1, 5])` is `[3, 3, 4, 4, 5]`.

**C2.** Write `group_by_length(words: list[str]) -> dict[int, list[str]]`. For example, `["hi", "cat", "yo"]` gives `{2: ["hi", "yo"], 3: ["cat"]}`.

<details>
<summary>Answers</summary>

- **A1:** `3 2 -4`
- **A2:** `ruch ege Bcog` (`s[::4]` takes indexes 0, 4, 8, 12, which are `B`, `c`, `o`, `g`)
- **A3:** `[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4, 5]`
- **A4:** `6`, then `None`
- **A5:** `0 [('a', 11), ('b', 2)]`
- **A6:** `[1, 9, 25]`
- **B1:** returns `True` as soon as it finds one positive number, so `[1, -1]` gives `True`. Fix: `if x <= 0: return False`, with `return True` after the loop. Assert: `assert all_positive([1, -1]) == False`
- **B2:** `count + 1` doesn't update `count`, so it always returns 0. Fix: `count += 1`. Assert: `assert count_vowels("hello") == 2`
- **B3:** `counts[w] = 1` runs every time, even after the `+= 1`, so every count is 1 and `["a", "a"]` gives `{"a": 1}`. Fix: put `counts[w] = 1` under an `else:`. Assert: `assert word_counts(["a", "a"]) == {"a": 2}`
</details>
