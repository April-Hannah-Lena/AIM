# Cross-review of the stochastic/PDE batch — 2026-09-22

Reviewed all 36 draft statements and their stated source/status distinctions. Priority full-text comparisons covered the Agresti–Veraar survey's Problems 4, 9, 10 and 11; Agresti–Sauerbrey–Veraar's two Hölder questions; the Fernández-Real–Ros-Oton book's open nonlocal questions; del Teso–Endal–Jakobsen–Vázquez's viscosity definition; the time-fractional PME open-problem section; and the nonlinear reaction–diffusion renormalization identities.

## Admission issue

**Hold `critical-allen-cahn-quadratic-noise-energy-moment`.** The statement does faithfully reproduce the model in Agresti–Veraar, Open Problem 4. This is not a misquotation and no published matching resolution was located. However, allowing spatially constant positive initial data produces a scalar stochastic differential equation whose endpoint maximum-moment behavior raises a material elementary-reduction concern. Hold for this formulation concern; **do not label it solved or present an attempted solution**. Root was notified and elected to seek a reserve candidate. This is the only admission-blocking issue identified in this review.

## Small precision improvements

- In `time-fractional-pme-barenblatt-attraction`, the phrase “mass-preserving weak solution” gives less information than the companion Dirac-uniqueness entry. Specify the admissible temporal continuity, local integrability of `u^m`, and initial trace in addition to the Volterra identity. This makes the “every such u” quantifier fully self-contained. The asymptotic exponents and the L1 convergence target agree with §8 of Gómez-Castro–Płociniczak–Vázquez, arXiv:2604.09281.
- In `nonlocal-pucci-finite-integrability-abp`, write `1 <= p < infinity` rather than merely `p < infinity` to state the requested integrability range explicitly. The sign of the Pucci inequality and the negative part of the source are consistent.
- Some supplementary references in `local-cahn-hilliard-three-dimensional-separation` and `critical-stochastic-sqg-global-regularity` omit authors. Add them during the final bibliography pass. This is metadata completion, not a mathematical defect.

## Priority checks that pass

- **No-slip stochastic Navier–Stokes:** the proposed `C B^{1/2}_{4,4} ∩ L4 W^{1,4}_0` class is consistent with a weak `W^{-1,4}` realization and its interpolation trace. Transport noise is allowed to be non-small subject to parabolicity. The survey's Problem 9 explicitly asks for such a local theory. A fresh search located Goodair's March 2026 arXiv:2603.13199, but that result concerns weak martingale solutions between plates and an inviscid limit, not the draft's local strong well-posedness assertion on arbitrary smooth bounded domains.
- **Negative-half critical Navier–Stokes:** `B^{-1/2}_{6,4}` and the `L4_t L6_x` continuation class have matching Navier–Stokes scaling. This fixes the first excluded smoothness endpoint of the source's critical theory and differs from the bounded-critical-norm blow-up criterion.
- **The two Hölder questions:** the rough-coefficient question permits an almost-sure positive exponent; the smooth-noise question asks for a deterministic exponent. These are separate questions in the source and are not parameter copies. The diffusion coefficients remain merely measurable in the second entry.
- **Nonlocal Pucci/Calderón–Zygmund/regularity:** the book explicitly separates the finite-Lp ABP bound, W^{2s,p} regularity of concave equations, and Hölder regularity under directional ellipticity. Structured angular-kernel estimates do not cover the first two broad classes. The higher Hölder target remains below the stated C^{1+2s} ceiling.
- **Infinity-fractional evolution:** the draft's sup/inf of the symmetric directional integral at zero gradient matches Definition 4.1 and Definition 4.3 of arXiv:2210.06414. It does not accidentally use the different classical zero-gradient operator.
- **Nonlinear diffusion renormalization:** the gradient conversion factors, exponent interval (0,2), and absence of an imposed conservation law match Definition 1.1/Remark 1.2 of Fellner–Fischer–Kniely–Tang. Linear-diffusion weak uniqueness and automatic nonlinear conservation are distinct questions.
- **Complex-balanced reaction–diffusion:** the network, stoichiometric class and bounded classical solution hypothesis are explicit. Boundary equilibria remain allowed, which separates this from standard entropy-decay results. The July 2026 Nguyen–Tang paper concerns selected irreversible systems, not arbitrary complex-balanced PDE networks.
- **Maxwell–Stefan:** the arbitrary positive pair-friction condition is materially broader than Bothe's September 2026 additive-friction theorem. N >= 4 avoids portraying additivity as a general parametrization.
- **Fourth-order aggregation:** the signs and coefficients in the weak identity match the stated PDE. Weak uniqueness, variational attainment, and finite propagation address different mathematical outputs; none is a rephrasing of another.

## Coverage and limits

The remaining entries—fully nonlinear Liouville, nonperturbative homogenization, stochastic quadratic reaction diffusion, the stable-cone and obstacle questions, fractional-pressure PME, nonlocal-to-local SKT, Cahn–Hilliard separation, fractional minimal cones, the three manifold PME questions, time-fractional point-source uniqueness, stochastic critical SQG, and unconditional entropy-system uniqueness—have coherent hypotheses and no additional concrete defect identified in this review. Their status reviews appropriately distinguish source-explicit open questions from narrower recent theorems. This is a literature and formulation review, not an independent proof that a problem is open.

## Resolution of review comments

The Allen–Cahn candidate was held and replaced by optimal obstacle regularity for general stable kernels with only angular L1 integrability. That replacement was researched by the PDE agent and read by the root agent against the book’s Open Question 4.3 and the published singular-kernel theorem. It asks for a smooth-obstacle C1,s estimate and is distinct from both lower obstacle smoothness and positive harmonic profiles in cones. The temporal solution class, ABP exponent range, and two missing author lists were corrected before integration.
