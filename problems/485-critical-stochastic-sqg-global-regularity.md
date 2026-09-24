# 485. Global regularity for critical SQG with state-dependent noise

**Area:** Stochastic PDEs; geophysical fluid dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

On $`\mathbb T^2`$, set $`\Lambda=(-\Delta)^{1/2}`$ and $`R^\perp=(-R_2,R_1)`$, with zero Fourier multiplier at frequency zero. Consider

```math
d\theta+[R^\perp\theta\cdot\nabla\theta+\Lambda\theta]dt
=\sum_{k=1}^K g_k(x,\theta)\,dW^k_t,\qquad\theta(0)=\theta_0,
```

in the Itô sense. The initial temperature $`\theta_0`$ is any deterministic smooth periodic function. The finite collection $`g_k`$ consists of smooth functions on $`\mathbb T^2\times\mathbb R`$, globally Lipschitz in their scalar argument uniformly in $`x`$, with bounded derivatives of positive order and bounded $`g_k(\cdot,0)`$. The $`W^k`$ are independent standard Brownian motions.

Does every such equation have a pathwise unique global adapted solution with paths in $`C([0,T];H^3(\mathbb T^2))`$ for every finite $`T`$, satisfying the integral equation in $`H^1`$? Equivalently, can its local $`H^3`$ solution blow up with positive probability? No smallness of the data or noise is imposed, and the $`g_k`$ need not be linear in $`\theta`$.

## Application

Critical SQG models surface temperature transport with borderline dissipative smoothing. The question tests whether that smoothing remains sufficient under nonlinear random forcing.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), equation (8.23), Theorem 8.22 and Remark 8.23. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. T. Liang and Y. Wang, *Sub-critical and critical stochastic quasi-geostrophic equations with infinite delay*, Discrete Contin. Dyn. Syst. B **26** (2021), 4697–4726, local pathwise theory at critical dissipation. [Article](https://doi.org/10.3934/dcdsb.2020309).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The survey explicitly leaves global existence and uniqueness at dissipation exponent $`\alpha=1/2`$ open; the statement selects smooth finite-dimensional Lipschitz noise to make the solution class concrete. Searches on 2026-09-22 checked critical stochastic SQG, nonlinear multiplicative forcing, and global regularity. Located results concern subcritical dissipation, local critical solutions, restricted noise, or modified SQG with Kraichnan transport noise; none settles the full class here. This is distinct from deterministic supercritical SQG already in the catalogue.
