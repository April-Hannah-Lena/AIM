# 109. A sharp universal inequality for clamped-plate eigenvalues

**Area:** Elastic vibration

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For every bounded connected smooth domain $\Omega\subset\mathbb R^d$, $d\ge2$, let $0<\Gamma_1\le\Gamma_2\le\cdots$ be the eigenvalues, with multiplicity, of

$$\Delta^2u=\Gamma u\text{ in }\Omega,\qquad u=\partial_nu=0\text{ on }\partial\Omega.$$

Prove or disprove, for every integer $k\ge1$,

$$\sum_{i=1}^k(\Gamma_{k+1}-\Gamma_i)^2\le\frac8d\sum_{i=1}^k(\Gamma_{k+1}-\Gamma_i)\Gamma_i.$$

The constant is required to be independent of the domain and of $k$.

## Application

This would constrain every higher vibration frequency of a clamped elastic plate from lower frequencies, without detailed knowledge of its shape.

## References

1. D. Chen, Q.-M. Cheng and G. Wei, [A gap for eigenvalues of a clamped plate problem](https://arxiv.org/abs/1610.05889), preprint (2016), Conjecture 1.1, equation (1.6): exact proposed inequality.
2. Z. Ji, [Upper and lower bounds for the eigenvalues of the clamped plate problem on Riemannian manifolds](https://doi.org/10.1016/j.jmaa.2026.130442), Journal of Mathematical Analysis and Applications (2026), introduction and main estimates: subsequent eigenvalue-bound research.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The source contrasts the requested coefficient $8/d$ with the established coefficient $8(d+2)/d^2$. Later gap and averaged-energy estimates concern different inequalities. Searches found no result replacing that coefficient by $8/d$ for all Euclidean domains and all indices.

**Search audit:** “Cheng Yang clamped plate universal inequality conjecture 8 n”; “clamped plate Conjecture 1.1 2025 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
