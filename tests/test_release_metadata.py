"""Verify consistent v1.0.0 metadata without claiming empirical market reproduction."""
import tomllib
from pathlib import Path

from scripts.validate_release_metadata import check_metadata

ROOT = Path(__file__).resolve().parents[1]


def test_basic_metadata_consistent():
    assert check_metadata() == []


def test_explicitly_approved_scoped_release_gate():
    # The code-and-synthetic scope is release approved; this is not a
    # claim that the full licensed-market empirical paper can be replicated.
    assert check_metadata(release=True) == []


def test_version_matches_scientific_python_packages():
    with (ROOT / "pyproject.toml").open("rb") as handle:
        version = tomllib.load(handle)["project"]["version"]
    assert version == "1.0.0"
    for path in (
        ROOT / "src" / "wti_apo_replication" / "__init__.py",
        ROOT / "src" / "bayesian_asian_options" / "__init__.py",
    ):
        assert ('__version__ = "1.0.0"') in path.read_text(encoding="utf-8")
