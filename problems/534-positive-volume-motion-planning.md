# 534. Maximal motion-planning complexity from positive simplicial volume

**Area:** Applied topology and robot motion planning

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $M$ be a closed, connected, oriented aspherical manifold of dimension $n\ge3$. Thus its universal cover is contractible. Define its simplicial volume using rational singular cycles by

$$
\|M\|=\inf\left\{\sum_j|a_j|:\ \sum_j a_j\sigma_j\text{ represents }[M]\in H_n(M;\mathbb Q)\right\}.
$$

Assume $\|M\|>0$.

Use unreduced topological complexity: $\mathop{\mathrm{TC}}\nolimits(M)$ is the least number of open sets covering $M\times M$ on each of which the endpoint map

$$
e:C([0,1],M)\longrightarrow M\times M,\qquad e(\gamma)=(\gamma(0),\gamma(1)),
$$

with the compact-open topology on the path space, has a continuous section.

Must

$$
\mathop{\mathrm{TC}}\nolimits(M)=2n+1?
$$

Prove this for every such $M$, or construct a counterexample. No curvature hypothesis is imposed. This is Question 5.1(b) of [1], with the already understood surface case omitted.

## Application

When $M$ models a configuration space, each local section is a continuous path-planning rule. The proposed equality would certify that positive simplicial volume forces the largest possible number of such rules allowed by dimension. It would extend a geometric obstruction to motion planning beyond negatively curved spaces.

## References

1. C. Neofytidis, [Topological complexity, asphericity and connected sums](https://doi.org/10.1007/s41468-025-00205-z), Journal of Applied and Computational Topology **9**, article 10 (2025), §3.2 and Question 5.1(b), p.13. [arXiv:2212.08962v2](https://arxiv.org/abs/2212.08962v2).
2. A. Dranishnikov, [On topological complexity of hyperbolic groups](https://arxiv.org/abs/1904.06720), Proceedings of the American Mathematical Society **148** (2020), 4547–4556. This reference uses reduced topological complexity.

## Status review

The negatively curved case follows from the hyperbolic-group result in [2], as explained in [1]. The target retains general positive-simplicial-volume aspherical manifolds. It is distinct from the [centre-rank question](523-aspherical-motion-planning-center.md): [1] explicitly treats the proposed vanishing of simplicial volume for aspherical manifolds with nontrivial centre as a further open conjecture, rather than an available implication.

Checks on 24 September 2026 found no matching general solution or announcement in the primary follow-ups, author publication list, indexed arXiv/Zenodo/GitHub searches, or the official Palomar metadata search.
