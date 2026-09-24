# 384. Attainment of the three-dimensional neo-Hookean energy in the regular admissible class

**Area:** Nonlinear elasticity; critical-growth energy minimization

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $\Omega\subset\mathbb R^3$ be a smooth bounded domain, $\widetilde\Omega\Subset\Omega$ a smooth subdomain, and $b:\overline\Omega\to b(\overline\Omega)$ an orientation-preserving bi-Lipschitz homeomorphism. Let $H:(0,\infty)\to[0,\infty)$ be finite and convex with $H(t)\to\infty$ as $t\downarrow0$ and $H(t)/t\to\infty$ as $t\to\infty$. Put
$$E(u)=\int_\Omega\bigl(|Du|^2+H(\det Du)\bigr)\,dx.$$
Let $\mathcal A$ consist of $u\in H^1(\Omega;\mathbb R^3)$ that equal $b$ on $\Omega\setminus\widetilde\Omega$, are one-to-one almost everywhere, satisfy $\det Du>0$ almost everywhere and $E(u)<\infty$, and obey, for every $g\in C_c^1(\mathbb R^3;\mathbb R^3)$,
$$\operatorname{Div}\bigl((\operatorname{adj}Du)g(u)\bigr)=(\operatorname{div}g)(u)\det Du\quad\hbox{in distributions}.$$
Here $Du=(\partial_j u_i)_{ij}$ and $\operatorname{adj}Du=(\operatorname{cof}Du)^T$. Whenever $\mathcal A\ne\varnothing$, must $\inf_{u\in\mathcal A}E(u)$ be attained by an element of $\mathcal A$?

## Application

The quadratic stretch energy is the standard neo-Hookean model for a compressible elastic solid. Attainment would justify equilibrium deformations without interpenetration or hidden singular creation of material volume.

## References

1. M. Barchiesi, D. Henao, C. Mora-Corral and R. Rodiac, [*A relaxation approach to the minimisation of the neo-Hookean energy in 3D*](https://arxiv.org/abs/2311.02952), SIAM Journal on Mathematical Analysis 56 (2024), 7830–7845, §1.2, admissible class and main relaxation theorem; DOI [10.1137/23M1614547](https://doi.org/10.1137/23M1614547).
2. M. Barchiesi, D. Henao, C. Mora-Corral and R. Rodiac, [*A Lavrentiev phenomenon in the neo-Hookean model*](https://arxiv.org/abs/2603.22873), preprint (2026), §1 and Theorem 1.1.
3. D. Kalayanamit, [*Sobolev regularity of the inverse for minimizers of the neo-Hookean energy satisfying condition INV*](https://arxiv.org/abs/2405.12156), Proceedings of the Royal Society of Edinburgh A, published online (2025), main inverse-regularity theorem.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using neo-Hookean minimizer existence, relaxation, inverse regularity and the new Lavrentiev example. The SIAM theorem minimizes a modified energy on a larger class; the extra term penalizes the singular derivative of the inverse. Kalayanamit's theorem requires the relevant topological condition. The March 2026 example gives a strict gap between the original energy on the regular class and its minimum on a weak closure. That disproves a particular unrelaxed closure strategy, but does not show nonattainment of the infimum restricted to the class displayed here. Neither theorem proves this attainment assertion or gives a counterexample to it. This critical quadratic-growth question is distinct from supercritical quasiconvex existence.
