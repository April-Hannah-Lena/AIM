# 200. The optimal Lieb–Oxford constant

**Area:** Electronic density-functional theory

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For every integer $`N\ge1`$, consider symmetric probability measures $`P`$ on $`(\mathbb R^3)^N`$ whose one-particle density $`\rho_P`$ is defined by $`\int\rho_P=N`$ and whose one-coordinate marginal has density $`\rho_P/N`$. Require $`\rho_P\in L^{4/3}(\mathbb R^3)`$ and all the following Coulomb integrals to be finite. Define

```math
E_{\rm ind}(P)=\int\sum_{i<j}\frac{1}{|x_i-x_j|}\,dP-\frac12\iint\frac{\rho_P(x)\rho_P(y)}{|x-y|}\,dx\,dy.
```

Determine the sharp universal constant

```math
C_{\rm LO}=\sup_{N,P}\frac{-E_{\rm ind}(P)}{\int_{\mathbb R^3}\rho_P(x)^{4/3}\,dx}.
```

Sharpness means both a universal inequality with this constant and admissible distributions approaching equality. No numerical conjecture for its exact value is assumed.

## Application

The constant controls how negative exchange and correlation energy can be. A sharp value would strengthen exact constraints used in electronic-structure approximations.

## References

1. M. Lewin, E. H. Lieb and R. Seiringer, [Statistical mechanics of the uniform electron gas](https://jep.centre-mersenne.org/articles/10.5802/jep.64/), Journal de l’École polytechnique — Mathématiques 5 (2018), §2, equation (2.2) and discussion: explicitly calls determination of the best constant a challenge.
2. M. Lewin, E. H. Lieb and R. Seiringer, [Improved Lieb–Oxford bound on the indirect and exchange energies](https://arxiv.org/abs/2203.12473), Letters in Mathematical Physics 112, 92 (2022), introduction and §5, equation (79): improved bound and optimization framework.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2022 work substantially narrows the known bounds but does not identify the optimum. Its numerical optimization supports the quoted upper estimate; the present question asks for the actual sharp constant rather than reproducing that computation. Gradient-corrected inequalities and bounds restricted to fixed particle number have different admissible expressions or classes.

**Search audit:** “Lieb Oxford optimal sharp constant 2025 2026”; “Lieb Oxford 1.5765 optimal constant proof”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
