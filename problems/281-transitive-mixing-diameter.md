# 281. A diameter bound for diffusion to uniform equilibrium

**Area:** Diffusion on symmetric networks

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

Let $G$ be any connected finite vertex-transitive simple graph with at least two vertices, degree $d$ and graph diameter $D$. Let $A_G$ be its adjacency matrix. For the lazy simple random walk $P=\tfrac12I+\tfrac1{2d}A_G$, let $t_{\rm mix}$ be the smallest integer $t$ for which $\max_x\|P^t(x,\cdot)-\mathrm{Unif}(V(G))\|_{\rm TV}\le1/4$. Is there a universal constant $C$ with $t_{\rm mix}\le C dD^2$ for every such $G$?

## Applied significance

The bound would estimate homogenization time from network size in space and local connectivity, without computing its full transition spectrum.

## References

- [David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, second edition (2017)](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf), Chapter 26, Question 8 and Theorem 13.26.
- [Sam Olesker-Taylor and Luca Zanetti, *Geometric bounds on the fastest mixing Markov chain* (2024)](https://link.springer.com/article/10.1007/s00440-023-01257-x), Introduction and diameter bounds for optimized chains.

## Status review

A bound of this order for relaxation time is known. Recent geometric results allow changing edge weights, transition rates, or the stationary law; the present question fixes the ordinary lazy walk and its uniform equilibrium.

Search topics checked on 2026-09-13: `vertex transitive lazy walk mixing diameter squared degree conjecture 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
