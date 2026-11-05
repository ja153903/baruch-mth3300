from collections.abc import Callable

# Implement from the spec (AI allowed: pair programmer)


def median(xs: list[float]) -> float:
    """The middle value of xs once sorted. For an even length, the mean of the two middle values.

    Raises ValueError if xs is empty. Does not change xs.
    median([3, 1, 2]) == 2 and median([4, 1, 3, 2]) == 2.5
    """
    raise NotImplementedError


def normalize_spaces(text: str) -> str:
    """text with every run of whitespace (spaces, tabs, newlines) replaced by one space,
    and no whitespace at either end.

    normalize_spaces("  a \t b\n\nc  ") == "a b c"
    """
    raise NotImplementedError


# Write the checks yourself. Each one returns True only if `fn` meets the spec above.
# The tests run your check on correct and buggy versions, so think about edge cases.
# A buggy fn might raise the wrong error: catch it and return False.


def check_median(fn: Callable[[list[float]], float]) -> bool:
    """True if fn behaves like median on every case you can think of."""
    raise NotImplementedError


def check_normalize_spaces(fn: Callable[[str], str]) -> bool:
    """True if fn behaves like normalize_spaces on every case you can think of."""
    raise NotImplementedError


# Slow vs. fast


def count_pairs_slow(xs: list[int], target: int) -> int:
    """How many pairs of positions i < j have xs[i] + xs[j] == target.

    Write the simplest version you're sure is correct: two nested loops.
    """
    raise NotImplementedError


def count_pairs_fast(xs: list[int], target: int) -> int:
    """The same as count_pairs_slow, in O(n): one pass with a dict of counts."""
    raise NotImplementedError


def agree(trials: int, seed: int) -> bool:
    """Compare count_pairs_slow and count_pairs_fast on `trials` random lists and targets.

    Use random.Random(seed). Return False as soon as they disagree.
    """
    raise NotImplementedError


# Fix the AI's code: this has two bugs. Write a failing example for each, then fix them.


def word_counts(text: str) -> dict[str, int]:
    """How many times each word appears in text.

    Words are compared in lower case, with . , ! ? ; : removed from both ends.
    Anything that's empty after removing punctuation isn't a word.
    """
    counts = {}
    for word in text.split():
        word = word.strip(".,!?;:")
        counts[word] = counts.get(word, 0) + 1
    return counts
