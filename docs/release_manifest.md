# Public release manifest and rights audit

**Stage: pre-release development; full manuscript replication not authorized for public release.**

| Candidate | Rights and origin | Verification | Status |
|---|---|---|---|
| Python metadata, docs, CI, license, citation | Original public project files; MIT | Metadata validation and CI | Public development |
| `src/wti_apo_replication/synthetic.py` | New independent illustrative GBM code; MIT | Analytic/deterministic/input unit tests | Public development, not manuscript reproduction |
| Barchart/Databento market records | Third-party commercial licenses | Not eligible for public transfer | Excluded |
| Empirical models and posterior integration | Private research workspace | No independent public reproduction | Not released |
| Derived market tables/figures | Publication and rights review pending | Not verified or approved | Not released |
| Full reproducibility snapshot | To be audited | Version, numerical comparisons, env provenance missing | Not released |

## File-level scientific release gate

For every future file, record its relative path, origin and checksum, applicable copyright/vendor terms, whether it might expose licensed observations or sensitive identifiers, reproducible command, expected numerical result/tolerance and author approval. Preserve original scientific evidence in the private workspace. Do not copy private Git history or unpublished internal material.

Before a stable release, replace this pre-release status with an explicit **Stage: public-release-approved** assertion only after all scientific and licensing gates pass.
