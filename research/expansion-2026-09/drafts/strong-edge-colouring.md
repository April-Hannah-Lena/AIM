# The sharp degree bound for strong edge-colouring

**Area:** Communication networks, interference scheduling and graph colouring

**Status:** Accepted; integrated as entry 347

**Last checked:** 2026-09-19

## Problem statement

Let $G=(V,E)$ be a finite undirected multigraph with no loops and at least one edge. Parallel edges are distinct elements of $E$. Let $\Delta$ be the maximum vertex degree, counting edge multiplicity.

A strong edge-colouring with $k$ colours is a map $c:E\to\{1,\ldots,k\}$ such that distinct edges receive different colours whenever they share an endpoint or there is a third edge sharing an endpoint with each of them. Write $\chi'_s(G)$ for the smallest possible $k$.

Prove or disprove the **Erdős–Nešetřil strong edge-colouring conjecture**:
$$
\chi'_s(G)\le
\begin{cases}
\dfrac{5\Delta^2}{4}, & \Delta\ \text{even},\\[4pt]
\dfrac{5\Delta^2-2\Delta+1}{4}, & \Delta\ \text{odd},
\end{cases}
\qquad\text{for every such }G.
$$

The colours come from one common palette, and the colouring is integral. There is no restriction on graph size, degree, planarity, cycle lengths or bipartiteness, and no running-time requirement. Parallel edges are included explicitly in the conventions of [1, §1] and [2, §1].

Equivalently, $\chi'_s(G)=\chi(L(G)^2)$: the line graph $L(G)$ has one vertex for each edge of $G$, with adjacency when the original edges share an endpoint, and its square additionally joins vertices at distance two. The degree in the conjectured bound is that of the original multigraph $G$.

The proposed values are attained already by simple graphs. For even $\Delta$, replace each vertex of a five-cycle by an independent set of size $\Delta/2$ and each cycle edge by all edges between its two sets. For odd $\Delta\ge3$, use sets of size $(\Delta+1)/2$ at two consecutive cycle vertices and $(\Delta-1)/2$ at the other three. Every two edges conflict, and their number equals the proposed bound. A single edge handles $\Delta=1$. [1, p. 206; 3, §4.1]

## Applied significance

In a graph model of a communication network, edges represent transmissions and colours represent slots or frequencies. Suppose two transmissions conflict when they share a device or an endpoint of one is directly linked to an endpoint of the other. A strong edge-colouring is then exactly a schedule satisfying these interference rules. Source [6, §1] discusses the connection to radio-frequency assignment.

The conjecture asks for the sharp worst-case number of slots as a function of the maximum number of links incident to one device. The conclusion concerns existence of a schedule in this graph model; it does not specify an efficient scheduling algorithm or a physical signal-propagation law.

## References

