"""Invariant checks for synthetic experiment001."""
import math

import pytest

from experiments.experiment001.run import run_experiment


def test_reproducible_synthetic_pi_pm():
    result = run_experiment(seed=2026, grid_points=101)
    assert result == run_experiment(seed=2026, grid_points=101)
    assert result["kind"] == "synthetic_only"
    assert result["historical_return_count"] == 63
    assert math.isclose(result["posterior_weights_sum"], 1.0, abs_tol=1e-12)
    assert 0.0 < result["posterior_sigma_mean"] < 2.0
    assert result["posterior_sigma_variance"] >= 0
    assert result["pi_price"] >= 0 and result["pm_price"] >= 0
    assert result["pi_minus_pm"] == pytest.approx(result["pi_price"] - result["pm_price"])
    assert math.isfinite(result["pi_minus_pm"])


def test_invalid_sigma_quadrature_grid():
    with pytest.raises(ValueError):
        run_experiment(grid_points=50)
