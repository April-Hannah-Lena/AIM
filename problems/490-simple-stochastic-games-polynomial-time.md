# 490. Polynomial-time solution of simple stochastic games

**Area:** Stochastic control, formal verification and algorithmic game theory

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-23

## Problem statement

Consider a finite directed simple graph $`G=(V,E)`$ with a partition

```math
V=V_{\max}\sqcup V_{\min}\sqcup V_{\mathrm{rand}}\sqcup\{0,1\}.
```

The vertices $`0`$ and $`1`$ are sinks. Every other vertex has exactly two outgoing edges, and every vertex has a directed path to at least one sink. A nonsink vertex $`o`$ is the starting state.

A token moves along the edges. At a vertex in $`V_{\max}`$, player Max chooses its next edge; at a vertex in $`V_{\min}`$, player Min chooses. At a vertex in $`V_{\mathrm{rand}}`$, an independent fair coin selects one of the two outgoing edges. The players observe the current state and the preceding play. Max receives payoff one if the token eventually reaches sink $`1`$, and zero otherwise, including when play continues forever.

A pure positional strategy selects one outgoing edge at every vertex controlled by that player. For strategies $`\sigma`$ of Max and $`\tau`$ of Min, let $`\mathbb P_o^{\sigma,\tau}`$ denote the law of the resulting Markov chain, with the sinks treated as absorbing. Define

```math
v(o)=\max_\sigma\min_\tau
\mathbb P_o^{\sigma,\tau}
\bigl(\text{the token eventually reaches }1\bigr).
```

Optimal pure positional strategies exist, so allowing strategies with memory or randomized choices does not change this value.

**Does a deterministic polynomial-time algorithm decide whether $`v(o)>1/2`$ for every such game?** More precisely, if $`L`$ is the bit length of the explicit adjacency-list encoding, vertex types and starting state, seek one algorithm and constants $`C,c>0`$, independent of the input, which always return the correct answer within $`C(L+1)^c`$ steps.

The equality case $`v(o)=1/2`$ requires a negative answer. All three vertex counts can grow. The graph-path assumption does not guarantee eventual absorption under every pair of strategies; no such stopping promise is imposed. This is the binary reachability decision formulation in [1, §2.2], counted as one problem.

## Application

The graph can represent a finite system with controlled decisions, adversarial environmental choices and random transitions. Its value measures the best guaranteed probability of reaching a specified goal despite the adversary. Computing this threshold is a basic capability in probabilistic verification and controller synthesis [2, 6]. A polynomial algorithm would give a worst-case efficiency guarantee for explicitly represented models; the number of states needed to encode a physical system could still be large.

## References

