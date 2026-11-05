# Warmup


def max_unsigned(bits: int) -> int:
    """The largest number that fits in `bits` bits with no sign. max_unsigned(8) == 255."""
    raise NotImplementedError


def utf8_bytes(text: str) -> int:
    """How many bytes text takes when encoded as UTF-8."""
    raise NotImplementedError


# Core


def to_base(n: int, base: int) -> str:
    """The digits of a non-negative integer n in a base from 2 to 10.

    to_base(13, 2) == "1101" and to_base(0, 2) == "0". Don't use bin() or format().
    """
    raise NotImplementedError


def wrap(n: int, bits: int) -> int:
    """What an unsigned `bits`-bit integer holds after storing n: wrap(260, 8) == 4."""
    raise NotImplementedError


def to_signed(pattern: int, bits: int) -> int:
    """Read an unsigned bit pattern (0 to 2**bits - 1) as a two's complement number.

    to_signed(255, 8) == -1, to_signed(127, 8) == 127, to_signed(128, 8) == -128.
    """
    raise NotImplementedError


def approx_equal(a: float, b: float, rel_tol: float = 1e-9) -> bool:
    """True if a and b differ by at most rel_tol times the larger of |a| and |b|.

    Don't use math.isclose.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find an input that breaks it, then fix it.


def total_cents(prices: list[float]) -> int:
    """The total of prices given in dollars, as a whole number of cents."""
    return int(sum(prices) * 100)


# Stretch


def machine_epsilon() -> float:
    """The smallest power of 2, eps, for which 1.0 + eps != 1.0.

    Find it with a loop: start at 1.0 and keep halving.
    """
    raise NotImplementedError


def utf8_length(ch: str) -> int:
    """How many bytes UTF-8 uses for the single character ch, without calling encode().

    Code points below 0x80 take 1 byte, below 0x800 take 2, below 0x10000 take 3,
    and the rest take 4.
    """
    raise NotImplementedError
