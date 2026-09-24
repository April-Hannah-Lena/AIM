# 130 — An SRB measure for the classical Hénon parameters

**Area:** Dissipative dynamics / chaotic statistics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Consider the fixed polynomial diffeomorphism

```math
H(x,y)=(1-1.4x^2+y,\ 0.3x).
```

Does $`H`$ admit a compactly supported ergodic invariant probability measure $`\mu`$ with a positive largest Lyapunov exponent and absolutely continuous conditional measures on its local unstable manifolds?

These conditions define the nonuniformly hyperbolic SRB measure sought here. In particular, such a measure describes empirical time averages for a set of initial conditions of positive planar Lebesgue measure; an invariant measure carried only by a repelling periodic orbit does not qualify.

## Application

This is a standard numerical model of a chaotic attractor. An SRB measure would put the observed long-run statistical behavior at its original parameter values on a rigorous basis.

## References

1. P. Berger et al. (collective pseudonym Julia Xénelkis de Hénon), *Hénon maps: a list of open problems* (2024), [Arnold Mathematical Journal, author text](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html), §1 and §2.1. States the original SRB conjecture and distinguishes it from parameter-set existence theorems.
2. M. Hénon, *A two-dimensional mapping with a strange attractor* (1976), [Communications in Mathematical Physics 50, 69–77](https://doi.org/10.1007/BF01608556), numerical model and original parameter choice.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Existence for a positive-measure set of parameters in sufficiently dissipative Hénon families does not certify the specific pair $`(1.4,0.3)`$. The 2024 collection retains the original conjecture. Searches included “Hénon 1.4 0.3 SRB measure proof 2025 2026” and “classical Hénon conjecture resolved”. Numerical Lyapunov exponents and theorems about other parameter values were not counted as resolutions.
