# The GNRS conjecture for minor-free network flow

**Integrated:** [503 — canonical entry](../../../problems/487-gnrs-minor-free-flow-cut.md) on 2026-09-23. This file preserves the September 19 research draft; use the canonical page for current status and wording.

**Area:** Network routing, metric geometry and combinatorial optimization

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-19

## Problem statement

A graph contains $`H`$ as a *minor* if a sequence of edge contractions and edge or vertex deletions produces $`H`$. Fix any finite simple graph $`H`$. Let $`G=(V,E)`$ range over finite connected undirected simple graphs that contain no $`H`$ minor. Give its edges arbitrary nonnegative lengths $`\ell:E\to[0,\infty)`$, and let $`d_\ell(u,v)`$ be shortest-path distance. Distinct vertices may have distance zero.

Does there exist a finite constant $`C_H\ge1`$, depending only on $`H`$, such that for every such $`(G,\ell)`$ there are an integer $`m\ge1`$ and a map $`f:V\to\mathbb R^m`$ satisfying

```math
d_\ell(u,v)\le\|f(u)-f(v)\|_1\le C_Hd_\ell(u,v)
\qquad\text{for every }u,v\in V,
```

where $`\|z\|_1=\sum_{j=1}^m|z_j|`$? The dimension and map may depend on the weighted graph. The constant must be independent of its size and length assignment. Zero-distance vertices may share an image. This is the Gupta–Newman–Rabinovich–Sinclair (GNRS) conjecture. [1, 2]

An equivalent formulation concerns fractional network routing. On such a supply graph $`G`$, choose finite nonnegative capacities $`c_e`$ and demands $`D_{uv}`$ for unordered pairs $`\{u,v\}\in\binom{V}{2}`$, with at least one positive demand. Let $`\mathcal P_{uv}`$ be the set of simple paths joining $`u`$ and $`v`$. Define $`\lambda^*`$ as the maximum $`\lambda\ge0`$ for which nonnegative real path weights $`x_{uv,P}`$ satisfy

```math
\begin{aligned}
\sum_{P\in\mathcal P_{uv}}x_{uv,P}&\ge\lambda D_{uv}
&&\text{for every }\{u,v\}\in\binom{V}{2},\\
\sum_{\{u,v\}\in\binom{V}{2}}\ \sum_{\substack{P\in\mathcal P_{uv}\\e\in P}}x_{uv,P}&\le c_e
&&\text{for every }e\in E.
\end{aligned}
```

Thus every demand receives the same multiplier, and traffic may split across paths. For a vertex set $`S`$, let $`\delta_G(S)`$ be the edges with exactly one endpoint in $`S`$, and set

```math
D(S)=\sum_{\substack{\{u,v\}\in\binom{V}{2}\\|\{u,v\}\cap S|=1}}D_{uv},
\qquad
\Phi=\min_{\substack{S\subseteq V\\D(S)>0}}
\frac{\sum_{e\in\delta_G(S)}c_e}{D(S)}.
```

Every cut bounds the routable multiplier from above. The equivalent conjecture asks for

```math
\frac{\Phi}{C_H}\le\lambda^*\le\Phi
```

for every capacity and demand assignment. This formulation also covers $`\Phi=0`$ without dividing by $`\lambda^*`$. The demand pairs are arbitrary; only the supply graph excludes $`H`$. No integral or single-path routing is required. The equivalence holds after taking the worst case over length assignments and, respectively, capacity and demand assignments on the same graph. [1, Theorem 3.2; 2, Theorem 1.1; 3, §19.1]

## Applied significance

In a communication network, edge capacities limit link traffic while many source–destination pairs compete for those links. A cut gives a necessary bottleneck bound: traffic crossing a partition cannot exceed its total link capacity. GNRS asks whether network topology alone makes these bounds sufficient up to a constant loss in every demanded transfer rate. It would provide a uniform comparison between bottleneck certificates and achievable fractional throughput for planar networks and other networks excluding a fixed minor. [1–3]

The associated sparsest-cut relaxation is used to find network partitions and analyze routing and layout algorithms. The constant is uniform as a network grows within the chosen graph class; an arbitrary size-dependent bound would not give that guarantee. This is an idealized capacitated-flow model and does not include interference, packet deadlines or queueing delay. [1, 2]

## References

