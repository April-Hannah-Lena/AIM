# 031. Komlós’s vector-balancing conjecture

**Area:** Discrepancy and matrix rounding

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Does there exist a universal constant $C<\infty$ such that, for every $m,n\ge1$ and every real matrix $A\in\mathbb R^{m\times n}$ whose columns satisfy $\sum_{i=1}^m a_{ij}^2\le1$, there is $x\in\{-1,1\}^n$ with
$$\|Ax\|_\infty\le C?$$
The constant must be independent of both dimensions and of the matrix.

## Application

The conjecture asks whether simultaneous linear constraints can be rounded with uniformly bounded error when each variable has bounded total Euclidean influence. It informs integer optimization, load balancing and numerical integration.

## References

1. N. Bansal and H. Jiang, [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961), 2025; STOC 2026. States the conjecture and improves the dimension-dependent bound.
2. N. Bansal, D. Dadush and S. Garg, [An algorithm for Komlós conjecture matching Banaszczyk’s bound](https://arxiv.org/abs/1605.02882), 2016. Earlier constructive bound.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. Bansal–Jiang obtain a bound of order $\widetilde O((\log n)^{1/4})$, where the suppressed factors are polylogarithmic in $\log n$. This remains dimension-dependent; the title of the earlier “algorithm for Komlós” paper does not mean that the constant-bound conjecture was proved. No subsequent constant bound was located.

Searches included: `Komlós conjecture 2026 solved`; `Decoupling Affine Spectral Independence Komlos`; `Komlos constant discrepancy proof`. This is a documented literature check, not a certification that no solution exists.
