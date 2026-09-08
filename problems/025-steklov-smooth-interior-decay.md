# 025. Exponential interior decay for smooth Steklov domains

**Area:** Boundary waves and harmonic extension

## Problem statement

Let $\Omega\subset\mathbb R^2$ be any bounded connected domain with $C^\infty$ boundary. Let $u_j$ be Steklov eigenfunctions satisfying $\Delta u_j=0$ in $\Omega$, $\partial_\nu u_j=\sigma_j u_j$ on $\partial\Omega$, and $\|u_j\|_{L^2(\partial\Omega)}=1$, with $\sigma_j\to\infty$. Is it true that, for every compact $K\subset\Omega$, there are constants $C_K,c_K>0$, independent of $j$ and of the choice of normalized eigenfunction, such that

$$\sup_{x\in K}|u_j(x)|\le C_K e^{-c_K\sigma_j}?$$

Prove the estimate in this smooth class, or construct a smooth domain and eigenfunction sequence that violates it.

## Applied significance

The rate measures penetration of high-frequency boundary modes into an interior region and determines how accurately boundary-localized approximations neglect interior fields.

## References

1. B. Colbois, A. Girouard, C. Gordon and D. Sher, [Some recent developments on the Steklov eigenvalue problem](https://doi.org/10.1007/s13163-023-00480-3), Revista Matemática Complutense (2024), Open Question 10.4.
2. J. Galkowski and J. A. Toth, [Pointwise bounds for Steklov eigenfunctions](https://arxiv.org/abs/1611.05363), Journal of Geometric Analysis 29 (2019), 142–193.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08.

The 2024 survey asks whether exponential decay survives replacement of analytic regularity by smoothness and notes that existing analytic techniques do not decide it. Galkowski–Toth prove the analytic case. Known faster-than-any-power decay in smooth domains is weaker than the displayed exponential rate. No later answer was located.

**Search audit:** “Steklov exponential interior decay smooth conjecture 2025 2026”; “Steklov exponential decay nonanalytic counterexample”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
