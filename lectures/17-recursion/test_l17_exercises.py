import pytest

from l17_exercises import (
    count_char,
    count_digits,
    countdown_list,
    digit_sum,
    fast_power,
    max_value,
    power,
    reverse,
    subsets,
)


def test_digit_sum():
    assert digit_sum(3300) == 6
    assert digit_sum(98765) == 35
    assert digit_sum(7) == 7
    assert digit_sum(0) == 0


def test_countdown_list():
    assert countdown_list(3) == [3, 2, 1]
    assert countdown_list(1) == [1]
    assert countdown_list(0) == []


def test_power():
    assert power(2, 0) == 1
    assert power(2, 10) == 1024
    assert power(1.5, 2) == 2.25


def test_reverse():
    assert reverse("") == ""
    assert reverse("a") == "a"
    assert reverse("baruch") == "hcurab"


def test_count_char():
    assert count_char("mississippi", "s") == 4
    assert count_char("baruch", "z") == 0
    assert count_char("", "a") == 0


def test_max_value():
    assert max_value([3, 9, 4]) == 9
    assert max_value([-5, -2, -8]) == -2
    assert max_value([7]) == 7


def test_count_digits():
    assert count_digits(3300) == 4
    assert count_digits(7) == 1
    assert count_digits(0) == 1


def test_fast_power():
    assert fast_power(2, 10) == 1024
    assert fast_power(1.5, 3) == 3.375
    assert fast_power(3, 0) == 1
    # Too deep for one call per step, but fine for about 13 calls.
    assert fast_power(1.001, 5000) == pytest.approx(1.001**5000)


def normalize(sets: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(s) for s in sets)


def test_subsets():
    assert normalize(subsets([1, 2])) == [[], [1], [1, 2], [2]]
    assert normalize(subsets([3, 1, 2])) == [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 3],
        [2],
        [2, 3],
        [3],
    ]
    assert subsets([]) == [[]]
    assert len(subsets(list(range(10)))) == 1024
