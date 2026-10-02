# 572. Unimodal connectivity by 2–3 and 3–2 Pachner moves

**Area:** Computational topology and triangulated 3-manifolds

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`M`$ be a compact connected 3-manifold with no 2-sphere boundary components. Use generalized triangulations formed by affine pairings of all faces of finitely many tetrahedra; vertices and edges within one tetrahedron may be identified, but an edge may not be identified with itself in reverse. A vertex whose link is a 2-sphere is internal. Other vertices are ideal, and truncating them produces boundary components of $`M`$.

Let $`T`$ and $`U`$ be triangulations of the closed manifold $`M`$, or ideal triangulations representing $`M`$ when its boundary is nonempty. Suppose each has at least two tetrahedra and they have the same number of internal vertices, possibly zero.

A legal $`2`$–$`3`$ move replaces two distinct tetrahedra joined along a face by three tetrahedra around a new edge; its inverse is a $`3`$–$`2`$ move. Is it always possible to pass from $`T`$ to $`U`$ by a finite sequence consisting first entirely of $`2`$–$`3`$ moves and then entirely of $`3`$–$`2`$ moves, with every move preserving the represented manifold?

Equivalently, must $`T`$ and $`U`$ have a common triangulation reachable from each using only $`2`$–$`3`$ moves? Either portion of the sequence may be empty.

## Application

Triangulation moves support manifold recognition and simplification algorithms. A common triangulation reachable by increasing moves would impose useful structure on the search space and justify algorithms that organize searches around a single maximum of the tetrahedron count.

## References

1. B. A. Burton and A. He, [Connecting 3-Manifold Triangulations with Unimodal Sequences of Elementary Moves](https://doi.org/10.1007/s00454-025-00735-4), *Discrete & Computational Geometry* **75** (2026), 1306–1330, Section 2.1, Notation 2.6 and Conjecture 3.1. [arXiv:2012.02398](https://arxiv.org/abs/2012.02398), version 3 (2025).
2. B. A. Burton, [Code accompanying computational topology papers](https://people.smp.uq.edu.au/BenjaminBurton/code/), including the experiments with A. He.

## Status review

Arbitrary sequences of $`2`$–$`3`$ and $`3`$–$`2`$ moves are known to connect the triangulations under these hypotheses. Theorem 3.2 of [1] proves a unimodal sequence when the descending moves may instead be $`2`$–$`0`$ moves. That theorem does not establish the conjecture above, which permits only $`2`$–$`3`$ and $`3`$–$`2`$ moves.

The current arXiv version and the published paper explicitly retain Conjecture 3.1. The connected-manifold formulation above avoids componentwise vertex-count ambiguities. Current literature and announcement searches found no proof or counterexample to this formulation.
