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
GENERATED_DOCUMENTS = ("README.md", "CATALOG.md", "RESOLVED.md")
RETIRED_STATUSES = ("Solved", "Solution claimed", "Retired")


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
            if "title" in item and (not isinstance(item["title"], str) or not item["title"].strip()):
                errors.append(f"catalogue.json: invalid retired title for {item['id']}")
            if item.get("status", "Retired") not in RETIRED_STATUSES:
                errors.append(f"catalogue.json: invalid retired status for {item['id']}")
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


def table_text(value):
    return " ".join(value.splitlines()).replace("|", "\\|")


def subject_index(entries, manifest, document=""):
    lines = ["| Subject group | Open targets |", "| --- | ---: |"]
    for group in manifest["groups"]:
        title = group["title"]
        anchor = title.lower().replace(",", "").replace(" ", "-")
        count = sum(row["group"] == group["key"] for row in entries)
        lines.append(f"| [{title}]({document}#{anchor}) | {count} |")
    return lines


def render_readme(entries, manifest):
    solved = sum(row.get("status") == "Solved" for row in manifest["retired"])
    claimed = sum(row.get("status") == "Solution claimed" for row in manifest["retired"])
    other = len(manifest["retired"]) - solved - claimed
    summary = (f"**{len(entries)} open targets** · **{solved} solved entries** · "
               f"**{claimed} solution claim{'s' if claimed != 1 else ''}**")
    if other:
        summary += f" · **{other} other retained entries**"
    lines = [
        "# AIM — Open Applied Problems", "",
        "A sourced collection of precise mathematical research problems in spectral theory, operator theory, applied mathematics, and related fields. Each entry has a self-contained statement, an applied motivation, references, and a dated literature-status review.", "",
        summary + ". Counts reflect the statuses recorded in this collection.", "",
        f"**[Browse all {len(entries)} open targets →](CATALOG.md)** · **[Solved and claimed solutions →](RESOLVED.md)**", "",
        "## Browse by subject", "",
        *subject_index(entries, manifest, "CATALOG.md"), "",
        "## Reading the collection", "",
        "Each [problem page](problems/) records its assumptions and quantifiers, applied significance, references, status, and last review date. Permanent IDs remain reserved when an entry leaves the open catalogue; its original statement and status record are retained.", "",
        "The collection includes foundational questions as well as directly applied ones, with a wide range of difficulty. Related entries may imply one another; the count does not assert logical independence. Further additions exclude numerical linear algebra (NLA).", "",
        "## What “open” means here", "",
        "An open target is unresolved in its cited literature, and targeted searches found no later resolution of its exact statement as of the entry's review date. Partial results and restrictions are explained on its page. These bounded checks cannot guarantee that no proof exists, and adding a batch does not revalidate earlier entries.", "",
        "A **solution claim** matches the target but awaits independent proof review. A **solved** entry has a documented resolution supported by the review recorded on its page. Both are listed separately from open targets in [RESOLVED.md](RESOLVED.md); other retirement reasons are kept distinct.", "",
        "See the [research methodology](research/METHODOLOGY.md), [source maps and exclusion records](research/README.md), and [publication batches](CATALOG.md#publication-batches) for the evidence behind the catalogue.", "",
        "## Contributing", "",
        "Suggestions, references, corrections, and resolution reports are welcome through [GitHub issues](https://github.com/MColbrook/AIM/issues) and pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for admission criteria, status updates, and catalogue maintenance. A resolution report should link to the proof or counterexample and explain how it matches the exact target.", "",
        "## Citing this collection", "",
        "If you use this collection, please cite:", "",
        "```bibtex",
        "@misc{aim2026openproblems,",
        "  author = {{AIM contributors}},",
        "  title  = {{AIM — Open Applied Problems}},",
        "  year   = {2026},",
        "  url    = {https://github.com/MColbrook/AIM},",
        "  note   = {GitHub repository}",
        "}",
        "```", "",
        "Machine-readable citation metadata is available in [CITATION.cff](CITATION.cff). Include your access date or the commit used when referring to a particular version. For an individual problem, give its permanent ID and cite the original sources listed in the entry as well. When using a solution, also cite its authors and the proof source linked from the status record.", "",
    ]
    return "\n".join(lines)


