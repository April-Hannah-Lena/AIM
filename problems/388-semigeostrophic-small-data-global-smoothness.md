# 388. Global smooth evolution of small semigeostrophic perturbations

**Area:** Geophysical PDEs / optimal transport

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

On $`\mathbb T^2=\mathbb R^2/\mathbb Z^2`$, consider

```math
\partial_t\rho+\nabla\!\cdot(\rho U)=0,\qquad U=J(x-\nabla P^*),\qquad \det D^2P^*=\rho,
```

where $`J(a,b)=(-b,a)`$, $`P^*(t,x)-|x|^2/2`$ is periodic with mean zero, and $`P^*(t,\cdot)`$ is convex. Does there exist an integer $`k\ge2`$ and $`\varepsilon>0`$ such that every $`\rho_0\in C^\infty(\mathbb T^2)`$ with $`\rho_0>0`$, $`\int\rho_0=1`$ and $`\|\rho_0-1\|_{C^k}<\varepsilon`$ produces a smooth solution for all $`t\ge0`$? Smoothness is required on every finite time interval, with $`D^2P^*`$ positive definite; no uniform-in-time bound is required.

## Application

The semigeostrophic model describes slowly varying, rapidly rotating atmospheric motion. The question asks whether sufficiently small smooth weather perturbations can form fronts or lose smoothness in finite time.

## References

1. G. Loeper, *A Fully Nonlinear Version of the Incompressible Euler Equations: The Semigeostrophic System*, SIAM Journal on Mathematical Analysis 38 (2006), 795–823, local regularity and uniqueness results. [DOI](https://doi.org/10.1137/050629070).
2. G. De Philippis and A. Figalli, *The Monge–Ampère Equation and Its Link to Optimal Transportation*, Bulletin of the AMS 51 (2014), 527–580, §2.5 and §5.2(3). [Publisher PDF](https://www.ams.org/journals/bull/2014-51-04/S0273-0979-2014-01459-4/S0273-0979-2014-01459-4.pdf).
3. A. Figalli, *Global existence for the semigeostrophic equations*, concluding open questions, item 2. [Author manuscript](https://cvgmt.sns.it/media/doc/paper/2665/MA_semigeo.pdf).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The concluding question in Figalli’s survey explicitly singles out initial densities sufficiently close to one in a strong norm. The formulation above makes that qualification existential in the differentiability order. Searches through 22 September 2026 covered small-amplitude semigeostrophic global regularity, Loeper and Silini, and the semigeostrophic–Euler limit. Silini’s SIAM JMA 55 (2023), 6554–6579 result is local in time; lifespan lower bounds and global weak-solution constructions do not establish the requested global smooth flow.
