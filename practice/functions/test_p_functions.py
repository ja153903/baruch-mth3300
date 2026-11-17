import math

from p_functions import (
    boxes_needed,
    celsius_to_fahrenheit,
    circle_circumference,
    format_price,
    mask_card,
    seconds_to_hms,
    tip_amount,
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(-40) == -40


def test_tip_amount():
    assert tip_amount(50) == 9
    assert tip_amount(50, 0.2) == 10
    assert tip_amount(23.45) == 4.22
    assert tip_amount(80, rate=0) == 0


def test_boxes_needed():
    assert boxes_needed(100, 12) == 9
    assert boxes_needed(96, 12) == 8
    assert boxes_needed(1, 12) == 1


def test_seconds_to_hms():
    assert seconds_to_hms(3723) == "1:02:03"
    assert seconds_to_hms(59) == "0:00:59"
    assert seconds_to_hms(36000) == "10:00:00"


def test_format_price():
    assert format_price(1234.5) == "$1,234.50"
    assert format_price(0.5) == "$0.50"
    assert format_price(1_000_000) == "$1,000,000.00"


def test_mask_card():
    assert mask_card("4111222233334444") == "**** 4444"
    assert mask_card("1234") == "**** 1234"


def test_circle_circumference():
    assert math.isclose(circle_circumference(1), 2 * math.pi)
    assert math.isclose(circle_circumference(3), 6 * math.pi)
