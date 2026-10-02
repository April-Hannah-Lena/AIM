# 551. Polynomial-time Bernoulli group testing at the information threshold

**Area:** High-dimensional inference and computational statistics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix $`\theta\in(0,1)`$ and $`\varepsilon>0`$, and let $`k=\lfloor n^\theta\rfloor`$. Choose an unknown infected set $`S\subseteq\{1,\ldots,n\}`$ uniformly among the sets of size $`k`$. Independently form a binary testing matrix $`X\in\{0,1\}^{N\times n}`$ with independent entries of success probability

```math
q=1-2^{-1/k},\qquad N=\left\lceil(1+\varepsilon)\log_2\binom nk\right\rceil.
```

The noiseless outcome of test $`a`$ is

```math
Y_a=\boldsymbol1\{\text{some }i\in S\text{ has }X_{ai}=1\}.
```

For every fixed $`\theta`$ and $`\varepsilon`$ as above, does there exist a possibly randomized decoder, with running time polynomial in $`n`$, which receives $`(X,Y,k)`$ and returns a set $`\widehat S`$ of size $`k`$ such that

```math
\frac{|\widehat S\triangle S|}{k}\xrightarrow{\mathbb P}0\qquad(n\to\infty)?
```

Probability is over the infected set, testing matrix and decoder randomness. The polynomial and algorithm may depend on the fixed parameters $`\theta,\varepsilon`$. The design is prescribed; the decoder cannot replace it with another pooling scheme.

This asks whether polynomial-time approximate recovery can approach the Bernoulli design's information threshold with an arbitrarily small fixed multiplicative overhead. It does not request exact support recovery or success with literally zero overhead.

## Application

Group testing economizes on pooled diagnostic tests and sparse-identification measurements. The question asks whether the statistically optimal sample count is attainable with feasible decoding for a particularly simple independent pooling design.

## References

1. M. Lovig and I. Zadik, [On the MCMC performance in Bernoulli group testing and the random max-set cover problem](https://doi.org/10.1214/25-AAP2290), *The Annals of Applied Probability* **36**(3) (2026),2626–2679. Introduction and model; [author preprint](https://arxiv.org/html/2410.09231v2), Sections1–2.
2. A. Coja-Oghlan, O. Gebhard, M. Hahn-Klimroth, A. S. Wein and I. Zadik, [Statistical and Computational Phase Transitions in Group Testing](https://proceedings.mlr.press/v178/coja-oghlan22a.html), COLT2022, PMLR178. Bernoulli-design computational gap and low-degree detection bounds.
3. F. Iliopoulos and I. Zadik, [Group testing and local search: is there a computational-statistical gap?](https://proceedings.mlr.press/v134/iliopoulos21a.html), COLT2021, PMLR134.

## Status review

The 2026 journal article retains the polynomial-time decoding question. Exhaustive search attains approximate recovery above the information threshold. The cited separate-list decoder needs a multiplicative test overhead $`1/\log 2`$; results for specially designed pools do not remove the gap for independent Bernoulli tests.

The source rules out a proposed family of low-temperature Markov-chain methods in a sufficiently sparse regime and disproves an earlier first-moment landscape prediction. These are algorithm-class restrictions, not a lower bound against every polynomial-time decoder. The low-degree result in2 is also a restricted computational obstruction, stated for detection.

The September2026 graph-aware testing preprint arXiv:2609.20418 assumes localized infections on a contact graph and gives order-level guarantees; it does not resolve the sharp constant for the uniform-size prior here. Checks through24September2026 found no matching solution announcement or repository duplicate. Native Palomar and exact-source GitHub searches returned no matching records. Zenodo's API was unavailable; indexed searches found no matching announcement. See the batch review for the search scope.
