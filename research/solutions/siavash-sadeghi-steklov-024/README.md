# Proposed counterexample to AIM Problem 024

**Contributor / submitter:** Siavash Sadeghi.  
**Target revision:** `aa776a01d7d48a79f93251af11fde9454b0aea95`.  
**Evidence status:** Solution claimed; independent mathematical review pending.

## Review status

This package contains an AI-generated research proof. Codex reviewed the argument
and its fit to the target, and separate AI reviewers checked the mathematics and
numerical supplement. It has not received human peer review or formal verification
and should not be described as an accepted resolution. The detailed target audit
and review scope are in `RESOLUTION_REPORT_024.md` and `REVIEW_AND_CHECKS.txt`. The mathematical argument, its exact hypotheses, and the full construction
are in the PDF and editable LaTeX source.

## Main result presented in the proof

With epsilon = 1/100, define

    q(z) = 1 + epsilon * sum_{n>=1} exp(-sqrt(n)) z^n,
    F(z) = integral_0^z q(zeta)^(-2) dzeta,
    Omega = F(unit disk).

The proof establishes that Omega is bounded, simply connected, smooth, and
strictly convex. For every complete real orthonormal Steklov eigenbasis,

    sum_j exp(t*sigma_j) * abs(u_j(0))^2 = infinity, for every t > 0.

Thus there is a single sequence on this fixed domain which violates every
positive exponential interior-decay rate. The proof uses ordinary Euclidean
arc-length normalization, not a changed physical boundary density.

## Files

- `steklov_counterexample.pdf`: mathematical manuscript, including an
  alternative factorial-growth contradiction and a numerical appendix.
- `steklov_counterexample.tex`: editable LaTeX source and scholarly references.
- `check_steklov.py`: finite cosine-Galerkin numerical supplement.
- `results_order256.csv`, `results_order384.csv`: numerical outputs at two orders.
- `numerical_check.txt`, `numerical_check_order384.txt`: diagnostics from both runs.
- `RESOLUTION_REPORT_024.md`: pinned target and hypothesis comparison.
- `REVIEW_AND_CHECKS.txt`, `ENVIRONMENT.txt`: review scope and reproduction environment.
- `requirements.txt`: tested numerical dependencies.
- `SHA256SUMS`: integrity hashes for all delivered files except the manifest itself.

## Reproduce the numerical supplement

The supplied code uses Python 3.10-compatible syntax. The pinned dependencies
below require Python 3.12 or later; the tested environment used Python 3.12.14:

    python -m pip install -r requirements.txt

    python check_steklov.py --order 256 --samples 8192 --output results_order256.csv
    python check_steklov.py --order 384 --samples 16384 --output results_order384.csv

The CSV index is the index in the even cosine sector, not the full two-sector
Steklov eigenvalue index. Center values have been converted to boundary norm one
with respect to physical Euclidean arc length.

These are floating-point Galerkin approximations without certified error bounds.
Small matrix residuals do not certify continuum eigenvalues or asymptotic decay.
Values near the highest retained mode are less stable across truncation orders;
see `numerical_validation.txt` for the measured comparison.
A finite truncation of q gives an analytic domain. The infinite-dimensional
counterexample rests on the exact proof and its infinite Fourier series, not on
finite numerical evidence.

## Typeset the manuscript

    pdflatex -interaction=nonstopmode -halt-on-error steklov_counterexample.tex
    pdflatex -interaction=nonstopmode -halt-on-error steklov_counterexample.tex

## Repository submission

The [contribution guide](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/CONTRIBUTING.md) accepts resolution reports through issues or pull requests.
This submission places the proof, source, target audit and reproducibility files
in `research/solutions/siavash-sadeghi-steklov-024/`. It proposes no catalogue
status change. The claim awaits independent mathematical review.
