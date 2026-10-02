# Review of original target 560: Monotone variance in the Gaussian approximation to DrMMD flow

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Affirmative proof of the complete recorded target.

**Submission:** [PR #12](https://github.com/MColbrook/AIM/pull/12); contributor and submitter: Siavash Sadeghi. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 229efc29ceecdd18ea846f15f60717708d993f7a

**Pinned target:** [Original 560 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/560-drmmd-gaussian-variance-monotonicity.md)

**Full proof:** [aim560_proof.tex](../../solutions/siavash-sadeghi-560/aim560_proof.tex)

**Current catalogue record:** [663: Monotone variance in the Gaussian approximation to DrMMD flow](../../resolved/663-drmmd-gaussian-variance-monotonicity.md)

## Mathematical audit

The density ratio and variance derivatives have the required L2 integrability. The kernel representative permits integration by parts, reducing the spatial integral to an inner product. I reconstructed the normalized Hermite basis, eigenvalues and Gaussian coefficient generating function, including the nonconstant degree-zero mode.

For positive curve parameters, the finite mixed derivative is a variance plus a product of positive mean gaps. The truncated negative-binomial mean bound proves the gaps, and integration gives strictly negative finite prefixes. At zero and negative parameters, the polynomial boundary identity and coefficient bound give the same sign.

Absolute convergence justifies Abel summation. Positive decreasing resolvent weights preserve prefix negativity; the multiplier returning to the target integral is positive. This covers every finite positive regularization and even every positive target variance. The scalar convergence corollary was checked. Exact certificates, direct-kernel comparisons, endpoints, sign stress tests and guard tests were rerun as support. The result concerns the Gaussian moment model and does not assert Gaussian preservation of unrestricted transport.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