def render_catalog(entries, manifest):
    lines = [
        "# Open targets", "",
        "[Repository overview](README.md) · [Solved and claimed solutions](RESOLVED.md)", "",
        f"**{len(entries)} open targets**, grouped by subject. Each linked page gives the precise statement, references, partial results, and its own literature-review date. These are the active entries; solution claims and resolved or otherwise retired entries are excluded from this count.", "",
        "## Browse by subject", "",
        *subject_index(entries, manifest), "",
        "[Publication batches and review dates](#publication-batches)",
    ]
    for group in manifest["groups"]:
        title = group["title"]
        lines += ["", f"## {title}", "", "| ID | Problem | Area |", "| --- | --- | --- |"]
        for row in entries:
            if row["group"] == group["key"]:
                title_text = table_text(row["title"])
                area = table_text(row["area"])
                lines.append(f"| {row['id']} | [{title_text}]({row['file']}) | {area} |")
    lines += ["", "## Publication batches", "",
              "Adding a batch does not revalidate earlier entries. Counts below include only currently open targets; retired IDs retain their original batch membership.", "",
              "| Publication batch | Open targets | Entry review dates |", "| --- | ---: | --- |"]
    for batch in manifest["batches"]:
        rows = [row for row in entries if row["id"] in batch["ids"]]
        dates = sorted({row["last_checked"] for row in rows})
        date_text = (dates[0] if len(dates) == 1 else f"{dates[0]}–{dates[-1]}") if dates else "—"
        lines.append(f"| {batch['title']} | {len(rows)} | {date_text} |")
    lines += ["", "## Maintaining the collection", "",
              "This index, [README.md](README.md), and [RESOLVED.md](RESOLVED.md) are generated from [catalogue.json](catalogue.json) and [data/](data/). Run `python3 scripts/catalogue.py --write` after metadata changes, then `python3 scripts/catalogue.py --check`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.", ""]
    return "\n".join(lines)


def render_resolved(manifest):
    lines = [
        "# Solved and claimed solutions", "",
        "[Repository overview](README.md) · [Browse open targets](CATALOG.md)", "",
        "This archive lists previously admitted targets that are no longer counted as open. A solution claim is not a verified solution. Each linked record preserves the original statement, permanent ID, sources, review date, and the scope of the review actually performed.", "",
    ]
    sections = (
        ("Solved", "Solved", "Documented resolutions of the exact target. Consult each record for the proof source and the kind of review performed.", "No solved entries are currently recorded in this archive."),
        ("Solution claimed", "Solution claimed", "A matching complete resolution has been announced, but independent proof review remains outstanding.", "No solution claims are currently recorded in this archive."),
        ("Retired", "Other retained entries", "Entries removed for reasons other than a recorded solution or solution claim. Retirement alone does not mean that a target is solved.", "No other retired entries are currently recorded."),
    )
    for status, heading, description, empty in sections:
        rows = sorted((row for row in manifest["retired"] if row.get("status", "Retired") == status),
                      key=lambda row: int(row["id"]))
        lines += [f"## {heading}", "", description, ""]
        if rows:
            lines += ["| ID | Problem and status record | Reason |", "| --- | --- | --- |"]
            for row in rows:
                title = table_text(row.get("title", f"Entry {row['id']}"))
                lines.append(f"| {row['id']} | [{title}]({row['record']}) | {table_text(row['reason'])} |")
            lines.append("")
        else:
            lines += [empty, ""]
    lines += [
        "## Reporting a solution", "",
        "Open a [GitHub issue](https://github.com/MColbrook/AIM/issues) or pull request with the problem ID, a direct proof or counterexample reference, and a comparison with the entry's assumptions and conclusion. State whether the result is a claim, a published result, or an independently reviewed argument, and identify the review evidence. See [CONTRIBUTING.md](CONTRIBUTING.md#reporting-a-resolution) for how to update the record and index.", "",
        "Candidates excluded before admission are documented in the [research records](research/README.md); they are not counted as resolved catalogue entries. This archive is generated from the `retired` records in [catalogue.json](catalogue.json).", "",
    ]
    return "\n".join(lines)


def validate(entries, manifest, documents=None):
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
    generated = {ROOT / name: content for name, content in (documents or {}).items()}
    markdown = {path: path.read_text() for path in ROOT.rglob("*.md")
                if ".git" not in path.parts and path not in generated}
    markdown.update(generated)
    for path, content in markdown.items():
        for target in re.findall(r"\]\(([^)\s]+)\)", content):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target_path = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target_path).resolve()
            if target_path and not resolved.exists() and resolved not in generated:
                errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="rebuild README, open catalogue and resolution archive after validation")
    mode.add_argument("--check", action="store_true", help="check content and freshness of all generated documents")
    args = parser.parse_args()
    manifest, errors = load_manifest()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    entries, errors = load_entries(manifest)
    documents = dict(zip(GENERATED_DOCUMENTS, (
        render_readme(entries, manifest), render_catalog(entries, manifest), render_resolved(manifest))))
    errors.extend(validate(entries, manifest, documents))
    if args.check:
        for name, content in documents.items():
            path = ROOT / name
            if not path.is_file():
                errors.append(f"{name} is missing; run python3 scripts/catalogue.py --write")
            elif path.read_text() != content:
                errors.append(f"{name} is stale; run python3 scripts/catalogue.py --write")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    if args.write:
        for name, content in documents.items():
            (ROOT / name).write_text(content)
        print(f"Wrote {', '.join(documents)} with {len(entries)} open targets and {len(manifest['retired'])} retained entries.")
    else:
        print(f"Validated {len(entries)} unique problems, metadata, required sections, math delimiters, local links, and freshness of {', '.join(documents)}.")


if __name__ == "__main__":
    main()
