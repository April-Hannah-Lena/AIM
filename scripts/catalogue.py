#!/usr/bin/env python3
"""Build and validate the Markdown catalogue; no third-party packages required."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
GROUPS = (
    ("spectral", "Spectral theory and spectral geometry", 1, 25),
    ("operators", "Operators, matrices and computation", 26, 50),
    ("inverse", "Inverse problems, control and dynamics", 51, 75),
    ("applied", "PDEs, materials, probability and optimization", 76, 100),
    ("spectral2", "Waves, quantum systems and spectral geometry", 101, 125),
    ("inverse2", "Imaging, control, geometry and dynamics", 126, 150),
    ("continuum2", "Fluids, kinetic theory and continuum mechanics", 151, 175),
    ("stochastic2", "Stochastic growth, populations and statistical mechanics", 176, 200),
    ("spectral3", "Many-body physics, quantum information and wave analysis", 201, 225),
    ("continuum3", "Nonlinear evolution, materials and continuum models", 226, 250),
    ("inverse3", "Applied geometry, control and information", 251, 275),
    ("stochastic3", "Stochastic dynamics, reaction networks and applied optimization", 276, 300),
)
TOTAL = GROUPS[-1][3]
REQUIRED = {"id", "title", "area", "file", "status", "last_checked"}
SECTIONS = ("Problem statement", "Applied significance", "References", "Status review")


def load_entries():
    entries = []
    errors = []
    for stem, _, lo, hi in GROUPS:
        path = ROOT / "data" / f"{stem}.json"
        if not path.exists():
            errors.append(f"Missing {path.relative_to(ROOT)}")
            continue
        try:
            rows = json.loads(path.read_text())
        except (ValueError, OSError) as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        if not isinstance(rows, list):
            errors.append(f"{path.name}: expected an array")
            continue
        if len(rows) != hi - lo + 1:
            errors.append(f"{path.name}: expected {hi - lo + 1} entries, found {len(rows)}")
        for row in rows:
            if not isinstance(row, dict) or not REQUIRED <= row.keys():
                errors.append(f"{path.name}: incomplete metadata row")
                continue
            if not all(isinstance(row[k], str) and row[k].strip() for k in REQUIRED):
                errors.append(f"{path.name}: all metadata fields must be nonempty strings")
                continue
            if not re.fullmatch(r"\d{3}", row["id"]) or not lo <= int(row["id"]) <= hi:
                errors.append(f"{path.name}: ID {row['id']} outside assigned range")
            try:
                if date.fromisoformat(row["last_checked"]) > date.today():
                    errors.append(f"{row['id']}: status check is in the future")
            except ValueError:
                errors.append(f"{row['id']}: invalid ISO date")
            entries.append(row)
    return sorted(entries, key=lambda row: row["id"]), errors


def render_readme(entries):
    lines = [
        f"# AIM — {TOTAL} Open Applied Problems", "",
        f"A sourced collection of **{TOTAL} precise mathematical research problems** in spectral theory, operator theory, applied mathematics, and related fields. Each problem has a self-contained statement, an applied motivation, brief references, and a dated literature-status review. The problem pages do not attempt solutions.", "",
        "**Latest addition:** Problems **201–300** add 100 questions from applied mathematics books, surveys, and specific papers, including many-body physics, nonlinear evolution, materials, geometry, control, stochastic kinetics, and optimization. Problems 101–200 form the preceding expansion. Both additions exclude numerical linear algebra (NLA); entries 001–200 are retained.", "",
        "**Literature checks:** Entries **201–300 were checked on 13 September 2026**; entries 001–200 retain their **8 September 2026** reviews. The entries are open in the cited literature, and targeted searches did not locate later resolutions of their exact statements as of their review dates. This is a documented literature check, not a guarantee that no proof exists. Restrictions and relevant partial results are explained on each page.", "",
        "Read the [research methodology](research/METHODOLOGY.md) and [contribution guide](CONTRIBUTING.md). The [source maps and exclusion records](research/README.md) identify the books and paper sections used, and explain why some older open problems are absent. Machine-readable index metadata lives in [data/](data/).", "",
        "The collection includes foundational questions as well as directly applied ones, with a wide range of difficulty. Related entries may have mathematical implications for one another; the count does not assert logical independence.", "",
        "| Subject group | Problems |", "| --- | ---: |",
    ]
    for _, title, lo, hi in GROUPS:
        anchor = title.lower().replace(",", "").replace(" ", "-")
        lines.append(f"| [{title}](#{anchor}) | {lo:03d}–{hi:03d} |")
    for _, title, lo, hi in GROUPS:
        lines += ["", f"## {title}", "", "| ID | Problem | Area |", "| --- | --- | --- |"]
        for row in entries:
            if lo <= int(row["id"]) <= hi:
                title_text = row["title"].replace("|", "\\|")
                area = row["area"].replace("|", "\\|")
                lines.append(f"| {row['id']} | [{title_text}]({row['file']}) | {area} |")
    lines += ["", "## Maintaining the collection", "",
              "Run `python3 scripts/catalogue.py --write` after metadata changes, then `python3 scripts/catalogue.py --check`. These commands use only the Python standard library and check count, unique IDs, required content, metadata consistency, and local links. They do not verify mathematical or open-status claims.", ""]
    return "\n".join(lines)


def validate(entries):
    errors = []
    ids = [row["id"] for row in entries]
    expected = [f"{i:03d}" for i in range(1, TOTAL + 1)]
    if ids != expected:
        errors.append(f"Catalogue must contain each ID 001–{TOTAL:03d} exactly once")
    for key in ("title", "file"):
        values = [row[key] for row in entries]
        if len(set(values)) != len(values):
            errors.append(f"Duplicate {key} in metadata")
    indexed = set()
    for row in entries:
        path = ROOT / row["file"]
        if path.parent != ROOT / "problems" or not path.name.startswith(row["id"] + "-"):
            errors.append(f"{row['id']}: invalid problem path")
            continue
        indexed.add(path)
        if not path.is_file():
            errors.append(f"Missing {row['file']}")
            continue
        content = path.read_text()
        first = content.splitlines()[0] if content else ""
        if not re.match(rf"^# {row['id']}(?:\.|\s+[—–-])\s+", first):
            errors.append(f"{row['id']}: incorrect heading ID")
        if row["title"] not in first:
            errors.append(f"{row['id']}: heading title differs from metadata")
        for section in SECTIONS:
            if f"## {section}" not in content:
                errors.append(f"{row['id']}: missing {section}")
        for field, value in (("Area", row["area"]), ("Last checked", row["last_checked"]), ("Status", row["status"])):
            if value not in content or f"**{field}:**" not in content:
                errors.append(f"{row['id']}: missing or inconsistent {field}")
        if len(re.findall(r"\]\(https?://", content)) < 1:
            errors.append(f"{row['id']}: no linked external reference")
        if re.search(r"(?<!\\)\\[\[\]()]", content):
            errors.append(f"{row['id']}: use GitHub dollar math delimiters")
        if content.count("$$") % 2:
            errors.append(f"{row['id']}: unmatched display math delimiter")
    actual = set((ROOT / "problems").glob("*.md"))
    for extra in sorted(actual - indexed):
        errors.append(f"Unindexed problem file: {extra.relative_to(ROOT)}")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\]\(([^)\s]+)\)", path.read_text()):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target_path = unquote(target.split("#", 1)[0])
            if target_path and not (path.parent / target_path).exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="rebuild README after validation")
    mode.add_argument("--check", action="store_true", help="check content and README freshness")
    args = parser.parse_args()
    entries, errors = load_entries()
    errors.extend(validate(entries))
    readme = render_readme(entries)
    if args.check and (ROOT / "README.md").read_text() != readme:
        errors.append("README is stale; run python3 scripts/catalogue.py --write")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    if args.write:
        (ROOT / "README.md").write_text(readme)
        print(f"Wrote README.md with {TOTAL} indexed problems.")
    else:
        print(f"Validated {TOTAL} unique problems, metadata, required sections, math delimiters, local links, and README freshness.")


if __name__ == "__main__":
    main()
