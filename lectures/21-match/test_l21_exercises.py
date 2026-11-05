import pytest

from l21_exercises import calculate, describe


def test_describe():
    assert describe([]) == "empty"
    assert describe([1]) == "one item"
    assert describe([1, 2, 3]) == "many items"
    assert describe((3, 4)) == "point at 3, 4"
    assert describe("hi") == "unknown"


def test_calculate():
    assert calculate(("add", 2, 3)) == 5
    assert calculate(("mul", 2, 3)) == 6
    assert calculate(("neg", 4)) == -4
    with pytest.raises(ValueError):
        calculate(("pow", 2, 3))
