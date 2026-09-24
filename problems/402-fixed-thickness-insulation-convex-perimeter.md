# 402. Best convex shape for insulation of fixed thickness and perimeter

**Area:** Elliptic PDEs / thermal shape optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $P,\beta,\delta>0$. For a compact convex planar set $K$ of perimeter $P$, define $\Omega_K=\{x:\operatorname{dist}(x,K)<\delta\}$ and
$$I_{\beta,\delta}(K)=\inf\left\{\int_{\Omega_K}|\nabla v|^2dx+\beta\int_{\partial\Omega_K}v^2d\mathcal H^1:v\in H^1(\Omega_K),\ v\ge1\text{ quasi-everywhere on }K\right\}.$$
Quasi-everywhere refers to Sobolev capacity. Degenerate line segments are admissible, with perimeter twice their length. Determine the minimum of $I_{\beta,\delta}$ in this class and characterize all minimizing sets, up to rigid motions, for every triple $(P,\beta,\delta)$.

## Application

The harmonic minimizer is the temperature in a body surrounded by a uniform insulation layer with convective heat exchange. The problem asks which cross-sectional shape loses the least heat when its perimeter and insulation thickness are prescribed.

## References

1. F. Della Pietra, C. Nitsch and C. Trombetti, *An optimal insulation problem*, Mathematische Annalen 382 (2022), 745–759, §5, Open Problem 1 and the preceding compactness discussion. [Full text](https://doi.org/10.1007/s00208-020-02058-6).
2. D. Bucur, M. Nahon, C. Nitsch and C. Trombetti, *Shape optimization of a thermal insulation problem*, Calculus of Variations and Partial Differential Equations 61 (2022), article 186, introduction and Theorem 1. [Full text](https://doi.org/10.1007/s00526-022-02298-1).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open Problem 1 asks precisely for this convex planar minimum; the source allows degenerate segments in its compact convex class. Its disk theorem concerns the maximum. The later two-body volume-constrained result allows the insulation boundary to vary independently and does not answer the fixed-thickness perimeter problem. Searches through 22 September 2026 for the exact problem title, convex perimeter minima and constant-thickness insulation found no resolution.
