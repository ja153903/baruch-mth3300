from p_strings import caesar, compress, is_anagram


def test_is_anagram():
    assert is_anagram("Dormitory", "dirty room")
    assert is_anagram("", "")
    assert not is_anagram("abc", "abd")
    assert not is_anagram("aab", "abb")


def test_caesar():
    assert caesar("abc", 1) == "bcd"
    assert caesar("xyz", 3) == "abc"
    assert caesar("Hello, World!", 13) == "Uryyb, Jbeyq!"
    assert caesar(caesar("Baruch", 7), -7) == "Baruch"


def test_compress():
    assert compress("") == ""
    assert compress("aaabcc") == "a3b1c2"
    assert compress("z") == "z1"
