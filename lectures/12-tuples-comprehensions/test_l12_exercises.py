import pytest

from l12_exercises import flatten, in_batches, pairwise_sums, period_returns


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
