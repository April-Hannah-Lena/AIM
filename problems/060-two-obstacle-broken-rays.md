# 060 — Broken-ray tomography with two smooth convex obstacles

**Area:** Reflection tomography / integral geometry

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be a bounded smooth strictly convex domain. Let $`K_1,K_2\Subset\Omega`$ be disjoint compact convex obstacles with smooth boundaries, with at least one strictly convex. Put $`M=\overline\Omega\setminus(K_1^\circ\cup K_2^\circ)`$.

A measured broken ray is a finite piecewise straight unit-speed path in $`M`$ that starts and ends on $`\partial\Omega`$, has no intermediate outer-boundary contacts, and reflects specularly at obstacle boundaries: outgoing velocity equals incoming velocity minus twice its normal component. Include rays with no reflection; discard grazing contacts.

For $`f\in C^\infty(M)`$, set $`Bf(\gamma)=\int_\gamma f\,ds`$. Is $`Bf=0`$ for every measured ray sufficient to conclude $`f=0`$ on $`M`$, for every admissible geometry?

## Application

This asks whether reflecting paths recover material hidden behind multiple inaccessible obstacles, a basic model of reflection-based tomography.

## References

1. S. R. Jathar and J. Railo, *Survey on Broken Ray Transforms* (2024), §2, open problem (i). [Preprint](https://arxiv.org/abs/2410.04908).
2. J. Ilmavirta, *On the broken ray transform* (2014), dissertation overview, p. 21. [Dissertation](https://users.jyu.fi/~jojapeil/thesis/brt_290814.pdf).

## Status review

**Literature check:** Open in cited literature; no later resolution located

The 2024 survey explicitly records this two-obstacle problem as unresolved. Both sources distinguish the counterexample with merely convex flat pieces from the case with a strictly convex obstacle. Results for one obstacle or for restrictive nonsmooth multiple-obstacle geometries do not settle this statement. Trapped infinite trajectories supply no measurements here.

The review searched `broken ray transform open problem obstacle` and `two smooth convex obstacles broken ray injectivity 2025 2026` on 2026-09-08. No later solution of the stated two-obstacle case was located.
