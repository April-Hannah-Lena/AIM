# 532. Linear inverse bounds for four-diamond scattering

**Area:** Numerical PDEs and acoustic scattering

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`Q=(-\pi,\pi)^2`$ and $`U_r=\bigcup_{a,b\in\{-1,1\}}B((a\pi,b\pi),r)`$, where $`B(x,r)`$ is the open Euclidean ball. A four-diamond obstacle is a bounded union $`\Omega_-=\bigcup_{j=1}^4\Omega_j\subset\mathbb R^2`$ of disjoint open convex sets with smooth boundary, as in Definition 8.19 of [1]. Writing $`\Gamma=\partial\Omega_-`$, require, for some $`0<\epsilon<\pi/2`$,

```math
\partial Q\setminus U_\epsilon\subseteq\Gamma\subseteq\mathbb R^2\setminus U_{\epsilon/2},\qquad \Omega_-\cap Q=\varnothing.
```

For wavenumber $`k>0`$, put $`\Phi_k(x,y)=\frac{i}{4}H_0^{(1)}(k|x-y|)`$, the outgoing two-dimensional Helmholtz fundamental solution. On $`L^2(\Gamma)`$ define the single- and double-layer operators

```math
V_k\phi(x)=\int_\Gamma\Phi_k(x,y)\phi(y)\,ds(y),\qquad K_k\phi(x)=\int_\Gamma\partial_{\nu(y)}\Phi_k(x,y)\phi(y)\,ds(y),
```

where $`\nu`$ points out of $`\Omega_-`$. Let $`K'_k`$ use $`\partial_{\nu(x)}\Phi_k(x,y)`$ in place of $`\partial_{\nu(y)}\Phi_k(x,y)`$, and set

```math
A_k=\tfrac12I+K_k-ikV_k,\qquad A'_k=\tfrac12I+K'_k-ikV_k.
```

Prove or refute that, for every fixed four-diamond obstacle and every $`k_0>0`$, there is $`C<\infty`$ such that

```math
\|A_k^{-1}\|_{L^2(\Gamma)\to L^2(\Gamma)}+\|(A'_k)^{-1}\|_{L^2(\Gamma)\to L^2(\Gamma)}\le Ck\qquad(k\ge k_0).
```

The constant may depend on the obstacle and $`k_0`$. The bound must hold at every such real frequency; excluding a small exceptional set of frequencies does not settle the problem.

## Application

This bound would quantify the conditioning of boundary integral formulations for a concrete trapping geometry. Combined with existing approximation estimates, it would establish sharp frequency dependence of boundary-element errors and remove an exceptional-frequency restriction from the corresponding pollution result.

## References

1. J. Galkowski and E. A. Spence, [Numerical analysis of the high-frequency Helmholtz equation using semiclassical analysis](https://doi.org/10.1017/S0962492925100275), Acta Numerica **35**, 1–171 (2026), equations (3.8), (8.2), Definition 8.19, Remark 8.22(i) and Appendix B.
2. J. Galkowski, M. Rachh and E. A. Spence, [Helmholtz boundary integral methods and the pollution effect](https://arxiv.org/abs/2507.22797v3), version 3 (21 March 2026), Definition 2.11 and Remark 2.14, equation (2.17).

## Status review

Both references retain the linear-growth conjecture. The known bound for two aligned squares and results allowing exceptional frequencies do not establish this four-obstacle statement. Searches on 24 September 2026 found no matching solution or announcement, including indexed arXiv, Zenodo, GitHub and Palomar searches.
