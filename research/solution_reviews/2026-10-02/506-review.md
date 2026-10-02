# Review of original target 506: Small-ball ratios for general symmetric product priors

**Date:** 2026-10-02

**Reviewer:** OpenAI Codex (AI), in this repository-maintenance session, separate from the originating proof-preparation runs. The review read the complete argument and checked its hypotheses and conclusion against the pinned target. Originating self-review and successful numerical checks were not treated as independent proof evidence.

**Decision:** Solved under the repository's documented-independent-audit convention. Counterexample of the complete recorded target.

**Submission:** [PR #13](https://github.com/MColbrook/AIM/pull/13); contributor and submitter: Siavash Sadeghi. The packages identify AI-generated derivations and reviews; submission credit is not an assertion of independent human review.

**Pinned submission head:** 0a60879abc7134f89d43b5b58cb1c757611df3c6

**Pinned target:** [Original 506 at aa776a01d7d48a79f93251af11fde9454b0aea95](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/506-product-prior-small-ball-ratios.md)

**Full proof:** [aim506_counterexample.tex](../../solutions/siavash-sadeghi-506/aim506_counterexample.tex)

**Current catalogue record:** [660: Small-ball ratios for general symmetric product priors](../../resolved/660-product-prior-small-ball-ratios.md)

## Mathematical audit

The quartic density meets positivity, continuity, evenness and strict decrease. The block scales define a full-support probability measure on ell2 and a center of formal energy one. Its standardized displacement is not square summable, so the established restricted-center theorem is respected.

I reconstructed the convolution bound. Centered unimodality bounds each ratio by one; integration by parts and symmetry give a positive quadratic displacement penalty. The elementary integral bound suffices. At each selected scale, accumulating the penalty over a block sends a subsequence of Laplace-transform ratios to zero.

The layer-cake formula represents those ratios as averages of ball ratios, with averaging measures concentrating at zero radius. A positive ball-ratio liminf would imply positive Laplace ratios, a contradiction. Thus liminf is zero although the prescribed value is exp(-1). This disproves the full universal formula without claiming that the full limit exists. The quantitative and polynomial-scale extensions and the supporting exact and convolution checks were also checked.

## Evidence and limits

The audit found no missing hypothesis or unresolved proof step for the recorded target. Standard analytic dependencies remain dependencies. This is a mathematical review, not a proof-assistant certificate; no human peer review, publication acceptance or novelty determination is claimed.

The [reproduction record](reproduction.json) links the supporting computations rerun on 2026-10-02. [Submitted file hashes](submitted_hashes.json) identify the unchanged source packages. Computation corroborates the audit where relevant and does not replace the analytic reasoning. IDs in submitted files refer to the pinned baseline.
