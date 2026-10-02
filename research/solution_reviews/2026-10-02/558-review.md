# Review of original target 558: Variance ordering for Gaussian alpha-divergence approximations

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Counterexample of the complete recorded target.

**Submission:** [PR #10](https://github.com/MColbrook/AIM/pull/10); contributor and submitter: Siavash Sadeghi. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 2cf63b0eff5619814f3a30721816afb3d18b3855

**Pinned target:** [Original 558 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/558-gaussian-variational-variance-ordering.md)

**Full proof:** [aim_558_counterexample.tex](../../solutions/siavash-sadeghi-457-558/aim_558_counterexample.tex)

**Current catalogue record:** [662: Variance ordering for Gaussian alpha-divergence approximations](../../resolved/662-gaussian-variational-variance-ordering.md)

## Mathematical audit

I checked the Gaussian integral, optimization over the mean and strict convexity in positive diagonal precisions. Boundary divergence gives existence and uniqueness, so stationarity identifies the global optimum.

The rational target precision is positive definite. At parameter ten, the stationary inverse matrix has diagonal one, proving identity covariance optimal. Above ten, the explicit feasible comparator has zero first gradient and equal negative leaf gradients. The convex supporting-plane inequality and symmetry force optimum leaf precisions above one, hence leaf variances below their values at ten. The Schur complement gives the increase of the first variance. Parameters ten and eleven alone disprove the target.

Exact arithmetic, symbolic identities and the 90-digit stationary calculation were rerun. I also checked the sensitivity, minimal-dimension and determinant-monotonicity arguments. The conclusion concerns separately optimized variances under the stated divergence; it makes no calibration or non-Gaussian claim.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
