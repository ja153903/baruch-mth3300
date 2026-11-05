import pytest

from p_classes import Inventory, Stack


def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()
    with pytest.raises(IndexError):
        s.pop()


def test_stacks_are_independent():
    a, b = Stack(), Stack()
    a.push(1)
    assert b.is_empty()


def test_inventory():
    inv = Inventory()
    assert inv.count("pens") == 0
    inv.add("pens", 10)
    inv.remove("pens", 3)
    assert inv.count("pens") == 7
    with pytest.raises(ValueError):
        inv.remove("pens", 8)
    assert inv.count("pens") == 7
