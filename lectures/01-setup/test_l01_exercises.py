import math

import l01_exercises as ex


def test_greeting():
    assert ex.greeting == "Hello, MTH 3300!"


def test_minutes_in_a_day():
    assert ex.minutes_in_a_day == 1440


def test_file_path():
    assert ex.file_path == "lectures/01-setup/notes.md"


def test_total_with_tax():
    assert ex.total_with_tax is not None
    assert math.isclose(ex.total_with_tax, 27.2078625)


def test_percent_change():
    assert ex.percent_change is not None
    assert math.isclose(ex.percent_change, 15)


def test_grains_on_last_square():
    assert ex.grains_on_last_square is not None
    assert ex.grains_on_last_square != 2**64, "square 1 has 2**0 grains, not 2**1"
    assert ex.grains_on_last_square == 9_223_372_036_854_775_808


def test_midpoint():
    assert ex.midpoint == 15


def test_larger_root():
    assert ex.larger_root is not None
    assert math.isclose(ex.larger_root, 3)


def test_monthly_balance():
    assert ex.monthly_balance is not None
    assert math.isclose(ex.monthly_balance, 1061.6778118644984)
