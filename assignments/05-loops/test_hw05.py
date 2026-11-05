import math

from hw05 import collatz_steps, compound_balance, factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(20) == math.factorial(20)


def test_collatz_steps():
    assert collatz_steps(1) == 0
    assert collatz_steps(2) == 1
    assert collatz_steps(6) == 8
    assert collatz_steps(27) == 111


def test_compound_balance():
    assert compound_balance(1000, 0.05, 0) == 1000
    assert math.isclose(compound_balance(1000, 0.05, 1), 1050)
    assert math.isclose(compound_balance(1000, 0.05, 30), 1000 * 1.05**30)
