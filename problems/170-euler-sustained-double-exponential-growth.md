# 170. Sustained double-exponential gradient growth on the Euler torus

**Area:** Fluid mixing and creation of small scales

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For mean-zero $\omega_0\in C^\infty(\mathbb T^2)$, let $\omega$ solve

$$
\partial_t\omega+u\cdot\nabla\omega=0,\qquad u=\nabla^\perp\Delta^{-1}\omega,
$$

where $\nabla^\perp=(-\partial_2,\partial_1)$ and $\Delta^{-1}$ is the inverse on mean-zero periodic functions. Does there exist one such initial datum, with $c>0$ and $t_0<\infty$, for which

$$
\|\nabla\omega(t)\|_{L^\infty}\ge\exp(\exp(ct))\qquad\text{for every }t\ge t_0?
$$

The initial datum must be fixed for the entire infinite time interval. The torus has no solid boundary.

## Application

Vorticity amplitude stays fixed along particles, so growth of its gradient measures the creation of small spatial scales in ideal two-dimensional mixing.

## References

1. Sergey A. Denisov, *Double exponential growth of the vorticity gradient for the two-dimensional Euler equation* (2012). [Paper](https://arxiv.org/abs/1201.1771). Main theorem obtains prescribed finite durations with initial data depending on the duration.

2. In-Jee Jeong, Yao Yao and Tao Zhou, *Superlinear gradient growth for 2D Euler equation without boundary* (2025). [Paper](https://arxiv.org/html/2507.15739v1). §1.1 reviews the gap between the double-exponential upper bound and known smooth-data lower growth; new results give robust superlinear growth.

3. Andrej Zlatoš, *Exponential growth of the vorticity gradient for the Euler equation on the torus*, Advances in Mathematics 268 (2015), 396–403. [Paper](https://arxiv.org/abs/1310.6128). Distinguishes infinite-time gradient growth with less smooth vorticity from smooth-data higher-derivative growth.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searches for “Euler torus double exponential vorticity gradient growth open 2026” and “Euler double exponential torus 2026 solved” located finite-duration torus constructions and boundary-assisted results on disks and half-planes. The 2025 smooth-data advance does not attain the displayed rate. Allowing a different datum for every desired observation time would weaken this question to a known result.
