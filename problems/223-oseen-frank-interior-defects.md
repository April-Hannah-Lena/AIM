# 223. Finiteness of interior defects in Oseen–Frank minimizers

**Area:** Liquid-crystal continuum mechanics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\Omega\subset\mathbb R^3$ be a bounded smooth domain, let $g:\partial\Omega\to\mathbb S^2$ be smooth with a nonempty $H^1$ extension class, and let $k_1,k_2,k_3>0$. For $n\in H^1(\Omega;\mathbb S^2)$ with trace $g$, set
$$E(n)=\frac12\int_\Omega\left[k_1(\operatorname{div}n)^2+k_2(n\cdot\operatorname{curl}n)^2+k_3|n\times\operatorname{curl}n|^2\right]dx.$$
For every global minimizer, is its interior singular set locally finite? Here a point is singular if no neighborhood admits a smooth representative of $n$; locally finite means that every compact subset of $\Omega$ contains only finitely many such points.

## Application

Point-defect descriptions underlie simulations and optical predictions for nematics with unequal splay, twist and bend constants. A dimension bound alone does not justify a finite collection of defects.

## References

- Fang-Hua Lin and Changyou Wang, [*Recent developments of analysis for hydrodynamic flow of nematic liquid crystals*](https://pmc.ncbi.nlm.nih.gov/articles/PMC4223669/) (2014), Question 1.4 and Theorem 1.1: the defect-finiteness question and partial regularity.
- Zhiyuan Dai, Haotong Fu, Huaijie Wang and Wei Wang, [*Boundary regularity for Oseen–Frank minimizers with arbitrary positive splay, twist, and bend constants*](https://arxiv.org/abs/2608.22287) (2026 preprint), §1.1 and Theorem 1.1: boundary regularity for the full range of positive constants.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “Oseen Frank minimizer interior singular set finite points” and “Oseen Frank regularity 2025 2026”. The August 2026 preprint proves smoothness in a neighborhood of the boundary. Its remaining interior estimate, like the older theory, does not establish isolated interior defects for arbitrary elastic constants. The omitted saddle-splay term is a null Lagrangian under the fixed trace and does not change the minimizing question.
