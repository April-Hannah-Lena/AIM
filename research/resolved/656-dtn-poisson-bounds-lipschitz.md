# 656. Poisson kernel bounds for elliptic boundary diffusion on Lipschitz domains

**Area:** Elliptic PDEs and boundary diffusion

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02
## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be a bounded connected Lipschitz domain, $`\Gamma=\partial\Omega`$, and let $`C(x)`$ be a real smooth symmetric matrix on a neighborhood of $`\overline\Omega`$, with $`\xi^TC(x)\xi\ge\mu|\xi|^2`$ for some $`\mu>0`$. Define $`N\varphi=\nu\cdot C\nabla u`$ weakly, where $`\mathop{\mathrm{div}}\nolimits(C\nabla u)=0`$ and $`u|_\Gamma=\varphi`$.
Does $`e^{-tN}`$ have an integral kernel, with respect to surface measure, satisfying

```math
|K_t(z,w)|\le M t^{-(d-1)}e^{\omega t}\left(1+\frac{|z-w|}{t}\right)^{-d}
```

for every $`t>0`$ and almost every $`z,w\in\Gamma`$, with $`M,\omega`$ depending only on the domain and coefficients? The weak definition uses $`u\in H^1(\Omega)`$ and the Green identity against all $`H^1(\Omega)`$ test functions.

## Application

The boundary operator converts applied voltage into current flux. Its semigroup also describes diffusion on an interface coupled to an equilibrated bulk; the estimate measures propagation along boundaries with corners.

## References

1. A. F. M. ter Elst and E. M. Ouhabaz, [Five Open Problems on the Dirichlet-to-Neumann Operator with Variable Coefficients](https://doi.org/10.1007/s00020-025-02796-9), *Integral Equations and Operator Theory* **97** (2025), article 14, problem 5.
2. A. F. M. ter Elst and E. M. Ouhabaz, [Analysis of the heat kernel of the Dirichlet-to-Neumann operator](https://arxiv.org/abs/1302.4199), *Journal of Functional Analysis* **267** (2014), 4066–4109, main Poisson-bound theorem and introduction.

## Status review

**Resolution (2026-10-02):** Counterexample. The complete target was checked in an independent Codex AI mathematical audit of [the submitted proof](../solutions/435-corner-poisson-counterexample/PROOF.md). See [the review record](../solution_reviews/2026-10-02/435-review.md) for the reasoning, scope and supporting checks.

**Original target:** [435 at the pinned catalogue revision](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/435-dtn-poisson-bounds-lipschitz.md). Current archive ID: 656. Submitted in [PR #15](https://github.com/MColbrook/AIM/pull/15).

**Evidence:** Solved under the documented-independent-audit convention. This review was performed by AI. It does not assert human peer review, publication, proof-assistant verification or novelty priority. The submitted package retains its original pending-review wording.

### Previous status review at the pinned revision

**Literature check:** Open in cited literature; no later resolution located.

The 2025 question explicitly leaves smooth real coefficients on Lipschitz domains unresolved. The smooth-boundary theorem was checked, and searches through the review date for Lipschitz DtN Poisson bounds and subsequent ter Elst–Ouhabaz papers located no result in this class. Estimates for the bulk heat kernel are different.
