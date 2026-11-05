from decimal import Decimal

from l22_exercises import coin_flip_frequency, round_money


def test_round_money():
    assert round_money("2.675") == Decimal("2.68")
    assert round_money("2.674") == Decimal("2.67")
    assert round_money("10") == Decimal("10.00")


def test_coin_flip_frequency():
    assert abs(coin_flip_frequency(100_000, seed=1) - 0.5) < 0.01
    assert coin_flip_frequency(100, seed=5) == coin_flip_frequency(100, seed=5)
