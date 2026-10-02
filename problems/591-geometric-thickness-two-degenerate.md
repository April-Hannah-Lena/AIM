# 591. Three or four layers for 2-degenerate graphs

**Area:** Computational geometry and graph drawing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

A finite simple graph is $`2`$-degenerate if every nonempty subgraph has a vertex of degree at most $`2`$. Its geometric thickness $`\bar\theta(G)`$ is the least number of colors in an edge coloring of some straight-line drawing of $`G`$ in the plane such that no two edges of the same color cross. Vertices are distinct, no edge passes through a nonincident vertex, and every color uses the same vertex positions.

Determine whether every $`2`$-degenerate graph satisfies

```math
\bar\theta(G)\le 3.
```

Equivalently, does a $`2`$-degenerate graph of geometric thickness $`4`$ exist? The maximum is already known to be either $`3`$ or $`4`$.

## Application

Geometric thickness measures the number of crossing-free layers required for straight-line network layouts. The answer would give the exact worst-case layer requirement for graphs constructed by adding each vertex with at most two earlier neighbors.

## References

1. R. Jain, M. Ricci, J. Rollin and A. Schulz, [On the geometric thickness of 2-degenerate graphs](https://jocg.org/index.php/jocg/article/view/5176), *Journal of Computational Geometry* **15**(2) (2024), 94–123, Section 4. [arXiv:2302.14721](https://arxiv.org/abs/2302.14721).

## Status review

The source proves a universal upper bound of four, even with each color class a forest, and constructs graphs requiring at least three. Its special monotone subclass admits three layers; this does not settle all $`2`$-degenerate graphs. A 2026 result about simple topological thickness allows curved edges and does not settle geometric thickness. Current searches found no matching solution announcement or duplicate.
