# 592. Sharp vertex bounds for generalized triangulations in even dimensions

**Area:** Computational topology and face-number bounds

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`d\ge4`$ be even, and let $`T`$ be a finite generalized triangulation of a closed connected piecewise-linear $`d`$-manifold. Thus $`T`$ is obtained by affine pairings of the codimension-one faces of abstract $`d`$-simplices, permitting identifications within a simplex and multiple face pairings between simplices. No face is identified with itself by a nonidentity map, and the quotient has the local PL manifold structure.

Write $`f_0(T)`$ for its number of vertices after the identifications and $`f_d(T)`$ for its number of top-dimensional simplices. Prove or disprove that

```math
f_0(T)\le\frac{f_d(T)}2+d
```

for every such $`T`$.

## Application

Face-number bounds constrain combinatorial encodings of manifolds and can reduce exhaustive census searches. In dimension four this bound would yield a homological lower bound on the number of simplices needed to triangulate a simply connected manifold.

## References

1. J. Spreer and L. Tobin, [Vertex Bounds in Triangulated d-Manifolds and an Application to 4-Manifold Complexity](https://arxiv.org/abs/2401.11152), arXiv:2401.11152v2 (1 July 2026), Conjecture 5.1, Corollary 3.6 and Theorem 5.3.
2. J. Spreer and L. Tobin, [Small triangulations of simply connected 4-manifolds](https://doi.org/10.1007/s41468-025-00221-z), *Journal of Applied and Computational Topology* **9** (2025), article 24; journal source leading to the reference follow-up.

## Status review

The latest preprint [1] explicitly leaves the even-dimensional case open. It proves the bound for balanced triangulations, in which vertices admit $`d+1`$ colors with each simplex containing all colors, and the bound also follows for simplicial complexes. Generalized triangulations require a separate argument. Singular nonmanifold examples violate the inequality, so the manifold hypothesis is essential.

Sphere triangulations attain the proposed bound, establishing its sharpness if true. The question concerns vertex counts in all even dimensions, whereas the related $`4`$-manifold complexity conjecture concerns the minimum simplex count of simply connected manifolds. Current searches found no matching solution announcement or duplicate.
