import math

from l05_exercises import average, cube


def test_cube():
    assert cube(3) == 27
    assert cube(-2) == -8


def test_average():
    assert average(1, 2, 3) == 2
    assert math.isclose(average(88, 92, 79), 259 / 3)
