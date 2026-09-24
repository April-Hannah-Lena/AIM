# 500. Constant-gap NP-hardness of densest k-subgraph

**Area:** Network optimization and approximation complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-09-23

## Problem statement

Let $G=(V,E)$ be a finite simple undirected unweighted graph, given explicitly, and let $n=|V|$. For an integer $2\leq k\leq n$, define

$$
\mathop{\mathrm{OPT}}\nolimits_k(G)=
\max_{\substack{S\subseteq V\\ |S|=k}} |E(G[S])|,
$$

where $G[S]$ is the subgraph induced by $S$. The input also includes an integer $1\leq \ell\leq \binom{k}{2}$.

**Does there exist an absolute rational constant $\lambda>1$ for which it is NP-hard to distinguish**

$$
\mathop{\mathrm{OPT}}\nolimits_k(G)\geq \ell
\qquad\text{from}\qquad
\mathop{\mathrm{OPT}}\nolimits_k(G)<\frac{\ell}{\lambda}\,?
$$

Here NP-hardness means a deterministic polynomial-time many-one reduction: one map must take every Boolean formula in 3-conjunctive normal form to an instance $(G,k,\ell)$, mapping satisfiable formulas to the first case and unsatisfiable formulas to the second. Its output size must be polynomial in the formula's length. The factor $\lambda$ is fixed independently of all input parameters; $k$ can grow with the input. Instances between the thresholds need not receive any prescribed answer.

The target is an unconditional reduction. If such a reduction exists, then $\mathsf P\ne\mathsf{NP}$ would rule out a deterministic polynomial-time algorithm that always returns a $k$-vertex set with at least $\mathop{\mathrm{OPT}}\nolimits_k(G)/\lambda$ edges. No Exponential Time Hypothesis, planted-clique assumption or other additional hardness conjecture is part of the requested reduction.

This is the constant-gap question stated in [1, §1], using its Definition 1. Allowing a real constant would be equivalent: a slightly smaller rational factor preserves a hardness gap. Since the vertex count is exactly $k$, dividing the objective by $k$ or by $\binom{k}{2}$ does not change approximation ratios. The at-least-$k$ density problem, which permits the denominator to vary with the selected set, is a different optimization problem.

## Application

A fixed vertex budget models selecting a prescribed number of entities while retaining as many interactions among them as possible. It gives a size-controlled version of dense community selection in a network; the survey [5, §§3.1.1, 7] explains the broader graph-mining setting. A positive answer would establish a worst-case limit on uniformly reliable approximation guarantees using the standard $\mathsf P\ne\mathsf{NP}$ assumption. It would not imply that every observed network is difficult or that useful heuristics fail on structured data.

## References

