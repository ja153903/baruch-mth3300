from dataclasses import is_dataclass

import pytest

from l20_exercises import (
    Bond,
    Cart,
    CartItem,
    CurvedGradebook,
    Gradebook,
    Money,
    Rectangle,
    Tally,
    Watchlist,
)


def test_tally():
    assert not is_dataclass(Tally)
    t = Tally()
    assert t.total() == 0
    t.click()
    t.click()
    assert t.total() == 2
    t.reset()
    assert t.total() == 0


def test_gradebook_is_hand_written():
    assert not is_dataclass(Gradebook)


def test_gradebook():
    g = Gradebook("MTH 3300")
    g.add(80)
    g.add(90)
    g.add(100)
    assert g.average() == 90
    assert repr(g) == "Gradebook('MTH 3300', 3 scores)"


def test_gradebook_rejects_bad_input():
    g = Gradebook("MTH 3300")
    with pytest.raises(ValueError):
        g.average()
    with pytest.raises(ValueError):
        g.add(101)
    with pytest.raises(ValueError):
        g.add(-1)
    assert repr(g) == "Gradebook('MTH 3300', 0 scores)"


def test_gradebooks_are_independent():
    a, b = Gradebook("A"), Gradebook("B")
    a.add(50)
    assert repr(b) == "Gradebook('B', 0 scores)"


def test_curved_gradebook():
    g = CurvedGradebook("MTH 3300", curve=5)
    assert isinstance(g, Gradebook)
    g.add(80)
    g.add(90)
    assert g.average() == 90
    g.add(100)
    g.add(100)
    assert g.average() == 97.5
    assert repr(g) == "Gradebook('MTH 3300', 4 scores)"


def test_curve_caps_at_100():
    g = CurvedGradebook("MTH 3300", curve=10)
    g.add(95)
    assert g.average() == 100


def test_area_and_perimeter():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14


def test_scale():
    r = Rectangle(3, 4)
    r.scale(2)
    assert r == Rectangle(6, 8)


def test_bond():
    b = Bond(1000.0, 0.05)
    assert b.annual_coupon() == 50.0
    assert b.with_rate(0.06) == Bond(1000.0, 0.06)
    assert b == Bond(1000.0, 0.05)
    assert Bond(500.0, 0.0).annual_coupon() == 0


def test_cart():
    cart = Cart()
    assert cart.total() == 0
    assert cart.count() == 0
    cart.add("bagel", 2.5, 2)
    cart.add("coffee", 3.0)
    assert cart.total() == 8.0
    assert cart.count() == 3
    assert cart.items[1] == CartItem("coffee", 3.0, 1)
    assert Cart().items == []


def test_watchlist():
    mine = ["MSFT"]
    tech = Watchlist("tech", mine)
    tech.add("nvda")
    assert tech.tickers == ["MSFT", "NVDA"]
    assert mine == ["MSFT"]
    empty = Watchlist("empty", [])
    assert empty.tickers == []


def test_money():
    assert Money(123456).dollars() == "$1,234.56"
    assert Money(5).dollars() == "$0.05"
    assert Money(0).dollars() == "$0.00"
    assert Money(150) + Money(275) == Money(425)
    assert Money(100).split(3) == [Money(34), Money(33), Money(33)]
    assert Money(10).split(5) == [Money(2)] * 5
    assert sum(part.cents for part in Money(1001).split(4)) == 1001
