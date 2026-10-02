# 090. One-dimensionality of monotone Allen–Cahn fronts in dimension five

**Area:** Phase transitions

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`u\in C^2(\mathbb R^5;(-1,1))`$ solve

```math
-\Delta u=u-u^3\quad\text{in }\mathbb R^5,\qquad
\partial_{x_5}u>0\quad\text{everywhere}.
```

Must there exist $`a\in\mathbb R^5`$ with $`|a|=1`$, $`a_5>0`$, and $`b\in\mathbb R`$ such that

```math
u(x)=\tanh\!\left(\frac{a\cdot x-b}{\sqrt2}\right)?
```

Do not assume prescribed limits as $`x_5\to\pm\infty`$, minimizing energy, or an additional energy-growth bound. This is the original monotone De Giorgi question specialized to five dimensions.

## Application

The Allen–Cahn equation models diffuse phase interfaces. The assertion would force every globally monotone stationary interface in this dimension to be planar.

## References

- [Nassif Ghoussoub and Changfeng Gui, *On De Giorgi's conjecture in dimensions 4 and 5* (Annals of Mathematics, 2003), hypotheses of the partial results](https://doi.org/10.4007/annals.2003.157.313).
- [Enric Florit-Simon and Joaquim Serra, *On stable solutions to the Allen-Cahn equation with bounded energy density in R⁴* (2025), introduction and main theorem](https://arxiv.org/abs/2509.02739).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The 2025 classification has both a dimension restriction and a bounded-energy-density hypothesis. It does not automatically provide the required control of the four-dimensional end states of an arbitrary monotone solution in R⁵. The original unrestricted dimension-five question, rather than the already-established additional-hypothesis versions, is retained.

Status-search topics (2026-09-08): `De Giorgi conjecture dimension five 2026`; `De Giorgi conjecture dimensions 5 2025 Serra`. This is a literature search, not a proof that no solution exists.
