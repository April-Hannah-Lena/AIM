# Reed's bound for the chromatic number

**Area:** Combinatorial optimization and conflict scheduling

**Status:** Accepted; integrated as entry 340

**Last checked:** 2026-09-18

## Problem statement

Let $`G=(V,E)`$ be any finite nonempty simple undirected graph. Write $`\Delta(G)`$ for the maximum vertex degree and $`\omega(G)`$ for the largest number of pairwise adjacent vertices. A proper $`k`$-colouring is a function $`c:V\to\{1,\ldots,k\}`$ satisfying $`c(u)\ne c(v)`$ whenever $`\{u,v\}\in E`$. The chromatic number $`\chi(G)`$ is the smallest such $`k`$.

Prove or disprove **Reed's colouring conjecture**:

```math
\chi(G)\leq
\left\lceil\frac{\Delta(G)+1+\omega(G)}{2}\right\rceil
\qquad\text{for every finite nonempty simple undirected graph }G.
```

The bound concerns ordinary integral colourings with a common palette, at every finite graph size and degree. It requires neither a large-degree hypothesis nor a restriction on induced subgraphs. The target is existence of a colouring, without an algorithmic running-time requirement. The ceiling cannot simply be removed: a cycle on five vertices has $`\Delta=2`$, $`\omega=2`$ and $`\chi=3`$. [1–3]

## Applied significance

Consider unit-duration tasks with pairwise incompatibilities: vertices represent tasks, an edge means two tasks cannot run in the same slot, and colours represent slots. A proper colouring is exactly a feasible schedule in this model. A clique requires that many separate slots, while the elementary greedy argument guarantees at most $`\Delta+1`$ slots. The conjecture asks whether the rounded average of these lower and upper bounds always suffices.

This would give a universal guarantee for arbitrary conflict patterns. The connection is to the number of slots whose existence can be guaranteed; the conjecture by itself supplies neither an efficient way to compute a maximum clique nor a polynomial-time scheduling algorithm. Durations, precedence constraints and job-specific availability lists are outside this model.

## References

1. Marthe Bonamy, Thomas Perrett and Luke Postle, *Colouring Graphs with Sparse Neighbourhoods: Bounds and Applications*, [arXiv:1810.06704v1](https://arxiv.org/html/1810.06704v1), October 15, 2018. Cited preprint version: §1, Conjecture 1.1 and Theorem 1.7.
2. Eoin Hurley, Rémi de Joannis de Verclos and Ross J. Kang, *An Improved Procedure for Colouring Graphs of Bounded Local Density*, Advances in Combinatorics **2022:7**, 33 pp. [DOI](https://doi.org/10.19086/aic.2022.7); [published-version PDF, arXiv:2007.07874v3](https://arxiv.org/pdf/2007.07874v3), September 10, 2022. §1.2, Conjecture 1.7 and Theorem 1.10; §3.2, Theorem 3.2 and Remark 3.1.
3. Ken-ichi Kawarabayashi and Lucas Picasarri-Arrieta, *Coloring digraphs with $`\tilde{\Delta}-b`$ colors*, [arXiv:2607.06928v1](https://arxiv.org/html/2607.06928v1), July 8, 2026, preprint. §1, Conjectures 1 and 4, Corollary 3 and Theorem 7.
4. Andrew D. King and Bruce A. Reed, *Claw-free graphs, skeletal graphs, and a stronger conjecture on $`\omega`$, $`\Delta`$, and $`\chi`$*, [arXiv:1212.3036v1](https://arxiv.org/pdf/1212.3036v1), December 13, 2012. §1.1, Conjecture 1.1 and Theorems 1.3 and 1.6; cited as the arXiv version.
5. Shenwei Huang, Yidong Zhou and Yeonsu Chang, *The optimal chromatic bound for even-hole-free graphs without induced seven-vertex paths*, [arXiv:2602.04403v1](https://arxiv.org/pdf/2602.04403v1), February 4, 2026, preprint. §1, Theorem 1.1 and following remark; §2, graph conventions.
6. Ken-ichi Kawarabayashi and Lucas Picasarri-Arrieta, *An analogue of Reed's conjecture for digraphs*, [arXiv:2407.05827v4](https://arxiv.org/html/2407.05827v4), revised September 8, 2026, preprint; a shorter version appeared in SODA 2025. §1, Conjectures 1.1 and 1.6, Theorem 1.7 and following discussion; §2.1, conventions.

## Status review

Open in cited literature; no later resolution located as of 2026-09-18. Bonamy–Perrett–Postle explicitly state the conjecture. The independently authored July 2026 paper [3] retains the same exact inequality, as does the September 2026 revision [6]. The formulation here uses these full scholarly restatements; Reed's original 1998 article was not directly read.

The general partial bound in [2, Theorem 1.10] replaces the coefficient $`1/2`$ on the clique number by $`0.119`$ and assumes sufficiently large maximum degree. Its §3.2 explicitly uses a claimed Delcourt–Postle result; Remark 3.1 also gives a $`0.113`$ alternative from another result. The cited v3 incorporates the correction recorded in the arXiv history. Neither bound gives the conjectured coefficient at all degrees, and this review does not independently certify their proofs.

King–Reed prove the exact bound for claw-free graphs, meaning graphs with no induced three-leaf star. Their fractional-colouring theorem has a different optimum. Huang–Zhou–Chang's February 2026 theorem excludes both induced seven-vertex paths and induced even cycles of length at least four. These hypotheses do not cover arbitrary conflict graphs. [4, 5]

The July 2026 directed theorem [3, Theorem 7] requires the degree parameter to exceed a threshold depending on a fixed integer $`b`$. Restriction to symmetric digraphs yields the older large-degree statement in Corollary 3, not the uniform assertion in Conjecture 4 equivalent to Reed's bound. The September revision [6, Theorem 1.7] gives a positive interpolation coefficient for all digraphs; the following discussion explicitly distinguishes it from the conjectured one-half coefficient. No directed variant or graph subclass is counted separately.

The review covered unrestricted and recent proof, disproof, counterexample, correction and version searches. Source locations, namesake resolution claims and access limits are in the [evidence record](../candidates/reed-colouring.json). Regenerated dates printed inside older documents were not treated as revision dates.

This differs from [rapid sampling of proper colourings](../../../problems/272-coloring-glauber-threshold.md), which concerns mixing with at least $`\Delta+2`$ colours, and from [list edge-colouring](list-edge-colouring.md), which asks for a guarantee under arbitrary lists on edges. The [triangle packing–covering question](tuza-triangle-packing-covering.md) compares edge deletion and packing optima.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../batch-05-review.md). No matching later resolution was located.

Integrated page: [348. Reed's bound for the chromatic number](../../../problems/340-reed-colouring.md).
