# 398. The sharp local maneuvering time for a shallow-water tank

**Area:** PDE control / fluid–structure dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For $0<x<1$ consider the normalized Saint-Venant tank system
$$
H_t+(Hv)_x=0,\qquad v_t+(H+v^2/2)_x=-a(t),\qquad
v(t,0)=v(t,1)=0,\qquad s'=a,\quad D'=s.
$$
The control $a$ is continuous, and $H,v$ are $C^1$. The equilibrium is $(H,v,s,D)=(1,0,0,0)$.
Let $\mathcal Y$ consist of $(H,v,s,D)\in C^1([0,1])^2\times\mathbb R^2$ satisfying $H>0$, $\int_0^1H=1$, $v(0)=v(1)=0$ and $H_x(0)=H_x(1)$. Use the norm $\|H-1\|_{C^1}+\|v\|_{C^1}+|s|+|D|$.
Is the following local controllability property valid for every $T>2$? For every $\varepsilon>0$, there exists $\eta>0$ such that any two states in $\mathcal Y$ within $\eta$ of equilibrium can be joined in time $T$ by a classical trajectory satisfying
$$
\sup_{0\le t\le T}\bigl(\|H(t)-1\|_{C^1}+\|v(t)\|_{C^1}+|s(t)|+|D(t)|+|a(t)|\bigr)<\varepsilon.
$$
Only sufficiency above $2$ is asked; the endpoint $T=2$ is not included.

## Application

This determines the shortest small-amplitude maneuver of a liquid-filled container that simultaneously returns the fluid to a prescribed shape and controls the tank position and velocity.

## References

1. J.-M. Coron, *Time for local controllability of a 1-D tank containing a fluid modeled by the shallow water equations*, Problem 7.1, pp. 247–250, in V. D. Blondel and A. Megretski (eds.), *Unsolved Problems in Mathematical Systems and Control Theory*, Princeton University Press (2004). [Publisher book](https://doi.org/10.1515/9781400826155).
2. J.-M. Coron, A. Koenig and H.-M. Nguyen, *Lack of local controllability for a water-tank system when the time is not large enough*, Annales de l’Institut Henri Poincaré C (2024 online), §1 and main noncontrollability theorem. [DOI](https://doi.org/10.4171/AIHPC/123); [publisher PDF](https://ems.press/content/serial-article-files/47556).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The book conjectures the threshold $2$ in this normalization. The 2024 paper proves the corresponding lower-time obstruction using the quadratic dynamics; it does not give local controllability for every time above the threshold. Searches through 22 September 2026 included tank Saint-Venant sharp/minimal control time and Coron–Koenig–Nguyen continuations. Large-time local controllability and feedback stabilization were distinguished from a proof for all $T>2$.
