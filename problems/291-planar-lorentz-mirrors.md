# 291. Localization of light rays in the planar random mirror model

**Area:** Transport in random optical media

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

Independently at each vertex of $\mathbb Z^2$, put no mirror with probability $1-p$, a mirror of slope $+1$ with probability $p/2$, or a mirror of slope $-1$ with probability $p/2$. A ray moves along nearest-neighbor lattice edges. At each encountered vertex it continues straight if no mirror is present and otherwise undergoes specular reflection through the indicated diagonal mirror. Launch a ray from the origin pointing east, and subsequently apply these rules also on returns to the origin. For every $p\in(0,1]$, is the set of visited vertices almost surely finite? Equivalently, must the directed trajectory eventually close into a finite orbit?

## Application

This is a minimal model of whether a dilute random scattering medium traps light or permits transport over arbitrarily large distances.

## References

- [Gady Kozma and Vladas Sidoravicius, *Lower bound for the escape probability in the Lorentz mirror model on the lattice*, Israel Journal of Mathematics 209 (2015)](https://doi.org/10.1007/s11856-015-1233-1), planar escape estimate.
- [Dor Elboim, Antoine Gloria and Felipe Hernández, *Diffusivity of the Lorentz mirror walk in high dimensions* (2025)](https://arxiv.org/abs/2505.01341), Introduction and the two-dimensional localization conjecture.
- [Raphaël Lefevere and Hal Tasaki, *Hierarchical Lorentz Mirror Model: Normal Transport and a Universal 2/3 Mean-Variance Law* (2026)](https://arxiv.org/abs/2602.07988), a different, hierarchical model.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The high-dimensional theorem concerns weak disorder on long but bounded time scales. The hierarchical 2026 model changes the geometry. Neither resolves the infinite-time planar question; a positive lower bound for reaching each finite distance also does not prove an infinite trajectory.

Search topics checked on 2026-09-13: `planar Lorentz mirror model all trajectories finite p positive proof 2026 localization`. No later resolution of this exact statement was located; this is a literature check, not a certification that no proof exists.
