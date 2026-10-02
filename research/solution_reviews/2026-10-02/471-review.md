# Review of original target 471: Does directional ellipticity force a fractional energy bound?

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Counterexample of the complete recorded target.

**Submission:** [PR #5](https://github.com/MColbrook/AIM/pull/5); contributor and submitter: George Stepaniants. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 26e18dc913a9c571f2d9943955a34e4fc80fa05d

**Pinned target:** [Original 471 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/471-nonlocal-directional-ellipticity-coercivity.md)

**Full proof:** [PROOF.md](../../solutions/471-nonlocal-coercivity/PROOF.md)

**Current catalogue record:** [658: Does directional ellipticity force a fractional energy bound?](../../resolved/658-nonlocal-directional-ellipticity-coercivity.md)

## Mathematical audit

The symmetric nonnegative half-plane kernel in dimension two and fractional order one-half satisfies the exact annular hypotheses. Away from the null interface, an outward hemisphere of each annulus remains in the same half-plane. Its radial and angular integrals prove the uniform upper mass and lower directional second-moment bounds.

I checked the smooth compactly supported one-sided test functions. Scaling controls the half-line transition seminorm uniformly; the transverse cutoff also contributes a bounded term. Integration of the transverse kernel bounds the submitted kernel energy independently of the shrinking layer.

Cross-interface pairs in the full fractional energy give a positive integral of dt/t, diverging logarithmically. A constant comparison with the bounded kernel energy is impossible. The target requires pair symmetry, not increment-wise evenness. All its stated conditions hold, so this is a counterexample to the entire universal coercivity assertion.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
