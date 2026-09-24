# 553. Simplices maximize the isotropic constant

**Area:** Geometric probability and covariance bounds

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`K\subset\mathbb R^n`$ be a compact convex set with nonempty interior, and let $`X`$ be uniformly distributed on $`K`$. Write

```math
c_K=\mathbb E X,\qquad A_K=\mathbb E[(X-c_K)(X-c_K)^T],\qquad L_K=\left(\frac{\det A_K}{\mathop{\mathrm{vol}}\nolimits_n(K)^2}\right)^{1/(2n)}.
```

The quantity $`L_K`$ is invariant under invertible affine transformations. For every $`n\ge1`$ and every such $`K`$, is

```math
L_K\le L_{\Delta_n}=\frac{(n!)^{1/n}}{(n+1)^{(n+1)/(2n)}\sqrt{n+2}},
```

where $`\Delta_n`$ is any nondegenerate $`n`$-simplex?

This is the strong isotropic constant conjecture, stated in [1, equation (1.2)]. The target is the displayed sharp inequality. No additional uniqueness or stability assertion is imposed. Equivalently, it asks for the sharp upper bound

```math
\det A_K\le \frac{(n!)^2}{(n+1)^{n+1}(n+2)^n}\mathop{\mathrm{vol}}\nolimits_n(K)^2.
```

## Application

For a uniform distribution on a convex region, the covariance determinant measures the squared volume scale of its covariance ellipsoid. The conjecture would bound that spread sharply in terms of the region's volume, independently of its affine coordinates. It provides an extremal benchmark for covariance normalization and geometric probability, both used in the analysis of sampling from convex sets.

## References

1. C. Kipp, [Shadow Systems, Decomposability and Isotropic Constants](https://doi.org/10.1007/s00454-026-00829-7), Discrete & Computational Geometry (2026), §1, equations (1.1)–(1.2) and Theorem 1.2; [revised preprint](https://arxiv.org/abs/2411.08722v2).
2. B. Klartag and J. Lehec, [Affirmative Resolution of Bourgain's Slicing Problem using Guan's Bound](https://arxiv.org/abs/2412.15044), for the dimension-independent bound that settles the weaker slicing problem.
3. L. Rademacher, [A simplicial polytope that maximizes the isotropic constant must be a simplex](https://doi.org/10.1112/S0025579315000133), Mathematika **62** (2016), 307–320; [preprint](https://arxiv.org/abs/1404.5662).

## Status review

**Known cases:** The inequality holds in dimension one and in dimension two; [1, §1] attributes the planar result to Campi, Colesanti and Gronchi. There are also structural restrictions on possible higher-dimensional maximizers: [3] treats simplicial polytopes, and [1, Theorem 1.2] records the stronger conclusion that a polytopal local maximizer with a simplicial vertex must be a simplex. These statements do not show that every maximizer has such a vertex.

**Remaining target:** Prove the sharp inequality for arbitrary convex bodies in every dimension $`n\ge3`$, or exhibit a counterexample. The universal, unspecified constant obtained in the solution of Bourgain's slicing problem does not identify the dimension-specific simplex value. The 2026 source [1] explicitly distinguishes the two questions after discussing that solution.

The literature and announcement checks found no matching resolution through the date above. They included live arXiv version records, 2025–2026 follow-ups, GitHub- and Zenodo-indexed searches, and native Palomar queries. Native Zenodo access returned HTTP 403. Related catalogue problems on KLS, Mahler volume products and illumination have different targets.
