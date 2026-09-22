# 374. Are bounded ancient Landau–Coulomb distributions necessarily Maxwellians?

**Area:** Plasma collisions; kinetic regularity

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

Let $f:(-\infty,0]\times\mathbb R^3\to[0,1]$ be a smooth classical solution of the spatially homogeneous Landau–Coulomb equation
$$\partial_tf=\nabla_v\cdot(A[f]\nabla_vf-f\nabla_va[f]),\quad A[f]\,(v)=\frac1{8\pi}\int_{\mathbb R^3}\frac{I-\widehat{v-w}\otimes\widehat{v-w}}{|v-w|}f(w)\,dw,\quad a[f]\,(v)=\frac1{4\pi}\int_{\mathbb R^3}\frac{f(w)}{|v-w|}\,dw,$$
where $\widehat z=z/|z|$. Suppose $\int f(t,v)(1+|v|^2)^{-1/2}\,dv<\infty$ for every $t\le0$. Must $f$ be stationary and equal to $A_0e^{-b|v-c|^2}$ for constants $A_0\ge0$, $b>0$, $c\in\mathbb R^3$? Ordinary mass, energy and entropy are not assumed finite. The zero solution is included.

## Applied significance

Ancient solutions arise when rescaling a concentrating collisional plasma. Their classification would constrain possible small-scale kinetic structures even when the rescaling destroys global mass and energy bounds.

## References

1. L. Silvestre, [*Regularity estimates and open problems in kinetic equations*](https://arxiv.org/abs/2204.06401), proceedings survey (2022), §7, Conjecture 7.5.
2. N. Guillen and L. Silvestre, [*The Landau equation does not blow up*](https://arxiv.org/abs/2311.09420), Acta Mathematica 234 (2025), 315–375, main global-existence theorem.
3. W. Golding, M. Gualdani and A. Loher, [*Global Smooth Solutions to the Landau–Coulomb Equation in $L^{3/2}$*](https://doi.org/10.1007/s00205-025-02107-x), Archive for Rational Mechanics and Analysis 249 (2025), article 34, §1, second item under “Open Problems.”

## Status review

Checked on 22 September 2026 using ancient Landau solutions, Maxwellian Liouville classification, and bounded infinite-mass solutions. Guillen–Silvestre settle finite-time blowup for an important class of finite-mass initial data; that result is not a classification of all ancient solutions in the much larger class here. The 2025 paper independently lists the locally finite-mass bounded class as an outstanding problem. No later proof or counterexample to the stated Conjecture 7.5 was located.
