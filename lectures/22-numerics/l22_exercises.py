from decimal import Decimal


def round_money(amount: str) -> Decimal:
    """Round to cents, with halves rounding up: "2.675" -> Decimal("2.68")."""
    raise NotImplementedError


def coin_flip_frequency(flips: int, seed: int) -> float:
    """The fraction of heads in `flips` simulated fair coin flips. Use random.Random(seed)."""
    raise NotImplementedError
