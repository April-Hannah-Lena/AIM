# 270 — The exact zero-error Shannon capacity of the seven-cycle

**Area:** Zero-error communication / combinatorial coding

## Problem statement

Let $C_7$ have vertex set $\mathbb Z/7\mathbb Z$, with distinct vertices adjacent when their difference is $\pm1$. For $k\geq1$, let $a_k$ be the largest size of a set $\mathcal C\subset(\mathbb Z/7\mathbb Z)^k$ such that any distinct $x,y\in\mathcal C$ have some coordinate $i$ with $x_i-y_i\notin\{0,1,-1\}$ modulo seven.

Determine exactly

$$
\Theta(C_7)=\sup_{k\geq1}a_k^{1/k}.
$$

Equivalently, $a_k$ is the independence number of the $k$-fold strong graph power. The corresponding zero-error rate is $\log_2\Theta(C_7)$ bits per channel use.

## Applied significance

The seven symbols model a channel where neighboring symbols can be confused. This asks for the best asymptotic rate when decoding errors are forbidden.

## References

1. L. Lovász, *On the Shannon capacity of a graph* (1979), [IEEE TIT 25, 1–7](https://doi.org/10.1109/TIT.1979.1055985), odd-cycle discussion and theta-function upper bound. Supplies the classical bound and solves the contrasting five-cycle case.
2. R. Tandon, *Strengthening Recursive Constructions for Zero-Error Shannon Capacity* (31 August 2026), [arXiv:2608.30273](https://arxiv.org/abs/2608.30273), abstract and $C_7$ construction. Explicitly states that exact capacities of odd cycles beyond $C_5$ remain unknown and reports a new lower bound.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

The 2026 preprint reports $\Theta(C_7)\geq3.25883262\ldots$, still below the classical upper bound $7\cos(\pi/7)/(1+\cos(\pi/7))$. Searches included “C7 Shannon capacity exact 2026”, “seven cycle capacity September 2026”, and “Tandon recursive Shannon capacity”. Recent improvements construct larger finite-block codes; no matching converse or exact capacity was located.
