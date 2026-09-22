# 147 — Global null control of a heat equation with cubic growth

**Area:** Nonlinear PDE control / reaction-diffusion

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^d$ be a bounded connected smooth domain, and let $\omega\Subset\Omega$ be a nonempty open actuator region. For every $T>0$ and every $y_0\in L^\infty(\Omega)$, does there exist $u\in L^\infty((0,T)\times\omega)$ such that

$$
\partial_ty-\Delta y=y^3+\mathbf1_\omega u,\qquad
y|_{\partial\Omega}=0,\qquad y(0,\cdot)=y_0,
$$

has a bounded weak solution throughout $[0,T]$ satisfying $y(T,\cdot)=0$?

The control amplitude may depend on $y_0$ and $T$; no fixed amplitude constraint is imposed. Global refers to arbitrary initial data, and successful control must prevent finite-time blow-up before reaching zero.

## Application

This is a minimal model of localized intervention in a self-amplifying thermal or chemical process. The question asks whether diffusion and an internal actuator can suppress every initial state within any prescribed time.

## References

1. J.-M. Coron, *Control and Nonlinearity* (AMS, 2007), [Mathematical Surveys and Monographs 136](https://doi.org/10.1090/surv/136), Open Problems 7.14–7.15. Book source of the global superlinear heat-control questions.
2. K. Le Balc'h and T. Takahashi, *Null-controllability of cascade reaction-diffusion systems with odd coupling terms* (2024 volume; published 2025), [Annales mathématiques Blaise Pascal 31, 239–271](https://doi.org/10.5802/ambp.430), §1.1, remarks following Theorem 1.1. Explicitly states that global null controllability of the scalar odd-power equation remains unresolved and points to Coron's problems.

## Status review

**Known cases:** Local null controllability is established for sufficiently small initial data.

**Remaining target:** Null controllability in every prescribed positive time for arbitrary bounded initial data, while preventing blow-up.

**Literature check:** Open in cited literature; no later resolution located.

The recent paper proves local null controllability for small data; it does not remove the size restriction for the scalar growing odd-power reaction. The sign $+y^3$ matters: this is not an absorbing reaction. Searches included “global null controllability cubic heat equation 2025 2026”, “Coron Open Problems 7.14 7.15” and “odd power heat equation arbitrary initial data control”. No general global result was located.
