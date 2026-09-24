# 213. GOE level spacings in a desymmetrized Sinai billiard

**Area:** Quantum chaos / wave-cavity spectra

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let

```math
\Omega=\{(x,y)\in\mathbb R^2:0<y<x<1,\quad x^2+y^2>1/4\},
```

and let $`0<\lambda_1\le\lambda_2\le\cdots`$ be the Dirichlet eigenvalues of $`-\Delta`$ on $`\Omega`$, counted with multiplicity. Set $`\mu_j=|\Omega|\lambda_j/(4\pi)`$.
Define $`F_{\mathrm{GOE}}`$ as the bulk nearest-neighbor spacing distribution of the Gaussian orthogonal ensemble: for an $`n\times n`$ real symmetric random matrix $`H_n`$, the entries above the diagonal are independent centered Gaussians of variance $`1/n`$, and diagonal entries are independent centered Gaussians of variance $`2/n`$. If $`\nu_1\le\cdots\le\nu_n`$ are its eigenvalues and $`k=\lfloor n/2\rfloor`$, then

```math
F_{\mathrm{GOE}}(s)=\lim_{n\to\infty}\mathbb P\left\{\frac n\pi(\nu_{k+1}-\nu_k)\le s\right\}.
```

Does the deterministic billiard spectrum satisfy

```math
\lim_{N\to\infty}\frac1N\#\{1\le j\le N:\mu_{j+1}-\mu_j\le s\}
=F_{\mathrm{GOE}}(s)
\quad\text{for every }s\ge0?
```

This domain is one symmetry sector of a square containing a circular obstacle; Dirichlet conditions on the symmetry cuts prevent mixing different symmetry sectors.

## Application

Sinai-type cavities model ballistic electron devices and microwave resonators. An exact spacing law would justify predicting unresolved resonance statistics from classical ray chaos and time-reversal symmetry.

## References

1. O. Bohigas, M. J. Giannoni, and C. Schmit, [*Characterization of Chaotic Quantum Spectra and Universality of Level Fluctuation Laws*](https://doi.org/10.1103/PhysRevLett.52.1), *Physical Review Letters* 52 (1984), 1–4, p. 2, Figure 1, and the conjecture on p. 3. Desymmetrized Sinai spectra and the original GOE conjecture.
2. Stéphane Nonnenmacher, [*Anatomy of Quantum Chaotic Eigenstates*](https://arxiv.org/abs/1005.5598), *Séminaire Poincaré* XIV (2010); reprinted in *Chaos: Poincaré Seminar 2010* (2013), §4.1. Discusses the unresolved random-matrix conjecture alongside eigenfunction statistics.
3. Javier M. Magan and Qingyue Wu, [*Two types of quantum chaos: testing the limits of the Bohigas–Giannoni–Schmit conjecture*](https://arxiv.org/abs/2411.08186), preprint (2024), abstract and discussion. Examines limits of broader formulations using other Hamiltonian models.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This is a fixed, explicitly desymmetrized Sinai instance of the BGS prediction. The original paper supplies numerical evidence; it does not prove the high-energy limit. Later constructions questioning an unrestricted relation between eigenbasis chaos and spectral statistics do not establish a counterexample for this Dirichlet billiard. $`F_{\mathrm{GOE}}`$ denotes the exact infinite-matrix spacing law, rather than the closely fitting two-by-two Wigner formula.

**Search audit:** Searched “Sinai billiard GOE conjecture rigorous proof 2026”, “Bohigas Giannoni Schmit nearest neighbor solved”, and later proof/counterexample discussions, including the 2024 Magan–Wu preprint. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
