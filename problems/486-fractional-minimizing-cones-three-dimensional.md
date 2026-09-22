# 486. Flatness of three-dimensional fractional minimizing cones for every interaction order

**Area:** Nonlocal variational PDEs; phase interfaces

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-22

## Problem statement

Fix any $s\in(0,1)$. For measurable $E\subset\mathbb R^3$ define
$$
\operatorname{Per}_s(E;U)=\int_{E\cap U}\!\int_{E^c}\frac{dy\,dx}{|x-y|^{3+s}}
+\int_{E\setminus U}\!\int_{E^c\cap U}\frac{dy\,dx}{|x-y|^{3+s}}.
$$
Suppose $E$ is a nontrivial cone, meaning $rE=E$ up to null sets for every $r>0$ and both $E$ and $E^c$ have positive volume in the unit ball. Assume $\operatorname{Per}_s(E;U)<\infty$ for every bounded smooth $U$, and
$\operatorname{Per}_s(E;U)\le\operatorname{Per}_s(F;U)$ for every measurable $F$ agreeing with $E$ outside $U$.

Must $E$ agree almost everywhere with a half-space whose boundary passes through the origin? The problem quantifies over the whole interval $0<s<1$, including interaction orders not sufficiently close to either endpoint.

## Application

These cones are possible singularity models for interfaces minimizing an energy with long-range interactions. Their classification controls regularity of nonlocal phase boundaries.

## References

1. L. Caffarelli, J.-M. Roquejoffre and O. Savin, *Nonlocal minimal surfaces*, Comm. Pure Appl. Math. **63** (2010), 1111–1144, minimizing cones and dimension reduction. [Article](https://doi.org/10.1002/cpa.20331).
2. X. Cabré, E. Cinti and J. Serra, *Stable $s$-minimal cones in $\mathbb R^3$ are flat for $s\sim1$*, J. Reine Angew. Math. (2020). [Preprint](https://arxiv.org/abs/1710.08722).
3. R. Tsiamis, *Stable $s$-minimal cones in $\mathbb R^3$ are flat for $s$ close to zero* (August 2026 preprint), Theorem 1.1 and Introduction. [Full preprint](https://arxiv.org/html/2608.21340v1).

## Status review

**Known cases:** Flatness is proved for interaction orders sufficiently close to one; the cited August 2026 preprint supplies the sufficiently-small-order regime.

**Remaining target:** Flatness for every interaction order strictly between zero and one, including the intervening orders.

**Literature check:** Open in cited literature; no later resolution located.

The August 2026 theorem was included in the check: it proves flatness only for sufficiently small $s$, complementing the near-one theorem. Searches on 2026-09-22 for three-dimensional minimizing cones and all fractional orders located no result closing the intervening orders. This entry uses minimizing cones, a stronger assumption than stationarity or stability; nonflat stationary cones do not disprove it. It also differs from the catalogue's local one-phase cone and Allen–Cahn questions.
