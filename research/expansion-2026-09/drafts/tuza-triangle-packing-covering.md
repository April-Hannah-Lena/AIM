# The factor-two relation between triangle deletion and packing

**Area:** Combinatorial optimization and network modification

**Status:** Accepted; integrated as entry 338

**Last checked:** 2026-09-18

## Problem statement

Let $G=(V,E)$ be any finite simple undirected graph. Write $\mathcal T(G)$ for the collection of three-edge subsets of $E$ that form triangles. Define the triangle packing and covering numbers by

$$
\nu_\triangle(G)=\max\bigl\{|\mathcal P|:\mathcal P\subseteq\mathcal T(G),\quad
T\cap T'=\varnothing\text{ for distinct }T,T'\in\mathcal P\bigr\}
$$

and

$$
\tau_\triangle(G)=\min\bigl\{|F|:F\subseteq E,\quad
F\cap T\ne\varnothing\text{ for every }T\in\mathcal T(G)\bigr\}.
$$

Thus a packing consists of edge-disjoint triangles, which may share vertices. A cover selects edges whose deletion removes every triangle. Both numbers are zero when $G$ has no triangles.

Prove or disprove **Tuza's triangle packing–covering conjecture**:

$$
\tau_\triangle(G)\leq 2\nu_\triangle(G)
\qquad\text{for every finite simple undirected graph }G.
$$

The extrema are integral and unweighted. The bound must hold exactly, without an additive error or a restriction on graph size, degree or density. This is an existence assertion; it does not require a polynomial-time algorithm. The constant cannot be reduced: the complete graph $K_4$ has packing number one and covering number two. [1, 2]

## Applied significance

This is a packing–covering question in combinatorial optimization. In its network-modification interpretation, one wants to disable every three-link closed interaction by deleting as few links as possible. An edge-disjoint family of triangles certifies a necessary deletion budget, since each member needs a different deleted edge. The conjecture asks whether the optimal budget is always at most twice the strongest such certificate.

Equivalently, form a hypergraph whose vertices are the network edges and whose hyperedges are its triangles. The question compares integral matching and vertex-cover optima in this structured family. Linear-programming relaxations already satisfy related factor-two bounds, but transferring them to the two integral optima is unresolved. This is a foundational optimization connection; the conjecture alone does not supply an efficient method for finding either optimum. [1, 2]

## References

