import hw02


def test_title_name():
    assert hw02.title_name == "Ada Lovelace"


def test_initials():
    assert hw02.initials == "AL"


def test_email_domain():
    assert hw02.email_domain == "baruch.cuny.edu"


def test_receipt():
    assert hw02.receipt == "4 x notebook @ $3.50 = $14.00"
