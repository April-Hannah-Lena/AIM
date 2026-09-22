# 006. Rayleigh's clamped-plate conjecture in higher dimensions

**Area:** Elasticity and fourth-order spectra

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For each integer $d\ge4$ and each bounded smooth domain $\Omega\subset\mathbb R^d$, define

$$\Gamma_1(\Omega)=\inf_{0\ne u\in H^2_0(\Omega)}\frac{\int_\Omega|\Delta u|^2\,dx}{\int_\Omega|u|^2\,dx}.$$

Here $H^2_0$ is the closure of compactly supported smooth functions in the Sobolev $H^2$ norm; for smooth boundaries it imposes $u=\partial_\nu u=0$. Prove or disprove $\Gamma_1(\Omega)\ge\Gamma_1(B)$ for a ball $B$ with $|B|=|\Omega|$.

## Application

The biharmonic eigenvalue models the fundamental clamped-plate vibration. The higher-dimensional statement tests the scope of the spectral comparison principle underlying that elastic model.

## References

1. R. Leylekian, [Sufficient conditions yielding the Rayleigh Conjecture for the clamped plate](https://arxiv.org/abs/2302.06313v2), preprint (2023), revised January 2025; abstract and main results.
2. R. Leylekian, [Towards the optimality of the ball for the Rayleigh Conjecture concerning the clamped plate](https://arxiv.org/abs/2306.15523), preprint (2023), published in Archive for Rational Mechanics and Analysis (2024).
3. A. Kristály, [Principal frequency of clamped plates on RCD(0,N) spaces: Sharpness, rigidity, and stability](https://doi.org/10.1112/plms.70079), Proceedings of the London Mathematical Society (2025), introduction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Leylekian's January 2025 version explicitly leaves d≥4 open and proves conditional results on optimal eigenfunctions. Kristály's 2025 extension concerns dimensions near two or three and does not settle the displayed Euclidean problem. Dimensions two and three are solved and deliberately excluded.

**Search audit:** “clamped plate Rayleigh conjecture dimensions 4 2025 2026”; “Rayleigh clamped plate proof higher dimension”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
