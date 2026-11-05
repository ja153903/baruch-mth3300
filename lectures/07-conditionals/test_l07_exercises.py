from l07_exercises import is_even, max_of_three


def test_is_even():
    assert is_even(0)
    assert is_even(-4)
    assert not is_even(7)


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(3, 2, 1) == 3
    assert max_of_three(2, 3, 1) == 3
    assert max_of_three(5, 5, 1) == 5