1. Bundit Laekhanukit, Pasin Manurangsi and Ohad Trabelsi, *A Note on Approximability of Densest At-Least-k-Subgraph*, [arXiv:2605.25464v1](https://arxiv.org/html/2605.25464v1), May 25, 2026; cited preprint. §1, Definition 1 and Theorems 2, 5, 7.
2. Chris Jones, Aaron Potechin, Goutham Rajendran and Jeff Xu, *Sum-of-Squares Lower Bounds for Densest k-Subgraph*, STOC 2023, DOI 10.1145/3564246.3585221. [Conference text](https://par.nsf.gov/servlets/purl/10483143); [full preprint, arXiv:2303.17506v1](https://arxiv.org/html/2303.17506v1), March 30, 2023. Preprint §1.1, Theorem 1.1 and Corollary 1.2; §1.4, “Lower bounds for Densest k-Subgraph.”
3. Pasin Manurangsi, *Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph*, STOC 2017; [author version, arXiv:1611.05991v2](https://arxiv.org/html/1611.05991v2), April 10, 2017. §1.1, Theorems 1–2 and the discussion of reduction size.
4. Aditya Bhaskara, Moses Charikar, Eden Chlamtac, Uriel Feige and Aravindan Vijayaraghavan, *Detecting High Log-Densities—an $O(n^{1/4})$ Approximation for Densest k-Subgraph*, STOC 2010, 201–210. [Author manuscript](https://users.cs.northwestern.edu/~aravindv/DkS.pdf). §1.1, Theorem 1.2 and the approximation/runtime discussion following Theorem 4.5.
5. Tommaso Lanciano, Atsushi Miyauchi, Adriano Fazzone and Francesco Bonchi, *A Survey on the Densest Subgraph Problem and Its Variants*, accepted to ACM Computing Surveys, DOI 10.1145/3653298; [cited author version, arXiv:2303.14467v2](https://arxiv.org/html/2303.14467v2), April 18, 2024. §§3.1.1, 7 and 8.
6. Shih-Chia Chang, Li-Hsuan Chen, Sun-Yuan Hsieh, Ling-Ju Hung, Shih-Shun Kao and Ralf Klasing, *On the Hardness and Approximation of the Densest k-Subgraph Problem in Parameterized Metric Graphs*, Acta Informatica 63, article 2 (2026), DOI 10.1007/s00236-025-00518-7. [Author manuscript in HAL](https://hal.science/hal-05747494/document), deposited September 11, 2026. §2, Theorems 1–3 and Lemma 1.
7. Qiheng Lu, Nicholas D. Sidiropoulos and Aritra Konar, *The Vertex-Attribute-Constrained Densest k-Subgraph Problem*, [arXiv:2508.06655v1](https://arxiv.org/html/2508.06655v1), August 8, 2025; cited preprint. §§2–4.1, Theorems 1–4, Corollaries 1–2 and Algorithm 2.
8. Julia Chuzhoy, Mina Dalirrooyfard, Vadim Grinberg and Zihan Tan, *A New Conjecture on Hardness of 2-CSP's with Implications to Hardness of Densest k-Subgraph and Other Problems*, ITCS 2023, LIPIcs 251, 38:1–38:23, DOI 10.4230/LIPIcs.ITCS.2023.38. [Published paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.38/LIPIcs.ITCS.2023.38.pdf). Introduction; §3, Conjecture 3 and Theorems 4–5.

## Status review

**Integration review (2026-09-23):** The September 19 source audit was refreshed with problem-specific web searches and searches scoped to arXiv, Zenodo, GitHub and Palomar. No matching full-scope solution announcement was located. Search coverage is limited by indexing and access; this is not a proof of openness. See the [integration record](../research/integration-2026-09-23.md).

Open in cited literature; no later resolution located as of 2026-09-19. The May 2026 paper [1] explicitly retains constant-factor NP-hardness as unresolved. Independently authored assessments appear in [2, §1.4] and [8, introduction]. These are dated literature assessments, not a certificate excluding an unindexed resolution.

Exact optimization is NP-hard, but the direct clique test only separates $\binom{k}{2}$ edges from at most $\binom{k}{2}-1$; its relative gap tends to zero. The algorithm in [4] attains an $O(n^{1/4+\varepsilon})$ approximation in time $n^{O(1/\varepsilon)}$ for fixed $\varepsilon>0$. That guarantee does not yield a constant factor. The exact exponent $1/4$ in the title must not be read as a polynomial-time guarantee at $\varepsilon=0$.

Theorems 1–2 of [3] give much larger inapproximability gaps under ETH or Gap-ETH. Their reduction-size regime does not supply the polynomial-time reduction required here. Theorem 4 of [8] assumes its separate 2-CSP hardness conjecture. The unconditional sum-of-squares results in [2] instead rule out particular relaxation methods; they do not establish NP-hardness for the promise above.

The January 2026 metric-graph paper [6] separates exact NP-hardness in Theorem 1 from approximation lower bounds in Theorems 2–3, which assume planted-clique hypotheses. The attribute-constrained result [7, Theorem 1] transfers hardness from ordinary densest k-subgraph to its generalization. Its tight continuous relaxation and convergence to a stationary point do not give a global constant-factor guarantee. Finally, the at-least-$k$ approximation results in [1] assume stronger densest-subgraph hardness hypotheses, while its unconditional Theorem 7 concerns exact parameterized complexity.

The September 19 searches covered names and aliases, gap promises, fixed-factor algorithms, proof and refutation terms, current and preceding years, unrestricted dates, author pages, versions, corrections and withdrawals. The [evidence ledger](../research/expansion-2026-09/candidates/densest-k-subgraph-constant-gap-hardness.json) records the theorem comparisons and additional semimetric-diversity check. The HAL manuscript supplied the full relevant metric-graph text after publisher access failed. The later journal text of [1] and TMLR version of [7] were not retrieved in full; all locators above refer to the specified accessible versions.

The [planted-clique problem](295-planted-clique.md) asks for average-case detection hardness in a random graph model. The [Unique Games Conjecture](296-unique-games.md) concerns permutation constraints. The [prescribed-machine scheduling conjecture](342-unit-job-unique-machine-hardness.md) asks for a growing approximation gap for a different objective. None has the worst-case graph-selection assertion above.

A separated adversarial self-pass passed on September 19, 2026. It also traced abbreviated no-PTAS claims to Khot's stronger complexity assumption, stated explicitly in [8, pp. 38:2–38:3]. No independent agent or human review is claimed.
