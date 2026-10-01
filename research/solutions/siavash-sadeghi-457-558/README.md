# AIM research resolution package

Prepared 1 October 2026. Contributor / submitter: **Siavash Sadeghi**. These are complete mathematical proof claims, not independently reviewed or formally verified repository resolutions.

## Problem 558

Read **aim_558_counterexample.pdf**. It gives an exact rational three-dimensional counterexample to coordinatewise variance monotonicity of Gaussian alpha-divergence projections, using the finite parameter pair 10 and 11. It also proves the stronger all-alpha>10 comparison for that target, minimality of dimension three, and strict determinant/entropy monotonicity for every non-diagonal Gaussian target when alpha>1.

The PDF's Sections 2–3 suffice for the disproof. Sections 4–5 contain the sensitivity identity and positive results. The full hypothesis-to-target audit is in **RESOLUTION_REPORT_558.md**.

### Reproduce the exact arithmetic

Requires Python 3.10 or later and no third-party packages:

```sh
python verify_558.py
```

A successful run is recorded in **exact_audit_log.txt**. These checks audit algebra, not every analytic step of the proof.

### Optional symbolic/numerical cross-check

Audited with SymPy 1.14.0 and mpmath 1.3.0. Install the optional pinned dependencies in an isolated environment:

```sh
python -m pip install -r requirements-audit.txt
python symbolic_audit_558.py
```

The successful output is in **symbolic_audit_log.txt**. The numerical calculation is illustrative only; the disproof uses exact rational data.

## Problem 457

Read **aim_457_uniform_sampling.pdf**. It proves that every sufficiently small uniform time grid produces the required unweighted frame under the target's bounded-normal-operator and initial-Bessel-family assumptions. No exponential stability is used. Explicit frame bounds and a non-exponentially-stable example are included. See **RESOLUTION_REPORT_457.md** for the hypothesis audit.

## Rebuild the PDFs

LaTeX source is included. With a standard TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error aim_558_counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error aim_558_counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error aim_457_uniform_sampling.tex
pdflatex -interaction=nonstopmode -halt-on-error aim_457_uniform_sampling.tex
```

## Provenance and review

The target statements were read from the repository's main branch on 1 October 2026. Both targets and the contribution rules were rechecked at commit `aa776a01d7d48a79f93251af11fde9454b0aea95` on the same date. Source paths, original papers, and review details are recorded in the reports and PDFs.

The original package attributes its research and audits to one AI assistant. Codex (AI assistant) subsequently read both arguments, checked their fit to the pinned targets and reran the executable audits. Siavash Sadeghi is credited as contributor and submitter; no human proof review is attributed to him. No independent reviewer, publication acceptance, or formal verification is claimed. Under the repository's stated evidence policy, these belong in the **Solution claimed** category pending independent review.

SHA256SUMS records the delivered local files. It is a checksum manifest for this package, not a Git commit hash.

## Submission scope

This contribution includes the proof PDFs, editable sources, hypothesis audits,
executable checks and reproducibility records for AIM 457 and AIM 558.
It proposes no catalogue or status change.

## Local checks and provenance

`REVIEW_AND_CHECKS.txt` records the completed review and its limits.
`repository_catalogue_check_log.txt` validates the unmodified pinned repository,
not integration of the claims into the catalogue. `compile_check_log.txt`
records successful local PDF compilation; all eleven PDF pages were inspected.
`ENVIRONMENT.txt` records the reproduction environment and preserves the
original package's environment as historical provenance.

The original twelve-file manifest passed. This package's `SHA256SUMS` covers
all files in this directory except the manifest itself.
