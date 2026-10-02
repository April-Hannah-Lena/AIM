# Review of original target 024: Exponential interior decay for smooth Steklov domains

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Counterexample of the complete recorded target.

**Submission:** [PR #11](https://github.com/MColbrook/AIM/pull/11); contributor and submitter: Siavash Sadeghi. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 5125d5b4c6401a485f09378878bd1121280c427b

**Pinned target:** [Original 024 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/024-steklov-smooth-interior-decay.md)

**Full proof:** [steklov_counterexample.tex](../../solutions/siavash-sadeghi-steklov-024/steklov_counterexample.tex)

**Current catalogue record:** [653: Exponential interior decay for smooth Steklov domains](../../resolved/653-steklov-smooth-interior-decay.md)

## Mathematical audit

The fixed conformal map is injective on the closed disk because its derivative differs from one by at most 101/2401. The coefficient sums and derivative bound give smoothness and strictly positive boundary curvature. The weighted boundary measure is exactly ordinary Euclidean arc length pulled back by the conformal map.

I reconstructed the weighted self-adjoint disk operator, its domain and the center-evaluation vector. Nonnegative Fourier coefficients persist under each finite power. Retaining diagonal convolution terms proves the lower bound for every spectral moment. Tonelli gives divergence of every positive exponential spectral moment. Min-max eigenvalue growth would make any uniform exponential eigenfunction bound imply a finite such moment, a contradiction. The subsequence argument uses one fixed domain and handles multiplicities.

This disproves the complete smooth planar target. The order-256 Galerkin run is corroboration only: finite analytic truncations cannot prove the infinite-series counterexample.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
