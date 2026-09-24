# Expansion batch 2 audit

Target: private `MColbrook/AIM`, upstream `7fe62d53378cb3f5ebbe7caeda9f3a4d72039395`. Review date: **2026-09-17**. The user authorized direct pushes to `main`; no PR is required.

## Admission and scope

Ten accepted statements are integrated as 311–320. Their candidate ledgers record source formulations, specialist status corroboration, comparisons with apparent resolutions, duplicate review and a separated adversarial self-pass. No independent agent or human review is claimed. The [search log](search-log.json) records the immediate refresh as R2-1 through R2-17.

The refresh inspected the 2026 LPN hardness-amplification reductions, which assume an oracle for transformed instances and do not supply a polynomial-time algorithm or unconditional hardness theorem. It also verified the withdrawal of the apparent linear sample-compression proof. The Ruskai–Audenaert review distinguishes the input-dimension rank bound from an older typographical error, equal-weight decompositions from arbitrary mixtures, and generalized extreme channels from actual extreme points. Other restricted results and their remaining gaps are recorded in the individual evidence ledgers.

| ID | Topic | Primary section |
| --- | --- | --- |
| 303 | Carrying-simplex interior regularity | inverse |
| 304 | Three-processor unit scheduling | stochastic3 |
| 305 | Entanglement-assisted Lovász bound | spectral3 |
| 306 | Fixed-disorder quantum diffusion | spectral2 |
| 307 | Reversible reaction–diffusion continuation | continuum3 |
| 308 | Splay-tree dynamic optimality | operators |
| 309 | Learning parity with noise | applied |
| 310 | Linear sample compression | applied |
| 311 | Belgian chocolate threshold | inverse |
| 312 | Ruskai–Audenaert channel decomposition | spectral3 |

There are now 20 accepted and published additions, 320 active entries and four held candidates without numerical IDs. At least 180 further additions are needed for the requested minimum; the working target of 250 requires 230 more. All twelve primary sections have at least one accepted addition. No new numerical-linear-algebra problem is included.

## Integration and validation

Problem IDs were assigned centrally after admission. Before integration, `git fetch origin main` and the remote branch listing confirmed that `main` was the only remote branch, at the upstream commit above. The connected GitHub open-PR search returned none. There was no intervening upstream content or competing addition.

- `python3 scripts/catalogue.py --write` and `--check` passed for all 320 unique entries, metadata, required sections, math delimiters, local links and README freshness.
- All original 300 pages match baseline `a602073` byte-for-byte, and all 310 previously published pages match `7fe62d5`. All prior metadata rows and historical review dates are unchanged.
- Research counts agree: 24 investigated records, 20 accepted and integrated, and four holds. Section counts, numerical IDs, accepted page paths and batch-2 archived draft paths agree.
- All 194 mathematics expressions in the ten new pages parsed with KaTeX without errors. All ten statements were visually inspected in five browser screenshots; equations were legible and unclipped. Temporary rendering assets remain outside the repository. This checks typesetting, not mathematical truth.
- Checked 54 distinct new-page URLs. Of these, 53 succeeded, including a Numdam URL that rejected HEAD and succeeded with GET. One publisher DOI returned HTTP 403; the institutional full-text copy used for source review remains accessible. The [link report](batch-02-link-check.json) records the attempts and limitation.
- The staged whitespace check passed before the content commit.
- The catalogue machinery is unchanged; its 17 regression tests passed in batch 1. No new machinery tests were required by `CONTRIBUTING.md`.

## Publication

Content commit [`7e1c7d7`](https://github.com/MColbrook/AIM/commit/7e1c7d7de3bf58063c7578edb77cc84e323a03fd) was pushed directly to `main` on 2026-09-17. Git reported a normal fast-forward from `7fe62d5`, and `git ls-remote --heads origin main` independently returned the new content commit. No remote work was overwritten and no PR was created.

## Limits

Source and version limitations are recorded in the ledgers. No search proves the absence of a resolution, and no independent proof certification is claimed. The original 300 entries and their historical review dates have not been revalidated. Discovery beyond the ten handoff seeds remains necessary.
