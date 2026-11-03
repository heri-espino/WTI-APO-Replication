# Handoff — Zenodo-ready repository foundation

**Stage:** `0.1.0.dev0` pre-release. **Repository cleanup (2026-11-03):** PR #3's package foundation was merged; obsolete placeholder READMEs under `src/`, `scripts/`, `tests/`, `examples/`, and `results/` were removed. The authoritative release status remains in this handoff, `docs/release_manifest.md`, and `docs/reproducibility.md`. Do not recreate empty placeholder directories; add them only when approved source, fixtures, or output files exist. The repository now includes author-controlled numerical methods, vendor-format preprocessing, offline empirical CLI entry points and the manual-only synthetic mechanism-map experiment002. No licensed observations or completed empirical reproductions are publicly released (synthetic regression tests, no empirical data), alongside its independent educational demonstration. The repository has an MIT license, `CITATION.cff`, `pyproject.toml`, `environment.yml`, an installable scientific core and a standalone synthetic Monte Carlo example. **No GitHub Release, Zenodo record, DOI, commercial data or manuscript-specific empirical replication is published.**

## Architecture

- `pyproject.toml`: version/install source of truth; `environment.yml`: Conda starting environment (not a lockfile).
- `CITATION.cff`: the only Zenodo citation metadata input; `.zenodo.json` intentionally absent.
- `src/wti_apo_replication/synthetic.py`: synthetic, no vendor data, not the private paper model.
- `scripts/verify_public_scaffold.py`: public privacy and data guard.
- `scripts/validate_release_metadata.py`: metadata checks; `--release` blocked while publication reproduction and approval are incomplete.
- `docs/zenodo_release.md`: GitHub–Zenodo sequence, DOI and version guidance.
- `docs/release_manifest.md`: file-by-file rights gate for future scientific code/results.

## Next steps

Curate and test publication-specific source **only after** a file-level licensing and scientific audit. Complete the file-level rights audit of the selected source snapshot (never mirror private history); add production experiment orchestration and tests with fixed seeds, clean environment, permitted aggregate outputs and an independent source-to-paper comparison. Document access instructions for separately licensed Barchart/Databento market inputs, without publishing the records.

Release preview is manual-only; no tags or DOI will be created by CI. Do not merge PRs or publish releases without explicit authorization.
