# 618. Reconstructing simplicial spheres from facet adjacency

**Area:** Combinatorial topology and polyhedral geometry

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`K`$ and $`L`$ be finite simplicial complexes whose geometric realizations are homeomorphic to $`S^d`$, where $`d\ge3`$. Their facet-ridge graphs have one vertex per $`d`$-dimensional facet; two graph vertices are adjacent exactly when their facets share a $`(d-1)`$-face.

Prove or disprove that every graph isomorphism

```math
\varphi:\mathop{\mathrm{FR}}\nolimits(K)\longrightarrow\mathop{\mathrm{FR}}\nolimits(L)
```

is induced by a unique simplicial isomorphism $`K\to L`$. No shellability or polytopality assumption is imposed.

## Application

This asks whether adjacency data between top-dimensional simplices suffices to recover all faces of a triangulated sphere, a basic question for compact representations and reconstruction of meshes.

## References

1. C. Ceballos and J. Doolittle, [Subword Complexes and Kalai's Conjecture on Reconstruction of Spheres](https://doi.org/10.1007/s00454-025-00733-6), *Discrete & Computational Geometry* **74** (2025), 23–48, Conjecture 1.2.
2. Y. Yang, [Reconstructing a shellable sphere from its facet-ridge graph](https://arxiv.org/abs/2401.04220), 2024, revised 2025.

## Status review

**Known cases:** Simplicial polytopes are reconstructible, and Yang proves reconstruction for shellable simplicial spheres.

**Remaining target:** Establish the stated extension property for arbitrary simplicial spheres, without shellability. Kalai's February 2026 update still identifies the unrestricted sphere problem as open. Counterexamples for triangulations of the torus and projective plane do not settle the sphere case.
