# 491. Deterministic parallel perfect matching in general graphs

**Area:** Parallel algorithms and combinatorial optimization

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-23

## Problem statement

Let $`G=([n],E)`$ be a finite simple undirected graph, where $`[n]=\{1,\ldots,n\}`$ and $`n\ge2`$. A **perfect matching** is a subset $`M\subseteq E`$ such that every vertex belongs to exactly one edge of $`M`$. The input consists of the $`\binom n2`$ adjacency bits, one for each unordered pair of vertices.

Is there a deterministic algorithm in uniform $`\mathrm{NC}`$ that, on every such input, returns a perfect matching if one exists and correctly reports nonexistence otherwise? This is the general-graph search question stated by Svensson–Tarnawski and Anari–Vazirani. [1, 3]

More precisely, seek absolute constants $`K,c,k>0`$ and a logspace-uniform family of Boolean circuits $`(C_n)_{n\ge2}`$ satisfying

```math
\mathop{\mathrm{size}}\nolimits(C_n)\le K n^c,
\qquad
\mathop{\mathrm{depth}}\nolimits(C_n)\le K\bigl(\log_2(n+2)\bigr)^k.
```

The gates are fan-in-two AND and OR, NOT, and constants. The output contains a success bit and an edge-incidence vector. Success must hold exactly when a perfect matching exists; on success, the vector must encode one. Logspace uniformity means that one deterministic machine, given $`1^n`$, writes the description of $`C_n`$ using $`O(\log n)`$ work space. This fixes the usual effective circuit convention for $`\mathrm{NC}`$. [2, Definition 7.1]

The guarantee is worst-case and exact, over all input graphs. There is no bipartiteness, planarity, bounded-degree or uniqueness promise. A maximal matching, which cannot be enlarged by adding an edge, need not cover every vertex. Merely deciding whether a perfect matching exists is a related question; its equivalence to this search task is not assumed.

## Application

A compatibility graph models a collection of participants or devices that must be paired: an edge permits a pair, and a perfect matching pairs everyone without conflicts. In a communication round with pairwise exchanges, the same model asks whether every device can participate exactly once and, if so, which exchanges to schedule.

A positive answer would establish that this global coordination task can be performed deterministically with polylogarithmic parallel depth and polynomial total circuit size. Sequential polynomial-time solvability is already known. The issue is how far parallelism can reduce the dependence between computational steps. This is an asymptotic capability question; it does not by itself predict speed on a fixed GPU or a network with communication constraints.

## References

