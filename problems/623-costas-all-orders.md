# 623. Costas arrays at every order

**Area:** Combinatorial signal design

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For each positive integer $`n`$, does there exist a permutation $`f`$ of $`\{1,\ldots,n\}`$ such that, for every $`h\in\{1,\ldots,n-1\}`$, the integers

```math
f(i+h)-f(i),\qquad 1\le i\le n-h,
```

are pairwise distinct? All differences are taken in the integers, without reduction modulo $`n`$.

Such a permutation describes a Costas array. Settle existence for every order, either by proving the assertion or by proving nonexistence at some order. Failure of a search or of a particular algebraic construction is insufficient for the negative answer.

## Application

Costas arrays prescribe frequency-hopping patterns with distinct displacement vectors. Their correlation properties help distinguish delay and Doppler shifts in radar, sonar and integrated sensing systems.

## References

1. K. Drakakis, [Open problems in Costas arrays](https://arxiv.org/abs/1102.5727), Section 3.1, Definition 1, and Section 4.1, Problem 1.
2. S. W. Golomb and G. Gong, [The Status of Costas Arrays](https://doi.org/10.1109/TIT.2007.907524), *IEEE Transactions on Information Theory* **53**(11) (2007), 4260–4265. Journal discovery route.
3. F. Güleç and V. Abolghasemi, [Universal Costas Matrices: Towards a General Framework for Costas Array Construction](https://arxiv.org/abs/2602.03407), 2026, Sections I and VI.

## Status review

**Known cases:** Finite-field constructions produce infinitely many orders, including $`p-1`$ for primes $`p`$ and $`q-2`$ for prime powers $`q\ge3`$. Enumeration supplies further examples.

**Remaining target:** Decide the universal existence assertion. The 2026 framework in [3] introduces search tools and does not establish existence at arbitrary order. The August 2026 census arXiv:2608.28690 concerns main-diagonal symmetric arrays of orders37–42, not a universal construction or a nonexistence result for unrestricted arrays.

Current literature and public GitHub, Zenodo and Palomar checks found no matching general solution or announcement. Exact search limitations and inspected primary locations are recorded in the integration review.
