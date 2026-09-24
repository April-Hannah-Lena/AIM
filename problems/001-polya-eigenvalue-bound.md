# 001. Pólya's eigenvalue inequalities

**Area:** Spectral geometry

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $d\ge2$ and let $\Omega\subset\mathbb R^d$ be a bounded connected Lipschitz domain. Write $\lambda_1\le\lambda_2\le\cdots$ for the Dirichlet eigenvalues of $-\Delta$ and $0=\mu_0<\mu_1\le\cdots$ for its Neumann eigenvalues, with multiplicity. Let $\omega_d$ be the volume of the unit ball. Prove or disprove, for every $k\ge1$,

$$\mu_k(\Omega)\le4\pi^2\left(\frac{k}{\omega_d|\Omega|}\right)^{2/d}\le\lambda_k(\Omega).$$

The target is arbitrary domains; tiling domains and balls are established special cases.

## Application

These bounds would turn the leading Weyl approximation into a rigorous bound for every vibration frequency and diffusion mode, using only volume.

## References

1. N. Filonov, M. Levitin, I. Polterovich and D. A. Sher, [Pólya's conjecture for Euclidean balls](https://doi.org/10.1007/s00222-023-01198-1), Inventiones Mathematicae (2023), introduction and main theorems.
2. The same authors, [Pólya's conjecture for Dirichlet eigenvalues of annuli](https://doi.org/10.1112/jlms.70425), Journal of the London Mathematical Society (2026), §1.
3. The same authors, [Pólya's conjecture for higher-dimensional Neumann balls](https://arxiv.org/abs/2607.29305), preprint (2026), abstract and introduction.

## Status review

**Known cases:** The inequalities are established for tiling domains and Euclidean balls; the cited 2026 work completes the higher-dimensional Neumann ball case.

**Remaining target:** Both displayed inequalities for every bounded connected Lipschitz domain in every dimension at least two.

**Literature check:** Open in cited literature; no later resolution located.

The 2023 paper states the general conjecture and proves ball cases. The 2026 annulus paper treats Dirichlet annuli. The July 2026 preprint completes the higher-dimensional Neumann ball case. None asserts the displayed inequalities for arbitrary Lipschitz domains.

**Search audit:** “Pólya conjecture Dirichlet Neumann general domains 2025 2026”; “Pólya higher dimensional Neumann balls”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.

**Repository research:** The [current programme record](../research/automated_attempts/001/STATUS.md) contains a conditional planar third-Neumann-mode route. The required simultaneous moment cancellation and overlap bound remain unproved, and the conditional analytic argument still needs independent checking. Finite algebra checks do not establish these hypotheses or resolve the all-index conjecture.
