from hw04 import is_leap_year, is_triangle, letter_grade, sign


def test_letter_grade():
    assert letter_grade(100) == "A"
    assert letter_grade(90) == "A"
    assert letter_grade(89.9) == "B"
    assert letter_grade(80) == "B"
    assert letter_grade(70) == "C"
    assert letter_grade(60) == "D"
    assert letter_grade(59) == "F"
    assert letter_grade(0) == "F"


def test_sign():
    assert sign(-3.5) == -1
    assert sign(0) == 0
    assert sign(42) == 1


def test_is_triangle():
    assert is_triangle(3, 4, 5)
    assert not is_triangle(1, 2, 3)  # flat: the two short sides only just reach
    assert not is_triangle(1, 1, 5)
    assert not is_triangle(0, 4, 4)
    assert not is_triangle(-3, 4, 5)


def test_is_leap_year():
    assert is_leap_year(2024)
    assert not is_leap_year(2023)
    assert not is_leap_year(1900)
    assert is_leap_year(2000)
