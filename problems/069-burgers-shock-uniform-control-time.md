# 069 — Exact uniform control time near a viscous Burgers shock

**Area:** Singular limits and control

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix $`L>0`$. For viscosity $`\varepsilon>0`$, set $`U^\varepsilon(x)=-\tanh(x/(2\varepsilon))`$ and consider

```math
\partial_t u-\varepsilon\partial_x^2u+\partial_x(U^\varepsilon u)=0
\quad(-L<x<L),\qquad
u(t,-L)=h(t),\quad u(t,L)=0,\quad u(0)=u_0.
```

Define

```math
C(T,\varepsilon)=\sup_{\|u_0\|_{L^2(-L,L)}=1}
 \inf\{\|h\|_{L^2(0,T)}:u(T)=0\},
\quad
T_{\rm unif}=\inf\{T>0:\limsup_{\varepsilon\downarrow0}C(T,\varepsilon)<\infty\}.
```

Determine the exact dimensionless constant $`T_{\rm unif}/L`$, closing the known interval between $`4\sqrt2-2`$ and $`4\sqrt3`$.

## Application

In boundary control of a viscous flow, an actuator must suppress small disturbances around a stationary shock. This constant gives the shortest time horizon for doing so without the required control cost diverging as viscosity tends to zero.

## References

1. Vincent Laheurte, *Cost of Controllability of the Burgers Equation Linearized at a Steady Shock in the Vanishing Viscosity Limit*, SIAM Journal on Mathematical Analysis **58** (2026), 2702–2737, Theorem 1.1 and Remark 1.2. [DOI](https://doi.org/10.1137/25M1723311), [March 2026 version](https://arxiv.org/html/2411.12267v3).
2. Pierre Lissy, *Explicit Lower Bounds for the Cost of Fast Controls for Some 1-D Parabolic or Dispersive Equations, and a New Lower Bound Concerning the Uniform Controllability of the 1-D Transport–Diffusion Equation*, Journal of Differential Equations **259** (2015), 5331–5352. [DOI](https://doi.org/10.1016/j.jde.2015.06.031).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Laheurte formulates the minimal-time problem and gives distinct lower and upper bounds in the 2026 theorem. The inviscid limit's own control time does not equal the proved viscous lower bound. Searches on 2026-09-08: "Cost of controllability steady shock 2026 Laheurte" and "Burgers steady shock exact uniform controllability time". No result closing the gap was located.
