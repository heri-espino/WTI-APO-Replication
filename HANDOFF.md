> **2026-11-03 Zenodo preparation audit:** The public repo now contains mainline curated scientific-core methods, licensed-format parsers without records, synthetic experiment001 and its reference JSON, and the synthetic historical ten-million mechanism-map experiment002 (driver, 5,880-row scenario archive, 35 cell summaries, 168 scenarios, 100 ranked rows). Main commit `fee20d6e` passed 69 unit tests in CI run 41687743436; no independent 10M re-execution was performed. The intended future release is a **methods and synthetic benchmark archive**, not a claim that licensed empirical settlement-price results are reproduced. Release version remains `0.1.0.dev0`; no GitHub Release or Zenodo DOI exists. Full release gate remains intentionally blocked pending scoped approval, exact environment review and double-blind implications. Other concurrent PRs #6–#8 were preserved; superseded PR #5 was closed and additive PR #9 merged.

> **2026-11-03 experiment002 additive archive:** The original synthetic ten-million-history mechanism-map script, deterministic tiny-cell test and five audited historical synthetic aggregate files were added without altering the concurrently merged scientific core or market adapters. Four CSV files contain exclusively numeric synthetic scenarios, including permitted blank undefined Taylor correlation/slope entries; their source Git blob IDs appear in the release manifest. The redacted report retains 10M count, seed/configuration and numerical summary but omits machine identifiers. Heavy reruns remain manual-only; this is historical output, not independent re-execution. Full market-data study replication is still incomplete.

# Handoff — Zenodo-ready repository foundation

**Stage:** `0.1.0.dev0` pre-release. **Repository cleanup (2026-11-03):** PR #3's package foundation was merged; obsolete placeholder READMEs under `src/`, `scripts/`, `tests/`, `examples/`, and `results/` were removed. The authoritative release status remains in this handoff, `docs/release_manifest.md`, and `docs/reproducibility.md`. Do not recreate empty placeholder directories; add them only when approved source, fixtures, or output files exist. The repository now includes curated, data-free Bayesian/Asian-option methods and two vendor-format input adapters with synthetic tests (no licensed observations) (synthetic regression tests, no empirical data), alongside its independent educational demonstration. The repository has an MIT license, `CITATION.cff`, `pyproject.toml`, `environment.yml`, an installable scientific core and a standalone synthetic Monte Carlo example. **No GitHub Release, Zenodo record, DOI, commercial data or manuscript-specific empirical replication is published.**

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
