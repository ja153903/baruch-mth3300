# Warmup


def tickers_above(prices: dict[str, float], threshold: float) -> list[str]:
    """The tickers whose price is above threshold, in alphabetical order.

    tickers_above({"MSFT": 410.25, "AAPL": 190.5, "NVDA": 120.0}, 150) == ["AAPL", "MSFT"]
    """
    raise NotImplementedError


def order_total(menu: dict[str, float], order: list[str]) -> float:
    """Sum the prices of the items ordered. Items that aren't on the menu cost 0."""
    raise NotImplementedError


# Core


def letter_frequencies(text: str) -> dict[str, int]:
    """Count letters only (str.isalpha), case-insensitive."""
    raise NotImplementedError


def net_positions(trades: list[tuple[str, str, int]]) -> dict[str, int]:
    """The shares you hold in each ticker after a list of (ticker, side, shares) trades.

    side is "buy" or "sell". Leave out tickers you no longer hold.
    net_positions([("AAPL", "buy", 10), ("AAPL", "sell", 4)]) == {"AAPL": 6}
    """
    raise NotImplementedError


def apply_splits(holdings: dict[str, int], splits: dict[str, int]) -> dict[str, int]:
    """A new dict of holdings after stock splits. Don't change holdings.

    splits maps a ticker to its split ratio: {"NVDA": 10} means each NVDA share
    becomes 10 shares. Tickers without a split keep their shares.
    """
    raise NotImplementedError


# Fix the AI's code: this has a bug. Find it, then fix it.


def first_trade_day(tickers: list[str]) -> dict[str, int]:
    """tickers[d] is the ticker traded on day d. Map each ticker to the first day it was traded.

    first_trade_day(["AAPL", "MSFT", "AAPL"]) == {"AAPL": 0, "MSFT": 1}
    """
    days: dict[str, int] = {}
    for day, ticker in enumerate(tickers):
        days[ticker] = day
    return days


# Stretch


def count_allocations(
    portfolios: list[dict[str, float]],
) -> dict[frozendict[str, float], int]:
    """Count how many times each portfolio appears. Use frozendict(portfolio) as the key."""
    raise NotImplementedError


def top_holding(holdings: dict[str, int], prices: dict[str, float]) -> str | None:
    """The ticker whose position (shares times price) is worth the most.

    Skip tickers that have no price. Return None if none of them has a price.
    """
    raise NotImplementedError
