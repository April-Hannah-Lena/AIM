# Resolution report: original problem 021

**Target revision:** `37a25361f243be77daea0ae0b3c5167b57f1b5f3`.

**Claim:** Complete counterexample to the recorded universal positive-Robin gap inequality, in dimension three. The [full proof](robin_gap_021.pdf) and [source](robin_gap_021.tex) are supplied for review against the [unchanged target](statement.md).

| Target requirement | Construction and proof |
| --- | --- |
| Euclidean Laplacian | Ordinary volume Dirichlet energy and Euclidean boundary measure; no weighted or effective operator replaces the target. |
| Dimension at least two | The example has dimension three. It does not settle a separately posed planar-only problem. |
| Positive Robin parameter | The same parameter, one, is used on the domain and interval, with the outward-normal convention. |
| Bounded connected convex domain | The starting polytope is a bounded intersection of nine half-spaces containing the origin; its smooth approximations are nonempty strictly convex sublevel sets. |
| Smooth boundary | The smooth defining function has positive definite Hessian and a regular level surface. |
| Actual diameter | The polytope diameter is computed from all vertex pairs. Smooth-domain diameters converge to it and the interval gap is continuous in diameter. |
| First two full eigenvalues | A positive simple ground state is used. The odd cutoff trial function is orthogonal to it, so the full second eigenvalue is bounded by min-max. |
| One fixed domain | Fix the explicit thickness, then select any sufficiently small smoothing parameter in the proved convergence regime. |
| Strict disproof | The final smooth gap is below 0.221 and its actual-diameter interval gap exceeds two. |

## Argument map

1. Compute the sections of a convex hull as a Minkowski interpolation. Their perimeter-to-area ratio has two reflection-related minima and a central barrier.
2. Prove a uniform transverse Robin lower bound, with an explicit quadratic remainder, from elementary Poincare and trace estimates.
3. Slice the full quadratic form. The lateral surface measure dominates the section-boundary measure. A localized transversely constant trial function supplies a matching ground-energy upper bound.
4. Deduce a central ground-state mass bound. Reflection symmetry and the exact ground-state cutoff identity yield a gap bound below 0.021 for the explicit polytope.
5. Bound the diameter-matched interval gap from below by exact inequalities for its even/odd Robin root equations; the lower bound exceeds 2.9.
6. Prove Robin spectral convergence for an explicit smooth strongly convex family using radial bi-Lipschitz pullbacks, compact volume and boundary traces, weighted orthogonality and min-max. This transfers the strict violation to a single smooth domain.

The original checker, the separate symbolic/geometry checker, and [reference audit](REFERENCES.md) support review. No numerical continuum spectrum, certified numerical smoothing threshold, human peer review, proof-assistant certificate or novelty determination is asserted. Standard Sobolev/trace and Robin spectral theory remain identified analytic dependencies. The current repository classification and its audit evidence belong to the [resolution archive](../../../RESOLVED.md).
