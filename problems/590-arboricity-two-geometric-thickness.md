# 590. Bounded geometric thickness for unions of two forests

**Area:** Computational geometry and graph drawing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`G`$ be a finite simple graph whose edge set can be partitioned into two forests, equivalently a graph of arboricity at most $`2`$. Define its geometric thickness $`\bar\theta(G)`$ to be the smallest number of edge colors in a straight-line drawing with no same-color crossings. All colors share the same positions of the vertices; vertices are distinct and no edge passes through a nonincident vertex.

Does there exist an absolute constant $`C`$ such that

```math
\bar\theta(G)\le C
```

for every such graph $`G`$?

## Application

A positive answer would give a constant number of crossing-free straight-line layers for a broad class of sparse networks. A negative answer would show that even the union of just two abstract forests can require arbitrarily many geometric layers.

## References

1. R. Jain, M. Ricci, J. Rollin and A. Schulz, [On the geometric thickness of 2-degenerate graphs](https://jocg.org/index.php/jocg/article/view/5176), *Journal of Computational Geometry* **15**(2) (2024), 94–123, Section 4. [arXiv:2302.14721](https://arxiv.org/abs/2302.14721).
2. C. A. Duncan, [On graph thickness, geometric thickness, and separator theorems](https://doi.org/10.1016/j.comgeo.2010.09.005), *Computational Geometry* **44**(2) (2011), 95–99. [Conference version](https://cccg.ca/proceedings/2009/cccg09_04.pdf).

## Status review

The known $`O(\log |V(G)|)`$ upper bound [2] grows with the graph size. Reference [1] obtains a constant bound for the proper subclass of $`2`$-degenerate graphs and explicitly leaves boundedness for arboricity-two graphs open. This question concerns the existence of any universal constant on the larger class, rather than the precise constant for that subclass. Searches found no matching resolution or duplicate.
