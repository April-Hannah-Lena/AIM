# 567. Maximal gain from randomization with nonadaptive linear measurements

**Area:** Information-based complexity and randomized approximation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $S:X\to Y$ be a bounded linear operator between real Banach spaces. Inputs lie in the closed unit ball $B_X$. A deterministic nonadaptive algorithm has the form
$$A(x)=\Phi(\lambda_1(x),\ldots,\lambda_n(x)),$$
where $\lambda_j\in X'$ are fixed continuous linear functionals and $\Phi:\mathbb R^n\to Y$ is unrestricted. Define
$$e_n^{\rm det}(S)=\inf_A\sup_{x\in B_X}\|Sx-A(x)\|_Y.$$
A randomized nonadaptive algorithm chooses such a complete measurement list and reconstruction using a random seed $\omega$ independently of the input. Require the error to be jointly measurable, and set
$$e_n^{\rm ran}(S)=\inf_{(A_\omega)}\sup_{x\in B_X}\mathbb E_\omega\|Sx-A_\omega(x)\|_Y.$$
Every realization uses at most $n$ measurements. The error criterion is expected norm, not root-mean-square norm.

For a nonnegative sequence $u=(u_n)$ define
$$\operatorname{rate}(u)=\sup\{\alpha\ge0:u_n=O(n^{-\alpha})\}.$$
Determine the maximal increase
$$G=\sup_S\left[\operatorname{rate}(e_n^{\rm ran}(S))-\operatorname{rate}(e_n^{\rm det}(S))\right],$$
where the supremum is over bounded operators between real Banach spaces with finite rates. Current results give $1/2\le G\le1$. In particular, can nonadaptive randomization improve the polynomial rate by strictly more than $1/2$?

## Application

The answer quantifies the strongest possible information savings from randomly choosing a fixed batch of linear measurements. This distinguishes benefits of random sensing from benefits that require feedback and adaptive measurement selection.

## References

1. D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica* **35** (2026), 273–457. Section 9.1 defines the error model; Section 10.2, equation (10.10), states the gap.
2. D. Krieg, E. Novak and M. Ullrich, [On the power of adaption and randomization](https://doi.org/10.1017/fms.2025.10101), *Forum of Mathematics, Sigma* **13** (2025), e152. Section 6.1.
3. R. J. Kunsch and M. Wnuk, [Adaptive and non-adaptive randomized approximation of high-dimensional vectors](https://arxiv.org/abs/2410.23067), *Journal of Approximation Theory* (2026), 106318. [DOI](https://doi.org/10.1016/j.jat.2026.106318).

## Status review

The lower bound $1/2$ comes from Sobolev approximation examples. The general upper bound of one is known, and gains of one are attainable when adaptive randomized measurements are allowed. Those adaptive examples do not settle this nonadaptive question. The vector-approximation results in [3] are among the advances already incorporated in the 2026 survey.

Current arXiv and author-publication checks found no solution of this remaining gap. Public GitHub and Palomar searches found no matching announcement; Zenodo's API returned an access denial, and indexed searches found none. The accompanying numerical-journal review records the checked sources and limitations. No equivalent existing catalogue entry was found.
