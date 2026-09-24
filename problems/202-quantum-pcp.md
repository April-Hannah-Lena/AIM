# 202. The quantum PCP conjecture for local Hamiltonians

**Area:** Quantum complexity; many-body energy approximation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Do there exist an integer $k\ge2$ and a constant $\varepsilon>0$ for which the following promise problem is QMA-hard under quantum polynomial-time reductions?

The input consists of $m$ positive semidefinite operators $0\le h_j\le I$ on $n$ qubits, each acting on at most $k$ qubits, and rational numbers $0\le a<b\le1$ with $b-a\ge\varepsilon$. Local matrices and thresholds have polynomial-length binary descriptions. With

$$
H=\frac1m\sum_{j=1}^m h_j,
$$

distinguish $\lambda_{\min}(H)\le a$ from $\lambda_{\min}(H)\ge b$, promised that one holds.

QMA comprises promise problems with polynomial-time quantum verifiers, polynomially many witness qubits, completeness at least $2/3$, and soundness at most $1/3$. Hardness here means that every such problem reduces to this one by a uniform polynomial-time quantum computation with bounded error.

## Application

Ground-energy estimates are central to computational models of quantum matter. The conjecture asks whether allowing a fixed error per interaction still leaves a worst-case problem as hard as general quantum verification, clarifying the computational limits of approximate many-body energy calculations.

## References

1. Dorit Aharonov, Itai Arad, and Thomas Vidick, [The Quantum PCP Conjecture](https://arxiv.org/abs/1309.7495), *ACM SIGACT News* 44 (2013). Conjecture 1.3 gives the local-Hamiltonian gap-amplification formulation; the discussion specifies quantum reductions.
2. Harry Buhrman, Jonas Helsen, and Jordi Weggemans, [Quantum PCPs: On Adaptivity, Multiple Provers and Reductions to Local Hamiltonians](https://arxiv.org/abs/2403.04841), *Quantum* 9 (2025), 1791. Introduction and overview of results examine partial advances and remaining barriers.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 paper continues to treat quantum PCP as conjectural. The proved no-low-energy-trivial-states property does not establish QMA-hardness of this constant-error energy problem. Quantum reductions are explicit to match the cited formulation.

**Search audit:** Queries: “quantum PCP conjecture solved proof 2026”, “quantum PCP constant gap local Hamiltonian 2025 2026”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
