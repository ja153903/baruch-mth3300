from l13_exercises import (
    apply_splits,
    count_allocations,
    first_trade_day,
    letter_frequencies,
    net_positions,
    order_total,
    tickers_above,
    top_holding,
)

PRICES = {"AAPL": 190.5, "MSFT": 410.25, "NVDA": 120.0}


def test_tickers_above():
    unsorted = {"MSFT": 410.25, "AAPL": 190.5, "NVDA": 120.0}
    assert tickers_above(unsorted, 150) == ["AAPL", "MSFT"]
    assert tickers_above(unsorted, 500) == []
    assert tickers_above({}, 0) == []


def test_order_total():
    menu = {"coffee": 3.0, "bagel": 2.5}
    assert order_total(menu, []) == 0
    assert order_total(menu, ["coffee", "bagel", "coffee"]) == 8.5
    assert order_total(menu, ["tea"]) == 0


def test_letter_frequencies():
    assert letter_frequencies("") == {}
    assert letter_frequencies("Aa b!") == {"a": 2, "b": 1}


def test_net_positions():
    assert net_positions([("AAPL", "buy", 10), ("AAPL", "sell", 4)]) == {"AAPL": 6}
    trades = [
        ("MSFT", "buy", 5),
        ("NVDA", "buy", 8),
        ("MSFT", "sell", 5),
        ("NVDA", "buy", 2),
    ]
    assert net_positions(trades) == {"NVDA": 10}
    assert net_positions([]) == {}


def test_apply_splits():
    holdings = {"NVDA": 3, "AAPL": 10}
    assert apply_splits(holdings, {"NVDA": 10}) == {"NVDA": 30, "AAPL": 10}
    assert holdings == {"NVDA": 3, "AAPL": 10}
    assert apply_splits(holdings, {}) == {"NVDA": 3, "AAPL": 10}
    assert apply_splits({}, {"TSLA": 3}) == {}


def test_first_trade_day():
    assert first_trade_day(["AAPL", "MSFT", "AAPL"]) == {"AAPL": 0, "MSFT": 1}
    assert first_trade_day(["NVDA", "NVDA", "NVDA"]) == {"NVDA": 0}
    assert first_trade_day([]) == {}


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


def test_top_holding():
    assert top_holding({"AAPL": 10, "MSFT": 5, "NVDA": 8}, PRICES) == "MSFT"
    assert top_holding({"AAPL": 10, "XYZ": 1000}, PRICES) == "AAPL"
    assert top_holding({"XYZ": 5}, PRICES) is None
    assert top_holding({}, PRICES) is None
