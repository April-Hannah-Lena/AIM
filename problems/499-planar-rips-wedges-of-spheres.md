# 499. Planar Rips complexes as wedges of spheres

**Area:** Applied topology and geometric complexes

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-23

## Problem statement

Let $`X`$ be a nonempty finite subset of $`\mathbb R^2`$ with its Euclidean metric, and let $`r>0`$. Define the Vietoris–Rips complex

```math
K=\mathop{\mathrm{VR}}\nolimits_{<}(X;r)=\{\sigma\subseteq X:\mathop{\mathrm{diam}}\nolimits(\sigma)<r\}.
```

Assume that $`K`$ is connected. Must its geometric realization be homotopy equivalent to a finite wedge of spheres,

```math
|K|\simeq\bigvee_{j=1}^{m}S^{d_j},\qquad d_j\ge1,
```

where $`m=0`$ denotes a point? Equivalently, ask this separately for each connected component of an arbitrary finite planar Rips complex.

This is the wedge-of-spheres question in Problem 7.3 of [1], retained as Conjecture 1.2 of [2]. The ambient point set is planar, but the simplicial complex can have arbitrarily high dimension.

## Application

Rips complexes encode pairwise proximity in point clouds and sensor networks. Classifying their possible homotopy types would clarify which topological features can arise from planar proximity data, beyond the information supplied by homology alone.

## References

1. M. Adamaszek, F. Frick and A. Vakili, [On Homotopy Types of Euclidean Rips Complexes](https://doi.org/10.1007/s00454-017-9916-5), Discrete & Computational Geometry **58** (2017), 526–542; [author preprint](https://arxiv.org/abs/1602.04131), §7, Problem 7.3.
2. V. Sipani and R. Kasilingam, [On the classification of planar-Rips complexes and their corresponding unit disk graphs](https://doi.org/10.4310/HHA.2026.v28.n3.a1), Homology, Homotopy and Applications **28**(3) (2026), 1–30. Conjecture 1.2 and Theorems A–C, pp.2–3; [author preprint](https://arxiv.org/abs/2406.01082).

## Status review

**Known cases:** The 2026 paper [2] classifies planar Rips pseudomanifolds of dimension at least two as cross-polytopal spheres. It also proves a wedge decomposition for two-dimensional pure closed planar Rips complexes.

**Remaining target:** Arbitrary finite connected planar Rips complexes, without purity, closedness or pseudomanifold assumptions.

The published July 2026 version of [2] explicitly calls the conjecture open. The 23 September 2026 search found no subsequent matching proof or counterexample announcement.
