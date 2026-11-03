"""Check the public pre-release repository for accidental private artefacts.

This is a *release-safety smoke test*, not a scientific reproducibility test.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DISALLOWED_EXTENSIONS = (
    ".dbn", ".dbn.zst", ".db", ".sqlite", ".sqlite3",
    ".parquet", ".feather", ".arrow", ".pickle", ".pkl",
    ".joblib", ".csv", ".csv.gz", ".tsv", ".gz", ".zst",
    ".pdf", ".png", ".jpg", ".jpeg", ".zip", ".tar", ".7z",
)
PRIVATE_IDENTIFIERS = (
    "Bayesian-Uncertainty-in-WTI-APOs",
    "heriberto.espinomo@udlap.mx",
    "0009-0009-1230-2931",
)
MANDATORY_FILES = (
    "README.md", "AGENTS.md", "HANDOFF.md",
    "docs/reproducibility.md", "docs/release_manifest.md",
)


def check_release_scaffold() -> list[str]:
    """Return clear pre-release safety failures; never inspect ignored files."""
    failures: list[str] = []
    for filename in MANDATORY_FILES:
        if not (ROOT / filename).is_file():
            failures.append(f"Missing required file: {filename}")

    proc = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True
    )
    tracked = [Path(p.decode()) for p in proc.stdout.split(b"\0") if p]
    for relative in tracked:
        path = ROOT / relative
        name = relative.as_posix()
        lowered = name.lower()
        if lowered.startswith("data/") or lowered.endswith(DISALLOWED_EXTENSIONS):
            failures.append(f"Unreviewed or proprietary file type/path: {name}")
            continue
        if not path.is_file():
            failures.append(f"Tracked path absent: {name}")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"Binary file without release approval: {name}")
            continue
        for identifier in PRIVATE_IDENTIFIERS:
            if identifier.casefold() in content.casefold():
                failures.append(f"Private identity/source reference in public file: {name}")
    return failures


if __name__ == "__main__":
    errors = check_release_scaffold()
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: pre-release public scaffold has no disallowed tracked artifacts")
