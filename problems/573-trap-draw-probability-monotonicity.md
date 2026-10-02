# 573. Monotonicity of draw probabilities under random vertex deletion

**Area:** Applied probability and random combinatorial games

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

For $`d\ge2`$ and $`p\in[0,1]`$, independently delete vertices of the nearest-neighbor graph on $`\mathbb Z^d`$ with probability $`p`$. On the remaining graph, play the following perfect-information game starting at the origin. Players alternate moving a token to an adjacent vertex never previously visited; a player unable to move loses. A deleted starting vertex is declared a first-player win. A draw means that neither player can force a win.

Write $`D_d(p)`$ for the unconditional probability of a draw. Is $`D_d`$ nonincreasing? More precisely, prove or disprove

```math
D_d(p_2)\le D_d(p_1)\qquad
(d\ge2,\;0\le p_1\le p_2\le1).
```

Both parity classes have the same deletion probability, and the probability is not conditioned on the origin surviving or belonging to an infinite cluster.

## Application

Monotonicity would constrain the possible phase diagram of this game on a diluted random network. If draws occur at positive deletion probability in a given dimension, the result would rule out their disappearance and subsequent reappearance as deletion increases.

## References

1. R. Basu, A. E. Holroyd, J. B. Martin and J. Wästlund, [Trapping games on random boards](https://doi.org/10.1214/16-AAP1190), *Annals of Applied Probability* **26**(6) (2016), 3727–3753. Section 1 and final Open problems, item (ii); [published manuscript](https://ora.ox.ac.uk/objects/uuid%3Ae8ce7dea-1da3-43e1-8c03-4905716f281a/files/rvx021h186).

## Status review

The endpoint values are $`D_d(0)=1`$ and $`D_d(1)=0`$, and sufficiently sparse surviving graphs have no draws because their components are finite. These facts do not prove monotonicity between the endpoints. Deleting vertices of only one parity favors one player, whereas deleting both parities changes both players' options; the standard percolation coupling does not directly order the draw event.

The source lists monotonicity separately from existence of a positive-probability draw phase. Either phase-existence answer in one dimension need not classify the probability function in all other dimensions. Directed games and games on Galton–Watson trees have different state spaces and do not resolve the displayed inequality. Current literature and announcement checks found no matching proof or counterexample.
