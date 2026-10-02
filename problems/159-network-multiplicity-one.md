# 159. Multiplicity one at planar network singularities

**Area:** Grain-boundary evolution

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-08

## Problem statement

Let $`\Gamma(t)`$ be a smooth embedded finite network in a bounded smooth strictly convex planar domain. Its interior vertices are triple junctions with $`120^\circ`$ angles, its boundary endpoints are fixed, and each edge moves with normal velocity equal to its curvature. Let $`T<\infty`$ be its first singular time and $`x_0`$ an interior singular point.

Must every self-similarly shrinking limit obtained from the parabolic rescalings

```math
\Gamma_j(s)=\lambda_j\bigl(\Gamma(T+s/\lambda_j^2)-x_0\bigr),\qquad\lambda_j\to\infty,\quad s<0,
```

be embedded and have multiplicity one? Multiplicity counts how many rescaled arcs converge to the same limiting arc; it is retained by taking limits of the associated arclength varifolds.

## Application

Multiple hidden sheets at a collapsing grain boundary obstruct a geometric rule for continuing the evolution after a singular event.

## References

1. Carlo Mantegazza, Matteo Novaga, Alessandra Pluda and Felix Schulze, *Evolution of networks with multiple junctions*, Astérisque 452 (2024). [Author text](https://people.dm.unipi.it/novaga/papers/mantegazza/tripunto/network-survey.pdf). Open Problem 9.1 (M1), §15 item 2 in the linked author version; numbering differs in earlier drafts.

2. Carlo Mantegazza, Matteo Novaga and Alessandra Pluda, *Type-0 singularities in the network flow—evolution of trees*, Journal für die reine und angewandte Mathematik 792 (2022), 189–221. [Article](https://doi.org/10.1515/crelle-2022-0055). Introduction and results for networks with few junctions give partial control.

## Status review

**Known cases:** Multiplicity one is established for networks with at most two triple junctions.

**Remaining target:** Embedded multiplicity-one shrinking limits for every network in the stated class, without a junction-count restriction.

**Literature check:** Open in cited literature; no later resolution located.

The book retains the conjecture without a bound on the number of junctions. Searches for “network flow multiplicity one conjecture 2026” and “planar networks M1 solved” found no general proof. The known case with at most two triple junctions is insufficient here.
