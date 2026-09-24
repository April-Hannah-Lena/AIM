# 365. Global classical solutions for repulsive relativistic Vlasov–Poisson

**Area:** Plasma kinetics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For every nonnegative $`f_0\in C_c^\infty(\mathbb R_x^3\times\mathbb R_p^3)`$, does the system

```math
\partial_tf+\frac{p}{\sqrt{1+|p|^2}}\cdot\nabla_xf+E\cdot\nabla_pf=0,\quad E=-\nabla_x\Phi,\quad-\Delta_x\Phi=4\pi\int_{\mathbb R^3}f\,dp,\quad\Phi(x)\to0\ (|x|\to\infty)
```

have a unique global classical solution with $`f(0)=f_0`$? More precisely, must its momentum support remain bounded on each finite time interval? No symmetry or smallness assumption is allowed. The sign displayed is repulsive.

## Application

This electrostatic kinetic approximation combines relativistic particle velocities with Coulomb repulsion. The question asks whether a smooth plasma distribution can develop arbitrarily large momenta in finite time.

## References

1. X. Wang, [*Global solution of the 3D relativistic Vlasov-Poisson system for a class of large data*](https://arxiv.org/abs/2003.14191), revised preprint (2022), §1, equation (1.1), Theorems 1.1–1.2 and Remark 1.2.
2. R. T. Glassey, [*The Cauchy Problem in Kinetic Theory*](https://doi.org/10.1137/1.9781611971477), SIAM (1996), Chapter 4, §§4.1–4.6, pp. 117–135 (classical nonrelativistic theory and gravitational comparison).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using relativistic Vlasov–Poisson large-data global regularity, repulsive sign, and later citations to Wang. Wang explicitly retains the unrestricted problem and proves spherical and constrained cylindrical cases. Classical nonrelativistic Vlasov–Poisson global existence uses a different transport velocity. The September 2026 point-charge paper [arXiv:2609.00973](https://arxiv.org/abs/2609.00973) assumes spherical symmetry and small data; it does not establish the assertion above. No matching general theorem was located.
