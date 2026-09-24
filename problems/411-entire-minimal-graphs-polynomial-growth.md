# 411. Polynomial growth of every entire minimal graph

**Area:** Quasilinear elliptic PDEs / minimal interfaces

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

For every integer $`n\ge8`$ and every smooth solution $`u:\mathbb R^n\to\mathbb R`$ of

```math
\mathop{\mathrm{div}}\nolimits\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right)=0,
```

must there exist finite constants $`C>0`$ and $`p>0`$, allowed to depend on $`u`$, such that

```math
|u(x)|\le C(1+|x|)^p\qquad\text{for all }x\in\mathbb R^n?
```

## Application

Minimal-graph equations describe equilibria of isotropic surface energy. A universal qualitative growth restriction would constrain possible large-scale interface geometries and the asymptotic boundary conditions used to approximate them.

## References

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.1, first open question on entire graphs. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf); [arXiv:2407.11903](https://arxiv.org/abs/2407.11903).
2. L. Simon, *Entire solutions of the minimal surface equation*, Journal of Differential Geometry 30 (1989), 643–688, introduction and construction of entire graphs asymptotic to cylinders. [DOI](https://doi.org/10.4310/jdg/1214443827).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The survey distinguishes this growth question from the existence of exact polynomial solutions. Dimensions at most seven are excluded because Bernstein rigidity gives affine solutions there. Searches through 22 September 2026 found no result bounding every entire graph by a solution-dependent power. Guo’s April 2026 polynomial-solution paper studies exact polynomial solutions, rather than growth of all smooth solutions.
