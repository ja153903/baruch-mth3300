# Warmup


def digit_sum(n: int) -> int:
    """The sum of the digits of n >= 0, recursively. digit_sum(3300) == 6.

    No loops, and no str(): use n % 10 and n // 10.
    """
    raise NotImplementedError


def countdown_list(n: int) -> list[int]:
    """[n, n - 1, ..., 1], built recursively. countdown_list(0) == []."""
    raise NotImplementedError


# Core


def power(base: float, exp: int) -> float:
    """base ** exp for exp >= 0, computed recursively. Don't use ** or pow."""
    raise NotImplementedError


def reverse(s: str) -> str:
    """Reverse a string recursively. Don't use slicing with a step of -1."""
    raise NotImplementedError


def count_char(s: str, ch: str) -> int:
    """How many times the character ch appears in s, recursively. Don't use .count()."""
    raise NotImplementedError


def max_value(xs: list[int]) -> int:
    """The largest number in xs, recursively. xs is not empty. Don't use max()."""
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def count_digits(n: int) -> int:
    """How many digits n >= 0 has, recursively. count_digits(3300) == 4."""
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


# Stretch


def fast_power(base: float, exp: int) -> float:
    """base ** exp for exp >= 0, recursively, in about log2(exp) calls.

    Compute half = fast_power(base, exp // 2) once, and square it. If exp is odd,
    multiply by base one more time. Don't use ** or pow.
    """
    raise NotImplementedError


def subsets(xs: list[int]) -> list[list[int]]:
    """Every subset of xs, as a list of lists. subsets([1, 2]) has [], [1], [2], and [1, 2].

    The subsets, and the items in each one, can be in any order.
    Hint: take the subsets of xs[1:], then add a copy of each one with xs[0] in it.
    """
    raise NotImplementedError
