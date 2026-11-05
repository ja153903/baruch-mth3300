from decimal import Decimal

import pytest

from hw12 import caesar, from_base, to_twos_complement, total_price


def test_from_base():
    assert from_base("0", 2) == 0
    assert from_base("1101", 2) == 13
    assert from_base("777", 8) == 511
    assert from_base("ff", 16) == 255
    assert from_base("FF", 16) == 255
    assert from_base("3300", 10) == 3300


def test_from_base_invalid_digit():
    with pytest.raises(ValueError):
        from_base("102", 2)
    with pytest.raises(ValueError):
        from_base("g", 16)


def test_to_twos_complement():
    assert to_twos_complement(0, 8) == "00000000"
    assert to_twos_complement(5, 8) == "00000101"
    assert to_twos_complement(-1, 8) == "11111111"
    assert to_twos_complement(-128, 8) == "10000000"
    assert to_twos_complement(127, 8) == "01111111"
    assert to_twos_complement(-2, 4) == "1110"


def test_to_twos_complement_out_of_range():
    with pytest.raises(ValueError):
        to_twos_complement(128, 8)
    with pytest.raises(ValueError):
        to_twos_complement(-129, 8)


def test_caesar():
    assert caesar("abc", 1) == "bcd"
    assert caesar("xyz", 3) == "abc"
    assert caesar("Hello, World!", 13) == "Uryyb, Jbeyq!"
    assert caesar(caesar("Baruch 3300", 7), -7) == "Baruch 3300"
    assert caesar("café", 1) == "dbgé"


def test_total_price():
    assert total_price([]) == 0
    assert total_price(["0.10", "0.20"]) == Decimal("0.30")
    assert total_price(["19.99"] * 3) == Decimal("59.97")
