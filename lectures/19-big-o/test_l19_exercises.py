from l19_exercises import (
    common_count,
    has_pair_with_sum,
    is_sorted,
    max_profit,
    max_profit_slow,
    nearby_duplicate,
    new_highs,
    range_sums,
)


def test_is_sorted():
    assert is_sorted([])
    assert is_sorted([1, 1, 2])
    assert not is_sorted([2, 1])


def test_common_count():
    assert common_count([1, 2, 2, 5], [2, 3, 5]) == 3
    assert common_count([1, 2], [3, 4]) == 0
    assert common_count([], [1]) == 0
    big = list(range(20_000))
    assert common_count(big, big) == 20_000  # O(n * m) takes seconds here


def test_has_pair_with_sum():
    assert has_pair_with_sum([1, 4, 6, 9], 10)
    assert not has_pair_with_sum([1, 4, 6, 9], 2)
    assert not has_pair_with_sum([5], 10)
    assert has_pair_with_sum([5, 5], 10)
    assert has_pair_with_sum(list(range(200_000)), 399_997)


def test_new_highs():
    assert new_highs([10.0, 12.0, 11.0, 13.0, 13.0]) == 3
    assert new_highs([1.0, 2.0, 3.0]) == 3
    assert new_highs([5.0, 4.0, 3.0]) == 1
    assert new_highs([]) == 0


def test_max_profit_slow():
    assert max_profit_slow([7.0, 1.0, 5.0, 3.0, 6.0, 4.0]) == 5.0
    assert max_profit_slow([5.0, 4.0, 3.0]) == 0
    assert max_profit_slow([4.0]) == 0
    assert max_profit_slow([]) == 0


def test_max_profit():
    assert max_profit([7.0, 1.0, 5.0, 3.0, 6.0, 4.0]) == 5.0
    assert max_profit([5.0, 4.0, 3.0]) == 0
    assert max_profit([]) == 0
    falling = [float(p) for p in range(20_000, 10_000, -1)]
    assert max_profit([*falling, 25_000.0]) == 14_999  # O(n²) takes seconds here


def test_range_sums():
    xs = [3, 1, 4, 1, 5, 9, 2, 6]
    assert range_sums(xs, [(0, 3), (2, 5), (0, 8)]) == [8, 10, 31]
    assert range_sums(xs, [(4, 4)]) == [0]
    assert range_sums([], []) == []
    big = list(range(100_000))
    assert range_sums(big, [(0, 100_000)] * 5_000) == [sum(big)] * 5_000


def test_nearby_duplicate():
    assert nearby_duplicate([1, 2, 3, 1], 3)
    assert not nearby_duplicate([1, 2, 3, 1], 2)
    assert nearby_duplicate([5, 5], 1)
    assert not nearby_duplicate([1, 2, 1], 0)
    assert not nearby_duplicate([], 5)
