# 205. Antiferromagnetic order in the half-filled square-lattice Hubbard model

**Area:** Correlated electrons; quantum materials

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For even $`L\ge4`$ and $`U>0`$, on $`\Lambda_L=(\mathbb Z/L\mathbb Z)^2`$ consider

```math
H_{L,U}=-\sum_{\{x,y\}\text{ nearest neighbors}}\sum_{s=\uparrow,\downarrow}(c_{xs}^\dagger c_{ys}+c_{ys}^\dagger c_{xs})+U\sum_x n_{x\uparrow}n_{x\downarrow}.
```

The fermionic operators satisfy $`\{c_{xs},c_{yt}^\dagger\}=\delta_{xy}\delta_{st}`$, $`\{c_{xs},c_{yt}\}=0`$, and $`n_{xs}=c_{xs}^\dagger c_{xs}`$. Restrict to exactly $`L^2`$ electrons and let $`\psi_{L,U}`$ be its normalized ground state. Define $`S_x^3=(n_{x\uparrow}-n_{x\downarrow})/2`$.

Does every fixed $`U>0`$ satisfy

```math
\liminf_{\substack{L\to\infty\\L\text{ even}}}\frac1{L^4}\left\langle\psi_{L,U},\left(\sum_x(-1)^{x_1+x_2}S_x^3\right)^2\psi_{L,U}\right\rangle>0?
```

## Application

The statement would derive collective magnetic order directly from electron hopping and local Coulomb repulsion, rather than assuming a spin-only effective model.

## References

1. Hal Tasaki, [The Hubbard Model: Introduction and Selected Rigorous Results](https://arxiv.org/abs/cond-mat/9512169), *J. Phys.: Condens. Matter* 10 (1998), 4353–4378. Sections 5.1–5.2 distinguish effective antiferromagnetic interactions and correlation signs from a proof of long-range order.
2. Edwin Langmann and Jonatan Lenells, [On the mean-field antiferromagnetic gap for the half-filled 2D Hubbard model at zero temperature](https://link.springer.com/article/10.1007/s11005-026-02085-5), *Lett. Math. Phys.* 116 (2026), 50. Introduction and Theorem 1.1 treat the Hartree–Fock gap, providing a recent explicitly restricted result.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The conjecture concerns the exact many-electron ground state for all positive interaction strengths. Lieb’s singlet theorem and signs of two-point correlations do not give a nonzero limiting structure factor. The April 2026 gap theorem is explicitly about Hartree–Fock theory; finite-cluster simulations and strong-coupling expansions do not settle the stated limit.

**Search audit:** Queries: “Hubbard antiferromagnetic long range order rigorous theorem 2026 half filled”, “Hubbard square lattice antiferromagnetism open rigorous proof”, “Hubbard half filling Neel order conjecture 2025”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
