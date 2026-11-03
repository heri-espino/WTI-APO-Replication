# Public release manifest — v1.0.0

**Stage: public-release-approved**

**Approved release scope:** Bayesian inference and Asian-option pricing **software with synthetic benchmark evidence** only. The author approved the scoped v1.0.0 release on 2026-11-03. This approval does **not** imply that the manuscript's Barchart/Databento observations, independent empirical settlement-price comparisons, or every paper figure/table can be publicly reproduced.

| Component | Origin and licensing | Verification evidence | v1.0.0 disposition |
|---|---|---|---|
| `src/bayesian_asian_options/` | Author-controlled source selected from the private research workspace, without copying private Git history; MIT approval covers the source the author has the right to license | Synthetic regression tests, code importing and method checks in CI | Included as public scientific software |
| `src/wti_apo_replication/` | Independently written educational synthetic pricing example, MIT | Fixed-seed Monte Carlo and zero-volatility analytic check | Included |
| `experiments/experiment001/`, `results/synthetic/experiment001.json` | Data-free fixed-seed synthetic demonstration | CI regeneration and exact saved-reference regression check; PI 1.0083270816192058, PM 1.0077629439307587, seed 2026 | Included, synthetic only |
| `experiments/experiment002/`, `results/experiment002/archive_10m/` | Data-free mechanism-map source and historically generated aggregate outputs, source provenance recorded in prior archive PR #9 | Small deterministic tests and archived 5,880/35/168/100-row structure checks; **10M-scale run not independently repeated** | Included, marked historical synthetic evidence |
| `experiments/wti_apo_*.py`, `experiments/wti_curran_benchmark.py` | Author-controlled offline empirical orchestration, using separately provided inputs | Import/`--help` smoke checks only; no complete empirical valuation run | Included as methods/source code, not verified empirical replication |
| Barchart/Databento format adapters and public/Yahoo/Treasury helpers | Author-controlled code; vendor observations remain under commercial licenses | Temporary synthetic data-format tests | Code included; separately licensed inputs excluded |
| Package, documentation, citation and release automation | Author-controlled public project, MIT | GitHub CI installation, CFF validation, public-file checks and release metadata gate | Included |
| Raw commercial records, contract-day vendor histories, tokens, LFS objects | Third-party restricted data or sensitive configurations | No license to redistribute; public release safety scan | **Excluded** |
| Manuscript's empirical price-proxy error panels and potentially restricted market-derived figures | May depend on third-party vendor licenses and valuation-time availability assumptions | Not independently reproduced or approved for public redistribution | **Excluded** |
| Private Git history, internal notes, reviewer documents, author correspondence | Private workspace | Explicitly not copied | **Excluded** |

## Source and reproducibility evidence

The latest merged pre-release baseline, [GitHub Actions #41704816775](https://github.com/heri-espino/WTI-APO-Replication/actions/runs/41704816775), passed **75 tests with one warning** on 2026-11-03. Earlier recorded environment details are in [environment_audit.md](environment_audit.md); these are not a platform-independent dependency lockfile.

The [release verification record](verified_replication.md) lists the known findings, numerical uncertainty, and the unverified scope. The tagged v1.0.0 commit must pass the CI checks, strict `scripts/validate_release_metadata.py --release`, citation schema, and the manual distribution build before a GitHub Release is created. Any change to files or contents must be verified again at the final SHA.

**Release approval is for public distribution of this scoped software and synthetic benchmark set, not a finding that the entire paper has been replicated.**

## Later releases

Before adding more files, review each proposed artifact's source commit/checksum, authorship, vendor license, numerical reproduction command and tolerance, data sensitivity and author approval. Preserve the full internal evidence in the private workspace and never mirror private history into this public repository.
