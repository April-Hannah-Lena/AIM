# Resolution report: AIM 560

**Problem:** 560, Monotone variance in the Gaussian approximation to DrMMD flow  
**Repository:** MColbrook/AIM  
**Pinned target revision:** aa776a01d7d48a79f93251af11fde9454b0aea95  
**Claim date:** 1 October 2026  
**Contributor / submitter:** Siavash Sadeghi  
**Requested status:** Solution claimed, pending independent review

## Claim

The answer is affirmative. For every target variance `s > 0`, every finite
`lambda > 0`, and every `0 < v < s`, the exact normalized witness in the target
statement satisfies

```
integral y h'(y) dN(0,v)(y) < 0.
```

This strengthens the repository statement, which requires only `s > 2`.

## Proof and target matching

The proof is [aim560_proof.pdf](aim560_proof.pdf), with editable [LaTeX source](aim560_proof.tex).
It is not yet hosted as a published or independently audited mathematical result.

The operator, target Gaussian, unit-bandwidth Gaussian kernel, density ratio,
normalized resolvent witness and strict sign are identical to those in the
pinned problem statement. No additional relation between `s`, `v` and `lambda`
is assumed. In particular, the argument includes arbitrarily small positive
`v`, not just variances close to `s` or the initialization `s/2`.

Section 2 rigorously reduces the witness pairing to the even Gaussian eigenmodes,
including the nonconstant degree-zero mode. Lemma 3.1 proves strict negativity
of every finite prefix. Section 4 applies summation by parts to all bounded,
nonnegative decreasing weights with positive first weight. The DrMMD resolvent
weights satisfy these conditions for every finite positive `lambda`.

Theorem 1.1 is exactly the required sign, with an expanded target-variance range.
Corollary 5.1 proves monotone convergence of the stated scalar Gaussian moment
model to its target variance. No Gaussian-preservation statement about the full
transport flow is needed or claimed.

## Additional conclusions

The proof establishes the sign for a larger class of decreasing spectral filters,
a strictly negative explicit upper bound, and local exponential attraction of
the scalar variance equilibrium. These additional conclusions are not required
to match the repository target.

## Verification performed

The supplied analytic proof and computational implementations were AI-generated.
Codex read the complete argument and pinned target; separate Codex AI reviewers
checked the mathematics and verifiers. The current rerun is documented in
`REVIEW_AND_CHECKS.txt`. Supporting verification includes 2,237
exact-arithmetic checks, rigorously enclosed infinite sums for seven examples,
12 direct-kernel integral-operator comparisons, six high-precision endpoint
checks, and 363,810 finite-prefix sign checks.

The direct-kernel discretization is independent of the spectral *computational
formula*, but was written in the same session and is not independent authorship
or independent mathematical review. Finite computation is not used to justify
the universally quantified theorem.

**Outstanding:** independent mathematical review of the full argument, publication,
and optional proof-assistant formalization. No human peer review or formal proof verification has been performed. The AI
reviews are part of this preparation workflow; no independent proof review is
attributed to Siavash Sadeghi. No claim of Lean verification is made.

## Literature/status audit

See `status_and_sources.md`. The pinned entry was Open, and a dated targeted
search found no matching later resolution. Search completeness and priority are
not guaranteed.

## Submission state

This report accompanies the proof package submitted through a pull request under
`research/solutions/siavash-sadeghi-560/`. No catalogue status change is proposed.
