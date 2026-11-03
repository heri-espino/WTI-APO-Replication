# Release manifest — reviewed code-only scientific subset

**Stage: pre-release development. Scientific code-only components are present; manuscript-wide reproduction is NOT verified.**

The author directed the creation of a public, curated scientific release on 2026-11-03. The selected source files were reviewed for embedded secrets, private workstation paths and commercial data; none of the copied modules include such records. Their original Git history was not transferred. Copyright/author control should be confirmed by the author when approving a stable public release.

| Public file | Original source blob SHA | Purpose | Approval and rights state |
|---|---|---|---|
| `src/wti_apo_replication/gbm_inference.py` | `2558dc91a488573b2798bb2a9be29ba715372808` | Physical GBM inference | Code-only, selected for public release |
| `src/wti_apo_replication/asian_pricing.py` | `de238a3cf4c6df6cb7029b3844b0091ae11bcc91` | Geometric-control Asian MC | Code-only, selected for public release |
| `src/wti_apo_replication/sigma_quadrature.py` | `b14faec16eeda556c90936aaa4d3d761dcf979e1` | Posterior quadrature | Code-only, selected for public release |
| `src/wti_apo_replication/average_price_option.py` | `c9efd789335a6533f27e570b751ab9aa941e1ebd` | Partially fixed fixing pricing | Code-only, selected for public release |
| `tests/test_gbm_inference.py` | `e9cfd2a7dc2c2b3dbd3cb56c1c3a6f0b42bd8258` | Gaussian inference tests | Renamed import namespace only |
| `tests/test_asian_pricing_methods.py` | `9c71b7fe8f862f7319807552ce3c47e637f633bb` | MC/control tests | Renamed import namespace only |
| `tests/test_sigma_quadrature.py` | `010e80f6b921a2be086ef4c3028c5a259e5d4e37` | Quadrature independent checks | Renamed import namespace only |
| `experiments/experiment001/` | New independent source | Synthetic PI–PM test | Public code; results unverified until executed and committed |
| Original `synthetic.py`, docs, CI, license | New public project | API, infrastructure, teaching demo | MIT for original public files |

## Excluded

- Raw or filtered proprietary Barchart/Databento datasets, caches, LFS pointers, private Git history and author credentials.
- Full empirical reconciliation scripts, unverified vendor as-of records, price-proxy data and private results.
- Derived market tables or images until third-party rights are checked.
- Full ten-million-history simulation and a verified independent reproduction of the manuscript.

**A stable version/Zenodo archive is not equivalent to verification of the private paper's market results.** If released earlier, its title/abstract must describe the software as a **partial methods replication package**, never a full replication archive.

## Release gate

Before stable release, record scientific test results, actual environment version pins and source commit, approve third-party rights/copyright, and document what is absent. A distinct manuscript-wide replication claim requires the separately licensed inputs and checks in `docs/reproducibility.md`.
