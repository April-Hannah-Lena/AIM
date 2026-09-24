# Integration audit — 22 September 2026

## Admission and count

Baseline: 360 active problems at commit `3bc9f5a`. New admission: 141 problems, numbered 353–493. This batch produced **500 active entries**. Counts here record the historical checkpoint; problem references use the current consecutive numbering.

The new set emphasizes PDEs. It draws from books and surveys as well as specific papers, including SIAM Journal on Mathematical Analysis, SIAM Journal on Control and Optimization, and SIAM Review. References distinguish an original open question, a recent status assessment and a restricted theorem. No new numerical linear algebra entry was admitted.

## Separate editorial reviews

- [Control and transport group](review-control.md), reviewed by the root agent.
- [Fluid and nonlinear PDE group](control/review-pde.md), reviewed by the control agent.
- [Spectral and elliptic group](pde/review-spectral.md), reviewed by the PDE agent.
- [Stochastic and nonlocal group](spectral/review-root.md), reviewed by the spectral agent.

The cross-review read the statements and reviews, checked hypotheses, quantifiers, normalization and immediate obstructions, and reopened selected primary texts. It did not independently re-search every reference or verify proofs. Automated similarity screening was supplemented by reading potentially overlapping statements; textual difference alone was not treated as evidence of mathematical distinctness.

## Corrections and holds

1. Existing **073** is an unforced periodic problem. The new Navier–Stokes manuscript explicitly constructs external forcing. Its dated review now makes that distinction and removes the earlier blanket status assertion about the entire Millennium problem.
2. A new p-harmonic unique-continuation candidate duplicated **073**. It was replaced by the sharp vector Riesz-transform norm question, with a separate check against the August 2026 weak-type result.
3. A critical Allen–Cahn maximum-moment candidate was held after a formulation concern in cross-review, despite being explicitly listed as open in its source. It was replaced before receiving an identifier; the [hold](stochastic-pde/held-allen-cahn-endpoint.md) does not claim a published solution or present an attempted proof.
4. The September 2026 extremal-solution theorem locator was corrected to Theorem 1.2. Bibliographic author names, several DOI links, four differential-spacing errors and two LaTeX parsing issues were corrected.
5. The irreversible catalytic reaction conjecture was restricted to strictly positive data, excluding stationary boundary equilibria that invalidate its source’s literal nonnegative-data wording.
6. The dispersion-managed ground-state question includes the evident reflection and conjugate-time-reversal symmetries. Its KIT open-status source is explicitly labelled as an archived research-program description.

Related questions about the same equation were retained only when their requested conclusions differ: global existence, conditional continuation, uniqueness, asymptotic selection, conserved quantities, support propagation, and stationary optimization are separate mathematical targets. Several dimensions or parameter values of one assertion were kept in a single entry.

## Verification

The final mechanical results are recorded in `validation.json`. They check the active count, problem IDs, metadata, required sections, local navigation, generated README and KaTeX parsing. These checks cannot establish open status or completeness of a literature search. External references were consulted during research; no claim of universal long-term URL availability is made.

The original catalogue was not globally re-dated. Except for the separately reviewed 073, older entries keep their previous status dates. The earlier September expansion’s pending unnumbered drafts remain outside this admission and outside the active count.
