# 122 — Exact minimum length of an opaque barrier for a square

**Area:** Geometric optimization / sensing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Put $`Q=[0,1]^2`$. A rectifiable barrier is a set $`B\subset\mathbb R^2`$ that is a countable union of rectifiable curves and intersects every straight line that intersects $`Q`$. It need not be connected or contained in $`Q`$. Determine exactly

```math
b(Q)=\inf\{\mathcal H^1(B):B\text{ is a rectifiable barrier for }Q\},
```

where $`\mathcal H^1`$ is one-dimensional Hausdorff measure. The question concerns the unrestricted infimum; attainment by a barrier is not assumed.

## Application

Such a barrier models a network of line detectors that must intercept every possible straight trajectory crossing a protected region. Its length measures the required sensing infrastructure.

## References

1. M. Kiderlen and F. Pausinger, *Explicit lower bounds for opaque sets of unit square and unit disc* (2026), [Acta Mathematica Hungarica](https://doi.org/10.1007/s10474-026-01606-x), §1 and Theorem 1.2(i). States the unresolved minimum problem and improves the square lower bound.
2. A. Kawamura, S. Moriyama, Y. Otachi and J. Pach, *A Lower Bound on Opaque Sets* (2016), [SoCG, Article 46](https://doi.org/10.4230/LIPIcs.SoCG.2016.46), main theorem and rectifiable-barrier formulation.
3. A. Dumitrescu and M. Jiang, *The opaque square* (2014), [arXiv:1311.3323](https://arxiv.org/abs/1311.3323), introduction. Records the short known construction and distinguishes interior from unrestricted barriers.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 paper explicitly retains the exact minimum as open. It improves the unrestricted lower bound to $`2+6.3\times10^{-5}`$; the familiar construction of length $`\sqrt2+\sqrt6/2`$ does not have a matching optimality proof. Searches included “opaque unit square shortest barrier 2026 solved” and “Kiderlen Pausinger opaque square minimum”. Results restricted to connected or interior barriers do not settle this formulation.
