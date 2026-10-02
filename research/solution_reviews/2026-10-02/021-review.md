# Review of original target 021: The Robin fundamental gap conjecture

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation conversation. I read the complete submitted argument, reconstructed its estimates and limit argument, checked its hypotheses against the pinned target, and wrote a separate symbolic/geometry verifier. I also packaged the manuscript, corrected and supplemented references, added the requested author information, and drew the domain. These roles are disclosed; this is not independent human peer review.

**Decision:** Solved under the repository's documented-independent-audit convention. Counterexample to the complete recorded universal statement, in dimension three.

**Author and submission:** Matthew J. Colbrook; [PR #16](https://github.com/MColbrook/AIM/pull/16). Department of Applied Mathematics and Theoretical Physics, University of Cambridge; [m.colbrook@damtp.cam.ac.uk](mailto:m.colbrook@damtp.cam.ac.uk). The owner requested this attribution. The uploaded argument is AI-assisted; neither attribution nor the originating checks constitute independent proof review.

**Pinned submission head:** `dd0e96874add04c0ea8bbd10342fd2f6bd630639`. The audited PDF has SHA-256 `ed022e624bad6f5b703884e51810e49464dc3e8939159077f61be2d6a2a1e5df`; the source has SHA-256 `7874017c718fcebd8fa7b6fe6f2688584ffecfc68659c86dd088a5365978f6f0`.

**Pinned target:** [Original 021 at revision 37a25361f243be77daea0ae0b3c5167b57f1b5f3](https://github.com/MColbrook/AIM/blob/37a25361f243be77daea0ae0b3c5167b57f1b5f3/problems/021-robin-fundamental-gap.md).

**Full proof:** [PDF](../../solutions/021-robin-gap-counterexample/robin_gap_021.pdf) and [standalone LaTeX source](../../solutions/021-robin-gap-counterexample/robin_gap_021.tex). [Target comparison](../../solutions/021-robin-gap-counterexample/RESOLUTION_REPORT.md); [current archive record](../../resolved/652-robin-fundamental-gap.md).

## Geometry and transverse estimate

The convex hull has eight end-square vertices and one transverse protruding vertex. Its sections are the Minkowski interpolants of a square and its hull with the protrusion. Independently enumerating the nine half-spaces recovers precisely those nine vertices. All vertex pairs give the claimed actual diameter, for the fixed small thickness. Section polygons give area $`A(t)=4+18t-9t^2`$ and perimeter $`P(t)=8+(2\sqrt{82}-2)t`$. Their ratio has a unique interior minimum $`m<3/2`$ and a central barrier of at least $`8/5`$, with the stated second-derivative bound.

I checked the uniform Robin estimate on every section, including the endpoint sections. Each contains the unit disk, has area at least four, and has bounded diameter and radius. The elementary convex-domain Poincare bound and the divergence-theorem trace estimate control the zero-mean part. Decomposing a normalized function into its mean and fluctuation, bounding the boundary cross term and completing the square gives

```math
\lambda_1(K_t;\beta)\ge\beta P(t)/A(t)-10100\beta^2
\quad (0<\beta\le1/976).
```

This is an analytic bound for arbitrary admissible functions, rather than a polygon sampling assertion. The constants and parameter range were checked separately with rational arithmetic.

## Full-domain spectrum and strict comparison

The section-boundary lower bound uses the actual Euclidean surface measure. On every lateral facet its Jacobian is at least one relative to axial coordinate times section arc length. End-cap terms are nonnegative because the Robin parameter is positive. Transverse scaling sets $`\beta=\varepsilon`$ while the physical domain and comparison interval both have $`\alpha=1`$.

For the upper bound I reconstructed the localized, transversely constant cosine trial function. The two moving fiber sides have physical normal velocity of magnitude $`9\varepsilon`$; the other sides give the perimeter term without that extra factor. The exact boundary integral, fiber area lower bound, and quadratic estimate around the minimum yield ground energy at most $`m/\varepsilon+130\varepsilon^{-1/2}`$. Combined with the barrier lower bound this controls the ground-state mass $`M`$ in the central slab:

```math
M\le1300\sqrt\varepsilon+101000\varepsilon.
```

The first eigenfunction is positive, simple and even by connectedness and axial reflection. Its product with the odd piecewise linear cutoff is orthogonal to it in the full volume inner product. The weak ground-state equation gives the exact cutoff identity; its quotient bounds the full second eigenvalue, not a restricted symmetry spectrum. Therefore

```math
\rho_2-\rho_1\le\frac{16M}{1-M}
\le\frac{20801616}{998699899}<0.021
\quad\text{at }\varepsilon=10^{-12}.
```

The nine-vertex diameter is $`D=2\sqrt{1+2\varepsilon^2}`$. The even and odd interval root equations, with the same outward-normal Robin parameter, give a first root below one and a second root above two. I checked the rigorous trigonometric bounds used for those inequalities. Thus the actual-diameter interval gap exceeds $`3/(1+2\varepsilon^2)>2.9`$. No computed continuum eigenvalue is used here.

## Smooth-domain transfer

The polytope alone would not satisfy the target. I checked the complete transfer to the specified smooth family. The log-sum-exp of all nine physical half-space normals, plus $`\delta|X|^2`$, has Hessian bounded below by $`2\delta I`$. Its unit sublevel set is nonempty for small positive $`\delta`$, bounded, strictly convex, and has a regular smooth boundary.

Uniform convergence to the polytope gauge yields radial and diameter convergence. At almost every boundary direction there is a unique active facet; the excluded edges have zero surface measure. The radial derivative stays bounded away from zero. The radial pullbacks are uniformly bi-Lipschitz for the already fixed thickness, and their derivatives and surface Jacobians converge almost everywhere to the identity and one. No uniform estimate as thickness also tends to zero is assumed.

The finite-dimensional min-max upper bound follows by dominated convergence. For the lower bound, pulled-back low eigenfunctions have uniform Sobolev bounds; volume compactness and compact boundary traces pass weighted orthogonality, mass, and boundary terms to the limit. The square-root coefficient argument gives weak lower semicontinuity of the gradient energy. Min-max on the limiting orthonormal span proves convergence of each fixed Robin eigenvalue. This addresses the boundary term, which cannot be justified solely by Hausdorff convergence.

After fixing the thickness, choose one sufficiently small smoothing parameter so each of the first two eigenvalues changes by less than 0.1 and the actual-diameter interval gap remains above two. The resulting single smooth strictly convex three-dimensional domain has gap below 0.221. This strictly disproves the target with all its recorded hypotheses.

## References, reproduction and limits

The [reference audit](../../solutions/021-robin-gap-counterexample/REFERENCES.md) documents all seven bibliography entries and the affiliation/email sources. It distinguishes published titles from earlier preprint titles, the one-dimensional result from the higher-dimensional conjecture, and negative-Robin background from this positive-Robin construction. Standard Robin spectral and Sobolev/trace dependencies are cited. No bibliography key or manuscript cross-reference is missing. Where publisher full text could not be fetched, the audit identifies the primary bibliographic record actually checked.

All seven original files match the uploaded archive hashes. The original checker reproduced 25 exact rational inequalities and nine diagnostic polygon checks; its JSON results agree with the supplied results. The separate [verifier](../../solutions/021-robin-gap-counterexample/verify_independently.py) passes 40 geometry, symbolic and cross-reference checks. These support, and do not replace, the analytic audit above.

The manuscript was compiled twice with the installed compiler; all citations and cross-references resolve and all nine rendered pages were inspected. The domain drawings use explicitly rescaled transverse axes. The displayed smooth example uses an illustrative parameter; it is not a numerically certified counterexample.

The audit found no missing hypothesis or unresolved analytic step for the recorded target. It leaves a separately posed planar-only question open and establishes existence rather than a certified numerical smoothing threshold. No human peer review, Lean verification, journal acceptance or exhaustive novelty determination is claimed. The [identity mapping and preservation check](021-id-mapping.json) records the archive transition and confirms that surviving active entries and programme histories are preserved.
