# 012. The sharp planar Pleijel constant

**Area:** Nodal domains and spectral complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $\Omega\subset\mathbb R^2$ be any bounded connected domain with piecewise smooth Lipschitz boundary. Choose any real orthonormal Dirichlet eigenbasis $(u_k)$, ordered by nondecreasing eigenvalue with multiplicity. Let $\nu(u_k)$ be the number of connected components of $\Omega\setminus\{u_k=0\}$. Prove or disprove

$$\limsup_{k\to\infty}\frac{\nu(u_k)}{k}\le\frac2\pi.$$

The assertion is uniform in the choice of domain and eigenbasis. The proposed constant is attained asymptotically by rectangular examples.

## Application

This would give the optimal asymptotic bound on how many sign-coherent vibration cells a planar mode can contain, improving complexity estimates based on Courant’s theorem.

## References

1. I. Polterovich, [Pleijel's nodal domain theorem for free membranes](https://arxiv.org/abs/0805.1553), Proceedings of the AMS 137 (2009), 1021–1024, concluding discussion.
2. V. Bobkov, [On exact Pleijel's constant for some domains](https://ems.press/content/serial-article-files/26416), Documenta Mathematica 23 (2018), 799–813, introduction, p. 800.
3. X. Han, [Notes on nodal sets (Section 4.1)](https://www.csun.edu/~xiaolong/Han_Pblm.pdf), author notes, §4.1, p. 59 (online text consulted September 2026).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Bobkov explicitly records the 2/π conjecture and the sharp rectangular examples. Han's notes retain it as the conjectural constant. Improvements below the classical 4/j₀,₁² bound and Pleijel theorems for other operators do not attain 2/π in this class.

**Search audit:** “Pleijel Polterovich 2/pi conjecture 2025 2026”; “sharp Pleijel constant proof”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
