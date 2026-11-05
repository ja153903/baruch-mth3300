import math

from hw09 import column_total, count_lines, safe_divide


def test_count_lines(tmp_path):
    empty = tmp_path / "empty.txt"
    empty.write_text("")
    assert count_lines(empty) == 0

    poem = tmp_path / "poem.txt"
    poem.write_text("one\ntwo\nthree\n")
    assert count_lines(poem) == 3


def test_column_total(tmp_path):
    csv_file = tmp_path / "trades.csv"
    csv_file.write_text("ticker,shares,price\nAAPL,10,190.5\nMSFT,5,410.25\n")
    assert column_total(csv_file, "shares") == 15
    assert math.isclose(column_total(csv_file, "price"), 600.75)


def test_safe_divide():
    assert safe_divide(6, 3) == 2
    assert safe_divide(1, 0) is None
