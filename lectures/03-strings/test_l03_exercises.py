import l03_exercises as ex


def test_first_three():
    assert ex.first_three == "pro"


def test_reversed_word():
    assert ex.reversed_word == "gnimmargorp"


def test_isin_parts():
    assert ex.country_code == "US"
    assert ex.check_digit == "5"


def test_clean_ticker():
    assert ex.clean_ticker == "NVDA"


def test_iso_date():
    assert ex.iso_date == "2026-07-04"


def test_masked_card():
    assert ex.masked_card == "************1234"


def test_last_three():
    assert ex.last_three == "ing"


def test_middle_letter():
    assert ex.middle_letter == "a"


def test_word_count():
    assert ex.word_count == 9
