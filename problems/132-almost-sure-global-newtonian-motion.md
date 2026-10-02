# 132 — Almost-everywhere global existence for Newtonian gravitation

**Area:** Celestial mechanics / singular dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix $`N\ge5`$ positive masses $`m_i`$. Let

```math
\mathcal P=\{(q_1,\ldots,q_N,v_1,\ldots,v_N)\in\mathbb R^{6N}:q_i\ne q_j\ (i\ne j)\}.
```

For each initial state in $`\mathcal P`$, solve $`\dot q_i=v_i`$ and

```math
\dot v_i=\sum_{j\ne i}m_j\frac{q_j-q_i}{|q_j-q_i|^3}
```

on its maximal classical forward interval $`[0,T_{\max})`$. Is the set of initial states with $`T_{\max}<\infty`$ of $`6N`$-dimensional Lebesgue measure zero?

Both collisions and finite-time noncollision singularities count as failures of global classical existence.

## Application

The question asks whether finite-time breakdown in ideal point-mass gravitational simulations is exceptional in the measure-theoretic sense, despite the existence of specially constructed singular motions.

## References

1. J. Xue, *On the Painlevé conjecture*, in *Current Developments in Mathematics 2020* (published 2022), [chapter, pp. 157–206](https://doi.org/10.4310/CDM.2020.v2020.n1.a4), §1.1, Conjecture 1.1. States the almost-everywhere global-existence question.
2. J. Xue, *Noncollision singularities in a planar four-body problem* (2020), [Acta Mathematica 224, 253–388](https://doi.org/10.4310/ACTA.2020.v224.n2.a2), main theorem. Establishes existence of exceptional singular trajectories, rather than their positive measure.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The chapter reports measure-zero results for collision-producing initial conditions and almost-everywhere global existence for at most four bodies. Constructing noncollision singularities does not settle the measure of their initial-data set for $`N\ge5`$. Searches included “Newtonian n body almost all global existence measure zero 2025 2026” and “noncollision singularities initial conditions measure zero five body”. No later theorem covering the stated quantifiers was located.
