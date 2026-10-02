# 138 — Uniqueness of nonnegative heat controls at the minimum time

**Area:** Constrained PDE control / thermal processes

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix constants $`a,b>0`$, $`a\ne b`$. On the rod $`(0,1)`$ consider $`y_t=y_{xx}`$, $`y(0,x)=a`$, with nonnegative Dirichlet controls $`y(t,0)=u_0(t)`$ and $`y(t,1)=u_1(t)`$. Let $`T_*`$ be the infimum of times in which bounded nonnegative controls can produce $`y(T,x)=b`$.

Is the pair of nonnegative finite Radon measures attaining this minimum time unique? To specify attainment without an implicit weak-solution convention, a pair $`(\mu_0,\mu_1)`$ on $`[0,T_*]`$ is admissible exactly when, for every integer $`k\ge1`$,

```math
\int_{[0,T_*]}e^{-k^2\pi^2(T_*-t)}
\bigl(d\mu_0(t)-(-1)^k d\mu_1(t)\bigr)
=\frac{(1-(-1)^k)(b-ae^{-k^2\pi^2T_*})}{k^2\pi^2}.
```

These are the terminal-state sine-mode equations. The question is whether they have exactly one nonnegative measure pair at $`T_*`$, for every $`a,b`$ above.

## Application

Nonnegative boundary temperatures impose a genuine waiting time. Uniqueness would determine whether the fastest feasible heating or cooling protocol is intrinsically specified.

## References

1. J. Lohéac, E. Trélat and E. Zuazua, *Minimal controllability time for the heat equation under unilateral state or control constraints* (2017), [M3AS 27, 1587–1644](https://doi.org/10.1142/S0218202517500270) ([author manuscript](https://cmc.deusto.eus/wp-content/uploads/2017/07/MinimalContHeat.pdf)), §6, “Uniqueness of controls at the minimal time,” and equation (6.1). States the question and its measure-moment formulation.
2. J. Lohéac, E. Trélat and E. Zuazua, *Nonnegative control of finite-dimensional linear systems* (2021), [Annales de l'Institut Henri Poincaré C 38, 301–346](https://doi.org/10.1016/j.anihpc.2020.07.004), abstract and main results. Proves uniqueness under finite-dimensional spectral hypotheses.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2017 paper proves positivity and finiteness of the waiting time and existence of measure controls, while explicitly leaving uniqueness open. The 2021 results apply to finite-dimensional systems, including spatial discretizations, and do not establish uniqueness for the continuum heat equation. Searches included “heat equation minimal time nonnegative Radon controls uniqueness 2025 2026” and “Lohéac Trélat Zuazua minimum time uniqueness”. No continuum resolution was located.
