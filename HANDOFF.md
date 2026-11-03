# Handoff — curated WTI APO methods and Zenodo preparation

**Status:** public scientific methods under development, version `0.1.0.dev0`. The package includes the actual GBM posterior inference, sigma quadrature, Asian pricing and partially fixed fixing modules from the author's research, with original adapted tests and a new synthetic PI–PM experiment. No proprietary raw data, private Git history, or completed manuscript-scale empirical reproduction were released.

**Provenance:** see `docs/release_manifest.md` for exact original source blob hashes and what was excluded. The existing MIT license applies to published code only, not vendor data. Confirm author control and rights before any stable release.

**Commands:**

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m experiments.experiment001.run --seed 2026 --pricing-paths 1024
python scripts/verify_public_scaffold.py
python scripts/validate_release_metadata.py
```

**Model boundary:** inference under physical measure P; futures pricing under risk-neutral Q; first-nearby CL daily fixings are externally supplied; one-factor perfect instantaneous correlation is a maintained assumption.

**Next steps:** confirm independent test outcomes in CI, capture an approved synthetic experiment001 result with exact environment, audit code author rights, and independently verify coverage relative to the manuscript. Complete the `--release` gate only when the intended published scope and provenance are accurately represented.

No GitHub release, DOI, or Zenodo archiving has yet occurred. The GitHub/Zenodo account integration requires the owner. Heavy experiments and release packaging remain manual-only.
