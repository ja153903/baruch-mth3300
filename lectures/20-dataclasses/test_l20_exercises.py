from l20_exercises import Rectangle


def test_area_and_perimeter():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14


def test_scale():
    r = Rectangle(3, 4)
    r.scale(2)
    assert r == Rectangle(6, 8)
