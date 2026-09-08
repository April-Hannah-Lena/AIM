# 076. Global regularity of the three-dimensional Navier–Stokes equations

**Area:** Fluid dynamics

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-08

## Problem statement

Let $\mathbb T^3=(\mathbb R/\mathbb Z)^3$, $\nu>0$, and let $u_0\in C^\infty(\mathbb T^3;\mathbb R^3)$ have zero mean and $\nabla\cdot u_0=0$. Does the unforced initial-value problem
$$
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,\qquad
\nabla\cdot u=0,\qquad u(0)=u_0
$$
have a smooth solution on $\mathbb T^3\times[0,T]$ for every finite $T>0$ and every such datum? Pressure is normalized to have zero spatial mean. A negative answer must demonstrate failure of smooth continuation for an admissible datum. This is the periodic smooth-data version, with fixed positive viscosity.

## Applied significance

This is the basic regularity question for the continuum model used in incompressible viscous-flow simulation.

## References

- [Charles L. Fefferman, *Existence and smoothness of the Navier–Stokes equation* (2000), official problem description linked by the Clay Mathematics Institute](https://www.claymath.org/millennium/navier-stokes-equation/).
- [Terence Tao, *Nonlinear dispersive equations: local and global analysis* (2006), discussion of supercritical evolution and regularity barriers](https://math.ucla.edu/~tao/preprints/chapter.pdf).

## Status review

The Clay Mathematics Institute continues to list the problem as unresolved. Global weak solutions and smooth solutions for restricted data do not establish this statement. Search results included general proof claims; no accepted resolution of the official periodic problem was located.

Searches run on 2026-09-08: `Navier Stokes global regularity open problem 2026 Clay mathematics`; `Navier Stokes smooth periodic global regularity solved 2026`. This is a literature search, not a proof that no solution exists.
