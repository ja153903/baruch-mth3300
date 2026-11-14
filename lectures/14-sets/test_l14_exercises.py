import pytest

from l14_exercises import (
    can_spell,
    common_elements,
    duplicates,
    has_duplicates,
    jaccard,
    missing_numbers,
    most_traded,
    unique_in_order,
)


def test_has_duplicates():
    assert not has_duplicates([])
    assert not has_duplicates([1, 2, 3])
    assert has_duplicates([1, 2, 1])


def test_missing_numbers():
    assert missing_numbers([4, 1, 2], 5) == [3, 5]
    assert missing_numbers([1, 2, 3], 3) == []
    assert missing_numbers([], 2) == [1, 2]


def test_common_elements():
    assert common_elements([3, 1, 2, 3], [3, 4, 1]) == [1, 3]
    assert common_elements([1], [2]) == []


def test_jaccard():
    assert jaccard({"AAPL", "MSFT"}, {"MSFT", "NVDA"}) == pytest.approx(1 / 3)
    assert jaccard({"AAPL"}, {"AAPL"}) == 1.0
    assert jaccard({"AAPL"}, {"TSLA"}) == 0.0
    assert jaccard(set(), set()) == 1.0


def test_most_traded():
    trades = ["MSFT", "AAPL", "NVDA", "AAPL", "MSFT", "AAPL"]
    assert most_traded(trades, 2) == ["AAPL", "MSFT"]
    assert most_traded(["NVDA", "TSLA", "TSLA", "NVDA"], 1) == ["NVDA"]
    assert most_traded([], 3) == []


def test_duplicates():
    assert duplicates([3, 1, 3, 2, 1, 3]) == [1, 3]
    assert duplicates([1, 2, 3]) == []
    assert duplicates([]) == []


def test_unique_in_order():
    assert unique_in_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert unique_in_order([5, 5, 5]) == [5]
    assert unique_in_order([]) == []


def test_can_spell():
    assert can_spell("pass", "sapsx")
    assert not can_spell("pass", "pas")
    assert can_spell("", "abc")
    assert not can_spell("a", "")
