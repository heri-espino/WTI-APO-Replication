"""Verify the historical synthetic summary archive, not proprietary observations."""
import csv
import json
from pathlib import Path
from scripts.verify_public_scaffold import APPROVED_SYNTHETIC_CSV

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/"results/experiment002/archive_10m"

def test_archived_ten_million_metadata_and_counts():
    report=json.loads((ARCHIVE/"mechanism_map_report.json").read_text())
    assert report["synthetic_datasets"] == 10_000_000
    assert report["contract_scenarios"] == 168
    assert report["summary_rows"] == 5880
    assert report["preset"] == "ten-million"
    assert "git_commit" not in report and "platform" not in report
    expected={
        "mechanism_map_summary.csv":5880,
        "posterior_cell_summary.csv":35,
        "scenario_grid.csv":168,
        "top_100_adverse_scenarios.csv":100,
    }
    assert {(ARCHIVE/name).relative_to(ROOT).as_posix() for name in expected} == APPROVED_SYNTHETIC_CSV
    for name,count in expected.items():
        with (ARCHIVE/name).open(newline="",encoding="utf-8") as handle:
            reader=csv.DictReader(handle)
            rows=list(reader)
        assert len(rows)==count
        assert all("market" not in k.lower() and "timestamp" not in k.lower() for k in reader.fieldnames)
    with (ARCHIVE/"mechanism_map_summary.csv").open(newline="",encoding="utf-8") as handle:
        rows=list(csv.DictReader(handle))
    assert max(float(row["max_abs_pi_minus_pm"]) for row in rows)>0.15
