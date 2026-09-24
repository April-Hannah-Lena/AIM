# 161. Uniqueness of the limiting shape at a network singularity

**Area:** Grain-boundary evolution

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Consider a finite embedded planar network moving by curvature, with only $120^\circ$ triple junctions and fixed endpoints on the boundary of a smooth strictly convex domain. At an interior singular point $(x_0,T)$, set

$$
\widetilde\Gamma(t)=\frac{\Gamma(t)-x_0}{\sqrt{2(T-t)}}.
$$

Is the limiting shrinker independent of the sequence $t_j\uparrow T$ used to obtain it? Precisely, must all locally convergent subsequences of the rescaled networks have the same limiting arclength varifold, including its integer multiplicities? No rotation of the limit is allowed when comparing subsequences.

## Application

A unique limiting shape would make the local geometry of a grain-rearrangement event predictable as observation resolution changes.

## References

1. Carlo Mantegazza, Matteo Novaga, Alessandra Pluda and Felix Schulze, *Evolution of networks with multiple junctions*, Astérisque 452 (2024). [Author text](https://people.dm.unipi.it/novaga/papers/mantegazza/tripunto/network-survey.pdf). Open Problem 7.25 and §15 item 3 in the linked author version explicitly ask for uniqueness of blow-up limits.

2. Alessandra Pluda and Marco Pozzetta, *Łojasiewicz–Simon inequalities for minimal networks: stability and convergence*, Mathematische Annalen (2023). [Article](https://doi.org/10.1007/s00208-023-02714-7). Conditional convergence results illustrate the role of a nondegenerate limiting network.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The source distinguishes this question from multiplicity one: different subsequences could have distinct shapes even if each had unit multiplicity. Searches for “network flow uniqueness blow up limits 2025 2026” and “Pluda Pozzetta uniqueness shrinker networks” found conditional convergence results, but no theorem covering all collapsing networks.
