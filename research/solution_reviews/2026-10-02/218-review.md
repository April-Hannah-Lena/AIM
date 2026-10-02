# Review of original target 218: Bounded harmonic lifting for complex media

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Affirmative proof of the complete recorded target.

**Submission:** [PR #14](https://github.com/MColbrook/AIM/pull/14); contributor and submitter: George Stepaniants. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 724edad2cdd2b52bd954e823d3965320d8493f0d

**Pinned target:** [Original 218 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/218-complex-harmonic-lifting.md)

**Full proof:** [PROOF.md](../../solutions/218-complex-harmonic-lifting/PROOF.md)

**Current catalogue record:** [654: Bounded harmonic lifting for complex media](../../resolved/654-complex-harmonic-lifting.md)

## Mathematical audit

Accretivity gives a nonzero complex principal symbol on every real covector. The homotopy to the identity preserves the nonzero leading coefficient and absence of real roots, proving the half-plane root condition even in dimension two.

I checked Theorem I, equation (7), page 78 of Agmon's published 1960 paper in the linked scan. Its second-order specialization gives the maximum estimate with the interior L1 remainder. The proof retains that remainder. The coercive adjoint Dirichlet problem, H2 regularity and Green's formula bound it by the boundary L2 norm, hence by the boundary supremum norm.

Heat smoothing on the compact boundary preserves the supremum norm for complex data and converges in H1/2. Continuity of the lifting into H1 and an almost-everywhere subsequence pass the estimate to the exact trace class. This proves the entire constant-coefficient smooth-domain target. It is a deduction from an existing maximum theorem, without a claim for measurable coefficients or Lipschitz domains.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
