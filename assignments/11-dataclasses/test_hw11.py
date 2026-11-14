import math
from dataclasses import is_dataclass

import pytest

from hw11 import Account, Circle, Point, Rectangle, SavingsAccount, Triangle, area


def test_account_is_hand_written():
    assert not is_dataclass(Account)


def test_account():
    acct = Account("Ada")
    assert acct.balance == 0
    acct.deposit(100)
    acct.withdraw(30)
    assert acct.balance == 70
    assert acct.owner == "Ada"


def test_account_repr():
    assert repr(Account("Ada", 70)) == "Account('Ada', 70.00)"
    assert repr(Account("Grace")) == "Account('Grace', 0.00)"


def test_account_rejects_bad_amounts():
    acct = Account("Ada", 50)
    with pytest.raises(ValueError):
        acct.deposit(0)
    with pytest.raises(ValueError):
        acct.withdraw(-5)
    with pytest.raises(ValueError):
        acct.withdraw(51)
    assert acct.balance == 50


def test_accounts_are_independent():
    a, b = Account("A"), Account("B")
    a.deposit(10)
    assert b.balance == 0


def test_savings_is_an_account():
    s = SavingsAccount("Ada", 100)
    assert isinstance(s, Account)
    s.deposit(50)
    assert s.balance == 150


def test_savings_interest():
    s = SavingsAccount("Ada", 1000, rate=0.05)
    s.add_interest()
    assert math.isclose(s.balance, 1050)
    assert math.isclose(SavingsAccount("Ada", 100).rate, 0.02)


def test_savings_allows_three_withdrawals():
    s = SavingsAccount("Ada", 100)
    s.withdraw(10)
    s.withdraw(10)
    s.withdraw(10)
    with pytest.raises(ValueError):
        s.withdraw(10)
    assert s.balance == 70


def test_savings_keeps_account_rules():
    s = SavingsAccount("Ada", 100)
    with pytest.raises(ValueError):
        s.withdraw(500)
    with pytest.raises(ValueError):
        s.withdraw(-1)
    assert s.balance == 100


def test_rejected_withdrawal_does_not_count():
    s = SavingsAccount("Ada", 100)
    with pytest.raises(ValueError):
        s.withdraw(500)
    s.withdraw(10)
    s.withdraw(10)
    s.withdraw(10)
    assert s.balance == 70


def test_distance_to():
    assert Point(0, 0).distance_to(Point(3, 4)) == 5
    assert Point(1, 1).distance_to(Point(1, 1)) == 0


def test_point_is_frozen():
    p = Point(1, 2)
    with pytest.raises(AttributeError):
        p.x = 5  # ty: ignore[invalid-assignment]


def test_moved():
    p = Point(1, 2)
    assert p.moved(3, -1) == Point(4, 1)
    assert p == Point(1, 2)


def test_area():
    assert math.isclose(area(Circle(1)), math.pi)
    assert area(Rectangle(3, 4)) == 12
    assert area(Triangle(3, 4)) == 6
    with pytest.raises(ValueError):
        area(("hexagon", 1))  # ty: ignore[invalid-argument-type]
