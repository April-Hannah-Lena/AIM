# 444. Analytic boundary diffusion on continuous functions for Lipschitz domains

**Area:** Elliptic PDEs and analytic semigroups

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For a bounded connected Lipschitz domain $\Omega\subset\mathbb R^d$, $d\ge2$, let $C$ be real symmetric uniformly positive definite with Lipschitz entries on $\overline\Omega$. Let $N$ be the weak Dirichlet-to-Neumann operator for $-\operatorname{div}(C\nabla)$, defined by harmonic extension and conormal differentiation. Its semigroup restricts to a strongly continuous semigroup $T(t)$ on $C(\partial\Omega)$ with the supremum norm.
Must there exist $\theta>0$ such that $T$ extends to an operator-valued holomorphic semigroup on $\{z\ne0:|\arg z|<\theta\}$, with $\sup_{0<|z|\le1,\ |\arg z|\le\theta'}\|T(z)\|<\infty$ for each $0<\theta'<\theta$?

## Application

Analyticity supplies time regularization for boundary evolution driven by flux from a conducting bulk. It matters when boundary data are continuous and the geometry includes corners.

## References

1. A. F. M. ter Elst and E. M. Ouhabaz, [Five Open Problems on the Dirichlet-to-Neumann Operator with Variable Coefficients](https://doi.org/10.1007/s00020-025-02796-9), *Integral Equations and Operator Theory* **97** (2025), article 14, final paragraph of problem 4.
2. W. Arendt and A. F. M. ter Elst, [The Dirichlet-to-Neumann operator on C(partial Omega)](https://arxiv.org/abs/1707.05556), *Annali della Scuola Normale Superiore di Pisa* **20** (2020), 1169–1196, main semigroup theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The second source supplies strong continuity; the first explicitly leaves holomorphy open. A review-date search for subsequent holomorphy results found smooth-domain theorems but no theorem for this Lipschitz class. This asks an endpoint function-space property rather than the separate pointwise Poisson-kernel estimate.
