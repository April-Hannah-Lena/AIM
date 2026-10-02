# 284. A periodic high-density limit for bounded-confidence opinion clusters

**Area:** Opinion dynamics and distributed agreement

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Start with a homogeneous Poisson point process of intensity $`\lambda>0`$ on $`\mathbb R`$, regarding its points as agent opinions. In synchronous discrete time, replace every opinion by the arithmetic mean of all current opinions at distance at most one, including itself and counting agents with multiplicity. Almost surely the initial gaps exceeding one split the process into finite isolated groups, so each agent has a final opinion. Let $`C_\lambda`$ be the simple counting measure on distinct final opinions, with one atom per cluster. As $`\lambda\to\infty`$, does $`C_\lambda`$ converge in distribution, in the vague topology on locally finite measures, to $`\sum_{j\in\mathbb Z}\delta_{U+2j}`$ with $`U`$ uniform on $`[0,2)`$?

## Application

The question makes the observed spacing of final opinion groups precise in a dense population with a fixed confidence radius.

## References

- [Carmela Bernardo, Claudio Altafini, Anton V. Proskurnikov and Francesco Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302](https://liu.diva-portal.org/smash/get/diva2%3A1809739/FULLTEXT01.pdf), Hegselmann–Krause clustering and the 2R conjecture.
- [Partha S. Dey, S. Rasoul Etesami and Aditya S. Gopalan, *The 2R-Conjecture for the Hegselmann–Krause Model: A Proof in Expectation and New Directions* (2025)](https://arxiv.org/abs/2508.08299), §3.3, Conjecture 2.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

This is the Poisson cluster-location case of the stated strong 2R conjecture. The paper’s mean-spacing result does not establish convergence of the entire cluster process to a randomly shifted lattice. Cluster mass convergence is not added as a second target.

Search topics checked on 2026-09-13: `strong 2R conjecture Hegselmann Krause Poisson cluster locations lattice proof 2026 Dey Etesami Gopalan`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
