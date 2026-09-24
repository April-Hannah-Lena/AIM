# 228. A length-independent mean energy bound for Kuramoto–Sivashinsky

**Area:** Combustion fronts and spatiotemporal chaos

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For each $L\geq1$, let $u$ solve the one-dimensional Kuramoto–Sivashinsky equation
$$u_t+uu_x+u_{xx}+u_{xxxx}=0$$
with spatial period $2\pi L$ and arbitrary smooth mean-zero initial data. Does there exist an absolute constant $C$, independent of $L$ and the initial data, such that
$$\limsup_{T\to\infty}\frac1{2\pi L T}\int_0^T\int_{-\pi L}^{\pi L}|u(x,t)|^2\,dx\,dt\leq C?$$
This concerns the full equation on intervals of unbounded length, with its coefficients fixed.

## Application

The equation models unstable flame fronts and serves as a model of distributed chaos. The bound would show that long-time energy grows at most in proportion to the size of the system.

## References

- David Goluskin and Giovanni Fantuzzi, [*Bounds on mean energy in the Kuramoto–Sivashinsky equation computed using semidefinite programming*](https://arxiv.org/abs/1802.08240) (2018 preprint; 2019 publication), abstract and §1: the conjectured bounded energy density and bounds for odd solutions on finite ranges of lengths.
- Felix Otto, [*Optimal bounds on the Kuramoto–Sivashinsky equation*](https://doi.org/10.1016/j.jfa.2009.01.034) (2009), main bounds: analytic estimates that still grow with the domain length.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “Kuramoto Sivashinsky mean energy uniform length bound”, “bounded energy density conjecture 2025 2026”, and follow-up auxiliary-functional bounds. Finite-length computations and estimates with a positive power or logarithmic dependence on length do not establish the uniform quantifier above.
