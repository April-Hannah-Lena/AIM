# 541. Optimal stable manifold widths of Besov balls

**Area:** Stable nonlinear approximation and numerical analysis

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`\Omega=[0,1]^d`$, $`d\ge1`$, $`1\le p,q,r\le\infty`$, and $`s>0`$ satisfy $`s>d(1/q-1/p)`$, with $`1/\infty=0`$. Write $`X=L^p(\Omega)`$ and let $`K`$ be the unit ball of $`B^s_{q,r}(\Omega)`$, which is compact in $`X`$ under this strict embedding condition.

Fix the following Besov norm convention. Choose the integer $`m=\lfloor s\rfloor+1`$, define

```math
\Delta_h^m f(x)=\sum_{j=0}^m(-1)^j\binom mj f(x+jh),\qquad \omega_m(f,t)_q=\sup_{|h|\le t}\|\Delta_h^m f\|_{L^q(\Omega_{mh})},
```

where $`\Omega_{mh}=\{x\in\Omega:x+mh\in\Omega\}`$. For $`r<\infty`$, put

```math
\|f\|_{B^s_{q,r}}=\|f\|_{L^q}+\left(\int_0^1[t^{-s}\omega_m(f,t)_q]^r\,\frac{dt}{t}\right)^{1/r};
```

for $`r=\infty`$, replace the integral term by $`\sup_{0<t\le1}t^{-s}\omega_m(f,t)_q`$. Thus $`K=\{f:\|f\|_{B^s_{q,r}}\le1\}`$.

For $`\gamma\ge1`$ define the stable manifold width

```math
\delta^*_{n,\gamma}(K)_X=\inf_{\|\cdot\|_Y,a,M}\ \sup_{f\in K}\|f-M(a(f))\|_X,
```

where the infimum ranges over norms on $`\mathbb R^n`$ and maps $`a:K\to(\mathbb R^n,\|\cdot\|_Y)`$ and $`M:(\mathbb R^n,\|\cdot\|_Y)\to X`$ satisfying

```math
\|a(f)-a(g)\|_Y\le\gamma\|f-g\|_X,\qquad \|M(y)-M(z)\|_X\le\gamma\|y-z\|_Y
```

on their entire respective domains. The norm and maps may depend on $`n`$; $`\gamma`$ must not.

For every fixed admissible $`(d,s,p,q,r)`$, do there exist constants $`\gamma<\infty`$ and $`C<\infty`$, independent of $`n`$, such that

```math
\delta^*_{n,\gamma}(K)_{L^p}\le Cn^{-s/d}\qquad(n\ge1)?
```

The matching lower order $`n^{-s/d}`$ is known. The question is whether optimal nonlinear approximation can always be achieved with both parameter selection and reconstruction uniformly Lipschitz stable. This entry takes the Besov-family part of the broader smoothness-class question in [1, §6.4]; it counts the parameter family once.

## Application

These widths measure how accurately numerical methods can encode and reconstruct functions using finitely many real parameters while controlling sensitivity to input and parameter errors. They provide benchmarks for adaptive approximation, reduced models and signal compression. Existence of optimal maps would not by itself provide an efficient training or evaluation algorithm.

## References

1. A. Cohen, R. DeVore, G. Petrova and P. Wojtaszczyk, [Optimal Stable Nonlinear Approximation](https://doi.org/10.1007/s10208-021-09494-z), Foundations of Computational Mathematics **22** (2022), 607–648; equations (1.6)–(1.7), Theorem 4.1 and §6.4, especially (6.15).
2. J. W. Siegel, [Sharp lower bounds on the manifold widths of Sobolev and Besov spaces](https://doi.org/10.1016/j.jco.2024.101884), Journal of Complexity **85** (2024), 101884; [preprint v4](https://arxiv.org/abs/2402.04407v4), definition (1.1) and Theorem 2.
3. G. Petrova and P. Wojtaszczyk, [Lipschitz widths](https://arxiv.org/abs/2111.01341), §6, especially Theorems 6.1–6.2, comparing decoder-only Lipschitz widths with stable manifold widths.

## Status review

**Known cases:** For $`p=2`$, [1, Theorem 4.1] bounds stable widths with a fixed stability constant by entropy numbers after a constant-factor change in dimension; this gives the requested rate. The lower bound in [1, (6.15)] also follows from the sharp ordinary manifold-width lower bound in [2], since admissible Lipschitz maps are continuous.

**Remaining target:** Establish the upper bound throughout the non-Hilbert parameter range not covered by existing stable constructions, or disprove it for an admissible Besov ball. No assertion is made that every individual choice with $`p\ne2`$ is unresolved.

The sharp ordinary manifold-width theorem [2] imposes continuity, without a uniform Lipschitz bound. Decoder-only Lipschitz and Hölder widths likewise do not enforce the required stability of $`a`$. Their optimal rates therefore do not settle this question.

No matching complete resolution or announcement was found in the literature, arXiv, author-page, GitHub-indexed, Zenodo-indexed and native Palomar checks on the date above. Native Zenodo access returned HTTP 403.
