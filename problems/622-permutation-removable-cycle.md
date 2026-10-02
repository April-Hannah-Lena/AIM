# 622. Removable cycles in cycle permutation graphs

**Area:** Computational graph theory and graph connectivity

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-24

## Problem statement

A *cycle permutation graph* is a finite simple cubic graph admitting a spanning 2-factor $`F`$ consisting of two chordless cycles. Given such an $`F`$, a cycle $`C`$ of $`G`$ is *removable relative to $`F`$* if the spanning graph

```math
G-\bigl(E(C)\cap E(F)\bigr)
```

is 2-connected: it is connected and remains connected after deletion of any one vertex. Only the indicated edges are deleted; every vertex is retained.

Prove or disprove the existential formulation of Goddyn's conjecture in [1, Conjecture 3]: every cycle permutation graph $`G`$ not isomorphic to the Petersen graph admits a permutation 2-factor $`F`$ and a cycle $`C`$ removable relative to $`F`$.

Both $`F`$ and $`C`$ may be chosen. The assertion here is $`\forall G\ne P\;\exists F\;\exists C`$, without requiring the same conclusion for every prescribed permutation 2-factor.

## Application

Removable cycles permit reductions that preserve connectivity while retaining a distinguished spanning structure. The conjecture gives a structural target for exhaustive generation and cycle-search algorithms in cubic graphs.

## References

1. J. Goedgebeur, J. Renders and S. Van Overberghe, [Generation of cycle permutation graphs and permutation snarks](https://doi.org/10.1090/mcom/4247), *Mathematics of Computation*, electronically published 13 August 2026. Section 5, Conjecture 3 and Observation 2; [arXiv:2411.12606v4](https://arxiv.org/abs/2411.12606v4).
2. L. A. Goddyn, J. van den Heuvel and S. McGuinness, [Removable circuits in multigraphs](https://doi.org/10.1006/jctb.1997.1775), *Journal of Combinatorial Theory, Series B* **71** (1997), 130–143. Conjecture 4.4 gives the related, stronger formulation with a prescribed permutation factor.

## Status review

**Known cases:** The conclusion holds for 3-edge-colourable cycle permutation graphs and for those without a Petersen minor. Observation 2 of [1] excludes further exceptions among permutation snarks on at most 48 vertices; together with the colourable case, this verifies the stated existential version through that order.

**Remaining target:** Prove existence of a suitable pair $`(F,C)`$ for every larger graph other than the Petersen graph, or exhibit a graph for which every permutation factor fails. The finite computation does not prove the stronger prescribed-factor statement in [2].

The August 2026 journal article still states the conjecture as open. Its public filter searches across permutation factors and accepts a graph once it finds a removable cycle. Current literature, arXiv, public GitHub, native Zenodo and Palomar checks found no resolution or matching announcement. The disproof of a different matroid conjecture from [2] does not settle this graph problem. No equivalent catalogue problem was found.