1. Anupam Gupta, Ilan Newman, Yuri Rabinovich and Alistair Sinclair, *Cuts, Trees and ℓ1-Embeddings of Graphs*, Combinatorica **24** (2004), 233–269, [publisher record](https://link.springer.com/article/10.1007/s00493-004-0015-x). The accessible [author manuscript](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf), dated October 22, 2002, gives the definitions in §2, Theorem 3.2 and the unnumbered conjecture in §3, internal pp.7–8; restricted results in Theorems 4.1 and 4.8.
2. James R. Lee and Anastasios Sidiropoulos, *On the Geometry of Graphs with a Forbidden Minor*, STOC 2009, 245–254. [Author-hosted proceedings text](https://people.csail.mit.edu/tasos/papers/geoforbid_stoc2009.pdf), §1, Theorem 1.1, Conjectures 1–3 and Theorems 1.4 and 1.8.
3. Chandra Chekuri, *CS 583: Approximation Algorithms*, [lecture notes](https://courses.grainger.illinois.edu/CS583/sp2026/approx-algorithms-lecture-notes.pdf), May 4, 2026; Chapter 19, pp.248–252 and bibliographic notes p.267.
4. Arnold Filtser, *A Face Cover Perspective to ℓ1 Embeddings of Planar Graphs*. [Revised author manuscript, arXiv:1903.02758v4](https://arxiv.org/html/1903.02758v4), July 28, 2024; preliminary version SODA 2020. §1, Theorem 1 and Corollaries 1–2; §2 definitions. Journal DOI 10.1145/3686800; the inspected full text is the arXiv version.
5. Nikhil Kumar, *An Approximate Generalization of the Okamura–Seymour Theorem*, FOCS 2022, 1093–1101. [Revised author manuscript, arXiv:2208.00795v3](https://arxiv.org/pdf/2208.00795v3), January 10, 2025, §§2–3, Theorems 5–6, internal pp.5–6.
6. David Alemán Espinosa and Niklas Schlomberg, *Pinning on Tight Cuts: Improved Algorithm and Bounds for Unsplittable Multicommodity Flows in Outerplanar Graphs*, ICALP 2026, LIPIcs **374**, Article 11. [Full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.11/LIPIcs.ICALP.2026.11.html), §§1.1–1.3 and 2.1, Theorems 1–2.
7. Chandra Chekuri, Guyslain Naves, Joseph Poremba and F. Bruce Shepherd, *Uncrossed Multiflows and Applications to Disjoint Paths*, APPROX/RANDOM 2026, LIPIcs **392**, 12:1–12:23, published September 9, 2026. [Full proceedings text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol392-approx-random2026/LIPIcs.APPROX-RANDOM.2026.12/LIPIcs.APPROX-RANDOM.2026.12.pdf), Theorems 1–3, Corollaries 4–5 and §§2.4–3.
8. Daniel Agassy, Dani Dorfman and Haim Kaplan, *Improved Tree Sparsifiers in Near-Linear Time*, ICALP 2026, LIPIcs **374**, Article 7. [Full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.7/LIPIcs.ICALP.2026.7.html), §2, Claim 2.7 and Theorem 2.8.

## Status review

The May 2026 notes [3] explicitly retain GNRS and its planar case as open. The independently authored July 2026 paper [6, §1.3] still reports a planar flow-cut gap between the lower bound $`2`$ and the upper bound $`O(\sqrt{\log n})`$, where $`n=|V|`$. The upper bound grows with graph size. A constant bound for all planar supply graphs with arbitrary demands remains unproved in these sources.

The original paper settles restricted classes, including graphs of treewidth two. Its bound in terms of $`|E|-|V|+1`$ concerns cycle rank, not surface genus. Lee–Sidiropoulos settle classes excluding a fixed tree and reduce general GNRS to planar and clique-sum conjectures; the reduction does not prove those remaining statements. [1, 2]

Filtser's terminal embedding has distortion $`O(\sqrt{\log(\gamma+1)})`$, where $`\gamma`$ is the number of faces needed to cover the terminals in a fixed planar drawing; the extra one accommodates the separately solved single-face case. This is constant for bounded $`\gamma`$, but not for unrestricted terminal placement. Kumar's constant bound requires each demanded pair to share a face. Such a face may vary between pairs, but arbitrary pairs need not share any face. [4, 5]

The 2026 outerplanar result rounds an already feasible fractional flow while allowing additive capacity overflow. The September result requires a strongly uncrossed fractional flow for its congestion rounding, and obtains approximation results for pairwise-planar demand layouts; its integral flow–multicut comparison uses a different objective from concurrent flow versus sparsest cut. The new tree sparsifier has a polylogarithmic quality bound. None gives the general size-independent constant sought here. [6–8]

The [evidence record](../candidates/gnrs-minor-free-flow-cut.json) records actual searches, source versions, theorem-scope comparisons and access limits. The publisher's original GNRS text and Filtser's journal text were not accessed in full; author versions were inspected. The September 19, 2026 check covered named and mathematical formulations, recent and unrestricted-date resolution searches, author pages, revisions and corrections. A64 was a separated adversarial self-review by the same assistant; it also checked directed-flow results and constant-distortion embeddings into the maximum norm. It was not an independent expert review or a certification of the cited proofs.

The [Li–Li question](../../../problems/298-li-li-multiple-unicast.md) compares coding with fractional routing. The [strong thin-tree question](../../../problems/323-strong-thin-tree.md) selects a spanning tree under cut constraints. Neither is this comparison of cut bottlenecks with fractional routing. The planar case and equivalent metric formulation receive no separate entry.
