# 420. Continuous gradients for three-dimensional infinity-harmonic functions

**Area:** Degenerate elliptic PDEs and supremal variational problems

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22
## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be open and let $`u\in C(\Omega)`$ be a viscosity solution of

```math
-\Delta_\infty u=-\sum_{i,j=1}^3(\partial_i u)(\partial_j u)\partial_{ij}u=0.
```

Must $`u\in C^1_{\mathrm{loc}}(\Omega)`$? Here the viscosity convention tests the displayed operator against smooth functions touching $`u`$ from above or below. This asks for continuity of the gradient, beyond its known existence at every point; it imposes no nonvanishing-gradient hypothesis.

## Application

Infinity-harmonic functions describe absolutely minimizing extensions for maximum-gradient costs. Gradient regularity matters for optimal Lipschitz interpolation and continuum limits of tug-of-war models.

## References

1. L. C. Evans and C. K. Smart, [Everywhere differentiability of infinity harmonic functions](https://doi.org/10.1007/s00526-010-0388-1), *Calculus of Variations and PDE* **42** (2011), 289–299, introduction and main theorem.
2. O. Savin, [C1 regularity for infinity harmonic functions in two dimensions](https://www.math.columbia.edu/~savin/c12d.pdf), *Archive for Rational Mechanics and Analysis* **176** (2005), 351–361, Theorem 1 and introduction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The first reference proves differentiability, while the second proves continuous differentiability in dimension two. Searches through the review date for “infinity harmonic C1 three dimensions”, “Evans Smart regularity”, and later Aronsson-equation results found no theorem giving continuous gradients in the stated three-dimensional class. Higher-dimensional differentiability alone does not answer this question.
