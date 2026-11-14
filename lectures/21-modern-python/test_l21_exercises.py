import pytest

from l21_exercises import (
    Buy,
    Dividend,
    Grade,
    LimitOrder,
    Order,
    Sell,
    calculate,
    cash_change,
    counts_toward_gpa,
    describe,
    describe_order,
    last,
    money,
    parse_grade,
)


def test_describe():
    assert describe([]) == "empty"
    assert describe([1]) == "one item"
    assert describe([1, 2, 3]) == "many items"
    assert describe((3, 4)) == "point at 3, 4"
    assert describe("hi") == "unknown"


def test_calculate():
    assert calculate(("add", 2, 3)) == 5
    assert calculate(("mul", 2, 3)) == 6
    assert calculate(("neg", 4)) == -4
    with pytest.raises(ValueError):
        calculate(("pow", 2, 3))


def test_parse_grade():
    assert parse_grade("pass") is Grade.PASS
    assert parse_grade(" FAIL ") is Grade.FAIL
    assert parse_grade("Incomplete") is Grade.INCOMPLETE
    with pytest.raises(ValueError):
        parse_grade("A+")


def test_counts_toward_gpa():
    assert counts_toward_gpa(Grade.PASS)
    assert counts_toward_gpa(Grade.FAIL)
    assert not counts_toward_gpa(Grade.INCOMPLETE)


def test_last():
    assert last([1, 2, 3]) == 3
    assert last(["a"]) == "a"
    assert last([]) is None


def test_money():
    name = "Ada"
    shares = 10
    price = 190.5
    assert money(t"{name} bought {shares} at {price}") == "Ada bought 10 at $190.50"
    total = 1234.5
    assert money(t"Total: {total}") == "Total: $1,234.50"
    assert money(t"no values") == "no values"


def test_cash_change():
    assert cash_change(Buy("AAPL", 10, 190.5)) == -1905.0
    assert cash_change(Sell("AAPL", 4, 200.0)) == 800.0
    assert cash_change(Dividend("MSFT", 12.5)) == 12.5
    assert cash_change(Buy("NVDA", 0, 120.0)) == 0


def test_describe_order():
    assert describe_order(Order("AAPL", 10)) == "buy 10 AAPL at market"
    limit = LimitOrder("AAPL", 10, 185.0)
    assert describe_order(limit) == "buy 10 AAPL at 185.0 or less"
    one = LimitOrder("MSFT", 1, 400.5)
    assert describe_order(one) == "buy 1 MSFT at 400.5 or less"
