# 214. Can entangled codewords improve amplitude-damping classical capacity?

**Area:** Quantum communication; dissipative qubits

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For $0<\gamma<1$, define a qubit channel
$$\mathcal A_\gamma(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger,\quad K_0=\begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix},\quad K_1=\begin{pmatrix}0&\sqrt\gamma\\0&0\end{pmatrix}.$$
For any finite-dimensional quantum channel $\Phi$, let
$$\chi(\Phi)=\sup_{\{p_j,\rho_j\}}\left[S\!\left(\sum_jp_j\Phi(\rho_j)\right)-\sum_jp_jS(\Phi(\rho_j))\right],$$
where the supremum is over finite ensembles of input density operators and $S(\rho)=-\operatorname{Tr}(\rho\log_2\rho)$.

Is $\chi(\mathcal A_\gamma^{\otimes n})=n\chi(\mathcal A_\gamma)$ for every $n\ge1$ and every $0<\gamma<1$? Equivalently, does its unassisted classical capacity $\sup_{n\ge1}\chi(\mathcal A_\gamma^{\otimes n})/n$ equal the one-use Holevo information?

## Application

Amplitude damping models energy relaxation, including spontaneous emission. This asks whether entangling classical-message codewords across repeated uses increases the achievable communication rate.

## References

1. Felix Leditzky, Eneet Kaur, Nilanjana Datta, and Mark M. Wilde, [Approaches for approximate additivity of the Holevo information of quantum channels](https://arxiv.org/abs/1709.01111), *Phys. Rev. A* 97 (2018), 012332. Introduction and Section IV.A, equation (28), explicitly leave the channel’s classical capacity undetermined.
2. Fernando G. S. L. Brandão, Jens Eisert, Michał Horodecki, and Dong Yang, [Entangled inputs cannot make imperfect quantum channels perfect](https://arxiv.org/abs/1010.5074), *Phys. Rev. Lett.* 106 (2011), 230502; corrected preprint 2013. The amplitude-damping application supplies rigorous capacity bounds.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The one-use Holevo quantity is known, but the cited capacity bounds do not establish its additivity over arbitrary block lengths. Recent results on symmetric generalized amplitude damping are unital-channel results; the channel here is nonunital. Known quantum-capacity formulas concern transmission of quantum states, a different task.

**Search audit:** Queries: “amplitude damping classical capacity additivity 2025 2026”, “amplitude damping Holevo information exact capacity proof”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
