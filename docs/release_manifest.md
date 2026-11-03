# Public release manifest and rights audit

**Stage: pre-release development; core source moved for review, but full manuscript replication not authorized for public release.**

| Candidate | Rights and origin | Verification | Status |
|---|---|---|---|
| Python metadata, docs, CI, license, citation | Original public project files; MIT | Metadata validation and CI | Public development |
| `src/wti_apo_replication/synthetic.py` | New independent illustrative GBM code; MIT | Analytic/deterministic/input unit tests | Public development, not manuscript reproduction |
| `src/bayesian_asian_options/*.py` (10 files) | Author-controlled, data-free scientific source selected for public review | Original regression tests; clean-environment CI pending | Public development branch; not full empirical replication |
| `tests/test_*.py` (curated 10 files) | Purely synthetic, fixed-seed regression tests, no commercial datasets | Automated unit checks pending | Public development branch |
| Vendor-format adapters `barchart_apo.py`, `databento_wti.py` | Author-controlled parsers, no vendor records | Synthetic data-format tests | Public development; licensed files remain excluded |
| Barchart/Databento market records | Third-party commercial licenses | Not eligible for public transfer | Excluded |
| Production empirical analysis and full posterior-integration experiments | Private research workspace | No independent full reproduction | Not released |
| Derived market tables/figures | Publication and rights review pending | Not verified or approved | Not released |
| Full reproducibility snapshot | To be audited | Version, numerical comparisons, env provenance missing | Not released |

| `experiments/experiment002/run.py` | Curated synthetic mechanism driver; source blob `8413de9b222cddf28f38dbf9356ac910186e1faa` | Tiny-cell deterministic test; 10M rerun not performed | Public synthetic source, manual large jobs only |
| `tests/test_experiment002.py` | Original tiny-cell test; blob `fef3ad906b80273d66ea2b3cf29535d5961f8984` | CI seed/allocation/restart checks | Public |
| `results/experiment002/archive_10m/` | Pure synthetic 10M historical aggregate results: original CSV blobs `8c7f2e3056a45f6963643e9aa4e3d3240274ea98`, `3ae4617cbbe4e59f89f28208fb2c2f101a4794ec`, `abd5359a8684c614a55d28476a8ed4dbe5903dc2`, `bc22ecc3969f40d7d75afcab1c5537062d327a78` | 5,880/35/168/100 numeric rows checked; archived report redacts machine and private commit identifiers | Historical synthetic outputs, not independent rerun |

## File-level scientific release gate

For every future file, record its relative path, origin and checksum, applicable copyright/vendor terms, whether it might expose licensed observations or sensitive identifiers, reproducible command, expected numerical result/tolerance and author approval. Preserve original scientific evidence in the private workspace. Do not copy private Git history or unpublished internal material.

Before a stable release, replace this pre-release status with an explicit **Stage: public-release-approved** assertion only after all scientific and licensing gates pass.
