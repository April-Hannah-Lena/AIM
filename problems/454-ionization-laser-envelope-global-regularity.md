# 454. Global smooth propagation for a laser envelope coupled to ionization

**Area:** Dispersive PDEs and nonlinear optics
**Status:** Open in cited literature; no later resolution located.
**Last checked:** 2026-09-22

## Problem statement

Write $x=(x_1,x_2,z)\in\mathbb R^3$. Fix $\varepsilon,c,c_g,\alpha_4>0$, $\alpha_5\ge0$, and an integer $K\ge2$. Consider a complex envelope $u$ and real electron density $\rho$ satisfying
$$\begin{aligned}i(\partial_t+c_g\partial_z)u+\varepsilon\Delta u+\varepsilon(|u|^2-\rho)u&=-i\varepsilon c\bigl(\alpha_4|u|^{2K-2}u+\alpha_5\rho u\bigr),\\
\partial_t\rho&=\varepsilon\alpha_4|u|^{2K}+\varepsilon\alpha_5\rho|u|^2.\end{aligned}$$
For every Schwartz initial pair $(u_0,\rho_0)$ with $\rho_0\ge0$, must the local solution extend to all $t\ge0$, with $(u,\rho)\in C([0,\infty);H^m(\mathbb R^3))$ for every integer $m\ge3$? The Laplacian is elliptic in all three spatial coordinates, corresponding to anomalous group-velocity dispersion.

## Applied significance

Ionization depletes and defocuses an intense optical pulse. Establishing global regularity would test the mathematical claim that these effects arrest the collapse predicted by the cubic focusing envelope equation.

## References

1. É. Dumas, D. Lannes and J. Szeftel, [Variants of the focusing NLS equation: derivation, justification, and open problems](https://david-lannes.perso.math.cnrs.fr/wp-content/uploads/2019/01/dumaslannesszeftel.pdf), in *Laser Filamentation*, CRM Series in Mathematical Physics, Springer (2016), 19–75, §4.1.2, equation (54), Open Problem 3; [chapter DOI](https://doi.org/10.1007/978-3-319-23084-9_2).
2. A. Couairon and A. Mysyrowicz, [Femtosecond filamentation in transparent media](https://www.teramobile.org/publications/couairon_mysy_filaments.pdf), *Physics Reports* **441** (2007), 47–189, sections on propagation models and plasma generation; [DOI](https://doi.org/10.1016/j.physrep.2006.12.005).

## Status review

The book proves local Sobolev well-posedness and explicitly asks for global existence for this coupled model. Review-date searches for ionization NLS global regularity, the Dumas–Lannes–Szeftel problem, and rigorous arrest of filamentation found no theorem with the displayed large-data quantifiers. Mass dissipation alone and simulations do not provide the requested regularity.
