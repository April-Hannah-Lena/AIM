# 400. Approximate velocity control of a viscoelastic fluid with prescribed transport

**Area:** PDE control / viscoelasticity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^2$ be a bounded connected smooth domain, $\Gamma\subset\partial\Omega$ a nonempty relatively open set, $T>0$, and $a,b,\nu>0$. Given $z\in C^\infty(\overline\Omega\times[0,T];\mathbb R^2)$ with $\nabla\cdot z=0$ and $z=0$ on the boundary, consider
$$u_t+(z\cdot\nabla)u-\nu\Delta u+\nabla p=\nabla\cdot\tau,\quad \nabla\cdot u=0,\qquad \tau_t+a\tau=bD(u),$$
where $D(u)=(\nabla u+\nabla u^T)/2$, $u=f\mathbf1_\Gamma$ on the boundary, and $\tau$ is symmetric. Write $H_\sigma=\overline{\{v\in C_c^\infty(\Omega;\mathbb R^2):\nabla\cdot v=0\}}^{L^2}$. Is it true that for every $u_0,u_T\in H_\sigma$, $\tau_0\in L^2(\Omega;\mathbb R_{\rm sym}^{2\times2})$ and $\varepsilon>0$, there is a boundary control $f\in L^2(\Gamma\times(0,T);\mathbb R^2)$ satisfying the zero-total-flux compatibility condition, and an associated weak solution continuous in $L^2$ at $0,T$, such that
$$\|u(T)-u_T\|_{L^2(\Omega)}<\varepsilon?$$
No terminal condition is imposed on $\tau$.

## Application

The stress relaxation equation represents memory in a viscoelastic fluid. Approximate steering of velocity under a time-dependent background flow is a prerequisite for controlling such fluids beyond a stationary linearization.

## References

1. E. Fernández-Cara, *Remarks on control and inverse problems for PDEs*, SeMA Journal 82 (2025), 267–288, §7, equation (25), Theorem 7 and Problem 14. [Full text](https://doi.org/10.1007/s40324-024-00363-7).
2. A. Doubova and E. Fernández-Cara, *On the control of viscoelastic Jeffreys fluids*, Systems & Control Letters 61 (2012), 573–579, approximate controllability result for the linear memory system. [DOI](https://doi.org/10.1016/j.sysconle.2012.02.003).
3. E. Fernández-Cara, J. L. F. Machado and D. A. Souza, *Non null controllability of Stokes equations with memory*, ESAIM: Control, Optimisation and Calculus of Variations 26 (2020), article 72. [DOI](https://doi.org/10.1051/cocv/2019067).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Problem 14 asks whether the approximate velocity-control theorem survives the added prescribed transport term. Smooth divergence-free backgrounds and compatible controls make the model unambiguous. The negative null-control result concerns exact arrival and does not answer this approximate question. Searches through 22 September 2026 for Oseen–Oldroyd, Jeffreys memory and time-dependent drift controllability found no resolution.
