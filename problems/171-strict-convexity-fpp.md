# 171. Strict convexity of the planar exponential first-passage shape

**Area:** Stochastic growth and random media

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Give each nearest-neighbor edge $e$ of $\mathbb Z^2$ an independent exponential random variable $\tau_e$ of mean one. Let $T(x,y)$ be the minimum of $\sum_{e\in\gamma}\tau_e$ over lattice paths from $x$ to $y$, and let $\mu(v)=\lim_{n\to\infty}T(0,\lfloor nv\rfloor)/n$, the deterministic time constant. Is the unit ball $B_\mu=\{v\in\mathbb R^2:\mu(v)\le1\}$ strictly convex? Equivalently, must $\mu(su+(1-s)v)<1$ hold for distinct $u,v\in\partial B_\mu$ and every $0<s<1$? The exponential law is fixed; no curvature or straightness hypothesis may be assumed.

## Application

This asks whether the macroscopic front of a lattice growth model has flat facets. The same random metric models travel times through heterogeneous media.

## References

- [Antonio Auffinger, Michael Damron and Jack Hanson, *50 Years of First-Passage Percolation* (AMS University Lecture Series 68, 2017); author manuscript](https://sites.math.duke.edu/~rtd/FPP/50yrsFPP.pdf), §§2.5 and 2.8, Questions 4 and 11.
- [Steven P. Lalley, *Strict Convexity of the Limit Shape in First-Passage Percolation* (2003)](https://doi.org/10.1214/ECP.v8-1089), conditional strict-convexity criteria.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The book poses the continuous-weight conjecture; this entry fixes its exponential case. Lalley assumes additional geodesic and fluctuation properties, so the title of that paper does not establish this statement. Later searches located no unconditional proof for the stated lattice model.

Search topics checked on 2026-09-08: `first-passage percolation strict convexity open 2025 2026; exponential first-passage limit shape strict convexity proof`. No later resolution of the exact statement was located; this is not a certification that no proof exists.
