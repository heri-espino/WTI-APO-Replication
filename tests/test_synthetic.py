"""Tests for the independent toy GBM Asian-option illustration."""
import math

import pytest

from wti_apo_replication.synthetic import arithmetic_asian_call_mc


def _demo(**changes):
    args = dict(
        spot=100.0, strike=98.0, rate=0.03, volatility=0.2,
        maturity=1.0, observations=12, paths=128, seed=1234,
        batch_size=20,
    )
    args.update(changes)
    return arithmetic_asian_call_mc(**args)


def test_reproducible_fixed_seed_and_batch_independence():
    a = _demo(batch_size=20)
    b = _demo(batch_size=20)
    c = _demo(batch_size=128)
    assert a == b
    assert a.price == pytest.approx(c.price, abs=1e-12)
    assert a.standard_error == pytest.approx(c.standard_error, abs=1e-12)


def test_zero_volatility_matches_deterministic_formula():
    n = 12
    spot, strike, rate, T = 100.0, 98.0, 0.03, 1.0
    average = sum(spot * math.exp(rate * T * j / n) for j in range(1, n + 1)) / n
    expected = math.exp(-rate * T) * max(average - strike, 0.0)
    actual = _demo(volatility=0.0, observations=n)
    assert actual.price == pytest.approx(expected, abs=1e-10)
    assert actual.standard_error < 1e-7


@pytest.mark.parametrize(
    "changes",
    [
        {"spot": 0.0}, {"strike": -1.0}, {"volatility": -0.2},
        {"maturity": 0.0}, {"paths": 1}, {"observations": 0},
        {"batch_size": 0}, {"seed": -1}, {"rate": float("nan")},
    ],
)
def test_invalid_inputs(changes):
    with pytest.raises(ValueError):
        _demo(**changes)
