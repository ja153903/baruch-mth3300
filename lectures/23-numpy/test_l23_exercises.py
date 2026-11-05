import math

import numpy as np

from l23_exercises import cumulative_return, normalize_prices


def test_normalize_prices():
    assert np.allclose(normalize_prices(np.array([50.0, 55.0, 45.0])), [1.0, 1.1, 0.9])


def test_cumulative_return():
    assert math.isclose(cumulative_return(np.array([0.10, -0.10])), -0.01)
    assert math.isclose(cumulative_return(np.array([])), 0.0)
