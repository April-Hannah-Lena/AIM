# 005. Does the disk minimize the third Dirichlet eigenvalue?

**Area:** Spectral shape optimization

## Problem statement

Let $A>0$. For every bounded open set $\Omega\subset\mathbb R^2$ with $|\Omega|=A$, let $\lambda_3(\Omega)$ denote the third Dirichlet eigenvalue of $-\Delta$, counted with multiplicity. Let $B$ be the disk of area $A$. Prove or disprove

$$\lambda_3(\Omega)\ge\lambda_3(B)=\frac{\pi j_{1,1}^2}{A},$$

where $j_{1,1}$ is the first positive zero of the Bessel function $J_1$. Disconnected competitors are allowed.

## Applied significance

The problem seeks the lowest possible third resonant frequency at a fixed material area, a basic benchmark for numerical membrane optimization.

## References

1. R. S. Laugesen (problem proposer), [Open problems from the miniconference on sharp eigenvalue estimates for partial differential operators](https://publish.illinois.edu/eigenvalues2020/files/2020/04/Open-problems.pdf), April 2020, Open Problem 1.
2. A. V. Penskoi, [Extremal metrics for eigenvalues of the Laplace–Beltrami operator on surfaces](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=9565&what=fullteng), Russian Mathematical Surveys 68 (2013), 1073–1130, introductory discussion, p. 1076.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08.

The 2020 problem list explicitly asks the planar inequality. The survey describes the disk as the conjectural third-eigenvalue minimizer. Searches located optimization numerics and related magnetic problems, but no proof or counterexample for the stated nonmagnetic planar problem. Neither the Faber–Krahn theorem for λ₁ nor the two-disk theorem for λ₂ answers it.

**Search audit:** “third Dirichlet eigenvalue disk minimization conjecture 2025 2026”; “third Dirichlet eigenvalue disk proof counterexample”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
