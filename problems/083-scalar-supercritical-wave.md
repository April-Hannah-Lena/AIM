# 083. Global smoothness for the real scalar defocusing septic wave equation

**Area:** Nonlinear waves

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

## Problem statement

For arbitrary real-valued $(u_0,u_1)\in C_c^\infty(\mathbb R^3)\times C_c^\infty(\mathbb R^3)$, does
$$
\partial_t^2u-\Delta u+u^7=0,\qquad
u(0,x)=u_0(x),\quad \partial_tu(0,x)=u_1(x)
$$
have a smooth solution on every finite time interval? Alternatively, exhibit admissible data with finite-time breakdown. No symmetry or smallness hypothesis is permitted. The conserved energy is
$$
E(u)=\int_{\mathbb R^3}\left(\tfrac12|\partial_tu|^2+
\tfrac12|\nabla u|^2+\tfrac18|u|^8\right)\,dx,
$$
but its scaling is supercritical for this equation.

## Applied significance

This isolates the effect of a positive nonlinear restoring force on wave concentration, a basic issue in nonlinear field and wave models.

## References

- [Feng Shao, Dongyi Wei and Zhifei Zhang, *On blow-up for the supercritical defocusing nonlinear wave equation* (Forum of Mathematics, Pi, 2025), introduction and distinction between real scalar and complex-valued equations](https://doi.org/10.1017/fmp.2025.7).
- [Terence Tao, *Nonlinear dispersive equations: local and global analysis* (2006), §3, local/global framework](https://math.ucla.edu/~tao/preprints/chapter.pdf).

## Status review

The 2025 paper explicitly leaves scalar defocusing blowup open while constructing complex-valued blowup in other dimensions/exponents. Later search results on complex-valued septic waves in four spatial dimensions do not settle this real-valued three-dimensional formulation. The older book's broad discussion must be read with those later counterexamples in mind.

Searches run on 2026-09-08: `scalar defocusing wave open 2025 blowup`; `site.arxiv.org defocusing supercritical open problem 2025 2026`. This is a literature search, not a proof that no solution exists.
