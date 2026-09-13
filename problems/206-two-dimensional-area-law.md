# 206. An area law for general gapped two-dimensional spin systems

**Area:** Quantum many-body theory; entanglement

## Problem statement

Fix an integer $q\ge2$ and $\Delta>0$. On $\Lambda=\{1,\ldots,L\}\times\{1,\ldots,M\}$ put a copy of $\mathbb C^q$ at each vertex. Let $H=\sum_x h_x+\sum_{\{x,y\}\text{ nearest neighbors}}h_{xy}$ be self-adjoint, with each term supported on its indicated sites and of operator norm at most $1$. Assume a unique normalized ground state $\psi$ and spectral gap at least $\Delta$. For $1\le\ell<L$, let $A=\{1,\ldots,\ell\}\times\{1,\ldots,M\}$ and $\rho_A=\operatorname{Tr}_{\Lambda\setminus A}|\psi\rangle\langle\psi|$.

Does a constant $C(q,\Delta)$, independent of $L,M,\ell$ and the interaction, always satisfy
$$-\operatorname{Tr}(\rho_A\log\rho_A)\le C(q,\Delta)M?$$

## Applied significance

This would justify boundary-sized entanglement as a general structural principle for insulating quantum matter and tensor-network representations of its ground states.

## References

1. Matthew B. Hastings, [An area law for one dimensional quantum systems](https://arxiv.org/abs/0705.2024), *J. Stat. Mech.* (2007), P08024. The main theorem establishes the one-dimensional precedent.
2. Anurag Anshu, Itai Arad, and David Gosset, [An area law for 2D frustration-free spin systems](https://arxiv.org/abs/2103.02492), STOC (2022), preprint revised 2023. Introduction and main-result discussion explicitly distinguish the general open area law from their locally gapped, frustration-free theorem.

## Status review

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13.

The cited two-dimensional theorem imposes frustration-freeness and a gap for local restrictions. A gap for the entire Hamiltonian alone does not supply those hypotheses. No general theorem for this class was located.

**Search audit:** Queries: “two dimensional gapped Hamiltonian area law general proof 2025 2026”, “Anshu Arad Gosset area law global gap frustration free”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
