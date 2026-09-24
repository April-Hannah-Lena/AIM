# 569. Unbounded chromatic number of associahedron graphs

**Area:** Discrete and computational geometry

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For each integer $n\ge3$, let $A_n$ be the graph whose vertices are all triangulations of a convex polygon with $n$ labeled vertices. Two triangulations are adjacent when one is obtained from the other by replacing one diagonal of a convex quadrilateral by its other diagonal. A proper coloring assigns different colors to adjacent triangulations; write $\chi(A_n)$ for the least number of colors required.

Prove or disprove that

$$
\sup_{n\ge3}\chi(A_n)=\infty.
$$

Equivalently, must every fixed number of colors fail for the flip graph of some sufficiently large convex polygon?

## Application

The graph describes local moves between triangulations and rotations of binary search trees. Its chromatic number measures the number of classes needed to separate configurations related by one move, and tests how much combinatorial complexity survives these geometric restrictions.

## References

1. L. Addario-Berry, B. Reed, A. Scott and D. R. Wood, [A logarithmic bound for the chromatic number of the associahedron](https://jocg.org/index.php/jocg/article/view/5192), *Journal of Computational Geometry* **17**(1) (2026), 61–74, introduction and Theorem 1. [arXiv:1811.08972](https://arxiv.org/abs/1811.08972).
2. D. R. Wood, [Chromatic number of associahedron](https://www.openproblemgarden.org/op/chromatic_number_of_associahedron), author-posted conjecture, 2015, updated 2019.

## Status review

The logarithmic upper bound $\chi(A_n)=O(\log n)$ is proved in [1]. Its introduction states that no lower bound growing with $n$ is known and records $\chi(A_{10})\ge4$. The solved logarithmic upper-bound conjecture is distinct from the unboundedness question in [2]. Facet colorings of generalized associahedra concern another graph.

Current searches found no matching solution announcement. A public GitHub research repository for this exact question has an empty results record and a planned source-check attempt, rather than an announced proof.
