# 247 — An overlap-free edge unfolding for every convex polyhedron

**Area:** Computational geometry / sheet fabrication

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $P\subset\mathbb R^3$ be a convex polytope with nonempty interior, and let $G$ be the graph formed by its vertices and edges. Does there always exist a spanning tree $T\subset G$ such that cutting $\partial P$ along $T$ and developing the resulting intrinsic Euclidean surface into the plane produces a single net whose face interiors are pairwise disjoint?

Each face must retain its original shape and size. Cuts may use only original edges; the question permits contact along boundaries of unfolded faces, but no overlapping interiors.

## Application

An affirmative answer would guarantee that every convex polyhedral shell can be manufactured from one connected planar sheet using cuts along its existing edges.

## References

1. J. O'Rourke, *The Open Problems Project*, [Problem 9: Edge-Unfolding Convex Polyhedra](https://topp.openproblem.net/p9), statement and status. Expert formulation of Dürer's edge-unfolding problem.
2. M. Ghomi, *Affine unfoldings of convex polyhedra* (2014), [Geometry & Topology 18, 3055–3090](https://doi.org/10.2140/gt.2014.18.3055), §1, Theorem 1.1; [author manuscript](https://ghomi.math.gatech.edu/Papers/durer.pdf). Proves an unfolding theorem after a suitable affine deformation.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The expert problem list continues to mark the unrestricted edge-unfolding question open. Ghomi's theorem may change the metric shape by affine stretching, so it does not give an unfolding of the original prescribed polyhedron. Searches included “Dürer unfolding conjecture 2026 proof”, “convex polyhedron edge unfolding solved”, and “prismatoid band unfolding 2026”. Results for special families and affine deformations were found, but no theorem covering every original convex polyhedron was located.
