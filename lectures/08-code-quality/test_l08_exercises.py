from l08_exercises import (
    absolute,
    grade_points,
    is_valid_ticker,
    minutes_late,
    next_business_day,
    parking_fee,
    ticket_price,
    with_tax,
)


def test_absolute():
    assert absolute(5) == 5
    assert absolute(0) == 0
    assert absolute(-5) == 5


def test_ticket_price():
    assert ticket_price(5) == 8
    assert ticket_price(11) == 8
    assert ticket_price(12) == 14
    assert ticket_price(64) == 14
    assert ticket_price(65) == 9


def test_is_valid_ticker():
    assert is_valid_ticker("AAPL")
    assert is_valid_ticker("F")
    assert not is_valid_ticker("aapl")
    assert not is_valid_ticker("GOOGLE")
    assert not is_valid_ticker("BRK.B")
    assert not is_valid_ticker("")


def test_next_business_day():
    assert next_business_day(0) == 1
    assert next_business_day(3) == 4
    assert next_business_day(4) == 0
    assert next_business_day(5) == 0
    assert next_business_day(6) == 0


def test_grade_points():
    assert grade_points("A") == 4
    assert grade_points("b") == 3
    assert grade_points("D") == 1
    assert grade_points("F") == 0


def test_parking_fee():
    assert parking_fee(0.5) == 5
    assert parking_fee(1) == 5
    assert parking_fee(1.25) == 8
    assert parking_fee(2.5) == 11
    assert parking_fee(10) == 20


def test_with_tax():
    assert with_tax(200) == 217.75
    assert with_tax(19.99) == 21.76
    assert with_tax(0) == 0


def test_minutes_late():
    assert minutes_late("08:15", "08:42") == 27
    assert minutes_late("10:50", "11:05") == 15
    assert minutes_late("09:00", "08:55") == 0
    assert minutes_late("23:10", "23:10") == 0
