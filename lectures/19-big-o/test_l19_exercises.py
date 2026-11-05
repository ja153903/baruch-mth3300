from l19_exercises import has_pair_with_sum, is_sorted


def test_has_pair_with_sum():
    assert has_pair_with_sum([1, 4, 6, 9], 10)
    assert not has_pair_with_sum([1, 4, 6, 9], 2)
    assert not has_pair_with_sum([5], 10)
    assert has_pair_with_sum([5, 5], 10)
    assert has_pair_with_sum(list(range(200_000)), 399_997)


def test_is_sorted():
    assert is_sorted([])
    assert is_sorted([1, 1, 2])
    assert not is_sorted([2, 1])
