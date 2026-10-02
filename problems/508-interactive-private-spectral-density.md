# 508. Sharp interactive privacy rates for spectral density estimation

**Area:** Statistical inference, time series and local differential privacy

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix $`s>1/2`$, $`C_0>1`$ and $`C_1>0`$. For an even, nonnegative, $`2\pi`$-periodic spectral density $`f`$, write

```math
\gamma_f(h)=\int_{-\pi}^{\pi}f(\lambda)e^{ih\lambda}\,d\lambda,
\qquad \rho_f(h)=\gamma_f(h)/\gamma_f(0).
```

Consider the class

```math
\mathcal F(C_0,C_1,s)=\left\{f:\ C_0^{-1}\le\gamma_f(0)\le C_0,
\quad\sum_{h\in\mathbb Z\setminus\{0\}}|h|^{2s}|\rho_f(h)|^2\le C_1^2\right\}.
```

The data $`X_1,\ldots,X_n`$ are consecutive observations of a centered, real stationary Gaussian process with spectral density $`f\in\mathcal F(C_0,C_1,s)`$.

A sequentially interactive mechanism releases $`Z_i`$ through a Markov kernel $`Q_i(\cdot\mid X_i,Z_{<i})`$ into a standard Borel space. Require, for every measurable output set $`B`$, every history $`z_{<i}`$ and all $`x,x'\in\mathbb R`$,

```math
Q_i(B\mid x,z_{<i})\le e^\alpha Q_i(B\mid x',z_{<i}).
```

Let $`\mathcal Q^{\mathrm{seq}}_{n,\alpha}`$ be the class of these mechanisms. Each release can use its own raw observation and earlier releases; it has no access to earlier raw observations.

Determine the joint dependence on $`n`$ and $`\alpha`$ of

```math
\mathcal R^{\mathrm{seq}}_{n,\alpha}
=\inf_{Q\in\mathcal Q^{\mathrm{seq}}_{n,\alpha}}\inf_{\widehat f}
\sup_{f\in\mathcal F(C_0,C_1,s)}
\mathbb E_{f,Q}\!\left[\int_{-\pi}^{\pi}|\widehat f(Z_{1:n})(\lambda)-f(\lambda)|^2\,d\lambda\right],
```

uniformly for $`n\ge2`$ and $`0<\alpha\le1`$. Here $`\widehat f`$ ranges over measurable $`L^2([-\pi,\pi])`$-valued estimators. The fixed class parameters are known to the mechanism and estimator. Seek matching bounds up to constants depending only on $`C_0,C_1,s`$, including any necessary logarithmic factors and the regime in which consistent estimation is impossible.

## Application

Spectral densities describe temporal dependence in correlated measurements. Sharp interactive rates would quantify how much accuracy can be recovered when each data holder may consult earlier privatized releases before transmitting a private measurement.

## References

1. C. Butucea, K. Klockmann and T. Krivobokova, [Nonparametric Spectral Density Estimation using Interactive Mechanisms under Local Differential Privacy](https://www.jmlr.org/papers/v27/25-0680.html), Journal of Machine Learning Research **27**(168) (2026), 1–49. The open question on p.5, the sequential privacy definition in §2, and global estimation in §2.4. [arXiv:2504.00919v3](https://arxiv.org/abs/2504.00919v3).
2. Y. Issartel and F. Roueff, [On the privacy cost for dependent Gaussian data: spectral density estimation under local differential privacy](https://arxiv.org/abs/2608.24847), arXiv:2608.24847v1 (25 August 2026). Equation (3), Theorems 1 and 3, and §3.4, “Interactive privacy.”

## Status review

The class above is the explicitly variance-bounded class in [2]. That preprint announces the sharp **non-interactive** rate

```math
\mathcal R^{\mathrm{NI}}_{n,\alpha}\asymp
1\wedge(n\alpha^4)^{-2s/(2s+1)},\qquad 0<\alpha\le1.
```

Its definition restricts each release to a channel depending only on $`X_i`$. Consequently, its lower bound does not establish an interactive lower bound. Section 3.4 explicitly leaves sharp interactive rates open and refers to [1].

Reference [1] constructs sequential mechanisms and leaves their global minimax optimality unresolved. The target here is the remaining interactive problem, with privacy allowed to strengthen as the sample size grows. It does not ask to re-establish the non-interactive result or assert that the currently available interactive bound is sharp.

Primary statements, version histories and the authors' public simulation repository were checked. Searches on 24 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar, located the non-interactive announcement above but no matching interactive resolution.
