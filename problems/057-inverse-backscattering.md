# 057 — Global uniqueness from inverse backscattering data

**Area:** Inverse scattering / monostatic imaging

**Status:** Open in cited literature; no later resolution located

**Last checked:** 2026-09-08

## Problem statement

For a real potential $q\in C_c^\infty(\mathbb R^3)$, let $u=e^{ikx\cdot\theta}+u^s$ be the outgoing solution of
$$
(-\Delta+q-k^2)u=0,\qquad k>0,\quad\theta\in S^2.
$$
Define its scattering amplitude by
$u^s(r\omega)=r^{-1}e^{ikr}a_q(\omega,\theta,k)+O(r^{-2})$, for $\omega\in S^2$. Prove or disprove that
$$
a_{q_1}(-\theta,\theta,k)=a_{q_2}(-\theta,\theta,k)
\quad\text{for every }(\theta,k)\in S^2\times(0,\infty)
$$
implies $q_1=q_2$. No smallness, symmetry, or angular-control assumption is imposed.

## Applied significance

Backscattering models experiments in which transmitter and receiver view the target from the same direction, as in monostatic radar and pulse-echo imaging.

## References

1. Rakesh and G. Uhlmann, *Uniqueness for the inverse backscattering problem for angularly controlled potentials* (2014). [Author manuscript](https://sites.math.washington.edu/~gunther/publications/Papers/backscatteringarxiv.pdf).
2. M. Nursultanov, L. Oksanen and P. Stefanov, *The Backscattering Problem for Time-Dependent Potentials*, Annales Henri Poincaré **27** (2026), 2041–2071; online 2025. [Paper](https://doi.org/10.1007/s00023-025-01579-7).
3. K. El Maddah, M. Lassas, T. Liimatainen, V. Pohjola and T. Tyni, *Reconstruction for an inverse scattering problem with a Kerr type nonlinearity* (2026), abstract and introduction. [Preprint](https://arxiv.org/abs/2606.13337).

## Status review

Reference 3 explicitly calls linear backscattering uniqueness largely open. Reference 1 requires angular control. Reference 2 obtains a small-potential result in a time-dependent setting. The Kerr-nonlinear reconstruction theorem changes the equation and does not settle this linear problem.

Searches on 2026-09-08 included `inverse backscattering 2025 2026 uniqueness` and `inverse scattering open problems fixed angle fixed energy 2024 survey`. No global theorem for arbitrary real compactly supported smooth potentials was located.
