# 022. The Robin eigenvalue ratio at fixed volume

**Area:** Robin spectra and resonator design

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Fix $d\ge2$ and $\alpha>0$. For every bounded convex smooth domain $\Omega\subset\mathbb R^d$, let $\rho_1(\Omega;\alpha)>0$ and $\rho_2(\Omega;\alpha)$ be the first two eigenvalues of $-\Delta$ with $\partial_\nu u+\alpha u=0$. If $B$ is a ball of the same volume, prove or disprove

$$\frac{\rho_2(\Omega;\alpha)}{\rho_1(\Omega;\alpha)}\le\frac{\rho_2(B;\alpha)}{\rho_1(B;\alpha)}.$$

The comparison uses the same unscaled boundary parameter and fixes volume. It must hold for all positive $\alpha$.

## Application

The inequality would identify the shape that maximally separates the first two frequencies of a membrane with elastic boundary support.

## References

1. R. S. Laugesen, [The Robin Laplacian — spectral conjectures, rectangular theorems](https://arxiv.org/abs/1905.07658), Journal of Mathematical Physics 60 (2019), 121507, Conjecture G. The present problem restricts its positive-parameter assertion to convex smooth domains.
2. G. Dai and Y. Sun, [Upper bound estimation for the ratio of the first two eigenvalues of Robin Laplacian](https://arxiv.org/abs/2511.20988v3), preprint, revised December 2025, Theorems 1.1–1.2 and discussion following them.

## Status review

**Known cases:** The cited sharp bound holds under its additional ground-state distribution condition, and its large-parameter conclusion applies to a fixed domain.

**Remaining target:** The same-volume eigenvalue-ratio bound for every positive Robin parameter and every bounded convex smooth domain.

**Literature check:** Open in cited literature; no later resolution located.

The December 2025 version imposes an additional ground-state distribution condition (its R-tilde≥R) for the sharp bound. It explicitly calls its complementary case weaker than the conjecture. The large-parameter conclusion for a fixed domain does not prove the assertion at every α>0. Laugesen's wider formulation also discusses negative parameters; results in that parameter regime do not decide this positive-parameter subcase.

**Search audit:** “Robin eigenvalue ratio PPW conjecture 2025 2026”; “Dai Sun Robin ratio theorem conditions”. Searches included proof, counterexample, and 2025–2026 updates. This is a literature search result, not a certification that no proof exists.
