# Fill this in BEFORE you implement to_roman: at least 8 (number, numeral) pairs,
# worked out by hand. For example: (3, "III").
TEST_CASES: list[tuple[int, str]] = []


def to_roman(n: int) -> str:
    """n as a Roman numeral, for 1 <= n <= 3999. Raises ValueError otherwise.

    The symbols are I=1, V=5, X=10, L=50, C=100, D=500, M=1000. A smaller symbol
    before a larger one is subtracted, only in these six pairs:
    IV=4, IX=9, XL=40, XC=90, CD=400, CM=900.
    to_roman(1994) == "MCMXCIV"
    """
    raise NotImplementedError


def from_roman(numeral: str) -> int:
    """The value of a Roman numeral written by the rules above.

    Raises ValueError if numeral is empty or contains a character that isn't a Roman symbol.
    from_roman("MCMXCIV") == 1994
    """
    raise NotImplementedError
