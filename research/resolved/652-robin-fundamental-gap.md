# 652. The Robin fundamental gap conjecture

**Area:** Diffusion and elastically supported membranes

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

Let $`d\ge2`$, $`\alpha>0`$, and let $`\Omega\subset\mathbb R^d`$ be a bounded convex smooth domain of diameter $`D`$. Write $`\rho_1(\Omega;\alpha)\le\rho_2(\Omega;\alpha)`$ for the first two eigenvalues of $`-\Delta`$ with $`\partial_\nu u+\alpha u=0`$. On the interval $`(0,D)`$ use the same outward-normal Robin condition at both endpoints. Prove or disprove

```math
\rho_2(\Omega;\alpha)-\rho_1(\Omega;\alpha)>\rho_2((0,D);\alpha)-\rho_1((0,D);\alpha).
```

The one-dimensional comparison is approached by thin boxes.

## Application

The gap controls relaxation toward the ground mode of a diffusion problem with boundary leakage and the separation of the two lowest elastic frequencies.

## References

1. R. S. Laugesen, [The Robin Laplacian — spectral conjectures, rectangular theorems](https://arxiv.org/abs/1905.07658), Journal of Mathematical Physics 60 (2019), 121507, Conjecture F.
2. B. Andrews, J. Clutterbuck and D. Hauer, [Non-concavity of the Robin ground state](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1805782368600416258-1805782368600416258-88f605793884422439eff9c89a8550e7.pdf), Cambridge Journal of Mathematics 8 (2020), 243–310, concluding open problem.

## Status review

**Resolution (2026-10-02):** Counterexample in dimension three, by Matthew J. Colbrook. The complete recorded target was checked in a Codex AI mathematical audit of the [full manuscript](../solutions/021-robin-gap-counterexample/robin_gap_021.pdf) and [source](../solutions/021-robin-gap-counterexample/robin_gap_021.tex). See the [review record](../solution_reviews/2026-10-02/021-review.md) and [target comparison](../solutions/021-robin-gap-counterexample/RESOLUTION_REPORT.md).

The construction gives one smooth strictly convex domain with the same positive Robin parameter on the domain and its actual-diameter comparison interval:

```math
U\subset\mathbb R^3,\qquad \alpha=1,\qquad
\rho_2(U;1)-\rho_1(U;1)<0.221<2<
\rho_2((0,\mathop{\mathrm{diam}}U);1)-\rho_1((0,\mathop{\mathrm{diam}}U);1).
```

The proof first obtains an explicit gap bound on a thin convex polytope, then proves Robin spectral convergence to a smooth strictly convex family. The smoothing parameter is chosen by this existence argument; no numerical threshold is certified. A separately posed planar-only version remains unresolved. The [domain diagram](../solutions/021-robin-gap-counterexample/domain.png) labels its transverse rescaling and illustrative smoothing parameter.

**Original target:** [021 at the pinned catalogue revision](https://github.com/MColbrook/AIM/blob/37a25361f243be77daea0ae0b3c5167b57f1b5f3/problems/021-robin-fundamental-gap.md). Current archive ID: 652. Submitted in [PR #16](https://github.com/MColbrook/AIM/pull/16).

**Evidence:** Solved under the documented-independent-audit convention. The argument is AI-assisted and the review was performed by AI. The review does not assert human peer review, publication, Lean verification or novelty priority. The package preserves its original submission status and the uploaded files.

### Previous status review at the pinned revision

**Literature check:** Open in cited literature; no later resolution located.

Laugesen states this conjecture and proves the box comparison. Andrews–Clutterbuck–Hauer explain why Robin ground-state nonconcavity obstructs the standard Dirichlet proof; their one-dimensional Robin result leaves d≥2 unresolved. Searches found no general higher-dimensional solution.

**Search audit:** “Robin fundamental gap conjecture 2025 2026”; “Robin spectral gap convex diameter proof”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
