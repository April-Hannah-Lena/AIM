# 149 — An irrational polygon with nonergodic billiard flow

**Area:** Billiard dynamics / transport and ergodicity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Does there exist a bounded simple polygon $P\subset\mathbb R^2$, with at least one interior angle an irrational multiple of $\pi$, whose unit-speed specular billiard flow is not ergodic?

More precisely, equip $P\times S^1$ with normalized Liouville measure

$$
d\mu=\frac{dx\,dy\,d\theta}{2\pi\,\operatorname{Area}(P)}.
$$

Straight motion inside $P$ is reflected at each side by equal incidence and reflection angles. Ignore the null set of trajectories hitting vertices. The requested example must have a measurable set $A$ invariant under this flow with $0<\mu(A)<1$.

The whole unit tangent bundle is used, rather than a single directional component of a rational-polygon unfolding.

## Application

Polygonal billiards model collision transport without curved focusing or dispersing walls. A counterexample would identify a mechanism preventing global mixing even when the reflection angles generate infinitely many directions.

## References

1. E. Gutkin, *Billiard dynamics: An updated survey with the emphasis on open problems* (2012), [Chaos 22, 026116](https://doi.org/10.1063/1.4729307), Problem 8. Explicit source of the existence question.
2. J. Chaika and G. Forni, *Weakly mixing polygonal billiards* (2026), [Annals of Mathematics 203, 695–735](https://doi.org/10.4007/annals.2026.203.3.1), main theorem. Establishes weak mixing for a dense $G_\delta$ set of nonrational polygons.
3. F. Arana-Herrera, J. Chaika and G. Forni, *Weak mixing in rational billiards* (2024), [arXiv:2410.11117](https://arxiv.org/abs/2410.11117), §6.2. Lists remaining ergodicity questions for nonrational polygons.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Generic ergodicity or weak mixing does not imply the property for every irrational polygon. Searches included “irrational polygon nonergodic example 2025 2026” and “Gutkin Problem 8 solution”. The 2024 *Billiards with Spatial Memory* model changes its accessible region during motion and is not a fixed polygon with the standard billiard flow above. No qualifying counterexample was located.
