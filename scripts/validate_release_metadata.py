"""Validate release metadata and explicitly block premature software releases."""
from __future__ import annotations

import argparse
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def check_metadata(*, release: bool = False) -> list[str]:
    errors: list[str] = []
    required = [
        "LICENSE", "pyproject.toml", "environment.yml", "CITATION.cff",
        "README.md", "CHANGELOG.md", "AGENTS.md", "HANDOFF.md",
        "docs/reproducibility.md", "docs/release_manifest.md",
        "docs/zenodo_release.md",
    ]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f"Missing {name}")
    if errors:
        return errors

    with (ROOT / "pyproject.toml").open("rb") as handle:
        config = tomllib.load(handle)
    project = config["project"]
    version = str(project["version"])
    if project["name"] != "wti-apo-replication":
        errors.append("Package name mismatch")
    if project.get("license") != "MIT":
        errors.append("Expected MIT package license")
    if "MIT License" not in (ROOT / "LICENSE").read_text():
        errors.append("LICENSE lacks the MIT license heading")

    conda = yaml.safe_load((ROOT / "environment.yml").read_text())
    if conda.get("name") != "wti-apo-replication":
        errors.append("Conda environment name mismatch")
    if not any(
        isinstance(dep, dict) and "-e .[dev]" in dep.get("pip", [])
        for dep in conda["dependencies"]
    ):
        errors.append("Conda environment must install the editable package")

    cff = yaml.safe_load((ROOT / "CITATION.cff").read_text())
    if cff.get("cff-version") != "1.2.0":
        errors.append("Citation schema must use CFF 1.2.0")
    if cff.get("license") != "MIT":
        errors.append("Citation license mismatch")
    if cff.get("repository-code") != project["urls"]["Repository"]:
        errors.append("Citation repository URL mismatch")
    if not cff.get("authors") or not cff.get("title"):
        errors.append("Citation author/title missing")
    if cff.get("version") and cff["version"] != version:
        errors.append("Citation version must match pyproject.toml")
    if (ROOT / ".zenodo.json").exists():
        errors.append("Remove .zenodo.json unless Zenodo-specific fields are needed")

    if release:
        manifest = (ROOT / "docs/release_manifest.md").read_text()
        if ".dev" in version or "a" in version or "b" in version:
            errors.append("Development/prerelease version is not a stable release")
        if "Stage: public-release-approved" not in manifest:
            errors.append("Scientific release manifest has not been approved")
        if cff.get("version") != version or not cff.get("date-released"):
            errors.append("Version and date-released required in CITATION.cff for release")
        if not (ROOT / "docs/verified_replication.md").is_file():
            errors.append("Missing independently verified scientific replication record")
        if f"## {version}" not in (ROOT / "CHANGELOG.md").read_text():
            errors.append("Missing versioned changelog section")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release", action="store_true",
        help="Enable strict scientific release gate (expected to fail pre-release)",
    )
    args = parser.parse_args()
    errors = check_metadata(release=args.release)
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: release metadata consistent" +
          (" and scientific release gate satisfied" if args.release else
           " (pre-release; not manuscript replication)"))


if __name__ == "__main__":
    main()
