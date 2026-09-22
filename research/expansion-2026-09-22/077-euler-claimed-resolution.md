# 077. Finite-time singularity for smooth three-dimensional Euler flow without a boundary

**Area:** Fluid dynamics

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-09-22

## Problem statement

Does there exist a divergence-free Schwartz vector field $u_0:\mathbb R^3\to\mathbb R^3$ whose classical solution of
$$
\partial_tu+(u\cdot\nabla)u+\nabla p=0,\qquad
\nabla\cdot u=0,\qquad u(0)=u_0
$$
has a finite maximal smooth lifespan? Equivalently, either construct such data, or prove that every datum in this class has a smooth solution for all positive time. Solutions must have finite kinetic energy; there is no forcing and the spatial domain is all of $\mathbb R^3$.

## Application

Resolving whether inviscid vortex stretching creates singularities would clarify the limits of ideal-fluid models and the interpretation of numerical blowup evidence.

## References

- [Jiajie Chen and Thomas Y. Hou, *Singularity formation in 3D Euler equations with smooth initial data and boundary* (PNAS, 2025), abstract and review](https://authors.library.caltech.edu/records/40zbk-gep55).
- [Bojin Chen, De Huang and Xiangyuan Li, *Novel Self-similar Finite-time Blowups with Singular Profiles of the 1D Hou-Luo Model and the 2D Boussinesq Equations: A Numerical Investigation* (2026), introduction](https://arxiv.org/abs/2604.01868).

## Status review

**Review note:** Matching resolution announced; awaiting independent review; excluded from the active open catalogue.

On 8 September 2026, OpenAI released *Finite Time Blowup for the Euler Equation*. Its Theorem 1.1 asserts finite-time breakdown of unforced three-dimensional Euler on $\mathbb R^3$ from a divergence-free $C_c^\infty$ initial velocity, with unbounded velocity gradient and divergent time-integrated vorticity maximum. These hypotheses match this entry: compactly supported smooth data are Schwartz and have finite energy.

- [Primary manuscript, Theorem 1.1, page 1](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf).
- [Dated announcement and accompanying materials](https://openai.com/index/navier-stokes-solution/).

Checked on 2026-09-22. This catalogue has compared the theorem statement with the entry, but has not independently verified the proof or the announced formalization. No journal acceptance or completed independent review was established during this check. Accordingly the entry is held outside the active open-problem count because of a matching resolution claim, rather than labelled a certified solved theorem. Its original statement and permanent identifier are retained here. The September 8 status search predates this correction and must not be treated as current evidence that no resolution has been proposed.

The accompanying forced Navier–Stokes claim does not by itself settle the unforced periodic problem 076. A new problem receives a new identifier; 077 is not reused.
