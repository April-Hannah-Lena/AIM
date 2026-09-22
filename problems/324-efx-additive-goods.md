# 324. Complete EFX allocation of indivisible goods with additive values

**Area:** Fair division and resource allocation

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-17

## Problem statement

Let $N=\{1,\ldots,n\}$ be a finite set of agents, with $n\ge1$, and let $M$ be a finite set of indivisible goods. Agent $i$ assigns a nonnegative real value $v_{ig}$ to each good $g$. The value of a bundle $S\subseteq M$ is additive:

$$
v_i(S)=\sum_{g\in S}v_{ig}.
$$

A complete allocation is a partition $(A_1,\ldots,A_n)$ of $M$; empty bundles are allowed. Does every such valuation profile admit a complete allocation satisfying

$$
v_i(A_i)\ge v_i(A_j\setminus\{g\})
\qquad\text{for all }i,j\in N\text{ and every }g\in A_j?
$$

Thus any envy disappears after the hypothetical removal of any single good from the envied bundle, including a good valued at zero by the comparing agent. This convention is sometimes called $\mathrm{EFX}_0$. Its universal existence question is equivalent to the convention that tests only positively valued goods, by perturbing values to be positive and passing to a limit over the finite set of allocations. All goods must actually be assigned; the removal in the inequality is only a comparison. No efficiency, welfare-maximization, incentive or running-time condition is imposed.

## Application

When allocating indivisible assets, equipment or donated items, exact envy-freeness can fail even with two recipients and one desired object. EFX asks whether a strong relaxation is always feasible when each recipient's values add across items. A positive answer would justify this fairness requirement for every instance of the additive model; a counterexample would identify a limit that no allocation method can overcome. The question concerns comparisons between recipients' bundles, whereas [entry 290](290-general-santa-claus.md) asks for an efficient approximation to the largest possible minimum utility.

## References

1. Ioannis Caragiannis, David Kurokawa, Hervé Moulin, Ariel D. Procaccia, Nisarg Shah and Junxing Wang, *The Unreasonable Fairness of Maximum Nash Welfare*, EC 2016, pp. 305–322, [author manuscript](https://eprints.gla.ac.uk/123283/1/123283.pdf), §4.2, Definition 4.4 and the following open question. The original definition tests positively valued goods.
2. Simina Brânzei, *Computing Envy-Free up to Any Good (EFX) Allocations via Local Search*, [arXiv:2510.05429v1](https://arxiv.org/html/2510.05429v1), October 6, 2025, §§1–2 and §5, Proposition 1. Independent formulation; experiments and a theorem for identical positive values.
3. Eyad Alkassar, Mahmoud Fouz and Kurt Mehlhorn, *Complete EFX Allocations Exist for Four Additive Agents and Up to Nine Goods*, [arXiv:2608.08590v1](https://arxiv.org/html/2608.08590v1), August 9, 2026, §1, Definition 1, Theorem 1 and footnote 1. Preprint with a finite-size existence result and the equivalence of zero-value conventions.
4. Vishwa Prakash HV, Pratik Ghosal, Prajakta Nimbhorkar and Nithin Varma, *EFX Exists for Three Types of Agents*, EC 2025; [arXiv:2410.13580v3](https://arxiv.org/html/2410.13580v3), revised May 23, 2025, §1, Theorem 1 and §3. Exact existence with at most three distinct additive valuation functions.
5. Georgios Amanatidis, Aris Filos-Ratsikas and Alkmini Sgouritsa, *Pushing the Frontier on Approximate EFX Allocations*, EC 2024; [arXiv:2406.12413v3](https://arxiv.org/html/2406.12413v3), revised July 29, 2026, §§1–2.1. General approximation status and stronger guarantees on restricted classes.
6. Wentao He and Biaoshuai Tao, *EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence*, [arXiv:2606.08872v2](https://arxiv.org/html/2606.08872v2), revised July 9, 2026, §§1–3, Definition 2 and Theorem 1. The counterexample concerns disutilities for chores; the paper explicitly retains the additive-goods question.
7. Haris Aziz, *Pairwise Maximin Share Allocations Need Not Exist*, [arXiv:2609.06282v1](https://arxiv.org/html/2609.06282v1), September 5, 2026, §1, Theorem 1 and §3. The stronger PMMS condition fails on some additive instances; the paper explicitly distinguishes this from EFX.
8. Hadi Hosseini, Payas Khurana, Shraddha Pathak and Rohit Vaish, *To EFX OR to MMS, That is the Question*, [arXiv:2608.10397v2](https://arxiv.org/html/2608.10397v2), revised September 15, 2026, Theorems 1, 3 and 4. Disjunctive fairness results with different valuation or efficiency assumptions.

## Status review

**Known cases:** Complete EFX allocations exist when there are at most three distinct additive valuation functions, including the three-agent case.

**Remaining target:** Exact complete EFX for arbitrary numbers of agents and goods with nonnegative additive valuations.

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-17. Exact existence is known with at most three distinct additive valuation functions, including the three-agent case. The August 2026 preprint establishes four agents and at most nine goods, using computer-assisted certificates; those certificates were not independently run in this review. The July 2026 revision of reference 5 reports a general factor $(\sqrt5-1)/2\approx0.618$, which multiplies the right-hand side of the EFX inequality and therefore falls short of exact EFX.

The 2026 [submodular counterexamples](https://arxiv.org/html/2605.06451v1) use nonadditive values. The additive-chore counterexample removes an item from the comparing agent's own bundle and reverses the preference inequality, so it does not establish impossibility for goods. Recent [positive results for multigraph valuations](https://arxiv.org/html/2606.18665v1) limit each good's positive values to its endpoints. The simultaneous [epistemic EFX and EFL guarantee](https://arxiv.org/html/2602.11732v2) uses, for its epistemic condition, a potentially different rearrangement of the remaining goods for each agent. It does not ensure EFX of the single actual allocation. The September PMMS counterexample concerns a stronger fairness condition; the EFX-or-MMS counterexamples require nonadditive values or an additional efficiency condition. These results, partial allocations and successful local-search experiments leave the unrestricted complete additive-goods question unresolved.

The [evidence ledger](../research/expansion-2026-09/candidates/efx-additive-goods.json) records full theorem comparisons, current versions, duplicate screening and access limits. The separated A25 adversarial self-pass passed on 2026-09-17; no independent agent or human review is claimed.

Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration. Review was a separated adversarial self-pass; no independent agent or human review is claimed.
