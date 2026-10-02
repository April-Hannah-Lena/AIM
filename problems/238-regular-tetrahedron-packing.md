# 238. The densest packing of congruent regular tetrahedra

**Area:** Granular packing and particle assembly

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $`T\subset\mathbb R^3`$ be a regular tetrahedron of side length one. A packing $`\mathcal P`$ is a locally finite collection of images of $`T`$ under Euclidean isometries, with pairwise disjoint interiors. Define

```math
\delta(\mathcal P)=\limsup_{R\to\infty}\frac{|B_R(0)\cap\bigcup_{P\in\mathcal P}P|}{|B_R(0)|},\qquad\delta_T=\sup_{\mathcal P}\delta(\mathcal P).
```

Determine $`\delta_T`$ exactly, by giving a matching rigorous upper bound and packing construction. Arbitrary orientations and nonperiodic packings are allowed; the known density $`4000/4671`$ is a lower bound, not an assumption about optimality.

## Application

The optimum constrains dense granular assemblies and crystalline structures made from faceted particles. Regular tetrahedra already favor arrangements with more than one orientation per cell.

## References

- Elizabeth R. Chen, Michael Engel and Sharon C. Glotzer, [*Dense crystalline dimer packings of regular tetrahedra*](https://arxiv.org/abs/1001.0586) (2010), abstract and densest dimer construction: density $`4000/4671`$ and limited-cell numerical optimality evidence.
- Simon Gravel, Veit Elser and Yoav Kallus, [*Upper bound on the packing density of regular tetrahedra and octahedra*](https://arxiv.org/abs/1008.2830) (2010 preprint; 2011 publication), abstract and tetrahedron bound: a strictly positive unavoidable void fraction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “regular tetrahedron densest packing exact proof 2025 2026”, “4000/4671 improved tetrahedron packing”, and current packing bounds. No matching upper bound or replacement exact optimum was located. Results for rounded, truncated or irregular tetrahedra concern different particles, and optimization within a bounded periodic unit cell does not cover all competitors.
