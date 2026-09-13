# 280. Does exclusion equilibrate as fast as independent particles?

**Area:** Interacting particle transport

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-13

## Problem statement

Let $G=(V,E)$ be any connected finite graph with $n$ vertices and positive symmetric edge rates $r_e$. In the $k$-particle exclusion process, each edge rings at rate $r_e$ and exchanges its endpoint occupations; $1\le k\le n/2$. Compare it with $k$ independent continuous-time walkers, each jumping across $e$ at rate $r_e$, allowing coincidences. The equilibrium laws are respectively uniform on $k$-subsets and uniform on $V^k$. With worst-start total-variation mixing times at error $1/4$, is there an absolute $C$ such that $t_{\rm mix}({\rm EX}(k))\le C\,t_{\rm mix}({\rm RW}^{\otimes k})$ for all choices of $G,r,k$?

## Applied significance

Exclusion models diffusing particles with a hard occupancy constraint. The comparison would quantify how congestion changes relaxation.

## References

- [Jonathan Hermon and Richard Pymar, *The exclusion process mixes (almost) faster than independent particles*, Annals of Probability 48 (2020)](https://arxiv.org/abs/1808.10846), Introduction, Oliveira’s conjecture.
- [Jonathan Hermon and Gady Kozma, *Sensitivity of mixing times of Cayley graphs* (2024)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0FDBD1D1ED671C875FB2DBB0DC7E905C/S0008414X23000421a.pdf/sensitivity_of_mixing_times_of_cayley_graphs.pdf), discussion of Oliveira’s mixing conjectures.

## Status review

The exclusion paper proves several regular-graph cases and general estimates with extra factors. Equality of spectral gaps, established for the interchange process, is a different assertion and does not imply the proposed total-variation comparison.

Search topics checked on 2026-09-13: `Oliveira exclusion independent particles mixing conjecture proof 2025 2026`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
