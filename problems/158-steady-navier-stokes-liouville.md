# 158. The finite-Dirichlet Liouville problem for steady three-dimensional flow

**Area:** Viscous fluid mechanics

## Problem statement

Suppose $u\in C^\infty(\mathbb R^3;\mathbb R^3)$ and $p\in C^\infty(\mathbb R^3)$ satisfy

$$
-\Delta u+(u\cdot\nabla)u+\nabla p=0,\qquad \nabla\cdot u=0,
$$

$$
\int_{\mathbb R^3}|\nabla u|^2\,dx<\infty,\qquad \lim_{|x|\to\infty}u(x)=0.
$$

Must $u$ vanish identically? No additional integrability or symmetry of $u$, and no rate of its decay, is assumed.

## Applied significance

This would rule out a persistent unforced viscous motion maintained by no boundary or far-field input while having finite viscous dissipation.

## References

1. Tai-Peng Tsai, *Lectures on Navier–Stokes Equations*, Graduate Studies in Mathematics 192, AMS (2018), Conjecture 2.5. [Book](https://doi.org/10.1090/gsm/192). Book formulation of the Liouville question.

2. Dongho Chae, *Liouville Type Theorems for the Stationary Navier–Stokes Equations in $\mathbb R^3$*, Communications in Mathematical Physics 407 (2026), article 53. [Article](https://doi.org/10.1007/s00220-026-05555-y). Introduction, equations (1.1)–(1.4), and Theorem 1.1 give the unresolved baseline and new conditional results.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08.

Chae’s February 2026 introduction still describes the unqualified three-dimensional problem as open. Its new theorem imposes extra head-pressure and velocity asymptotics. Searches for “Navier Stokes Liouville Dirichlet integral open 2026” and the exact 2026 paper title located no subsequent resolution. Results assuming $u\in L^{9/2}$ or axial symmetry impose assumptions absent here.
