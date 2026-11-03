# Reproducible environment and numerical evidence audit

**Date:** 2026-11-03. **Code revision:** `fee20d6e9c60784cb21a8229d26aeec04589b429`.

The public GitHub Actions workflow [#41687743436](https://github.com/heri-espino/WTI-APO-Replication/actions/runs/41687743436) completed successfully after the synthetic ten-million archive was merged.

## Recorded environment (CI installation log)

- Python: 3.11.17
- NumPy: 2.4.6
- SciPy: 1.17.1
- pandas: 2.3.3
- pytest: 9.2.0
- PyYAML: 6.0.3
- cffconvert: 2.0.0

**Validation:** 69 tests passed, one warning; the workflow also validated package installation, citation metadata, and the synthetic-only artifact safety audit. These are the **observed CI versions**, not a fully resolved, cross-platform lockfile. Optional CUDA/CuPy packages were not verified by this Linux CI job.

## Evidence classes

1. **Unit-tested mathematical core:** GBM posterior inference, volatility quadrature, Asian/futures pricing, partial fixings, Curran approximation and input adapters (synthetic fixtures only).
2. **Synthetic reference output:** `results/synthetic/experiment001.json`, checked by CI.
3. **Historically generated synthetic experiment:** `results/experiment002/archive_10m/`, containing the reported 10,000,000 synthetic-history aggregates and a redacted run manifest. Source and aggregate counts were audited; it was **not** independently rerun in this public environment.
4. **Not reproduced:** the manuscript's Barchart/Databento market observations, 310-sample and 2,381-row empirical price-proxy comparisons, vendor publication-vintage assumptions and contract/valuation-specific volatility inputs.

## Release classification

Current quality level: **tested partial-methods archive, not full-manuscript replication**. Do not change the `--release` gate to pass merely because the unit tests pass or an archived historical result exists. A future first release may be explicitly scoped to methods and synthetic evidence after rights review, independent numerical convergence checks and explicit approval.

## v1.0.0 preparation audit

The merged release-workflow commit `93233d4010d637225cddddb4055d5a62fbd60f3f` passed **75 tests with one warning** on [Actions run 41704816775](https://github.com/heri-espino/WTI-APO-Replication/actions/runs/41704816775), including installation, syntax/import tests, CFF schema validation, synthetic reference comparison and public-data safety checks. Version-1.0.0 metadata/approval validation is performed on the separate release-preparation PR and must pass again on the final release commit.

The recorded Linux dependency versions above belong to an earlier successful run and remain **observed versions**, not a complete frozen Conda lockfile. The 10-million-history synthetic archive was preserved from a previous run; it has **not** been independently rerun here. The paid-data empirical panels were not verified in public CI.