1. R. J. Faudree, R. H. Schelp, A. Gyárfás and Zs. Tuza, *The strong chromatic index of graphs*, Ars Combinatoria 29(B) (1990), 205–211. [Author-hosted published scan](https://www.renyi.hu/~gyarfas/Cikkek/52_FaudreeSchelpGyarfasTuza_TheStrongChromaticIindexOfGraphs.pdf), §1, conventions p. 205 and Conjecture 1 p. 206.
2. Mingfang Huang, Michael Santana and Gexin Yu, *Strong chromatic index of graphs with maximum degree four*, Electronic Journal of Combinatorics 25(3) (2018), P3.31, published August 24. [Full paper](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i3p31/pdf/), §1, multigraph conventions p. 1, Conjecture 1 and Theorem 2 p. 2.
3. Daniel W. Cranston, *Coloring, List Coloring, and Painting Squares of Graphs (and other related problems)*, Electronic Journal of Combinatorics, Dynamic Survey DS25, version 3, July 3, 2026. [Full survey](https://www.combinatorics.org/ojs/index.php/eljc/article/download/ds25/pdf/), §4.1, Conjecture 28 and sharp examples p. 20; small-degree and clique-number discussion pp. 20–22.
4. Eoin Hurley, Rémi de Joannis de Verclos and Ross J. Kang, *An Improved Procedure for Colouring Graphs of Bounded Local Density*, Advances in Combinatorics 2022:7, 33 pp. [Published-version PDF, arXiv:2007.07874v3](https://arxiv.org/pdf/2007.07874v3), September 10, 2022; §1.1, Conjecture 1.4 and Theorem 1.6; §3.1.
5. Eoin Davey, Eoin Hurley, Rémi de Joannis de Verclos, Ross J. Kang and Jan Volec, *Strong edge-colouring via local flag algebras*, [arXiv:2607.17421v1](https://arxiv.org/html/2607.17421v1), submitted July 19, 2026, preprint. §1, Theorems 1.1–1.4 and the note on formal verification; §3, reductions. The displayed HTML typesetting date is August 24; the arXiv submission history supplies the version date.
6. Ilkyoo Choi, Jaehoon Kim, Alexandr V. Kostochka and André Raspaud, *Strong edge-colorings of sparse graphs with large maximum degree*, European Journal of Combinatorics 67 (2018), 21–39. [Full paper](https://kostochk.web.illinois.edu/docs/submit/ejc18ckr.pdf), §1, definition, conjecture and radio-network application, pp. 21–22.
7. Daniel W. Cranston, *Strong Edge-Coloring of Cubic Bipartite Graphs: A Counterexample*, [arXiv:2112.01443v1](https://arxiv.org/pdf/2112.01443v1), December 2, 2021. §1, six-part conjecture; §2, Main Theorem and Lemmas 1–2. Published subsequently in Discrete Applied Mathematics 321 (2022), 258–260; locators here refer to the three-page arXiv manuscript.

## Status review

Open in cited literature; no later resolution located as of 2026-09-19. Sources [1–3] explicitly pose the parity-sensitive bound. The review checked current and unrestricted searches for proofs, counterexamples, corrected versions and related formulations.

For the simple-graph case, the published general bound in [4, Theorem 1.6] is $1.772\Delta^2$ for sufficiently large $\Delta$. The July 2026 preprint [5, Theorem 1.1] reports an improvement to $1.73\Delta^2$, again at sufficiently large degree. Both constants exceed $5/4$. These simple-graph comparisons do not assert an unverified extension of the newer proofs to multigraphs. At degree four, [2, Theorem 2] gives $21$ colours, including for multigraphs; the target is $20$.

The bipartite and random-bipartite theorems in [5] impose additional hypotheses. Its random result holds with probability tending to one for fixed edge density and bounded part-size ratio; that does not cover every finite input. The accompanying [formalization record](https://github.com/rossjkang/localflagalgebras/blob/main/RESULTS.md), §§1 and 4, lists certificate calculations and an external colouring theorem among its remaining assumptions. The code and certificates were not rerun in this review.

The counterexample in [7] refutes a different proposed bound of five colours for cubic bipartite graphs of large girth. Its conclusion is $\chi'_s(G)>5$, whereas the present bound at degree three is $10$. Likewise, bounding the largest clique of $L(G)^2$ or treating graphs whose every pair of edges conflicts does not by itself bound the chromatic number for arbitrary $G$.

The [evidence record](../candidates/strong-edge-colouring.json) records the full scope comparisons, source access limits and finite-order computational claims. This differs from [entry 336](../../../problems/336-list-edge-colouring.md), which uses edge-specific colour lists and only shared-endpoint conflicts, and [entry 340](../../../problems/340-reed-colouring.md), whose bound depends on the degree and clique number of the graph being vertex-coloured. Parity, fixed-degree cases and the equivalent line-graph formulation are one problem family.

A separated adversarial self-pass checked the statement, recent theorem scopes, duplicates and applied interpretation on September 19, 2026. No independent agent or human review is claimed.
