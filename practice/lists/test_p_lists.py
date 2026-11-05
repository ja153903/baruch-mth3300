from p_lists import chunk, merge_sorted, second_largest


def test_second_largest():
    assert second_largest([3, 1, 4, 1, 5]) == 4
    assert second_largest([5, 5, 5]) is None
    assert second_largest([]) is None
    assert second_largest([2, 5, 5]) == 2


def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([], 3) == []


def test_merge_sorted():
    assert merge_sorted([1, 4, 6], [2, 3, 7, 8]) == [1, 2, 3, 4, 6, 7, 8]
    assert merge_sorted([], [1]) == [1]
    assert merge_sorted([1, 1], [1]) == [1, 1, 1]
