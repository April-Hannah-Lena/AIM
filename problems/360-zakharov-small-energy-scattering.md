# 360. Scattering of arbitrary small energy data for the three-dimensional Zakharov system

**Area:** Plasma physics; dispersive asymptotics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Is there $`\varepsilon>0`$ such that every datum $`(u_0,n_0,n_1)\in H^1(\mathbb R^3;\mathbb C)\times L^2(\mathbb R^3;\mathbb R)\times\dot H^{-1}(\mathbb R^3;\mathbb R)`$ satisfying

```math
\|u_0\|_{H^1}+\|n_0\|_2+\|n_1\|_{\dot H^{-1}}<\varepsilon
```

produces a global solution of

```math
i\partial_tu-\Delta u=nu,\qquad\partial_{tt}n-\Delta n=-\Delta|u|^2
```

that scatters as $`t\to\pm\infty`$? Precisely, for each sign require a free Schrödinger solution $`u_{\pm}^{\rm lin}`$ and a free wave $`n_{\pm}^{\rm lin}`$ such that

```math
\|u-u_{\pm}^{\rm lin}\|_{H^1}+\|n-n_{\pm}^{\rm lin}\|_2+\|\partial_tn-\partial_tn_{\pm}^{\rm lin}\|_{\dot H^{-1}}\longrightarrow0.
```

No radial symmetry, spatial weights or additional angular regularity may be imposed.

## Application

Scattering means a weak plasma disturbance eventually behaves as uncoupled linear waves. This asks whether finite small energy alone guarantees that nonlinear wave–density interactions become negligible.

## References

1. Z. Guo and K. Nakanishi, [*Global dynamics above the ground state energy for the 3D Zakharov system*](https://arxiv.org/abs/2608.14993), preprint (2026), §1, paragraph immediately before the first-order formulation (1.4), explicitly identifying nonradial small-energy scattering as open.
2. Z. Guo and K. Nakanishi, [*Small energy scattering for the Zakharov system with radial symmetry*](https://arxiv.org/abs/1203.3959), Communications in Mathematical Physics 324 (2013), 359–371, main theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using nonradial Zakharov scattering, small energy, angular regularity, and 2025–2026 results. The August 2026 primary source explicitly retains the displayed issue even for small data. The radial theorem and weighted or angularly regular scattering results impose hypotheses absent here. This concerns asymptotic completeness of small disturbances, independently of finite-time collapse for large disturbances. No later unweighted nonradial energy-space theorem was located.
