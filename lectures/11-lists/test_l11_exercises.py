import pytest

from l11_exercises import (
    apply_split,
    column,
    last_n,
    max_drawdown,
    price_range,
    remove_all,
    rotate,
    top_three,
    transpose,
)


def test_last_n():
    assert last_n([1, 2, 3, 4], 2) == [3, 4]
    assert last_n([1, 2, 3, 4], 0) == []
    assert last_n([1, 2], 5) == [1, 2]


def test_price_range():
    assert price_range([101.5, 99.0, 103.25]) == 4.25
    assert price_range([3.0, 1.0, 2.0]) == 2.0
    assert price_range([50.0]) == 0


def test_rotate():
    assert rotate([1, 2, 3, 4], 1) == [2, 3, 4, 1]
    assert rotate([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    assert rotate([1, 2, 3, 4], 4) == [1, 2, 3, 4]


def test_remove_all():
    xs = [1, 2, 1, 3, 1]
    assert remove_all(xs, 1) == [2, 3]
    assert xs == [1, 2, 1, 3, 1]
    assert remove_all([], 1) == []


def test_apply_split():
    xs = [10, 5, 8]
    assert apply_split(xs, 2) is None
    assert xs == [20, 10, 16]
    empty: list[int] = []
    apply_split(empty, 3)
    assert empty == []


def test_column():
    table = [[1, 2, 3], [4, 5, 6]]
    assert column(table, 0) == [1, 4]
    assert column(table, 2) == [3, 6]
    assert column([], 0) == []


def test_top_three():
    scores = [70, 95, 88, 60]
    assert top_three(scores) == [95, 88, 70]
    assert scores == [70, 95, 88, 60]
    assert top_three([5, 9]) == [9, 5]


def test_max_drawdown():
    assert max_drawdown([100.0, 120.0, 90.0, 130.0, 117.0]) == pytest.approx(0.25)
    assert max_drawdown([100.0, 80.0, 60.0]) == pytest.approx(0.4)
    assert max_drawdown([1.0, 2.0, 3.0]) == 0
    assert max_drawdown([50.0]) == 0


def test_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[1, 2]]) == [[1], [2]]
    assert transpose([[7]]) == [[7]]
