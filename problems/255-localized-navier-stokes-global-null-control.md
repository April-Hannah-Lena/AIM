# 255 — Small-time global null control of no-slip Navier–Stokes flow

**Area:** Fluid control / distributed actuation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be a bounded connected smooth domain, $`\varnothing\ne\omega\Subset\Omega`$ an open set, and $`T>0`$. Let $`H`$ be the $`L^2(\Omega)^3`$ closure of smooth compactly supported divergence-free vector fields. For every $`u_0\in H`$, does there exist $`f\in L^2(\omega\times(0,T))^3`$ and a Leray–Hopf weak solution of

```math
\partial_tu+(u\cdot\nabla)u-\Delta u+\nabla p=\mathbf1_\omega f,\qquad \nabla\cdot u=0,
```

with $`u=0`$ on $`\partial\Omega`$, $`u(0)=u_0`$, and $`u(T)=0`$? Here the solution must belong to $`L^\infty(0,T;H)\cap L^2(0,T;H_0^1(\Omega)^3)`$, be weakly continuous in $`L^2`$, and satisfy the usual energy inequality with forcing. No smallness bound is imposed on $`u_0`$.

## Application

This asks whether localized forcing can stop an arbitrary finite-energy viscous flow in any prescribed positive time while the vessel wall remains fixed.

## References

1. E. Fernández-Cara, *Los Lions (I)* (17 April 2026), [author's University of Seville article](https://institucional.us.es/blogimus/2026/04/los-lions-i/), section “Una conjetura”. Writes this distributed-force, homogeneous-Dirichlet model and explicitly says Lions' conjecture remains open.
2. J.-M. Coron, F. Marbach and F. Sueur, *Small-time global exact controllability of the Navier–Stokes equation with Navier slip-with-friction boundary conditions* (2020), [JEMS 22, 1625–1673](https://doi.org/10.4171/JEMS/952), introduction and main theorem. Establishes the related slip-boundary result and explains the boundary-layer issue.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Small-data local control, large-time dissipation followed by local control, and global results with Navier slip conditions do not give the quantified no-slip statement. Searches included “Navier Stokes global null controllability 2026 no-slip”, “localized distributed Lions conjecture”, and “global controllability curved boundary no-slip”. No arbitrary-data, arbitrary-time theorem in this class was located.
