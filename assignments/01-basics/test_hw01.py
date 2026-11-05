import math

import hw01


def test_seconds_in_a_week():
    assert hw01.seconds_in_a_week == 604_800


def test_average_score():
    assert hw01.average_score is not None
    assert math.isclose(hw01.average_score, 259 / 3)


def test_hypotenuse():
    assert hw01.hypotenuse == 5


def test_eggs():
    assert hw01.full_boxes == 8
    assert hw01.leftover_eggs == 4