1. Michael Krivelevich, *On a conjecture of Tuza about packing and covering of triangles*, Discrete Mathematics **142** (1995), 281–286. [Author-hosted published paper](https://www.math.tau.ac.il/~krivelev/2.pdf), §1, definitions and Conjecture 1, pp. 281–282; Theorems 6–8, pp. 283–284.
2. Venkatesan Guruswami and Sai Sandeep, *Approximate Hypergraph Vertex Cover and Generalized Tuza's Conjecture*, SIAM Journal on Discrete Mathematics **39**(2) (2025), 1312–1334. [Publication record](https://doi.org/10.1137/23M1570351); accessible [arXiv:2008.07344v2](https://arxiv.org/html/2008.07344v2), November 10, 2020, §1 and Theorems 1 and 3. The locators here refer to the preprint.
3. Patrick Bennett, Ryan Cushman, Andrzej Dudek and Xavier Pérez-Giménez, *Almost-perfect packings and Tuza's conjecture in the random geometric graph*, [arXiv:2606.09736v1](https://arxiv.org/html/2606.09736v1), June 8, 2026, preprint. §1, Conjecture 1, Theorems 1–2 and Corollary 3.
4. Jeff Kahn and Jinyoung Park, *Tuza's conjecture for random graphs*, [arXiv:2007.04351v2](https://arxiv.org/html/2007.04351v2), July 10, 2020. §1, Theorem 1.2; cited version is the preprint.
5. Jacob D. Baron and Jeff Kahn, *Tuza's Conjecture is Asymptotically Tight for Dense Graphs*, Combinatorics, Probability and Computing **25**(5) (2016), 645–667. [DOI](https://doi.org/10.1017/S0963548316000067); [arXiv:1408.4870v2](https://arxiv.org/pdf/1408.4870v2), October 20, 2015, §1, Conjectures 1.1–1.2 and Theorem 1.3, pp. 1–3.
6. Anish Gupta, *Tuza's conjecture for graphs of maximum degree at most seven*, [arXiv:2608.06538v1](https://arxiv.org/html/2608.06538v1), August 6, 2026, preprint. §1, Conjecture 1.1 and Theorems 1.3–1.4.
7. Zijian Zeng, *Tuza's Conjecture for Split Graphs with an Eight-Vertex Clique Part and Two Neighborhood Types*, [Preprints.org, version 1](https://www.preprints.org/manuscript/202608.1304), posted August 19, 2026. §§1 and 3, Theorems 1–2 and Corollary 1.
8. Épi Team / Bake AI, *Tuza's inequality with three neighborhood types*, public research artifact, [released statement and proof outline](https://github.com/BakeLab/Epi-results/blob/97fa6a420f417458e11723c8bceb70f1529e447a/mathematics/tuza/PROOF.md), revision of September 14, 2026. Opening theorem and the classification, finite-certificate and arbitrary-multiplicity sections.

## Status review

Open in cited literature; no later resolution located as of 2026-09-18. Krivelevich gives the full formulation, while the independently authored 2026 paper [3] retains it and reports Haxell's general bound $\tau_\triangle\leq(66/23)\nu_\triangle$. The unresolved target is the exact factor two for every graph.

Krivelevich proves $\tau_\triangle\leq2\tau_\triangle^*$ and $\nu_\triangle^*\leq2\nu_\triangle$, where stars denote fractional optima and linear-programming duality gives $\tau_\triangle^*=\nu_\triangle^*$. These two inequalities do not combine into the conjectured factor two. His integral result excludes subdivisions of $K_{3,3}$. Guruswami–Sandeep's counterexamples to a proposed forbidden-subhypergraph explanation concern a larger hypergraph family; they do not refute the triangle-hypergraph assertion. [1, 2]

Kahn–Park prove the inequality with probability tending to one in $G(n,p)$ for every function $p=p(n)$. Bennett and coauthors obtain it for random geometric graphs in specified sparse and dense radius ranges. Neither is an assertion about every finite graph. Baron–Kahn's construction refutes Yuster's proposed improvement in dense graphs and approaches Tuza's factor two; their theorem does not assert a violation of Tuza's inequality. [3–5]

Gupta's August 2026 preprint claims the maximum-degree-seven case. Zeng's theorem assumes a split partition with an eight-vertex clique and at most two active neighborhood types; its additional maximum-cut criterion is sufficient, not automatic. The September Épi artifact extends the fixed-eight-clique result to three active neighborhood types with arbitrary multiplicities. Their complete relevant statements were checked, but their computer-assisted certificates were not independently rerun. All retain hypotheses absent from the unrestricted question. [6–8]

The review covered current and unrestricted searches for proofs, disproofs, counterexamples, corrections, versions and equivalent formulations. Haxell's original full text was inaccessible in this check; its bound is explicitly reported in [3, 4]. The 2025 journal metadata in [2] was verified, and its accessible preprint was read. Additional dense-graph and algorithmic sufficient-condition results are compared in the [evidence record](../candidates/tuza-triangle-packing-covering.json).

The [strong thin-tree question](../../../problems/326-strong-thin-tree.md) selects a connected spanning subnetwork under all-cut bounds. The [list edge-colouring draft](list-edge-colouring.md) concerns scheduling edges into matchings. Neither compares triangle deletion with edge-disjoint triangle packing. Equivalent edge-decomposition formulations and graph subclasses are included in this single entry.

A separated adversarial self-pass passed on September 18, 2026. No independent agent or human review is claimed.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../batch-05-review.md). No matching later resolution was located.

Integrated page: [346. The factor-two relation between triangle deletion and packing](../../../problems/338-tuza-triangle-packing-covering.md).
