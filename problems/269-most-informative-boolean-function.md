# 269 — The most informative Boolean function conjecture

**Area:** Information theory / noisy one-bit compression

## Problem statement

For every integer $n\geq1$, let $X$ be uniform on $\{0,1\}^n$ and let $Y=X\oplus Z$, where the coordinates of $Z$ are independent Bernoulli$(\delta)$ variables independent of $X$, with $0\leq\delta\leq1/2$. Is

$$
I(f(X);Y)\leq1-h_2(\delta)
$$

true for every $f:\{0,1\}^n\to\{0,1\}$? Here $h_2(p)=-p\log_2p-(1-p)\log_2(1-p)$, with $0\log_2 0=0$, and $I(U;V)=H(U)+H(V)-H(U,V)$ is mutual information in bits. A coordinate projection $f(X)=X_i$ attains the proposed bound.

## Applied significance

This determines how much information a single retained bit can preserve about a noisy binary signal, with applications to compression and information bottlenecks.

## References

1. T. A. Courtade and G. R. Kumar, *Which Boolean Functions Maximize Mutual Information on Noisy Inputs?* (2014), [IEEE TIT 60, 4515–4525](https://doi.org/10.1109/TIT.2014.2326877); [author manuscript](https://people.eecs.berkeley.edu/~courtade/pdfs/CourtadeKumar_TransITAug2014.pdf), Conjecture 1. Original statement.
2. A. Samorodnitsky, *The “Most informative boolean function” conjecture holds for high noise* (2015), [arXiv:1510.08656](https://arxiv.org/abs/1510.08656), main theorem. Proves a dimension-independent neighborhood of $\delta=1/2$.
3. Z. Chen, A. Gohari and C. Nair, *A Differential Equation Approach to the Most-Informative Boolean Function Conjecture* (2025; revised 5 August 2026), [arXiv:2502.10019v2](https://arxiv.org/abs/2502.10019v2), §I and Conjecture 1. Keeps the full question open while reducing a balanced case to additional inequalities.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

Searches included “most informative Boolean conjecture proof 2026”, “Courtade Kumar solved”, and the Chen–Gohari–Nair title. An older [2015 manuscript by M. Kesal](https://arxiv.org/abs/1511.01828) claims a proof, but the cited August 2026 primary work still treats the conjecture as unresolved. No independently established resolution of that discrepancy was located; the status here follows the later specialist literature, without certifying or refuting the old manuscript.
