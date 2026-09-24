# 623. Low-degree representations determining a unitary shuffle's gap

**Area:** Random unitary sampling and spectral analysis

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $n\ge2$ and assign nonnegative weights $w_B$ to the nonempty subsets $B\subseteq[n]$. Assume connectivity of the graph joining vertices that share a positive-weight subset. Let $U_B\le U(n)$ consist of matrices acting as the identity outside the coordinate subspace indexed by $B$, with normalized Haar measure $m_B$.

For each nontrivial irreducible unitary representation $\rho$ of $U(n)$, define the positive semidefinite matrix

$$
A_\rho=\sum_Bw_B\left(I-\int_{U_B}\rho(V)\,dm_B(V)\right).
$$

Set $\gamma=\inf_{\rho\ne\mathbf1}\lambda_{\min}(A_\rho)$. This is the spectral gap of the process that, at rate $w_B$, multiplies its current unitary matrix by an independent Haar element of $U_B$.

Write $\rho_1,\rho_2$ for the irreducible representations with highest weights $(1,0,\ldots,0,-1)$ and $(2,0,\ldots,0,-2)$, respectively; for $n=2$ the weights are $(1,-1)$ and $(2,-2)$. Prove or disprove

$$
\gamma=\min\{\lambda_{\min}(A_{\rho_1}),\lambda_{\min}(A_{\rho_2})\}.
$$

## Application

This would identify the slowest mode of block-Haar unitary sampling using just two finite representations, aiding quantitative analysis of random quantum operations.

## References

1. G. Alon and D. Puder, [Aldous-type Spectral Gaps in Unitary Groups](https://arxiv.org/abs/2603.00353), 2026, Section 1.2, Conjecture 1.7 and Theorem 1.5.
2. P. Caputo, M. Quattropani and F. Sau, [Aldous' spectral gap phenomena in stochastic exchange models](https://arxiv.org/abs/2609.10450), September 2026, Section 1.4.6.
3. S. Kim and F. Sau, [Spectral gap of the symmetric inclusion process](https://doi.org/10.1214/24-AAP2085), *Annals of Applied Probability* **34** (2024), 4899–4920. Journal discovery route through related exchange models.

## Status review

**Known cases:** Reference [1] proves the assertion for weights supported on subsets of size at least $n-1$, among other special cases.

**Remaining target:** All connected weighted hypergraphs. Reference [2] explicitly retains Conjecture 1.7. It solves the separate KMP two-particle identity, which does not establish this assertion about every unitary representation.

Current announcement and duplicate checks found no matching solution.
