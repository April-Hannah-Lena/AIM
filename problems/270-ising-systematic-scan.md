# 270. A constant comparison between systematic and random Ising updates

**Area:** Monte Carlo simulation and update scheduling

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For a finite zero-field ferromagnetic Ising measure $`\pi`$ on an $`n`$-vertex graph, let $`K_v`$ resample the spin at $`v`$ conditionally on all other spins. Set $`P=n^{-1}\sum_vK_v`$ and $`P_\alpha=K_{\alpha(1)}\cdots K_{\alpha(n)}`$ for a permutation $`\alpha`$ of the vertices. For a kernel $`Q`$ define $`t_{\rm mix}(Q)=\min\{t\in\mathbb N:\max_\sigma\|Q^t(\sigma,\cdot)-\pi\|_{\rm TV}\le1/4\}`$. Is there an absolute $`C<\infty`$ such that $`n\,t_{\rm mix}(P_\alpha)\le C\,t_{\rm mix}(P)`$ for every graph, every finite nonnegative set of couplings, and every $`\alpha`$? One step of $`P_\alpha`$ is a complete sweep.

## Application

Simulation software often visits sites in a fixed order. The question compares its total number of spin updates with random scanning.

## References

- [David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, second edition (2017)](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf), Chapter 26, Question 3(i).
- [Jason Gaitonde and Elchanan Mossel, *Comparison Theorems for the Mixing Times of Systematic and Random Scan Dynamics* (2024; revised 2025)](https://arxiv.org/abs/2410.11136), Theorems 1.1–1.2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The newer paper proves polynomial comparisons for general Gibbs samplers and explains examples obstructing stronger general comparisons. It does not give this uniform constant comparison for ferromagnetic Ising measures. The restriction to attractive Ising interactions is essential to the question being retained.

Search topics checked on 2026-09-13: `ferromagnetic Ising systematic scan random scan constant mixing comparison Gaitonde Mossel 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
