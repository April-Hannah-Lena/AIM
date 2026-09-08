# 077. Finite-time singularity for smooth three-dimensional Euler flow without a boundary

**Area:** Fluid dynamics

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

## Problem statement

Does there exist a divergence-free Schwartz vector field $u_0:\mathbb R^3\to\mathbb R^3$ whose classical solution of
$$
\partial_tu+(u\cdot\nabla)u+\nabla p=0,\qquad
\nabla\cdot u=0,\qquad u(0)=u_0
$$
has a finite maximal smooth lifespan? Equivalently, either construct such data, or prove that every datum in this class has a smooth solution for all positive time. Solutions must have finite kinetic energy; there is no forcing and the spatial domain is all of $\mathbb R^3$.

## Applied significance

Resolving whether inviscid vortex stretching creates singularities would clarify the limits of ideal-fluid models and the interpretation of numerical blowup evidence.

## References

- [Jiajie Chen and Thomas Y. Hou, *Singularity formation in 3D Euler equations with smooth initial data and boundary* (PNAS, 2025), abstract and review](https://authors.library.caltech.edu/records/40zbk-gep55).
- [Bojin Chen, De Huang and Xiangyuan Li, *Novel Self-similar Finite-time Blowups with Singular Profiles of the 1D Hou-Luo Model and the 2D Boussinesq Equations: A Numerical Investigation* (2026), introduction](https://arxiv.org/abs/2604.01868).

## Status review

The 2025 review explicitly leaves the general singularity problem unresolved; its construction uses a boundary. The 2026 numerical paper distinguishes free-space Euler from those results. Neither boundary blowup nor blowup from finite Hölder regularity supplies Schwartz data for this question.

Searches run on 2026-09-08: `three dimensional Euler smooth compact support blowup open problem 2025 2026`; `Boussinesq smooth without boundary 2026`. This is a literature search, not a proof that no solution exists.
