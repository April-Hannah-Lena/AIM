# 278. Abrupt equilibration on every family of transitive expanders

**Area:** Transport and sampling on homogeneous networks

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $G_n$ be connected vertex-transitive finite simple graphs with $|V(G_n)|\to\infty$, degrees bounded by a fixed $D$, and lazy-random-walk gaps bounded below by a fixed $\gamma>0$. A lazy step stays put with probability $1/2$ and otherwise chooses a uniform neighbor. Define $t_n(\varepsilon)=\min\{t:\max_x\|P_n^t(x,\cdot)-\mathrm{Unif}(V(G_n))\|_{\rm TV}\le\varepsilon\}$. Must $t_n(\varepsilon)/t_n(1-\varepsilon)\to1$ for every $0<\varepsilon<1/2$?

## Application

This asks whether homogeneous, well-connected transport networks have a sharply predictable time to reach equilibrium.

## References

- [David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, second edition (2017)](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf), Chapter 26, Question 5.
- [Justin Salez, *The varentropy criterion is sharp on expanders* (2024)](https://www.numdam.org/item/10.5802/ahl.199.pdf), Conjecture 1.7.
- [Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon* (2025)](https://arxiv.org/abs/2508.21055), §2.2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Ramanujan and other structured families are covered by existing cutoff theorems. The recent survey retains the arbitrary vertex-transitive expander case. Criteria requiring additional entropy or local functional-inequality bounds do not establish those bounds from transitivity alone.

Search topics checked on 2026-09-13: `vertex transitive expander cutoff conjecture proof 2026 local product condition Pedrotti Salez`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
