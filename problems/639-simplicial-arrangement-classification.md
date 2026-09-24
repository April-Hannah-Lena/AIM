# 639. Eventual classification of simplicial line arrangements

**Area:** Computational geometry and incidence geometry

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

A finite set of distinct lines in $`\mathbb{RP}^2`$ is simplicial if every complementary region is a triangle. Equivalence here means isomorphism of the induced vertex-edge-face incidence structures.

Does an integer $`N`$ exist such that every simplicial arrangement of at least $`N`$ lines is equivalent to one of these configurations?

1. A pencil of $`k\ge2`$ lines and one line missing its common point.
2. The supporting lines of the sides and the symmetry axes of a regular $`k`$-gon, $`k\ge3`$.
3. The second configuration for even $`k\ge4`$, with the line at infinity added.

The question allows finitely many exceptional equivalence classes. It does not prescribe a catalogue of all small exceptions.

## Application

A classification would delimit the geometric configurations that exhaustive arrangement generators need to discover beyond the three explicit families, and clarify the structure of triangular cell decompositions.

## References

1. D. Panov and G. Tahar, [Simplicial Arrangements with Few Double Points](https://doi.org/10.1007/s00454-025-00798-3), *Discrete & Computational Geometry* **76** (2026), 958–977; online November 2025. [Primary manuscript](https://arxiv.org/abs/2409.01892), introduction, Definitions 1.1–1.3 and Theorem 1.5.

## Status review

**Known cases:** For each fixed $`K>0`$, the classification holds beyond a threshold depending on $`K`$ when the number of double intersection points is at most $`Kn`$, where $`n`$ is the number of lines.

**Remaining target:** Remove the bound on double points and obtain a universal threshold. The source's conditional classification does not supply one.

Current literature and announcement checks found no matching resolution. The July 2026 special-vertex work and September 2026 Boolean-building-set classification treat restricted families. The integration review records exact scope comparisons, duplicate checks and retrieval limits.
