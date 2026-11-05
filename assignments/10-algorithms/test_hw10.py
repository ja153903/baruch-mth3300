import random

from hw10 import binary_search, fib, merge_sort


def test_binary_search():
    xs = [1, 3, 5, 7, 9, 11]
    for i, x in enumerate(xs):
        assert binary_search(xs, x) == i
    assert binary_search(xs, 4) == -1
    assert binary_search(xs, 12) == -1
    assert binary_search([], 1) == -1


def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    rng = random.Random(3300)
    for _ in range(50):
        xs = [rng.randint(-100, 100) for _ in range(rng.randint(0, 30))]
        original = list(xs)
        assert merge_sort(xs) == sorted(xs)
        assert xs == original


def test_fib():
    assert [fib(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib(30) == 832_040
