# 375. Global smoothness of the one-dimensional surface-growth equation

**Area:** Epitaxial growth; fourth-order evolution equations

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For every real-valued $`h_0\in C^\infty(\mathbb T)`$ of zero mean, where $`\mathbb T=\mathbb R/(2\pi\mathbb Z)`$, does the maximal classical solution of

```math
\partial_t h+\partial_x^4h+\partial_x^2\big((\partial_xh)^2\big)=0,\qquad h(0,x)=h_0(x),
```

exist for all $`t\ge0`$? Equivalently, is $`\sup_{0\le t\le T}\|h(t)\|_{H^m(\mathbb T)}<\infty`$ for every finite $`T`$ and integer $`m\ge0`$? There is no smallness assumption on $`h_0`$.

## Application

The height field describes a growing crystal surface. A resolution would establish whether the nonlinear surface current can overwhelm fourth-order smoothing and create an infinite slope or a sharper singularity.

## References

1. D. Blömker and M. Romito, [*Regularity and blow-up in a surface growth model*](https://arxiv.org/abs/0902.1409), Dynamics of Partial Differential Equations 6 (2009), 227–252, equation (1.1), §1.1 and §§3–4; DOI [10.4310/DPDE.2009.v6.n3.a2](https://doi.org/10.4310/DPDE.2009.v6.n3.a2).
2. D. Blömker, C. Nolde and J. C. Robinson, [*Rigorous numerical verification of uniqueness and smoothness in a surface growth model*](https://arxiv.org/abs/1311.2205), Journal of Mathematical Analysis and Applications 429 (2015), 311–325, verification theorem.
3. Y. Cheng, Z. Li and X. Wei, [*Regularity criteria for the surface growth model with a forcing term*](https://arxiv.org/abs/2603.12714), preprint (2026), §1 and main regularity criteria.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using the displayed deterministic surface-growth equation, global regularity and finite-time blowup. The 2009 paper proves small-data regularity and conditional continuation, and bounds possible singular times; these do not rule out singularities for arbitrary data. The 2015 work certifies specified computations. The March 2026 results give additional regularity criteria, not unconditional smoothness. Large-time decay of weak solutions also leaves possible finite-time singularities unresolved. No proof or counterexample for the stated arbitrary-data assertion was located.
