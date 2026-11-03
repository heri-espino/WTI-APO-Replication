# WTI APO Replication

**Status: pre-release `0.1.0.dev0`. Reproducible mathematical methods and a synthetic PI–PM experiment are available; manuscript-scale and market-data results are not reproduced.**

This public software package is independently versioned from the author's private WTI research workspace. It contains an **audited, code-only subset** of the actual research methods: physical-measure GBM volatility inference, marginal volatility-posterior quadrature, risk-neutral arithmetic Asian option valuation, a one-factor partially fixed WTI-like average-price option pricer, and a Curran geometric-conditioning approximation. The original synthetic ten-million-history mechanism-map driver and its archived scenario summaries are also available.

No commercial Barchart/Databento records, private Git history, market-derived rows, or confidential vendor data have been imported.

## Setup

Requires Python 3.11+.

```bash
conda env create -f environment.yml
conda activate wti-apo-replication
python -m pytest -q
```

Or use `python -m pip install -e ".[dev]"` in a Python environment. Dependency ranges are provided for development; a verified publication lockfile is still required.

## Run a transparent synthetic PI–PM experiment

```bash
python -m experiments.experiment001.run --seed 2026 --pricing-paths 1024
```

This independently generates physical-measure GBM returns, integrates over a posterior volatility grid, and compares the posterior-integrated option value with the value at posterior-mean volatility using common random numbers. **All fixing values and futures levels are artificial.**

To save the summary for versioned review:

```bash
python -m experiments.experiment001.run --seed 2026 --pricing-paths 1024 --output results/experiment001/summary.json
```

The full report and production-scale numerical evidence have **not** been certified for reproduction here. See [experiment001](experiments/experiment001/README.md), [released methods](docs/scientific_methods.md), [data input contract](docs/data_contract.md) and [limitations](docs/reproducibility.md).

The pre-existing standalone spot-GBM instructional demonstration remains available as `wti-apo-synthetic --seed 2026`.

## Synthetic mechanism map and archived results

[experiment002](experiments/experiment002/README.md) contains the original dense-grid 10-million-history computational design and the executable mechanism-map driver. The historical run's synthetic summaries (5,880 rows over 168 scenarios) and redacted report are in [the archive](results/experiment002/archive_10m/). Those aggregates are **historical**, not a newly reproduced run on this repository; the run requires substantial CPU/GPU resources and remains manual-only.

```bash
python -m experiments.experiment002.run --preset quick --backend numpy
```

## Public methods

- `wti_apo_replication.gbm_inference`
- `wti_apo_replication.sigma_quadrature`
- `wti_apo_replication.asian_pricing`
- `wti_apo_replication.average_price_option`
- `wti_apo_replication.curran_approximation`

The release manifest records the original internal blob identifiers of the curated source and its unit tests without transferring the private repository's history. The numerical assumptions include a **single shared Brownian risk factor for remaining forward fixings**, which should not be interpreted as the actual exchange settlement model.

## Archiving and legal status

This original public code is MIT licensed; **vendor market data and rights-restricted derived results are excluded**. Reproducing empirical results requires separately licensed source data, as-of-date provenance and eligibility rules.

[Software citation](CITATION.cff) · [License](LICENSE) · [Release manifest](docs/release_manifest.md) · [Zenodo release guide](docs/zenodo_release.md) · [Agent instructions](AGENTS.md) · [Handoff](HANDOFF.md)

No GitHub Release or Zenodo DOI exists yet. A DOI will identify the exact archived software version, not certify the full scientific study.
