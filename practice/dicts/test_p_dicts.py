import pytest

from p_dicts import invert_unique, most_frequent, two_sum_indices


def test_most_frequent():
    assert most_frequent([3, 1, 3, 2]) == 3
    assert most_frequent([2, 1, 2, 1]) == 1


def test_invert_unique():
    assert invert_unique({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    with pytest.raises(ValueError):
        invert_unique({"a": 1, "b": 1})


def test_two_sum_indices():
    assert two_sum_indices([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_indices([3, 2, 4], 6) == (1, 2)
    assert two_sum_indices([1, 2], 10) is None
