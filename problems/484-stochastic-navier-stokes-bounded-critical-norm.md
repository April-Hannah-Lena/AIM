# 484. A bounded critical norm continuation criterion for stochastic Navier–Stokes

**Area:** Stochastic fluid PDEs; regularity criteria

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

On $\mathbb R^3$, let $P$ be the Helmholtz projection onto divergence-free vector fields and consider the Itô equation

$$
du=[\nu\Delta u-P((u\cdot\nabla)u)]\,dt+
\sum_{k=1}^K P((b_k\cdot\nabla)u)\,dW^k_t.
$$

Here $\nu>0$, the $W^k$ are independent real Brownian motions, and $b_k\in C_c^\infty(\mathbb R^3;\mathbb R^3)$ are divergence-free, not all zero, and satisfy

$$
\tfrac12\sum_k|b_k(x)\cdot\xi|^2\le(\nu-\eta)|\xi|^2
\quad(x,\xi\in\mathbb R^3)
$$

for some $\eta>0$. For a smooth compactly supported divergence-free $u_0$, let $(u,\tau)$ be the maximal local strong solution in the critical class
$C([0,\tau);B^{-1/4}_{4,4})\cap L^4_{\mathrm{loc}}([0,\tau),t^{1/2}dt;H^{1/2,4})$.
Is

$$
\mathbb P\!\left(\tau<\infty,\ \sup_{0\le t<\tau}\|u(t)\|_{B^{-1/4}_{4,4}(\mathbb R^3)}<\infty\right)=0?
$$

Use the inhomogeneous Besov norm $\|u\|_{B^{-1/4}_{4,4}}=(\sum_{j\ge-1}2^{-j}\|\Delta_j u\|_4^4)^{1/4}$ for a smooth dyadic frequency partition. The question requires boundedness alone, without assuming that $u(t)$ has a limit at $\tau$.

## Application

Such a criterion would identify a measurable threshold for loss of regularity in fluid models with spatially varying random transport.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Theorems 8.26–8.27 and Open Problem 11. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. A. Agresti and M. Veraar, *Stochastic Navier–Stokes equations for turbulent flows in critical spaces*, Commun. Math. Phys. (2024), critical local theory and continuation criteria. [Preprint](https://arxiv.org/abs/2107.03953).
3. A. Agresti, *On the absence of blow-up in the 3D Navier–Stokes equations with transport noise* (2026 preprint). [Current preprint](https://arxiv.org/abs/2607.15140).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This fixes the survey's parameters to $(p,\delta,\kappa,q)=(4,-1/2,1/2,4)$ and asks for its explicitly open improvement from existence of a critical-space limit to boundedness. The 2026 preprint proves high-probability global smoothness for suitably chosen noise, rather than this continuation criterion for arbitrary admissible spatial fields. Searches on 2026-09-22 for stochastic endpoint Serrin criteria and bounded critical Besov norms found no matching resolution. Constant transport fields, removable by translation, do not settle the spatially varying case.
