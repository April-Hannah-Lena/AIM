# 082. Bressan's logarithmic lower bound on the cost of mixing

**Area:** Transport and mixing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix $0<\kappa<1/2$ and $A=\{x\in\mathbb T^2:0<x_1<1/2\}$ on the unit flat torus. Let $b:[0,1]\times\mathbb T^2\to\mathbb R^2$ be smooth and divergence-free, with flow $X_t$. Suppose, for every torus ball $B_\varepsilon(x)$ with $0<\varepsilon<1/4$,
$$
\kappa |B_\varepsilon|\le
|X_1(A)\cap B_\varepsilon(x)|\le(1-\kappa)|B_\varepsilon|.
$$
Does there exist $c_\kappa>0$, independent of $b$ and $\varepsilon$, such that
$$
\int_0^1\int_{\mathbb T^2}|D_xb(t,x)|\,dx\,dt
\ge c_\kappa\log(1/\varepsilon)?
$$
Use the Frobenius norm of the velocity gradient. This is the incompressible geometric-mixing version of the conjecture.

## Application

The inequality would give a universal strain budget for mixing two fluids to a prescribed spatial resolution.

## References

- [Alberto Bressan, *A Lemma and a Conjecture on the Cost of Rearrangements* (2003), originating conjecture](https://arxiv.org/abs/math/0302228).
- [Gianluca Crippa, *The flow associated to weakly differentiable vector fields* (thesis, 2007), Conjecture 7.6.1 and Theorem 7.6.2](https://www.math.ias.edu/delellis/sites/math.ias.edu.delellis/files/Gianluca.pdf).
- [Elia Brué, Maria Colombo and Carl Johan Peter Johansson, *Lyapunov exponents, entropy and mixing for DiPerna-Lions flows* (2025), §1.5](https://arxiv.org/abs/2510.02921).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The October 2025 work proves an asymptotic version for time-periodic flows. It does not give the uniform one-time estimate above for arbitrary smooth time dependence. Results controlling an Lᵖ norm with p>1 and results restricted to shears also leave this endpoint problem.

Searches run on 2026-09-08: `Bressan mixing conjecture 2026 solved arxiv`; `Bressan mixing conjecture 2025 2026`. This is a literature search, not a proof that no solution exists.
