# 088. Smooth unforced inviscid Boussinesq evolution on the whole plane

**Area:** Geophysical fluid dynamics

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

## Problem statement

For arbitrary real Schwartz data $u_0:\mathbb R^2\to\mathbb R^2$ and $\theta_0:\mathbb R^2\to\mathbb R$ with $\nabla\cdot u_0=0$, determine whether
$$
u_t+(u\cdot\nabla)u+\nabla p=\theta e_2,\qquad
\theta_t+u\cdot\nabla\theta=0,\qquad \nabla\cdot u=0
$$
has a global smooth finite-energy solution. Here $e_2=(0,1)$, $(u,\theta)(0)=(u_0,\theta_0)$, and neither viscosity nor thermal diffusion is present. There is no external forcing beyond the displayed buoyancy coupling and no solid boundary. A finite-time singularity from these smooth data would resolve the question negatively.

## Applied significance

The model captures buoyancy-driven transport and the production of vorticity by temperature gradients.

## References

- [Jiajie Chen and Thomas Y. Hou, *Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data I* (2022; revised 2023), introduction and boundary hypotheses](https://arxiv.org/abs/2210.07191).
- [Bojin Chen, De Huang and Xiangyuan Li, *Novel Self-similar Finite-time Blowups with Singular Profiles of the 1D Hou-Luo Model and the 2D Boussinesq Equations: A Numerical Investigation* (2026)](https://arxiv.org/abs/2604.01868).
- [Terence Tao, *Finite time blowup with smooth forcing term for the incompressible porous medium, Boussinesq, and incompressible Euler equations* (7 September 2026), research commentary](https://terrytao.wordpress.com/2026/09/).

## Status review

Boundary constructions and numerical singular profiles do not settle the stated whole-plane smooth-data problem. The September 2026 work discussed by Tao includes additional smooth forcing; it therefore does not resolve this unforced formulation. A March 2026 search result concerns a transformed sector model with weighted energy, rather than a verified Schwartz-data solution of this system.

Status-search topics (2026-09-08): `Boussinesq blowup smooth plane 2025 2026`; `Boussinesq Alpöge Buckmaster smooth 2026 arxiv`. This is a literature search, not a proof that no solution exists.
