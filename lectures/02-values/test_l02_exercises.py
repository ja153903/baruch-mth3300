import math

import l02_exercises as ex


def test_fahrenheit():
    assert ex.fahrenheit is not None
    assert math.isclose(ex.fahrenheit, 98.6)


def test_last_digit():
    assert ex.last_digit == 0
