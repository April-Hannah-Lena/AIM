# 154. Steady planar flow around an obstacle at arbitrary Reynolds number

**Area:** Viscous flow around bodies

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $D\subset\mathbb R^2$ be a bounded simply connected domain with smooth boundary, and $\Omega=\mathbb R^2\setminus\overline D$. For every viscosity $\nu>0$ and every constant $U\in\mathbb R^2\setminus\{0\}$, does there exist a smooth solution $(u,p)$ on $\Omega$, continuous up to the boundary, satisfying

$$
-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,\qquad \operatorname{div}u=0,
$$

$$
u|_{\partial D}=0,\qquad \lim_{|x|\to\infty}u(x)=U,\qquad\int_\Omega|\nabla u|^2\,dx<\infty?
$$

The far-field convergence is uniform, and no smallness condition on $|U|/\nu$ is permitted.

## Application

This is the basic existence question for a stationary viscous flow past a two-dimensional body with prescribed incoming velocity.

## References

1. Mikhail V. Korobkov and Xiao Ren, *Leray’s plane stationary solutions at small Reynolds numbers* (2021), introduction and Theorem 1. [Paper](https://arxiv.org/abs/2105.08898). Explicit far-field problem and its small-Reynolds-number resolution.

2. Mikhail V. Korobkov, Konstantin Pileckas and Remigio Russo, *Leray’s plane steady state solutions are nontrivial*, Advances in Mathematics 376 (2021), 107451. [Article](https://doi.org/10.1016/j.aim.2020.107451). Removes symmetry restrictions for nontriviality of the constructed flow.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searches for “stationary Navier Stokes exterior two dimensional arbitrary velocity infinity existence open 2026”, “Leray plane arbitrary Reynolds prescribed velocity infinity”, and “Korobkov Ren 2026 infinity” located small-data far-field results and later estimates. Nontriviality and convergence to some constant do not identify that constant with prescribed $U$. No arbitrary-Reynolds existence theorem satisfying all conditions above was located.
