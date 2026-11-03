# v1.0.0 verification — software and synthetic benchmarks only

**Release scope: software-and-synthetic**

**Not verified: licensed-market empirical results**

**Author approval:** 2026-11-03. The approved public artifact is a software package with curated Bayesian inference and Asian-option methods, reproducible synthetic checks, a historical synthetic aggregate archive, offline empirical processing scripts, and instructions for users who separately obtain licensed inputs. This is **not** an assertion that the manuscript's market pricing/error tables have been independently reproduced.

## Evidence verified before preparing v1.0.0

1. **Automated scientific and packaging-input checks.** The merged public-repository workflow [#41704816775](https://github.com/heri-espino/WTI-APO-Replication/actions/runs/41704816775), commit `93233d4010d637225cddddb4055d5a62fbd60f3f`, completed with **75 passing pytest tests and one warning**. Installation, CFF schema validation, public source safety scan, numerical synthetic checks and offline empirical CLI import/help checks passed. The final tagged release commit must repeat these checks.
2. **Experiment001.** Fixed seed 2026, 63 generated Gaussian-GBM return observations, 301 sigma quadrature nodes. From the committed `results/synthetic/experiment001.json`: PI = 1.0083270816192058; PM = 1.0077629439307587; PI−PM = 0.0005641376884470972; posterior mean sigma = 0.24739605304318488. A regression test recomputes the result using fixed tolerances.
3. **Experiment002.** The historical data-free 10,000,000-history synthetic mechanism-map source and aggregate archive are preserved. Automated tests check small deterministic synthetic cells and aggregate file structure (5,880 scenario rows, 35 posterior-cell summaries, 168 scenarios and 100 ranked rows); **the entire 10M experiment has not been independently rerun from the public repository**.
4. **Software scope.** The included Bayesian, Asian futures, partial-fixing and Curran components are checked by unit tests on synthetic inputs. The original market-data workflow cannot be completely evaluated without commercial datasets and publication-vintage auditing.
5. **Environment.** Python 3.11.17 and selected library versions were recorded from earlier Linux CI in `docs/environment_audit.md`. `environment.yml` gives an installable Conda starting point, **not** a fully locked, cross-platform computational environment.
6. **Release rights and privacy.** The author approved releasing author-controlled code and synthetic aggregates under MIT to the extent of their rights. Commercial Barchart/Databento records, private research history, secrets and unreviewed market-derived tables are excluded. Automated scans are helpful but cannot independently guarantee every right or disclosure obligation.

## Validation commands

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python scripts/verify_public_scaffold.py
python scripts/validate_release_metadata.py --release
cffconvert --validate
```

The release workflow also builds and checks a wheel and source distribution **when manually invoked**. It does not run expensive simulations or create tags on commits/pushes.

## Scientific and publication limitations

These results are **conditional numerical demonstrations** of posterior integration, plug-in pricing and selected Asian-option approximations, not executable trading forecasts or independent exchange-settlement validation. The 10-million history archive is a historical computation with structure/source audit, not an independent rerun. The manuscript's 310-observation and 2,381-observation commercial-data comparisons, implied-volatility cutoffs, vendor timestamp availability, market-price proxies and third-party redistribution rights remain outside this verification.

The software version `1.0.0` and its eventual GitHub tag `v1.0.0` identify a stable public **software artifact**, not the completeness of replication of every scientific result. A Zenodo DOI, once actually assigned, identifies the archived software version only.