1. Bernd Gärtner, Sebastian Haslebacher and Hung P. Hoang, *Sinks and Ladders: ARRIVAL and SSG with Two Vertices per Level*, FUN 2026, LIPIcs 366, 19:1–19:16, published May 15, 2026. [Publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2026.19); [full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol366-fun2026/html/LIPIcs.FUN.2026.19/LIPIcs.FUN.2026.19.html). Introduction, §§2–2.2 and Theorem 2.
2. Hugo Gimbert and Florian Horn, *Solving Simple Stochastic Games with Few Random Vertices*, Logical Methods in Computer Science 5(2:9) (2009), 1–17. [Published PDF](https://lmcs.episciences.org/1119/pdf). §§1.1–1.3, Theorem 1.1, Theorem 3.4 and conclusion.
3. Xi Chen, Yuhao Li and Mihalis Yannakakis, *The Mystery Deepens: On the Query Complexity of Tarski Fixed Points*, [arXiv:2604.00268v1](https://arxiv.org/html/2604.00268v1), March 31, 2026; preprint. §1, Theorems 1–2 and Corollary 1.
4. Andrei Feodorov and Sebastian Haslebacher, *Faster Approximate Fixed Points of $`\ell_\infty`$-Contractions*, [arXiv:2604.01006v1](https://arxiv.org/html/2604.01006v1), April 1, 2026; preprint. Theorems 1.1–1.2 and §1, “Implications for Condon’s and Shapley’s Stochastic Games.”
5. Manuel Bodirsky, Georg Loho and Mateusz Skomra, *Reducing Stochastic Games to Semidefinite Program Feasibility*, [arXiv:2411.09646v2](https://arxiv.org/html/2411.09646v2), December 2, 2025; expanded preprint. §§1–2.2, Definition 1, Corollary 11 and Theorem 12. The ICALP 2025 conference version has the title *Reducing Stochastic Games to Semidefinite Programming*, LIPIcs 334, 145:1–145:15.
6. Edon Kelmendi, Julia Krämer, Jan Křetínský and Maximilian Weininger, *Value Iteration for Simple Stochastic Games: Stopping Criterion and Learning Algorithm*, CAV 2018, 623–642; [accessible author version, arXiv:1804.04901v1](https://arxiv.org/html/1804.04901v1), April 13, 2018. §§1–2, Algorithm 1 and §4.3, Theorem 4.2.
7. Lei Huang and Toniann Pitassi, *Automatizability and Simple Stochastic Games*, ICALP 2011, Part I, LNCS 6755, 605–617; [author PDF](https://www.cs.utoronto.ca/~toni/Papers/automatizability.pdf). §§1–2 and §3, Theorem 5 and Corollary 1.

## Status review

**Known cases:** Polynomial algorithms exist when the number of random vertices is fixed, and for the stopping ladder class; see references 1–2.

**Remaining target:** One deterministic polynomial bound for the exact strict-threshold decision problem when all vertex counts grow, without a stopping or ladder promise.

**Integration review (2026-09-23):** The September 19 source audit was refreshed with problem-specific web searches and searches scoped to arXiv, Zenodo, GitHub and Palomar. No matching full-scope solution announcement was located. Search coverage is limited by indexing and access; this is not a proof of openness. See the [integration record](../research/integration-2026-09-23.md).

The integration refresh on 2026-09-23 also checked the [September 19 information-value-free equilibrium announcement](https://arxiv.org/abs/2609.22757). Its abstract gives a hardness comparison with simple stochastic games, not a polynomial algorithm for them. The HTML full-text fetch failed, so this comparison uses the primary abstract only.

The general polynomial-time question is explicit in [2] and is independently retained in the 2026 introductions of [1] and [3]. In particular, [1] defines the strict half-threshold problem used here. These are dated assessments, not a certificate excluding an unindexed resolution.

Recent progress must be interpreted with its parameters intact. The preprint [4] gives a deterministic algorithm with running time $`L^{O(\sqrt n\log n)}`$, where $`n=|V|`$; its exponent is not a fixed constant. The fixed-dimensional Tarski query improvements in [3] likewise do not give a uniform polynomial running time when dimension varies.

The polynomial algorithm in [1, Theorem 2] assumes both stopping and a ladder structure: distance levels from the sinks have two vertices, with a possible single vertex at the last level. General inputs need not satisfy either condition. The older enumeration method in [2] has factorial dependence on the number of random vertices.

The reduction in [5] leads to **exact semidefinite feasibility**, itself not known to admit a polynomial-time algorithm; numerical approximation of an SDP is insufficient to infer one. The interval method in [6] terminates at a requested positive error tolerance but does not establish the required polynomial exact-decision bound. The algorithmic implication in [7] has an additional feasible-interpolation hypothesis.

The September 19 search covered binary and stopping games, reachability thresholds, polynomial algorithms, proofs and counterexamples, current and preceding years, unrestricted dates, original and later authors, corrections and version histories. The [evidence ledger](../research/expansion-2026-09/candidates/simple-stochastic-games-polynomial-time.json) records nine source audits and the full relevant scope comparisons. Condon’s historical original is accessed through explicit scholarly restatements; its proof is not claimed to have been checked. The related 2022 journal extension of [6] was not retrieved in full, so the cited theorem locator refers to the accessible 2018 version.

The [simplex pivot-rule problem](093-strongly-polynomial-simplex.md) asks for a stronger arithmetic guarantee within a specified LP algorithm family. The [continuous Skolem problem](263-continuous-skolem-decidability.md) concerns decidability for deterministic continuous-time dynamics. Neither has the finite stochastic-game assertion above.

A separated adversarial self-pass passed on September 19, 2026. No independent agent or human review is claimed.
