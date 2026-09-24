# 372. Does a bounded interface slope prevent two-phase Muskat singularities?

**Area:** Porous-media interfaces; free boundaries

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $f_0\in\bigcap_{k\ge0}H^k(\mathbb R)$ be real and let $f$ be the classical solution on its maximal interval $[0,T_*)$ of
$$\partial_tf(t,x)=\operatorname{PV}\int_{\mathbb R}\frac{\alpha[\partial_xf(t,x)-\partial_xf(t,x-\alpha)]}{\alpha^2+[f(t,x)-f(t,x-\alpha)]^2}\,d\alpha,\qquad f(0)=f_0.$$
This is the equal-viscosity, zero-surface-tension, two-phase Muskat equation on the whole plane, normalized with the heavier fluid below the graph. If $T_*<\infty$ and $\sup_{t<T_*}\|\partial_xf(t)\|_\infty<\infty$, must $f$ extend as a classical solution beyond $T_*$? No common modulus of continuity of $\partial_x f(t)$ is assumed.

## Application

The criterion asks whether finite slopes alone preclude an interface singularity in the displacement of one fluid by another through a porous medium. It separates true loss of interface smoothness from overturning of a graph.

## References

1. P. Constantin, F. Gancedo, R. Shvydkoy and V. Vicol, [*Global regularity for 2D Muskat equations with finite slope*](https://cims.nyu.edu/~vicol/CGSV1.pdf), Annales de l'Institut Henri Poincaré C, Analyse non linéaire 34 (2017), 1041–1074, §1.3 and Theorem 1.2.
2. A. Zlatoš, [*The 2D Muskat Problem II: Stable Regime Small Data Singularity on the Half-plane*](https://arxiv.org/abs/2401.14660), revised preprint (2024), §1, discussion immediately before the half-plane model.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using bounded-slope Muskat continuation, stable-regime whole-plane singularities, and 2025–2026 developments. The first theorem additionally assumes a uniform modulus of continuity of the slope. Zlatoš explicitly retains the bounded-slope whole-plane question while constructing singularities on the half-plane, where contact with an impermeable bottom changes the problem. One-phase global theorems, splash constructions with a dry region and post-overturning singularities have different hypotheses. No matching continuation theorem or counterexample was located.
