from hw06 import evens, moving_average, running_total


def test_running_total():
    assert running_total([]) == []
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([5, -5, 5]) == [5, 0, 5]


def test_evens():
    assert evens([]) == []
    assert evens([1, 2, 3, 4, 6, 7]) == [2, 4, 6]
    assert evens([-2, -1, 0]) == [-2, 0]


def test_moving_average():
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    assert moving_average([1, 2, 3, 4], 4) == [2.5]
    assert moving_average([1, 2, 3], 1) == [1, 2, 3]
    assert moving_average([1, 2], 3) == []


def test_inputs_not_modified():
    xs: list[float] = [3, 1, 2]
    running_total(xs)
    moving_average(xs, 2)
    assert xs == [3, 1, 2]
