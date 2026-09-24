# 591. A sharp Betti-number bound for 4-manifold triangulation complexity

**Area:** Computational topology and triangulation complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $M$ be a closed simply connected piecewise-linear $4$-manifold, and let $\beta_2(M)=\dim_{\mathbb Q}H_2(M;\mathbb Q)$. A generalized triangulation of $M$ consists of finitely many abstract $4$-simplices, called pentachora, with their tetrahedral faces paired by affine maps, whose quotient represents the given PL manifold. Multiple face identifications between simplices and identifications between distinct faces of the same simplex are allowed; no face may be identified with itself by a nonidentity map.

Define $c(M)$ to be the minimum number of pentachora in such a triangulation. Prove or disprove that
$$c(M)\ge 2\beta_2(M)+2$$
for every such $M$.

## Application

A lower bound depending only on homology would certify optimality of small manifold representations produced by computational searches. It would establish the minimality of known explicit triangulations of connected sums of standard $\mathbb{CP}^2$ and $S^2\times S^2$ summands.

## References

1. J. Spreer and L. Tobin, [Small triangulations of simply connected 4-manifolds](https://doi.org/10.1007/s41468-025-00221-z), *Journal of Applied and Computational Topology* **9** (2025), article 24, Conjecture 1.2 and Section 2.2. [arXiv:2501.18933](https://arxiv.org/abs/2501.18933).
2. J. Spreer and L. Tobin, [Vertex Bounds in Triangulated d-Manifolds and an Application to 4-Manifold Complexity](https://arxiv.org/abs/2401.11152), arXiv:2401.11152v2 (1 July 2026), Section 3.

## Status review

Theorem 1.1 of [1] constructs triangulations with $2\beta_2+2$ pentachora for the stated standard connected-sum families. These are upper bounds, so they do not establish the universal lower bound. The problem concerns generalized triangulations; lower bounds for simplicial complexes or graph-encoded triangulations do not automatically apply.

The July 2026 paper [2] still obtains a lower bound of $2\beta_2$ only conditionally on an unresolved vertex bound. That conditional result is both unproved in full generality and weaker than the displayed target. Current searches found no matching solution announcement or duplicate.
