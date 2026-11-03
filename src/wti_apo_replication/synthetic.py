"""Independent synthetic arithmetic-Asian call Monte Carlo demonstration.

This is a deliberately *simplified spot-GBM example*, not the manuscript's
WTI futures-curve model and not empirical replication. There are no market
data inputs. The function is designed as a small, reproducible smoke test.

Under the risk-neutral model S(t)=S0 exp((r-sigma^2/2)t+sigma W(t)), the
discounted payoff is exp(-rT) max(mean(S(T*j/n), j=1..n) - K, 0).
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass

import numpy as np


@dataclass(frozen=True)
class Estimate:
    """Monte Carlo result in the same units as the synthetic input price."""

    price: float
    standard_error: float
    paths: int
    seed: int


def arithmetic_asian_call_mc(
    *,
    spot: float,
    strike: float,
    rate: float,
    volatility: float,
    maturity: float,
    observations: int,
    paths: int,
    seed: int = 2026,
    batch_size: int = 2048,
) -> Estimate:
    """Estimate a fixed-strike arithmetic-average call using synthetic GBM paths.

    Observation times are equally spaced in (0,T], excluding the initial spot.
    The standard error uses the sample variance of discounted path payoffs.
    Batches avoid allocating a full (paths x observations) simulation matrix.
    """
    for name, value in (
        ("spot", spot), ("strike", strike), ("rate", rate),
        ("volatility", volatility), ("maturity", maturity),
    ):
        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite")
    if spot <= 0 or strike < 0 or volatility < 0 or maturity <= 0:
        raise ValueError("Require spot>0, strike>=0, volatility>=0, maturity>0")
    for name, value, minimum in (
        ("observations", observations, 1),
        ("paths", paths, 2),
        ("batch_size", batch_size, 1),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
            raise ValueError(f"{name} must be an integer >= {minimum}")
    if isinstance(seed, bool) or not isinstance(seed, int) or seed < 0:
        raise ValueError("seed must be a non-negative integer")

    rng = np.random.default_rng(seed)
    dt = maturity / observations
    drift = (rate - 0.5 * volatility**2) * dt
    diffusion = volatility * math.sqrt(dt)
    discount = math.exp(-rate * maturity)
    total = 0.0
    squares = 0.0
    remaining = paths

    while remaining:
        n = min(batch_size, remaining)
        increments = drift + diffusion * rng.standard_normal((n, observations))
        simulated = np.exp(math.log(spot) + np.cumsum(increments, axis=1))
        average = simulated.mean(axis=1)
        discounted = discount * np.maximum(average - strike, 0.0)
        total += float(np.sum(discounted))
        squares += float(np.sum(discounted * discounted))
        remaining -= n

    price = total / paths
    variance = max(0.0, (squares - paths * price**2) / (paths - 1))
    standard_error = math.sqrt(variance / paths)
    return Estimate(price, standard_error, paths, seed)


def main() -> None:
    """Print a reproducible synthetic reference estimate; no market data used."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spot", type=float, default=100.0)
    parser.add_argument("--strike", type=float, default=100.0)
    parser.add_argument("--rate", type=float, default=0.03)
    parser.add_argument("--volatility", type=float, default=0.25)
    parser.add_argument("--maturity", type=float, default=1.0)
    parser.add_argument("--observations", type=int, default=12)
    parser.add_argument("--paths", type=int, default=4096)
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()
    result = arithmetic_asian_call_mc(**vars(args))
    print(json.dumps(asdict(result), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
