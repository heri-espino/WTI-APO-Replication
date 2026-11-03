"""experiment001: reproducible, data-free PI-versus-PM numerical illustration.

Synthetic physical-measure GBM returns and the author's Gaussian marginal
sigma quadrature are combined with a one-factor Curran-style arithmetic
futures-option approximation. This tiny experiment does not reproduce
published numerical tables or exercise commercial market data.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from bayesian_asian_options.bayesian_gbm import gbm_log_returns
from bayesian_asian_options.gaussian_sigma_quadrature import posterior_sigma_quadrature
from bayesian_asian_options.asian_futures_pricing import curran_arithmetic_futures_option


def run_experiment(*, seed: int = 2026, grid_points: int = 301) -> dict:
    """Compute one small PI–PM comparison with fully specified synthetic inputs."""
    if grid_points < 51 or grid_points % 2 != 1:
        raise ValueError("grid_points must be odd and >=51")
    dt = 1.0 / 252.0
    history = gbm_log_returns(
        mu=0.07, sigma=0.25, dt=dt, n_obs=63, seed=seed
    )
    grid = np.linspace(0.03, 1.50, grid_points)
    posterior = posterior_sigma_quadrature(
        grid,
        n_obs=len(history),
        sum_returns=float(np.sum(history)),
        sumsq_returns=float(np.dot(history, history)),
        dt=dt,
        mu_prior_sd=1.0,
        sigma_prior_alpha=2.0,
        sigma_prior_beta=0.1,
    )
    mean_sigma = float(np.asarray(posterior.mean).reshape(-1)[0])
    variance_sigma = float(np.asarray(posterior.variance).reshape(-1)[0])
    weights = np.asarray(posterior.weights).reshape(-1)

    realized = np.array([100.4, 99.9, 100.2])
    remaining = np.array([100.8, 101.0, 100.9, 101.3, 101.2, 101.1])
    times = np.arange(1, len(remaining) + 1, dtype=float) / 365.0
    df = math.exp(-0.04 * float(times[-1]))

    def price(sig: float) -> float:
        return curran_arithmetic_futures_option(
            realized_fixings=realized,
            forward_fixings=remaining,
            fixing_times=times,
            strike=100.0,
            sigma=sig,
            discount_factor=df,
            option_type="call",
        )

    price_nodes = np.array([price(float(sig)) for sig in grid])
    posterior_integrated = float(weights @ price_nodes)
    plug_in = float(price(mean_sigma))
    return {
        "experiment": "experiment001",
        "kind": "synthetic_only",
        "seed": seed,
        "historical_return_count": len(history),
        "sigma_grid_points": grid_points,
        "posterior_sigma_mean": mean_sigma,
        "posterior_sigma_variance": variance_sigma,
        "pi_price": posterior_integrated,
        "pm_price": plug_in,
        "pi_minus_pm": posterior_integrated - plug_in,
        "posterior_weights_sum": float(weights.sum()),
        "model": "Gaussian physical-measure GBM + Curran one-factor futures Asian approximation",
        "data": "synthetic fixed inputs only; no vendor or market observations",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--grid-points", type=int, default=301)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_experiment(seed=args.seed, grid_points=args.grid_points)
    formatted = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(formatted, encoding="utf-8")
    else:
        print(formatted, end="")


if __name__ == "__main__":
    main()
