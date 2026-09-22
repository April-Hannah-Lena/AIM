# 267 — Global constrained null control of a two-phase Stefan interface

**Area:** Free-boundary control / thermal processing

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Fix $L,d_l,d_r,\lambda,T>0$, $L_0,L_T\in(0,L)$, and arbitrary $y_0\in C_c^\infty(0,L_0)$, $z_0\in C_c^\infty(L_0,L)$. Can two controls $v_l,v_r\in L^\infty(0,T)$ produce a solution on the whole interval $[0,T]$ of

$$
\begin{aligned}
y_t-d_ly_{xx}&=0&& (0<x<\ell(t)),\\
z_t-d_rz_{xx}&=0&& (\ell(t)<x<L),\\
y(\ell(t),t)=z(\ell(t),t)&=0,\qquad y(0,t)=v_l(t),\quad z(L,t)=v_r(t),\\
d_ly_x(\ell(t)^-,t)-d_rz_x(\ell(t)^+,t)&=-\lambda\ell'(t),
\end{aligned}
$$

with initial data $(y_0,z_0,L_0)$ and terminal conditions $y(\cdot,T)=z(\cdot,T)=0$, $\ell(T)=L_T$? Require $\ell\in C^1([0,T])$ and $0<\ell(t)<L$ throughout, with the temperatures continuous in $L^2$ after extension by zero to $(0,L)$. These smooth data satisfy the initial interface compatibility conditions. No sign restrictions or smallness assumptions are imposed on the data or controls.

## Application

This asks whether arbitrary temperature profiles and a phase interface can be reset in a prescribed time by heating or cooling at both ends of a rod.

## References

1. E. Fernández-Cara, *Remarks on control and inverse problems for PDEs* (2025), [SeMA Journal 82, 267–288](https://doi.org/10.1007/s40324-024-00363-7), §3, equations (6)–(7), Theorem 3 and Problem 5. Provides this boundary model and asks whether global control or a data-dependent minimal time holds.
2. R. K. C. Araújo, E. Fernández-Cara, J. Límaco and D. A. Souza, *Remarks on the control of two-phase Stefan free-boundary problems* (2022), [SIAM JCO 60, 3078–3099](https://doi.org/10.1137/21M1402261); [manuscript](https://arxiv.org/abs/2402.06710), introduction and main theorem. Establishes local constrained control for two distributed actuators and gives an obstruction with one actuator.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This is the smooth compatible-data version of the survey’s global question; its local theorem holds near the terminal equilibrium. Global means all stated profiles at every prescribed positive time while keeping both phases nonempty. Searches included “two-phase Stefan global controllability 2026”, “Stefan minimal time boundary controls”, and the Araújo–Fernández-Cara–Límaco–Souza title. Stabilization, local control and one-phase results do not settle it; no global theorem or matching obstruction was located.
