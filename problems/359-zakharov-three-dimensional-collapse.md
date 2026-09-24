# 359. Finite-time Langmuir collapse for the three-dimensional Zakharov system

**Area:** Plasma physics; coupled dispersive equations

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Do there exist smooth rapidly decaying initial data $u_0:\mathbb R^3\to\mathbb C$, $n_0,n_1:\mathbb R^3\to\mathbb R$ for which the Zakharov system

$$
i\partial_tu-\Delta u=nu,\qquad\partial_{tt}n-\Delta n=-\Delta|u|^2,\qquad (u,n,\partial_tn)|_{t=0}=(u_0,n_0,n_1)
$$

has a finite maximal energy-space existence time $T_+<\infty$ and

$$
\limsup_{t\uparrow T_+}\left(\|u(t)\|_{H^1}+\|n(t)\|_{L^2}+\|\partial_tn(t)\|_{\dot H^{-1}}\right)=\infty?
$$

Here $\|g\|_{\dot H^{-1}}=\||D|^{-1}g\|_2$ and all norms are on $\mathbb R^3$. Unbounded growth only as $t\to\infty$ does not answer the question.

## Application

This coupled wave–Schrödinger model describes concentration of Langmuir waves and ion-density response. A finite-time singularity would rigorously identify wave collapse in the physical three-dimensional system.

## References

1. Z. Guo, K. Nakanishi and S. Wang, [*Global dynamics below the ground state energy for the Klein–Gordon–Zakharov system in the 3D radial case*](https://arxiv.org/abs/1304.3570), Communications in Partial Differential Equations 39 (2014), introduction, comparison with the Schrödinger–Zakharov system and its open finite-time blowup problem.
2. Z. Guo and K. Nakanishi, [*Global dynamics above the ground state energy for the 3D Zakharov system*](https://arxiv.org/abs/2608.14993), preprint (2026), §1, equation (1.1), and Theorems 1.1–1.3.
3. V. Masselin, [*A Result on the Blow-up Rate for the Zakharov System in Dimension 3*](https://doi.org/10.1137/S0036141099363687), SIAM Journal on Mathematical Analysis 33 (2001), 440–447, blowup-rate criterion conditional on a finite blowup time.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using three-dimensional Zakharov finite-time collapse, finite-energy blowup, and the August 2026 Guo–Nakanishi paper. That paper still allows finite or infinite time in its growup alternative. Blowup constructions for the two-dimensional system, the four-dimensional energy-critical system, the Klein–Gordon–Zakharov system, and Zakharov systems with extra nonlinearities have different equations or dimensions. The SIAM rate theorem assumes finite-time blowup rather than constructing it. No matching three-dimensional construction was located.
