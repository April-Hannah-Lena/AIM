# 136 — Saari's constant-inertia conjecture for planar gravitation

**Area:** Celestial mechanics / rigid gravitational motions

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix $N\ge4$ and masses $m_1,\ldots,m_N>0$. Let collision-free planar positions $q_i:J\to\mathbb R^2$ solve Newton's equations on an open time interval $J$:

$$
\ddot q_i=\sum_{j\ne i}m_j\frac{q_j-q_i}{|q_j-q_i|^3},
\qquad \sum_i m_iq_i=0.
$$

If the polar moment of inertia $I(t)=\sum_i m_i|q_i(t)|^2$ is constant, must the solution be a relative equilibrium? That is, must there be a constant $\omega$ such that $q_i(t)=R_{\omega(t-t_0)}q_i(t_0)$ for all $i,t$, where $R_\theta$ is planar rotation by $\theta$?

## Application

This asks whether constant spatial spread forces an isolated gravitational system into rigid rotation, connecting observable bulk quantities with the classification of orbital motions.

## References

1. F. Diacu, E. Pérez-Chavela and M. Santoprete, *Saari's Conjecture for the Collinear n-Body Problem* (2005), [Transactions of the AMS 357, 4215–4223](https://doi.org/10.1090/S0002-9947-04-03606-2), §1 and main theorem. States the Newtonian conjecture and proves the collinear case.
2. T. Schmah and C. Stoica, *Saari's Conjecture is True for Generic Vector Fields* (2007), [author preprint, arXiv:math/0510012](https://arxiv.org/abs/math/0510012), introduction and genericity theorem. Explains the planar mechanical formulation; generic vector fields do not include a verification of every Newtonian mass tuple.
3. P. Tibboel, *A proof of Saari's conjecture* (2022; withdrawn 2024), [arXiv:2212.09718](https://arxiv.org/abs/2212.09718), version-5 withdrawal notice. Documents an unsuccessful claimed general solution.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The planar three-body and collinear cases are established. Tibboel withdrew the general proof on March 22, 2024, reporting an incorrect main theorem and a proof error. Searches included “Saari conjecture planar n body 2025 2026 proof”, “Saari constant moment inertia solution” and “Tibboel Saari withdrawal”. No later valid general resolution was located.
