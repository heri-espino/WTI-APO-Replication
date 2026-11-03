# WTI APO Replication v1.0.0 — software and synthetic-evidence release

This **stable software version (1.0.0)** includes Bayesian inference and Asian-option valuation methods, synthetic regression tests, recorded synthetic option-pricing evidence, and a historical 10-million-history synthetic mechanism-map aggregate. Offline analysis scripts can consume separately licensed market inputs.

**Verification:** See docs/environment_audit.md, docs/reproducibility.md, docs/release_manifest.md, and the GitHub Actions run for the release.

**Limitations:** This is a **software and synthetic-evidence archive**, not an independent reproduction of the paper's commercial-data results. Barchart and Databento observations are third-party licensed and excluded. Vendor publication-vintage and end-of-day price-proxy limitations remain. Historical large synthetic aggregates were not independently rerun at production scale in public CI.

No prospective trading advantage or exact exchange-model implementation is claimed.
