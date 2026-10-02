# Review of original target 488: Full-space minimizers for subcritical fourth-order aggregation energy

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Affirmative proof of the complete recorded target.

**Submission:** [PR #6](https://github.com/MColbrook/AIM/pull/6); contributor and submitter: George Stepaniants. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 7a3971c3c8f8821960ec7229b109fa8d3fea791b

**Pinned target:** [Original 488 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/488-fourth-order-aggregation-full-space-minimizer.md)

**Full proof:** [PROOF.md](../../solutions/488-aggregation-minimizer/PROOF.md)

**Current catalogue record:** [659: Full-space minimizers for subcritical fourth-order aggregation energy](../../resolved/659-fourth-order-aggregation-full-space-minimizer.md)

## Mathematical audit

The Gagliardo-Nirenberg exponent is below two throughout the stated subcritical range, giving a finite energy infimum. Spreading a unit-mass trial function gives negative energy. I checked the exact scaling law: the infimum is negative and proportional to mass to a power greater than one.

Radial rearrangement gives an H1-bounded minimizing sequence. Local compactness and the radial tail bound give global strong convergence in the nonlinear norm. Lower semicontinuity and the negative mass scaling law exclude loss of mass, producing a minimizer without assuming a second moment.

A two-sided mass variation inside the positive region identifies the negative multiplier. If its support were unbounded, the radial Euler equation would have a strictly positive forcing term sufficiently far out. Its integrated form forces a positive radial derivative, contradicting decrease. Compact support supplies the missing finite second moment. These steps cover every stated dimension, coupling and exponent.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
