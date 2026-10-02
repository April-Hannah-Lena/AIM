# 144. Energy conservation at the exact Onsager Hölder exponent

**Area:** Fluid mechanics and turbulence

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`u\in C([0,T];C^{1/3}(\mathbb T^3;\mathbb R^3))`$ solve, in distributions,

```math
\partial_tu+\nabla\!\cdot(u\otimes u)+\nabla p=0,\qquad \nabla\!\cdot u=0.
```

Here $`C^{1/3}`$ means that $`\sup_{x\ne y}|u(x)-u(y)|/d(x,y)^{1/3}`$ is finite. Must $`E(t)=\tfrac12\int_{\mathbb T^3}|u(t,x)|^2\,dx`$ be constant? Equivalently, decide whether an energy-changing weak Euler solution exists in this exact class.

## Application

Turbulence models use transfer toward finer spatial scales to explain energy loss that persists at very small viscosity. This endpoint question determines whether an ideal incompressible flow with exactly one-third Hölder regularity can change its total kinetic energy, fixing the conservation threshold at the critical roughness.

## References

1. Philip Isett, *On the endpoint regularity in Onsager’s conjecture*, Analysis & PDE 17 (2024), 2123–2159, introduction and main construction. [Publisher PDF](https://msp.org/apde/2024/17-6/apde-v17-n6-p09-s.pdf). Explicit endpoint question and results approaching it.

2. Alexey Cheskidov, Peter Constantin, Susan Friedlander and Roman Shvydkoy, *Energy conservation and Onsager’s conjecture for the Euler equations*, Nonlinearity 21 (2008), 1233–1252, energy-conservation theorem. [Paper](https://arxiv.org/abs/0704.0759). Conservation in the smaller critical Besov class with vanishing high-frequency tail.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Isett’s 2024 article explicitly leaves the endpoint open. The subcritical Onsager conjecture is already solved. Searches for “Onsager endpoint C 1/3 open problem 2026” and “Onsager energy conservation Cheskidov Constantin Friedlander Shvydkoy” found no resolution of the stated exact Hölder class. The vanishing small-scale increment condition used in known conservation theorems is stronger than the assumption here.
