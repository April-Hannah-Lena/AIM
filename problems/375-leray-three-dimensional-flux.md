# 375. The three-dimensional steady Leray problem with unrestricted boundary fluxes

**Area:** Steady viscous flow; inlet–outlet boundary conditions

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Let $`\Omega\subset\mathbb R^3`$ be any bounded connected smooth domain whose boundary has finitely many connected components $`\Gamma_0,\ldots,\Gamma_m`$. Given arbitrary $`\nu>0`$, $`f\in C^\infty(\overline\Omega;\mathbb R^3)`$ and $`a\in C^\infty(\partial\Omega;\mathbb R^3)`$ satisfying only

```math
\sum_{j=0}^m\int_{\Gamma_j}a\cdot n\,dS=0,
```

does there exist $`u\in H^1(\Omega;\mathbb R^3)`$ with $`\nabla\cdot u=0`$, trace $`a`$, and

```math
\nu\int_\Omega\nabla u:\nabla\varphi+\int_\Omega(u\cdot\nabla)u\cdot\varphi=\int_\Omega f\cdot\varphi
```

for every smooth compactly supported divergence-free $`\varphi`$? Individual component fluxes may be nonzero and arbitrarily large; neither the domain nor the data are assumed axisymmetric.

## Application

The compatibility condition expresses conservation of fluid volume across all inlets and outlets together. The problem asks whether this physical condition alone guarantees at least one steady flow in an arbitrary three-dimensional geometry.

## References

1. M. Korobkov, K. Pileckas and R. Russo, [*The Steady Navier–Stokes System: Basics of the Theory and the Leray Problem*](https://doi.org/10.1007/978-3-031-50898-1), Birkhäuser (2024), Preface and Chapters 4–6; [publisher's front matter](https://link.springer.com/content/pdf/bfm:978-3-031-50898-1/1).
2. M. V. Korobkov, K. Pileckas, V. V. Pukhnachev and R. Russo, [*The flux problem for the Navier–Stokes equations*](https://doi.org/10.1070/RM2014v069n06ABEH004928), Russian Mathematical Surveys 69 (2014), 1065–1122, introduction and solvability results for planar and axisymmetric domains.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using the steady Leray flux problem in general three-dimensional domains and subsequent work on nonzero component fluxes. The 2024 book solves the planar and axisymmetric spatial cases; its unrestricted-flux conclusion has those geometric hypotheses. Standard existence with zero flux on each separate component is weaker than the single total-flux condition here. Later symmetric-domain results do not remove that distinction. The [Avrin paper published in CPAA 2026](https://doi.org/10.3934/cpaa.2025090), Theorems 1.1–1.5, gives local results for unrestricted data but imposes smallness for global stability; it does not yield arbitrary-flux steady existence. No general three-dimensional resolution was located.
