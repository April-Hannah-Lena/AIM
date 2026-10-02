# 267. Does stronger ferromagnetic coupling always slow Ising relaxation?

**Area:** Statistical mechanics and Monte Carlo sampling

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

Let $`G=(V,E)`$ be a finite simple graph with at least one vertex. For $`J\in[0,\infty)^E`$ let $`\pi_J(\sigma)\propto\exp(\sum_{uv\in E}J_{uv}\sigma_u\sigma_v)`$ on $`\{-1,1\}^V`$, with zero external field. Each vertex, at rate one, resamples its spin from the conditional law under $`\pi_J`$. Write $`\gamma(J)`$ for the smallest positive eigenvalue of the negative generator. For every edge $`e`$ and $`s\ge0`$, must $`\gamma(J+s\mathbf1_e)\le\gamma(J)`$?

## Application

This tests whether strengthening one attractive interaction can ever accelerate equilibration of a magnetic spin system.

## References

- [David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, second edition (2017)](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf), Chapter 26, Question 2.
- [Şerban Nacu, *Glauber dynamics on the cycle is monotone* (2003)](https://arxiv.org/abs/math/0305056), the coupling-monotonicity theorem for cycles.

## Status review

**Known cases:** The spectral-gap monotonicity assertion is proved on cycles with arbitrary ferromagnetic couplings.

**Remaining target:** The same monotonicity for every finite simple graph.

**Literature check:** Open in cited literature; no later resolution located.

The cycle theorem covers arbitrary ferromagnetic couplings on that graph. The catalogue asks for every finite graph; equilibrium correlation inequalities alone do not establish the dynamical comparison.

Search topics checked on 2026-09-13: `Ising Glauber spectral gap coupling monotonicity Nacu proof counterexample 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
