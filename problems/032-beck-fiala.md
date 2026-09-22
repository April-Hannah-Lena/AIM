# 032. The Beck–Fiala discrepancy conjecture

**Area:** Sparse constraint rounding

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Is there a universal constant $C$ with the following property? For every finite set $X$, every family $\mathcal F\subseteq2^X$, and every integer $t\ge1$ such that each element of $X$ belongs to at most $t$ members of $\mathcal F$, there is a coloring $\epsilon:X\to\{-1,1\}$ satisfying
$$\left|\sum_{x\in S}\epsilon(x)\right|\le C\sqrt t\quad\text{for every }S\in\mathcal F.$$
All sparsity regimes, including small $t$ relative to $|X|$, are included.

## Application

Sparse allocation and scheduling models often let each decision affect only a few constraints. The conjecture predicts the sharp order of rounding error based on that local participation count.

## References

1. N. Bansal and H. Jiang, [Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk](https://arxiv.org/abs/2508.03961), 2025; STOC 2026. Major progress for large degree.
2. D. J. Altschuler and K. Tikhomirov, [Online Beck–Fiala Down to Logarithmic Sparsity](https://arxiv.org/abs/2607.14238), 2026. Further progress down toward logarithmic degree.

## Status review

**Known cases:** The cited large-degree results establish the conjectured square-root discrepancy bound down toward logarithmic sparsity.

**Remaining target:** A universal square-root bound in every sparsity regime, including the smaller degrees not covered by those results.

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The July 2026 preprint extends the proved degree regime to $t\ge(\log|X|)^{1+o(1)}$. It does not establish the full conjecture for all smaller degrees. This entry retains the universal offline statement, not a now-proved large-degree or online-Spencer subproblem.

Searches included: `Beck-Fiala conjecture 2026 solved`; `Online Beck-Fiala Down Logarithmic Sparsity`; `Beck Fiala small degree open`. This is a documented literature check, not a certification that no solution exists.
