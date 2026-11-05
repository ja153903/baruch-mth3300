from collections.abc import Callable

import pytest

from hw13 import TEST_CASES, from_roman, to_roman


def test_to_roman():
    assert to_roman(1) == "I"
    assert to_roman(4) == "IV"
    assert to_roman(9) == "IX"
    assert to_roman(14) == "XIV"
    assert to_roman(40) == "XL"
    assert to_roman(90) == "XC"
    assert to_roman(400) == "CD"
    assert to_roman(1994) == "MCMXCIV"
    assert to_roman(2026) == "MMXXVI"
    assert to_roman(3999) == "MMMCMXCIX"


def test_to_roman_out_of_range():
    for n in [0, -5, 4000]:
        with pytest.raises(ValueError):
            to_roman(n)


def test_from_roman():
    assert from_roman("I") == 1
    assert from_roman("XIV") == 14
    assert from_roman("MCMXCIV") == 1994
    assert from_roman("MMMCMXCIX") == 3999


def test_from_roman_invalid():
    for bad in ["", "ABC", "x"]:
        with pytest.raises(ValueError):
            from_roman(bad)


def test_round_trip():
    for n in range(1, 4000):
        assert from_roman(to_roman(n)) == n


# Your TEST_CASES


def test_enough_cases():
    assert len(TEST_CASES) >= 8, "write at least 8 TEST_CASES"


def test_cases_are_correct():
    for n, numeral in TEST_CASES:
        assert to_roman(n) == numeral, f"TEST_CASES has ({n}, {numeral!r})"


# Each buggy version is built from your (correct) to_roman, then broken in one way.
BUGGY_VERSIONS: dict[str, Callable[[int], str]] = {
    "writes 4 as IIII": lambda n: to_roman(n).replace("IV", "IIII"),
    "writes 9 as VIIII": lambda n: to_roman(n).replace("IX", "VIIII"),
    "writes 40 as XXXX": lambda n: to_roman(n).replace("XL", "XXXX"),
    "writes 90 as LXXXX": lambda n: to_roman(n).replace("XC", "LXXXX"),
    "writes 400 as CCCC": lambda n: to_roman(n).replace("CD", "CCCC"),
    "writes 900 as DCCCC": lambda n: to_roman(n).replace("CM", "DCCCC"),
    "drops an M above 2000": lambda n: to_roman(n).replace("MM", "M", 1),
}


@pytest.mark.parametrize("bug", BUGGY_VERSIONS)
def test_cases_catch_bug(bug: str):
    buggy = BUGGY_VERSIONS[bug]
    caught = any(buggy(n) != numeral for n, numeral in TEST_CASES)
    assert caught, f"none of your TEST_CASES catches a to_roman that {bug}"
