# GitHub release and Zenodo preservation

This repository is a **pre-release development workspace**. Do not create a GitHub Release or Zenodo deposit before its scientific source and redistribution rights are approved.

## Source-of-truth files

- `pyproject.toml`: package version (`0.1.0.dev0` until release), dependencies, build settings.
- `environment.yml`: developer setup, **not** a complete frozen lockfile.
- `LICENSE`: MIT for original public software only.
- `CITATION.cff`: public authorship and license metadata. It intentionally lacks a DOI and release date.
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
8. Run `python scripts/validate_release_metadata.py --release`. This **must fail at present**, while scientific release approval is outstanding.

## First Zenodo archive

1. Sign in to [Zenodo](https://zenodo.org), connect GitHub, select its GitHub section, choose **Sync now**, and enable `heri-espino/WTI-APO-Replication`.
2. Only after the release gate passes and the repository is enabled, publish an authorized GitHub Release from an immutable approved tag such as `v0.1.0`.
3. Confirm that Zenodo archived the exact release snapshot with the expected title, authors, license, version and file inventory.
4. Record Zenodo's version-specific DOI and concept DOI in the README and release documentation. Do not invent DOI values or assume editing metadata later updates an already archived snapshot.

Official guides:
- https://help.zenodo.org/docs/github/enable-repository/
- https://help.zenodo.org/docs/github/describe-software/citation-file/

A DOI identifies an archived release, **not** a guarantee that the included code reproduces an empirical paper.
