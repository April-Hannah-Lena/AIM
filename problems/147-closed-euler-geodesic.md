# 147. A closed Lagrangian Euler trajectory on a surface of higher genus

**Area:** Geometric hydrodynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

For every closed connected oriented smooth Riemannian surface $`(M,g)`$ of genus at least two and every $`s>2`$, does there exist a nonzero divergence-free $`u_0\in H^s(TM)`$ and $`T>0`$ whose Euler solution has

```math
\eta(T)=\mathop{\mathrm{id}}\nolimits_M,\qquad u(T)=u_0?
```

The equations are $`\partial_tu+\nabla_u u=-\mathop{\mathrm{grad}}\nolimits p`$, $`\mathop{\mathrm{div}}\nolimits u=0`$, and $`\partial_t\eta=u\circ\eta`$, with $`\eta(0)=\mathop{\mathrm{id}}\nolimits_M`$. Thus every marked particle, as well as the velocity, must return; $`u_0=0`$ is excluded.

## Application

No direct application is identified in this entry. The mathematical question is whether ideal Euler flow on every surface of higher genus admits nontrivial exact material recurrence: every particle and the velocity return together. This is a question about the geometry of fluid configuration spaces.

## References

1. Boris Khesin, Gerard Misiołek and Alexander Shnirelman, *Geometric Hydrodynamics in Open Problems*, Archive for Rational Mechanics and Analysis 247 (2023), article 15. [Author copy](https://www.math.toronto.edu/khesin/papers/Problems_in_GHD_ARMA.pdf). §5.3, Problem 10, explicitly asks about closed geodesics on these fluid configuration spaces.

2. Vladimir Arnold and Boris Khesin, *Topological Methods in Hydrodynamics*, Springer (1998). [Book](https://doi.org/10.1007/b97593). Chapter I supplies the right-invariant kinetic metric and Euler–geodesic correspondence.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2023 list poses the higher-genus case separately from endpoint surjectivity. The problem is the existence of a nonconstant closed geodesic in the group of area-preserving maps, not a closed geodesic on the underlying surface. Searches for “Euler closed geodesics genus 2025 2026” and “Khesin Misiolek Shnirelman Problem 10 closed geodesic” located no resolution. Torus translations do not address the topology specified here.
