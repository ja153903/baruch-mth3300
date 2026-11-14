import math

from l07_exercises import (
    commission,
    count_real_roots,
    is_even,
    late_fee,
    max_of_three,
    median_of_three,
    price_signal,
    quadrant,
    trade_allowed,
)


def test_is_even():
    assert is_even(0)
    assert is_even(-4)
    assert not is_even(7)


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(3, 2, 1) == 3
    assert max_of_three(2, 3, 1) == 3
    assert max_of_three(5, 5, 1) == 5


def test_trade_allowed():
    assert trade_allowed(1000, 37.5, 26)
    assert not trade_allowed(1000, 37.5, 27)
    assert trade_allowed(100, 25, 4)
    assert not trade_allowed(1000, 37.5, 0)


def test_commission():
    assert commission(999) == 5
    assert math.isclose(commission(1000), 10)
    assert math.isclose(commission(10_000), 100)
    assert math.isclose(commission(20_000), 100)


def test_price_signal():
    assert price_signal(90, 100) == "buy"
    assert price_signal(110, 100) == "sell"
    assert price_signal(100, 100) == "hold"
    assert price_signal(95, 100) == "hold"
    assert price_signal(105, 100) == "hold"


def test_quadrant():
    assert quadrant(1, 1) == 1
    assert quadrant(-1, 1) == 2
    assert quadrant(-2, -3) == 3
    assert quadrant(2, -3) == 4
    assert quadrant(0, 5) == 0
    assert quadrant(5, 0) == 0


def test_late_fee():
    assert late_fee(0) == 0
    assert late_fee(1) == 25
    assert late_fee(30) == 25
    assert late_fee(31) == 40


def test_median_of_three():
    assert median_of_three(1, 2, 3) == 2
    assert median_of_three(3, 1, 2) == 2
    assert median_of_three(2, 3, 1) == 2
    assert median_of_three(5, 5, 1) == 5
    assert median_of_three(4, 4, 4) == 4


def test_count_real_roots():
    assert count_real_roots(1, -3, 2) == 2
    assert count_real_roots(1, 2, 1) == 1
    assert count_real_roots(1, 0, 1) == 0
