# Cross-review of the spectral batch

Reviewer: PDE batch agent. Reviewed 2026-09-22. Read all 35 draft statements and status reviews, compared with the existing spectral/operator/inverse/applied metadata and the other new PDE reservations, and reopened the source texts for the magnetic Airy operator, imaginary-power completeness, spherical PT boundary problem, laser models, and September 2026 extremal-solution result.

## Required corrections

1. **p-harmonic-unique-continuation:** exact conceptual duplicate of existing problem 073. Root had already identified this; remove and replace, rather than counting a dimension restriction as a new problem.
2. **convex-domain-extremal-single-singularity:** reference 3 gives the wrong main-theorem locator. In [2609.06673](https://arxiv.org/html/2609.06673), the main ellipsoid result is **Theorem 1.2**, not Theorem 1.1. The paper resolves an existence/nonlinearity comparison question and does not state a classification of the entire singular set. The draft's status distinction is appropriate; fix the locator.

## Checks with no additional blocking issue found

- Almog's [magnetic operator note](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-02/2015-02_AIM_Almog_2.pdf) agrees exactly with the draft expression, half-plane and displayed domain. Its small/large-parameter results are properly excluded from the unsolved intermediate regime.
- Almog's [power-potential note](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-01/2015-01_AIM_Almog_1.pdf) asks completeness of eigenfunctions, so the draft need not change that target to a Riesz-basis or generalized-eigenvector assertion.
- Siegl's [spherical strip note](https://nsa.fjfi.cvut.cz/problems/01_ESF_2010/2010-10/2010-10_ESF_Siegl.pdf), equation (2), matches the potential, derivative signs and beta normalization.
- The [Laser Filamentation chapter](https://david-lannes.perso.math.cnrs.fr/wp-content/uploads/2019/01/dumaslannesszeftel.pdf), equation (54) and Open Problem 3, supports the lab-frame ionization system. The draft retains the correct time equation for electron density, rather than accidentally using the moving-frame quasistatic equation (55).
- The self-steepening entry correctly distinguishes amplitude collapse from a numerical observation. Its book source has a broader blow-up-scenario question; the ESAIM numerical model is the direct source for the narrower amplitude target.
- Strong comparison, very-weak energy regularity and second-derivative regularity are different p-harmonic questions; they are not duplicates of continuation or one another.
- DtN Poisson bounds and analyticity on continuous boundary functions ask different endpoint properties. Existing 223–224 ask harmonic lifting and commutators and do not directly repeat either.
- General uniformly hyperbolic Schrödinger trapping is distinct from the existing fractal-Weyl count and Jakobson–Naud hyperbolic-surface gap question.
- The normalized Gaussian has unit L2 norm and the displayed hexagonal lattice has covolume 1/delta.
- No further conceptual duplicate was found among the other 33 reviewed entries. This cross-review does not independently certify every cited proof or exhaust future literature.

## Resolution of review comments

The duplicate was removed and replaced by the sharp vector Riesz-transform inequality. The main-theorem locator was corrected to Theorem 1.2. The replacement received a separate control-agent check before integration.
