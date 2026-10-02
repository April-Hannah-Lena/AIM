# 164. A uniform limit-cycle bound for quadratic planar dynamics

**Area:** Nonlinear oscillations and dynamical systems

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Does there exist an integer $`H_2<\infty`$ such that every system

```math
\dot x=P(x,y),\qquad\dot y=Q(x,y),\qquad P,Q\in\mathbb R[x,y],\quad\max(\deg P,\deg Q)\le2,
```

has at most $`H_2`$ distinct limit cycles in $`\mathbb R^2`$? A limit cycle is an isolated periodic orbit, counted once as a geometric curve, without multiplicity. The bound must be independent of all polynomial coefficients.

## Application

Quadratic rate equations model interacting populations, chemical kinetics, and nonlinear oscillators. A uniform bound would limit the number of isolated oscillatory regimes such models can support.

## References

1. Armengol Gasull and Paulo Santana, *A note on Hilbert 16th Problem* (2024), §1. [Paper](https://arxiv.org/html/2407.13465v2). Explicitly states that finiteness of the quadratic Hilbert number is unknown.

2. Yulij Ilyashenko, *Centennial history of Hilbert’s 16th problem*, Bulletin of the American Mathematical Society 39 (2002), 301–354. [Article](https://doi.org/10.1090/S0273-0979-02-00946-1). Distinguishes individual finiteness from the uniform-bound problem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searches for “quadratic Hilbert sixteenth uniform bound solved 2026” and “Hilbert quadratic limit cycles 2025 2026” located new lower-bound and restricted-family results. The Gasull–Santana source explicitly leaves this finiteness question open. Individual polynomial systems are known to have finitely many limit cycles; that theorem supplies no coefficient-independent bound.
