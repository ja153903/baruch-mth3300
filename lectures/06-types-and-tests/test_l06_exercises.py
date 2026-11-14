import math

from l06_exercises import (
    average_rating,
    break_even_units,
    cagr,
    clamp,
    continuous_growth,
    is_passing,
    quarter,
    round_up_to,
    shift_hours,
)


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-3, 0, 10) == 0
    assert clamp(42, 0, 10) == 10
    assert clamp(10, 0, 10) == 10


def test_is_passing():
    assert is_passing(60)
    assert not is_passing(59.9)


def test_shift_hours():
    assert shift_hours(9, 17) == 8
    assert shift_hours(22, 6) == 8
    assert shift_hours(9, 9) == 0


def test_quarter():
    assert quarter(1) == 1
    assert quarter(3) == 1
    assert quarter(4) == 2
    assert quarter(12) == 4


def test_break_even_units():
    assert break_even_units(1000, 15, 5) == 100
    assert break_even_units(1001, 15, 5) == 101
    assert break_even_units(0, 15, 5) == 0


def test_cagr():
    assert math.isclose(cagr(100, 121, 2), 0.1)
    assert math.isclose(cagr(1000, 2000, 10), 0.07177346253629313)
    assert cagr(100, 100, 5) == 0


def test_average_rating():
    assert average_rating(47, 10) == 4.7
    assert average_rating(10, 3) == 3.3
    assert average_rating(5, 1) == 5


def test_round_up_to():
    assert round_up_to(1234, 100) == 1300
    assert round_up_to(1200, 100) == 1200
    assert round_up_to(0.01, 0.25) == 0.25


def test_continuous_growth():
    assert math.isclose(continuous_growth(1000, 0.05, 10), 1648.7212707001281)
    assert continuous_growth(1000, 0.05, 0) == 1000
    assert continuous_growth(0, 0.05, 10) == 0


# TODO (in class): add one more test for each function.
