from l11_exercises import remove_all, rotate


def test_rotate():
    assert rotate([1, 2, 3, 4], 1) == [2, 3, 4, 1]
    assert rotate([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    assert rotate([1, 2, 3, 4], 4) == [1, 2, 3, 4]


def test_remove_all():
    xs = [1, 2, 1, 3, 1]
    assert remove_all(xs, 1) == [2, 3]
    assert xs == [1, 2, 1, 3, 1]
    assert remove_all([], 1) == []
