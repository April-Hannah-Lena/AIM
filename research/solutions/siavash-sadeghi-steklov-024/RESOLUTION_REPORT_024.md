# Resolution report: AIM 024

**Claim:** A counterexample to exponential interior decay on smooth planar Steklov domains.  
**Evidence status:** Solution claimed; independent mathematical review pending.  
**Contributor / submitter:** Siavash Sadeghi.  
**Review date:** 1 October 2026.  
**Repository revision:** `aa776a01d7d48a79f93251af11fde9454b0aea95`.  
**Target:** [024. Exponential interior decay for smooth Steklov domains](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/024-steklov-smooth-interior-decay.md).

## Proof and result

The complete argument is in [steklov_counterexample.pdf](steklov_counterexample.pdf), with editable [LaTeX source](steklov_counterexample.tex).

Set epsilon = 1/100, q(z) = 1 + epsilon sum_{n>=1} exp(-sqrt(n)) z^n, F(z) = integral_0^z q(zeta)^(-2) dzeta, and Omega = F(D). The claim proves that this one domain is bounded, simply connected, smooth and strictly convex. For every complete real orthonormal Steklov eigenbasis, the center values satisfy

    sum_j exp(t sigma_j) |u_j(0)|^2 = infinity, for every t > 0.

The argument then selects one subsequence with sigma_{j_k} >= k^2 and |u_{j_k}(0)| > exp(-sigma_{j_k}/k). It follows that exp(c sigma_{j_k}) |u_{j_k}(0)| tends to infinity for every c > 0. This disproves the target already on K = {0}, and on the closed disk of radius 1/2 contained in Omega.

## Hypothesis-to-target comparison

| Target requirement | Where the proof supplies it |
| --- | --- |
| One bounded connected domain in the Euclidean plane | Section 2 proves F is injective on the closed disk; Omega is bounded and simply connected. |
| C-infinity boundary | Every differentiated Fourier series converges; F has nonzero boundary derivative and an embedded smooth boundary. |
| Exact harmonic Steklov eigenfunctions | Section 3 reduces the physical boundary problem to A = a Lambda, a = 1/abs(F') = abs(q)^2, a nonnegative self-adjoint operator with compact resolvent. |
| Physical L2 boundary normalization | The pullback measure is ds = a^(-1) dtheta, exactly Euclidean arc length. No separate physical density is introduced. |
| Eigenvalues tending to infinity | Min-max gives sigma_j >= (49/50)^2 j/2, with eigenvalues ordered with multiplicity. |
| A fixed interior compact set | F(0) = 0 and the closed disk of radius 1/2 lies in Omega. The failure occurs at its center. |
| Failure for every positive exponential rate | Sections 4-5 prove divergence of every positive exponential spectral moment and construct a single violating subsequence. |
| Arbitrary eigenvalue multiplicities | The spectral-moment identity is basis independent; the argument applies to any complete real orthonormal eigenbasis. |

## What was reviewed, and by whom

The supplied argument is AI-generated. Codex, the coordinating AI assistant, read the complete source and target, checked the contribution guide, and prepared the submission. A separate Codex AI mathematical reviewer checked the domain estimates, conformal normalization, operator domains, Fourier positivity, spectral-moment argument, and subsequence quantifiers. Another Codex AI reviewer checked the numerical implementation and reproduction. No blocking flaw was identified in these checks.

These are AI reviews within this preparation workflow. They do not constitute human peer review, formal proof-assistant verification, publication acceptance, or a certified novelty finding. Siavash Sadeghi is credited as contributor and submitter; no independent proof review is attributed to him. The numerical program and tests do not certify the infinite-dimensional proof.

## Reproduction and limits

The README contains the reproduction commands. Both supplied Galerkin orders were rerun, and independent numerical checks are recorded in `numerical_validation.txt`. The PDF compilation log and `REVIEW_AND_CHECKS.txt` document the document checks. All delivered files are covered by `SHA256SUMS`, except the manifest itself.

Finite Fourier truncations define analytic domains. Small residuals and agreement between two truncations do not provide rigorous continuum error bounds or establish asymptotic decay. The infinite-series proof is the basis of the claim.

## Primary-source checks and submission scope

- The [contribution guide](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/CONTRIBUTING.md) accepts claims through a PR with a proof link, pinned target, and reviewer disclosure.
- [Colbois, Girouard, Gordon and Sher, Section 10.1](https://doi.org/10.1007/s13163-023-00480-3) contains the smooth-versus-analytic question as Open Question 10.4.
- [Galkowski and Toth, Theorem 1](https://arxiv.org/html/1611.05363v3) assumes analytic regularity. Its boundary estimate and the maximum principle support the analytic comparison used in the manuscript.
- [Wang and Zhang, Corollary 2](https://arxiv.org/html/2412.13955v1) gives a boundary-collar exponential term with a remainder smaller than each fixed inverse power. This is compatible with the proposed counterexample.
- [Malkovich and Sharafutdinov](https://arxiv.org/abs/1404.2117) is the cited source for the conformal Steklov setting; the manuscript includes the needed reduction explicitly.

A targeted web search on 1 October 2026 did not identify a later resolution of this exact smooth-domain question. This limited search does not establish publication priority or exhaustive novelty.

The PR adds the package under `research/solutions/siavash-sadeghi-steklov-024/`. It proposes no changes to the catalogue, problem numbering, or evidence status of the target page.
