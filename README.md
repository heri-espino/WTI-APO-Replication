# WTI APO Replication

**Status: pre-release (`0.1.0.dev0`). No stable software release, Zenodo DOI, or manuscript replication dataset exists yet.**

This is an independent public software workspace for future reproducibility of arithmetic-average option research. It is **not** a copy of the private research repository. The current Python package includes a small, original **synthetic spot-GBM example**, not the empirical model or published WTI option results. Third-party Barchart and Databento market records are not distributed.

## Quick start

Python 3.11+ is required. From the repository root:

```bash
conda env create -f environment.yml
conda activate wti-apo-replication
python -m pytest -q
wti-apo-synthetic --paths 4096 --observations 12 --seed 2026
```

Or use a Python virtual environment:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m wti_apo_replication.synthetic --paths 4096 --seed 2026
```

The demonstration returns a simulated price, a Monte Carlo standard error, a path count, and the seed. These numbers are **synthetic**, not observed WTI settlements. The unit tests check an analytic zero-volatility limit, seeded reproducibility, and invalid inputs.

## Repository files

| File | Purpose |
|---|---|
| [`pyproject.toml`](pyproject.toml) | Installable Python package, dependencies, and development version |
| [`environment.yml`](environment.yml) | Conda environment for development |
| [`LICENSE`](LICENSE) | MIT license for original public source and documentation |
| [`CITATION.cff`](CITATION.cff) | GitHub citation metadata, suitable for later Zenodo ingestion |
| [`CHANGELOG.md`](CHANGELOG.md) | Version and release history |
| [`docs/zenodo_release.md`](docs/zenodo_release.md) | Release checklist and Zenodo integration instructions |
| [`docs/reproducibility.md`](docs/reproducibility.md) | Scientific limits and reproduction boundaries |
| [`docs/release_manifest.md`](docs/release_manifest.md) | Rights/provenance approvals for public materials |
| [`AGENTS.md`](AGENTS.md), [`HANDOFF.md`](HANDOFF.md) | AI-agent instructions and implementation handoff |

Automated CI runs only quick tests, syntax/metadata validation, and a tracked-file privacy audit. A **manual-only release preview** can build a source distribution and wheel without publishing a release or archiving to Zenodo.

## Licensing, citation, and privacy

MIT applies to **original public files** here and is not a license for private code or vendor-owned records. Publication-specific code, numerical results, and market-derived aggregates require scientific and redistribution-rights review before copying.

[`CITATION.cff`](CITATION.cff) contains preliminary attribution but **no invented DOI**. Once an authorized GitHub Release is archived by Zenodo, cite the verified version-specific DOI. Do **not** cite this scaffold as a reproduction of any unpublished manuscript.
