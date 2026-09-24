# 080. Soliton resolution for bounded nonradial energy-critical waves

**Area:** Nonlinear waves

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $u$ be a global real strong solution of $u_{tt}-\Delta u-u^5=0$ on $\mathbb R^{1+3}$, meaning $(u,u_t)\in C([0,\infty);\dot H^1\times L^2)$, $u\in L^8([0,T]\times\mathbb R^3)$ for every finite $T>0$, and the equation holds in the standard Duhamel sense. Assume
$\sup_{t\ge0}\|(u,u_t)(t)\|_{\dot H^1\times L^2}<\infty$.
Must there exist a free wave $v_{tt}-\Delta v=0$, an integer $J\ge0$, nonzero stationary solutions $Q_j\in\dot H^1$ of $-\Delta Q_j=Q_j^5$, velocities $|\ell_j|<1$, scales $\lambda_j(t)>0$ and centers $x_j(t)$ such that

$$
\left\|(u,u_t)(t)-(v,v_t)(t)
-\sum_{j=1}^J\left(
\lambda_j^{-1/2}Q_{j,\ell_j}(0,\tfrac{\cdot-x_j}{\lambda_j}),
\lambda_j^{-3/2}\partial_sQ_{j,\ell_j}(0,\tfrac{\cdot-x_j}{\lambda_j})
\right)\right\|_{\dot H^1\times L^2}\longrightarrow0?
$$

Here $Q_{j,\ell}$ is the Lorentz boost of $Q_j$:
$Q_{j,\ell}(s,y)=Q_j(y+(\gamma_\ell-1)(y\cdot\ell)\ell/|\ell|^2-\gamma_\ell\ell s)$,
$\gamma_\ell=(1-|\ell|^2)^{-1/2}$, with $Q_{j,0}=Q_j$.
Require $\lambda_j(t)/t\to0$, $x_j(t)/t\to\ell_j$ and, for $i\ne j$,
$\lambda_i/\lambda_j+\lambda_j/\lambda_i+
|x_i-x_j|^2/(\lambda_i\lambda_j)\to\infty$ as $t\to\infty$.
The limit is along all times.

## Application

This would justify describing long-time nonlinear wave evolution by finitely many coherent structures plus dispersive radiation.

## References

- [Charles Collot, Thomas Duyckaerts, Carlos Kenig and Frank Merle, *Non-radial soliton resolution for the energy critical wave equation for initial data with compact support* (2026), introduction and conditional results](https://doi.org/10.3934/dcds.2026115).
- [Jacek Jendrej and Andrew Lawrie, *Soliton resolution for the energy-critical nonlinear wave equation in the radial case* (Annals of PDE, 2023)](https://doi.org/10.1007/s40818-023-00159-4).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The June 2026 paper treats compact support and additional assumptions on ground-state solitons and their velocities; it excludes a collision scenario only in certain cases. Radial results and decomposition along selected times do not provide the general nonradial all-time assertion above.

Searches run on 2026-09-08: `soliton resolution nonradial wave 2026`; `Soliton resolution for the energy-critical nonlinear wave equation in the radial case`. This is a literature search, not a proof that no solution exists.
