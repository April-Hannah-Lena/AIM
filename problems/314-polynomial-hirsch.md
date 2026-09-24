# 314. Polynomial bounds for the graph diameter of polytopes

**Area:** Convex geometry and linear optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

A convex polytope $`P\subset\mathbb R^d`$ is a bounded intersection of finitely many closed half-spaces. Assume $`P`$ has nonempty interior in $`\mathbb R^d`$, where $`d\ge1`$, and exactly $`n`$ facets, its faces of dimension $`d-1`$. In particular, $`n\ge d+1`$.

The vertex-edge graph $`G(P)`$ has the vertices of $`P`$ as its nodes; two nodes are adjacent precisely when they are the endpoints of an edge of $`P`$. For vertices $`u,v`$, let $`\mathop{\mathrm{dist}}\nolimits_{G(P)}(u,v)`$ be the minimum number of edges in a path joining them. Define

```math
\mathop{\mathrm{diam}}\nolimits G(P)=\max_{u,v\in V(P)}\mathop{\mathrm{dist}}\nolimits_{G(P)}(u,v).
```

Do there exist absolute constants $`C,k>0`$ such that every such polytope satisfies

```math
\mathop{\mathrm{diam}}\nolimits G(P)\le C(n+d)^k?
```

The same constants must work for all dimensions and all facet counts. There are no rationality, simplicity or conditioning assumptions. Paths use actual edges and may move in either direction; no linear objective is prescribed. This is the polynomial Hirsch conjecture for bounded polytopes. It asks for the existence of short paths, without requiring an algorithm to find them.

## Application

A bounded feasible region in linear programming is a polytope, and nondegenerate simplex pivots move between its vertices along edges. Its graph diameter therefore gives a geometric lower bound on the worst-case number of pivots needed when the starting vertex and objective vary. A superpolynomial diameter family would obstruct every uniformly polynomial pivot bound. A polynomial diameter bound would remove that obstruction, while leaving the additional tasks of choosing objective-improving steps and computing them efficiently. These extra algorithmic requirements are the subject of existing [entry 095](095-strongly-polynomial-simplex.md); the present question concerns the geometry of the feasible region.

## References

1. Alexander E. Black and Lei Xue, *Any Proof of Polynomial Hirsch Must be Completely Incoherent*, [arXiv:2607.11628v1](https://arxiv.org/html/2607.11628v1), July 13, 2026, §1 and Theorem 1.1. Explicit polynomial Hirsch formulation and a counterexample for coherent monotone paths.
2. Bento Natura, *Circuit Diameter of Polyhedra is Strongly Polynomial*, [arXiv:2602.06958v2](https://arxiv.org/html/2602.06958v2), revised February 10, 2026, §§1–1.2 and Theorem 1.1. Independent status discussion and a positive result for circuit walks.
3. Lasse Wulf, *Computing the Polytope Diameter is Even Harder than NP-Hard (Already for Perfect Matchings)*, FOCS 2025, [proceedings PDF](https://ieee-focs.org/FOCS-2025-Papers/pdfs/FOCS2025-4pLZMZRP5BPG9n0GSua5T9/713200a531/713200a531.pdf), §I and Theorem 1. Independent formulation and the distinction between diameter bounds and computing diameter.
4. Michael J. Todd, *An Improved Kalai–Kleitman Bound for the Diameter of a Polyhedron*, [author manuscript](https://people.orie.cornell.edu/~miketodd/diampolynn.pdf), 2014, §1 and Theorem 2.1; [arXiv version record](https://arxiv.org/abs/1402.3579). A general quasipolynomial upper bound.
5. Noriyoshi Sukegawa, *An Asymptotically Improved Upper Bound on the Diameter of Polyhedra*, Discrete & Computational Geometry 62 (2019), 690–699, [DOI 10.1007/s00454-018-0016-y](https://doi.org/10.1007/s00454-018-0016-y), first published online June 19, 2018; [2017 conference manuscript](https://real.mtak.hu/80732/1/jXaio4T11ygd57.pdf), printed pp. 459–460, §1.1, Theorem 1 and Corollary 3. An asymptotically improved exponent; the accessible conference text was used for the theorem review.
6. Francisco Santos, *A counterexample to the Hirsch conjecture*, Annals of Mathematics 176 (2012), 383–412, [DOI 10.4007/annals.2012.176.1.7](https://doi.org/10.4007/annals.2012.176.1.7); [accepted manuscript](https://arxiv.org/html/1006.2814v3), Conjecture 1.3, Theorems 1.5–1.6 and Corollary 1.7. The surviving polynomial question and the counterexample to the stronger linear bound.
7. Alexander E. Black, *Monotone Diameters of Lattice Polytopes*, [arXiv:2609.08647v1](https://arxiv.org/html/2609.08647v1), September 8, 2026, §1, Theorems 1.1–1.2. Distinguishes monotone bounded examples from unbounded graph-diameter examples.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-17. The independently authored 2025 and 2026 sources retain the unrestricted graph-diameter question. General upper bounds remain quasipolynomial: Todd proves $`(n-d)^{\log_2 d}`$, while Sukegawa obtains an exponent of the form $`\log_2 d-\log_2\log_2 d+O(1)`$ for $`d\ge2`$. This exponent still grows with dimension. The original linear Hirsch bound $`n-d`$ is false, but its counterexamples do not refute every polynomial bound.

Black–Xue's Theorem 1.1 concerns coherent monotone paths, a restricted class obtained by varying a linear objective along an affine line in objective space. Its exponential lower bound does not apply to all undirected edge paths. Natura's Theorem 1.1 bounds circuit walks, whose steps can pass through the interior and finish at nonvertices. Such walks are not paths in $`G(P)`$. Black's September 2026 Theorem 1.1 imposes objective monotonicity, while Theorem 1.2 concerns unbounded polyhedra and does not control facet count. Neither gives a counterexample to the statement here. Wulf's hardness theorem concerns deciding the diameter of an input polytope; it does not provide a family with superpolynomial diameter.

The [evidence ledger](../research/expansion-2026-09/candidates/polynomial-hirsch.json) records source versions, theorem comparisons, duplicate checks and the separate adversarial review. The separated A23 adversarial self-pass passed on September 17, 2026. No independent agent or human review is claimed.

Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration. Review was a separated adversarial self-pass; no independent agent or human review is claimed.
