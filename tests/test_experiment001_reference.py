"""Check committed synthetic experiment001 output against the current algorithm."""
import json
from pathlib import Path

import pytest

from experiments.experiment001.run import run_experiment


def test_committed_synthetic_reference_matches_calculation():
    reference = json.loads(
        (Path(__file__).resolve().parents[1] / "results/synthetic/experiment001.json").read_text()
    )
    current = run_experiment(seed=2026, grid_points=301)
    assert set(current) == set(reference)
    for key, expected in reference.items():
        if isinstance(expected, float):
            assert current[key] == pytest.approx(expected, abs=1e-10, rel=1e-10)
        else:
            assert current[key] == expected
