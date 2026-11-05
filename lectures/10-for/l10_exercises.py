# Warmup


def count_multiples(n: int, k: int) -> int:
    """How many numbers from 1 to n (inclusive) are divisible by k."""
    raise NotImplementedError


def product(xs: list[int]) -> int:
    """The product of all numbers in xs. The product of an empty list is 1."""
    raise NotImplementedError


# Core


def factorial(n: int) -> int:
    """n! = 1 * 2 * ... * n, for n >= 0. factorial(0) == 1."""
    raise NotImplementedError


def digit_sum(n: int) -> int:
    """The sum of the digits of a non-negative integer. digit_sum(3300) == 6.

    Hint: loop over str(n).
    """
    raise NotImplementedError


def remove_vowels(text: str) -> str:
    """text with every vowel (a, e, i, o, u, upper or lower case) removed."""
    raise NotImplementedError


def alternating_sum(xs: list[int]) -> int:
    """xs[0] - xs[1] + xs[2] - xs[3] + ...  The alternating sum of [] is 0.

    Use enumerate.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def count_evens(n: int) -> int:
    """How many even numbers from 1 to n (inclusive)."""
    count = 0
    for k in range(1, n):
        if k % 2 == 0:
            count += 1
    return count


# Stretch


def is_prime(n: int) -> bool:
    """True if n is prime. Numbers less than 2 are not prime.

    Return as soon as you find a divisor.
    """
    raise NotImplementedError


def seven_frequency(trials: int, seed: int) -> float:
    """Roll two dice `trials` times. Return the fraction of rolls that sum to 7.

    Add `import random` at the top of this file. Call random.seed(seed) first,
    so the result is the same on every run.
    """
    raise NotImplementedError
