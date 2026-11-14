import pytest

from l12_exercises import (
    best_performers,
    flatten,
    in_batches,
    longest_streak,
    min_max,
    pairwise_sums,
    period_returns,
    squares_of_evens,
    total_value,
)


def test_min_max():
    assert min_max([3, 9, 1]) == (1, 9)
    assert min_max([-2, -8, 0]) == (-8, 0)
    assert min_max([5]) == (5, 5)


def test_squares_of_evens():
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]
    assert squares_of_evens([0, -2]) == [0, 4]
    assert squares_of_evens([1, 3, 5]) == []


def test_pairwise_sums():
    assert pairwise_sums([1, 2, 3], [10, 20, 30]) == [11, 22, 33]
    assert pairwise_sums([], []) == []
    with pytest.raises(ValueError):
        pairwise_sums([1, 2], [1])


def test_flatten():
    assert flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []


def test_period_returns():
    assert period_returns([100.0, 110.0, 99.0]) == pytest.approx([0.1, -0.1])
    assert period_returns([100.0]) == []
    assert period_returns([]) == []


def test_in_batches():
    assert in_batches(["AAPL", "MSFT", "NVDA"], 2) == [["AAPL", "MSFT"], ["NVDA"]]
    assert in_batches(["AAPL", "MSFT"], 2) == [["AAPL", "MSFT"]]
    assert in_batches([], 2) == []


def test_total_value():
    assert total_value([10, 5], [190.5, 410.25]) == 3956.25
    assert total_value([], []) == 0
    with pytest.raises(ValueError):
        total_value([10, 5, 8], [190.5, 410.25])


def test_longest_streak():
    assert longest_streak([1.0, 2.0, 3.0, 2.0, 3.0, 4.0, 5.0]) == 3
    assert longest_streak([1.0, 1.0, 2.0]) == 1
    assert longest_streak([5.0, 4.0, 3.0]) == 0
    assert longest_streak([100.0]) == 0


def test_best_performers():
    assert best_performers(["A", "B", "C"], [0.05, 0.12, -0.02], 2) == ["B", "A"]
    assert best_performers(["X", "Y", "Z"], [0.3, 0.1, 0.2], 5) == ["X", "Z", "Y"]
    assert best_performers(["A", "B"], [0.01, 0.02], 0) == []
