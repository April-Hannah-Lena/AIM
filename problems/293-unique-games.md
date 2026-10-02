# 293. The Unique Games Conjecture

**Area:** Constraint satisfaction and approximation algorithms

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

A unique game consists of a finite bipartite graph $`G=(L\sqcup R,E)`$, with $`E\ne\varnothing`$, an alphabet $`[r]=\{1,\ldots,r\}`$ and a permutation $`\pi_e:[r]\to[r]`$ for each edge $`e=(u,v)`$ directed from $`L`$ to $`R`$. A labeling $`\ell:L\sqcup R\to[r]`$ satisfies $`e`$ when $`\ell(v)=\pi_e(\ell(u))`$. Define the classical value

```math
\mathop{\mathrm{val}}\nolimits(G,\pi)=
\max_{\ell}\frac{1}{|E|}\sum_{e=(u,v)\in E}
\mathbf 1\{\ell(v)=\pi_e(\ell(u))\}.
```

Is it true that, for every $`0<\varepsilon<1/2`$, there exists an integer $`r=r(\varepsilon)`$ such that it is NP-hard to distinguish instances satisfying

```math
\mathop{\mathrm{val}}\nolimits(G,\pi)\ge 1-\varepsilon
\qquad\text{from those satisfying}\qquad
\mathop{\mathrm{val}}\nolimits(G,\pi)\le\varepsilon?
```

The alphabet is fixed for each $`\varepsilon`$, independently of the number of vertices. This is a promise problem: behavior on intermediate values is unrestricted. The value uses ordinary classical labelings.

## Application

The conjecture is a proposed foundation for sharp limits on approximation algorithms for discrete optimization. For example, Heilman's 2026 Theorem 1.4 uses it to derive sharp approximation hardness for MAX-3-CUT, whose objective is to divide a graph into three classes while maximizing the number of edges between classes. Such hardness consequences remain conditional on this conjecture.

## References

1. Y. Fei, D. Minzer and S. Wang, [*On the Hardness of 4-to-1 Games with Perfect Completeness*](https://eccc.weizmann.ac.il/report/2026/179/download/), ECCC TR26-179, September 14, 2026; Definitions 1.1 and 1.3, Conjecture 1.4, Theorem 1.6 and the discussion in §1.1, printed pp. 4–6.
2. J. Kempe, O. Regev and B. Toner, [*Unique Games with Entangled Provers are Easy*](https://arxiv.org/pdf/0710.0655v3), arXiv:0710.0655v3, October 3, 2009; Conjecture 1.2, p. 2, and Theorem 1.3, p. 5.
3. S. Heilman, [*Sharp Hardness for MAX-3-CUT and Quantum MAX-CUT*](https://arxiv.org/pdf/2608.00333v1), arXiv:2608.00333v1, submitted July 31, 2026; §1.1 and Theorem 1.4. The served manuscript bears August 24, 2026.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 17, 2026 review covered Unique Games and unique-label-cover aliases, permutation constraints, proof and refutation claims, 2025–2026 papers, unrestricted searches and version/correction records. Fei–Minzer–Wang still state the exact conjecture in their September 14 report. Their new perfect-completeness hardness theorem has four-to-one constraints. The one-to-one condition required here is different. Their discussion of existing hardness with completeness $`1/2`$ also leaves the almost-satisfiable regime unresolved.

Kempe–Regev–Toner's algorithm concerns entangled game value. A small classical optimum need not imply a small entangled optimum, so it does not decide the displayed classical promise problem. Heilman's hardness theorem assumes Unique Games rather than proving it.

The review also inspected two 2026 vertex-cover manuscripts by Frank Vega. The Hallelujah manuscript's displayed guarantee is strictly below $`2\mathop{\mathrm{OPT}}\nolimits`$ for each finite graph; it supplies no uniform constant improvement below factor two. The Salvador manuscript explicitly conjectures its proposed $`7/4`$ upper bound. Neither displayed result supplies a contradiction to Unique Games. These are scope assessments, not certifications of their proofs; the accessible author versions and publisher-access limitation are documented in the [evidence record](../research/expansion-2026-09/candidates/unique-games.json).

The record includes duplicate screening and a separate adversarial self-review. The classical constraint problem differs from the catalogue's quantum PCP and traveling-salesperson integrality-gap questions.
