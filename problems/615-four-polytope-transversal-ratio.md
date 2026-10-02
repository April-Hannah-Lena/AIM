# 615. Transversal ratio approaching one for simplicial four-polytopes

**Area:** Discrete geometry and extremal topology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`P\subset\mathbb R^4`$ be a full-dimensional simplicial convex polytope, with vertex set $`V(P)`$. Let $`\tau(P)`$ be the minimum size of a subset of $`V(P)`$ meeting the vertex set of every facet.

Prove or disprove that, for every $`\varepsilon>0`$, there exists such a polytope with

```math
\tau(P)\ge(1-\varepsilon)|V(P)|.
```

Equivalently, every sufficiently large fraction of its vertices contains all four vertices of a facet, with the fraction made arbitrarily small by choosing $`P`$.

## Application

Facet transversals measure how many vertices must be selected to touch every boundary simplex. Their extremal size connects polytope geometry to independent sets, weak colorings and geometric surrounding properties.

## References

1. S. Lee and E. Nevo, [On Colorings of Hypergraphs Embeddable in $`\mathbb R^d`$](https://doi.org/10.1007/s00454-026-00856-4), *Discrete & Computational Geometry* (2026), Problem 1.2(2).
2. M. G. Dobbins and S. Lee, [Polytopes with large transversal ratio](https://arxiv.org/abs/2603.16298), 2026, Conjecture 1.4.

## Status review

Dobbins and Lee prove the analogous assertion for dimensions at least five and formulate the remaining dimension-four conjecture. The unrestricted class of simplicial three-spheres is broader than boundaries of convex four-polytopes; results for that class do not establish this statement. The weaker dimension-four chromatic-number question is not counted separately.
