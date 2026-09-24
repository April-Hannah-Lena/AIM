# 392. Uniqueness of bounded semigeostrophic potential vorticity

**Area:** Geophysical PDEs / nonlinear transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix a ball $\Omega\subset\mathbb R^3$ of volume one and a compactly supported probability density $\rho_0\in L^\infty(\mathbb R^3)$. For every $t$, let $T_t=\nabla P_t^*$ be the quadratic-cost optimal transport map carrying $\rho_t(y)\,dy$ to $\mathbf1_\Omega(x)\,dx$. Set $J(a,b,c)=(-b,a,0)$.
Is there at most one distributional solution
$$\partial_t\rho+\nabla_y\!\cdot\bigl[\rho J(y-T_t(y))\bigr]=0,\qquad \rho|_{t=0}=\rho_0,$$
among nonnegative probability densities that are narrowly continuous in time and, on each finite interval $[0,T]$, are uniformly bounded in $L^\infty$ and supported in a common compact set? Narrow continuity means continuity of $\int\phi\rho_t$ for every bounded continuous $\phi$. Equality of solutions means equality of their measures at every time.

## Application

This asks whether bounded initial atmospheric potential vorticity determines a unique predicted semigeostrophic evolution. It concerns weak solutions, including fronts, rather than the separate persistence of smoothness.

## References

1. D. P. Bourne, C. P. Egan, B. Pelloni and M. Wilkinson, *Semi-discrete optimal transport methods for the semi-geostrophic equations*, Calculus of Variations and PDE 61 (2022), article 39, §1, equations (1)–(2), and §3. [Full text](https://doi.org/10.1007/s00526-021-02133-z).
2. T. Lavier, *A semi-discrete optimal transport scheme for the 3D incompressible semi-geostrophic equations*, IMA Journal of Applied Mathematics 90 (2025), 443–464, Remark 1.1. [Full text](https://doi.org/10.1093/imamat/hxaf023).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Both sources distinguish available existence results from unresolved weak uniqueness. The ball and bounded-density assumptions select a concrete subclass of their question and make the transport velocity unambiguous almost everywhere. Searches through 22 September 2026 included semigeostrophic bounded-vorticity uniqueness, weak–strong uniqueness and entropic approximation. Local Hölder uniqueness and uniqueness relative to a uniformly convex strong solution do not prove uniqueness between two arbitrary bounded weak solutions.
