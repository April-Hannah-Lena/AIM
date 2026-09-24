# 545. Mixing time of the reflected Burnside sampler for integer partitions

**Area:** Monte Carlo sampling and statistical computation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $\mathcal P_n$ be the set of integer partitions of $n\ge2$, and let $u_n$ be its uniform probability measure. Define a Markov kernel $Q_n$ by the following step from $\lambda\in\mathcal P_n$:

1. Transpose the Young diagram of $\lambda$, obtaining the conjugate partition $\lambda^{\mathsf T}$.
2. Choose any permutation $\sigma\in S_n$ with cycle type $\lambda^{\mathsf T}$, and sample $\tau$ uniformly from its centralizer
   $$C_{S_n}(\sigma)=\{\tau\in S_n:\tau\sigma=\sigma\tau\}.$$
3. Return the cycle type of $\tau$.

The resulting kernel is independent of the representative $\sigma$ and has stationary distribution $u_n$. Define its worst-case total-variation mixing time by
$$t_n=\min\left\{t\in\mathbb N_0:\max_{\lambda\in\mathcal P_n}\frac12\sum_{\mu\in\mathcal P_n}\left|Q_n^t(\lambda,\mu)-\frac1{|\mathcal P_n|}\right|\le\frac14\right\}.$$

Determine the asymptotic order of $t_n$ as $n\to\infty$. In particular, is $t_n=O(\log n)$? This asks about the distribution of the entire partition, uniformly over starting states.

## Application

A mixing bound would give a justified run length for approximate uniform partition sampling and quantify how a deterministic transposition accelerates a Monte Carlo method.

## References

1. P. Diaconis and M. Howes, [Random sampling of contingency tables and partitions: Two practical examples of the Burnside process](https://doi.org/10.1007/s11222-025-10708-5), Statistics and Computing **35**, 181 (2025), §§4.2–4.3; [author version](https://arxiv.org/abs/2503.02818v2).
2. M. Howes, [Limit Profiles and Cutoff for the Burnside Process on Sylow Double Cosets](https://doi.org/10.1007/s10959-026-01488-3), Journal of Theoretical Probability **39**, 29 (2026).

## Status review

Reference [1] leaves a quantitative explanation of the reflected chain's speed open. Its numerical observations motivate the logarithmic question; they do not establish a worst-case total-variation bound. The formulation above makes that distinction explicit.

Reference [2] treats a different group action. Recent binary, set-partition and dual Burnside results likewise do not supply the stated bound. The review found no matching solution announcement as of the check date; author-dissertation access remains a stated search limitation.
