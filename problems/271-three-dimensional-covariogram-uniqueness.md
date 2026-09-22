# 271 — Matheron’s covariogram uniqueness problem in three dimensions

**Area:** Geometric tomography / phase retrieval

**Status:** 🟡 PARTIAL

**Last checked:** 2026-09-13

## Problem statement

For a compact convex body $K\subset\mathbb R^3$ with nonempty interior, define

$$
g_K(x)=\operatorname{Vol}_3(K\cap(K+x)),\qquad x\in\mathbb R^3.
$$

If two such bodies $K,L$ satisfy $g_K(x)=g_L(x)$ for every $x\in\mathbb R^3$, must $L=a+K$ or $L=a-K$ for some $a\in\mathbb R^3$? No smoothness, positive-curvature or polyhedral assumption is imposed. Translation and point reflection are the unavoidable ambiguities.

## Application

The covariogram is the autocorrelation of a shape indicator. Its Fourier transform is the squared diffraction magnitude, so uniqueness would justify a natural three-dimensional reconstruction model without phase measurements.

## References

1. G. Bianchi, *The covariogram problem* (2023), in *Harmonic Analysis and Convexity*, pp. 37–82, [book chapter](https://doi.org/10.1515/9783110775389-002); [author manuscript](https://people.dimai.unifi.it/bianchi/lavori/covariogram_survey14.pdf), §§3.3–3.5. Surveys the unresolved three-dimensional class and precise smoothness restrictions.
2. G. Bianchi, *The covariogram determines three-dimensional convex polytopes* (2009), [Advances in Mathematics 220, 1771–1808](https://doi.org/10.1016/j.aim.2008.11.011), Theorem 1.1; [manuscript](https://arxiv.org/abs/0805.1605). Establishes polytope uniqueness.

## Status review

**Known cases:** Covariogram uniqueness is established for three-dimensional convex polytopes, and for pairs of sufficiently smooth positively curved bodies under the cited $C^9$ hypotheses.

**Remaining target:** Uniqueness up to translation and point reflection for arbitrary three-dimensional convex bodies without polyhedral or smoothness assumptions.

**Literature check:** Open in cited literature; no later resolution located.

Planar convex-body uniqueness and three-dimensional polytope uniqueness are known. The smooth result described in the chapter, Theorem 3.25, requires both bodies to be $C^9$ with positive curvature in dimension three. Counterexamples in dimension at least four do not answer this question. Searches included “Matheron covariogram three dimensional 2026 solved”, “Bianchi covariogram uniqueness 2025 2026”, and “covariogram general convex bodies R3”. No general resolution was located.
