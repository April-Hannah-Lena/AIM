# Review of original target 593: Logarithmic controlled bandwidth for locally analytic functions

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Affirmative proof of the complete recorded target.

**Submission:** [PR #8](https://github.com/MColbrook/AIM/pull/8); contributor and submitter: George Stepaniants. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** ce81353cb9dbf846104550739e294b7a100c7dee

**Pinned target:** [Original 593 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/593-analytic-controlled-bandwidth.md)

**Full proof:** [PROOF.md](../../solutions/593-analytic-bandwidth/PROOF.md)

**Current catalogue record:** [664: Logarithmic controlled bandwidth for locally analytic functions](../../resolved/664-analytic-controlled-bandwidth.md)

## Mathematical audit

Local analyticity supplies uniform Cauchy derivative bounds on a slightly larger interval where the supremum is at most twice the original bound. The repeated convolution cutoff equals one on the target interval; distributing derivatives proves its finite-order derivative estimates.

I checked the product-rule bound and factorial estimate. Integrating the Fourier tail beyond a multiple of the derivative order makes the error exponentially small. A smooth compact-frequency cutoff produces a Schwartz function with the required bandwidth. Spatial mass and first moment directly control its Fourier transform and derivative; the cutoff derivative gives the stated controlled extra term. The spatial supremum follows from the extended-function bound and tail error.

Choosing derivative order logarithmic in inverse error proves the exact bandwidth assertion. Approximation, all three global norm bounds, compact Fourier support and Schwartz regularity hold simultaneously for complex functions with only local analyticity.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
