import math

import p_basics as b


def test_minutes_in_a_year():
    assert b.minutes_in_a_year == 525_600


def test_fahrenheit():
    assert b.fahrenheit is not None
    assert math.isclose(b.fahrenheit, 86)


def test_dollars_and_cents():
    assert b.dollars == 12
    assert b.cents == 34


def test_balance():
    assert b.balance is not None
    assert math.isclose(b.balance, 5000 * 1.04**7)


def test_hours_and_minutes():
    assert b.whole_hours == 7
    assert b.leftover_minutes is not None
    assert math.isclose(b.leftover_minutes, 45)


def test_average():
    assert b.average == 87.5
