# Draft — Critical quadratic noise and the Allen–Cahn energy maximum

**Area:** Stochastic PDEs; phase separation

**Status:** Held for a formulation concern; excluded from the active catalogue.

**Last checked:** 2026-09-22

## Problem statement

Let $`\mathbb T=\mathbb R/\mathbb Z`$ and let $`W`$ be one real standard Brownian motion. For an $`\mathcal F_0`$-measurable random initial condition $`u_0\in L^2(\Omega;L^2(\mathbb T))`$, consider the Itô equation

```math
du=(\partial_{xx}u+u-u^3)\,dt+\sqrt2\,u^2\,dW_t,\qquad u(0)=u_0.
```

Use its global variational solution with almost surely continuous $`L^2(\mathbb T)`$ paths and locally square-integrable $`H^1(\mathbb T)`$ paths. Is it true that, for every finite $`T>0`$, there is a finite deterministic $`C_T`$, independent of the law of $`u_0`$, such that

```math
\mathbb E\sup_{0\le t\le T}\|u(t)\|_{L^2(\mathbb T)}^2
\le C_T\bigl(1+\mathbb E\|u_0\|_{L^2(\mathbb T)}^2\bigr)?
```

The coefficient $`\sqrt2`$ is part of the question: it is the endpoint at which the cubic damping and the Itô correction balance in the basic energy estimate.

## Applied significance

This asks whether a phase-field model retains an integrable maximum energy when multiplicative fluctuations are as strong as its elementary dissipation estimate allows.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 4 and §6.3.1. [Published article](https://doi.org/10.1007/s00030-025-01090-2).
2. A. Agresti and M. Veraar, *The critical variational setting for stochastic evolution equations*, Probab. Theory Related Fields (2024), global existence and energy estimates. [Author preprint](https://arxiv.org/abs/2206.00230).

## Status review

The survey explicitly isolates this one-dimensional model and the endpoint $`\gamma^2=2`$; its estimates for $`\gamma^2<2`$ do not answer the question. Searches on 2026-09-22 for the equation, “quadratic noise”, endpoint energy moments, and Agresti–Veraar found no later endpoint estimate or counterexample. Boundary-preserving Allen–Cahn approximations using noise $`1-u^2`$ concern a different coefficient and bounded state interval. This entry asks for a moment estimate, not for existence of the already constructed variational solution.

## Editorial hold

The cross-review raised a material concern about the endpoint maximum-moment claim after restricting the equation to spatially constant data. Although the cited survey explicitly calls this model case open, the catalogue has not adjudicated that concern. The candidate was replaced before receiving an identifier. This is an exclusion for unresolved formulation reliability, not a claim that a published resolution was found or that the catalogue has proved a counterexample.
