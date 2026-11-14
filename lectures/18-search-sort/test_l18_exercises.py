import random

from l18_exercises import (
    bubble_sort,
    closest,
    count_inversions,
    count_occurrences,
    insertion_sort,
    last_index,
    sort_by_value,
    two_sum_sorted,
)


def test_count_occurrences():
    assert count_occurrences([], 1) == 0
    assert count_occurrences([1, 2, 1, 1], 1) == 3


def test_last_index():
    assert last_index([4, 2, 4, 1], 4) == 2
    assert last_index([4, 2, 4, 1], 1) == 3
    assert last_index([4, 2, 4, 1], 7) == -1
    assert last_index([], 1) == -1


def test_insertion_sort():
    rng = random.Random(18)
    for _ in range(30):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 20))]
        original = list(xs)
        assert insertion_sort(xs) == sorted(xs)
        assert xs == original


def test_sort_by_value():
    holdings = {"NVDA": 960.0, "AAPL": 2286.0, "TSLA": 2051.25, "MSFT": 2051.25}
    assert sort_by_value(holdings) == ["AAPL", "MSFT", "TSLA", "NVDA"]
    assert sort_by_value({"A": 1.0}) == ["A"]
    assert sort_by_value({}) == []


def test_count_inversions():
    assert count_inversions([3, 1, 2]) == 2
    assert count_inversions([4, 3, 2, 1]) == 6
    assert count_inversions([1, 2, 3]) == 0
    assert count_inversions([2, 2]) == 0
    assert count_inversions([]) == 0


def test_closest():
    xs = [1, 4, 9, 16]
    assert closest(xs, 10) == 9
    assert closest(xs, 13) == 16
    assert closest(xs, 0) == 1
    assert closest(xs, 100) == 16
    assert closest([10, 20], 15) == 10
    assert closest([5], 5) == 5


def test_bubble_sort():
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert bubble_sort([]) == []
    xs = [3, 2, 1]
    bubble_sort(xs)
    assert xs == [3, 2, 1]


def test_two_sum_sorted():
    assert two_sum_sorted([1, 4, 6, 9], 10)
    assert not two_sum_sorted([1, 4, 6, 9], 12)  # 6 + 6 would use one position twice
    assert two_sum_sorted([3, 3], 6)
    assert not two_sum_sorted([5], 10)
    assert not two_sum_sorted([], 0)
