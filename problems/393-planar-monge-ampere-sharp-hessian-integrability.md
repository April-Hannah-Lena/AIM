# 393. Sharp weak integrability of planar Monge–Ampère Hessians

**Area:** Nonlinear elliptic PDEs / optimal transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $0<\lambda<1$, let $\Omega\subset\mathbb R^2$ be bounded and convex, and let $u$ be a convex Alexandrov solution with
$$\lambda\le\det D^2u\le\lambda^{-1}\quad\text{in }\Omega.$$
Here the inequalities mean $\lambda|E|\le|\partial u(E)|\le\lambda^{-1}|E|$ for every Borel $E\subset\Omega$. Is the distributional Hessian represented by a matrix field satisfying, for every $\Omega'\Subset\Omega$,
$$\sup_{s>0}s^{p_\lambda}\bigl|\{x\in\Omega':|D^2u(x)|>s\}\bigr|<\infty,\qquad p_\lambda=\frac{1+\lambda^2}{1-\lambda^2}?$$
This is the conjectured endpoint weak-$L^{p_\lambda}$ estimate, not merely integrability with some unspecified exponent larger than one.

## Application

Hessian bounds control distortion and sensitivity of transport maps used in mesh adaptation and mass redistribution. The conjecture identifies how sharply that distortion can concentrate when only density ratios are controlled.

## References

1. G. De Philippis and A. Figalli, *The Monge–Ampère Equation and Its Link to Optimal Transportation*, Bulletin of the AMS 51 (2014), 527–580, §5.2(2). [Publisher PDF](https://www.ams.org/journals/bull/2014-51-04/S0273-0979-2014-01459-4/S0273-0979-2014-01459-4.pdf).
2. G. De Philippis, A. Figalli and O. Savin, *A note on interior $W^{2,1+ε}$ estimates for the Monge–Ampère equation*, Mathematische Annalen 357 (2013), 11–22, Theorem 1.1. [DOI](https://doi.org/10.1007/s00208-012-0895-9); [preprint](https://arxiv.org/abs/1202.5566).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The survey explicitly proposes this exponent using planar quasiconformal theory. Searches through 22 September 2026 covered sharp planar Hessian integrability, the stated exponent, and subsequent work by De Philippis, Figalli, Savin and Mooney. Higher integrability with a non-sharp positive epsilon is established; the upper-bound-only degenerate problem has counterexamples, but those remove the positive lower bound essential here. No endpoint resolution was located.
