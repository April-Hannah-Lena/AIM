# 197. Bose condensation at fixed dilute density

**Area:** Ultracold quantum gases

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Fix a nonzero, nonnegative, radial potential $`V\in C_c^\infty(\mathbb R^3)`$. Let $`\Lambda_L=(\mathbb R/L\mathbb Z)^3`$ and $`V_L(x)=\sum_{k\in\mathbb Z^3}V(x+Lk)`$. On symmetric $`L^2(\Lambda_L^N)`$ define

```math
H_{N,L}=\sum_{j=1}^N-\Delta_{x_j}+\sum_{i<j}V_L(x_i-x_j).
```

Let $`\Psi_{N,L}`$ be its normalized nonnegative ground state, let $`\gamma_{N,L}^{(1)}`$ be its one-particle reduced density operator normalized to trace $`N`$, and put $`\phi_L=L^{-3/2}`$. Prove or disprove: there is $`\rho_0(V)>0`$ such that every fixed $`0<\rho<\rho_0(V)`$ satisfies

```math
\liminf_{\substack{L\to\infty,\ N\to\infty\\N/L^3\to\rho}}\frac{\langle\phi_L,\gamma_{N,L}^{(1)}\phi_L\rangle}{N}>0.
```

The potential and the density remain fixed during the thermodynamic limit.

## Application

This would derive macroscopic occupation of one orbital directly from a repulsive many-atom Hamiltonian, a basic microscopic explanation of condensation in a homogeneous dilute gas.

## References

1. J. J. Chong, H. Liang and P. T. Nam, [Kinetic localization via Poincaré-type inequalities and applications to the condensation of Bose gases](https://arxiv.org/abs/2510.20493), preprint (2025; revised May 2026), §1 and §2.2: explicitly identifies thermodynamic condensation as open and distinguishes its scaling regime.
2. E. H. Lieb and R. Seiringer, [Bose-Einstein Condensation of Dilute Gases in Traps](https://arxiv.org/abs/math-ph/0210028), preprint (2002), §1, Introduction and Main Results: rigorous condensation in the different Gross–Pitaevskii limit.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Chong–Liang–Nam prove condensation beyond the Gross–Pitaevskii regime but explicitly stop short of the fixed-density thermodynamic limit. Their scaling parameter remains below its thermodynamic endpoint. The displayed question isolates a regular repulsive-potential class and zero temperature; neither energy asymptotics nor trapped-gas condensation proves it.

**Search audit:** “Bose Einstein condensation interacting homogeneous gas thermodynamic limit proof 2026”; “2510.20493 thermodynamic fixed density condensation”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
