# 089. Gaussian-energy optimality of the triangular lattice among periodic configurations

**Area:** Crystallization and energy minimization

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`\Lambda_\triangle\subset\mathbb R^2`$ be the triangular lattice scaled to covolume one. For any integer $`N\ge1`$, a lattice $`L`$ of covolume $`N`$, and points $`a_1,\ldots,a_N`$ distinct modulo $`L`$, set $`P=\bigcup_i(a_i+L)`$. Prove or disprove, for every $`\alpha>0`$,

```math
\frac1N\sum_{i,j=1}^{N}\ \sum_{\substack{v\in L\\(i,j,v)\ne(i,i,0)}}
e^{-\pi\alpha|a_i-a_j-v|^2}
\ \ge\
\sum_{v\in\Lambda_\triangle\setminus\{0\}}e^{-\pi\alpha|v|^2}.
```

In the left sum, omit only the self-interaction $`j=i,v=0`$ for each $`i`$. All configurations have point density one. This is the periodic Gaussian formulation of triangular-lattice universal optimality.

## Application

This is a crystallization question for particles with repulsive Gaussian interactions: at fixed density, can any periodic arrangement have lower energy than the triangular crystal? Because positive mixtures of Gaussian kernels generate a broad family of completely monotone pair energies, a proof would identify the same preferred crystal for many such interaction models.

## References

- [Henry Cohn and Abhinav Kumar, *Universally optimal distribution of points on spheres* (Journal of the AMS, 2007), Euclidean universal-optimality conjecture](https://arxiv.org/abs/math/0607446).
- [Mircea Petrache and Sylvia Serfaty, *Crystallization for Coulomb and Riesz Interactions as a Consequence of the Cohn-Kumar Conjecture* (2019), opening discussion](https://arxiv.org/abs/1908.09714).

## Status review

**Known cases:** The triangular lattice minimizes the Gaussian energy among lattices, the one-point-per-cell case of the displayed periodic formulation.

**Remaining target:** The same lower bound for arbitrary periodic configurations with any number of points per cell.

**Literature check:** Open in cited literature; no later resolution located.

The two-dimensional conjecture remains separate from the proven universal optimality of E₈ and the Leech lattice in dimensions eight and 24. The triangular lattice is known to minimize among lattices; allowing N>1 offsets is the unresolved extension here. The 2026 status search found no resolution for arbitrary periodic configurations.

Status-search topics (2026-09-08): `triangular lattice universal optimality 2026`; `Coulomb triangular lattice crystallization conjecture 2026`. This is a literature search, not a proof that no solution exists.
