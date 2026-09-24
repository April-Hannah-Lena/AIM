# 598. Sidorenko's lower bound for bipartite homomorphism counts

**Area:** Information theory and graphical models

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

Let $`H`$ be a finite simple bipartite graph with $`v`$ vertices and $`e\geq1`$ edges. For a finite simple graph $`G`$ on $`n\geq1`$ vertices, let $`\mathop{\mathrm{hom}}\nolimits(H,G)`$ count all maps $`f:V(H)\to V(G)`$ that preserve adjacency. These maps need not be injective. Define the edge density $`p=2|E(G)|/n^2`$.

Prove or disprove that, for every such pair of graphs,

```math
\frac{\mathop{\mathrm{hom}}\nolimits(H,G)}{n^v}\geq p^e.
```

This is Sidorenko's conjecture. It says that the density of any fixed bipartite pattern is at least the corresponding independent-edge baseline. The displayed inequality is the unweighted specialization of Conjecture I.1 in [1].

## Application

Homomorphism counts are partition functions of finite-state graphical models. A general lower bound gives a rigorous baseline for counting and approximate inference, and helps assess variational approximations such as the Bethe free energy. Entropy inequalities are one of the principal tools for proving the bound.

## References

1. P. Csikvári, N. Ruozzi, and S. Shams, [Markov Random Fields, Homomorphism Counting, and Sidorenko's Conjecture](https://doi.org/10.1109/TIT.2022.3169487), *IEEE Transactions on Information Theory* **68**(9) (2022), 6052–6062. Conjecture I.1 and the following unweighted specialization; [author manuscript](https://real.mtak.hu/162333/1/Markov_random_fields_Sidorenko.pdf), page 2.
2. Y. Zhao, [Conjugacy Class Averages and Sidorenko's Conjecture](https://arxiv.org/abs/2606.15368), arXiv:2606.15368 (2026).

## Status review

**Known cases:** Trees, even cycles, cubes, and bipartite graphs having a vertex adjacent to every vertex in the opposite part satisfy the inequality; [1] reviews these cases and proves additional weighted results. The 2026 work [2] gives a conditional reduction through conjugacy averaging and proves an inequality for particular subdivision graphs and averaged Cayley kernels.

**Remaining target:** Establish the bound for every bipartite pattern and every host graph, or exhibit a counterexample. The stronger universal Bethe lower bound in [1, Conjecture I.2] is disproved in that same paper and is excluded here. Counterexamples to hypergraph versions also do not settle the graph conjecture.

Searches through 24 September 2026 found no matching general solution or repository duplicate. Two GitHub pull requests describe completed proofs, but their theorem statements respectively assume that the pattern has no edges and assume the desired inequality for the nontrivial cases; neither proves this target. Other inspected formalizations concern known special cases or explicitly retain the general conjecture. Native Zenodo searches returned two unrelated resolution deposits, and Palomar returned no matching record.
