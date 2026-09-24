# 447. Finite-time collapse in the planar self-steepening Schrödinger equation

**Area:** Derivative dispersive PDEs and optical pulses

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Does there exist $u_0\in\mathcal S(\mathbb R^2;\mathbb C)$ and $0<T<\infty$ such that the equation
$$i\partial_tu+\partial_x^2u+\partial_y^2u+|u|^2u+i\partial_y(|u|^2u)=0,\qquad u(0)=u_0,$$
has a classical solution on $[0,T)$, belonging to $C([0,T);H^m(\mathbb R^2))$ for every integer $m\ge3$, with
$$\limsup_{t\uparrow T}\|u(t)\|_{L^\infty(\mathbb R^2)}=\infty?$$
The derivative coefficient is fixed and nonzero. Thus the question asks for an actual singular solution of the two-dimensional equation, not a dispersionless approximation or a periodic numerical discretization.

## Application

Self-steepening changes pulse velocity according to intensity. A rigorous collapse example would distinguish this correction from mechanisms that arrest concentration in laser propagation.

## References

1. J. Arbunich, C. Klein and C. Sparber, [On a class of derivative Nonlinear Schrödinger-type equations in two spatial dimensions](https://doi.org/10.1051/m2an/2019018), *ESAIM: Mathematical Modelling and Numerical Analysis* **53** (2019), 1477–1505, §3.4, equations (3.5)–(3.6) and Figure 9; [preprint](https://arxiv.org/abs/1805.12351).
2. É. Dumas, D. Lannes and J. Szeftel, [Variants of the focusing NLS equation: derivation, justification, and open problems](https://doi.org/10.1007/978-3-319-23084-9_2), in *Laser Filamentation*, Springer (2016), §4.1.5, equation (68), Open Problem 5.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The ESAIM paper reports apparent amplitude blow-up for Gaussian data in precisely this equation, while other data appear globally regular; these are numerical findings. Searches through the review date for two-dimensional derivative NLS collapse and self-steepening singularities found no rigorous construction satisfying the stated criterion. One-dimensional integrable models and off-axis regularized equations differ from this PDE.
