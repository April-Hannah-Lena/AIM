# 167. Sharp enstrophy-limited heat transport in two dimensions

**Area:** Heat transfer and flow optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On $\Omega=(\mathbb R/\mathbb Z)\times(0,1)$, let $u$ range over smooth steady divergence-free velocities, periodic horizontally, with $u=0$ at both walls and $\int_\Omega|\nabla u|^2\le\mathrm{Pe}^2$. Let $T_u$ solve

$$
u\cdot\nabla T_u=\Delta T_u,\qquad T_u(x,0)=1,\qquad T_u(x,1)=0.
$$

Define $M_2(\mathrm{Pe})=\sup_u\int_\Omega|\nabla T_u|^2$. Is there $c>0$ such that $M_2(\mathrm{Pe})\ge c\,\mathrm{Pe}^{2/3}$ for all sufficiently large $\mathrm{Pe}$? Equivalently, can the known upper scaling be achieved without a logarithmic loss in two dimensions?

## Application

This gives the largest heat flux obtainable from planar stirring with a fixed viscous-dissipation budget.

## References

1. Charles R. Doering and Ian Tobasco, *On the Optimal Design of Wall-to-Wall Heat Transport*, Communications on Pure and Applied Mathematics 72 (2019), 2385–2448. [Article](https://doi.org/10.1002/cpa.21832). Main bounds and the branching construction leave a logarithmic gap.

2. Anuj Kumar, *Three dimensional branching pipe flows for optimal scalar transport between walls* (2022). [Paper](https://arxiv.org/abs/2205.03367). Main theorem removes the logarithmic loss by a three-dimensional construction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searches for “two dimensional wall to wall heat transport logarithmic gap 2026” and “three dimensional branching pipe flows optimal scalar transport” located the three-dimensional resolution and two-dimensional numerical studies. Neither gives the required two-dimensional lower bound. The velocity here is optimized freely and need not solve the momentum equation of buoyant convection.
