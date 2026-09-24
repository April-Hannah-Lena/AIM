# 074. Global regularity for supercritical dissipative surface quasi-geostrophic flow

**Area:** Geophysical fluid dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For each fixed $`0<\gamma<1`$, determine whether every smooth mean-zero real datum $`\theta_0`$ on $`\mathbb T^2`$ generates a global smooth solution of

```math
\partial_t\theta+(\mathcal R^\perp\theta)\cdot\nabla\theta+
(-\Delta)^{\gamma/2}\theta=0,\qquad \theta(0)=\theta_0.
```

Here $`\mathcal R_j`$ is the periodic Riesz transform with multiplier $`-ik_j/|k|`$ at nonzero Fourier mode $`k`$, $`\mathcal R^\perp=(-\mathcal R_2,\mathcal R_1)`$, and the fractional Laplacian has multiplier $`(2\pi|k|)^\gamma`$. No smallness restriction or dependence of $`\gamma`$ on the datum is allowed.

## Application

SQG models the transport of temperature at a geophysical boundary and provides a concrete test of nonlinear transport against weak diffusion.

## References

- [Michele Coti Zelati and Vlad Vicol, *On the global regularity for the supercritical SQG equation* (2014 preprint; Indiana Univ. Math. J., 2016), abstract and main theorem](https://arxiv.org/abs/1410.3186).
- [Anuj Kumar, *Existence of weak solutions to the generalized SQG equations in Sobolev spaces* (2026), introduction](https://arxiv.org/abs/2608.23059).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The August 2026 paper still identifies the supercritical smooth-solution problem as open. Coti Zelati–Vicol allow the dissipation exponent to approach the critical value depending on the size of the initial datum. That quantifier order does not resolve any fixed arbitrary exponent for all data; weak or eventual regularity is also insufficient.

Searches run on 2026-09-08: `site.arxiv.org supercritical SQG global regularity open 2026`; `Global regularity in the supercritical generalized SQG regime`. This is a literature search, not a proof that no solution exists.
