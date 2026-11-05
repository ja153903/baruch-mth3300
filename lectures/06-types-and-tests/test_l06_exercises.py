from l06_exercises import clamp, is_passing


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-3, 0, 10) == 0
    assert clamp(42, 0, 10) == 10
    assert clamp(10, 0, 10) == 10


def test_is_passing():
    assert is_passing(60)
    assert not is_passing(59.9)


# TODO (in class): add one more test for each function.
