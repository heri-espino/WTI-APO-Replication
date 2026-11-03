# GitHub release and Zenodo preservation

## v1.0.0 published release (2026-11-03)

- **GitHub release:** [v1.0.0](https://github.com/heri-espino/WTI-APO-Replication/releases/tag/v1.0.0)
- **Immutable tag commit:** `93f657607307909e088fd8f77fcc772e10d63fd9`
- **Zenodo DOI reported by the repository owner:** [10.5281/zenodo.23932925](https://doi.org/10.5281/zenodo.23932925)
- **Release scope:** curated research software and synthetic benchmarks; no licensed-market empirical reproduction or proprietary raw data

The DOI was reported on Zenodo's GitHub integration release list. Follow the DOI to confirm the archived record and metadata before relying on it externally. The version-tagged GitHub snapshot is immutable; changes to `main` after this release (including its DOI badge and citation-file update) **do not change the contents of the archived v1.0.0 release**. Do not recreate or overwrite the tag to backfill documentation. For a future release, increment the package and citation version and update the `doi` field appropriately: do not reuse the v1.0.0 version DOI as if it identified new release files.


The author approved the **v1.0.0 software-and-synthetic scope** on November 3, 2026. The strict release metadata gate can now validate this limited scope; it does **not** certify the manuscript’s licensed-market empirical results. Zenodo archival remains dependent on the repository owner enabling integration **before** publishing the verified GitHub Release.

## Source-of-truth files

- `pyproject.toml`: stable software package version `1.0.0`, dependencies, build settings.
- `environment.yml`: developer setup, **not** a complete frozen lockfile.
- `LICENSE`: MIT for original public software only.
- `CITATION.cff`: approved v1.0.0 authorship, license, version and intended release date. Its v1.0.0 version DOI is now recorded; check the archived record for exact metadata.
- `CHANGELOG.md`: version history.
- `docs/release_manifest.md`: reviewed public-file allowlist and third-party rights gate.

**No `.zenodo.json` is used.** Zenodo ignores `CITATION.cff` if both files are present; introduce `.zenodo.json` only when a specific Zenodo-only metadata field requires it.

## Before the first release

1. Independently review each proposed scientific file's source, license, sensitive metadata, tests, and provenance. Never mirror private Git history or vendor data.
2. Verify which scientific results can be reproduced from the public package, and what requires separately licensed market inputs.
3. Record numerical tests with fixed seeds/tolerances, a clean-environment dependency lock or export, comparison to the manuscript, and a release authorizer.
4. Review whether public metadata is consistent with ongoing double-anonymized peer review.
5. Install and test: `python -m pip install -e ".[dev]"`, `python -m pytest -q`, `python scripts/verify_public_scaffold.py`, `python scripts/validate_release_metadata.py`.
6. Run `cffconvert --validate` for citation schema validation. Run the manual **Release preview** GitHub Actions workflow and inspect the archived wheel and sdist.
7. Change the version in `pyproject.toml` to the approved stable release number. Synchronize `CITATION.cff` version/date if added, update the changelog and manifest, and confirm reproducibility is documented.
8. Run `python scripts/validate_release_metadata.py --release`. It must pass **for methods and synthetic evidence only**, as documented in `docs/verified_replication.md`; it cannot claim full empirical replication.

## Release-specific review of the synthetic methods archive

**Verified on GitHub:** commit `fee20d6e9c60784cb21a8229d26aeec04589b429` passed 69 tests and release-metadata checks on [GitHub Actions #41687743436](https://github.com/heri-espino/WTI-APO-Replication/actions/runs/41687743436). The 10M data-free mechanism-map summary is **historical**; it has not been independently recomputed from the public environment. The archived four CSVs and redacted report are covered by focused content checks.

**Defensible first release scope:** “Bayesian and Asian-option methods with synthetic benchmarks” — NOT “full empirical replication of WTI APO settlement comparisons.” The full paper's third-party licensed histories, vendor as-of verification and conditional error panels remain unavailable publicly. Do not use the software DOI to imply verification of these results.

**Before creating v1.0.0:** confirm author/rightsholder approval to license the imported research code under MIT, check double-anonymized-review risk, run the manual release-preview wheel/sdist build, review the distribution file inventory, pin/document the exact environment and record a scoped scientific review. The `--release` gate is explicitly scoped to verified software and synthetic evidence, and must be checked on the final release commit.

**Capabilities:** This connection can edit GitHub source and merge PRs but cannot create GitHub Releases or configure the author's Zenodo account. Once the release gates are satisfied, the repository owner must publish a GitHub Release and enable GitHub-to-Zenodo archiving (or use an authorized interactive workflow).

## Manual-only verified release workflow

A new workflow `.github/workflows/publish-verified-release.yml` can publish an approved GitHub Release **only** when manually dispatched on `main`. It requires a stable version equal to `pyproject.toml`, a successful `scripts/validate_release_metadata.py --release` gate, citation validation, privacy scanning, passing tests, wheel/sdist validation and two explicit author checkboxes confirming scientific/licensing/anonymity review and that Zenodo has already been enabled. It publishes the version tag with release notes and SHA256 checksums and refuses to overwrite existing tags/releases.

**The workflow may only be dispatched for an approved final commit:** Version `1.0.0` and the scoped verification record are required. A passing gate is **not** permission to claim empirical market-data reproduction. A GitHub workflow cannot verify the owner's actual Zenodo authorization; the repository owner must enable Zenodo integration before dispatch. Publishing a release is an irreversible public step and may affect double-anonymized peer review.

## First Zenodo archive

1. Sign in to [Zenodo](https://zenodo.org), connect GitHub, select its GitHub section, choose **Sync now**, and enable `heri-espino/WTI-APO-Replication`.
2. Only after the release gate passes and the repository is enabled, publish an authorized GitHub Release from an immutable approved tag such as `v1.0.0`.
3. Confirm that Zenodo archived the exact release snapshot with the expected title, authors, license, version and file inventory.
4. Record Zenodo's version-specific DOI and concept DOI in the README and release documentation. Do not invent DOI values or assume editing metadata later updates an already archived snapshot.

Official guides:
- https://help.zenodo.org/docs/github/enable-repository/
- https://help.zenodo.org/docs/github/describe-software/citation-file/

A DOI identifies an archived release, **not** a guarantee that the included code reproduces an empirical paper.
