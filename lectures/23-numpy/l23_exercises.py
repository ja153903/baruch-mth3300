import numpy as np


def normalize_prices(prices: np.ndarray) -> np.ndarray:
    """Divide every price by the first one, so the series starts at 1.0. No loops."""
    raise NotImplementedError


def cumulative_return(returns: np.ndarray) -> float:
    """The total return from compounding a series of period returns: product(1 + r) - 1."""
    raise NotImplementedError
