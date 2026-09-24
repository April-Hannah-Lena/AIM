# 462. Global quadratic reaction–diffusion systems with general transport noise

**Area:** Stochastic PDEs; chemical and population kinetics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $d\ge2$, $N\ge2$, and $\nu_i>0$. On $\mathbb T^d$, consider

$$
du_i=(\nu_i\Delta u_i+f_i(u))\,dt+\sum_{k=1}^K\bigl[b_{ki}(x)\cdot\nabla u_i+g_{ki}(u)\bigr]dW^k_t.
$$

The vector fields $b_{ki}$ are smooth and divergence-free, and, for each $i$,

$$
\nu_i I-\tfrac12\sum_k b_{ki}\otimes b_{ki}\ge\delta I\quad\hbox{for some }\delta>0.
$$

The smooth functions $g_i:\mathbb R^N\to\mathbb R^K$ are globally Lipschitz and vanish on $\{u\ge0:u_i=0\}$. The locally Lipschitz reactions satisfy, for nonnegative $u,v$,

$$
f_i(u)\ge0\ \hbox{if }u_i=0,\qquad \sum_i f_i(u)\le C(1+\sum_i u_i),
$$



$$
|f(u)-f(v)|\le C(1+|u|+|v|)|u-v|.
$$

For every nonnegative smooth initial condition, is the maximal local strong solution global almost surely, with $\sup_{t\le T}\|u(t)\|_\infty<\infty$ almost surely for each finite $T$? Local solutions are understood in the parabolic strong-solution class, continuous in space and time and satisfying the integral SPDE; the continuation criterion is divergence of the spatial supremum norm. The transport fields may differ between species and are arbitrary subject to the displayed parabolicity condition.

## Application

Quadratic interactions model bimolecular chemistry and population interactions. The question tests whether mass control prevents concentration singularities under random advection.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 8 and §8.2. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. A. Agresti and M. Veraar, *Reaction-Diffusion Equations with Transport Noise and Critical Superlinear Diffusion: Global Well-Posedness of Weakly Dissipative Systems*, SIAM J. Math. Anal. (2024). [Article](https://doi.org/10.1137/23M1562482).
3. A. Agresti, M. Kniely and B. Q. Tang, *Global classical solutions by transport noise for reaction–diffusion systems with entropy dissipation* (2026 preprint), Introduction. [Preprint](https://arxiv.org/abs/2608.13332).
4. D. Milesis and M. Salins, *Global in time solutions to stochastic reaction-diffusion systems with superlinear reactions satisfying a triangular control of mass* (2026 preprint). [Preprint](https://arxiv.org/abs/2604.06645).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The survey explicitly poses this quadratic mass-control extension. Searches on 2026-09-22 checked the subsequent stochastic De Giorgi paper and the two 2026 global-existence papers. The August result selects a special transport noise and gives arbitrarily high probability, while the desired assertion quantifies over every admissible noise and asks probability one. Milesis–Salins impose triangular mass control and noise without spatial derivatives. Neither covers these species-dependent transport fields and general quadratic reactions. Deterministic quadratic mass-control global existence is already known and is not counted as open here.
