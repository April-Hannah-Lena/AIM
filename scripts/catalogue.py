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
REQUIRED = {"id", "title", "area", "file", "status", "last_checked"}
SECTIONS = ("Problem statement", "Applied significance", "References", "Status review")


def valid_id(value):
    return (isinstance(value, str) and bool(re.fullmatch(r"[0-9]{3,}", value))
            and int(value) > 0 and value == f"{int(value):03d}")


def load_manifest():
    errors = []
    try:
        manifest = json.loads((ROOT / "catalogue.json").read_text())
    except (ValueError, OSError) as exc:
        return {}, [f"catalogue.json: {exc}"]
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        return {}, ["catalogue.json: expected schema_version 1"]
    for key in ("groups", "batches", "retired"):
        if not isinstance(manifest.get(key), list):
            errors.append(f"catalogue.json: {key} must be an array")
    if errors:
        return {}, errors
    for key in ("groups", "batches"):
        items = manifest[key]
        if not items:
            errors.append(f"catalogue.json: {key} must not be empty")
        seen = set()
        for item in items:
            if (not isinstance(item, dict) or
                    not isinstance(item.get("key"), str) or
                    not re.fullmatch(r"[a-z0-9-]+", item["key"]) or
                    not isinstance(item.get("title"), str) or not item["title"].strip()):
                errors.append(f"catalogue.json: invalid {key} record")
                continue
            if item["key"] in seen:
                errors.append(f"catalogue.json: duplicate {key} key {item['key']}")
            seen.add(item["key"])
            if key == "batches" and (not isinstance(item.get("ids"), list) or
                                     not item["ids"] or
                                     not all(valid_id(i) for i in item["ids"])):
                errors.append(f"catalogue.json: invalid IDs in batch {item['key']}")
    for item in manifest["retired"]:
        if (not isinstance(item, dict) or not valid_id(item.get("id")) or
                not isinstance(item.get("reason"), str) or not item["reason"].strip() or
                not isinstance(item.get("record"), str)):
            errors.append("catalogue.json: retired ID needs id, reason and research record")
        else:
            record = (ROOT / item["record"]).resolve()
            if ROOT / "research" not in record.parents or not record.is_file():
                errors.append(f"catalogue.json: invalid retirement record for {item['id']}")
    return manifest if not errors else {}, errors


def load_entries(manifest):
    entries = []
    errors = []
    expected_files = {f"{group['key']}.json" for group in manifest["groups"]}
    for path in sorted((ROOT / "data").glob("*.json")):
        if path.name not in expected_files:
            errors.append(f"Unregistered metadata file: data/{path.name}")
    for group in manifest["groups"]:
        stem = group["key"]
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
        for row in rows:
            if not isinstance(row, dict) or not REQUIRED <= row.keys():
                errors.append(f"{path.name}: incomplete metadata row")
                continue
            if not all(isinstance(row[k], str) and row[k].strip() for k in REQUIRED):
                errors.append(f"{path.name}: all metadata fields must be nonempty strings")
                continue
            if not valid_id(row["id"]):
                errors.append(f"{path.name}: invalid ID {row['id']}")
                continue
            try:
                checked = date.fromisoformat(row["last_checked"])
                if checked.isoformat() != row["last_checked"]:
                    errors.append(f"{row['id']}: date must use YYYY-MM-DD")
                if checked > date.today():
                    errors.append(f"{row['id']}: status check is in the future")
            except ValueError:
                errors.append(f"{row['id']}: invalid ISO date")
            entries.append({**row, "group": stem})
    return sorted(entries, key=lambda row: int(row["id"])), errors


