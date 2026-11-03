# Agent contract — public replication repository

This repository is a **pre-release public workspace**, not a mirror of the underlying private research repository.

## Before editing
1. Read README.md, HANDOFF.md, docs/reproducibility.md, and docs/release_manifest.md.
2. Check the existing public tree and PRs. Preserve previously approved work.
3. Use a short-lived branch and PR. Do not merge without the author's explicit authorization.
4. Do not silently transform a pre-release placeholder into a purportedly complete replication package.

## Non-negotiable publication safeguards
- **Never import private Git history** (including forks, mirrors, old branches, internal issues or PRs).
- **Never commit licensed raw market data**, vendors' download exports, LFS pointers, credentials, user-specific paths, passwords or API tokens.
- Do not publish proprietary-derived rows, figures or numerical tables until rights and disclosure review are recorded in docs/release_manifest.md.
- Do not publish author-identifying links to a particular double-anonymized manuscript while it is under review.
- Use a file-by-file allowlist; review each file's copyright, license, data origin, metadata and test provenance.
- No fabricated experiments or implied verification; a passed syntax test is not evidence of reproduced paper results.
- Commit approved scripts, reproducible configurations, tests, notes and allowable results with explicit source and version.
- Name new empirical experiments sequentially (experiment001, experiment002, ...), with purpose, reproducibility steps, findings and next action.

## Automation
Lightweight validation may run automatically on pushes and PRs. Any computationally expensive numerical study, PDF/figure compilation, or release packaging must be manual-only, without automatically committing generated outputs.

## Release gate
A publication release requires author approval, a documented rights audit, a scoped source snapshot, an executable environment, synthetic validation, data-provider instructions and verification of every reported figure/table where permitted. See docs/reproducibility.md.
