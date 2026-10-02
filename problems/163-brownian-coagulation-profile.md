# 163. Uniqueness of the Brownian coagulation similarity profile

**Area:** Aerosol kinetics and aggregation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For cluster masses $`x,y>0`$, set

```math
K(x,y)=2+(x/y)^{1/3}+(y/x)^{1/3}.
```

Is there exactly one nonnegative profile $`F`$ with $`\int_0^\infty xF(x)\,dx=1`$, $`\int_0^\infty(1+x+x^{-1/3})F(x)\,dx<\infty`$, satisfying for every $`\varphi\in C_c^\infty(0,\infty)`$

```math
\int_0^\infty F(x)[x\varphi'(x)-\varphi(x)]\,dx
=\frac12\int_0^\infty\!\int_0^\infty K(x,y)F(x)F(y)[\varphi(x+y)-\varphi(x)-\varphi(y)]\,dx\,dy?
```

This is the self-similar-profile equation for $`f(t,x)=t^{-2}F(x/t)`$ in Smoluchowski’s coagulation equation. Equality of profiles means equality almost everywhere.

## Application

A unique normalized profile would identify the universal particle-size distribution predicted for Brownian aerosol aggregation.

## References

1. Miguel Escobedo, Stéphane Mischler and María Rodríguez Ricard, *On self-similarity and stationary problem for fragmentation and coagulation models*, Annales de l’Institut Henri Poincaré C 22 (2005), 99–125. [Article](https://ems.press/journals/aihpc/articles/4076412). Self-similar existence theory for coagulation kernels.

2. Barbara Niethammer, Sebastian Throm and Juan J. L. Velázquez, *A revised proof of uniqueness of self-similar profiles to Smoluchowski’s coagulation equation for kernels close to constant* (2015 preprint, revised 2017). [Version 3](https://arxiv.org/abs/1510.03361v3). Introduction and main theorem explain the general uniqueness problem and prove a small-perturbation result.

3. José A. Cañizo and Sebastian Throm, *The scaling hypothesis for Smoluchowski’s coagulation equation with bounded perturbations of the constant kernel*, Journal of Differential Equations 270 (2021), 285–342. [Article](https://doi.org/10.1016/j.jde.2020.07.036). Later perturbative uniqueness and attraction result.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searches for “Brownian coagulation kernel self similar profiles uniqueness 2025 2026” and “Niethammer Throm Brownian uniqueness” located perturbative results, not uniqueness for this full Brownian kernel. The coefficient of its singular ratio terms is fixed at one; a theorem requiring sufficiently small perturbations of a constant does not apply. This concerns finite-mass profiles, not uniqueness of time-dependent solutions or infinite-mass fat-tailed profiles.
