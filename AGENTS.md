# Public repository agent instructions

**This is a pre-release public repository, never a mirror of the private research workspace.**

Before changes, inspect README.md, AGENTS.md, HANDOFF.md, docs/reproducibility.md, docs/release_manifest.md, docs/zenodo_release.md, pyproject.toml, current scripts, tests and PRs. Preserve all existing decisions.

- Do not import private history, licensed market data, restricted derived outputs, credentials, original private manifests or confidential author correspondence.
- MIT applies only to original public code/documentation, not third-party/private research.
- Keep the independently implemented synthetic GBM example distinguished from the paper's market-data and Bayesian research.
- Record licenses, source provenance and verification for each approved scientific addition in docs/release_manifest.md.
- Keep all approved code/tests/configurations/results and future experiments reproducible in this Git repository.
- Number numerical experiments sequentially (`experiment001`, `experiment002`, ...). Document purpose, method, commands, results, uncertainty, and next steps.
- Update HANDOFF.md with each substantive change. Respect collaborators and concurrent branches.
- Use PRs and **never merge without the author's explicit authorization**.
- Lightweight tests and static metadata checks may run automatically. Heavy simulations, figures, PDFs, and release packaging remain manual-only; never automatically create or publish GitHub Releases or Zenodo deposits.

Checks:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python scripts/verify_public_scaffold.py
python scripts/validate_release_metadata.py
```

The `--release` gate is intentionally blocked until publication-specific verification and author approval.
