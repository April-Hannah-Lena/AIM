# 334. List edge-colouring with no extra colours

**Area:** Scheduling, resource allocation and graph colouring

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-18

## Problem statement

Let $`G=(V,E)`$ be a finite undirected multigraph with no loops and at least one edge. Parallel edges are allowed. A proper edge-colouring assigns a colour to each edge so that distinct edges sharing an endpoint receive different colours. Write $`\chi'(G)`$ for the smallest number of colours needed when every edge may use the same palette.

For each edge $`e`$, let $`L(e)`$ be an arbitrary finite set of permitted colours. Prove or disprove the **List Edge-Colouring Conjecture**: for every such $`G`$ and every list assignment satisfying

```math
|L(e)|\geq\chi'(G)\qquad(e\in E),
```

there is a function $`c:E\to\bigcup_{e\in E}L(e)`$ such that

```math
c(e)\in L(e)\quad(e\in E),\qquad
c(e)\ne c(f)\quad\text{whenever distinct edges }e,f\text{ share an endpoint}.
```

Equivalently, is $`\chi'_\ell(G)=\chi'(G)`$ for every finite loopless multigraph, where the list chromatic index $`\chi'_\ell(G)`$ is the smallest integer $`k`$ for which every assignment of lists of size at least $`k`$ permits a proper edge-colouring? The lower bound follows by taking identical lists on all edges. All lists are given in advance. The question asks for existence, without a running-time requirement. The empty-edge case is automatic and is omitted only to avoid a convention for its indices.

## Application

Interpret vertices as resources and edges as unit-duration jobs that each occupy their two endpoint resources simultaneously. Colours represent time slots; jobs sharing a resource cannot run together. The list of a job specifies its available slots. This includes a basic model of direct packet exchanges with node contention, discussed by Iliopoulos–Sinclair in §1.

The conjecture asks whether giving every job at least the common-palette optimum number of available slots always guarantees a feasible schedule, regardless of which slots are available. This is a statement about the size of each availability set; those slots need not fit within a short common time horizon. Unequal job durations, precedence constraints and an efficient scheduling algorithm require separate analysis.

## References

1. Uwe Schauz, *Proof of the List Edge Coloring Conjecture for Complete Graphs of Prime Degree*, Electronic Journal of Combinatorics 21(3) (2014), P3.43. [Full paper](https://emis.de/ft/30050), definition on p. 1, Conjecture 1.1 on p. 2 and Theorems 1.4–1.5 on p. 3.
2. Abhishek Dhawan, *Multigraph edge-coloring with local list sizes*, Discrete Mathematics 348(6) (2025), 114420. [DOI](https://doi.org/10.1016/j.disc.2025.114420); [author version, arXiv:2307.12094v3](https://arxiv.org/html/2307.12094v3), January 15, 2025, §1, Definitions 1.1–1.2 and Theorem 1.4.
3. Jeff Kahn, *Asymptotics of the list-chromatic index for multigraphs*, Random Structures & Algorithms 17(2) (2000), 117–156. [Author manuscript](https://sites.math.rutgers.edu/~jkahn/LMULTI.pdf), §1, Theorem 1.1 and equation (3), printed p. 2.
4. Marthe Bonamy, Michelle Delcourt, Richard Lang and Luke Postle, *Edge-colouring graphs with local list sizes*, Journal of Combinatorial Theory, Series B 165 (2024), 68–96. [DOI](https://doi.org/10.1016/j.jctb.2023.10.010); [author version, arXiv:2007.14944v2](https://arxiv.org/html/2007.14944v2), November 8, 2023, §1, Conjecture 1 and Theorems 2–5.
5. Amir Jafari, *The List Edge-Coloring Conjecture for New Infinite Families*, [arXiv:2608.22895v2](https://arxiv.org/html/2608.22895v2), September 16, 2026. Preprint; §1, Theorems 1.1–1.2, §6 and Conclusion.
6. Fotis Iliopoulos and Alistair Sinclair, *Efficiently list-edge coloring multigraphs asymptotically optimally*, [arXiv:1812.10309v3](https://arxiv.org/html/1812.10309v3), December 7, 2021. §1, application and Theorems 1.2–1.4; citations here refer to this two-author version.
7. Joakim Blikstad, Ola Svensson, Radu Vintan and David Wajc, *Online Edge Coloring is (Nearly) as Easy as Offline*, [arXiv:2402.18339v1](https://arxiv.org/html/2402.18339v1), February 28, 2024. §1 and Appendix A, Theorem A.1.
8. Jonathan Narboni, *Vizing's edge-recoloring conjecture holds*, [arXiv:2302.12914v1](https://arxiv.org/html/2302.12914v1), February 24, 2023. §1, Theorem 7 and Lemma 8.
9. Yi-Jun Chang and Nima Dolatabadi, *Introvert Clustering for Distributed Graph Algorithms*, [arXiv:2609.10044v1](https://arxiv.org/html/2609.10044v1), September 9, 2026. Preprint; §1, distributed model and Theorem 1.

## Status review

**Known cases:** Galvin's theorem proves the exact list edge-colouring assertion for bipartite multigraphs.

**Remaining target:** The exact common-palette optimum as a sufficient list size for every finite loopless multigraph.

**Literature check:** Open in cited literature; no later resolution located.

Schauz states the multigraph conjecture explicitly; independently authored Dhawan §1 retains it in the 2025 work. Galvin's theorem settles bipartite multigraphs. Kahn's Theorem 1.1 gives asymptotic agreement with the fractional chromatic index, and Iliopoulos–Sinclair make an asymptotic guarantee constructive. A relative error tending to zero does not imply exact equality for every graph.

Bonamy–Delcourt–Lang–Postle's Theorem 5 concerns simple graphs, includes a minimum-degree condition and permits multiplicative slack in list sizes. Dhawan's Theorem 1.4 requires sufficiently large intersections of lists at each vertex. Arbitrary lists satisfying the proposed cardinality bound need not have such intersections.

Schauz's prime-degree complete-graph theorem is restricted to that family. Jafari's September 16 preprint states results for two further prime-indexed complete-graph families and specified matching deletions. Its full relevant statements and conclusion were checked: they do not cover all multigraphs. These are scoped preprint claims, not an independent certification of their proofs.

The online result of Blikstad and coauthors requires additional colours; Theorem A.1 specifies a positive slack term depending on degree and graph size. Narboni's theorem concerns Kempe transformations between ordinary colourings, without edge-specific list constraints. Neither supplies the asserted list-size guarantee.

The separate adversarial review also checked Chang–Dolatabadi's September 9 distributed algorithm. Their Theorem 1 assumes lists of size at least $`(3/2+\varepsilon)\Delta`$ and, outside the bipartite case, sufficiently large maximum degree $`\Delta`$. Its communication-round guarantee does not remove this extra-colour requirement.

The September 18 review included current and unrestricted proof, disproof, counterexample, correction and version searches. Exact reading locations and comparisons are in the [evidence ledger](../research/expansion-2026-09/candidates/list-edge-colouring.json). The arXiv version history, rather than a regenerated date printed inside its HTML, dates the Bonamy–Delcourt–Lang–Postle manuscript.

This is distinct from [three-processor precedence scheduling](302-three-processor-unit-scheduling.md), which asks about exact algorithmic complexity for jobs using one of three interchangeable processors. The present question is an existence guarantee for jobs requiring specified pairs of resources. Simple graphs, complete graphs and the equivalent index identity are included in this single entry.

A separated adversarial self-pass passed on September 18, 2026. No independent agent or human review is claimed.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../research/expansion-2026-09/batch-05-review.md). No matching later resolution was located.
