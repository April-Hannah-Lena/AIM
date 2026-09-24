# 449. Optimal dimension for bounded subquadratic p-Laplace extremal states

**Area:** Singular quasilinear elliptic PDEs

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $1<p<2$ and let $d$ be an integer with $2\le d<p+4p/(p-1)$. Let $\Omega\subset\mathbb R^d$ be bounded, smooth and strictly convex. Suppose $f\in C^2([0,\infty))$ is positive, strictly increasing and convex, and $f(t)/t^{p-1}\to\infty$. For
$$-\operatorname{div}(|\nabla u|^{p-2}\nabla u)=\lambda f(u),\qquad u\in W^{1,p}_0(\Omega),\quad u>0,$$
let $u_\lambda$ be the minimal bounded weak solution for $0<\lambda<\lambda^*$, where $\lambda^*$ is the supremum of parameters with such a solution. Must the monotone extremal limit $u^*=\lim_{\lambda\uparrow\lambda^*}u_\lambda$ belong to $L^\infty(\Omega)$? The weak equation is tested against $C_c^\infty(\Omega)$.

## Application

These equilibria combine a subquadratic constitutive law with a growing reaction. The critical dimension identifies when a stable branch can develop an unbounded concentration at the limiting forcing level.

## References

1. X. Cabré, [Stable solutions to reaction-diffusion elliptic problems](https://arxiv.org/abs/2603.03161), lecture survey (2026), §3.5.2.
2. X. Cabré, P. Miraglio and M. Sanchón, [Optimal regularity of stable solutions to nonlinear equations involving the p-Laplacian](https://doi.org/10.1515/acv-2020-0055), *Advances in Calculus of Variations* **15** (2022), 749–785, introduction, Theorem 1.1 and §1.2; [preprint](https://arxiv.org/abs/2006.01445).
3. M. Qu and Z. Wang, [Endpoint Morrey interior regularity of stable solutions to the p-Laplace equation](https://doi.org/10.3934/era.2026210), *Electronic Research Archive* **34** (2026), 4765–4776, Theorems 1.1–1.3.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The optimal threshold is known for p≥2, and for special nonlinearities or radial data. The subquadratic theory in the second reference reaches a smaller dimensional range. The June 2026 paper improves endpoint Morrey integrability above that smaller threshold; its estimates do not imply boundedness throughout the range in this question. Searches through the review date found no removal of the remaining dimensional gap.
