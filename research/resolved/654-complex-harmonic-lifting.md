# 654. Bounded harmonic lifting for complex media

**Area:** Elliptic equations / complex material coefficients

**Status:** ✅ SOLVED

**Last checked:** 2026-10-02

## Problem statement

Let $`d\ge2`$, let $`\Omega\subset\mathbb R^d`$ be any bounded connected $`C^\infty`$ domain, and let $`C\in\mathbb C^{d\times d}`$ be a constant matrix satisfying

```math
\mathop{\mathrm{Re}}\nolimits\sum_{j,k}C_{jk}\xi_k\overline{\xi_j}\ge\mu|\xi|^2
\quad(\xi\in\mathbb C^d)
```

for some $`\mu>0`$. For $`\varphi\in H^{1/2}(\partial\Omega)\cap L^\infty(\partial\Omega)`$, let $`u_\varphi\in H^1(\Omega)`$ have trace $`\varphi`$ and satisfy

```math
\int_\Omega C\nabla u_\varphi\cdot\overline{\nabla v}=0
\quad(v\in H^1_0(\Omega)).
```

Does there always exist a finite $`K(\Omega,C)`$ such that

```math
\|u_\varphi\|_{L^\infty(\Omega)}\le K(\Omega,C)\|\varphi\|_{L^\infty(\partial\Omega)}
\quad\text{for every such }\varphi?
```

## Application

Complex elliptic coefficients represent phase-dependent response in frequency-domain material models. This asks whether bounded boundary excitation can produce arbitrarily large interior amplitude, even in a smooth homogeneous specimen.

## References

1. A. F. M. ter Elst and E. M. Ouhabaz, [*Five Open Problems on the Dirichlet-to-Neumann Operator with Variable Coefficients*](https://link.springer.com/article/10.1007/s00020-025-02796-9), *Integral Equations and Operator Theory* 97, 14 (2025), Question 1, final paragraph. Explicitly identifies the constant-coefficient, smooth-domain case as unresolved.
2. A. F. M. ter Elst and E. M. Ouhabaz, [*Commutator estimates and Poisson bounds for Dirichlet-to-Neumann operators with variable coefficients*](https://arxiv.org/abs/2404.18272), *Calculus of Variations and Partial Differential Equations* 64, 58 (2025), Theorem 1.2 and §6, Theorem 6.5(d). Finite-$`p`$ and Hölder estimates under regularity assumptions.

## Status review

**Resolution (2026-10-02):** Affirmative proof. The complete target was checked in an independent Codex AI mathematical audit of [the submitted proof](../solutions/218-complex-harmonic-lifting/PROOF.md). See [the review record](../solution_reviews/2026-10-02/218-review.md) for the reasoning, scope and supporting checks.

**Original target:** [218 at the pinned catalogue revision](https://github.com/MColbrook/AIM/blob/aa776a01d7d48a79f93251af11fde9454b0aea95/problems/218-complex-harmonic-lifting.md). Current archive ID: 654. Submitted in [PR #14](https://github.com/MColbrook/AIM/pull/14).

**Evidence:** Solved under the documented-independent-audit convention. This review was performed by AI. It does not assert human peer review, publication, proof-assistant verification or novelty priority. The submitted package retains its original pending-review wording.

### Previous status review at the pinned revision

**Literature check:** Open in cited literature; no later resolution located.

The June 2025 problem paper specifically leaves this smooth homogeneous case open. Finite-$`p`$ estimates do not supply a bound at $`p=\infty`$ unless their constants are controlled as $`p`$ grows. The real-coefficient maximum principle does not settle the complex case.

**Search audit:** Searched “harmonic lifting complex coefficients L infinity bounded 2026”, “ter Elst Ouhabaz harmonic lifting maximum principle”, and later work on the 2025 open questions. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
