# Infrastructure audit — 2026-09-17

Repository: `MColbrook/AIM`; original base: `a602073d986b7f5ce57b1aa0db1687d1bd87761d`; local topic branch: `codex/expand-open-problems-2026-09`; infrastructure commit: `8126792`.

The remote main ref matched the base during the initial read-only check. The connected account was `sgstepaniants`; connector metadata reported a private repository and push access, with no open pull requests and only the main remote branch. The normalized connector result did not expose a fork flag, so this audit does not independently refresh that field from the handoff. No remote mutation has occurred.

`catalogue.json` separates problem IDs, twelve section keys and explicit publication-batch membership. The original infrastructure change preserved problem content. The current numbering policy supersedes the former permanent-ID policy: remaining active entries are numbered consecutively after deletions, and references and batch membership follow each problem. `scripts/catalogue.py` validates this policy. CONTRIBUTING and the generated README describe the current schema.

Validation completed:

- `python3 scripts/catalogue.py --write`: passed, 300 active entries.
- `python3 scripts/catalogue.py --check`: passed, 300 active entries.
- `python3 scripts/test_catalogue.py`: 17 tests passed on temporary copies, covering preserved baseline paths/counts, noncontiguous grouping, duplicate IDs/files, missing metadata/headings/pages, unindexed pages, invalid/future dates, broken local links, stale README, publication membership, unregistered metadata, and retired-ID handling.
- `git diff --check`: passed.
- `git diff a602073d986b7f5ce57b1aa0db1687d1bd87761d --name-only -- problems data`: empty.

The infrastructure commit contains only catalogue.json, scripts/catalogue.py, scripts/test_catalogue.py, CONTRIBUTING.md and README.md. The supplied handoff directory and zip are not staged or committed. There is no accepted-content batch audit yet because the accepted count is zero. Structural tests do not certify mathematical correctness or open status.
