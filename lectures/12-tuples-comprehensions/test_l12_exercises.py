import pytest

from l12_exercises import flatten, pairwise_sums


def test_pairwise_sums():
    assert pairwise_sums([1, 2, 3], [10, 20, 30]) == [11, 22, 33]
    assert pairwise_sums([], []) == []
    with pytest.raises(ValueError):
        pairwise_sums([1, 2], [1])


def test_flatten():
    assert flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
