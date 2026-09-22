# 246. The exact minimum ropelength of a trefoil

**Area:** Geometry of ropes and knotted polymers

**Status:** 🔵 OPEN

**Last checked:** 2026-09-13

## Problem statement

For a closed $C^{1,1}$ embedded curve $\gamma:S^1\to\mathbb R^3$, define its thickness $\tau(\gamma)$ as its reach: the supremum of $r>0$ such that every point at distance less than $r$ from the curve has a unique nearest point on it. Define ropelength by $\mathcal R(\gamma)=\operatorname{Length}(\gamma)/\tau(\gamma)$.

Determine the exact value
$$\mathcal R_{3_1}=\inf\{\mathcal R(\gamma):\gamma\text{ is ambient isotopic to a trefoil}\}.$$
A trefoil is the knot type represented, for $t\in[0,2\pi]$, by $((2+\cos3t)\cos2t,(2+\cos3t)\sin2t,\sin3t)$. Ambient isotopy means deformation by a continuous family of homeomorphisms of $\mathbb R^3$. Thickness here is a tube radius, not its diameter.

## Application

Ropelength is the minimum material needed to tie a knot with a fixed tube thickness. The trefoil is the simplest nontrivial test case for tightly packed filaments and coarse polymer geometry.

## References

- Elizabeth Denne, [*Quadrisecants and essential secants of knots with applications to the geometry of knots*](https://doi.org/10.1515/9783110571493-007), in *New Directions in Geometric and Applied Knot Theory* (2018), §7.4, discussion after Theorem 7.4.11: the open ropelength question and trefoil numerical bounds.
- Jason Cantarella, Rob Kusner and John M. Sullivan, [*On the minimum ropelength of knots and links*](https://arxiv.org/abs/math/0103224) (2002), abstract and existence/regularity theorems: existence of $C^{1,1}$ minimizers and the radius convention.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Searched “trefoil exact minimum ropelength proof 2025 2026”, “ideal trefoil rigorous optimal”, and new tight-link bounds. The existence theorem does not identify the minimizer or its exact length. Numerical tightening and results for multicomponent torus links do not determine the unrestricted trefoil infimum; reported numbers also vary by a factor of two with the thickness convention.
