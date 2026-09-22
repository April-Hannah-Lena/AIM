# 252 — The least-area convex cover of every unit-length planar curve

**Area:** Geometric optimization / coverage

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\mathcal C$ be the class of compact convex sets $K\subset\mathbb R^2$ with the following property: for every continuous rectifiable curve $\gamma:[0,1]\to\mathbb R^2$ of length one, there are a rotation $R\in SO(2)$ and a translation vector $a\in\mathbb R^2$ such that

$$
R\gamma([0,1])+a\subset K.
$$

Determine $\inf_{K\in\mathcal C}\operatorname{Area}(K)$ and characterize the minimizers up to rigid motion. Curves may self-intersect and need not be closed. This is the convex version of Moser's worm problem.

## Application

The cover is a smallest convex container that accommodates a flexible unit-length object regardless of its planar shape, after repositioning it.

## References

1. T. Khandhawit, D. Pagonakis and S. Sriswasdi, *Lower Bound for Convex Hull Area and Universal Cover Problems* (2013), [International Journal of Computational Geometry & Applications 23, 197–212](https://doi.org/10.1142/S0218195913500076), §1; [author manuscript](https://arxiv.org/abs/1101.5638). States the convex worm problem and proves a lower bound.
2. Z. Deng, *Balanced Support Calibrations for Moser's Worm Problem: Exact Certificate and Bound of Triangular Cover* (2026), [arXiv:2609.04591](https://arxiv.org/abs/2609.04591), abstract and triangular-cover construction. A recent upper-bound claim, rather than an exact solution.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Existence of an optimal convex cover is known; the question is its area and shape. The September 2026 preprint claims an improved triangular cover, leaving a gap from established lower bounds. It was treated as a preprint claim, without independent proof certification. Searches included “Moser worm 2025 2026”, “worm problem convex cover exact solution”, and “Moser convex cover lower bound”. No matching lower and upper bounds identifying the optimum were located.
