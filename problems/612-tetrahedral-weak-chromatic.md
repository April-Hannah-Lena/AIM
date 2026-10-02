# 612. Unbounded weak chromatic number for geometric tetrahedral complexes

**Area:** Combinatorial topology and geometric hypergraphs

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`H=(V,E)`$ be a finite $`4`$-uniform hypergraph. A geometric embedding into $`\mathbb R^3`$ is an injection $`\phi:V\to\mathbb R^3`$ such that each $`\mathop{\mathrm{conv}}\nolimits\phi(e)`$ is a nondegenerate tetrahedron and

```math
\mathop{\mathrm{conv}}\nolimits\phi(e)\cap\mathop{\mathrm{conv}}\nolimits\phi(f)
=\mathop{\mathrm{conv}}\nolimits\phi(e\cap f)\qquad(e,f\in E),
```

with $`\mathop{\mathrm{conv}}\nolimits\varnothing=\varnothing`$.

The weak chromatic number is the minimum number of vertex colors for which no hyperedge is monochromatic. Is it unbounded over hypergraphs admitting such an embedding? Equivalently, for every integer $`m`$, does such a hypergraph exist with weak chromatic number greater than $`m`$?

## Application

This determines whether three-dimensional tetrahedral geometry forces a uniform bound on a natural vertex-coloring constraint for meshes and simplicial complexes.

## References

1. S. Lee and E. Nevo, [On Colorings of Hypergraphs Embeddable in $`\mathbb R^d`$](https://doi.org/10.1007/s00454-026-00856-4), *Discrete & Computational Geometry* (2026), Problem 1.2(1).
2. M. G. Dobbins and S. Lee, [Polytopes with large transversal ratio](https://arxiv.org/abs/2603.16298), 2026, Section 1.4 and Corollary 1.7.

## Status review

The journal source gives examples requiring at least three colors. The follow-up proves unboundedness in every ambient dimension at least four and singles out dimension three as remaining. Piecewise-linear embeddings, which allow subdivision, have already been settled and are not the embeddings required here.
