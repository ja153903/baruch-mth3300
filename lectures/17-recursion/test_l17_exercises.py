from l17_exercises import power, reverse


def test_power():
    assert power(2, 0) == 1
    assert power(2, 10) == 1024
    assert power(1.5, 2) == 2.25


def test_reverse():
    assert reverse("") == ""
    assert reverse("a") == "a"
    assert reverse("baruch") == "hcurab"
