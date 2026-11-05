from l13_exercises import letter_frequencies, order_total


def test_letter_frequencies():
    assert letter_frequencies("") == {}
    assert letter_frequencies("Aa b!") == {"a": 2, "b": 1}


def test_order_total():
    menu = {"coffee": 3.0, "bagel": 2.5}
    assert order_total(menu, []) == 0
    assert order_total(menu, ["coffee", "bagel", "coffee"]) == 8.5
    assert order_total(menu, ["tea"]) == 0