1. Ola Svensson and Jakub Tarnawski, *The Matching Problem in General Graphs is in Quasi-NC*, FOCS 2017, 696–707, DOI 10.1109/FOCS.2017.70. [Full version, arXiv:1704.01929v2](https://arxiv.org/pdf/1704.01929v2), September 4, 2017: §1, Theorem 1.2, §1.4 and §2.1.
2. Jakub Tarnawski, *New Graph Algorithms via Polyhedral Techniques*, EPFL thesis 9622 (2019). [Institutional full text](https://infoscience.epfl.ch/server/api/core/bitstreams/f4aa4b6a-5245-4adc-a748-7a0597f5368c/content), Definition 7.1, p.81, and Open question 7, p.123.
3. Nima Anari and Vijay V. Vazirani, *Matching Is as Easy as the Decision Problem, in the NC Model*, ITCS 2020, LIPIcs 151, 54:1–54:25. [Published paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol151-itcs2020/LIPIcs.ITCS.2020.54/LIPIcs.ITCS.2020.54.pdf), Theorem 1, §4 and Corollary 39. Also checked: [arXiv:1901.10387v5](https://arxiv.org/html/1901.10387v5), November 9, 2020, Notation 1, Theorem 2 and §1.2.
4. Abhranil Chatterjee, Sumanta Ghosh, Rohit Gurjar, Roshan Raj and Thomas Thierauf, *Bipartite Matching is in NC*, ECCC TR26-100, [revision 2](https://eccc.weizmann.ac.il/report/2026/100/revision/2/download), July 15, 2026, preprint: Theorems 1.1–1.2 and 1.5; Definitions 1.3–1.4.
5. Swastik Kopparty and Shubhangi Saraf, *On the CGGRT Criterion for Detecting Bipartite Perfect Matchings in NC*, [arXiv:2607.15554v1](https://arxiv.org/html/2607.15554v1), July 17, 2026, preprint: §1 and Theorem 1.1.
6. Hiroshi Hirai, Yuni Iwamasa, Taihei Oki and Tasuku Soma, *Algebraic combinatorial optimization on the degree of determinants of noncommutative symbolic matrices*, Mathematical Programming 213 (2025), 941–984, published online November 2, 2024. [Full text and DOI](https://link.springer.com/article/10.1007/s10107-024-02158-0), §§2.3.1–2.3.3, especially equation (2.9).
7. Gil Kalai, *Matching in NC and Local Events*, [author's specialist commentary](https://gilkalai.wordpress.com/2026/06/22/matching-in-nc-and-local-events/), June 22, 2026, opening section and June 25 clarification by Rohit Gurjar. This is expert commentary, not a research-paper proof.
8. Gregory Schwing, Daniel Grosu and Loren Schwiebert, *Parallel Maximum Cardinality Matching for General Graphs on GPUs*, IPDPSW 2024. [Author manuscript](https://dgrosu.eng.wayne.edu/_resources/pdfs/pdco24-gpu-match-cr.pdf), §§I–III, Algorithms 1–2 and §III.B.
9. Foram Lakhani and Partha Mukhopadhyay, *Approximating commutative rank of matrix spaces in NC*, [ECCC TR26-185](https://eccc.weizmann.ac.il/report/2026/185/download), posted September 17, 2026; manuscript dated September 15. Preprint: Theorem 1.1, Theorem 5.4 and §§5.1–5.2.
10. Hiroshi Hirai, *On integral polytopes related to Edmonds' problem*, [arXiv:2609.19703v1](https://arxiv.org/html/2609.19703v1), September 17, 2026, preprint: definitions (2.7), (3.1), (3.6) and Theorems 3.13–3.14.
11. Srijan Chakraborty, Samir Datta, Aryan Kusre, Partha Mukhopadhyay and Amit Sinhababu, *Maximum Matching and Related Problems in Catalytic Logspace*, ECCC TR26-080, [revision 1](https://eccc.weizmann.ac.il/report/2026/080/revision/1/download), June 1, 2026; manuscript dated May 31. Preprint: introduction, Theorem 1.1 and Definitions 2.1–2.2.

## Status review

**Known cases:** Deterministic NC constructions are known for planar and suitably embedded low-genus graphs; see reference 3. The 2026 bipartite result is recorded separately as a preprint.

**Remaining target:** A uniform deterministic polynomial-size, polylogarithmic-depth construction for arbitrary graphs.

**Integration review (2026-09-23):** The September 19 source audit was refreshed with problem-specific web searches and searches scoped to arXiv, Zenodo, GitHub and Palomar. No matching full-scope solution announcement was located. Search coverage is limited by indexing and access; this is not a proof of openness. See the [integration record](../research/integration-2026-09-23.md).

Open in cited literature; no later resolution located as of 2026-09-19. The independent research formulation in [3] retains the general-graph search question. After the bipartite breakthrough, Kalai explicitly identifies construction for general graphs as a remaining problem [7]. His statement is dated June 2026; it is not a September status certificate. Current and unrestricted searches, revisions and possible indirect resolutions were checked on the date above.

Svensson–Tarnawski obtain depth $`O(\log^3 n)`$ with $`n^{O(\log^2 n)}`$ processors [1]. The latter bound is quasipolynomial, not polynomial. Randomized and pseudodeterministic parallel algorithms also leave a randomness requirement [3].

The July revision of [4] gives deterministic $`\mathrm{NC}`$ algorithms for bipartite matching, including polynomially bounded weights, and for linear matroid intersection. The independently authored criterion [5] also requires a bipartite graph. Those results do not supply the general-graph construction requested here.

The noncommutative-rank result in [4] needs a further distinction. For a general graph's Tutte matrix, ordinary rank detects integral matching whereas noncommutative rank corresponds to fractional matching [6]. The two ranks already differ for a triangle. Thus replacing the former by the latter is not an indirect solution.

Anari–Vazirani's reduction [3] assumes an oracle for deciding whether a perfect matching of **weight at most a supplied threshold** exists, with polynomially bounded integer edge weights. Their latest revision explicitly distinguishes that oracle from unweighted existence. Their Corollary 39 solves embedded graphs with genus $`O(\log n)`$, a restricted class.

The GPU implementation [8] allows up to $`n`$ breadth-first-search iterations per phase and uses randomized initialization. Its empirical speedups do not establish the required deterministic polylogarithmic bound. Its full manuscript was read after verified HTTPS downloads failed; that transport limitation is recorded.

The September 17 rank-approximation preprint [9] assumes fixed accuracy $`\varepsilon>0`$. Its polynomial-size guarantee depends on a fixed parameter $`k=\lceil1/\varepsilon-1\rceil`$; choosing accuracy depending on graph size to force exact rank is not covered. Hirai's same-week result [10] identifies the second blow-up with a fractional relaxation and bounds its gap. It does not identify that relaxation with integral matchings or provide the requested parallel construction.

The catalytic-logspace construction [11] does handle general graphs. Its model permits a polynomial-sized auxiliary tape that must be restored, and its time bound is polynomial. Those resource bounds do not give the polylogarithmic depth requested here; the paper separately identifies the parallel question as unresolved.

The [evidence record](../research/expansion-2026-09/candidates/general-graph-perfect-matching-nc.json) supplies reading locations, source histories, comparisons and review details. The thesis [2] shares an author with [1] and is not independent corroboration. The work has a separated adversarial self-review, not independent expert review or certification of the cited proofs.

[Entry 311](311-deterministic-polynomial-identity-testing.md) concerns sequential polynomial-time identity testing for general arithmetic circuits. The Tutte-matrix connection does not equate that target with the present parallel search bound. [Entry 334](334-list-edge-colouring.md) asks for existence of an entire list-constrained edge-colouring, without a parallel algorithm. The general matching question and its contextual variants form one entry here.
