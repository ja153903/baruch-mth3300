import re

from l23_exercises import (
    agree,
    check_median,
    check_normalize_spaces,
    count_pairs_fast,
    count_pairs_slow,
    median,
    normalize_spaces,
    word_counts,
)

# Buggy versions that a good check should reject.


def median_upper_middle(xs: list[float]) -> float:
    return sorted(xs)[len(xs) // 2]


def median_unsorted(xs: list[float]) -> float:
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def median_no_error(xs: list[float]) -> float:
    return median(xs) if xs else 0.0


def median_sorts_input(xs: list[float]) -> float:
    xs.sort()
    return median(xs)


def normalize_strip_only(text: str) -> str:
    return text.strip()


def normalize_spaces_only(text: str) -> str:
    return " ".join(part for part in text.split(" ") if part)


def normalize_no_strip(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def test_median():
    assert median([3, 1, 2]) == 2
    assert median([4, 1, 3, 2]) == 2.5
    assert median([7]) == 7
    data: list[float] = [3, 1, 2]
    median(data)
    assert data == [3, 1, 2]
    try:
        median([])
    except ValueError:
        pass
    else:
        raise AssertionError("median([]) should raise ValueError")


def test_normalize_spaces():
    assert normalize_spaces("  a \t b\n\nc  ") == "a b c"
    assert normalize_spaces("") == ""
    assert normalize_spaces("one") == "one"


def test_check_median_accepts_correct():
    assert check_median(median)


def test_check_median_rejects_bugs():
    for buggy in [
        median_upper_middle,
        median_unsorted,
        median_no_error,
        median_sorts_input,
    ]:
        assert not check_median(buggy), buggy.__name__


def test_check_normalize_spaces_accepts_correct():
    assert check_normalize_spaces(normalize_spaces)


def test_check_normalize_spaces_rejects_bugs():
    for buggy in [normalize_strip_only, normalize_spaces_only, normalize_no_strip]:
        assert not check_normalize_spaces(buggy), buggy.__name__


def test_count_pairs():
    for count_pairs in [count_pairs_slow, count_pairs_fast]:
        assert count_pairs([], 5) == 0
        assert count_pairs([1, 2, 3, 4], 5) == 2
        assert count_pairs([2, 2, 2], 4) == 3
        assert count_pairs([1, -1, 0, 0], 0) == 2


def test_agree():
    assert agree(500, 3300)


def test_word_counts():
    assert word_counts("The cat saw the CAT.") == {"the": 2, "cat": 2, "saw": 1}
    assert word_counts("Wait -- what?! ...") == {"wait": 1, "--": 1, "what": 1}
    assert word_counts("") == {}
