# 621. Hypergraph shuffles and the one-particle spectral gap

**Area:** Markov chains and spectral graph theory

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $n\ge2$ and give each subset $B\subseteq[n]$ with $|B|\ge2$ a weight $w_B\ge0$. Assume the graph joining vertices that share a positive-weight subset is connected.

Place one distinct label at each vertex. Independently, each $B$ rings at rate $w_B$ and uniformly permutes its labels. Let $L_{\rm IP}$ be this continuous-time generator on $S_n$. The position of one label has generator

$$
L_{\rm RW}f(x)=\sum_{B\ni x}w_B\left(\frac1{|B|}\sum_{y\in B}f(y)-f(x)\right).
$$

For either reversible chain, let $\lambda$ be the smallest positive eigenvalue of its negative generator. Prove or disprove Caputo's conjecture:

$$
\lambda_{\rm IP}=\lambda_{\rm RW}.
$$

## Application

The equality would determine the relaxation rate of a many-label block shuffle from a matrix with only $n$ states, supporting analysis of sampling algorithms with collective updates.

## References

1. G. Alon and D. Puder, [Aldous-type Spectral Gaps in Unitary Groups](https://arxiv.org/abs/2603.00353), 2026, Conjecture 1.2 and the following particle interpretation.
2. P. Caputo, M. Quattropani and F. Sau, [Aldous' spectral gap phenomena in stochastic exchange models](https://arxiv.org/abs/2609.10450), September 2026, introduction and Section 1.4.6.
3. S. Kim and F. Sau, [Spectral gap of the symmetric inclusion process](https://doi.org/10.1214/24-AAP2085), *Annals of Applied Probability* **34** (2024), 4899–4920. Journal discovery route into this family of spectral-gap questions.

## Status review

**Known cases:** Pair updates satisfy the theorem of Caputo–Liggett–Richthammer. Mean-field weights depending only on subset size and further special hypergraphs are also covered.

**Remaining target:** Arbitrary connected weighted hypergraphs. Reference [2] explicitly retains this question; its new degree-two theorem concerns other exchange models. The recent Plücker-positivity paper arXiv:2609.03746 proves particular inequalities, not this full conjecture.

Current announcement and duplicate checks found no matching resolution.
