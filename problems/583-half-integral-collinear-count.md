# 583. Counting half-integral polygons with collinear interior lattice points

**Area:** Discrete geometry and lattice-point enumeration

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

A half-integral polygon is a two-dimensional convex polygon $`P\subset\mathbb R^2`$ whose vertices belong to $`\tfrac12\mathbb Z^2`$. Integral polygons are included. Two polygons are considered equivalent when $`P'=UP+b`$ for some $`U\in\mathop{\mathrm{GL}}\nolimits_2(\mathbb Z)`$ and $`b\in\mathbb Z^2`$.

For each integer $`i\ge3`$, let $`N(i)`$ be the number of these equivalence classes for which $`P`$ has exactly $`i`$ interior lattice points and all of those points lie on one line. Prove or disprove that

```math
N(i)=\frac{i+1}{1260}\left(512i^6+12928i^5+137740i^4+685145i^3+1582743i^2+1665222i+710640\right)
```

for every $`i\ge3`$.

## Application

Exact enumeration supplies benchmark collections for algorithms on rational polytopes and for classifications of the toric geometric objects encoded by polygons. The conjecture would replace enumeration of billions of examples by a closed formula for this family.

## References

1. M. Bohnert and J. Springer, [Classifying Rational Polygons with Small Denominator and Few Interior Lattice Points](https://doi.org/10.1007/s00454-026-00822-0), *Discrete & Computational Geometry* **76** (2026), 1238–1265, Section 2 and Conjecture 3.7. [arXiv:2410.17244](https://arxiv.org/abs/2410.17244).
2. J. Springer and M. Bohnert, [Half-integral polygons with few interior lattice points](https://doi.org/10.5281/zenodo.13928298), computational dataset (2024).
3. J. Springer, [RationalPolygons.jl](https://github.com/justus-springer/RationalPolygons.jl), reference implementation of rational-polygon classification algorithms.

## Status review

The 2026 published paper explicitly poses this formula and reports verification for $`3\le i\le20`$. Its classification algorithm and the accompanying finite datasets do not prove the identity for every $`i`$. The equivalence relation uses integral translations, and half-integrality means denominator dividing two, not denominator exactly two.

The known count for integral polygons is a different, smaller family. The other conjecture in the same paper concerning distinct Ehrhart quasipolynomials counts different objects and imposes no collinearity condition. Current searches found no matching proof, counterexample, or announced solution.
