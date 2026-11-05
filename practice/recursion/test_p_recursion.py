from p_recursion import binary_strings, flatten_nested, grid_paths


def test_binary_strings():
    assert binary_strings(0) == [""]
    assert binary_strings(2) == ["00", "01", "10", "11"]
    assert len(binary_strings(8)) == 256


def test_flatten_nested():
    assert flatten_nested([]) == []
    assert flatten_nested([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]


def test_grid_paths():
    assert grid_paths(1, 1) == 1
    assert grid_paths(2, 2) == 2
    assert grid_paths(3, 3) == 6
    assert grid_paths(3, 7) == 28
