# 277. Gaussian fluctuations of the optimal Euclidean traveling-salesman tour

**Area:** Spatial logistics and random optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $X_1,X_2,\ldots$ be independent uniform points in $[0,1]^2$. Let $L_n$ be the minimum Euclidean length of a closed polygonal tour visiting $X_1,\ldots,X_n$. Does $(L_n-\mathbb E L_n)/\sqrt{\operatorname{Var}(L_n)}$ converge in distribution to the standard normal law as $n\to\infty$? The tour must be globally optimal; a tour produced by a specified heuristic is not substituted for $L_n$.

## Application

A limit law would quantify uncertainty in optimal routing cost when customer locations are random.

## References

- [J. Michael Steele, *Probability and Problems in Euclidean Combinatorial Optimization*, in *Probability and Algorithms* (1992)](https://www.nationalacademies.org/read/2026/chapter/9), §8.8.
- [David Aldous and Rick Durrett, *Workshop Report: Future Directions in Probability Research* (2002)](https://www.stat.berkeley.edu/~aldous/Real-World/probrep2002.html), §1.2.
- [Sourav Chatterjee and Sanchayan Sen, *Minimal spanning trees and Stein’s method* (2013)](https://arxiv.org/abs/1307.1661), a distinct geometric optimization problem with a proved central limit theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The report explicitly poses the optimal-tour central limit question. Limit laws for spanning trees, local geometric functionals, and heuristic tours do not settle it. The normalization uses the actual variance, without adding a conjectural variance asymptotic.

Search topics checked on 2026-09-13: `optimal Euclidean traveling salesman tour central limit theorem Gaussian fluctuations proof 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
