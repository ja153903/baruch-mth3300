from l16_exercises import parse_int, read_prices


def test_parse_int():
    assert parse_int("42") == 42
    assert parse_int("-7") == -7
    assert parse_int("4.5") is None
    assert parse_int("") is None


def test_read_prices(tmp_path):
    path = tmp_path / "prices.csv"
    path.write_text("ticker,price\nAAPL,190.5\nBAD,n/a\nMSFT,410.25\n")
    assert read_prices(path) == {"AAPL": 190.5, "MSFT": 410.25}
