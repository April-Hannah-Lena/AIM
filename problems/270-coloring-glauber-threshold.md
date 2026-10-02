# 270. Rapid sampling of proper colorings at the ergodicity threshold

**Area:** Antiferromagnetic spin systems and constrained sampling

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For each integer $`\Delta\ge2`$ and $`q\ge\Delta+2`$, consider any finite simple graph $`G`$ with $`n`$ vertices and maximum degree at most $`\Delta`$. A step chooses a uniform vertex and replaces its color by a uniform color absent from its neighbors. Starting from any proper $`q`$-coloring, this heat-bath chain has the uniform proper-coloring law as its stationary distribution. Do there exist constants $`C_{\Delta,q},a_{\Delta,q}<\infty`$ such that its worst-start total-variation mixing time to error $`\varepsilon`$ is at most $`C_{\Delta,q}n^{a_{\Delta,q}}\log(1/\varepsilon)`$ for all $`G`$ and $`0<\varepsilon<1/2`$?

## Application

Proper colorings are zero-temperature antiferromagnetic Potts states and models of assignments with local incompatibilities. A polynomial mixing bound would justify generating approximately uniform feasible assignments by repeatedly updating just one site, even when the number of available colors is close to the threshold that guarantees the updates can explore every coloring.

## References

- [Alan Frieze and Eric Vigoda, *A Survey on the Use of Markov Chains to Randomly Sample Colourings* (2007)](https://www.math.cmu.edu/~af1p/Texfiles/colouringsurvey.pdf), introductory mixing conjecture.
- [Xiaoyu Chen and Kuikui Liu, *A Spectral Local-to-Global Principle for Spin Systems on Graphs with Girth At Least Five* (26 August 2026)](https://arxiv.org/abs/2608.25491), Introduction and Theorem 1.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The August 2026 preprint proves a restricted high-degree, girth-at-least-five result. Arbitrary graphs and the full range down to $`q=\Delta+2`$ remain outside it. This entry asks for polynomial mixing; the stronger optimal $`n\log n`$ conjecture is not separately counted.

Search topics checked on 2026-09-13: `proper colorings Glauber Delta plus two rapid mixing 2026 Chen Liu girth five resolution`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
