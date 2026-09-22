# 292. Existence of a planar sandpile avalanche-size exponent

**Area:** Avalanches and self-organized criticality

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Let $\nu$ be the infinite-volume weak limit of uniform recurrent Abelian sandpile configurations on wired square boxes in $\mathbb Z^2$. Stable heights are $0,1,2,3$; wiring identifies the exterior with a sink before taking the limit. Sample from $\nu$, add one grain at the origin and stabilize, toppling a site with at least four grains by sending one grain to each nearest neighbor. Let $S$ be the total number of topplings, counting repeated topplings of a site separately; $S<\infty$ almost surely is known. Does there exist $a\in[0,\infty)$ such that $\lim_{k\to\infty}\log\nu(S\ge k)/\log k=-a$? The target is existence of the exponent, without requiring a conjectural numerical value.

## Application

A power-law exponent describes the frequency of extreme cascade sizes in a basic model of slowly driven threshold systems.

## References

- [Antal A. Járai, *Sandpile models*, Probability Surveys 15 (2018)](https://doi.org/10.1214/14-PS228), §3.3.2, Conjecture 3.8.
- [Sandeep Bhupatiraju, Jack Hanson and Antal A. Járai, *Inequalities for critical exponents in d-dimensional sandpiles* (2016)](https://arxiv.org/abs/1602.06475), avalanche tail bounds.
- [Tom Hutchcroft, *Universality of high-dimensional spanning forests and sandpiles* (2018)](https://arxiv.org/abs/1804.04120), results in dimensions at least five.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Known planar bounds do not establish a limiting logarithmic exponent for total topplings. The high-dimensional exponent theorem is not a planar theorem. Avalanche area, radius and total topplings are different observables; only the last is counted here.

Search topics checked on 2026-09-13: `two dimensional Abelian sandpile total topplings avalanche size exponent existence proof 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
