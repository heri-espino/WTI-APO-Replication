"""Entirely synthetic vendor-format parsing example (no purchased data)."""
from pathlib import Path

import pandas as pd

from bayesian_asian_options.barchart_cl import (
    barchart_cl_curve_on_date,
    load_barchart_cl_history,
    load_barchart_cl_strip,
)


def test_synthetic_curve_and_timestamp_parsing(tmp_path: Path):
    for contract, level in [("CLX26", 123.45), ("CLZ26", 120.15)]:
        pd.DataFrame(
            {
                "Time": ["2026-09-01", "2026-09-02"],
                "Open": [level, level],
                "High": [level, level],
                "Low": [level, level],
                "Latest": [level, level],
                "Change": [0, 0],
                "%Change": ["0%", "0%"],
                "Volume": [1, 2],
                "Open Int": [3, 4],
            }
        ).to_csv(tmp_path / f"{contract}.csv", index=False)
    test = load_barchart_cl_history(tmp_path / "CLX26.csv")
    assert len(test) == 2
    strip, manifest = load_barchart_cl_strip(tmp_path, contracts=["CLX26", "CLZ26"])
    curve = barchart_cl_curve_on_date(
        strip, "2026-09-02", contracts=["CLX26", "CLZ26"]
    ).set_index("contract")
    assert curve.loc["CLX26", "settlement"] == 123.45
    assert curve.loc["CLZ26", "settlement"] == 120.15
    assert len(manifest) == 2
