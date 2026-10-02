# 166. Anomalous viscous dissipation with fixed large-scale forcing

**Area:** Turbulence and energy transfer

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Does there exist a nonzero, time-independent, mean-zero, divergence-free trigonometric polynomial $`f`$ on $`\mathbb T^3`$, a sequence $`\nu_j\downarrow0`$, and global Leray–Hopf solutions $`u_j`$ of

```math
\partial_tu_j+(u_j\cdot\nabla)u_j+\nabla p_j=\nu_j\Delta u_j+f,\qquad\mathop{\mathrm{div}}\nolimits u_j=0,
```

with mean-zero initial velocities uniformly bounded in $`L^2`$, such that

```math
\sup_j\limsup_{T\to\infty}\frac1T\int_0^T\|u_j(t)\|_2^2\,dt<\infty,
```



```math
0<\lim_{j\to\infty}\left[\limsup_{T\to\infty}\frac{\nu_j}{T}\int_0^T\|\nabla u_j(t)\|_2^2\,dt\right]<\infty?
```

Leray–Hopf means distributional solutions in $`L^\infty_{\mathrm{loc},t}L^2_x\cap L^2_{\mathrm{loc},t}H^1_x`$ satisfying the energy inequality. The same finite set of forced spatial frequencies and the same forcing amplitudes are used for every viscosity.

## Application

This is a precise large-scale-forcing version of the turbulence prediction that viscous energy loss stays positive as viscosity tends to zero, while kinetic energy remains bounded.

## References

1. Tristan Buckmaster and Vlad Vicol, *Convex integration and phenomenologies in turbulence*, EMS Surveys in Mathematical Sciences 6 (2019). [Author text](https://cims.nyu.edu/~vicol/BV2.pdf). §8, Problem 10, asks for positive finite long-time dissipation with viscosity-independent forcing scales.

2. Elia Bruè and Camillo De Lellis, *Anomalous Dissipation for the Forced 3D Navier–Stokes Equations*, Communications in Mathematical Physics 400 (2023), 1507–1533. [Article](https://doi.org/10.1007/s00220-022-04626-0). Main theorem allows viscosity-dependent forces with controlled regularity.

3. Bartosz Protas, *Extreme flows: where physics meets mathematically rigorous bounds* (2026). [Paper](https://arxiv.org/html/2608.04859v1). §5.2 reviews the unresolved dissipation-anomaly problem and recent conditional constructions.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This fixes the forcing in the published large-scale question and explicitly excludes divergent average kinetic energy. Searches for “anomalous dissipation fixed smooth force”, “anomalous dissipation smooth forcing open Navier”, and “Navier Stokes dissipation anomaly 2026” found constructions using viscosity-dependent small-scale forcing or other hypotheses. No result meeting this fixed trigonometric-forcing formulation was located. The order of limits is long time first, then vanishing viscosity.
