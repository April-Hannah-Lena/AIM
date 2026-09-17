# Expansion batch 1 audit

Target: private `MColbrook/AIM`, base `a602073d986b7f5ce57b1aa0db1687d1bd87761d`, branch `codex/expand-open-problems-2026-09`. Review date: **2026-09-17**. This is partial progress toward 200–300 additions, with a working target of 250.

## Admission and scope

Ten accepted statements have source-backed formulations, independent specialist status corroboration, full-text scope comparisons for material apparent resolutions, semantic duplicate checks, applied motivations and evidence ledgers. Each received a clearly separated adversarial self-pass by the researching agent. No independent agent or human review is claimed. The [search log](search-log.json) records actual queries; R1-1 through R1-13 are the immediate batch refresh.

The refresh additionally checked Rodaro–Venturi’s conditional reduction of Černý’s conjecture, the distinction between Gaussian simplex measure and partition noise stability, and Ravi–Pillai–Prabhakaran–Wigger’s noisy-feedback capacity-enlargement theorem. None resolves the corresponding accepted statement. Existing ledger comparisons cover the other material hits, including July/August 2026 partial results.

## Results

| Measure | Result |
| --- | ---: |
| Original active entries | 300 |
| Investigated candidate records | 14 |
| Accepted and locally integrated additions | 10 |
| Held for formulation/evidence | 1 |
| Held for unresolved proof/capacity claims | 3 |
| Excluded candidate records | 0 |
| Active total | 310 |
| Remaining to minimum 200 additions | 190 |
| Remaining to working target 250 | 240 |

The held candidates are Morrey’s planar implication, Yang–Mills existence/mass gap, FIFO queue feedback and Gaussian multiple-access feedback. They have no active pages or numerical IDs. Discovery-only leads are not counted as investigated candidates or additions.

## Integration and validation

- Assigned permanent IDs 301–310 centrally after admission; subject membership remains independent of ID.
- Refreshed GitHub metadata, branch listing and open PR listing: main remains at the baseline commit, no other branch or pending PR was present. The connected account is `sgstepaniants`, with push permission and no administrative permission. Destination and private visibility are unchanged.
- All original 300 problem pages match the baseline byte-for-byte. All original metadata rows and review dates are preserved.
- `python3 scripts/catalogue.py --write` and `--check` passed for 310 unique entries, required sections, metadata, math delimiters, local links and generated README.
- All 17 integrity regression tests passed. The staged whitespace check found Markdown hard-break spaces in new files; these were removed and metadata lines separated with blank lines.
- All new-page math expressions parsed with KaTeX without errors. The ten statements were visually inspected in five local browser screenshots; equations were legible and unclipped. Temporary QA assets remain outside the repository. This checks mathematical typesetting, not mathematical truth.
- Checked 52 distinct new-page bibliography URLs separately. All returned success; one Numdam URL rejected HEAD with 405 and succeeded with GET 200. The [link report](batch-01-link-check.json) distinguishes this from full source-content review.

## Coverage

| Subject group | New entries |
| --- | ---: |
| Spectral theory and spectral geometry | 1 |
| Operators, matrices and computation | 1 |
| Inverse problems, control and dynamics | 0 |
| PDEs, materials, probability and optimization | 1 |
| Waves, quantum systems and spectral geometry | 0 |
| Imaging, control, geometry and dynamics | 1 |
| Fluids, kinetic theory and continuum mechanics | 1 |
| Stochastic growth, populations and statistical mechanics | 1 |
| Many-body physics, quantum information and wave analysis | 0 |
| Nonlinear evolution, materials and continuum models | 0 |
| Applied geometry, control and information | 3 |
| Stochastic dynamics, reaction networks and applied optimization | 1 |

This batch covers communication, control, statistical inference, approximation hardness, noise robustness, inverse geometry, disordered magnets and plasma kinetics. Biology and additional operations-research/stochastic-network coverage still require substantial work. No new numerical-linear-algebra problem is included.

## Limits and next actions

Search indexing and source availability limit the status review; absence of a located resolution is not proof of openness. Per-source access limitations are recorded in the ledgers. The original 300 entries have not been revalidated. Continue source discovery across all twelve groups and admit further batches only after the same review gates.

## Publication

The batch is integrated in the local worktree. Staging review, a content commit, push and draft PR are pending. No default-branch write or merge has occurred.
