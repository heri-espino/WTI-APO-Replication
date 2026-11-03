"""Pre-release metadata and explicit publication gate."""
from scripts.validate_release_metadata import check_metadata


def test_pre_release_metadata_consistent():
    assert check_metadata() == []


def test_cannot_publish_stable_zenodo_release_prematurely():
    failures = check_metadata(release=True)
    assert any("Development/prerelease version" in s for s in failures)
    assert any("scientific" in s.lower() or "replication" in s.lower()
               for s in failures)
