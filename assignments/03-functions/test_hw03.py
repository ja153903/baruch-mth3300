import math

from hw03 import circle_area, split_bill, sum_of_three_digits


def test_circle_area():
    assert circle_area(0) == 0
    assert math.isclose(circle_area(1), math.pi)
    assert math.isclose(circle_area(2), 4 * math.pi)


def test_split_bill():
    assert split_bill(100, 4) == 29.5
    assert split_bill(100, 4, tip_rate=0.2) == 30
    assert split_bill(60, 1, 0) == 60
    assert split_bill(10, 3) == 3.93


def test_sum_of_three_digits():
    assert sum_of_three_digits(472) == 13
    assert sum_of_three_digits(100) == 1
    assert sum_of_three_digits(999) == 27
