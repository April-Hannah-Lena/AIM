# 194. A uniform gap for the spin-one Heisenberg chain

**Area:** Quantum magnetism

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For each even integer $`N\ge4`$, put a three-dimensional spin space at every site of a periodic chain. On $`\mathbb C^3`$, indexed by $`m=-1,0,1`$, define $`S^z|m\rangle=m|m\rangle`$, $`S^+|m\rangle=\sqrt{2-m(m+1)}|m+1\rangle`$ (zero at $`m=1`$), $`S^-=(S^+)^*`$, $`S^x=(S^++S^-)/2`$, and $`S^y=(S^+-S^-)/(2i)`$. Let

```math
H_N=\sum_{j=1}^{N}\sum_{a=x,y,z}S_j^aS_{j+1}^a,\qquad S_{N+1}^a=S_1^a.
```

Write $`E_0(N)<E_1(N)`$ for its lowest two distinct eigenvalues. Prove or disprove that there is a constant $`\Delta>0`$, independent of even $`N`$, such that $`E_1(N)-E_0(N)\ge\Delta`$.

## Application

A positive excitation threshold distinguishes an integer-spin quantum magnet from a gapless chain and underlies the robustness of the Haldane phase in magnetic materials.

## References

1. F. D. M. Haldane, [Continuum dynamics of the 1-D Heisenberg antiferromagnet: identification with the O(3) nonlinear sigma model](https://www.sciencedirect.com/science/article/pii/037596018390631X), Physics Letters A 93 (1983), 464–468: original physical gap prediction.
2. H. Tasaki, [The Ground State of the S=1 Antiferromagnetic Heisenberg Chain is Topologically Nontrivial if Gapped](https://arxiv.org/abs/2407.17041), preprint (2024; revised December 2024), introduction and Main results: explicitly unproved gap assumption, and a conditional topological theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Tasaki explicitly separates the unproved Heisenberg gap from his conditional topological result. His finite-chain theorem uses boundary fields; the statement here uses periodic boundaries to remove edge excitations. The rigorously gapped AKLT model contains a different, biquadratic interaction and does not settle this Hamiltonian. Searches located no uniform-gap proof for the standard chain.

**Search audit:** “Haldane conjecture spin 1 Heisenberg chain spectral gap proof 2025 2026”; “Tasaki Haldane gap periodic chain rigorous”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
