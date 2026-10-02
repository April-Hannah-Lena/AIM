# 639. Strong convergence rate of the fractional WIS Euler integrator

**Area:** Numerical stochastic differential equations

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Fix $`T>0`$, $`H\in(0,1)`$, $`\alpha,\beta,x_0\in\mathbb R`$, and a globally Lipschitz function $`a:\mathbb R\to\mathbb R`$ of at most linear growth. Let $`B^H`$ be centered fractional Brownian motion with covariance

```math
\mathbb E[B^H(t)B^H(s)]=\tfrac12(t^{2H}+s^{2H}-|t-s|^{2H}).
```

Consider

```math
dX(t)=[\alpha X(t)+a(X(t))]dt+\beta X(t)\,dB^H(t),\qquad X(0)=x_0,
```

where the stochastic integral has the Wick–Itô–Skorohod interpretation of [1].

For $`n\ge1`$, set $`h=T/n`$, $`t_i=ih`$, and

```math
J_i=\exp\!\left(-\alpha t_i+\frac{\beta^2}{2}[T^{2H}-(T-t_i)^{2H}]-\beta B^H(t_i)\right),\qquad 0\le i\le n.
```

Using exact samples from the same fractional Brownian path as $`X`$, define

```math
Z_0=x_0,\qquad Z_{i+1}=Z_i+hJ_i a(Z_i/J_i),\qquad X_n=Z_n/J_n.
```

This is the terminal-time GfBm_EM scheme in [1, equations (3.12)–(3.13)]. Does every such fixed problem admit a finite constant $`C`$, independent of $`n`$, such that

```math
\bigl(\mathbb E|X(T)-X_n|^2\bigr)^{1/2}\le C h^{\min\{H+1/2,1\}}?
```

The question concerns the autonomous drift and the stated scheme; the constant may depend on all fixed problem data.

## Application

This determines the time-step accuracy attainable when simulating stochastic models with correlated multiplicative noise.

## References

1. U. Erdoğan, G. J. Lord and R. B. Schieven, [Numerical approximation of SDEs driven by fractional Brownian motion for all H ∈ (0,1) using WIS integration](https://doi.org/10.1093/imanum/drag055), *IMA Journal of Numerical Analysis* (2026). [arXiv:2404.07013v2](https://arxiv.org/abs/2404.07013v2), conjectured estimate (1.3), Assumption 3.1, equations (3.12)–(3.13), Theorem 3.6 and Section 6.

## Status review

**Known cases:** Theorem 3.6 gives the weaker rate $`h^H`$. The source reports order one for the Brownian case $`H=1/2`$ and exactness when $`a=0`$.

**Remaining target:** Establish or refute the displayed improved rate for general autonomous Lipschitz drift and $`H\ne1/2`$. Correlated error terms obstruct the source's argument. Targeted literature, arXiv, GitHub, Zenodo and Palomar searches found no matching resolution; these checks are bounded announcement searches. No equivalent catalogue entry was found.
