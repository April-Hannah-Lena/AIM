# 155. Approximation preserving a compressible elastic energy

**Area:** Nonlinear elasticity and variational approximation

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`\Omega,\Delta\subset\mathbb R^2`$ be bounded domains, $`1\le p<\infty`$, $`a>0`$, and $`f:\Omega\to\Delta`$ an orientation-preserving Sobolev homeomorphism with $`J_f=\det Df>0`$ almost everywhere and

```math
E(f)=\int_\Omega\left(|Df|^p+J_f^{-a}\right)\,dx<\infty.
```

Must there exist orientation-preserving smooth diffeomorphisms $`f_j:\Omega\to\Delta`$ with $`f_j\to f`$ strongly in $`W^{1,p}(\Omega)`$ and $`E(f_j)\to E(f)`$? The question is quantified over all these choices.

## Application

The determinant penalty models the energetic cost of compressing material into vanishing volume. The question asks whether smooth approximations of an elastic deformation can preserve that cost as well as the deformation gradient, so that replacing a rough deformation by a smooth one does not introduce an energy discrepancy.

## References

1. Stanislav Hencl, *Ball–Evans approximation problem: recent progress and open problems* (2025). [Paper](https://arxiv.org/abs/2502.01336). §2, Open problem 4, functional $`E_1`$, is the explicit source formulation.

2. Tadeusz Iwaniec, Leonid Kovalev and Jani Onninen, *Diffeomorphic Approximation of Sobolev Homeomorphisms* (2011), main theorem. [Paper](https://arxiv.org/abs/1009.0286). Establishes the unweighted planar approximation used for comparison.

3. John M. Ball, *Some Open Problems in Elasticity*, in *Geometry, Mechanics, and Dynamics* (2002), pp. 3–59, §2. [Chapter](https://doi.org/10.1007/0-387-21791-6_1). Explains determinant blow-up and the variational approximation difficulty.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 source poses energy approximation even in two dimensions. Searches for “Ball Evans more general functionals determinant energy approximation” and “incompressible diffeomorphisms approximation 2026” found related constrained recovery constructions but no theorem for this full injective energy class. This is a constitutive-energy question; the unweighted planar Ball–Evans theorem does not settle it.
