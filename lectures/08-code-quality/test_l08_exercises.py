from l08_exercises import absolute, ticket_price


def test_absolute():
    assert absolute(5) == 5
    assert absolute(0) == 0
    assert absolute(-5) == 5


def test_ticket_price():
    assert ticket_price(5) == 8
    assert ticket_price(11) == 8
    assert ticket_price(12) == 14
    assert ticket_price(64) == 14
    assert ticket_price(65) == 9
