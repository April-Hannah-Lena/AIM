# Review of original target 405: Logarithmic convexity for subdiffusion with non-gradient drift

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Counterexample of the complete recorded target.

**Submission:** [PR #1](https://github.com/MColbrook/AIM/pull/1); contributor and submitter: George Stepaniants. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 57442cba88fcfa5d8dcfe500ffe61d0d1b552cc7

**Pinned target:** [Original 405 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/405-fractional-drift-logarithmic-convexity.md)

**Full proof:** [PROOF.md](../../solutions/405-fractional-drift/PROOF.md)

**Current catalogue record:** [655: Logarithmic convexity for subdiffusion with non-gradient drift](../../resolved/655-fractional-drift-logarithmic-convexity.md)

## Mathematical audit

If the odd entire error function omitted one, it would also omit minus one, contradicting Little Picard. Its complementary function therefore has a nonreal zero. The half-order Mittag-Leffler identity transfers it, and conjugation supplies the needed sign.

The first angular Dirichlet Bessel mode on the disk is an eigenfunction of the Laplacian and rotation field. Identity diffusion, smooth rotational drift and a real constant potential give the specified nonreal eigenvalue. Taking the real part of its Mittag-Leffler evolution gives a real solution of the exact Caputo equation. I checked the fractional series identity, Dirichlet trace and nonzero initial data. Its simple zero yields a zero terminal norm and positive norm at earlier times.

The target allows this potential and drift. The asserted inequality fails for every finite constant because the terminal factor vanishes. An admissible fractional order is enough to disprove the universal target; no self-adjointness restriction has been introduced.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
