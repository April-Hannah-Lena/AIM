# 016. Localization at every disorder strength in two dimensions

**Area:** Disordered quantum transport

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

On $\ell^2(\mathbb Z^2)$ let

$$
(H_\eta\psi)(n)=\sum_{|m-n|_1=1}\psi(m)+\eta V_n\psi(n),
$$

where the $V_n$ are independent uniform variables on $[-1,1]$. Prove or disprove that for every fixed $\eta>0$, almost surely $H_\eta$ has a complete orthonormal basis of exponentially decaying eigenfunctions. Explicitly, each basis vector $\phi$ must satisfy $|\phi(n)|\le C_\phi e^{-c_\phi|n-n_\phi|}$ for some $C_\phi,c_\phi>0$ and $n_\phi\in\mathbb Z^2$. No uniform decay rate across all eigenvalues is demanded.

## Application

This would establish whether arbitrarily weak disorder ultimately localizes all single-particle states in a two-dimensional material, despite apparently extended behavior at accessible finite scales.

## References

1. B. Simon, [Schrödinger operators in the twenty-first century](https://web.ma.utexas.edu/mp_arc-bin/mpa?yn=00-78), in Mathematical Physics 2000 (2000), Problem 2.
2. F. Hernández, [Lecture notes on Quantum Diffusion and Random Matrix Theory](https://arxiv.org/abs/2511.04380), preprint (2025), §1, two-dimensional localization discussion.
3. J. Šuntajs, T. Prosen and L. Vidmar, [Localization challenges quantum chaos in the finite two-dimensional Anderson model](https://arxiv.org/abs/2212.10625), Physical Review B 107 (2023), 064205, numerical investigation.

## Status review

**Known cases:** Exponential localization is established in the strong-disorder regime of the stated Anderson model.

**Remaining target:** Localization throughout the spectrum at every positive disorder strength, including arbitrarily weak disorder.

**Literature check:** Open in cited literature; no later resolution located.

The 2025 notes explicitly leave bulk localization in d=2 conjectural. Strong-disorder and spectral-edge localization do not cover every energy at weak disorder. The numerical study emphasizes finite-size effects; it cannot decide the stated infinite-lattice assertion. Simon's pure-point question is given here in its standard exponential-localization form.

**Search audit:** “Anderson localization two dimensions arbitrary weak disorder open 2025 2026”; “two dimensional Anderson localization proof”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
