# 518. Monotonicity of unordered graph motion-planning complexity

**Area:** Applied topology and robot motion planning

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Let $\Gamma$ be a connected finite graph, viewed as a finite one-dimensional CW complex with at least one edge. Define its unordered configuration space by

$$
B_k(\Gamma)=\left\{(x_1,\ldots,x_k)\in\Gamma^k:x_i\ne x_j\text{ for }i\ne j\right\}/\mathfrak S_k,
$$

with the quotient topology, where the symmetric group permutes coordinates.

For a path-connected space $X$, let $PX=C([0,1],X)$ have the compact-open topology and let $e:PX\to X\times X$ be endpoint evaluation, $e(\gamma)=(\gamma(0),\gamma(1))$. Use the reduced topological complexity $\mathop{\mathrm{TC}}\nolimits(X)$: the least $q\ge0$ such that $X\times X$ admits an open cover $U_0,\ldots,U_q$ and continuous maps $s_j:U_j\to PX$ satisfying $e\circ s_j=\mathop{\mathrm{id}}\nolimits_{U_j}$.

Is it true that, for every such graph and every integer $k\ge1$,

$$
\mathop{\mathrm{TC}}\nolimits(B_k(\Gamma))\le\mathop{\mathrm{TC}}\nolimits(B_{k+1}(\Gamma))?
$$

Prove this universal inequality or exhibit a finite graph and particle number for which it fails. Configurations forbid all collisions; particles are indistinguishable and the underlying graph stays fixed.

## Application

The space $B_k(\Gamma)$ models $k$ identical robots moving along a network of tracks without collisions. Its topological complexity counts, after adding one, the minimum number of continuous local rules needed to plan between arbitrary configurations. The question asks whether introducing another robot can ever lower this requirement.

## References

1. B. Knudsen, [On the stabilization of the topological complexity of graph braid groups](https://doi.org/10.1007/s41468-026-00232-4), Journal of Applied and Computational Topology **10**, article 9 (2026). Section 1.2, third bullet, p.3; conventions and configuration spaces on pp.4–5. [arXiv:2302.04346v2](https://arxiv.org/abs/2302.04346v2).
2. K. Jankiewicz and K. Schreve, [Products of free groups inside graph braid groups](https://people.ucsc.edu/~kjankiew/GraphBraidGroups.pdf), author manuscript, Theorem 3. The published stabilization result is also discussed in [1, §1.1].

## Status review

Reference [1] explicitly asks the monotonicity question for unordered configurations. It distinguishes this from monotonicity for ordered configurations and from eventual stabilization.

For graphs with $m>0$ vertices of valence at least three, [2] proves that $\mathop{\mathrm{TC}}\nolimits(B_k(\Gamma))=2m$ once $k\ge2m+m_3$, where $m_3$ counts trivalent vertices. This settles the eventual value but does not compare every consecutive pair below that threshold. The entry concerns precisely that all-particle-number comparison, not the resolved stabilization conjecture.

The published April 2026 question, the February 2026 arXiv revision and the cited stabilization theorem were checked. Searches on 24 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar, located no matching proof, counterexample or announced solution.
