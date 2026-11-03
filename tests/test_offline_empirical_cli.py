"""Confirm that empirical CLI entry points import without licensed market data.

This is an *import and help-text smoke check*, not a validation of results.
"""
import subprocess
import sys

import pytest


@pytest.mark.parametrize(
    "module",
    [
        "experiments.wti_apo_empirical",
        "experiments.wti_apo_date_panel",
        "experiments.wti_curran_benchmark",
        "experiments.wti_apo_implied_volatility",
        "experiments.experiment002.run",
    ],
)
def test_offline_empirical_scripts_show_help_without_vendor_files(module):
    proc = subprocess.run(
        [sys.executable, "-m", module, "--help"],
        capture_output=True,
        text=True,
        timeout=40,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "usage:" in proc.stdout.lower()
