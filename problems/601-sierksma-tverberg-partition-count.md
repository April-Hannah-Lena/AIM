# 601. Sierksma's lower bound for Tverberg partitions

**Area:** Discrete geometry and convexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`d\ge2`$ and $`r\ge3`$ be integers, and let $`X\subset\mathbb R^d`$ consist of exactly $`(d+1)(r-1)+1`$ distinct points. A Tverberg partition is an unordered partition

```math
X=X_1\sqcup\cdots\sqcup X_r
```

into nonempty sets such that

```math
\bigcap_{i=1}^r\mathop{\mathrm{conv}}\nolimits(X_i)\ne\varnothing.
```

Prove or disprove that every such $`X`$ has at least

```math
((r-1)!)^d
```

distinct Tverberg partitions. Partitions differing only by the order of their parts are counted once. The claim imposes no general-position assumption.

## Application

The bound would quantify the multiplicity of convex consensus partitions, strengthening Tverberg's existence theorem. It would provide a sharp combinatorial benchmark for algorithms that enumerate common-intersection partitions of point data.

## References

1. S. H. Chan, G. Kalai, B. Narayanan, N. Ter-Saakov and M. White, [Unimodality for Radon Partitions of Random Vectors](https://doi.org/10.1007/s00454-026-00870-6), *Discrete & Computational Geometry* (2026), Conjecture 7.3. [arXiv:2507.01353](https://arxiv.org/abs/2507.01353).
2. P. Soberón, [An elementary proof of Sierksma's conjecture for seven points in the plane](https://arxiv.org/abs/2604.18485), arXiv:2604.18485 (2026).

## Status review

Configurations attaining the proposed count are known, so the unresolved assertion is the universal lower bound. Reference [2] gives a new proof only for $`(d,r)=(2,3)`$, a case already known by topological methods. The general conjecture remains explicitly stated in the September 2026 source [1]. Current searches found no general solution announcement or duplicate.
