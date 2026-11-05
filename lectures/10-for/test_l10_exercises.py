from l10_exercises import count_multiples, product


def test_count_multiples():
    assert count_multiples(10, 3) == 3
    assert count_multiples(10, 1) == 10
    assert count_multiples(2, 5) == 0


def test_product():
    assert product([]) == 1
    assert product([2, 3, 4]) == 24
    assert product([5, 0, 2]) == 0
