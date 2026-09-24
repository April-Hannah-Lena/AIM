# 542. Homotopy type of torus-grid Rips complexes at half the diameter

**Area:** Applied topology and persistent homology

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For an integer $k\ge3$, give $T_{2k}=\{0,\ldots,2k-1\}^2$ the periodic grid metric

$$
d((a,b),(c,e))=\min\{|a-c|,2k-|a-c|\}+\min\{|b-e|,2k-|b-e|\}.
$$

Its diameter is $2k$. Let $K_{2k}(k)$ be the simplicial complex of subsets of diameter at most $k$.

Prove or disprove the homotopy equivalence

$$
K_{2k}(k)\simeq S^3\vee\bigvee_{j=1}^{4k}S^{2k-1}
$$

for every integer $k\ge3$, where $\vee$ denotes a wedge at a common base point.

## Application

An exact homotopy description would identify high-dimensional features that arise when a Rips filtration of periodic data passes beyond local geometric reconstruction.

## References

1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, [Vietoris–Rips Complexes of Torus Grids](https://doi.org/10.1007/s00009-025-02945-9), Mediterranean Journal of Mathematics **22**, 173 (2025), Table 1 and Question 8.6. [Author version](https://arxiv.org/abs/2502.07134v2).

## Status review

Question 8.6 also includes $k=2$, whose nine-sphere wedge is already known; the statement here starts at $k=3$. Matching Betti numbers alone would not prove the asserted homotopy equivalence. The cross-polytope result at scale $2k-1$ concerns a different scale.

Primary-source and announcement checks on 24 September 2026 found no matching resolution. A live [persistence-map counterexample announcement](https://zenodo.org/records/22250420) does not claim this half-diameter homotopy formula. Its limited overlapping third-homology computations are consistent with the formula and do not establish the required homotopy equivalence.
