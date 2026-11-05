from hw07 import group_by_value, unique_sorted, word_counts


def test_word_counts():
    assert word_counts("") == {}
    assert word_counts("the cat and the hat") == {
        "the": 2,
        "cat": 1,
        "and": 1,
        "hat": 1,
    }
    assert word_counts("The the THE") == {"the": 3}


def test_unique_sorted():
    assert unique_sorted([]) == []
    assert unique_sorted([3, 1, 3, 2, 1]) == [1, 2, 3]


def test_group_by_value():
    assert group_by_value({}) == {}
    assert group_by_value({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}


# TODO: add a test for most_common_word that fails on the buggy version.
