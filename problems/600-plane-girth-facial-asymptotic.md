# 600. The sharp asymptotic facial length in girth-saturated plane graphs

**Area:** Graph theory and topological graph embeddings

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For an integer $`\ell\ge3`$, consider finite simple graphs with fixed crossing-free embeddings in the plane, girth at least $`\ell`$, and the following maximality property: no edge between two currently nonadjacent vertices can be drawn without crossings while preserving girth at least $`\ell`$.

A facial cycle is a simple cycle that constitutes the entire boundary of a face. Let $`F(\ell)`$ be the maximum length of such a cycle over all the embeddings above; assign value zero to an embedding with no facial cycle.

Prove or disprove that

```math
F(\ell)=3\ell+o(\ell)\qquad(\ell\to\infty).
```

## Application

Facial-length bounds control the possible size of unfilled regions in saturated sparse planar networks. Sharp bounds also improve edge-count estimates for planar saturation problems through Euler's formula.

## References

1. M. Axenovich, L. Kießle, A. Sagdeev and M. Zhukovskii, [Faces in Girth-Saturated Graphs on Surfaces](https://doi.org/10.1007/s00454-026-00833-x), *Discrete & Computational Geometry* (2026), Section 6, Question 1. [arXiv:2410.13481](https://arxiv.org/abs/2410.13481).

## Status review

The source proves $`3\ell-11\le F(\ell)\le8\ell-13`$ for $`\ell\ge7`$. Thus linear growth is established, but its proposed leading constant is unresolved. This is a bound on facial cycles, not on boundary walks that repeat vertices or edges, and maximality refers to the fixed embedding. The later independent linear bound noted in the source does not give the target constant. Searches found no matching resolution or duplicate.
