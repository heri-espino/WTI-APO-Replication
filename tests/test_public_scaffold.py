"""Pre-release safety checks; no scientific reproduction is claimed."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.verify_public_scaffold import check_release_scaffold


class PublicScaffoldTests(unittest.TestCase):
    def test_no_unreviewed_tracked_artifacts_or_private_identifiers(self):
        self.assertEqual(check_release_scaffold(), [])


if __name__ == "__main__":
    unittest.main()
