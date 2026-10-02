# 170. The two-thirds passage-time variance exponent

**Area:** Random interfaces and growth fluctuations

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

On the nearest-neighbor graph of $`\mathbb Z^2`$, let independent edge times have the exponential distribution of mean one, and let $`T_n`$ be the minimum total edge time over all paths from $`(0,0)`$ to $`(n,0)`$. Prove or disprove

```math
\lim_{n\to\infty}\frac{\log\mathop{\mathrm{Var}}\nolimits(T_n)}{\log n}=\frac23.
```

Paths may move in all four lattice directions. This is the undirected minimum-passage model, not a directed maximum-passage model.

## Application

The exponent quantifies uncertainty in stochastic growth fronts and tests the predicted KPZ universality of propagation through random media.

## References

- [Antonio Auffinger, Michael Damron and Jack Hanson, *50 Years of First-Passage Percolation* (AMS University Lecture Series 68, 2017); author manuscript](https://sites.math.duke.edu/~rtd/FPP/50yrsFPP.pdf), §3.1 (fluctuation exponent) and §4.3 (scaling relations).
- [Riddhipratim Basu, Vladas Sidoravicius and Allan Sly, *Rotationally invariant first passage percolation: Breaking the n/log n variance barrier* (2026 preprint)](https://arxiv.org/abs/2604.01214), introduction and model scope.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The April 2026 paper obtains a polynomial improvement of a variance bound for a rotationally invariant Riemannian model. It explicitly distinguishes the unresolved lattice fluctuation problem. Exactly solvable last-passage results do not imply the displayed limit.

Search topics checked on 2026-09-08: `first passage percolation variance exponent 2026; exponential undirected FPP two thirds variance proof`. No later resolution of the exact statement was located; this is not a certification that no proof exists.
