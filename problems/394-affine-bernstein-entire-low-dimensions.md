# 394. Affine Bernstein rigidity in dimensions three through nine

**Area:** Fourth-order elliptic PDEs / geometric variational problems

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For each integer $3\le n\le9$, let $u\in C^4(\mathbb R^n)$ have positive-definite Hessian everywhere. Define

$$
U^{ij}=\mathop{\mathrm{cof}}\nolimits(D^2u)_{ij},\qquad w=(\det D^2u)^{-(n+1)/(n+2)}.
$$

If $u$ satisfies the affine maximal surface equation

$$
\sum_{i,j=1}^n U^{ij}\partial_{ij}w=0\quad\text{on }\mathbb R^n,
$$

must $u$ be a quadratic polynomial with positive-definite quadratic part? This asks the entire-graph case of the affine Bernstein conjecture, without additional growth, bounded-Hessian or affine-metric completeness assumptions.

## Application

The equation is the Euler–Lagrange equation for affine surface area. Rigidity of entire profiles is a basic obstruction to singularity formation and loss of compactness in geometric optimization governed by this fourth-order PDE.

## References

1. N. S. Trudinger and X.-J. Wang, *The Monge–Ampère equation and its geometric applications*, Handbook of Geometric Analysis, vol. I (2008), 467–524, §6.3, conjecture following Theorem 6.4. [Author chapter](https://maths-people.anu.edu.au/~wang/publications/MA.pdf).
2. Y. Sun, C. Xing and R. Xu, *New non-quadratic Euclidean complete affine maximal type hypersurfaces via Calabi affine geometry*, preprint (26 August 2026), §1, equations (1.1)–(1.3) and Theorem 1.3. [arXiv:2608.25330](https://arxiv.org/abs/2608.25330).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The August 2026 paper explicitly says the affine maximal conjecture remains open even in dimension three. Its new counterexamples have exponent a at least -n/(n+1), which does not include the affine maximal exponent -(n+1)/(n+2). The older dimension-ten example is nonsmooth and also outside the requested dimension range. Searches through 22 September 2026 for higher-dimensional Chern/affine Bernstein proofs and counterexamples found no matching resolution.
