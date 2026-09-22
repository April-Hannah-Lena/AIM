# 418. Stationarity of Lipschitz weak solutions of the minimal-surface system

**Area:** Nonlinear elliptic PDE systems / surface energy

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $n\ge3$, $m\ge2$ and $u\in W^{1,\infty}(B_1\subset\mathbb R^n;\mathbb R^m)$. Put $g_{ij}=\delta_{ij}+\sum_{\alpha=1}^m\partial_i u^\alpha\partial_j u^\alpha$, and let $(g^{ij})=g^{-1}$. Suppose, distributionally,
$$\sum_{i,j=1}^n\partial_i\big(\sqrt{\det g}\,g^{ij}\partial_j u^\alpha\big)=0\qquad(1\le\alpha\le m).$$
Must the domain-variation equations also hold distributionally,
$$\sum_{i=1}^n\partial_i\big(\sqrt{\det g}\,g^{ij}\big)=0\qquad(1\le j\le n)?$$
No small-slope or area-decreasing condition is imposed.

## Application

The two systems express force balance under changes of surface height and changes of its parametrizing domain. Their equivalence would justify the stationarity and monotonicity tools used to analyze weak surface equilibria.

## References

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §3, equations (7)–(8) and Remark 3.2. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf); [arXiv:2407.11903](https://arxiv.org/abs/2407.11903).
2. J. Hirsch, C. Mooney and R. Tione, *On the Lawson–Osserman conjecture*, Inventiones mathematicae (2026), §1, Theorem 1.1 and Remark 1.2. [DOI and full text](https://doi.org/10.1007/s00222-026-01442-4).
3. C.-J. Tsai and M.-T. Wang, *Calibrating Forms for Minimal Graphs in Arbitrary Codimension*, preprint (2026), §5, results under two-dilation assumptions. [Full text](https://arxiv.org/html/2604.04336v1).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2026 Inventiones paper solves two-dimensional domains, and explicitly leaves higher-dimensional outer-critical maps unresolved. The April 2026 calibration paper assumes bounds on products of singular values of Du. These restrictions are absent here. Searches through 22 September 2026 for the higher-dimensional Lawson–Osserman conjecture located no general resolution.
