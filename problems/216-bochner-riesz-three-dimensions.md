# 216. Sharp Bochner–Riesz summability in three dimensions

**Area:** Harmonic analysis; frequency filtering

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

For $\delta>0$ and a Schwartz function $f$ on $\mathbb R^3$, define $B^\delta f$ through its Fourier transform by
$$\widehat{B^\delta f}(\xi)=(1-|\xi|^2)_+^\delta\widehat f(\xi),\qquad r_+=\max\{r,0\}.$$
For every $1<p<\infty$ and
$$\delta>\max\left\{3\left|\frac1p-\frac12\right|-\frac12,\,0\right\},$$
does there exist $C_{p,\delta}<\infty$ such that $\|B^\delta f\|_{L^p}\le C_{p,\delta}\|f\|_{L^p}$ for all such $f$?

## Application

Bochner–Riesz means smooth a spherical frequency cutoff. The sharp threshold determines how little smoothing suffices to reconstruct a signal without unbounded amplification in the chosen integrability norm.

## References

1. Shukun Wu, [On the Bochner–Riesz operator in three dimensions](https://arxiv.org/abs/2008.13043), *J. Anal. Math.* 149 (2023), 677–718. Introduction, Conjecture 1.1 and equation (1.3), states the threshold; the main theorem covers a restricted exponent range.
2. Shaoming Guo, Changkeun Oh, Hong Wang, Shukun Wu, and Ruixiang Zhang, [The Bochner–Riesz problem: an old approach revisited](https://arxiv.org/abs/2104.11188), *Peking Math. J.* 8 (2025), 201–270. Conjecture 1.1, Theorem 1.3, and Remark 1.4 separate the conjecture from known bounds.

## Status review

**Known cases:** The cited results achieve the predicted smoothing threshold when the larger of p and its conjugate exponent is at least 13/4.

**Remaining target:** The predicted threshold for every exponent between one and infinity, including intermediate exponents not covered by those results.

**Literature check:** Open in cited literature; no later resolution located.

The cited results reach $\max\{p,p/(p-1)\}\ge13/4$ with the predicted threshold. They do not cover all intermediate exponents. Two-dimensional results and improvements for maximal or weighted variants do not establish this full three-dimensional strong-type assertion.

**Search audit:** Queries: “Bochner Riesz conjecture R3 proof 2025 2026”, “Wu Guo Oh Wang Zhang Bochner Riesz sharp range”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
