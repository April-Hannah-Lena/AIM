# 663. Monotone variance in the Gaussian approximation to DrMMD flow

**Area:** Sampling and kernel gradient flows

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

Fix a target variance $`s>2`$ and let $`\pi=N(0,s)`$ on $`\mathbb R`$. Use the Gaussian kernel

```math
k(x,y)=\exp\bigl(-(x-y)^2/2\bigr)
```

and its integral operator on $`L^2(\pi)`$,

```math
T_\pi f(y)=\int_{\mathbb R}k(x,y)f(x)\,d\pi(x).
```

For $`0<v<s`$, put $`\nu_v=N(0,v)`$ and $`r_v=d\nu_v/d\pi-1`$. For a fixed finite regularization parameter $`\lambda>0`$, define the normalized witness

```math
h_{v,\lambda}=T_\pi(T_\pi+\lambda I)^{-1}r_v.
```

Here $`r_v\in L^2(\pi)`$, the resolvent is bounded, and the witness has a differentiable Gaussian-kernel representative.

Prove or disprove that, for every $`s>2`$, $`\lambda>0`$ and $`0<v<s`$,

```math
\int_{\mathbb R}y\,h_{v,\lambda}'(y)\,d\nu_v(y)<0.
```

This is the sign inequality underlying the variance-monotonicity conjecture in Appendix C of [1]. In the centered Gaussian moment approximation, it makes the scalar evolution

```math
\dot v(t)=-2(1+\lambda)\int_{\mathbb R}y\,h_{v(t),\lambda}'(y)\,d\nu_{v(t)}(y)
```

strictly increase whenever $`0<v(t)<s`$. In particular it applies to the source's initialization $`v(0)=s/2`$; the target variance $`v=s`$ is an equilibrium.

The normalized witness matches the spectral expansion used in Appendix C. Multiplying it by the positive factor 2 in the variational optimizer of equation (32) changes only the time scale, not the requested sign. The question concerns the Gaussian moment approximation with fixed $`\lambda`$. The unrestricted DrMMD transport flow need not preserve Gaussian distributions.

## Application

De-regularized maximum mean discrepancy (DrMMD) interpolates between kernel-based distribution matching and a chi-square-divergence flow. The conjecture tests whether this interpolation preserves the expected movement of uncertainty toward a Gaussian target. In the source's illustrative model, monotone variance also supports uniform estimates used in its convergence analysis.

## References

1. Z. Chen, A. Mustafi, P. Glaser, A. Korba, A. Gretton and B. K. Sriperumbudur, [(De)-regularized Maximum Mean Discrepancy Gradient Flow](https://www.jmlr.org/papers/v26/24-1574.html), *Journal of Machine Learning Research* **26**(235) (2025), 1–77. Integral operator, p.4; equation (32), p.30; Appendix C, especially equations (C.1)–(C.2), pp.71–72, and Lemma C.2, p.74. [Published PDF](https://www.jmlr.org/papers/volume26/24-1574/24-1574.pdf).
2. The same authors, [arXiv:2409.14980v3](https://arxiv.org/html/2409.14980v3), 24 November 2025, Appendix C. This version retains the finite-regularization conjecture.

## Status review

**Resolution (2026-10-02):** Affirmative proof. The complete target was checked in an independent Codex AI mathematical audit of [the submitted proof](../solutions/siavash-sadeghi-560/aim560_proof.tex). See [the review record](../solution_reviews/2026-10-02/560-review.md) for the reasoning, scope and supporting checks.

**Original target:** [560 at the pinned catalogue revision](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/560-drmmd-gaussian-variance-monotonicity.md). Current archive ID: 663. Submitted in [PR #12](https://github.com/MColbrook/AIM/pull/12).

**Evidence:** Solved under the documented-independent-audit convention. This review was performed by AI. It does not assert human peer review, publication, proof-assistant verification or novelty priority. The submitted package retains its original pending-review wording.

### Previous status review at the pinned revision

Lemma C.2 proves the corresponding sign in the limiting chi-square and MMD regimes. These endpoint results do not prove it for a finite positive $`\lambda`$, where the integral operator's spectral multipliers become $`\rho/(\rho+\lambda)`$. The source explicitly leaves this intermediate regime conjectural. Numerical examples and convergence results conditional on regularity estimates do not settle the sign inequality.

The 2026 Sobolev-regularized MMD work uses a different operator, with a gradient penalty measured against the evolving distribution; its convergence theorem does not establish this fixed-target resolvent inequality. Searches through 24 September 2026 found no matching solution or announced solution. No equivalent entry was found in the repository.
