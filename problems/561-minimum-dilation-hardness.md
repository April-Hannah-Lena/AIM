# 561. Hardness of minimum-dilation triangulation

**Area:** Computational geometry and optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`P\subset\mathbb Q^2`$ be a finite set of distinct points not all on one line. A triangulation $`T`$ is a maximal plane straight-line graph on exactly the vertex set $`P`$: edges have disjoint interiors and no edge passes through another vertex. Give each edge its Euclidean length. For $`p,q\in P`$, let $`d_T(p,q)`$ be the length of a shortest path in $`T`$, and define

```math
\delta(T)=\max_{p\ne q\in P}\frac{d_T(p,q)}{\|p-q\|_2}.
```

Is the following decision problem NP-hard under polynomial-time many-one reductions in the standard binary input model? Given rational coordinates for $`P`$ and a rational threshold $`\tau\ge1`$, decide whether some triangulation $`T`$ satisfies $`\delta(T)\le\tau`$.

The edge lengths and the inequality are interpreted exactly. The question asks for NP-hardness; it does not assume membership in NP, since comparing sums of square roots introduces a separate arithmetic issue.

## Application

Minimum-dilation triangulations optimize the worst routing detour in a planar geometric network. Their complexity controls what exact algorithms can guarantee for mesh-based routing, sensor networks and geometric network design.

## References

1. S. P. Fekete, P. Keldenich and M. Perk, [Exact algorithms for minimum dilation triangulation](https://jocg.org/index.php/jocg/article/view/5783), *Journal of Computational Geometry* **17**(2) (2026), 1–45, Sections 1, 2 and 8. [arXiv:2502.18189](https://arxiv.org/abs/2502.18189).
2. [Oriented spanners](https://doi.org/10.1007/s00453-025-01342-8), *Algorithmica* (2026), related-work discussion of undirected minimum-dilation triangulation.

## Status review

The current journal source states that no polynomial-time algorithm or NP-hardness proof is known. Its exact methods solve large benchmark instances and improve a worst-case dilation lower bound; they do not classify the computational complexity. Hardness of minimum-dilation trees, edge-budgeted graphs, minimum-weight triangulations or oriented variants does not establish this target.

The formulation fixes rational input and exact comparisons to make the computational question explicit. Current searches found no matching hardness announcement. A public project announcing results for regular polygons and convex point sets does not announce general NP-hardness.
