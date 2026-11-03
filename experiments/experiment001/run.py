"""Small synthetic posterior-integration versus plug-in pricing experiment.

No proprietary market data or empirical statements are used.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from wti_apo_replication.gbm_inference import gbm_log_returns
from wti_apo_replication.sigma_quadrature import posterior_sigma_quadrature
from wti_apo_replication.average_price_option import wti_average_price_option_mc


def calculate(*, seed: int = 2026, pricing_paths: int = 1024,
              grid_points: int = 129) -> dict[str, object]:
    """Evaluate PI and PM using a common random-number stream."""
    if grid_points < 17 or pricing_paths < 2:
        raise ValueError("Require grid_points>=17 and pricing_paths>=2")
    dt = 1 / 252
    returns = gbm_log_returns(mu=0.08, sigma=0.25, dt=dt,
                              n_obs=126, seed=seed)
    sigma_grid = np.linspace(0.04, 0.90, grid_points)
    posterior = posterior_sigma_quadrature(
        sigma_grid, n_obs=len(returns),
        sum_returns=float(returns.sum()),
        sumsq_returns=float(np.sum(returns**2)), dt=dt)
    weights = np.asarray(posterior.weights).reshape(-1)
    mean = float(np.asarray(posterior.mean).item())
    variance = float(np.asarray(posterior.variance).item())
    kwargs = dict(
        realized_fixings=np.array([99., 101., 100.]),
        forward_fixings=np.array([102., 101., 99., 100.]),
        fixing_times=np.array([1., 2., 4., 7.])/252,
        strike=101., rate=0.03, time_to_expiry=7./252,
        option_type="call", n_paths=pricing_paths, seed=seed+1)
    by_sigma = np.array([
        wti_average_price_option_mc(sigma=float(s), **kwargs).price
        for s in sigma_grid])
    pi = float(np.dot(weights, by_sigma))
    pm = float(wti_average_price_option_mc(sigma=mean, **kwargs).price)
    return dict(experiment="experiment001", status="synthetic_only",
                seed=seed, n_return_observations=126,
                pricing_paths_per_sigma=pricing_paths,
                sigma_grid_points=grid_points,
                sigma_posterior_mean=mean,
                sigma_posterior_variance=variance,
                pi_price=pi, pm_price=pm, pi_minus_pm=pi-pm,
                market_data_used=False)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--pricing-paths", type=int, default=1024)
    parser.add_argument("--grid-points", type=int, default=129)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    body = json.dumps(calculate(seed=args.seed,
                                pricing_paths=args.pricing_paths,
                                grid_points=args.grid_points),
                      sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(body, encoding="utf-8")
        print("Saved", args.output)
    else:
        print(body, end="")


if __name__ == "__main__":
    main()
