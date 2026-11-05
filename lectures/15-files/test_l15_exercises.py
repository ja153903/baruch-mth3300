from l15_exercises import longest_line, write_lines


def test_write_lines(tmp_path):
    path = tmp_path / "out.txt"
    write_lines(path, ["a", "bb"])
    assert path.read_text() == "a\nbb\n"


def test_longest_line(tmp_path):
    path = tmp_path / "in.txt"
    path.write_text("short\nthe longest one\nmid\n")
    assert longest_line(path) == "the longest one"
    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert longest_line(empty) == ""
