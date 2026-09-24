# 626. Decomposing complete graphs into squares of Hamilton cycles

**Area:** Graph theory and combinatorial designs

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For $n\ge5$, the square $C_n^2$ of an $n$-cycle joins every pair of vertices at cyclic distance one or two.

Prove or disprove that, whenever $n\equiv1\pmod4$ and $n\ne9$, the edges of the complete graph $K_n$ can be partitioned into copies of $C_n^2$. Thus the required decomposition consists of $(n-1)/4$ edge-disjoint spanning cycle squares.

## Application

Such decompositions give explicit dense packing designs and help construct simplicial complexes with large distances in their facet-adjacency graphs.

## References

1. O. Parczyk, S. Rathke and T. Szabó, [The Maximum Diameter of 2-Dimensional Simplicial Complexes](https://doi.org/10.1007/s00454-026-00844-8), *Discrete & Computational Geometry* (2026), Conjecture 4.1. [arXiv:2511.10144](https://arxiv.org/abs/2511.10144).

## Status review

The divisibility condition is necessary, and $n=9$ is impossible. The source constructs decompositions for infinitely many primes and several additional orders. The later solution of the maximum simplicial-diameter problem, arXiv:2602.20890, concerns extra-tight tours and does not supply these Hamilton-square decompositions.
