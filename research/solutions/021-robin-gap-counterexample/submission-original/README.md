# AIM #021 — proposed positive-Robin gap counterexample

Research argument developed in this conversation, 2 October 2026.

**Evidence status: proposed complete disproof, pending independent mathematical review.** No external peer review, proof-assistant verification, publication acceptance, or novelty determination is claimed. This package concerns one catalogue problem, not five.

## Result

The manuscript constructs a bounded C-infinity strictly convex Euclidean domain U in R^3 for which, at the fixed positive Robin parameter alpha = 1,

    rho_2(U; 1) - rho_1(U; 1) < 0.221 < 2
        < rho_2((0, diam U); 1) - rho_1((0, diam U); 1).

Its starting polytope has an analytic gap upper bound below 0.021. The comparison interval has gap above 2.9. An explicit smooth, strongly convex approximating family and a proved quadratic-form convergence argument transfer the strict violation to a fixed smooth domain. The sufficiently small smoothing parameter is established existentially, not numerically certified.

## Files

- `robin_gap_021.pdf`: eight-page manuscript, including the full smoothness transfer.
- `robin_gap_021.tex`: editable LaTeX source.
- `check_counterexample.py`: standard-library Python program checking the finite arithmetic and polygon formulas; it also implements the smooth defining function.
- `checks.json`: recorded output of that program.
- `SCOPE_AND_PROVENANCE.md`: match to the exact target and evidence limitations.
- `SHA256SUMS.txt`: integrity checks for these files.

## Reproduce the checks

Python 3.10 or later is sufficient; no third-party packages are required.

```sh
python check_counterexample.py --output checks.json
```

Expected console result:

```text
Passed 25 exact arithmetic checks and 9 polygon checks.
Certified comparison: polyhedral gap < 0.021; interval gap > 2.9.
```

These are finite arithmetic and geometric checks, **not** finite-element eigenvalue estimates, interval enclosures of the full PDE spectrum, or a formal verification of the proof. The diagnostic floating-point values are separately labeled in `checks.json`.

## Rebuild the PDF

With a standard LaTeX installation containing the packages named in the source:

```sh
pdflatex -interaction=nonstopmode -halt-on-error robin_gap_021.tex
pdflatex -interaction=nonstopmode -halt-on-error robin_gap_021.tex
```

The delivered PDF was compiled twice, checked for LaTeX and box warnings, and visually inspected after rendering. Such checks validate document production, not mathematical correctness.
