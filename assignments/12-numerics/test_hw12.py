import math
from decimal import Decimal
from fractions import Fraction

from hw12 import estimate_pi, harmonic, total_price


def test_total_price():
    assert total_price([]) == 0
    assert total_price(["0.10", "0.20"]) == Decimal("0.30")
    assert total_price(["19.99"] * 3) == Decimal("59.97")


def test_harmonic():
    assert harmonic(1) == 1
    assert harmonic(3) == Fraction(11, 6)
    assert harmonic(10) == Fraction(7381, 2520)


def test_estimate_pi():
    assert abs(estimate_pi(100_000) - math.pi) < 0.05
    assert estimate_pi(1_000, seed=7) == estimate_pi(1_000, seed=7)
