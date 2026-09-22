# 478. Hölder regularity under directional nonlocal ellipticity alone

**Area:** Nonlocal PDEs; heterogeneous jump diffusion

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $n\ge2$, $0<s<1$, $\lambda>0$ and $\Lambda>1$. For each $x\in B_1$, let $K_x$ be an even nonnegative measure on $\mathbb R^n\setminus\{0\}$, measurably dependent on $x$, satisfying for all $r>0$ and all unit $e$
$$r^{2s}K_x(B_{2r}\setminus B_r)\le\Lambda,\qquad
r^{2s-2}\int_{B_{\Lambda r}\setminus B_r}|e\cdot y|^2K_x(dy)\ge\lambda.$$
For smooth bounded $u$, set
$$L_xu(x)=\frac12\int[2u(x)-u(x+y)-u(x-y)]K_x(dy).$$
Do there exist $\gamma>0$ and $C<\infty$, depending only on $n,s,\lambda,\Lambda$, such that every bounded continuous viscosity solution of $L_xu=0$ in $B_1$ satisfies
$$\|u\|_{C^\gamma(B_{1/2})}\le C\|u\|_{L^\infty(\mathbb R^n)}?$$
Require no continuity or small-oscillation condition in $x$, and no pointwise density lower bound on the jump measures. Use test functions patched with $u$ outside the contact neighborhood to define the nonlocal viscosity inequalities.

## Application

The jump measures describe a medium in which long-range transport can favor a few directions that change from place to place. A Hölder estimate would quantitatively limit the spatial variation of bounded stationary fields using directional transport strength alone, without imposing a smooth medium or jumps in every individual direction.

## References

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. R. W. Schwab and L. Silvestre, *Regularity for parabolic integro-differential equations with very irregular kernels*, Analysis & PDE **9** (2016), 727–772. [Article](https://doi.org/10.2140/apde.2016.9.727).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The statement is Open Question 3.4, with equations (3.6.3)–(3.6.5), in §3.6.4 of the book. Searches on 2026-09-22 checked directional ellipticity, singular jump kernels and rough-coefficient Hölder estimates. Located theorems require positive-measure directional lower bounds, comparable energy forms, or small spatial oscillation. New regularity from a coercive Hamiltonian does not apply to this homogeneous linear equation. No matching resolution was found.
