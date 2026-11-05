from l14_exercises import common_elements, has_duplicates


def test_has_duplicates():
    assert not has_duplicates([])
    assert not has_duplicates([1, 2, 3])
    assert has_duplicates([1, 2, 1])


def test_common_elements():
    assert common_elements([3, 1, 2, 3], [3, 4, 1]) == [1, 3]
    assert common_elements([1], [2]) == []
