# experiment002 — Large synthetic PI–PM mechanism map

**Source:** Rights-reviewed adaptation of the author's full synthetic mechanism-map driver. It uses Gaussian GBM returns, integrates drift analytically under its Gaussian prior, computes a marginal volatility posterior on a dense grid, and evaluates a Curran-style arithmetic-average futures-option approximation for synthetic scenarios. No Barchart or Databento market observations enter this study.

## Run manually

```bash
python -m pip install -e ".[dev]"
python -m experiments.experiment002.run --preset quick --backend numpy
```

The original **ten-million-history** configuration is retained (seed 2468, 35 cells, 4,097 volatility nodes, 168 option scenarios) but is computationally expensive. **Do not run it through automatic CI:**

```bash
python -m experiments.experiment002.run --preset ten-million --backend cupy
```

A CUDA-compatible CuPy installation and sufficient GPU resources are required for that example. CPU execution is available using `--backend numpy` but may be prohibitively expensive.

The script writes restartable cell checkpoints, configuration and posterior summaries, ranked scenario statistics, and a run report into `results/experiment002/<config-fingerprint>/`. Treat the reported maximum as experiment-size dependent. An independently verified paper-scale rerun is **not** claimed.

## Archived synthetic evidence

A published synthetic-summary snapshot from a previous 10-million-history run is preserved in `results/experiment002/archive_10m/` as a provenance-labelled historical result. It is **not** proof of a fresh public-environment reproduction; the derived aggregates do not involve commercial market observations. See `docs/release_manifest.md` for the original source identifiers.

## Checks and next experiment

Automatic unit tests use only a tiny cell to validate deterministic chunking, seed allocation, and temporary-file cleanup. The next independent comparison should rerun a small scenario on clean Linux and Windows environments, compare means/quantiles and report tolerance and floating-point backend differences; keep all numerical outputs under sequential experiment directories.
