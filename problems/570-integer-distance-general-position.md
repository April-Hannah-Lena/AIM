# 570. Arbitrarily large integer-distance sets in general position

**Area:** Discrete geometry and arithmetic geometry

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Is it true that for every positive integer $n$ there is a set $P\subset\mathbb R^2$ of $n$ distinct points satisfying all three conditions?

- $\|p-q\|_2$ is an integer for every pair of distinct points $p,q\in P$.
- No three points of $P$ lie on a line.
- No four points of $P$ lie on a circle.

The set may depend on $n$, and there is no prescribed bound on its diameter. This is a question about arbitrarily large finite configurations, not an infinite configuration with all pairwise distances integral.

## Application

These configurations test the compatibility of exact distance constraints with geometric general position. They connect distance geometry and geometric reconstruction with Diophantine equations and incidence bounds.

## References

1. D. Eppstein, [Non-Euclidean Erdős–Anning theorems](https://jocg.org/index.php/jocg/article/view/5850), *Journal of Computational Geometry* **17**(2) (2026), 46–76, Section 3.1, PDF p. 7. [arXiv:2401.06328](https://arxiv.org/abs/2401.06328).
2. R. Greenfeld, M. Iliopoulou and S. Peluse, [On integer distance sets](https://arxiv.org/abs/2401.10821), arXiv:2401.10821v3 (2025).
3. D. Eppstein, [Tangent spheres and integer distances](https://arxiv.org/abs/2606.18569), arXiv:2606.18569 (2026), CCCG 2026.

## Status review

The journal source explicitly retains this question. Seven-point configurations are known. The structure and diameter estimates of [2] constrain the size inside a bounded region, and [3] bounds the number of points in terms of the diameter of a general-position reference simplex. Neither gives a diameter-independent upper bound or constructs arbitrarily large examples.

A current GitHub announcement concerning Erdős problem 130 constructs integer-distance graphs with infinite chromatic number and clique number two; its README explicitly leaves the extremal clique question open. A separate formalization certifies the known seven-point construction and explicitly does not claim the case $n\ge8$. Thus neither announcement settles this question.
