# 586. Draws in the undirected trapping game on percolation clusters

**Area:** Applied probability and random combinatorial games

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix an integer $`d\ge2`$. Independently delete every vertex of the nearest-neighbor graph on $`\mathbb Z^d`$ with probability $`p\in(0,1)`$. Both players know the resulting graph. A token starts at the origin, and the players alternate moving it along an edge to an undeleted vertex that has never previously been visited. A player with no legal move loses. If the origin is deleted, declare the first player the winner, so this outcome is never a draw.

A board is a draw if neither player has a strategy that forces a win against every strategy of the opponent. Let $`D_d(p)`$ be the probability of this event, over the independently sampled board.

For which dimensions $`d\ge2`$ does there exist $`p\in(0,1)`$ with $`D_d(p)>0`$? The conjectured picture suggested by the source is

```math
D_2(p)=0\quad\text{for every }p\in(0,1),\qquad
\text{and for every }d\ge3\text{ there exists }p\in(0,1)\text{ with }D_d(p)>0.
```

Prove or disprove this picture. The game is undirected and forbids revisiting vertices; directional percolation games have different rules.

## Application

The game connects optimal strategies on random networks to maximum-cardinality matchings and their sensitivity to distant boundary conditions. Determining whether a draw phase exists would identify whether local random deletions can eliminate this persistent dependence in different dimensions.

## References

1. R. Basu, A. E. Holroyd, J. B. Martin and J. Wästlund, [Trapping games on random boards](https://doi.org/10.1214/16-AAP1190), *Annals of Applied Probability* **26**(6) (2016), 3727–3753. Section 1 and final Open problems, item (i); [published manuscript](https://ora.ox.ac.uk/objects/uuid%3Ae8ce7dea-1da3-43e1-8c03-4905716f281a/files/rvx021h186).
2. A. E. Holroyd and J. B. Martin, [Galton–Watson games](https://doi.org/10.1002/rsa.21008), *Random Structures & Algorithms* (2021), discussion of undirected Trap on Euclidean percolation clusters.
3. A. E. Holroyd, I. Marcovici and J. B. Martin, [Percolation games, probabilistic cellular automata, and the hard-core model](https://arxiv.org/abs/1503.05614), version 3 (2018), for the distinct directed game.

## Status review

At $`p=0`$ the full lattice gives a draw. For sufficiently large deletion probability every open cluster is finite, excluding draws. The asymmetric model in [1], with different deletion probabilities on the two parity classes, also has a proved region without draws; this does not settle equal positive deletion probabilities.

The later discussion [2] retains the undirected question. The planar no-draw result in [3] permits only steps in two positive coordinate directions and therefore does not resolve this problem. Current literature, arXiv-indexed, public GitHub and native Palomar checks found no matching solution announcement. Zenodo's native API returned HTTP 403; indexed searches found no matching announcement.
