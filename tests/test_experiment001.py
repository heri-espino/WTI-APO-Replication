"""Fast, synthetic-only smoke test for the numbered experiment."""
import numpy as np
from experiments.experiment001.run import calculate

def test_reproducible_pi_pm():
    first=calculate(seed=104,pricing_paths=128,grid_points=33)
    second=calculate(seed=104,pricing_paths=128,grid_points=33)
    assert first==second
    assert first["market_data_used"] is False
    assert first["status"]=="synthetic_only"
    assert np.isfinite(first["pi_price"])
    assert np.isclose(first["pi_minus_pm"],first["pi_price"]-first["pm_price"])
    assert first["sigma_posterior_variance"]>=0
