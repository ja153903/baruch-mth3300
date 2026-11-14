import l04_exercises as ex


def test_formatted_price():
    assert ex.formatted_price == "$1,234.50"


def test_rate_text():
    assert ex.rate_text == "7.25%"


def test_invoice_text():
    assert ex.invoice_text == "INV-000381"


def test_table_row():
    assert ex.table_row == "AAPL  |    227.50"


def test_debug_text():
    assert ex.debug_text == "shares=25"


def test_change_text():
    assert ex.change_text == "+15.0%"


def test_balance_text():
    assert ex.balance_text == "$9,876.50"


def test_banner():
    assert ex.banner == "******MTH 3300******"


def test_scientific():
    assert ex.scientific == "6.02e+23"
