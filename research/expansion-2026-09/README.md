# September 2026 expansion research

The active catalogue contains 350 entries: the original 300 and fifty published additions. All five ten-entry batches (301–350) are published directly on main. [Batch 5](batch-05-review.md) was pushed as [1240ebf](https://github.com/MColbrook/AIM/commit/1240ebfbdae361901472a7d33ca0baa7073c51cb), and a separate remote-ref read verified the exact commit on September 18, 2026. No accepted drafts remain outside the catalogue. There are 50 accepted additions toward the requested 200–300, with a working target of 250: 150 more additions are needed for the minimum.

- [Progress and reading coverage](progress.json): counts, publication state and next actions.
- [Baseline inventory](baseline-inventory.json): all original statements and metadata at a602073d986b7f5ce57b1aa0db1687d1bd87761d.
- [Candidate evidence](candidates/), [actual search log](search-log.json), [source map](source-map.md), [exclusions](exclusions.md) and [discovery queue](discovery-queue.md).
- [Historical-entry status follow-ups](baseline-status-followup.md): later claims, separate from the new-entry count.
- [Batch 1 audit](batch-01-review.md), [batch 2 audit](batch-02-review.md), [batch 3 audit](batch-03-review.md) [batch 4 audit](batch-04-review.md) and [batch 5 audit](batch-05-review.md).

The original 300 pages and historical review dates are preserved. Permanent IDs are assigned centrally after admission. Research drafts and evidence records are not additional catalogue entries. Review consists of source research followed by a separated adversarial self-pass; no independent agent or human review is claimed.

The 50 accepted additions cover all twelve primary sections. Batch 4 adds decentralized rendezvous, deletion-trace inference, delayed population feedback, network backbones, nutrient-directed migration, cumulative allocation, passive rule learning, quantum query limits, ancestral-state inference and Gaussian multiple testing. Batch 5 concerns online selection, the information density of binary codes, decidability of stability under arbitrary switching, scheduling under job-specific availability constraints, microbial competition with species-specific removal, integral triangle packing–covering optimization, two-user broadcast throughput, the number of slots for arbitrary pairwise-conflict schedules exact verification of nonlinear equilibrium stability and approximation limits for scheduling jobs on prescribed machines. No further numerical-linear-algebra problems were added.

Fifty-five candidates have investigation records: 50 accepted and five held. Morrey, Yang–Mills, Gaussian multiple-access feedback and graph isomorphism have unresolved matching claims; FIFO queue feedback has a formulation/evidence hold. These have no active IDs. Discovery-only leads are not counted as investigated records.

The user authorized repository uploads and direct pushes to main. No PR is required. Current upstream and open-PR checks are recorded in the batch audit and individual refresh records.

## Stability under arbitrary switching (2026-09-18)

The [accepted control record](candidates/switched-linear-stability-decidability.json) preserves exact rational input, every initial state and switching sequence, and the strict threshold. Jungers’s Open question 1 and independently authored Ahmadi–de Klerk–Hall §5.2 supply the formulation and corroboration. The evidence compares nonstrict undecidability, conditional certificate algorithms and approximation results. The September 10 Ninite–Jungers version was checked through Theorem 4, Algorithm 1 and Remark 2. Journal full-text access limits are explicit. A44 passed after drafting; the accepted problem is integrated as entry 343.

## Availability-constrained scheduling (2026-09-18)

The [list edge-colouring record](candidates/list-edge-colouring.json) preserves arbitrary finite lists on every finite loopless multigraph. Its scheduling interpretation uses simultaneous pairs of resources. Nine primary works support the formulation and scope comparisons; A45 checked an additional September 9 distributed algorithm and the September 16 complete-graph preprint. Exact equality remains distinct from asymptotic guarantees, extra colours, common-list-intersection conditions and recolouring. The accepted problem is integrated as entry 344; special cases are not counted separately.

## Microbial competition (2026-09-18)

The [chemostat record](candidates/chemostat-unequal-removal-exclusion.json) preserves Hsu's finite-species, single-resource model with general increasing growth and arbitrary positive species removal rates. Sari–Mazenc supply independent corroboration, and Hsu's 2019 lectures retain the question. A46 checked later common-removal, perturbation and infinite-strain results at model/theorem level, including the 2025 oscillation construction. The equilibrium keeps the nutrient dilution factor. The accepted problem is integrated as entry 345; species numbers and kinetic subclasses are not counted separately.

## Triangle packing and network modification (2026-09-18)

The [Tuza record](candidates/tuza-triangle-packing-covering.json) preserves finite simple graphs, edge-disjoint triangles, edge deletion, integral optima and the exact factor two. Krivelevich's formulation and the independently authored June 2026 Bennett–Cushman–Dudek–Pérez-Giménez paper supply the core evidence. A47 checked fractional and random-graph results, dense-graph counterexamples to a stronger claim, bounded-degree claims and a September three-type split-graph extension. The latter retains a fixed eight-vertex clique. Eleven source records and ten scope comparisons are saved; no computational proof certificates were independently rerun. The draft passed research and rendering checks and was [published directly to main](https://github.com/MColbrook/AIM/commit/02e5ac183cddf5e1d4559a15394340353981baf3); the full remote commit was independently checked on September 18, 2026. It is now integrated in batch 5.

## Binary broadcast capacity (2026-09-18)

The [broadcast record](candidates/binary-skew-symmetric-broadcast.json) fixes the two binary transition matrices, independent private messages, no feedback, separate decoders and vanishing average block error. Nair's explicit open question and Dou and coauthors' independently authored account supply the core evidence. Nine source records and nine scope comparisons distinguish evaluation of an achievable region, numerical outer bounds, local tensorization and exact-capacity results for other channel classes. A48 found and checked the expanded June 2026 sum-channel theorem and a solved single-user channel sharing the BSSC acronym. Twenty-four expressions passed strict KaTeX and a full-page visual check. The accepted research draft was [published directly to main](https://github.com/MColbrook/AIM/commit/66617e03315b6184d0ec802ff7132d9cbf5bccc1) and the full remote commit independently checked on September 18, 2026. It is now integrated in batch 5.

## Continuous-time control discovery (2026-09-18)

The [Carrasco discovery audit](carrasco-discovery.md) records a July 2026 discrete-time disproof claim and the original continuous-time formulation. Their relationship and precise stability conventions remain under review. This lead is not counted among accepted drafts or formal candidate records.

## Vertex colouring and conflict schedules (2026-09-18)

The [Reed record](candidates/reed-colouring.json) passed formulation, current-status, duplicate and separated A49 self-review. It retains the integral colouring optimum and exact ceiling for every finite simple graph. The evidence includes a September revision, correction and dependency caveats, and comparisons with fractional, restricted-class and directed results. Twenty-three expressions passed strict KaTeX and a full-page visual check. The eighth accepted draft was [pushed directly to main](https://github.com/MColbrook/AIM/commit/e49b24d6fcd6fa3be767df39595fd8ca08062445) and its full remote commit independently verified. It is now integrated as entry 348 in batch 5.

## Polynomial equilibrium stability (2026-09-18)

The [accepted draft](drafts/polynomial-local-stability-decidability.md) asks for a terminating algorithm on every rational polynomial vector field, with dimension and degree part of the input. Stability and attraction are separately defined. The [evidence record](candidates/polynomial-local-stability-decidability.json) contains nine scholarly source records and ten scope comparisons. A50 checked exponential stability, certificate hierarchies, discrete-time undecidability, finite-time blow-up, bounded tolerance decisions and conditional transformations. Nineteen expressions passed strict KaTeX and final visual inspection; bibliography transport limits are recorded. This ninth accepted draft was [pushed directly to main](https://github.com/MColbrook/AIM/commit/e2a291c4328224f406e29f1b9811f744faeb1040) and the exact remote commit independently verified. It is now integrated in batch 5.

## Prescribed-machine scheduling and batch 5 (2026-09-18)

The [scheduling evidence record](candidates/unit-job-unique-machine-hardness.json) passed full-source, quantifier, duplicate and A51 self-review. Its precise power-of-job-count hardness target differs from the current constant and polylogarithmic bounds. Nineteen expressions passed strict KaTeX and a full-page visual check. This fiftieth accepted addition completes the next ten-entry integration batch. The [batch audit](batch-05-review.md) records fresh searches, the new coding-relaxation comparison, current repository access and validation/publication state.
