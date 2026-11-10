from l13_exercises import count_allocations, letter_frequencies, order_total


def test_letter_frequencies():
    assert letter_frequencies("") == {}
    assert letter_frequencies("Aa b!") == {"a": 2, "b": 1}


def test_order_total():
    menu = {"coffee": 3.0, "bagel": 2.5}
    assert order_total(menu, []) == 0
    assert order_total(menu, ["coffee", "bagel", "coffee"]) == 8.5
    assert order_total(menu, ["tea"]) == 0


def test_count_allocations():
    assert count_allocations([]) == {}
    counts = count_allocations(
        [
            {"tech": 0.6, "energy": 0.4},
            {"energy": 0.4, "tech": 0.6},  # same weights, different key order
            {"tech": 1.0},
        ]
    )
    assert counts == {
        frozendict(tech=0.6, energy=0.4): 2,
        frozendict(tech=1.0): 1,
    }
