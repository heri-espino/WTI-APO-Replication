# Contributing

This is a pre-release public workspace with a strict separation from a private research source of truth.

1. Open an issue describing the change, scientific assumptions and expected verification.
2. Work on a narrowly scoped branch. Do not import Git history, private data, vendor exports, credentials or restricted derived outputs.
3. Run `python -m pip install -e ".[dev]"` and `python -m pytest -q`.
4. Run `python scripts/verify_public_scaffold.py` and `python scripts/validate_release_metadata.py`.
5. Open a PR with the implementation, tests, reproducibility details and rights/provenance review.
6. Do **not** merge another contributor's PR without author authorization; do not create releases without explicit approval.

Experimental changes use `experiment001`, `experiment002`, and so forth, with purpose, steps, configurations, results, verification and next actions. The current synthetic sample is not a paper experiment.

The MIT license applies to original files in this public repository. It does not sublicense any private or vendor-owned source data or code.
