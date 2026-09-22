# 377. Continuation of the cutoff Boltzmann flow from macroscopic bounds

**Area:** Rarefied gases; nonlinear kinetic transport

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-22

## Problem statement

Let $f\ge0$ be a smooth solution on $[0,T)\times\mathbb T^3_x\times\mathbb R^3_v$, $T<\infty$, of the hard-sphere cutoff equation
$$\partial_tf+v\cdot\nabla_xf=\int_{\mathbb R^3}\int_{\mathbb S^2}|v-v_*|\,[f(v')f(v_*')-f(v)f(v_*)]\,d\sigma\,dv_*,$$
where $v'=(v+v_*)/2+|v-v_*|\sigma/2$ and $v_*'=(v+v_*)/2-|v-v_*|\sigma/2$; all factors share $(t,x)$. Assume $f(0)$ and all its derivatives decay faster than any inverse power of $|v|$. Suppose constants $m_0,M_0,E_0>0$ and $H_0\in\mathbb R$ satisfy, for all $(t,x)$,
$$m_0\le\int f\,dv\le M_0,\qquad\int |v|^2f\,dv\le E_0,\qquad\int f\log f\,dv\le H_0.$$
Must $f$ extend beyond $T$ as a smooth solution with the same rapid velocity decay? No a priori bound on $f$ itself or on its derivatives is assumed.

## Applied significance

The criterion would distinguish breakdown caused by concentration of observable gas density, energy or entropy from a loss of microscopic smoothness invisible to those quantities.

## References

1. L. Silvestre, [*Regularity estimates and open problems in kinetic equations*](https://arxiv.org/abs/2204.06401), proceedings survey (2022), §8.5 and hydrodynamic assumptions (3.1)–(3.3).
2. R. T. Glassey, [*The Cauchy Problem in Kinetic Theory*](https://doi.org/10.1137/1.9781611971477), SIAM (1996), §§1.2–1.5, pp. 5–14, and Chapter 3, §§3.6–3.14 (hard-sphere collision operator and perturbative Cauchy theory).

## Status review

Checked on 22 September 2026 using cutoff Boltzmann continuation, hydrodynamic bounds, mass energy entropy and hard-sphere regularity. Silvestre explicitly proposes propagation of initial regularity under these assumptions for the cutoff equation. The 2025 pressure-and-moment conditional-regularity theorem concerns non-cutoff collisions and uses the regularizing angular singularity; it does not settle the hard-sphere cutoff problem. Global smooth results close to Maxwellians impose smallness. No matching large-data continuation criterion was located.
