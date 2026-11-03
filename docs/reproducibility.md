# Reproducibility plan (not yet a released package)

This document describes the **release criteria**; it does not claim that the manuscript can already be reproduced from this public repository.

## Replication boundaries

| Layer | Planned material | Current public availability |
|---|---|---|
| Deterministic methods and simulations | Reviewed implementation, tests, seed/configuration and synthetic examples | Not released |
| Commercial WTI APO/futures observations | Provider identifiers, retrieval schema, date cutoffs, processing instructions | Raw observations not released; licensing required |
| Empirical analysis | Reviewed processing and valuation scripts with configurable licensed-data input | Not released |
| Results and figures | Approved aggregate tables, provenance hashes, scripts for regenerating figures | Not released; rights review pending |
| Environment | Pinned dependencies, platform-specific instructions and verification commands | Not released |

## Minimum release requirements

1. Select only reviewed source files from the private development workspace, without importing its Git history.
2. Audit the license for every included library, file, plot and derived numerical result. Exclude raw Barchart/Databento records and any restricted derivatives.
3. Provide an independently runnable synthetic example with fixed seed, assumptions, expected tolerance and test results.
4. Document how separately licensed market inputs must be obtained. Avoid suggesting that private or commercial data can be requested from the author without provider permission.
5. Include clean-environment installation instructions, exact code version, test commands and scripts to regenerate each publicly reproducible table/figure.
6. Label results that cannot be reproduced without licensed data. Distinguish reproduction from partial or synthetic verification.
7. Obtain explicit author approval for the audited public release, and add a license and citation metadata only after the appropriate rights and double-anonymized-review assessment.
8. Revisit this page to replace each "Not released" cell with a verified release path or a justified limitation.

## Scientific conventions

Physical-measure inference and risk-neutral valuation are different stages. Any replication scripts must specify model assumptions, settlement-proxy status, information cutoffs, volatility-estimator definitions and limitations on claims of prospective forecasting or trading advantage. Do not infer missing empirical results from manuscript prose.

## Current verification

The public CI only checks repository safety and documentation consistency. **It does not execute the paper's numerical experiments.**
