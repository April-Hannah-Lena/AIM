# 648. Finitely many radius sets for compact sphere packings

**Area:** Discrete geometry and sphere packing

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For a packing of balls with pairwise disjoint interiors in $\mathbb R^d$, use the centers as vertices. Form the contact complex from subsets $E$ of at most $d+1$ centers for which the corresponding balls are pairwise tangent and $\operatorname{conv}(E)$ contains no other center. Call the packing **compact** when these simplices form a geometric simplicial complex whose underlying space is all of $\mathbb R^d$, with every simplex contained in a $d$-simplex.

Fix integers $d\ge3$ and $n\ge2$. Let $\Pi_{d,n}$ consist of all tuples
$$0<r_0<r_1<\cdots<r_{n-1}=1$$
that occur as the exact set of radii in such a compact packing. Is $\Pi_{d,n}$ finite for every fixed pair $(d,n)$?

All $n$ radii must occur. The packing need not be periodic, and the question counts radius tuples, not the number of packings.

## Application

Compact packings describe tightly constrained arrangements relevant to self-assembled particle structures. Finiteness would make classification by admissible particle sizes possible even when there are infinitely many spatial arrangements.

## References

1. M. Messerschmidt and E. Kikianty, [On Compact Packings of Euclidean Space with Spheres of Finitely Many Sizes](https://doi.org/10.1007/s00454-024-00628-y), *Discrete & Computational Geometry* **74** (2025), 719–742, Conjecture 1.1. [arXiv:2305.00758](https://arxiv.org/abs/2305.00758).
2. M. Messerschmidt, [The Raspberries in Three Dimensions with at Most Two Sizes of Berry](https://doi.org/10.1007/s00454-026-00821-1), *Discrete & Computational Geometry* **76** (2026), 1212–1237, introduction.

## Status review

**Known cases:** Finiteness is proved in dimension two for every fixed number of radii. The three-dimensional two-radius case is classified. The source also establishes finiteness in every dimension under an additional condition on the associated spherical triangulations.

**Remaining target:** Remove the additional geometric condition and prove finiteness for all fixed $d\ge3,n\ge2$, or exhibit a fixed pair admitting infinitely many normalized radius tuples. The June 2026 follow-up still describes the higher-dimensional theorem as conditional. Equal-radius densest packings and finite classifications with prescribed few radii do not resolve this target.
