# 268 — Minimum-time eradication of an expanding set inside a geographic barrier

**Area:** Geometric optimal control / invasive-species containment

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $V\subset\mathbb R^2$ be a bounded connected Lipschitz domain and $M>0$. A motion is a measurable set $E\subset(0,T)\times V$ of finite perimeter, meaning its indicator has distributional gradient given by a finite vector measure. Write $\partial^*E$ for its reduced boundary, $\nu=(\nu_0,\nu_1,\nu_2)$ for its generalized **inner** unit normal, and $\mathcal H^2$ for surface measure. Require

$$
\int_{\partial^*E\cap((a,b)\times V)}
\max\{-\nu_0+\sqrt{\nu_1^2+\nu_2^2},0\}\,d\mathcal H^2
\leq M(b-a)\qquad(0\leq a<b\leq T).
$$

The slices $\Omega(t)=\{x:(t,x)\in E\}$ must have endpoint traces $\mathbf1_{\Omega(t)}\to\mathbf1_V$ as $t\downarrow0$ and $\mathbf1_{\Omega(t)}\to0$ as $t\uparrow T$, in $L^1(V)$. For every $(V,M)$ permitting such a motion, determine the least $T$ and characterize its minimizers.

This is the published BV formulation. At a smooth front with inward speed $\beta$, effort is $\int_{\partial\Omega(t)\cap V}\max\{1+\beta,0\}\,ds$; the integrated constraint and endpoint traces account for all removal, including possible discontinuities.

## Application

The model asks how to allocate a bounded cleaning or suppression rate when an infestation spreads locally but cannot cross the coastline.

## References

1. A. Bressan, *Results and Open Questions on the Boundary Control of Moving Sets* (2025), [arXiv:2502.06050](https://arxiv.org/abs/2502.06050), §7, Problem 3. Explicit request for minimum-time strategies under geographical constraints.
2. A. Bressan, E. Marchini and V. Staicu, *Optimally Controlled Moving Sets with Geographical Constraints* (2025), [Milan Journal of Mathematics](https://doi.org/10.1007/s00032-025-00419-x), §2, Definition 2.1 and equations (2.5), (2.9)–(2.10); §§4–5 and §17. Supplies BV admissibility and endpoint traces, existence results and special optimality criteria.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The published paper warns that constructions satisfying necessary conditions need not beat all admissible BV strategies. Its sufficient criterion applies when compatible minimum-perimeter slices exist, which fails for general domains. Searches included “Bressan minimum time eradication 2026”, “optimally controlled moving sets geographical constraints solved”, and “optimal eradication moving sets”. No general characterization was located.
