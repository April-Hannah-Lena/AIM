# 487. Uniqueness of all weak dual solutions of fractional porous-medium flow

**Area:** Nonlocal PDEs; diffusion on curved spaces

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

Let $(M,g)$ be a complete, connected, noncompact Riemannian manifold of dimension $N\ge2$, with $\mathrm{Ric}\ge-(N-1)k$ for some $k\ge0$ and the uniform Faber–Krahn inequality
$\lambda_1(D)\ge c\,\mathrm{Vol}(D)^{-2/N}$ for all relatively compact smooth domains $D\subset M$, with $c>0$. Fix $m>1$ and $0<s<1$ and use the spectral fractional Laplace–Beltrami operator in
$$\partial_tu+(-\Delta_M)^s(u^m)=0.$$

Write $G_s(x,y)=\Gamma(s)^{-1}\int_0^\infty p_t(x,y)t^{s-1}\,dt$, where $p_t$ is the heat kernel, and set
$$\|f\|_{1,x_0,G_s}=\int_{B_1(x_0)}|f|+\int_{M\setminus B_1(x_0)}|f(x)|G_s(x,x_0).$$
All integrals use Riemannian volume. A nonnegative weak dual solution has $u\in C([0,T];L^1_{x_0,G_s})$ for every $x_0,T$, $u^m\in L^1((0,T);L^1_{\rm loc}(M))$, and
$$\int_0^T\!\int_M\bigl[(-\Delta_M)^{-s}u\,\partial_t\psi-u^m\psi\bigr]=0$$
for every compactly supported smooth space-time test function $\psi$.

Given any $u_0\ge0$ with $\sup_{x_0\in M}\|u_0\|_{1,x_0,G_s}<\infty$, are any two such solutions with trace $u_0$ identical? Do not restrict solutions to those constructed by a monotone sequence of bounded integrable approximations.

## Applied significance

The same initial concentration should determine one evolution when nonlinear nonlocal diffusion occurs on a curved substrate.

## References

1. E. Berchio, M. Bonforte, G. Grillo and M. Muratori, *The fractional porous medium equation on noncompact Riemannian manifolds*, Math. Ann. **389** (2024), 3603–3651, Assumption 2.1, Definition 2.1 and §7. [Article](https://doi.org/10.1007/s00208-023-02731-6); [accepted manuscript](https://iris.polito.it/retrieve/handle/11583/2984889/691780).
2. G. Grillo, *The Fractional Porous Medium Equation on noncompact Riemannian manifolds*, Oberwolfach Reports 14/2025, contribution on weak dual solutions and unresolved uniqueness/fundamental solutions. [Workshop report](https://ems.press/content/serial-article-files/51358?nt=1).

## Status review

The 2024 paper proves uniqueness only within its monotone approximation construction and explicitly asks for uniqueness in the full weak dual class in §7. The 2025 Oberwolfach contribution repeats the unresolved uniqueness issue. Searches on 2026-09-22 for weak dual uniqueness, fractional porous-medium manifolds, and later work of the authors found no full-class theorem. Euclidean very-weak uniqueness and local-in-space porous-medium uniqueness on manifolds concern different operators or geometries.
