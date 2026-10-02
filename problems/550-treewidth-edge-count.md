# 550. Maximum treewidth at a prescribed edge count

**Area:** Statistical computation and extremal graph theory

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

For an integer $`e\ge1`$, let

```math
t(e)=\max\{\mathop{\mathrm{tw}}\nolimits(G):G\text{ is a finite simple graph with }|E(G)|=e\}.
```

Here a tree decomposition consists of vertex sets indexed by the nodes of a tree, with every graph vertex in some set, both endpoints of every edge in some set, and the sets containing any fixed vertex forming a connected subtree. Its width is the largest set size minus one, and $`\mathop{\mathrm{tw}}\nolimits(G)`$ is the minimum such width.

Determine $`t(e)`$ for general $`e`$: find a sharp edge-count bound valid for every finite simple graph and graph constructions attaining it. Equivalently, determine the minimum number of edges needed for treewidth at least $`k`$, for every positive integer $`k`$. Exhaustive enumeration for finitely many edge counts does not settle the general extremal question.

## Application

Exact computation of structured higher-order $`U`$-statistics can be reduced to tensor contractions whose cost depends on the treewidth of a decomposition graph and its quotients. Sharp bounds in terms of the number of interactions would give tighter worst-case computational guarantees for these estimators.

## References

1. X. Chen, L. Liu and R. Zhang, [On computing and the complexity of computing higher-order U-statistics, exactly](https://doi.org/10.1007/s11222-026-10974-x), *Statistics and Computing* **36**,223 (2026), Remark11 and supplementary AppendixF. [arXiv:2508.12627v3](https://arxiv.org/html/2508.12627v3), AppendixF and Observation1; proof in AppendixG.
2. J. Kneis, D. Mölle, S. Richter and P. Rossmanith, [A Bound on the Pathwidth of Sparse Graphs with Applications to Exact Algorithms](https://doi.org/10.1137/080715482), *SIAM Journal on Discrete Mathematics* **23**(1) (2009),407–427, Theorem4.7.

## Status review

**Known cases:** Reference1 proves

```math
t(e)=1\ (1\le e\le2),\quad 2\ (3\le e\le5),\quad
3\ (6\le e\le9),\quad4\ (10\le e\le14),\quad t(15)=5.
```

Reference2 gives the general upper bound $`\mathop{\mathrm{tw}}\nolimits(G)\le |E(G)|/5.769+O(\log |V(G)|)`$. Isolated vertices can be removed, so this yields $`t(e)\le e/5.769+O(\log e)`$. Clique constructions give $`t(e)\ge\lfloor(\sqrt{8e+1}-1)/2\rfloor`$ by adding disjoint edges as needed; this elementary lower bound is not claimed optimal.

**Remaining target:** The sharp extremal function for unbounded edge counts. The listed small cases and general upper bound do not determine it.

Reference1 explicitly poses the general sharp edge-count bound as unresolved. Its August2026 revision retains the question, and the journal published the paper on23September2026. The bound from2 applies to pathwidth and hence also to treewidth. Efficient algorithms for finding a decomposition of a given graph do not answer this extremal question over all graphs.

Current-source, author-code and announcement searches through24September2026 found no matching general solution. Palomar returned no treewidth entry; the author repositories' issue and pull-request lists concern implementations and benchmarks. The Zenodo API was unavailable and indexed searches found no matching resolution. See the batch review for evidence and search limits.
