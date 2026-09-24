# 554. Bounded weakening for constrained invertibility

**Area:** Applied topology and structured linear algebra

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Fix a field $`k`$. A constrained invertibility problem consists of two $`n\times n`$ patterns $`P,Q\in\{0,*\}^{n\times n}`$. It is feasible over $`k`$ if there exist $`A,B\in k^{n\times n}`$ with $`AB=I_n`$, such that $`A_{ij}=0`$ whenever $`P_{ij}=0`$ and $`B_{ij}=0`$ whenever $`Q_{ij}=0`$. A star permits any field element, including zero.

Form the directed bipartite graph $`G(P,Q)`$ with vertices $`u_1,\ldots,u_n,v_1,\ldots,v_n`$ and edges

```math
u_i\longrightarrow v_j\quad\Longleftrightarrow\quad P_{j,i}=*,\qquad
v_j\longrightarrow u_i\quad\Longleftrightarrow\quad Q_{i,j}=*.
```

Write $`d_G(x,y)`$ for the length of a shortest directed path, with value $`+\infty`$ if no such path exists.

Does there exist an odd integer $`c\ge1`$, independent of $`n,P,Q`$, such that every feasible problem admits a permutation $`\sigma`$ of $`\{1,\ldots,n\}`$ satisfying

```math
d_G(u_i,v_{\sigma(i)})\le c\quad\text{and}\quad d_G(v_{\sigma(i)},u_i)\le c
\qquad (1\le i\le n)?
```

The question is posed for each fixed field; no uniformity in the field is additionally required. All paths are measured in the original graph. Equivalently, add every edge between opposite parts that is reachable by a directed path of length at most $`c`$. The resulting patterns must admit a permutation matrix and its inverse as a feasible pair. This is Bjerkevik's Conjecture 6.10 [1].

## Application

Constrained invertibility encodes interleavings between persistence modules built from upsets. Theorem 6.14 of [1] identifies this conjecture with a uniform bound on the matching distance between their decompositions in terms of the interleaving distance. Such a bound would justify stable matching-based comparisons in multiparameter topological data analysis. The equivalent persistence formulation is counted here as the same problem.

## References

1. H. B. Bjerkevik, [Stabilizing Decomposition of Multiparameter Persistence Modules](https://doi.org/10.1007/s10208-025-09695-w), Foundations of Computational Mathematics **26** (2026), 939–998, Definitions 6.6 and 6.9, Conjecture 6.10 and Theorem 6.14; [preprint](https://arxiv.org/abs/2305.15550).
2. R. N. Nehme, [Pruning distance of upset-decomposable persistence modules](https://arxiv.org/abs/2602.15243), version 1 (2026), Theorem 1.1, for related bounds involving pruning distance and pointwise dimension.
3. E. Miller, [III. Distances between modules](https://sites.math.duke.edu/~ezra/Talks/distances.pdf), Combinatorial Coworkspace, 24–27 March 2026, slide 13 (PDF page 58), for the conjecture and progress with a size-dependent constant.

## Status review

The choice $`c=1`$ fails: [1, Example 6.7] gives a feasible pair of size three with no permutation-matrix solution. The target is the existence of some constant for all sizes, rather than the particular choice $`c=3`$ or a bound that grows with $`n`$.

Miller's 2026 slides still state the uniform bound as a conjecture while reporting a bound depending on the number of summands. Nehme's theorem compares bottleneck and pruning distances with a factor depending on maximal pointwise dimension; it does not give the uniform bottleneck/interleaving bound. A related FoCM 2026 poster announces a pruning/interleaving comparison, but does not assert the uniform matching bound required here.

No matching solution or announced solution was located through the check date.
