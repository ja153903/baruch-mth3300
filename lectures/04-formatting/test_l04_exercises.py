import l04_exercises as ex


def test_formatted_price():
    assert ex.formatted_price == "$1,234.50"


def test_rate_text():
    assert ex.rate_text == "7.25%"
