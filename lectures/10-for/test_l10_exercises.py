from l10_exercises import (
    alternating_sum,
    count_evens,
    count_multiples,
    digit_sum,
    factorial,
    is_prime,
    product,
    remove_vowels,
    seven_frequency,
)


def test_count_multiples():
    assert count_multiples(10, 3) == 3
    assert count_multiples(10, 1) == 10
    assert count_multiples(2, 5) == 0


def test_product():
    assert product([]) == 1
    assert product([2, 3, 4]) == 24
    assert product([5, 0, 2]) == 0


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_digit_sum():
    assert digit_sum(0) == 0
    assert digit_sum(3300) == 6
    assert digit_sum(98765) == 35


def test_remove_vowels():
    assert remove_vowels("Baruch College") == "Brch Cllg"
    assert remove_vowels("AEIOU aeiou") == " "
    assert remove_vowels("") == ""


def test_alternating_sum():
    assert alternating_sum([]) == 0
    assert alternating_sum([5]) == 5
    assert alternating_sum([1, 2, 3, 4]) == -2


def test_count_evens():
    assert count_evens(1) == 0
    assert count_evens(10) == 5
    assert count_evens(7) == 3


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(97)
    assert not is_prime(91)
    assert not is_prime(100)


def test_seven_frequency():
    assert seven_frequency(1000, 42) == seven_frequency(1000, 42)
    assert abs(seven_frequency(100_000, 3300) - 1 / 6) < 0.01
