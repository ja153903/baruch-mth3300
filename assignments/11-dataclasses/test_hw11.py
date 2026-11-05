import math

import pytest

from hw11 import Account, Point, area


def test_distance_to():
    assert Point(0, 0).distance_to(Point(3, 4)) == 5
    assert Point(1, 1).distance_to(Point(1, 1)) == 0


def test_point_is_frozen():
    p = Point(1, 2)
    with pytest.raises(AttributeError):
        p.x = 5  # ty: ignore[invalid-assignment]


def test_account():
    acct = Account("Ada")
    assert acct.balance == 0
    acct.deposit(100)
    acct.withdraw(30)
    assert acct.balance == 70


def test_account_rejects_bad_amounts():
    acct = Account("Ada", 50)
    with pytest.raises(ValueError):
        acct.deposit(0)
    with pytest.raises(ValueError):
        acct.withdraw(-5)
    with pytest.raises(ValueError):
        acct.withdraw(51)
    assert acct.balance == 50


def test_area():
    assert math.isclose(area(("circle", 1)), math.pi)
    assert area(("rectangle", 3, 4)) == 12
    assert area(("triangle", 3, 4)) == 6
    with pytest.raises(ValueError):
        area(("hexagon", 1))
