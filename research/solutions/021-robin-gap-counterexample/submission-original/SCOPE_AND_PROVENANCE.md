# Scope, target match, and provenance

## Exact target

AIM problem #021, checked publicly on 2 October 2026:
https://github.com/MColbrook/AIM/blob/main/problems/021-robin-fundamental-gap.md

The target quantifies over bounded smooth convex Euclidean domains in dimension at least two and all positive Robin parameters. It compares the first spectral gap with that of an interval of the domain's actual diameter, using the same parameter. One admissible counterexample therefore disproves its universal claim.

The original source is Conjecture F of R. S. Laugesen, *The Robin Laplacian—spectral conjectures, rectangular theorems*, Journal of Mathematical Physics 60 (2019), 121507:
https://arxiv.org/abs/1905.07658

## Hypotheses and quantifiers

| Requirement | Where it is met |
|---|---|
| Ordinary Euclidean Laplacian | The manuscript uses the unweighted Dirichlet energy and Euclidean surface measure. |
| Positive, unchanged Robin parameter | Alpha equals one on both the domain and the comparison interval. |
| Allowed dimension | The counterexample is three-dimensional; no planar conclusion is claimed. |
| Boundedness and connectedness | The starting domain is the interior of a bounded convex polytope; each final sublevel set is nonempty, bounded, and convex. |
| Smoothness | The final domain is a regular level sublevel set of an explicit C-infinity function. |
| Convexity | The defining function has Hessian at least 2 delta times the identity; the boundary is strictly convex. |
| Actual diameter | The polytope diameter is computed, and the smooth-domain diameter passes to it. The interval comparison follows that actual diameter, not an arbitrarily fixed limiting value. |
| Actual first two eigenvalues | Positivity identifies the ground state. A trial function orthogonal to it bounds the full second eigenvalue by min–max; the argument is not limited to a symmetry-restricted spectrum. |
| One domain | First fix the explicit thickness, then choose any sufficiently small smoothing parameter in the proved convergence regime. |
| Strict inequality in the wrong direction | The smooth gap is below 0.221, while its comparison interval gap exceeds two. |

## Distinctions from related work

Derek Kielty's *Degeneration of the spectral gap with negative Robin parameter* concerns alpha < 0 and double-cone domains. The argument here uses alpha = 1 and a different transverse perimeter-to-area barrier. The sign distinction is essential:
https://arxiv.org/abs/2105.02323

Problem #024 was excluded after checking PR #11. The pull request already contains a proposed Steklov counterexample and explicitly labels it a claimed solution pending independent mathematical review:
https://github.com/MColbrook/AIM/pull/11

A separate recent result was located for #010: Mikael Sundqvist's preprint, submitted 18 September 2026, claims the unrestricted optimality of the equal-sector three-partition of the disk. This is external work, not a solution generated in this package; the complete 32-page proof has not been independently verified here:
https://arxiv.org/abs/2609.21964

## Review status and limitations

No independent reviewer has evaluated this package. No formal proof system was used. No exhaustive novelty search is claimed. No numerical three-dimensional spectrum was computed. The smoothness transfer is analytic and supplies no explicit numerical smoothing threshold. The arithmetic script does not verify functional analysis, trace compactness, spectral convergence, or the full PDE argument.

The principal points for mathematical audit are the fiber geometry, uniform small-parameter Robin estimate, boundary-coarea lower bound, exact lateral boundary measure, ground-state cutoff identity, and radial pullback proof of smooth spectral convergence. Each is included in the manuscript rather than replaced by a numerical assertion.
