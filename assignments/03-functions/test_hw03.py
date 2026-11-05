import math

from hw03 import circle_area, digit_sum, is_leap_year


def test_circle_area():
    assert circle_area(0) == 0
    assert math.isclose(circle_area(1), math.pi)
    assert math.isclose(circle_area(2), 4 * math.pi)


def test_is_leap_year():
    assert is_leap_year(2024)
    assert not is_leap_year(2023)
    assert not is_leap_year(1900)
    assert is_leap_year(2000)


def test_digit_sum():
    assert digit_sum(0) == 0
    assert digit_sum(7) == 7
    assert digit_sum(3300) == 6
    assert digit_sum(98765) == 35
