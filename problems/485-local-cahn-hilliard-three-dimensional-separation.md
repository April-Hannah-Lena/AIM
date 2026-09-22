# 485. Instantaneous strict separation for three-dimensional local Cahn–Hilliard

**Area:** Phase-field PDEs; binary mixtures

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^3$ be smooth, bounded and connected, and $0<\theta<\theta_0$. Consider
$$
\partial_tu=\Delta\mu,\qquad
\mu=-\Delta u+\frac\theta2\log\frac{1+u}{1-u}-\theta_0u,
\qquad\partial_\nu u=\partial_\nu\mu=0.
$$
Take $u_0\in H^1(\Omega)$ with $|u_0|\le1$ almost everywhere and $|\Omega|^{-1}\int_\Omega u_0\in(-1,1)$. Let $u$ be the global energy weak solution: $u\in L^\infty(0,T;H^1)\cap H^1(0,T;H^1{}^*)$, $\mu\in L^2(0,T;H^1)$, the equations hold weakly, and the free energy decreases by $\int|\nabla\mu|^2$. The logarithmic energy density uses the continuous convention $0\log0=0$.

For every $\tau>0$, must there exist $\delta=\delta(\tau,u_0,\Omega,\theta,\theta_0)>0$ such that
$$\mathop{\rm ess\,sup}_{(x,t)\in\Omega\times[\tau,\infty)}|u(x,t)|\le1-\delta?$$
There is no initial separation or small-energy assumption. The Laplacian in the chemical potential is local and the mobility is constant.

## Applied significance

The separation bound prevents a binary-mixture order parameter from approaching a pure phase where its logarithmic chemical potential becomes singular.

## References

1. C. G. Gal and A. Poiatti, *Unified framework for the separation property in binary phase-segregation processes with singular entropy densities*, European J. Appl. Math. **36** (2025), 40–67, §§6.1.1–6.3. [Article](https://doi.org/10.1017/S0956792524000196).
2. C. Hurm, P. Knopf and A. Poiatti, *Nonlocal-to-local convergence rates for strong solutions to a Navier–Stokes–Cahn–Hilliard system with singular potential*, Comm. Partial Differential Equations **49** (2024), 832–871, Introduction's discussion of the missing uniform separation bound. [Article](https://doi.org/10.1080/03605302.2024.2401445).
3. A. Poiatti, *The 3D strict separation property for the nonlocal Cahn–Hilliard equation with singular potential*, Analysis & PDE **18** (2025), 109–139. [Article](https://doi.org/10.2140/apde.2025.18.109).

## Status review

The first two sources distinguish this open local three-dimensional problem from proved separation in two dimensions, at sufficiently late times, or near an energy minimizer. The third source resolves the nonlocal equation, whose chemical potential has an integral interaction operator instead of $-\Delta u$. Searches on 2026-09-22 for local three-dimensional logarithmic Cahn–Hilliard instantaneous separation found no matching theorem. Numerical separation, stronger singular potentials, and eventual separation do not settle the stated quantifier “every $\tau>0$.”
