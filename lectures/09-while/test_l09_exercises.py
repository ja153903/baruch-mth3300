import math

from l09_exercises import (
    count_digits,
    first_space,
    gcd,
    newton_sqrt,
    next_power_of_two,
    payoff_months,
    reverse_number,
    sum_of_odds,
    years_to_reach,
)


def test_count_digits():
    assert count_digits(0) == 1
    assert count_digits(7) == 1
    assert count_digits(3300) == 4


def test_years_to_reach():
    assert years_to_reach(100, 0.10, 100) == 0
    assert years_to_reach(100, 0.10, 110) == 1
    assert years_to_reach(1000, 0.07, 2000) == 11


def test_sum_of_odds():
    assert sum_of_odds(0) == 0
    assert sum_of_odds(1) == 1
    assert sum_of_odds(9) == 25
    assert sum_of_odds(10) == 25


def test_reverse_number():
    assert reverse_number(1234) == 4321
    assert reverse_number(3300) == 33
    assert reverse_number(7) == 7
    assert reverse_number(0) == 0


def test_next_power_of_two():
    assert next_power_of_two(1) == 1
    assert next_power_of_two(5) == 8
    assert next_power_of_two(8) == 8
    assert next_power_of_two(1000) == 1024


def test_gcd():
    assert gcd(12, 18) == 6
    assert gcd(17, 5) == 1
    assert gcd(7, 0) == 7
    assert gcd(0, 9) == 9


def test_first_space():
    assert first_space("New York") == 3
    assert first_space(" x") == 0
    assert first_space("Baruch") == -1
    assert first_space("") == -1


def test_newton_sqrt():
    assert math.isclose(newton_sqrt(2), 1.4142135623730951)
    assert math.isclose(newton_sqrt(9), 3)
    assert math.isclose(newton_sqrt(0.25), 0.5)
    assert math.isclose(newton_sqrt(1), 1)


def test_payoff_months():
    assert payoff_months(1000, 0.12, 100) == 11
    assert payoff_months(1200, 0, 100) == 12
    assert payoff_months(0, 0.12, 100) == 0
    assert payoff_months(1000, 0.12, 5) == -1
