# 432. Sharp gradient regularity for higher-dimensional p-Poisson equations

**Area:** Nonlinear elliptic PDEs and nonlinear diffusion

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

For every integer $d\ge3$ and every $p>2$, does there exist $C=C(d,p)$ such that each weak solution $u\in W^{1,p}(B_1)$ of
$$-\operatorname{div}(|\nabla u|^{p-2}\nabla u)=f,\qquad f\in L^\infty(B_1),$$
satisfies
$$\|u\|_{C^{1,1/(p-1)}(\overline B_{1/2})}\le C\left(\|u\|_{L^p(B_1)}+\|f\|_{L^\infty(B_1)}^{1/(p-1)}\right)?$$
Here $B_r$ is the centered Euclidean ball in $\mathbb R^d$, and the weak equation means $\int |\nabla u|^{p-2}\nabla u\cdot\nabla\varphi=\int f\varphi$ for all compactly supported smooth $\varphi$. The endpoint Hölder exponent, not merely every smaller exponent, is requested.

## Application

The p-Poisson equation models stationary nonlinear conduction and power-law diffusion. The endpoint estimate quantifies how concentrated forcing can change a flux and gives the natural regularity scale near degenerate critical points.

## References

1. S.-C. Lee and T. Lee, [The C-p-prime regularity conjecture near p = 2](https://arxiv.org/abs/2609.09966), preprint (2026), Conjecture 1.1 and Theorem 1.2.
2. D. J. Araújo, E. V. Teixeira and J. M. Urbano, [A proof of the C-p-prime-regularity conjecture in the plane](https://doi.org/10.1016/j.aim.2017.06.027), *Advances in Mathematics* **316** (2017), 541–553, main theorem; [preprint](https://arxiv.org/abs/1901.03827).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 9, 2026 preprint was checked directly: Theorem 1.2 covers $2<p<2+\varepsilon_d$, not arbitrary $p>2$. The planar theorem and higher-dimensional special classes also do not cover the quantifiers above. Searches for the conjecture, endpoint p-Poisson regularity, and 2026 proofs located no full higher-dimensional result beyond this near-quadratic range.
