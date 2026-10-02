# 556. Does integration of uniformly derivative-bounded analytic functions suffer the dimensional curse?

**Area:** Numerical integration and information-based complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For each $`d\ge1`$, define

```math
F_d=\{f\in C^\infty([0,1]^d):\|D^\alpha f\|_\infty\le1\text{ for every }\alpha\in\mathbb N_0^d\},\qquad
I_d(f)=\int_{[0,1]^d}f(x)\,dx.
```

The derivative condition includes $`\alpha=0`$ and every mixed derivative, with the same bound one at all orders.

Let $`n(\varepsilon,d)`$ be the smallest number of exact function evaluations needed by a deterministic algorithm to approximate $`I_d(f)`$ with absolute error at most $`\varepsilon`$ for every $`f\in F_d`$. Sampling may be adaptive and reconstruction may be nonlinear; there is no restriction to positive quadrature weights.

Does this integration problem suffer from the curse of dimensionality? Specifically, do there exist $`\varepsilon_0\in(0,1)`$, $`c>0`$ and $`\rho>1`$ such that

```math
n(\varepsilon_0,d)\ge c\rho^d
```

for infinitely many dimensions $`d`$?

## Application

This problem tests whether uniformly controlling derivatives of every order is enough to prevent exponential sampling cost for high-dimensional integration. It would clarify what analytic regularity alone can guarantee before extra structure or randomness is imposed.

## References

1. D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica* **35** (2026), 273–457. Section 8.1, equation (8.5) and the discussion following Proposition 8.3.
2. E. Novak and F. Pillichshammer, [Intractability results for integration in tensor product spaces](https://arxiv.org/abs/2404.17163), arXiv:2404.17163. Section 5.2 compares related classes of infinitely smooth functions.

## Status review

The 2026 survey explicitly leaves this integration question open. A curse is known for uniform approximation on the same class, but this does not imply a lower bound for integration. The latter is known not to have dimension-independent complexity; that weaker fact does not establish exponential growth.

The related tensor-product integration results in [2] use finite-summability derivative norms and, for the analytic examples, positive quadrature formulas. Its Section 5.2 explicitly distinguishes the unresolved supremum derivative norm. These restrictions prevent treating those results as a solution here.

Checks through 24 September 2026 found no matching announced solution or catalogue duplicate. Searches covered the current literature and arXiv, author publications, public GitHub and Palomar. Zenodo's native API was inaccessible, and indexed Zenodo searches found no matching announcement. The accompanying numerical-journal review records scope and access limits.
