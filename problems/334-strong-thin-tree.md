# 334. Strong thin-tree conjecture

**Area:** Network design and combinatorial optimization

**Status:** Open in cited literature; no later resolution located.

**Last checked:** 2026-09-18

## Problem statement

Let $G=(V,E)$ be a finite undirected loopless multigraph with at least two vertices. Parallel edges are counted separately. For a nonempty proper set $S\subsetneq V$, write $\delta_G(S)$ for the edges with exactly one endpoint in $S$. For an integer $k\ge1$, call $G$ $k$-edge-connected if $|\delta_G(S)|\ge k$ for every such $S$.

Does there exist an absolute constant $C>0$ such that every $k$-edge-connected $G$, for every $k\ge1$, has a spanning tree $T\subseteq E$ satisfying

$$
|T\cap\delta_G(S)|\le\frac{C}{k}\,|\delta_G(S)|
\qquad\text{for every }\varnothing\ne S\subsetneq V?
$$

The same tree must satisfy every cut inequality, and $C$ must be independent of $k$, $G$ and $|V|$. Edges are unweighted. This is the strong thin-tree conjecture; the question requires existence, without an efficient construction or verification algorithm. Goddyn's weaker version permits an arbitrary thinness bound tending to zero with connectivity. It is included here as context, without a separate count or a claim of equivalence. [1, 2]

## Applied significance

A spanning tree supplies a connected backbone in a communication or transport network. Thinness limits the fraction of available links that this backbone uses across every partition of the network. A positive answer would also guarantee that, when $k>C$, removing the tree leaves edge connectivity at least $k-C$: every remaining cut has at least $(1-C/k)|\delta_G(S)|$ edges. This connects the conjecture to preserving network redundancy while reserving a connected subnetwork. [1]

Thin trees also support rounding arguments for asymmetric routing. An existence theorem would provide a constant integrality bound for the directed traveling-salesman relaxation; a corresponding efficient construction would yield an approximation algorithm. Constant bounds for that routing problem already exist by other methods. This connection does not establish the sharp factor two asked for in [entry 323](323-asymmetric-tsp-integrality-gap.md). [1, 2]

## References

1. Nathan Klein, Neil Olver and Zi Song Yeoh, *Thin Trees for near Minimum Cuts*, ICALP 2026, LIPIcs 374, 129:1–129:18, published July 1, 2026, [DOI and publication record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.129). [Full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.129/LIPIcs.ICALP.2026.129.html), §1, Theorems 1–2 and §2.1.
2. Nima Anari and Shayan Oveis Gharan, *Effective-Resistance-Reducing Flows, Spectrally Thin Trees, and Asymmetric TSP*, FOCS 2015, 20–39. Accessible [arXiv:1411.4613v4](https://arxiv.org/html/1411.4613v4), revised September 1, 2015: Definition 1.1, Theorem 1.2, discussion after Conjecture 1.3, §1.1 and Corollary 1.8.
3. Alice Moayyedi, *Thin Tree Verification is coNP-Complete*, [arXiv:2512.25043v1](https://arxiv.org/html/2512.25043v1), December 31, 2025, preprint, §1 Conjecture 1, Theorem 1 and Remark 1.
4. Mohit Daga, *Thin Trees via k-Respecting Cut Identities*, [arXiv:2510.12050v1](https://arxiv.org/html/2510.12050v1), October 14, 2025, preprint, §1.3 and Theorems 2.1–2.5.
5. Alireza Haqi and Shayan Oveis Gharan, *On Thin Perfect Matchings up to Polylogarithmic Factors*, [arXiv:2606.01330v2](https://arxiv.org/html/2606.01330v2), revised July 1, 2026, preprint, Lemma 1.2 and Theorems 1.3–1.4.

## Status review

Open in cited literature; no later resolution located as of 2026-09-18. The July 2026 publication [1] explicitly retains the strong conjecture. The general bound in [2, Corollary 1.8] has a numerator polynomial in $\log\log |V|$, so it does not give the required absolute constant. Spectral thinness imposes inequalities for all real vectors and is stronger than the cut condition here; spectral counterexamples do not refute this statement.

Theorem 1 of [1] finds one tree crossing each cut of size less than $41k/40$ in at most $88$ edges. Its Theorem 2 gives $66/k$ thinness for a prescribed laminar family, whose shores are pairwise nested or disjoint. Neither result controls all cuts simultaneously. The example in §1.1 defeats a particular laminar-selection strategy, not the conjecture.

The certification results [4] restrict the cuts under examination or allow a different tree for each cut. The verification-hardness claim [3] concerns a supplied tree and does not disprove existence. The matching counterexample [5] uses a fractional perfect-matching model with degree-one constraints, a different feasible class from connected spanning trees.

The [evidence record](../research/expansion-2026-09/candidates/strong-thin-tree.json) documents source versions, exact resolution searches, scope comparisons and duplicate checks. The research review examines full relevant statements and model assumptions; it does not certify the cited technical proofs.

The September 17, 2026 check covered named and mathematical formulations, author pages, current and preceding years, unrestricted resolution searches, versions, corrections and withdrawals. A35 was a separated adversarial self-pass by the same assistant. The forthcoming beyond-laminar title was rechecked on September 18; no manuscript or theorem was linked.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 4 audit](../research/expansion-2026-09/batch-04-review.md). No matching later resolution was located.
