import math

import numpy as np

from hw13 import daily_returns, portfolio_return, zscore


def test_daily_returns():
    prices = np.array([100.0, 110.0, 99.0])
    assert np.allclose(daily_returns(prices), [0.10, -0.10])


def test_zscore():
    z = zscore(np.array([1.0, 2.0, 3.0, 4.0, 5.0]))
    assert math.isclose(z.mean(), 0, abs_tol=1e-12)
    assert math.isclose(z.std(), 1)
    assert z[0] < z[-1]


def test_portfolio_return():
    weights = np.array([0.5, 0.3, 0.2])
    returns = np.array([0.10, -0.05, 0.02])
    assert math.isclose(portfolio_return(weights, returns), 0.039)
    assert isinstance(portfolio_return(weights, returns), float)
