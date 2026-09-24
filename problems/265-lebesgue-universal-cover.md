# 265 — The minimum-area universal cover of planar diameter-one sets

**Area:** Geometric optimization / universal containment

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`\mathcal U`$ be the class of compact convex sets $`K\subset\mathbb R^2`$ such that, for every nonempty compact set $`E\subset\mathbb R^2`$ with $`\mathop{\mathrm{diam}}\nolimits E\leq1`$, there exists a Euclidean isometry $`g`$ with $`g(E)\subseteq K`$. Reflections as well as rotations and translations are allowed.

Determine the exact value of

```math
a_{\mathrm{Leb}}=\inf_{K\in\mathcal U}\mathop{\mathrm{Area}}\nolimits(K)
```

and characterize the minimizing covers. The objects being covered are arbitrary diameter-bounded sets, not only curves with a prescribed length.

## Application

This is a universal packaging problem: one container must accommodate every planar object satisfying only a diameter specification.

## References

1. J. C. Baez, K. Bagdasaryan and P. Gibbs, *The Lebesgue universal covering problem* (2015), [Journal of Computational Geometry 6, 288–299](https://doi.org/10.20382/jocg.v6i1a12), §1. Classical formulation and improved construction.
2. P. Gibbs, *An Upper Bound for Lebesgue’s Covering Problem* (2018), [arXiv:1810.10089](https://arxiv.org/abs/1810.10089), abstract and main construction. Gives an upper bound of $`0.8440935944`$.
3. S. Zeng, *An exact hierarchy for Lebesgue’s universal covering constant and a certified 0.834 lower bound* (2026), [arXiv:2609.01284](https://arxiv.org/abs/2609.01284), abstract and main results. Reports a convergent hierarchy and a lower bound, rather than an exact value.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 2026 preprint improves the claimed lower bound to $`0.834`$ while leaving a gap to the known upper construction. “Exact hierarchy” does not mean an exact evaluation of the constant. Searches included “Lebesgue universal covering solved 2026”, “universal covering minimum area September 2026”, and the Zeng and Gibbs titles. No exact value or proven minimizing shape was located.
