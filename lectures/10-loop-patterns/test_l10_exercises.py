from l10_exercises import (
    all_even_digits,
    count_pairs,
    count_primes,
    count_triples,
    has_repeat,
    largest_digit,
    longest_run,
    staircase,
    times_table,
)


def test_largest_digit():
    assert largest_digit(3790) == 9
    assert largest_digit(5) == 5
    assert largest_digit(0) == 0
    assert largest_digit(1111) == 1


def test_staircase():
    assert staircase(1) == "#"
    assert staircase(3) == "#\n##\n###"
    assert staircase(0) == ""


def test_count_pairs():
    assert count_pairs(5, 6) == 2
    assert count_pairs(5, 3) == 1
    assert count_pairs(5, 2) == 0  # 1 + 1 doesn't count: a must be less than b
    assert count_pairs(10, 11) == 5
    assert count_pairs(4, 20) == 0


def test_times_table():
    assert times_table(1) == "1"
    assert times_table(3) == "1 2 3\n2 4 6\n3 6 9"
    assert times_table(4).splitlines()[-1] == "4 8 12 16"


def test_has_repeat():
    assert not has_repeat("Baruch")
    assert has_repeat("Brooklyn")
    assert has_repeat("abca")
    assert not has_repeat("")
    assert not has_repeat("Aa")


def test_count_primes():
    assert count_primes(1) == 0
    assert count_primes(2) == 1
    assert count_primes(10) == 4
    assert count_primes(100) == 25


def test_all_even_digits():
    assert all_even_digits(2468)
    assert all_even_digits(8)
    assert not all_even_digits(2467)
    assert not all_even_digits(1246)
    assert not all_even_digits(32)


def test_longest_run():
    assert longest_run("aabbbc") == 3
    assert longest_run("") == 0
    assert longest_run("x") == 1
    assert longest_run("abc") == 1
    assert longest_run("aaab") == 3
    assert longest_run("abbbb") == 4


def test_count_triples():
    assert count_triples(4) == 0
    assert count_triples(5) == 1
    assert count_triples(13) == 3
    assert count_triples(20) == 6
