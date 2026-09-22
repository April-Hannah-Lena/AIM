# 168. The maximal heat-transfer exponent at finite Prandtl number

**Area:** Buoyant convection and heat transfer

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $\Omega=(\mathbb R/\mathbb Z)\times(0,1)$, take Prandtl number one and consider the two-dimensional Boussinesq system

$$
\partial_tu+u\cdot\nabla u+\nabla p=\Delta u+\mathrm{Ra}\,T e_2,\quad\operatorname{div}u=0,\quad\partial_tT+u\cdot\nabla T=\Delta T.
$$

Impose horizontal periodicity, $u=0$ on the walls, $T(x,0)=1$ and $T(x,1)=0$. For each $\mathrm{Ra}>0$, let $\mathcal N(\mathrm{Ra})$ be the supremum, over smooth compatible initial data with $0\le T_0\le1$, of

$$
\limsup_{\tau\to\infty}\frac1\tau\int_0^\tau\int_\Omega|\nabla T(t,x)|^2\,dx\,dt.
$$

Determine the number $\beta_*:=\limsup_{\mathrm{Ra}\to\infty}\log\mathcal N(\mathrm{Ra})/\log\mathrm{Ra}$. This asks for the optimal power-law exponent for actual solutions with these fixed boundary conditions and finite Prandtl number.

## Application

The exponent measures the greatest possible enhancement of heat transfer by buoyancy as the imposed temperature difference grows.

## References

1. Zijing Ding and Rich R. Kerswell, *Exhausting the background approach for bounding the heat transport in Rayleigh–Bénard convection*, Journal of Fluid Mechanics 889 (2020), A33. [Paper](https://arxiv.org/abs/1906.03376). Introduction and concluding discussion describe the unresolved optimal scaling and the limitations of standard upper-bound methods.

2. Zijing Ding, Baole Wen and Hui Li, *Optimal heat transport at the edge of energy stability* (2026). [Paper](https://arxiv.org/html/2606.14138v1). Introduction and mathematical formulation distinguish proposed extremal states from rigorous bounds on full buoyant dynamics.

3. Sagun Chanillo and Andrea Malchiodi, *Sharp bounds on the Nusselt number in Rayleigh–Bénard convection and a bilinear estimate by Coifman–Meyer*, Inventiones Mathematicae 240 (2025), 633–660. [Article](https://doi.org/10.1007/s00222-025-01326-z). Resolves a logarithmic gap for the infinite-Prandtl model.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This makes the published optimal-scaling question concrete at fixed Prandtl number and aspect ratio. Searches for “finite Prandtl Nusselt optimal exponent open 2026” and “Ding Wen Li optimal heat transport 2026” located model predictions rather than a matching upper and lower exponent for these solutions. The 2025 sharp infinite-Prandtl result omits fluid inertia and does not determine this exponent.
