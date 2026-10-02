# AIM 506: proposed counterexample to the general product-prior small-ball formula

**Contributor / submitter:** Siavash Sadeghi.  
**Review date:** 2 October 2026.  
**Pinned repository revision:** `aa776a01d7d48a79f93251af11fde9454b0aea95`.  
**Evidence status:** complete proposed disproof, awaiting independent mathematical review.
The target is the remaining open general conjecture in the repository's **Partial** entry 506, not a problem whose entire statement is labeled Open. The package is prepared as a resolution report for review; no catalogue status change is proposed.

## Main result

Use the density `rho(z) = exp(-z^4) / integral_R exp(-u^4) du` and the usual Hilbert space `ell^2`.
Partition the coordinates into consecutive blocks of size `8^j`, for integers `j >= 1`. On block j use

- coordinate scale `gamma_k = 4^(-j)`;
- center `h_k = 8^(-j)`;
- standardized displacement `h_k / gamma_k = 2^(-j)`.

For the product law of independent `gamma_k Z_k`, the proof establishes

    sum gamma_k^2 = 1
    norm(h)^2 = 1/7
    Q(h) = sum (h_k/gamma_k)^4 = 1
    liminf_{r -> 0} mu(B_r(h)) / mu(B_r(0)) = 0.

The conjecture prescribes the positive limit `exp(-Q(h)) = exp(-1)`. The zero liminf therefore disproves it.
**The proof does not assert that the full ball-ratio limit exists.** A liminf different from the conjectured limit suffices for a complete disproof.

The construction satisfies the target's assumptions and also has an analytic log-concave density with finite Fisher information. Its standardized displacement is not square summable, so it does not contradict the established lower bound in the source paper's Theorem 4.10.

## Files

| File | Role |
|---|---|
| `aim506_counterexample.pdf` | Analytic proof, quantitative bound, robustness, second power-law example and verification appendices |
| `aim506_counterexample.tex` | Editable LaTeX source |
| `verify_exact.py` | Standard-library exact supporting certificates |
| `exact_results.json` | Recorded rational integral enclosures and 31 passed checks |
| `verify_numerical.py` | Separate floating-point corroboration using mpmath and SciPy |
| `numerical_results.json` | Recorded 60-digit calculations, 25 cross-implementation comparisons, and 80 passed checks |
| `requirements-numerical.txt` | Versions used for the optional numerical checks |
| `target_audit.md` | Target-to-theorem match, repository/PR checks and bounded literature review |
| `resolution_report.md` | Resolution report with target matching and review disclosure |
| `environment.txt` | Actual execution environment |
| `verification_logs.txt` | Recorded command output |
| `SHA256SUMS` | File hashes (all deliverables except the hash file itself) |

## Reproduce the exact certificates

Python 3.10 or later, with no third-party packages:

```bash
python3 verify_exact.py --output exact_results.json
```

Expected terminal output begins `PASS: 31 exact supporting checks`.
All mathematical decisions in this script use integers and fractions. Decimal strings are for display only. The certificate proves, among other supporting facts, an optional strengthened one-dimensional constant. The main analytic proof uses only an elementary weaker constant and does not depend on computation.

The script does **not** formally verify measure-theoretic arguments, differentiation under integrals, or limit passages. Those are proved in the PDF and remain subject to independent review.

## Reproduce the numerical checks

The current checked environment uses Python 3.12.14, mpmath 1.3.0 and SciPy 1.18.1. The original package used Python 3.13.5 and SciPy 1.17.0. Use Python 3.12 or later for the pinned numerical dependencies:

```bash
python3 -m pip install -r requirements-numerical.txt
python3 verify_numerical.py --output numerical_results.json
```

The default run uses 60 decimal digits and reports `PASS: 80 numerical supporting checks`. It compares a stable mpmath evaluation of the convolution with a separately coded direct SciPy quadrature over 25 pairs of parameters. The current maximum absolute discrepancy in log ratios is recorded in `numerical_results.json`; every comparison must be below the portable tolerance `3e-12`.

The numerical script also computes prefixes of the infinite Laplace product. It gives an analytic bound for the omitted-coordinate log tail, but **does not certify the finite-prefix quadrature error**. Those results are corroborations, not interval proofs. No small-ball probability was estimated by Monte Carlo.

## Rebuild the PDF

A LaTeX distribution with the packages named at the top of the source is needed:

```bash
pdflatex -interaction=nonstopmode -halt-on-error aim506_counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error aim506_counterexample.tex
```

## Verification and priority limits

The supplied argument and computations are AI-generated. Codex read the full proof and pinned target; separate Codex AI reviewers examined the mathematical argument and primary source, computational programs, and public repository submissions. No human peer review or proof-assistant verification is claimed, and no independent proof review is attributed to Siavash Sadeghi. The current public audit found no matching prior submission. It does not establish exhaustive priority. See `REVIEW_AND_CHECKS.txt`, `target_audit.md` and `repository_submission_check.txt` for scope and limitations.

## Submission process

The repository accepts issues or pull requests containing the problem ID and
repository revision, a proof link, full-target comparison, and explicit reviewer
and AI disclosure. This package provides those records under
`research/solutions/siavash-sadeghi-506/` as a **Solution claimed** contribution.
The claim is a zero **liminf**, which suffices to refute the proposed positive
limit; the full ball-ratio limit is not asserted.

This PR adds the proof package and proposes no catalogue status change. A later
status change requires the coordinated archival, data and catalogue updates
described in the repository's `CONTRIBUTING.md`. Structural catalogue checks do
not certify mathematical correctness.

## Verifier robustness regression

```bash
python3 test_numerical_guards.py
python3 -O test_numerical_guards.py
```

Both runs pass 21 focused checks that invalid integrals and error estimates are
rejected. The guard fix preserves valid numerical outputs. See
`REVIEW_AND_CHECKS.txt` for the complete review and change record,
`compile_check_log.txt` for PDF checks, and
`repository_catalogue_check_log.txt` for structural validation.
