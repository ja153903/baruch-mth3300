from collections.abc import Callable

import pytest

from hw06 import (
    PRICES,
    SIGNAL_CASES,
    backtest,
    best_windows,
    daily_changes,
    moving_average,
    running_total,
    signals,
)

ZIGZAG: list[float] = [3, 2, 1, 2, 3, 4, 3, 2, 1]


# Part 1


def test_running_total():
    assert running_total([]) == []
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([5, -5, 5]) == [5, 0, 5]


def test_moving_average():
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    assert moving_average([1, 2, 3, 4], 4) == [2.5]
    assert moving_average([1, 2, 3], 1) == [1, 2, 3]
    assert moving_average([1, 2], 3) == []


def test_daily_changes():
    assert daily_changes([]) == []
    assert daily_changes([5]) == []
    assert daily_changes([10, 12, 11]) == [2, -1]


# Part 2


def test_signals_basic():
    assert signals(ZIGZAG, 1, 3) == [(3, "buy"), (6, "sell")]


def test_signals_lines_up_the_two_averages():
    assert signals(ZIGZAG, 2, 3) == [(4, "buy"), (7, "sell")]


def test_signals_after_equal_averages():
    assert signals([3, 3, 3, 4], 1, 3) == [(3, "buy")]
    assert signals([3, 3, 3, 2], 1, 3) == [(3, "sell")]


def test_signals_with_no_crossing():
    assert signals([5, 5, 5, 5, 5], 1, 3) == []
    assert signals([1, 2, 3, 4, 5], 1, 3) == []


def test_signals_first_day_has_no_signal():
    assert signals([1, 2, 9], 1, 3) == []


def test_signals_not_enough_prices():
    assert signals([1, 2], 1, 3) == []


def test_backtest_buy_and_sell():
    assert backtest([10, 20, 40], [(0, "buy"), (1, "sell")], 100) == pytest.approx(200)


def test_backtest_still_holding_at_the_end():
    assert backtest([10, 20, 40], [(0, "buy")], 100) == pytest.approx(400)


def test_backtest_no_trades():
    assert backtest([10, 20], [], 100) == pytest.approx(100)


def test_backtest_ignores_trades_that_do_not_apply():
    trades = [(0, "buy"), (1, "buy"), (2, "sell")]
    assert backtest([10, 20, 40], trades, 100) == pytest.approx(400)
    assert backtest([10, 20, 40], [(1, "sell")], 100) == pytest.approx(100)


def test_backtest_round_trips():
    trades = [(0, "buy"), (1, "sell"), (2, "buy"), (3, "sell")]
    assert backtest([10, 20, 10, 30], trades, 100) == pytest.approx(600)


def test_best_windows():
    short, long, value = best_windows(ZIGZAG, [1, 2], [3], 100)
    assert (short, long) == (1, 3)
    assert value == pytest.approx(backtest(ZIGZAG, signals(ZIGZAG, 1, 3), 100))


def test_best_windows_skips_invalid_pairs():
    # (3, 3) would never trade and keep the 100, beating the losing (2, 3).
    short, long, value = best_windows(ZIGZAG, [3, 2], [3], 100)
    assert (short, long) == (2, 3)
    assert value < 100


def test_best_windows_ties_keep_the_first():
    assert best_windows([5, 5, 5, 5, 5], [2, 1], [4, 3], 100) == (2, 4, 100)


def test_best_windows_on_prices():
    short, long, value = best_windows(PRICES, [2, 3, 5], [8, 10, 15], 1000)
    assert value == pytest.approx(backtest(PRICES, signals(PRICES, short, long), 1000))
    for s in [2, 3, 5]:
        for k in [8, 10, 15]:
            assert value >= backtest(PRICES, signals(PRICES, s, k), 1000) - 1e-9


def test_inputs_not_modified():
    xs: list[float] = [3, 1, 2]
    running_total(xs)
    moving_average(xs, 2)
    daily_changes(xs)
    signals(xs, 1, 2)
    assert xs == [3, 1, 2]


# Part 2: your SIGNAL_CASES


def test_enough_cases():
    assert len(SIGNAL_CASES) >= 5, "write at least 5 SIGNAL_CASES"


def test_cases_are_correct():
    for prices, short, long, expected in SIGNAL_CASES:
        assert signals(prices, short, long) == expected, (
            f"SIGNAL_CASES has ({prices}, {short}, {long}, {expected})"
        )


def test_cases_cover_the_main_situations():
    expected_lists = [expected for _, _, _, expected in SIGNAL_CASES]
    actions = [{action for _, action in expected} for expected in expected_lists]
    assert [] in expected_lists, "add a case with no signals"
    assert {"buy", "sell"} in actions, "add a case with both a buy and a sell"
    assert any(short > 1 for _, short, _, _ in SIGNAL_CASES), (
        "add a case with short > 1"
    )


def averages_tied_day_before(p: list[float], d: int, short: int, long: int) -> bool:
    return sum(p[d - short : d]) / short == sum(p[d - long : d]) / long


def test_cases_include_a_signal_right_after_a_tie():
    assert any(
        averages_tied_day_before(p, d, short, long)
        for p, short, long, expected in SIGNAL_CASES
        for d, _ in expected
    ), "add a case where the averages are equal on the day before a signal"


# Each buggy version is built from your (correct) signals, then broken in one way.
BUGGY_VERSIONS: dict[str, Callable[[list[float], int, int], list[tuple[int, str]]]] = {
    "reports every signal a day late": lambda p, s, k: [
        (d + 1, a) for d, a in signals(p, s, k)
    ],
    "reports every signal a day early": lambda p, s, k: [
        (d - 1, a) for d, a in signals(p, s, k)
    ],
    "swaps buy and sell": lambda p, s, k: [
        (d, "sell" if a == "buy" else "buy") for d, a in signals(p, s, k)
    ],
    "misses the first signal": lambda p, s, k: signals(p, s, k)[1:],
    "misses the last signal": lambda p, s, k: signals(p, s, k)[:-1],
    "stops after two signals": lambda p, s, k: signals(p, s, k)[:2],
    "uses a short window one day too long": lambda p, s, k: signals(p, s + 1, k),
    "uses a long window one day too long": lambda p, s, k: signals(p, s, k + 1),
}


@pytest.mark.parametrize("bug", BUGGY_VERSIONS)
def test_cases_catch_bug(bug: str):
    buggy = BUGGY_VERSIONS[bug]
    caught = any(buggy(p, s, k) != expected for p, s, k, expected in SIGNAL_CASES)
    assert caught, f"none of your SIGNAL_CASES catches a signals that {bug}"


# Part 3: the fee


def test_fee_on_buy_and_sell():
    trades = [(0, "buy"), (1, "sell")]
    assert backtest([10, 20], trades, 101, fee=1) == pytest.approx(199)


def test_fee_while_still_holding():
    assert backtest([10, 20], [(0, "buy")], 101, fee=1) == pytest.approx(200)


def test_fee_only_on_trades_that_happen():
    trades = [(0, "buy"), (1, "buy"), (1, "sell"), (1, "sell")]
    assert backtest([10, 20], trades, 101, fee=1) == pytest.approx(199)


def test_fee_skips_a_buy_you_cannot_afford():
    assert backtest([10, 20], [(0, "buy")], 1, fee=1) == pytest.approx(1)
    assert backtest([10, 20], [(0, "buy")], 0.5, fee=1) == pytest.approx(0.5)