def render_readme(entries, manifest):
    total = len(entries)
    lines = [
        f"# AIM — {total} Open Applied Problems", "",
        f"A sourced collection of **{total} precise mathematical research problems** in spectral theory, operator theory, applied mathematics, and related fields. Each problem has a self-contained statement, an applied motivation, brief references, and a dated literature-status review. The problem pages do not attempt solutions.", "",
        "**Literature checks:** Each entry records its own review date. Adding a batch does not revalidate earlier entries. The entries are open in the cited literature, and targeted searches did not locate later resolutions of their exact statements as of their review dates. This is a documented literature check, not a guarantee that no proof exists. Restrictions and relevant partial results are explained on each page. Further additions exclude numerical linear algebra (NLA).", "",
        "Read the [research methodology](research/METHODOLOGY.md) and [contribution guide](CONTRIBUTING.md). The [source maps and exclusion records](research/README.md) identify the books and paper sections used, and explain why some older open problems are absent. Machine-readable index metadata lives in [data/](data/).", "",
        "The collection includes foundational questions as well as directly applied ones, with a wide range of difficulty. Related entries may have mathematical implications for one another; the count does not assert logical independence.", "",
        "| Publication batch | Active entries | Entry review dates |", "| --- | ---: | --- |",
    ]
    for batch in manifest["batches"]:
        rows = [row for row in entries if row["id"] in batch["ids"]]
        dates = sorted({row["last_checked"] for row in rows})
        date_text = (dates[0] if len(dates) == 1 else f"{dates[0]}–{dates[-1]}") if dates else "—"
        lines.append(f"| {batch['title']} | {len(rows)} | {date_text} |")
    lines += ["", "| Subject group | Problems |", "| --- | ---: |"]
    for group in manifest["groups"]:
        title = group["title"]
        anchor = title.lower().replace(",", "").replace(" ", "-")
        count = sum(row["group"] == group["key"] for row in entries)
        lines.append(f"| [{title}](#{anchor}) | {count} |")
    for group in manifest["groups"]:
        title = group["title"]
        lines += ["", f"## {title}", "", "| ID | Problem | Area |", "| --- | --- | --- |"]
        for row in entries:
            if row["group"] == group["key"]:
                title_text = row["title"].replace("|", "\\|")
                area = row["area"].replace("|", "\\|")
                lines.append(f"| {row['id']} | [{title_text}]({row['file']}) | {area} |")
    lines += ["", "## Maintaining the collection", "",
              "Run `python3 scripts/catalogue.py --write` after metadata changes, then `python3 scripts/catalogue.py --check`. These commands use only the Python standard library and check count, unique IDs, required content, metadata consistency, and local links. They do not verify mathematical or open-status claims.", ""]
    return "\n".join(lines)


def validate(entries, manifest):
    errors = []
    ids = [row["id"] for row in entries]
    retired = [row["id"] for row in manifest["retired"]]
    issued = ids + retired
    if len(set(issued)) != len(issued):
        errors.append("Duplicate ID in active or retired records")
    if not issued or set(issued) != {f"{i:03d}" for i in range(1, max(map(int, issued), default=0) + 1)}:
        errors.append("Every issued ID must be active or explicitly retired; IDs cannot be silently removed")
    batched = [identifier for batch in manifest["batches"] for identifier in batch["ids"]]
    if len(set(batched)) != len(batched) or set(batched) != set(issued):
        errors.append("Publication batches must partition all active and retired IDs exactly once")
    for key in ("title", "file"):
        values = [row[key] for row in entries]
        if len(set(values)) != len(values):
            errors.append(f"Duplicate {key} in metadata")
    indexed = set()
    for row in entries:
        path = ROOT / row["file"]
        if (path.parent != ROOT / "problems" or path.suffix != ".md" or
                path.is_symlink() or not path.name.startswith(row["id"] + "-")):
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
            if not re.search(rf"^## {re.escape(section)}\s*$", content, re.MULTILINE):
                errors.append(f"{row['id']}: missing {section}")
        for field, value in (("Area", row["area"]), ("Last checked", row["last_checked"]), ("Status", row["status"])):
            matches = re.findall(rf"^\*\*{field}:\*\*\s*(.+?)\s*$", content, re.MULTILINE)
            if len(matches) != 1 or matches[0].rstrip(".") != value.rstrip("."):
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
    manifest, errors = load_manifest()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    entries, errors = load_entries(manifest)
    errors.extend(validate(entries, manifest))
    readme = render_readme(entries, manifest)
    if args.check and (ROOT / "README.md").read_text() != readme:
        errors.append("README is stale; run python3 scripts/catalogue.py --write")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    if args.write:
        (ROOT / "README.md").write_text(readme)
        print(f"Wrote README.md with {len(entries)} indexed problems.")
    else:
        print(f"Validated {len(entries)} unique problems, metadata, required sections, math delimiters, local links, and README freshness.")


if __name__ == "__main__":
    main()
