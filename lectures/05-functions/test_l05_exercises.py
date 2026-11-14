import math

from l05_exercises import (
    average,
    cube,
    distance,
    doubling_time,
    leftover_cash,
    name_tag,
    rent_share,
    sales_tax,
    shares_affordable,
)


def test_cube():
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0


def test_average():
    assert average(1, 2, 3) == 2
    assert math.isclose(average(88, 92, 79), 259 / 3)
    assert average(-5, 0, 5) == 0


def test_sales_tax():
    assert sales_tax(24.99) == 2.22
    assert sales_tax(50, rate=0.1) == 5
    assert sales_tax(0) == 0


def test_name_tag():
    assert name_tag("ada", "lovelace") == "LOVELACE, Ada"
    assert name_tag("Grace", "HOPPER") == "HOPPER, Grace"
    assert name_tag("j", "doe") == "DOE, J"


def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(-1, -1, 2, 3) == 5
    assert distance(1, 1, 1, 1) == 0


def test_shares_affordable():
    assert shares_affordable(500, 30) == 16
    assert shares_affordable(100, 100) == 1
    assert shares_affordable(10, 20) == 0
    assert isinstance(shares_affordable(1000, 37.5), int)


def test_rent_share():
    assert rent_share(2500, 3) == 833.33
    assert rent_share(1800, 2) == 900
    assert rent_share(1000, 1) == 1000


def test_leftover_cash():
    assert leftover_cash(500, 30) == 20
    assert leftover_cash(100, 100) == 0
    assert leftover_cash(10, 20) == 10


def test_doubling_time():
    assert doubling_time(1.0) == 1
    assert math.isclose(doubling_time(0.07), 10.244768351058712)
    assert math.isclose(doubling_time(0.01), 69.66071689357483)
