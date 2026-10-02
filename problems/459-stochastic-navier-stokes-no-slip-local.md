# 459. Local no-slip Navier–Stokes theory under non-small transport noise

**Area:** Stochastic fluid PDEs; solid boundaries

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`D\subset\mathbb R^3`$ be bounded with smooth boundary, $`\nu>0`$, and $`b_1,\ldots,b_K\in C^\infty(\overline D;\mathbb R^3)`$ be divergence-free, tangent to $`\partial D`$, and satisfy

```math
\nu I-\tfrac12\sum_kb_k\otimes b_k\ge\delta I\quad(\delta>0).
```

For every smooth divergence-free $`u_0`$ vanishing on $`\partial D`$, does

```math
du=[\nu\mathbb P_D\Delta u-\mathbb P_D\nabla\cdot(u\otimes u)]dt+\sum_k\mathbb P_D[(b_k\cdot\nabla)u]dW^k_t,\qquad u|_{\partial D}=0,
```

have a pathwise unique local adapted solution in

```math
C([0,\tau];B^{1/2}_{4,4}(D;\mathbb R^3))\cap L^4(0,\tau;W^{1,4}_0(D;\mathbb R^3))
```

for an almost surely positive stopping time $`\tau`$, with continuous dependence in probability after common stopping? Here $`\mathbb P_D`$ is the Helmholtz projection and the equation is understood in the weak solenoidal $`W^{-1,4}`$ space, or equivalently by the extrapolated Dirichlet Stokes semigroup. Require only the displayed stochastic parabolicity condition on noise amplitude, rather than a perturbatively small norm of $`b`$.

## Application

Solid walls impose a physically important constraint on turbulent transport models; a local theory is needed before questions of long-time behavior can be posed in this setting.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 9. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. D. Goodair, *Navier-Stokes Equations with Navier Boundary Conditions and Stochastic Lie Transport: Well-Posedness and Inviscid Limit*, discussion of the no-slip obstruction. [Author manuscript](https://arxiv.org/abs/2308.04290).
3. D. Goodair, *Anisotropic Inviscid Limit for the Navier-Stokes Equations with Transport Noise Between Two Plates* (2026 preprint). [Preprint](https://arxiv.org/abs/2603.13199).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open Problem 9 requests a non-small-noise local theory for no-slip domains; the statement specifies one subcritical maximal-regularity solution class. Searches on 2026-09-22 checked Goodair's boundary results and 2026 transport-noise papers. Navier-slip strong solutions do not impose the displayed zero trace, and the 2026 no-slip inviscid-limit theorem uses weak martingale solutions rather than this pathwise unique local class. Perturbative small-noise arguments do not establish the full parabolicity range.
