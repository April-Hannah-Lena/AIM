# 592. Connectivity of plane spanning-path reconfiguration

**Area:** Computational geometry and geometric reconfiguration

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`P\subset\mathbb R^2`$ be a finite set of at least three points with no three collinear. Form a graph $`\mathcal F(P)`$ whose vertices are all non-crossing straight-line Hamiltonian paths on $`P`$, viewed as undirected edge sets. Two vertices of $`\mathcal F(P)`$ are adjacent if one path can be obtained from the other by deleting one edge and inserting one edge, leaving a non-crossing Hamiltonian path. Endpoints may change, and the deleted and inserted edges may cross each other.

Prove or disprove that $`\mathcal F(P)`$ is connected for every such point set $`P`$.

## Application

Connectivity is necessary for local edge-exchange algorithms to explore every feasible non-crossing route. It would guarantee that any two such routes through fixed sites can be transformed into one another while maintaining a valid route at every step.

## References

1. O. Aichholzer et al., [Reconfiguration of non-crossing spanning trees](https://doi.org/10.20382/jocg.v15i1a9), *Journal of Computational Geometry* **15**(1) (2024), 224–253, Section 1.1, p. 228.
2. V. Boucard, G. D. da Fonseca and B. Rivier, [Further Connectivity Results on Plane Spanning Path Reconfiguration](https://arxiv.org/abs/2407.00244), arXiv:2407.00244 (2024), Conjecture 1.
3. L. Kleist, P. Kramer and C. Rieck, [On the Connectivity of the Flip Graph of Plane Spanning Paths](https://arxiv.org/abs/2407.03912), *WG 2024*, 327–342.
4. H. B. Bjerkevik et al., [Flip Distance of Non-Crossing Spanning Trees: NP-Hardness and Improved Bounds](https://doi.org/10.4230/LIPIcs.SoCG.2026.16), *SoCG 2026*, Section 1.1.

## Status review

Connectivity is known for convex point sets and for sets with at most two convex layers. Reference [4] still identifies the general case as open. The 2026 linear-time algorithm for paths on convex point sets addresses a solved geometric special case, while connectivity for spanning trees allows intermediate branching and does not settle paths. The public code accompanying earlier work performs finite-instance checks. Current searches found no matching general resolution or duplicate.
