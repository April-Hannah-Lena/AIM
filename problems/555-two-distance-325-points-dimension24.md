# 555. A 325-point two-distance set in dimension 24

**Area:** Computational geometry and Euclidean distance matrices

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For a finite set $`X\subset\mathbb R^d`$, define its set of nonzero pairwise distances by

```math
D(X)=\{\|x-y\|_2:x,y\in X,\ x\ne y\}.
```

Call $`X`$ a two-distance set when $`|D(X)|=2`$.

Does there exist a set $`X\subset\mathbb R^{24}`$ with

```math
|X|=325\qquad\text{and}\qquad |D(X)|=2?
```

The two distances are not prescribed, and the points need not lie on a sphere. The target is an exact construction or a proof of nonexistence. This is the final question in §3 of [1].

## Application

Two-distance sets give Euclidean distance matrices with only two off-diagonal values. Their existence tests the interaction between combinatorial patterns, positive semidefiniteness and low embedding dimension. The proposed configuration would be an extremal benchmark for exact distance-geometry construction and certification methods.

## References

1. H.-J. Ge, J. Koolen and A. Munemasa, [A 2-Distance set with 277 Points in the Euclidean Space of Dimension 23](https://doi.org/10.1007/s00454-026-00843-9), Discrete & Computational Geometry (2026), §3; [corrected preprint, version 4](https://arxiv.org/abs/2504.18110v4), 3 August 2026.
2. W.-C. Chen and W.-H. Yu, [Bounds on two-distance sets in Euclidean space and Unit Sphere](https://arxiv.org/abs/2509.00858), version 1 (2025), §3, for bounds depending on the distance ratio.

## Status review

The general cardinality bound recorded in [1, §1] is $`|X|\le\binom{d+2}{2}`$, which equals $`325`$ at $`d=24`$. The midpoints of the edges of a regular $`24`$-simplex give $`\binom{25}{2}=300`$ points. Thus the question asks whether the general upper bound can be attained in this dimension.

The corrected Proposition 3 of [1] rules out obtaining $`325`$ points by extending the authors' particular $`277`$-point configuration into dimension $`24`$. It does not exclude other configurations. Bounds restricted to spherical sets do not answer the stated Euclidean question. The distance-dependent estimates in [2] likewise do not supply a strict bound below $`325`$ for all admissible distance ratios.

The August 2026 corrected preprint still explicitly poses the question. No matching resolution or announcement was located through the check date.
