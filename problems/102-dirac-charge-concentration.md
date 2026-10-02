# 102. Concentration of nuclear charge minimizes the Dirac gap level

**Area:** Relativistic quantum chemistry

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}`$, $`\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix}`$, $`\sigma_3=\mathop{\mathrm{diag}}\nolimits(1,-1)`$ be the Pauli matrices, $`\alpha_j=\begin{pmatrix}0&\sigma_j\\\sigma_j&0\end{pmatrix}`$, and $`\beta=\mathop{\mathrm{diag}}\nolimits(I_2,-I_2)`$. Let $`\mu`$ be a nonnegative finite Borel measure on $`\mathbb R^3`$ with mass $`\nu\in(0,1)`$, and set

```math
D_\mu=-i\alpha\cdot\nabla+\beta-V_\mu,\qquad V_\mu(x)=\int\frac{d\mu(y)}{|x-y|}.
```

Define its first upper/lower-spinor min–max level by

```math
\lambda_1(\mu)=\inf_{0\ne\varphi\in C_c^\infty(\mathbb R^3;\mathbb C^2)}\ \sup_{\chi\in C_c^\infty(\mathbb R^3;\mathbb C^2)}\frac{\langle(\varphi,\chi),D_\mu(\varphi,\chi)\rangle}{\|\varphi\|_2^2+\|\chi\|_2^2}.
```

Prove or disprove $`\lambda_1(\mu)\ge\sqrt{1-\nu^2}`$. The right side is the gap eigenvalue for $`\mu=\nu\delta_0`$; the assertion also prevents this first level from diving into the negative continuum.

## Application

It asks whether concentrating a fixed subcritical nuclear charge at one point produces the lowest relativistic electronic energy, a basic comparison for heavy nuclei and multi-center models.

## References

1. M. J. Esteban, M. Lewin and É. Séré, [Dirac–Coulomb operators with general charge distribution II. The lowest eigenvalue](https://arxiv.org/abs/2003.04051), Proceedings of the London Mathematical Society 123 (2021), §2.3, Conjecture 1, equation (30): exact charge-concentration conjecture.
2. M. J. Esteban, M. Lewin and É. Séré, [Dirac–Coulomb operators with general charge distribution I. Distinguished extension and min-max formulas](https://arxiv.org/abs/2003.04004), preprint (2020), distinguished realization and min–max framework.

## Status review

**Known cases:** The displayed Dirac-level lower bound is established for radially symmetric charge measures.

**Remaining target:** The lower bound for every nonnegative charge measure of mass strictly between zero and one.

**Literature check:** Open in cited literature; no later resolution located.

Part II proves existence and singular support properties of an optimizing charge measure below a critical coupling, not that the optimizer is a point mass. Radially symmetric measures are an established case. The search found no general resolution or improvement that establishes the displayed bound for every charge distribution of mass below one.

**Search audit:** “Dirac Coulomb general charge distribution optimal delta conjecture”; “Dirac charge concentration lowest eigenvalue 2025 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
