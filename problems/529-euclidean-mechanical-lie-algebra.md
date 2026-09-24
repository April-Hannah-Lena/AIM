# 529. Universal identities for Euclidean mechanical Lie brackets

**Area:** Geometric numerical integration and numerical PDEs

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Over $\mathbb R$, let $\mathfrak P$ consist of Lie algebras $L=\bigoplus_{n\ge0}L_n$ satisfying

$$
[L_n,L_m]\subseteq L_{n+m-1}\quad(n+m>0),\qquad [L_0,L_0]=0.
$$

Let $F$ be freely generated in this class by $A$ of degree two and $B$ of degree zero: every degree-preserving assignment of these generators extends uniquely to a homomorphism.

For $d\ge1$ and $V\in C^\infty(\mathbb R^d;\mathbb R)$, define

$$
\Phi_V:F\longrightarrow C^\infty_{\mathrm{pol}}(\mathbb R^{2d}),\qquad A\mapsto\tfrac12|p|^2,\quad B\mapsto V(q).
$$

The target consists of smooth functions polynomial in $p$, with bracket

$$
\{f,g\}=\sum_{j=1}^d(\partial_{q_j}f\,\partial_{p_j}g-\partial_{p_j}f\,\partial_{q_j}g).
$$

Prove or refute

$$
\bigcap_{d\ge1}\ \bigcap_{V\in C^\infty(\mathbb R^d;\mathbb R)}\ker\Phi_V=\{0\}.
$$

The quantifier ranges over all dimensions and potentials; injectivity for each individual potential is not asserted.

## Application

The answer determines whether mechanical splitting integrators have additional universal order-condition reductions. It also bears on splitting the Laplacian and potential in Schrödinger evolution.

## References

1. R. I. McLachlan and A. Murua, [The Lie algebra of classical mechanics](https://doi.org/10.3934/jcd.2019017), Journal of Computational Dynamics **6**, 345–360 (2019), Definitions 1–4 and Conjecture 1. [Preprint](https://arxiv.org/abs/1905.07554).
2. S. Blanes, F. Casas and A. Murua, [Splitting methods for differential equations](https://doi.org/10.1017/S0962492923000077), Acta Numerica (2024), discussion of Runge–Kutta–Nyström order conditions.

## Status review

Reference [2] retains the conjecture. Searches on 24 September 2026 found no matching solution or announcement, including indexed arXiv, Zenodo, GitHub and Palomar searches.
