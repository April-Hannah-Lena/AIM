# 428. Completeness of modes for slowly growing imaginary Schrödinger potentials

**Area:** Nonselfadjoint Schrödinger equations and modal expansions

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For each $`0<\alpha\le1/2`$, define $`A_\alpha`$ on $`L^2(0,\infty)`$ by

```math
A_\alpha u=-u''+i x^\alpha u,
```



```math
D(A_\alpha)=\{u\in L^2:u\in H^2_{\mathrm{loc}}([0,\infty)),\ -u''+ix^\alpha u\in L^2,\ u(0)=0\}.
```

Is the closed linear span of all its eigenfunctions equal to $`L^2(0,\infty)`$? Completeness alone is requested, with no Riesz-basis or stable-expansion assertion. This is the small-exponent part of Almog’s original $`0<\alpha\le2/3`$ question.

## Application

Spatially increasing imaginary potentials model absorption. Completeness determines whether all square-integrable initial wave profiles can be approximated by finite combinations of the damped normal modes.

## References

1. Y. Almog, [Completeness of eigenfunctions for Schrödinger operators with complex potentials](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-01/2015-01_AIM_Almog_1.pdf), AIM problem 2015-01.
2. S. Tumanov, [Completeness theorem for the system of eigenfunctions of the complex Schrödinger operator with power potential](https://arxiv.org/abs/2101.01680), *Journal of Differential Equations* **319** (2022), 80–99, introduction, Theorem 1 and its corollary.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Tumanov proves completeness when $`|\arg c|<\theta_0(\alpha)<\pi\alpha`$, including $`c=i`$ for exponents sufficiently close to $`2/3`$. For $`0<\alpha\le1/2`$, this sector cannot contain $`\arg i=\pi/2`$. Searches for later Tumanov, Almog, and imaginary power-potential completeness results through the review date found no theorem covering this remaining range.
