# 638. Convex realizations of spherical subword complexes

**Area:** Polyhedral geometry and combinatorial topology

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $(W,S)$ be a finite Coxeter system, let $Q=(q_1,\ldots,q_m)$ be a word in its simple generators, and let $w\in W$. A reduced expression for $w$ is an expression using the smallest possible number $\ell(w)$ of simple generators.

Define $\Delta(Q,w)$ to have facets exactly the sets $I\subseteq\{1,\ldots,m\}$ for which the complementary subword $Q_{\{1,\ldots,m\}\setminus I}$ is a reduced expression for $w$. Its faces are the subsets of these facets.

Assume $\Delta(Q,w)$ is homeomorphic to a sphere of dimension $m-\ell(w)-1\ge0$. Must it be combinatorially isomorphic to the boundary complex of a convex simplicial polytope of dimension $m-\ell(w)$?

## Application

Convex realizations would turn these combinatorial spheres into explicit polytopes, linking Coxeter combinatorics with optimization, flip graphs and geometric models of generalized associahedra.

## References

1. C. Ceballos and J. Doolittle, [Subword Complexes and Kalai's Conjecture on Reconstruction of Spheres](https://doi.org/10.1007/s00454-025-00733-6), *Discrete & Computational Geometry* **74** (2025), 23–48, introduction and Section 2.2.
2. L. Bossinger, M. Gorsky and J. Simental, [Torus actions on compactified braid varieties and polytopality of subword complexes](https://arxiv.org/abs/2609.12414), 11 September 2026, Section 1.3, Theorem 1.6 and Corollary 5.11.

## Status review

**Known cases:** Root-independent constructions and generalized associahedra give established families. Reference [2] realizes further double-root-free families in its Lie-group setting, extending the earlier brick-polytope method.

**Remaining target:** Remove the special-family restrictions. Reference [2] explicitly retains general polytopality as open and does not resolve the multiassociahedron problem. Its characterization of when its particular moment-polytope construction works is not a characterization of all possible convex realizations.

Reconstruction from facet adjacency, problem632, asks for different data and is already known for these finite-type subword spheres. Current literature and public-platform checks found no matching general solution or announcement; see the integration review.
