# 148. An inertial manifold for the two-dimensional Navier–Stokes flow

**Area:** Fluid mechanics and reduced models

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $`\mathbb T^2`$, fix $`\nu>0`$ and a smooth time-independent, mean-zero, divergence-free force $`f`$. Let $`S(t)`$ be the solution semigroup on the Hilbert space $`H`$ of mean-zero divergence-free $`L^2`$ velocities for

```math
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u+f.
```

Does every such system admit a finite-dimensional Lipschitz inertial manifold? Here this means a graph $`\mathcal M=\{p+\Phi(p):p\in P H\}`$ over a finite-rank orthogonal projection $`P`$, with Lipschitz $`\Phi:PH\to(I-P)H`$, such that $`S(t)\mathcal M\subset\mathcal M`$, the global attractor is contained in $`\mathcal M`$, and some $`\gamma>0`$ satisfies

```math
\sup_{u\in B}\mathop{\mathrm{dist}}\nolimits_H(S(t)u,\mathcal M)\le C_Be^{-\gamma t}
```

for every bounded $`B\subset H`$ and all $`t\ge0`$.

## Application

An affirmative result would give an exact finite-dimensional description of the long-time flow with an exponential error bound for transients.

## References

1. Sergey Zelik, *Attractors. Then and now*, Russian Mathematical Surveys 78 (2023), 635–777. [Publisher record and full text](https://www.mathnet.ru/eng/rm10095). Inertial-manifold discussion explicitly identifies two-dimensional Navier–Stokes as open.

2. Yanqiu Guo, *Inertial manifolds for the two-dimensional hyperviscous Navier–Stokes equations* (2024 preprint). [Paper](https://arxiv.org/abs/2401.14642). Main theorem concerns dissipation $`(-\Delta)^\beta`$ with $`\beta>17/12`$, not ordinary viscosity $`\beta=1`$.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cited survey distinguishes finite-dimensional attractors from inertial manifolds. Searches for “inertial manifold two dimensional Navier Stokes open problem 2025 2026” and “inertial manifolds Zelik 2023 survey” found hyperviscous and modified-equation results but no construction or obstruction for the ordinary equation stated here. A spectral-gap obstruction to one proof method is not a nonexistence theorem.
