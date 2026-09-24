# Optimal asymptotic competitiveness for online bin packing

**Area:** Online optimization and resource allocation

**Status:** Accepted; integrated as entry 318

**Last checked:** 2026-09-17

## Problem statement

An input is any finite sequence $`I=(s_1,\ldots,s_n)`$ of rational item sizes $`0<s_i\le1`$. Items arrive one at a time, and the length $`n`$ is not announced. An algorithm must assign each arriving item to a bin before seeing the next item. Every bin has capacity $`1`$: the sum of its assigned sizes must never exceed $`1`$. Assignments are irrevocable, and arbitrarily many bins are available.

For a deterministic online algorithm $`A`$, let $`A(I)`$ be the number of nonempty bins it uses. Let $`\mathop{\mathrm{OPT}}\nolimits(I)`$ be the minimum number of bins achievable with the entire sequence known in advance. Define

```math
R_\infty(A)=\lim_{N\to\infty}
\sup_{\substack{I:\ \mathop{\mathrm{OPT}}\nolimits(I)\ge N}}
\frac{A(I)}{\mathop{\mathrm{OPT}}\nolimits(I)},
\qquad
R_*=\inf_A R_\infty(A).
```

Determine the exact value of $`R_*`$. The infimum ranges over single deterministic online algorithms with no advice, predictions or advance information about the input, and with no restriction on their computation time or number of available bins. This is the classical adversarial-input problem; no probability distribution or random arrival order is imposed.

The lower-bound and algorithmic results cited below give

```math
\frac{1363-\sqrt{1387369}}{120}
\ \le R_*\ \le 1.57828956,
```

with the lower endpoint approximately $`1.5427809065`$. The task is to determine the optimum over all algorithms, rather than the performance of a particular heuristic. The definition does not assume that an algorithm attains the infimum. It also differs from the absolute competitive ratio, which takes a supremum over inputs of every size without the large-$`\mathop{\mathrm{OPT}}\nolimits`$ limit.

## Applied significance

The model isolates the capacity loss caused by irreversible decisions when future demand is unknown. Examples include allocating arriving data to storage blocks or cutting successive requested lengths from identical stock, under the model's single capacity constraint and inability to rearrange earlier assignments. The ratio measures the extra number of resources required relative to a planner who knows all requests. Its asymptotic form separates persistent inefficiency on large workloads from a fixed startup cost. Resolving the gap would establish the best possible worst-case guarantee for this basic online allocation model; it would not by itself account for multidimensional geometry or other operational constraints.

## References

1. János Balogh, József Békési, György Dósa, Leah Epstein and Asaf Levin, *A New and Improved Algorithm for Online Bin Packing*, ESA 2018, LIPIcs 112, 5:1–5:14. [Published paper](https://doi.org/10.4230/LIPIcs.ESA.2018.5), §1; [full manuscript](https://arxiv.org/abs/1707.01728), v1 (2017), §1 and Appendix B, Theorem 25, p. 38.
2. The same five authors, *A New Lower Bound for Classic Online Bin Packing*, Algorithmica 83(7) (2021), 2047–2062, [DOI](https://doi.org/10.1007/s00453-021-00818-7). [Author manuscript](https://arxiv.org/abs/1807.05554), v1 (2018), §1 and Theorem 9, p. 12.
3. Matthias Gehnen and Andreas Usdenski, *Online Bin Packing with Item Size Estimates*, [arXiv:2505.09321](https://arxiv.org/abs/2505.09321), v1 (2025), §1, Definitions 2–4 and Theorems 7 and 12. Independent current bounds and the distinction between ordinary online input and advance estimates.
4. Julien Herrmann and Guillaume Pallez, *An In-depth Study of LLM Contributions to the Bin Packing Problem*, [arXiv:2510.27353](https://arxiv.org/abs/2510.27353), v2 (June 17, 2026), §4 opening, p. 12; accepted for publication in ACM Transactions on Evolutionary Learning and Optimization according to the arXiv record. Identifies the remaining canonical question and distinguishes distribution-specific heuristic experiments.
5. János Balogh, József Békési, György Dósa, Jiří Sgall and Rob van Stee, *The optimal absolute ratio for online bin packing*, SODA 2015, 1425–1438. [Author manuscript](https://iuuk.mff.cuni.cz/~sgall/ps/below.pdf), §1, equations (1.1)–(1.2), §2 and Theorem 6.15. The solved absolute ratio is a different objective.
6. Leah Epstein and Asaf Levin, *Lower Bounds for Several Standard Bin Packing Algorithms in the Random Order Model*, WADS 2025, LIPIcs 349, 26:1–26:15. [Published paper](https://doi.org/10.4230/LIPIcs.WADS.2025.26), §1, pp. 26:1–26:2. Retains the classical worst-case interval while studying random arrival order.

## Status review

The 2025 Gehnen–Usdenski introduction reports the same unresolved classical lower/upper gap; Herrmann–Pallez's June 2026 revision explicitly distinguishes the canonical open problem from improvements to empirical heuristics on specified input distributions. Epstein–Levin's WADS 2025 paper also retains the interval. The bounds above come from full theorem statements in the original manuscripts. Their complete proofs and computer-assisted upper-bound calculations were not independently certified.

Several nearby results require care. The optimal absolute ratio $`5/3`$ does not determine $`R_*`$. Ayyadevara–Dabas–Khan–Sreenivas, ICALP 2022, Theorem 1 and Corollary 2, give near-optimal expected guarantees for independent identically distributed inputs. Gehnen–Usdenski's $`3/2`$ guarantee requires advance estimates of every item. Fekete and coauthors evaluate the best of several parallel packings, rather than one irrevocable packing. Chen–Ye–Zhang's competitive scheme approaches an optimal ratio in its finite integer-size model without determining the exact unrestricted constant. The resolved cardinality-constrained problem imposes an additional item-count limit per bin. These statements do not close the classical gap.

Searches on September 17, 2026 covered asymptotic/absolute performance, classic online packing, current bounds, original and later authors, proof and counterexample claims, corrections and withdrawals, 2025–2026 and unrestricted dates. Full scope comparisons, independent corroboration and access limits are recorded in the [candidate ledger](../candidates/online-bin-packing-optimal-ratio.json). The dated review is not a certificate that no unindexed result exists.

This question minimizes the number of fixed-capacity bins. Unrelated-machine and precedence scheduling likewise have different objectives and input models. This is one canonical competitive-ratio question, without separate entries for algorithms, size classes or numerical improvements.

Integrated as [entry 318](../../../problems/318-online-bin-packing-optimal-ratio.md) after the September 17, 2026 batch refresh.
