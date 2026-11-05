from l09_exercises import count_digits, years_to_reach


def test_count_digits():
    assert count_digits(0) == 1
    assert count_digits(7) == 1
    assert count_digits(3300) == 4


def test_years_to_reach():
    assert years_to_reach(100, 0.10, 100) == 0
    assert years_to_reach(100, 0.10, 110) == 1
    assert years_to_reach(1000, 0.07, 2000) == 11
