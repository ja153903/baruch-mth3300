# Warmup


def largest_digit(n: int) -> int:
    """The largest digit of a non-negative integer: largest_digit(3790) == 9."""
    raise NotImplementedError


def staircase(n: int) -> str:
    """n lines of #, one more on each line, joined by newlines.

    staircase(3) == "#\\n##\\n###", which prints as:
    #
    ##
    ###
    """
    raise NotImplementedError


# Core


def count_pairs(n: int, target: int) -> int:
    """How many pairs a, b with 1 <= a < b <= n add up to target.

    count_pairs(5, 6) == 2, because 1 + 5 and 2 + 4 add up to 6.
    """
    raise NotImplementedError


def times_table(n: int) -> str:
    """An n-by-n multiplication table: numbers separated by spaces, rows by newlines.

    times_table(3) == "1 2 3\\n2 4 6\\n3 6 9"
    """
    raise NotImplementedError


def has_repeat(text: str) -> bool:
    """True if some character appears more than once in text.

    has_repeat("Baruch") is False; has_repeat("Brooklyn") is True.
    Hint: compare each position with every position after it.
    """
    raise NotImplementedError


def count_primes(n: int) -> int:
    """How many primes there are from 2 to n: count_primes(10) == 4 (2, 3, 5, 7)."""
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it with the tests, then fix it.


def all_even_digits(n: int) -> bool:
    """True if every digit of a positive integer n is even: all_even_digits(2468) is True."""
    while n > 0:
        if n % 2 == 0:
            return True
        n = n // 10
    return False


# Stretch


def longest_run(text: str) -> int:
    """The length of the longest run of one repeated character.

    longest_run("aabbbc") == 3, and longest_run("") == 0.
    """
    raise NotImplementedError


def count_triples(limit: int) -> int:
    """How many Pythagorean triples a < b < c <= limit there are, with a**2 + b**2 == c**2.

    count_triples(13) == 3: (3, 4, 5), (6, 8, 10), and (5, 12, 13).
    """
    raise NotImplementedError
