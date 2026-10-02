# 501. A strict gap between face and cycle percolation thresholds

**Area:** Applied topology and random geometric complexes

**Status:** 🔵 OPEN

**Last checked:** 2026-09-23

## Problem statement

Fix integers $`D\ge3`$ and $`2\le d<D`$. Let $`X_\lambda`$ be a homogeneous Poisson process of intensity $`\lambda>0`$ in $`\mathbb R^D`$. Form the Vietoris–Rips complex whose simplices are finite subsets of $`X_\lambda`$ with all pairwise Euclidean distances at most $`1`$.

Two $`d`$-simplices are adjacent when they share a $`(d-1)`$-face. Let $`F_d`$ be the event that this adjacency graph has an infinite connected component. Let $`C_d`$ be the event that there is an infinite, locally finite, face-connected collection $`M`$ of $`d`$-simplices such that every $`(d-1)`$-face belongs to an even number of members of $`M`$.

Define

```math
\lambda_d^{\mathrm{face}}=\inf\{\lambda>0:\mathbb P(F_d)>0\},\qquad
\lambda_d^{\mathrm{cycle}}=\inf\{\lambda>0:\mathbb P(C_d)>0\}.
```

Is

```math
\lambda_d^{\mathrm{face}}<\lambda_d^{\mathrm{cycle}}
```

true for every such $`D,d`$?

Here a cycle means precisely the even-incidence collection above; it need not represent a nonzero persistent or ordinary homology class.

## Application

These thresholds describe when connected chains and boundary-free structures span a random geometric complex. Their separation would distinguish regimes relevant to controlling spatial dependence in topological statistics; it does not by itself establish a statistical limit theorem.

## References

1. C. Hirsch and D. Valesin, [Face and cycle percolation](https://doi.org/10.1007/s41468-025-00202-2), Journal of Applied and Computational Topology **9** (2025), article 6. §2, equations (1)–(2), Theorem 2 and the first paragraph of p.8; [preprint](https://arxiv.org/abs/2212.06243).
2. S. Kanazawa, O. Bobrowski and P. Skraba, [Sharp Phase Transition for the Formation of Infinite Tubes](https://arxiv.org/abs/2605.14910), 2026 preprint, §§1–3. A related lattice model.

## Status review

Theorem 2 of [1] proves $`0<\lambda_d^{\mathrm{face}}\le\lambda_d^{\mathrm{cycle}}<\infty`$ in the displayed range. Its strict inequality for a different, proximity-based adjacency rule (Theorem 3) does not prove the requested gap. The dimension-one thresholds coincide, so that case is excluded.

The 2026 paper [2] studies independently retained lattice plaquettes, not Poisson Vietoris–Rips simplices. Searches on 23 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar checks, located no matching resolution or announcement.
