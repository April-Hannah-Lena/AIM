# 076. Global regularity of the three-dimensional Navier–Stokes equations

**Area:** Fluid dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\mathbb T^3=(\mathbb R/\mathbb Z)^3$, $\nu>0$, and let $u_0\in C^\infty(\mathbb T^3;\mathbb R^3)$ have zero mean and $\nabla\cdot u_0=0$. Does the unforced initial-value problem
$$
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,\qquad
\nabla\cdot u=0,\qquad u(0)=u_0
$$
have a smooth solution on $\mathbb T^3\times[0,T]$ for every finite $T>0$ and every such datum? Pressure is normalized to have zero spatial mean. A negative answer must demonstrate failure of smooth continuation for an admissible datum. This is the periodic smooth-data version, with fixed positive viscosity.

## Application

This is the basic regularity question for the continuum model used in incompressible viscous-flow simulation.

## References

- [Charles L. Fefferman, *Existence and smoothness of the Navier–Stokes equation* (2000), official problem description linked by the Clay Mathematics Institute](https://www.claymath.org/millennium/navier-stokes-equation/).
- [Terence Tao, *Nonlinear dispersive equations: local and global analysis* (2006), discussion of supercritical evolution and regularity barriers](https://math.ucla.edu/~tao/preprints/chapter.pdf).

- OpenAI, *Finite time blowup for Navier–Stokes* (September 2026 manuscript), Theorem 1.1 and Corollary 10.6. [Primary manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

A September 8, 2026 announcement claims finite-time blowup for smooth **forced** Navier–Stokes flow. The primary manuscript’s Theorem 1.1 explicitly includes a smooth nonzero force and zero initial velocity; Corollary 10.6 transfers that construction to the torus. It therefore does not settle the **unforced** initial-value problem stated here. This distinction concerns the hypotheses, independently of whether the announced proof is ultimately accepted. No independent verification of that proof or its announced formalization is claimed by this catalogue.

Searches on 2026-09-22 covered unforced periodic Navier–Stokes regularity, smooth-data blowup, and the new forced construction. No matching resolution of the displayed unforced statement was located. Global weak existence, restricted-data regularity, and a forced singularity do not by themselves answer this question. The earlier blanket assertion about the status of the entire Millennium problem has been removed.
