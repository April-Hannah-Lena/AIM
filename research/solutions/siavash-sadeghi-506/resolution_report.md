# Resolution report: AIM 506

**Contributor / submitter:** Siavash Sadeghi.  
**Review date:** 2 October 2026.

**Target:** 506. Small-ball ratios for general symmetric product priors.

**Pinned repository revision:** `aa776a01d7d48a79f93251af11fde9454b0aea95`.

**Current inspected target status:** Partial, with the general finite-energy conjecture remaining open.

**Proposed classification:** Solution claimed (counterexample).

**Evidence:** [Proof note](aim506_counterexample.pdf), with editable [LaTeX source](aim506_counterexample.tex). The package is a proposed resolution for review, not a journal publication or an independently accepted theorem.

## Claimed resolution

The conjecture is false even for a positive real-analytic log-concave reference density with finite Fisher information. Take the reference density proportional to exp(-z^4), the Hilbert space ell^2, and m = 0. On successive blocks of 8^j coordinates, choose gamma_k = 4^(-j) and h_k = 8^(-j). The formal energy is exactly Q(h) = 1, yet the small-ball probability ratio at h relative to 0 has liminf zero as the radius tends to zero. This contradicts the asserted limit exp(-1).

The main proof is analytic and does not depend on floating-point calculations. Its steps are:
1. Verify support, admissibility and all series exactly.
2. Prove a Gaussian-convolution ratio bound R_1(d) <= exp(-d^2/144) for |d| <= 1 and R_a(d) <= 1 for every a > 0.
3. Factor the squared-norm Laplace transform ratio over coordinates, retain one growing block, and obtain L_h(16^j)/L_0(16^j) <= exp(-2^j/144).
4. Express this transform ratio as an average of ball ratios over a probability measure on radii concentrating at zero. A positive ball-ratio liminf is then impossible.

The proof also gives radii 0 < r_j < 3*2^(-j) with ratios below 2*exp(-4^j/144), extends the example to arbitrarily small positive formal energy, and supplies a second example with gamma_k = 1/k and h_k = k^(-4/3).

## Matching the full target

The target is universal over the permitted densities, scales, norms and centers. One admissible example with a ball-ratio liminf different from the required limit disproves that universal assertion. Establishing a full limit of zero for the example is not necessary and is not claimed.

All target hypotheses are verified in Section 1 of the PDF. Its center lies outside ell_gamma^2, so the counterexample does not overlap the known restricted lower bound of Theorem 4.10 in the source paper. The exact matching audit appears in `target_audit.md`.

## Review actually performed

The supplied argument is AI-generated. Codex read the complete proof and pinned target; separate Codex AI reviewers examined the proof and published source assumptions, verification programs and public submission records. Reviewed mathematical steps include convolution bounds, product limits with positive denominators, the Laplace-to-ball argument and the quantitative and robust variants. The review record accompanies the package. No independent proof review is attributed to Siavash Sadeghi.

The standard-library verifier passed 31 exact supporting checks. A separate numerical implementation passed 80 floating-point corroborations, including 25 mpmath/SciPy quadrature comparisons. These are arithmetic and computational checks, not independent proof review.

**Independent human review:** none.

**Proof-assistant verification:** none.

**Submission:** proposed proof package under `research/solutions/siavash-sadeghi-506/`; no journal publication or catalogue status change is claimed.

The current public audit found no matching AIM 506 submission after checking all indexed issues/PRs, available comments/reviews and changed-file evidence, plus focused searches and the main branch. See `repository_submission_check.txt` for the timestamp, counts and limits. Literature searches were bounded and do not prove priority. Independent audit of the complete argument is requested before any upgrade to Solved.
