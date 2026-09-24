# 289. Is the variance of fair binary sequence alignment linear?

**Area:** Uncertainty in sequence similarity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $X_1,\ldots,X_n$ and $Y_1,\ldots,Y_n$ be independent fair binary strings. Let $L_n$ be the largest $k$ for which indices $i_1<\cdots<i_k$ and $j_1<\cdots<j_k$ in $\{1,\ldots,n\}$ satisfy $X_{i_r}=Y_{j_r}$ for all $r$. Is there a constant $c>0$ such that $\operatorname{Var}(L_n)\ge cn$ for every sufficiently large $n$? A matching upper bound of order $n$ is known. A negative answer would also resolve this formulation of the linear-variance question.

## Application

Fluctuation size controls the calibration of significance tests for an observed alignment score under a random-sequence null model.

## References

- [Jüri Lember and Heinrich Matzinger, *Standard deviation of the longest common subsequence*, Annals of Probability 37 (2009)](https://math.ut.ee/sites/default/files/inline-files/08-aop436.pdf), Introduction and biased binary result.
- [Qingqing Liu, *Topics on the Longest Common Subsequences: Simulations, Computations, and Variance*, Georgia Institute of Technology dissertation (2018)](https://repository.gatech.edu/bitstreams/0312a292-44ee-435a-8440-7ce2883e6704/download), Chapter 1 and §3.1.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Linear lower bounds for sufficiently biased strings and asymmetric or dependent models do not cover two independent fair binary strings. Competing fluctuation predictions make the unbiased case a question, rather than an asserted established scaling law. Entry 280 instead concerns the limiting mean coefficient.

Search topics checked on 2026-09-13: `unbiased fair binary longest common subsequence linear variance Waterman conjecture solved 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
