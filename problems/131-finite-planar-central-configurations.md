# 131 — Finiteness of planar central configurations for fixed masses

**Area:** Celestial mechanics / relative equilibria

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

For every integer $`N\ge5`$ and every fixed tuple $`m_1,\ldots,m_N>0`$, are there only finitely many planar central configurations up to rotation?

Precisely, consider labelled points $`q_i\in\mathbb R^2`$ satisfying $`q_i\ne q_j`$ for $`i\ne j`$,

```math
\sum_i m_iq_i=0,\qquad \sum_i m_i|q_i|^2=1,\qquad
\sum_{j\ne i}m_j\frac{q_j-q_i}{|q_j-q_i|^3}=-\lambda q_i
\quad(i=1,\ldots,N)
```

for some $`\lambda>0`$. Must the solution set have finitely many orbits under the common action of $`SO(2)`$? The normalizations remove translation and scale; the assertion includes exceptional mass ratios.

## Application

Central configurations generate rigidly rotating or homothetic gravitational motions and organize collision asymptotics. Finiteness would make their classification a finite task for each physical mass tuple.

## References

1. S. Smale, *Mathematical problems for the next century* (1998), [The Mathematical Intelligencer 20, 7–15](https://doi.org/10.1007/BF03025291), Problem 6. Original modern problem-list formulation.
2. M. Moczurad and P. Zgliczyński, *Central Configurations with Unequal Masses: Finiteness in Several Exceptional Cases of Five Bodies* (2026), [arXiv:2601.01165](https://arxiv.org/abs/2601.01165), introduction and main results. Treats specified exceptional five-body mass cases.
3. K.-M. Chang and K.-C. Chen, *Toward Finiteness of Central Configurations of the Planar Six-Body Problem (II): Determine Mass Relations* (2025), [SIAM Journal on Applied Dynamical Systems 24, 2369–2404](https://doi.org/10.1137/24M1716070), introduction. Advances the six-body algebraic reduction.

## Status review

**Known cases:** Finiteness is established for generic five-body mass tuples and for several exceptional five-body cases treated in the cited 2026 paper.

**Remaining target:** Finiteness for every positive mass tuple and every number of bodies at least five, including all exceptional mass ratios.

**Literature check:** Open in cited literature; no later resolution located.

Finiteness for four bodies and generic five-body mass tuples does not cover every mass tuple in this statement. The 2026 five-body paper resolves several exceptional cases, not all of them. Searches included “Smale problem 6 central configurations finiteness 2026”, “five body exceptional masses finiteness 2601.01165” and “six body central configurations finiteness proof 2025 2026”. No full resolution was located.
