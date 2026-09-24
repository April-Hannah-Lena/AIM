# 450. Can bounded positive time-dependent potentials trap a Schrödinger wave?

**Area:** Time-dependent Schrödinger PDEs and quantum confinement

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Is it possible to find $V\in C^\infty([0,\infty)\times\mathbb R^3;\mathbb R)$ with $V\ge0$, every space-time derivative bounded, and $\operatorname{supp}V(t,\cdot)\subset B_R$ for one fixed $R<\infty$, together with $\psi_0\in L^2(\mathbb R^3)$ of norm one, such that the unitary solution of
$$i\partial_t\psi=(-\Delta+V(t,x))\psi,\qquad \psi(0)=\psi_0,$$
is uniformly localized in the sense
$$\lim_{L\to\infty}\ \sup_{t\ge0}\int_{|x|>L}|\psi(t,x)|^2\,dx=0?$$
A negative answer would say that no nonzero state stays spatially tight under any potential in this class. The potential may vary arbitrarily in time within the stated bounds.

## Application

The question tests whether time-varying repulsive fields can confine a quantum wave without an attractive static well. It is relevant to dynamical trapping by externally driven optical or electromagnetic fields.

## References

1. A. Soffer, [A new paradigm for scattering theory of linear and nonlinear waves: review and open problems](https://doi.org/10.1186/s13662-024-03831-6), *Advances in Continuous and Discrete Models* (2024), article 34, §14.2, “Quantum ping-pong.”
2. A. Soffer and X. Wu, [Local Decay Estimates](https://arxiv.org/abs/2211.00500), version 4 (August 2026), §1.1, assumptions and Theorems 1.1–1.4.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The first source explicitly leaves localization by regular bounded positive time-dependent potentials open. The August 2026 decay theorem controls the scattering projection and does not establish that the bound-state projection vanishes merely from positivity at each time. Searches for quantum ping-pong, positive driven-potential confinement, and later localization constructions found no resolution for this smooth uniformly supported class.
