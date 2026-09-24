# 182. The density conjecture for activated random walk on the square lattice

**Area:** Self-organized criticality

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Fix a sleep rate $\lambda>0$. On $\mathbb Z^2$, active particles perform independent continuous-time simple random walks at jump rate one. A lone active particle sleeps at rate $\lambda$; arrival of an active particle wakes a sleeping one. Define $\zeta_c(\lambda)$ as the infimum of densities $\zeta$ for which the system started with iid Poisson$(\zeta)$ active particles fails to fixate almost surely; fixation means finitely many jumps at every site.

For $\Lambda_n=[-n,n]^2\cap\mathbb Z^2$, kill particles that jump out. On stable configurations (at most one sleeping particle per site), repeatedly add one active particle at a uniformly chosen site and run to stabilization. Let $\pi_n$ be the stationary law of this finite Markov chain, and $N(\eta)$ its number of sleeping particles. Is
$$\lim_{n\to\infty}\frac{\mathbb E_{\pi_n}N}{|\Lambda_n|}=\zeta_c(\lambda)$$
for every $\lambda>0$?

## Application

The equality would connect the density selected by slow driving and boundary dissipation with the threshold of the closed system, a central prediction of self-organized criticality.

## References

- [Christopher Hoffman, Tobias Johnson and Matthew Junge, *The density conjecture for activated random walk* (2024 preprint)](https://arxiv.org/abs/2406.01731), introduction and one-dimensional theorem.
- [Nicolas Forien, *A new proof of superadditivity and of the density conjecture for Activated Random Walks on the line* (2025 preprint)](https://arxiv.org/abs/2502.02579), explicitly one-dimensional progress.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The cited density-conjecture resolutions concern the line. Searches also found later complete-graph results, which do not treat expanding square boxes. This entry specifies the expectation form of the two-dimensional density equality.

Search topics checked on 2026-09-08: activated random walk density conjecture Z2 2025 2026; density conjecture complete graph 2604.04747.
