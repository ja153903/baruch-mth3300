from l15_exercises import (
    append_line,
    backup,
    filter_file,
    find_lines,
    longest_line,
    read_numbers,
    save_prices,
    word_index,
    write_lines,
)


def test_write_lines(tmp_path):
    path = tmp_path / "out.txt"
    write_lines(path, ["a", "bb"])
    assert path.read_text() == "a\nbb\n"


def test_read_numbers(tmp_path):
    path = tmp_path / "nums.txt"
    path.write_text("101.5\n  99\n\n103.25  \n")
    assert read_numbers(path) == [101.5, 99.0, 103.25]
    blanks = tmp_path / "blanks.txt"
    blanks.write_text("\n  \n")
    assert read_numbers(blanks) == []
    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert read_numbers(empty) == []


def test_longest_line(tmp_path):
    path = tmp_path / "in.txt"
    path.write_text("short\nthe longest one\nmid\n")
    assert longest_line(path) == "the longest one"
    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert longest_line(empty) == ""


def test_append_line(tmp_path):
    path = tmp_path / "log.txt"
    append_line(path, "Mon: ok")
    append_line(path, "Tue: ok")
    assert path.read_text() == "Mon: ok\nTue: ok\n"
    old = tmp_path / "old.txt"
    old.write_text("first\n")
    append_line(old, "second")
    assert old.read_text() == "first\nsecond\n"


def test_find_lines(tmp_path):
    path = tmp_path / "news.txt"
    path.write_text("Apple rises\nMarkets flat\nAPPLE falls\n")
    assert find_lines(path, "apple") == [1, 3]
    assert find_lines(path, "Markets") == [2]
    assert find_lines(path, "tesla") == []


def test_filter_file(tmp_path):
    src = tmp_path / "prices.txt"
    src.write_text("101.5\n99.0\n103.25\n")
    dst = tmp_path / "above.txt"
    assert filter_file(src, dst, 100) == 2
    assert dst.read_text() == "101.5\n103.25\n"
    assert filter_file(src, dst, 200) == 0
    assert dst.read_text() == ""


def test_save_prices(tmp_path):
    path = tmp_path / "prices.txt"
    save_prices(path, [1.5, 2.25, 10.0])
    assert path.read_text() == "1.50\n2.25\n10.00\n"
    save_prices(path, [3.0])
    assert path.read_text() == "3.00\n"
    save_prices(path, [])
    assert path.read_text() == ""


def test_backup(tmp_path):
    (tmp_path / "a.txt").write_text("A\n")
    (tmp_path / "b.txt").write_text("B\n")
    (tmp_path / "c.csv").write_text("C\n")
    assert backup(tmp_path) == 2
    assert (tmp_path / "backup" / "a.txt").read_text() == "A\n"
    assert (tmp_path / "backup" / "b.txt").read_text() == "B\n"
    assert not (tmp_path / "backup" / "c.csv").exists()
    assert (tmp_path / "a.txt").exists()
    empty = tmp_path / "empty"
    empty.mkdir()
    assert backup(empty) == 0
    assert (empty / "backup").is_dir()


def test_word_index(tmp_path):
    path = tmp_path / "trades.txt"
    path.write_text("Buy AAPL\nsell aapl\nbuy buy NVDA\n")
    assert word_index(path) == {
        "buy": [1, 3],
        "aapl": [1, 2],
        "sell": [2],
        "nvda": [3],
    }
    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert word_index(empty) == {}
