# 513. Maximal motion-planning complexity of aspherical connected sums

**Area:** Applied topology and robot motion planning

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $`M`$ and $`N`$ be closed, connected, oriented aspherical manifolds of the same dimension $`n\ge3`$. Here aspherical means that the universal cover is contractible. Form the oriented connected sum $`X=M\#N`$ by removing the interiors of embedded $`n`$-balls and identifying their boundary spheres by an orientation-reversing map.

Define $`\mathop{\mathrm{TC}}\nolimits(X)`$ to be the least number of open sets covering $`X\times X`$ on which the endpoint map

```math
e:C([0,1],X)\longrightarrow X\times X,\qquad e(\gamma)=(\gamma(0),\gamma(1)),
```

admits continuous sections; the path space has the compact-open topology. Thus this is unreduced topological complexity.

Is the dimensional upper bound always attained,

```math
\mathop{\mathrm{TC}}\nolimits(M\#N)=2n+1?
```

Prove the assertion or exhibit an aspherical pair for which it fails. Asphericity is required of each summand, not of their connected sum.

## Application

Connected sums give a concrete way to join two configuration-space models through a neck. The question asks whether joining two aspherical pieces always forces the largest possible number of continuous motion-planning rules in that dimension. It tests how a local gluing operation changes global planning complexity.

## References

1. C. Neofytidis, [Topological complexity, asphericity and connected sums](https://doi.org/10.1007/s41468-025-00205-z), Journal of Applied and Computational Topology **9**, article 10 (2025), Question 5.5(b), p.15; Corollary 1.3 and Question 5.10. [arXiv:2212.08962v2](https://arxiv.org/abs/2212.08962v2).
2. N. Daundkar, R. Santhanam and S. Thandar, [Higher topological complexity of Seifert fibered manifolds](https://arxiv.org/abs/2304.01274v3), revised 30 January 2026, §5, particularly Proposition 5.3.

## Status review

The final version of [1] proves the maximal value for certain four-dimensional sums and retains the general question. Its earlier preprint contained erroneous stronger conclusions that were explicitly removed in revision. Dimension two is already understood; dimension one is excluded.

Reference [2] computes the value for wedges of aspherical three-manifolds and records bounds for their connected sums. A wedge is a different space, so that computation does not settle this target. Searches on 24 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar records, found no matching general resolution.
