# WTI APO Replication

**Status: pre-release (`0.1.0.dev0`). No stable software release, Zenodo DOI, or manuscript replication dataset exists yet.**

This is an independent public software workspace for future reproducibility of arithmetic-average option research. It is **not** a copy of the private research repository. The Python distribution now includes a curated **Bayesian inference and Asian-option pricing core** from the author-controlled research workspace, plus a separate independent spot-GBM example. The public code covers inference, numerical integration, Curran conditioning, first-nearby mapping, and partial-fixing Monte Carlo; it does **not** reproduce the full manuscript empirical results without separately licensed data and validated analysis pipelines. Third-party Barchart and Databento market records are not distributed. Data-format adapters for independently licensed inputs and synthetic-only adapter tests are available; see [licensed input requirements](docs/licensed_inputs.md).

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

The project also exposes `bayesian_asian_options` modules (see [available scientific methods](docs/reproducibility.md)) and synthetic regression tests. The demonstration returns a simulated price, a Monte Carlo standard error, a path count, and the seed. These numbers are **synthetic**, not observed WTI settlements. The unit tests check an analytic zero-volatility limit, seeded reproducibility, and invalid inputs.

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

MIT applies to **original public files** here and is not a license for private code or vendor-owned records. Publication-specific **empirical orchestration**, numerical market results, and market-derived aggregates require scientific and redistribution-rights review before copying. The subset of model functions now included was selected for being self-contained and data-free; the original private Git history was not imported.

[`CITATION.cff`](CITATION.cff) contains preliminary attribution but **no invented DOI**. Once an authorized GitHub Release is archived by Zenodo, cite the verified version-specific DOI. Do **not** cite this code-only development branch as an independently verified reproduction of unpublished empirical findings.
