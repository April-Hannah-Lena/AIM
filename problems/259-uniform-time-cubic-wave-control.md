# 259 — A data-independent time for global control of the defocusing cubic wave

**Area:** Nonlinear wave control / vibration suppression

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\Omega\subset\mathbb R^3$ be bounded and smooth, and let $\omega\subset\Omega$ be open. Assume the geometric control condition: for some $T_0<\infty$, every unit-speed generalized ray of the Dirichlet wave equation meets $\omega$ within time $T_0$.

Is there a time $T_*=T_*(\Omega,\omega)$ such that every two states in $H_0^1(\Omega)\times L^2(\Omega)$ can be joined in time $T_*$ by an energy-class solution of

$$
u_{tt}-\Delta u+u^3=\mathbf1_\omega f,\qquad u|_{\partial\Omega}=0,
$$

using $f\in L^2(\omega\times(0,T_*))$? Energy class means $(u,u_t)\in C([0,T_*];H_0^1\times L^2)$. The time may depend on the geometry but must be independent of the sizes of both endpoint states.

## Application

The question separates a geometric transport time from a potentially amplitude-dependent time needed to control a strongly nonlinear vibration.

## References

1. B. Dehman, G. Lebeau and E. Zuazua, *Stabilization and control for the subcritical semilinear wave equation* (2003), [Annales scientifiques de l’ENS 36, 525–551](https://doi.org/10.1016/S0012-9593(03)00021-1), Corollary 4 and subsequent discussion. Establishes global control with energy-dependent time and poses uniformity.
2. J.-M. Coron, J. Krieger and S. Xiang, *Wave maps from circle to Riemannian manifold: global controllability is equivalent to homotopy* (2025), [arXiv:2509.12779](https://arxiv.org/abs/2509.12779), introduction, “Open Problem (Dehman–Lebeau–Zuazua)”. Explicitly restates the cubic-wave question and distinguishes its geometric-map partial result.
3. C. Laurent and C. Loyola, *Global propagation of analyticity and unique continuation for semilinear waves* (2026), [JEP 13, 1323–1387](https://doi.org/10.5802/jep.348), introduction and observability theorem. Gives optimal geometric-time observability with constants depending on the data bound.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2009 Dehman–Lebeau result on “uniform time” does not remove all low-frequency data dependence. The 2025 wave-map theorem concerns a different constrained equation; the 2026 observability result alone does not yield the displayed global endpoint control in a data-independent time. Searches included “uniform time global cubic wave controllability 2026”, “Dehman Lebeau Zuazua open problem”, and the Laurent–Loyola title. No full resolution was located.
