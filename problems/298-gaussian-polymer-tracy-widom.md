# 298. Tracy–Widom fluctuations for a Gaussian lattice polymer at fixed temperature

**Area:** Random media and fluctuating interfaces

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

Let $(\omega_{ij})_{i,j\ge0}$ be independent standard normal variables. Let $\Pi_n$ be all up-right lattice paths from $(0,0)$ to $(n,n)$ and set $Z_n=\sum_{\pi\in\Pi_n}\exp(\sum_{v\in\pi}\omega_v)$, with each visited vertex counted once. Write $f=\lim_{n\to\infty}n^{-1}\mathbb E\log Z_n$, whose existence is known. Does there exist $s>0$ such that $(\log Z_n-nf)/(s n^{1/3})$ converges in distribution to the standard GUE Tracy–Widom law $F_2$? Here $F_2$ is the limit law of $N^{2/3}(\lambda_{\max}(M_N)-2)$ for complex Hermitian Gaussian matrices with density proportional to $\exp(-N\operatorname{Tr}M_N^2/2)$. The noise coefficient remains one as $n$ grows.

## Applied significance

This is a concrete universality prediction for the energy fluctuations of a polymer in a disordered medium.

## References

- [Arjun Krishnan and Jeremy Quastel, *Tracy–Widom fluctuations for perturbations of the log-gamma polymer in intermediate disorder* (2016)](https://arxiv.org/abs/1610.06975), Introduction and universality conjecture.
- [Pranay Agarwal, *Improved universality bounds for directed polymers in the intermediate disorder regime* (2025)](https://arxiv.org/abs/2509.21453), temperature scaling and moment-matching assumptions.
- [Sen Mu, Abbas Ali Saberi, Roderich Moessner and Mehran Kardar, *Directed Polymer Transfer Matrices as a Unified Generator of Distinct One-Point Fluctuation Laws* (2026)](https://arxiv.org/abs/2603.14477), numerical study.

## Status review

Intermediate-disorder theorems send the noise strength to zero and often impose moment matching with an integrable law. The 2026 transfer-matrix paper reports numerical fluctuation laws. Neither proves the fixed-temperature, square-geometry Gaussian assertion. This differs from entry 200, which concerns a continuum polymer’s moment spectrum.

Search topics checked on 2026-09-13: `Gaussian lattice directed polymer fixed temperature Tracy Widom universality proof 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
