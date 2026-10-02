# 558. Deciding nonnegativity of unnormalized univariate trace polynomials

**Area:** Real algebraic geometry and matrix inequalities

**Status:** 🔵 OPEN

**Last checked:** 2026-09-24

## Problem statement

Given a positive integer $`d`$ and a polynomial $`F\in\mathbb Q[z_1,\ldots,z_d]`$, determine whether there is an algorithm that always terminates and correctly decides the statement

```math
F\bigl(\mathop{\mathrm{tr}}\nolimits(A),\mathop{\mathrm{tr}}\nolimits(A^2),\ldots,\mathop{\mathrm{tr}}\nolimits(A^d)\bigr)\ge0
\quad\text{for every }n\ge1\text{ and every real symmetric }A\in\mathbb R^{n\times n}.
```

Here $`\mathop{\mathrm{tr}}\nolimits`$ is the ordinary, unnormalized matrix trace. The input polynomial is a finite rational expression; matrix dimension is universally quantified and is not bounded in the input.

This uses the pure trace convention of [1, Definition 6.1]: there is no additional free matrix factor. In its symmetric-function formulation, the positive power sums are the generators and the zeroth symbol is the constant 1.

Equivalently, decide whether

```math
F\left(\sum_{i=1}^n x_i,\sum_{i=1}^n x_i^2,\ldots,\sum_{i=1}^n x_i^d\right)\ge0
```

for every $`n\ge1`$ and every $`(x_1,\ldots,x_n)\in\mathbb R^n`$. Give a decision algorithm or prove that this decision problem is undecidable.

## Application

A decision procedure would certify matrix trace inequalities uniformly over all dimensions. An undecidability theorem would establish a fundamental limit on automated symbolic verification of such inequalities, even with just one matrix variable.

## References

1. J. Acevedo, G. Blekherman, S. Debus and C. Riener, [The wonderful geometry of the Vandermonde map](https://doi.org/10.1007/s10208-025-09718-6), *Foundations of Computational Mathematics* **26** (2026), 2005–2051. Definition 6.1, Theorems 6.2 and 6.5, and Section 7. [arXiv:2303.09512](https://arxiv.org/abs/2303.09512).
2. I. Klep, J. E. Pascoe and J. Volčič, [Positive univariate trace polynomials](https://arxiv.org/abs/2009.10081), arXiv:2009.10081.

## Status review

Section 7 of [1] explicitly leaves the univariate case open. Its undecidability construction uses several matrix variables. Its decidability result for normalized traces uses $`n^{-1}\mathop{\mathrm{tr}}\nolimits(A^j)`$ and does not apply to the statement above. The trace convention in [2] is also normalized, as specified in its abstract and introduction.

For each fixed dimension, real quantifier elimination decides the inequality. The challenge is a single terminating procedure valid across all dimensions.
