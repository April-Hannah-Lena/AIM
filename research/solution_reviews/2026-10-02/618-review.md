# Review of original target 618: Smooth-gradient approximation of finite-Fisher-information scores

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Affirmative proof of the complete recorded target.

**Submission:** [PR #4](https://github.com/MColbrook/AIM/pull/4); contributor and submitter: George Stepaniants. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 35780d362add4011ed7ad7a36446efee5a633323

**Pinned target:** [Original 618 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/618-fisher-score-gradient-closure.md)

**Full proof:** [PROOF.md](../../solutions/618-fisher-score/PROOF.md)

**Current catalogue record:** [665: Smooth-gradient approximation of finite-Fisher-information scores](../../resolved/665-fisher-score-gradient-closure.md)

## Mathematical audit

I checked Erbar's published Proposition 4.3: finite entropy and a W1,1 density whose weak gradient equals the density times an L2 vector field place that field in the tangent space, the closure of smooth gradients.

Extend the nonnegative square root in H1 to a compact smooth double with a freely chosen smooth metric, then normalize its square. Sobolev embedding supplies finite entropy. The product rule, zero-set locality and H1 energy give precisely the weak-gradient and L2-score hypotheses. Compactness supplies completeness, finite second moment and a Ricci lower bound.

Restrict the smooth ambient potentials and compare the two smooth metrics and volume forms to obtain convergence for the exact target score and weighted L2 norm. No boundary condition is imposed. Componentwise normalization handles disconnected components; zero-mass components contribute nothing. This proves the full boundary-allowed target without assuming smooth reflection of the original metric.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
