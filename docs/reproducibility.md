# Reproducibility boundaries

**Pre-release:** The package is installable and its illustrative synthetic model is testable, but the manuscript's WTI APO empirical and Bayesian analyses are **not publicly replicated yet**.

| Layer | Present | Missing for manuscript replication |
|---|---|---|
| Python packaging | `pyproject.toml`, Conda environment, installation and CI tests | Fully frozen, cross-platform publication environment |
| Synthetic arithmetic Asian | Independent risk-neutral spot-GBM Monte Carlo example; fixed seed and zero-volatility tests | Paper-specific futures term structure and volatility-posterior integration |
| Commercial market observations | None | Authorized provider inputs and acquisition instructions |
| Empirical numerical results | None | Reviewed scripts, rights-cleared aggregates and result audits |
| Publication figures/tables | None | Source-to-figure code, configuration and verified numerical comparisons |

## Synthetic demonstration

For `S_t = S_0 exp((r - sigma^2/2)t + sigma W_t)`, monitor `n` equally spaced times `t_j = jT/n`. The estimated discounted payoff is

`exp(-r T) max(n^{-1} sum_j S_{t_j} - K, 0)`.

The implementation uses seeded, batched NumPy pseudo-random sampling and returns a sample standard error. It is **not** an empirical WTI futures-curve, partially fixed average, or posterior-integrated pricing model.

Run:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python scripts/verify_public_scaffold.py
python scripts/validate_release_metadata.py
wti-apo-synthetic --seed 2026 --paths 4096 --observations 12
```

For a future publication release, add tested numerical configurations, independent source and model checks, approved derived outputs, exact environment provenance and documentation mapping each claimed figure and table to a reproducible command.
