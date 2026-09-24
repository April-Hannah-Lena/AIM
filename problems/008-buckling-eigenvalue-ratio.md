# 008. The sharp ratio of the first two buckling eigenvalues

**Area:** Elastic stability and eigenvalue inequalities

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`d\ge2`$ and let $`\Omega\subset\mathbb R^d`$ be a bounded connected smooth domain. Let $`0<\Lambda_1\le\Lambda_2\le\cdots`$ be the eigenvalues, with multiplicity, of

```math
\Delta^2u=-\Lambda\Delta u,\qquad u=\partial_\nu u=0\text{ on }\partial\Omega.
```

Prove or disprove the sharp inequality

```math
\frac{\Lambda_2(\Omega)}{\Lambda_1(\Omega)}\le\frac{j_{d/2+1,1}^2}{j_{d/2,1}^2},
```

where $`j_{a,1}`$ is the first positive zero of $`J_a`$. The right side is the ratio for a ball.

## Application

A sharp ratio controls how far apart the first two instability loads can be when a plate or higher-dimensional elastic model changes shape.

## References

1. M. S. Ashbaugh, F. Gesztesy, M. Mitrea, R. Shterenberg and G. Teschl, [A survey on the Krein–von Neumann extension, the corresponding abstract buckling problem, and Weyl-type spectral asymptotics for perturbed Krein Laplacians in nonsmooth domains](https://arxiv.org/abs/1203.5713), in Mathematical Physics, Spectral Theory and Stochastic Analysis (2013), Remark 8.10.
2. A. Chakib, I. Khalil and A. Sadik, [On numerical resolution of shape optimization bi-Laplacian eigenvalue problems](https://doi.org/10.1016/j.matcom.2024.11.007), Mathematics and Computers in Simulation 230 (2025), 149–164.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Remark 8.10 explicitly gives this Bessel-zero conjecture. The 2025 work investigates spectral quotients numerically and supplies no general proof. The 2026 counterexample to a higher-index Dirichlet membrane ratio concerns another operator and another claim.

**Search audit:** “buckling eigenvalue ratio ball conjecture proof 2025 2026”; “buckling Payne Polya Weinberger sharp ratio”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
