def is_anagram(a: str, b: str) -> bool:
    """True if a and b use the same letters, ignoring case and spaces. "Dormitory", "dirty room" -> True."""
    raise NotImplementedError


def caesar(text: str, shift: int) -> str:
    """Shift each letter `shift` places through the alphabet, wrapping around and keeping its case. Leave other characters alone."""
    raise NotImplementedError


def compress(text: str) -> str:
    """Run-length encoding: "aaabcc" -> "a3b1c2"."""
    raise NotImplementedError
