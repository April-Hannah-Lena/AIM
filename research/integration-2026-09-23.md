# Integration and maintenance — 23 September 2026

At this historical checkpoint, seven previously accepted research drafts were integrated into the local catalogue, which then had 501 active entries. Previously removed problems remain excluded. Problem references below use the current consecutive numbering. No commit or remote publication was performed by this maintenance pass.

## Admission and scope

All seven full drafts and their stated references, scope exclusions and prior review conclusions were read. The existing September 19 source audits were supplemented by searches on September 23 using names, mathematical formulations, proof/counterexample terms and a second pass scoped to arXiv, Zenodo, GitHub and Palomar. No matching full-scope announcement was located. Searches are not exhaustive, registry coverage is search-index based, and no proof or formalization was independently certified. The refresh does not revalidate every bibliography item. The [search log](integration-2026-09-23-searches.json) records the queries and scope.

| ID | Canonical problem | Catalogue status |
| --- | --- | --- |
| 494 | [The sharp number of directions illuminating a convex body](../problems/486-hadwiger-boltyanski-illumination.md) | Partially resolved |
| 495 | [The GNRS conjecture for minor-free network flow](../problems/487-gnrs-minor-free-flow-cut.md) | Partially resolved |
| 496 | [The Fourier entropy–influence conjecture](../problems/488-fourier-entropy-influence.md) | Partially resolved |
| 497 | [Global attraction in D-stable Lotka–Volterra systems](resolved/650-lotka-volterra-d-stable-global-attraction.md) | Partially resolved |
| 498 | [Deterministic parallel perfect matching in general graphs](../problems/489-general-graph-perfect-matching-nc.md) | Partially resolved |
| 499 | [Polynomial-time solution of simple stochastic games](../problems/490-simple-stochastic-games-polynomial-time.md) | Partially resolved |
| 500 | [Constant-gap NP-hardness of densest k-subgraph](../problems/491-densest-k-subgraph-constant-gap-hardness.md) | Open |

Six entries are marked Partial because the cited literature proves cases within their displayed targets. Each has explicit Known cases and Remaining target notes. The densest-k-subgraph entry stays Open: exact NP-hardness, stronger complexity assumptions and restricted-method lower bounds do not establish its unconditional constant-gap reduction.

## New leads compared with the targets

- **494:** Gorodzha, [arXiv:2609.23913v1](https://arxiv.org/html/2609.23913v1), Theorems 1–2: fractional illumination at the conjectured bound and integral illumination with an additional factor of order dimension times log dimension. Neither establishes the full integral statement or its equality classification. Primary theorem statements inspected; proof not certified.
- **496:** Potapov, [arXiv:2609.21563v1](https://arxiv.org/html/2609.21563v1), Theorems 1–2: partially bent and plateaued Boolean functions only. Primary definitions and theorem statements inspected; proof not certified. The later version listed by the abstract page was not used for theorem locators.
- **499:** [arXiv:2609.22757](https://arxiv.org/abs/2609.22757) compares equilibrium computation with simple stochastic games through hardness reductions. It does not announce a polynomial solution of the games. The HTML fetch failed; only the primary abstract supports this exclusion.
- **495:** Tree, treewidth and constrained-demand embedding results preserve restrictions absent from general GNRS; no later general resolution located.
- **497:** The Hong–Pego D-stability question remains distinct from diagonal Lyapunov sufficient conditions and counterexamples for unrestricted polynomial vector fields; no matching later claim located.
- **498:** Catalytic-space matching and bipartite NC results do not supply deterministic NC search for all general graphs; no matching later claim located.
- **500:** The at-least-k-subgraph reduction and ETH/Gap-ETH or planted-clique lower bounds do not prove the stated unconditional polynomial reduction.

## Other maintenance

Problem 290 now correctly describes entry 195 as a three-dimensional lattice polymer. Its literature date is unchanged because this is a wording correction. The research programme queue is synchronized to current active and retained metadata, with old programme statuses preserved and newly discovered entries marked unstarted. The current Pólya research status explicitly separates the conditional lemma, missing existence step, algebra checks and full all-index target. Historical attempt/review records are preserved.

## Validation

- `python scripts/catalogue.py --check`: passed for 501 unique active entries, metadata, required sections, math delimiters, local links and generated catalogue freshness.
- Queue/state cross-check: 501 active files match the queue; 405 new queue entries, 96 preserved active programme statuses, and the six owner-removed IDs absent. The current campaign, attempt/review counters and historical attempt/review files are unchanged. Legacy discovery dates remain unknown and are distinguished from their September 8 snapshot date.
- Existing fold-overlap Fraction verifier: all 13 finite algebra checks passed; no analytic verification or existence proof is implied.
- `git diff --check`: passed.
- `python -m unittest scripts/test_catalogue.py`: all 39 tests passed. The retirement fixture now rebases sibling links when moving a problem page into the archive; the newly integrated highest-ID entry exposed the fixture issue.
