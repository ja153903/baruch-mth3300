import pytest

from l16_exercises import (
    check_percent,
    count_bad_rows,
    parse_int,
    parse_money,
    read_prices,
    read_trades,
    total_shares,
    write_report,
)


def test_parse_int():
    assert parse_int("42") == 42
    assert parse_int("-7") == -7
    assert parse_int("4.5") is None
    assert parse_int("") is None


def test_check_percent():
    assert check_percent(50) == 50
    assert check_percent(0) == 0
    assert check_percent(100) == 100
    with pytest.raises(ValueError, match="120"):
        check_percent(120)
    with pytest.raises(ValueError):
        check_percent(-0.5)


def test_read_prices(tmp_path):
    path = tmp_path / "prices.csv"
    path.write_text("ticker,price\nAAPL,190.5\nBAD,n/a\nMSFT,410.25\n")
    assert read_prices(path) == {"AAPL": 190.5, "MSFT": 410.25}


def test_parse_money():
    assert parse_money("$1,234.50") == 1234.5
    assert parse_money("(12.50)") == -12.5
    assert parse_money("42") == 42.0
    with pytest.raises(ValueError):
        parse_money("abc")
    with pytest.raises(ValueError):
        parse_money("")


def test_count_bad_rows(tmp_path):
    path = tmp_path / "prices.csv"
    path.write_text("ticker,price\nAAPL,190.5\nBAD,n/a\nMSFT,410.25\nNONE,\n")
    assert count_bad_rows(path, "price") == 2
    assert count_bad_rows(path, "ticker") == 4
    clean = tmp_path / "clean.csv"
    clean.write_text("ticker,price\n")
    assert count_bad_rows(clean, "price") == 0


def test_write_report(tmp_path):
    path = tmp_path / "report.csv"
    write_report(path, {"MSFT": 2051.25, "AAPL": 1905.0})
    assert path.read_text() == "ticker,total\nAAPL,1905.00\nMSFT,2051.25\n"
    empty = tmp_path / "empty.csv"
    write_report(empty, {})
    assert empty.read_text() == "ticker,total\n"


def test_total_shares(tmp_path):
    path = tmp_path / "trades.csv"
    path.write_text("ticker,shares\nAAPL,10\nBAD,x\nMSFT,5\n")
    assert total_shares(path) == 15
    mixed = tmp_path / "mixed.csv"
    mixed.write_text("ticker,shares\nAAPL,10\nMSFT,2.5\nNVDA,-3\n")
    assert total_shares(mixed) == 7
    empty = tmp_path / "empty.csv"
    empty.write_text("ticker,shares\n")
    assert total_shares(empty) == 0


def test_read_trades(tmp_path):
    good = tmp_path / "good.csv"
    good.write_text("ticker,shares,price\nAAPL,10,190.5\nMSFT,5,410.25\n")
    assert read_trades(good) == [("AAPL", 10, 190.5), ("MSFT", 5, 410.25)]
    bad = tmp_path / "bad.csv"
    bad.write_text("ticker,shares,price\nAAPL,10,190.5\nMSFT,x,410.25\n")
    with pytest.raises(ValueError, match="line 3"):
        read_trades(bad)
    empty = tmp_path / "empty.csv"
    empty.write_text("ticker,shares,price\n")
    assert read_trades(empty) == []
