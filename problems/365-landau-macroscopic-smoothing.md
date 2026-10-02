# 365. Landau–Coulomb smoothing controlled only by macroscopic quantities

**Area:** Plasma kinetics; quantitative regularization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Consider nonnegative smooth rapidly decaying solutions on $`[0,T]\times\mathbb R^3`$ of

```math
\partial_tf=\nabla_v\cdot(A[f]\nabla_vf-f\nabla_va[f]),\quad A[f]\,(v)=\frac1{8\pi}\int_{\mathbb R^3}\frac{I-\widehat{v-w}\otimes\widehat{v-w}}{|v-w|}f(w)\,dw,\quad a[f]\,(v)=\frac1{4\pi}\int_{\mathbb R^3}\frac{f(w)}{|v-w|}\,dw,
```

with $`\widehat z=z/|z|`$. Normalize $`\int f\,dv=1`$, $`\int vf\,dv=0`$ and $`\int|v|^2f\,dv=3`$. For every $`H\in\mathbb R`$ and $`0<\tau<T`$, is there a finite $`C(H,\tau,T)`$ such that

```math
\sup_{\tau\le t\le T}\|f(t)\|_{L^\infty_v}\le C(H,\tau,T)\quad\text{whenever}\quad\int f(0,v)\log f(0,v)\,dv\le H?
```

The constant must be independent of all initial higher moments, Fisher information, pointwise bounds and derivative norms. The question asks for a bound, without prescribing a conjectural sharp time exponent.

## Application

A bound in terms of mass, temperature and entropy would connect measurable plasma quantities to pointwise control of the collision distribution and provide estimates that survive approximation by rough data.

## References

1. W. Golding, M. Gualdani and A. Loher, [*Global Smooth Solutions to the Landau–Coulomb Equation in $`L^{3/2}`$*](https://doi.org/10.1007/s00205-025-02107-x), Archive for Rational Mechanics and Analysis 249 (2025), article 34, §1, first item under “Open Problems.”
2. M. Gualdani and N. Guillen, [*On $`A_p`$ weights and the Landau equation*](https://arxiv.org/abs/1708.00067), Analysis & PDE 12 (2019), 77–170, conditional Coulomb regularization results.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using Landau–Coulomb mass-energy-entropy smoothing and quantitative $`L^\infty`$ estimates. The 2025 primary paper explicitly leaves this estimate open after its global smooth-existence theorem: its bounds retain stronger information about the initial distribution. The 2019 estimates are unconditional for moderately soft potentials but conditional in the Coulomb case. Later global-existence and numerical entropy-stability papers located in the search do not remove these quantitative dependencies. No matching estimate or counterexample was located.
