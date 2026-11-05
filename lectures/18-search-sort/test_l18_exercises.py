import random

from l18_exercises import count_occurrences, insertion_sort


def test_count_occurrences():
    assert count_occurrences([], 1) == 0
    assert count_occurrences([1, 2, 1, 1], 1) == 3


def test_insertion_sort():
    rng = random.Random(18)
    for _ in range(30):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 20))]
        original = list(xs)
        assert insertion_sort(xs) == sorted(xs)
        assert xs == original
