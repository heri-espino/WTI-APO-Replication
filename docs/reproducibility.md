# Reproducibility scope

**Current status:** Mathematical source modules and unit tests are openly available. A complete third-party reproduction of historical WTI market marks, vendor implied-volatility vintages, or the manuscript's large synthetic experiment is **not** established.

| Layer | Public now | Excluded or incomplete |
|---|---|---|
| Physical GBM inference | Return simulator, likelihood, Metropolis, numerical tests | Licensed observed returns |
| Posterior volatility | Gaussian drift-marginal quadrature on a specified grid, analytic comparison tests | Full manuscript's 10-million-history output |
| Risk-neutral option values | Arithmetic Asian control-variate MC, partially fixed one-factor APO MC, synthetic numerical invariants | Verified exchange settlement model and entire original empirical pipeline |
| Experiment | `experiment001` synthetic PI–PM demonstration with deterministic seed | Published aggregate mechanism maps and raw result archive |
| Market inputs | Public numerical interface documented in `data_contract.md` | Barchart and Databento raw records, full timing audit |
| Release environment | Python package and editable Conda environment | Fully pinned platform lock and independent long-run verification |

## Explicit method boundary

The source models physical historical log returns as `N((mu-sigma^2/2)dt, sigma^2 dt)` and evaluates volatility inference using stated Gaussian/inverse-gamma priors. Pricing uses a risk-neutral one-factor forward fixing model and discounts option payoffs. **Physical drift does not enter risk-neutral pricing.**

Posterior integration (`PI`) is `E[C(sigma)|D]`, while posterior mean plug-in (`PM`) is `C(E[sigma|D])`. The synthetic experiment supplies invented returns and fixing values, computes both prices, and reports `PI-PM`. The sign is not guaranteed a priori.

## Install and verify

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python scripts/verify_public_scaffold.py
python scripts/validate_release_metadata.py
python -m experiments.experiment001.run --seed 2026 --pricing-paths 1024
```

## Full manuscript replication gate

To claim reproducibility of particular published empirical tables, add a reviewed input-schema implementation, documented eligibility and historical information cutoffs, source-specific licensed-data acquisition instructions, tested numerical configuration/seeds, reproducible output hashes, and a verification ledger against the actual publication numbers. These requirements are not fulfilled by the current synthetic tests.

See [scientific methods](scientific_methods.md), [release manifest](release_manifest.md), and [Zenodo guidance](zenodo_release.md).
