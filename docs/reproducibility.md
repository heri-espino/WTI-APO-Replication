# Reproducibility boundaries

**Pre-release:** The package now includes the author-selected, data-free inference/pricing modules and synthetic tests, but the manuscript's full WTI APO empirical and Bayesian results are **not publicly replicated yet**.

| Layer | Present | Missing for manuscript replication |
|---|---|---|
| Python packaging | `pyproject.toml`, Conda environment, installation and CI tests | Fully frozen, cross-platform publication environment |
| Numerical scientific core | Gaussian/Student-t Bayesian inference, sigma quadrature, Asian futures pricing, first-nearby mapping, partially fixed WTI APO Monte Carlo, Curran approximation, synthetic validation | Full production experiment orchestration and recorded empirical input provenance |
| Synthetic arithmetic Asian | Independent risk-neutral spot-GBM Monte Carlo example; fixed seed and zero-volatility tests | Published experiment configuration and full numerical results |
| Commercial market observations | No raw observations; publicly reviewed parsing interfaces with synthetic tests | Authorized provider inputs and complete acquisition/cutoff instructions |
| Empirical numerical results | None | Reviewed scripts, rights-cleared aggregates and result audits |
| Publication figures/tables | None | Source-to-figure code, configuration and verified numerical comparisons |

## Synthetic demonstration

For `S_t = S_0 exp((r - sigma^2/2)t + sigma W_t)`, monitor `n` equally spaced times `t_j = jT/n`. The estimated discounted payoff is

`exp(-r T) max(n^{-1} sum_j S_{t_j} - K, 0)`.

The implementation uses seeded, batched NumPy pseudo-random sampling and returns a sample standard error. The standalone example is **not** an empirical WTI futures-curve, partially fixed average, or posterior-integrated pricing model. Separate source modules under `src/bayesian_asian_options/` implement such components, but no licensed observations or full market pipeline are provided here.

Run:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python scripts/verify_public_scaffold.py
python scripts/validate_release_metadata.py
wti-apo-synthetic --seed 2026 --paths 4096 --observations 12
```

For a future publication release, add tested numerical configurations, independent source and model checks, approved derived outputs, exact environment provenance and documentation mapping each claimed figure and table to a reproducible command.

## Curated scientific source boundary

The `bayesian_asian_options` package contains the author-controlled numerical routines selected from the private workspace, without commercial records or private history. The curated regression tests exercise only synthetic inputs. Full empirical reproduction requires model configuration, earlier-data cutoffs, licensed market input schemas, transaction/settlement proxy handling, and an independent comparison with every reported table and figure. The original private research tree and LFS data are not redistributed.
