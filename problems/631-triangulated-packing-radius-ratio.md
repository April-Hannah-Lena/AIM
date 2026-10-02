# 631. Largest radius ratio in nonuniform triangulated circle packings

**Area:** Discrete geometry and circle packing

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

A triangulated packing of the Euclidean plane consists of closed disks with pairwise disjoint interiors whose contact graph, drawn with straight segments between the centers of tangent disks, triangulates the entire plane. Assume the smallest and largest radii are attained and satisfy $`0<r_{\min}\le r_{\max}<\infty`$. Require at least two distinct radii and set $`q=r_{\min}/r_{\max}`$.

Let $`q_*=0.6510501858\ldots`$ be the radius ratio of Fernique's three-radius packing, equivalently the root near $`0.65105`$ of

```math
89x^8+1344x^7+4008x^6-464x^5-2410x^4+176x^3+296x^2-96x+1=0.
```

Prove or disprove that every such packing satisfies $`q\le q_*`$. The competing packings need not be periodic, and there is no fixed upper bound on the number of distinct radii.

## Application

The problem asks how nearly uniform a triangulated disk packing can be before it must become the equal-disk hexagonal packing. It connects local tangency constraints with global geometric rigidity and the design of polydisperse packings.

## References

1. R. Connelly and Z. Zhang, [Rigidity of Circle Packings with Flexible Radii](https://doi.org/10.1007/s00454-025-00776-9), *Discrete & Computational Geometry* **74** (2025), 585–618, Conjecture 1 and Section 7. [arXiv:2206.07165](https://arxiv.org/abs/2206.07165).
2. T. Fernique, [A Densest Ternary Circle Packing in the Plane](https://arxiv.org/abs/1912.02297), 2019.

## Status review

**Known cases:** A periodic packing using three radii attains $`q_*`$. Classifications with two and three sizes and local rigidity tests provide evidence, but do not cover arbitrarily many sizes.

**Remaining target:** Establish the universal upper bound on the radius ratio. Fernique's density optimality result for a particular prescribed triple of radii does not resolve this problem of optimizing the radii themselves. The larger ratio near $`0.658`$ discussed in the source concerns a perturbed packing that is not triangulated. No matching solution announcement was found in the status checks.
