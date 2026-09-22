# 037. Existence of NPT bound entanglement

**Area:** Quantum information and positive operators

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Does there exist a density matrix $\rho\ge0$, $\operatorname{tr}\rho=1$, on some finite-dimensional $\mathbb C^{d_A}\otimes\mathbb C^{d_B}$ such that $\rho^{T_B}$ has a negative eigenvalue, yet for every integer $k\ge1$ and every vector $v$ of Schmidt rank at most two across $A^k:B^k$,
$$\langle v,(\rho^{T_B})^{\otimes k}v\rangle\ge0?$$
Here $T_B$ transposes matrix entries on the second tensor factor in a fixed product basis. Schmidt rank is the rank of the coefficient matrix of $v$. The all-$k$ condition is the finite-copy criterion for nondistillability under local operations and classical communication.

## Application

The answer determines whether some negative-partial-transpose entanglement can never be converted into usable maximally entangled pairs, even when arbitrarily many identical copies are available.

## References

1. P. Horodecki, Ł. Rudnicki and K. Życzkowski, [Five open problems in quantum information](https://arxiv.org/abs/2002.03233), 2020 / PRX Quantum 3 (2022), 010101. NPT bound-entanglement question.
2. T. C. Fraser, F. Huber, B. Pozsgay and I. Vona, [On the two-copy distillability of Werner states and a new partial trace inequality](https://arxiv.org/abs/2607.24309), 2026. Resolves the two-copy Werner subproblem.

## Status review

**Literature check:** Open in cited literature; no later resolution located

Checked on **2026-09-08**. The July 2026 result establishes two-copy undistillability for the stated Werner region. This is progress toward the all-copy problem, not proof of an NPT state satisfying the criterion for every k. Searches did not locate a general all-copy existence or impossibility theorem.

Searches included: `NPT bound entanglement 2025 2026`; `negative partial transpose bound entanglement solved`; `two-copy distillability Werner 2026`. This is a documented literature check, not a certification that no solution exists.
