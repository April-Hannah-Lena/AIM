# 293. Spatial coexistence despite extinction in the mean-field game

**Area:** Spatial ecology and evolutionary games

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

At each $x\in\mathbb Z^2$ let $H_x,D_x\in\mathbb N_0$ count hawks and doves. Individuals migrate at rate $\mu$ to a uniform nearest neighbor and die from crowding at rate $\kappa(H_x+D_x)$. For $N_L=\{z:\|z\|_\infty\le L\}$ set $p_x=\sum_{z\in N_L}H_{x+z}/\sum_{z\in N_L}(H_{x+z}+D_{x+z})$, with $p_x=0$ when the denominator vanishes. The additional per-individual game rate is $r_H=-0.6p_x+0.9(1-p_x)$ for hawks and $r_D=-0.9p_x+0.37(1-p_x)$ for doves: positive rate creates an offspring at $x$, negative rate adds death at its absolute value. Do some finite $L\ge1$ and $\mu,\kappa>0$ admit a translation-invariant stationary law with finite mean population per site, supported on configurations containing infinitely many individuals of both types?

## Applied significance

This tests whether local demographic fluctuations sustain species that a well-mixed approximation predicts will disappear.

## References

- [Rick Durrett, *Interacting Particle Systems: Ideas, Techniques, Applications*, author book manuscript accessed 13 September 2026](https://sites.math.duke.edu/~rtd/PASTA/PASTAcurrent.pdf), §3.2, Case 3, Open Problem 3.2.3, printed p. 89.
- [Rick Durrett and Simon A. Levin, *The Importance of Being Discrete (and Spatial)*, Theoretical Population Biology 46 (1994), 363–394](https://doi.org/10.1006/tpbi.1994.1032), spatial game model and simulations.

## Status review

The book explicitly requests a coexistence proof. Neighborhood frequency is normalized by the neighborhood population here; the manuscript’s displayed denominator omits hats. Finite simulations do not prove existence of the stated invariant law.

Search topics checked on 2026-09-13: `Durrett Levin 1994 hawk dove negative payoffs spatial coexistence evolutionary suicide rigorous proof 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
