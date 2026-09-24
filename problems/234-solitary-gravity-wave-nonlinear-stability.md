# 234. Nonlinear orbital stability of small solitary gravity waves

**Area:** Free-surface fluid dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Consider two-dimensional irrotational water of unit rest depth and gravity, with no surface tension. Its surface variables $(\eta,\psi)$ on $\mathbb R$ satisfy
$$\eta_t=G(\eta)\psi,\qquad \psi_t=-\eta-\frac12\psi_x^2+\frac{(G(\eta)\psi+\eta_x\psi_x)^2}{2(1+\eta_x^2)}.$$
Here $\psi$ is the surface velocity potential, and $G(\eta)\psi=(\phi_y-\eta_x\phi_x)|_{y=\eta}$, where $\Delta\phi=0$ in $-1<y<\eta(x)$, $\phi_y|_{y=-1}=0$, and $\phi|_{y=\eta}=\psi$. Potentials are taken modulo constants.

Let $Q_c=(\eta_c,\psi_c)$ be the classical branch of smooth solitary elevation waves of speed $c>1$ bifurcating from zero at $c=1$; thus $Q_c(x-ct)$ solves this system and $(\eta_c,\psi_c')$ decays at infinity. Define $K$ by the Fourier multiplier $\widehat{Kf}(\xi)=\sqrt{|\xi|\tanh|\xi|}\,\widehat f(\xi)$ and $\|(a,b)\|_{X^s}=\|a\|_{H^s}+\|Kb\|_{H^s}$.

Does there exist $c_*>1$ such that, for every $c\in(1,c_*)$ and $\varepsilon>0$, some $\delta>0$ has the following property? Every smooth initial state with positive depth, finite $\|Q_0-Q_c\|_{X^s}$ for all integers $s\geq0$, and $\|Q_0-Q_c\|_{X^6}<\delta$ generates a global smooth graph solution satisfying
$$\sup_{t\geq0}\inf_{a\in\mathbb R}\|Q(t)-Q_c(\cdot-a)\|_{X^0}<\varepsilon.$$

## Application

Small solitary pulses travel long distances in shallow water. This asks whether their observed persistence survives perturbations under the full free-boundary equations.

## References

- Robert L. Pego and Shu-Ming Sun, [*Asymptotic linear stability of solitary water waves*](https://www.math.cmu.edu/cna/Publications/publications2010/015abs/10-CNA-015.pdf) (2010 preprint; 2016 publication), §1, p. 3, and the linear-stability theorems: expressly leaves nonlinear stability open.
- Frédéric Rousset and Changzhen Sun, [*Transverse linear stability of one-dimensional solitary gravity water waves*](https://arxiv.org/html/2402.11115v1) (2024 preprint; 2025 publication), introduction before §1.1: distinguishes gravity from capillary results and reviews the unresolved nonlinear problem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “nonlinear orbital stability small solitary gravity water waves 2026”, “Pego Sun nonlinear stability solved”, and the 2025 Rousset–Sun result. Located linear stability and nonlinear results for reduced equations or capillary waves. None establishes the displayed unconditional global orbital-stability formulation for pure gravity. This states a precise smooth-data version of the published nonlinear question; the chosen high-regularity initial norm is a formulation choice, not a claimed quotation.
