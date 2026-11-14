import math

import l02_exercises as ex


def test_fahrenheit():
    assert ex.fahrenheit is not None
    assert math.isclose(ex.fahrenheit, 98.6)


def test_last_digit():
    assert ex.last_digit == 0


def test_hundreds_digit():
    assert ex.hundreds_digit == 4


def test_order_total():
    assert ex.order_total is not None
    assert math.isclose(ex.order_total, 59.97)


def test_price_range():
    assert ex.price_range is not None
    assert math.isclose(ex.price_range, 3.75)


def test_making_change():
    assert ex.quarters == 3
    assert ex.dimes == 1
    assert ex.nickels == 0
    assert ex.pennies == 2


def test_price_in_cents():
    assert ex.price_in_cents == 450
    assert isinstance(ex.price_in_cents, int), "a number of cents should be an int"


def test_nickel_price():
    assert ex.nickel_price is not None
    assert math.isclose(ex.nickel_price, 4.95)


def test_future_weekday():
    assert ex.future_weekday == 6
