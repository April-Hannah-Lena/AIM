# Review of original target 435: Poisson kernel bounds for elliptic boundary diffusion on Lipschitz domains

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Counterexample of the complete recorded target.

**Submission:** [PR #15](https://github.com/MColbrook/AIM/pull/15); contributor and submitter: George Stepaniants. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** eca72de682043eb87be3084ed238f307c07cf56a

**Pinned target:** [Original 435 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/435-dtn-poisson-bounds-lipschitz.md)

**Full proof:** [PROOF.md](../../solutions/435-corner-poisson-counterexample/PROOF.md)

**Current catalogue record:** [656: Poisson kernel bounds for elliptic boundary diffusion on Lipschitz domains](../../resolved/656-dtn-poisson-bounds-lipschitz.md)

## Mathematical audit

The three-quarter disk sector is connected and Lipschitz, and identity coefficients meet the real smooth symmetric assumptions. The harmonic function with radial exponent 2/3 has finite H1 energy. Its trace is supported on the distant circular arc, while its side flux is unbounded but in L2.

I checked the Green identity after deleting a small disk at the corner. The extra flux tends to zero; density extends the identity to all H1 tests. The trace therefore lies in the actual L2 generator domain, allowing differentiation of the semigroup at zero.

A side-segment indicator of length epsilon remains uniformly separated from the arc. Integrating the proposed kernel bound and taking the generator limit would bound its flux pairing by a constant times epsilon. The exact pairing is a positive constant times epsilon to the power 2/3, giving a contradiction. Integration avoids exceptional boundary points. This disproves the full real-coefficient Lipschitz-domain target.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
