# 660. Compact orbit covers of aspherical manifolds

**Area:** Applied topology / geometric topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-09-24

## Problem statement

Let $`M`$ be a closed connected smooth aspherical manifold, and let $`\widetilde M`$ be its universal cover. Thus $`M`$ is compact without boundary and $`\widetilde M`$ is contractible. Write $`G=\pi_1(M)`$ for the group acting on $`\widetilde M`$ by deck transformations.

Does there always exist a compact subset $`K\subseteq\widetilde M`$ such that

```math
\widetilde M=\bigcup_{g\in G}gK,
```

and, for every finite nonempty subset $`F\subseteq G`$, the intersection

```math
\bigcap_{g\in F}gK
```

is either empty or contractible?

The condition includes singleton $`F`$, so $`K`$ itself must be contractible. The entire cover must consist of translates of this one compact set.

## Application

The question arises in extending lattice growth models, such as the Eden model, to universal covers of manifolds. Such an orbit cover would supply pieces whose topology and intersections are simple, helping separate topology created by growth from topology already present inside the pieces.

## References

1. D. M. Hua, F. Manin, T. Queer and T. Wang, [Local behavior of the Eden model on graphs and tessellations of manifolds](https://doi.org/10.1007/s41468-023-00153-6), Journal of Applied and Computational Topology **8** (2024), 1607–1647, Conjectures 1.4 and 6.8; §§4 and 6. [Preprint](https://arxiv.org/abs/2212.14146).

## Status review

**Known cases:** Closed Euclidean and hyperbolic manifolds have suitable compact Voronoi cells: the cells and their nonempty intersections are convex and therefore contractible.

**Remaining target:** The compact orbit-cover assertion for arbitrary closed connected smooth aspherical manifolds.

This is the compact-cover formulation of Conjecture 1.4, with the closed-manifold scope made explicit in Conjecture 6.8. The latter additionally asks for a closed fundamental domain. Current searches found no matching solution or announced counterexample to the compact-cover target.
