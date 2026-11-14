# Use a while loop in each function.

# Warmup


def count_digits(n: int) -> int:
    """The number of digits in a non-negative integer. count_digits(0) == 1. Use a while loop."""
    raise NotImplementedError


def years_to_reach(balance: float, rate: float, goal: float) -> int:
    """How many years of annual compounding until balance >= goal."""
    raise NotImplementedError


# Core


def sum_of_odds(n: int) -> int:
    """1 + 3 + 5 + ..., adding every odd number up to n (inclusive).

    sum_of_odds(10) == 25 and sum_of_odds(0) == 0.
    """
    raise NotImplementedError


def reverse_number(n: int) -> int:
    """The digits of a non-negative integer in reverse order.

    reverse_number(1234) == 4321. Use % and //, not strings.
    Zeros that end up in front disappear: reverse_number(3300) == 33.
    """
    raise NotImplementedError


def next_power_of_two(n: int) -> int:
    """The smallest power of 2 (1, 2, 4, 8, ...) that is at least n, for n >= 1.

    next_power_of_two(5) == 8 and next_power_of_two(8) == 8.
    """
    raise NotImplementedError


def gcd(a: int, b: int) -> int:
    """The greatest common divisor of two non-negative integers, not both 0.

    gcd(12, 18) == 6. Use Euclid's algorithm: while b isn't 0, the new a is
    the old b, and the new b is old a % old b. When b reaches 0, a is the answer.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def first_space(text: str) -> int:
    """The index of the first space in text, or -1 if there isn't one."""
    i = 0
    while i <= len(text):
        if text[i] == " ":
            return i
        i += 1
    return -1


# Stretch


def newton_sqrt(x: float) -> float:
    """The square root of x > 0, by Newton's method. Don't use ** or math.sqrt.

    Start with guess = x. Then repeat guess = (guess + x / guess) / 2
    until abs(guess * guess - x) < 1e-9.
    """
    raise NotImplementedError


def payoff_months(balance: float, annual_rate: float, payment: float) -> int:
    """Like months_to_pay_off in the notes, but -1 if the loan never gets paid off.

    It never gets paid off when the payment is no more than the first month's
    interest, balance * annual_rate / 12. Check for that before the loop starts.
    """
    raise NotImplementedError
