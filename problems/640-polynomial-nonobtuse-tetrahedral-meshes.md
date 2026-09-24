# 640. Polynomial-size nonobtuse tetrahedral meshes

**Area:** Numerical PDEs and computational geometry

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $P\subset\mathbb R^3$ be the closure of a bounded polyhedral domain with a finite polygonal boundary, and let $n$ be its boundary combinatorial complexity (vertices, edges and faces).

Do universal constants $C,k>0$ exist such that every such $P$ admits a conforming tetrahedralization with at most $Cn^k$ tetrahedra, all of whose interior dihedral angles are at most $\pi/2$?

Here the tetrahedra have disjoint interiors and cover $P$; intersections are common faces, edges or vertices, and each input boundary face is a union of mesh triangles. Arbitrary additional vertices on the boundary and in the interior are allowed. The bound must be independent of geometric aspect ratios. The target is an element-count bound, without a prescribed polynomial-time construction.

## Application

Nonobtuse tetrahedra provide useful sufficient conditions for discrete maximum principles in finite-element discretizations. A geometry-independent size bound would control the number of unknowns needed to enforce these angle conditions on general polyhedral domains.

## References

1. M. Bern, S. Mitchell and J. Ruppert, [Linear-size Nonobtuse Triangulation of Polygons](https://doi.org/10.1007/BF02570715), *Discrete & Computational Geometry* **14** (1995), 411–428, concluding question. [Author manuscript](https://www.sandia.gov/files/samitch/files/ls-nonobtuse.pdf), Section 7.
2. C. J. Bishop, [Research proposal](https://www.math.stonybrook.edu/~bishop/vita/nsf12.pdf) (2012), Question 17, p. 9, restating the three-dimensional size question.
3. J. Brandts, S. Korotov, M. Křížek and J. Šolc, [On Nonobtuse Simplicial Partitions](https://doi.org/10.1137/060669073), *SIAM Review* **51** (2009), 317–335, Definition 1 and pp. 327–328. [Published text](https://pure.uva.nl/ws/files/836396/73198_315330.pdf).
4. S. Korotov and M. Křížek, [Two-sided bounds for dihedral angle sums of path and 4-ball tetrahedra](https://arxiv.org/abs/2601.08304) (2026), Theorem 7 and Remark 8.

## Status review

**Known cases:** The planar polygon analogue has a linear-size construction. In three dimensions, the 2026 paper partitions a tetrahedron having a sphere tangent to all six edges into 24 nonobtuse path tetrahedra when that sphere's center lies inside it; a boundary-center variant uses 18.

**Remaining target:** A uniform polynomial size bound for conforming meshes of arbitrary polyhedral domains. Decompositions that fail to meet face-to-face do not establish this statement. The 2009 survey explicitly distinguishes such dissections from conforming partitions.

Literature and public announcement searches found no matching general resolution. The source review records the comparison with the older dissection claim and the limits of GitHub and Zenodo retrieval.
