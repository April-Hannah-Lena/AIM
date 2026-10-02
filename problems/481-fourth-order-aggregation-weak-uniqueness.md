# 481. Weak uniqueness for fourth-order aggregation–diffusion

**Area:** Degenerate parabolic PDEs; cell adhesion

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $`d\ge2`$ and $`\chi>0`$. On $`\mathbb R^d`$ consider

```math
\partial_t\rho=-\nabla\cdot(\rho\nabla\Delta\rho)-\chi\Delta(\rho^2),\qquad \rho(0)=\rho_0,
```

where $`\rho_0\ge0`$, $`\int\rho_0=1`$, $`\rho_0\in H^1(\mathbb R^d)`$, and $`\int |x|^2\rho_0(x)\,dx<\infty`$. Is the nonnegative weak solution unique in the following class on every finite interval $`[0,T]`$?

The curve $`t\mapsto\rho(t)`$ is narrowly continuous with values in probability measures having finite second moment, and

```math
\rho\in L^\infty(0,T;H^1(\mathbb R^d))\cap L^2(0,T;H^2(\mathbb R^d)).
```

For every $`\phi\in C_c^2(\mathbb R^d)`$ and $`0\le a<b\le T`$ it satisfies

```math
\int\phi[\rho(b)-\rho(a)]
=-\int_a^b\!\int\bigl(\rho\Delta\rho\Delta\phi+\Delta\rho\nabla\rho\cdot\nabla\phi+\chi\rho^2\Delta\phi\bigr)\,dx\,dt.
```

Narrow continuity means convergence against bounded continuous spatial test functions. Vacuum is allowed; positivity bounded away from zero is not assumed.

## Application

This fourth-order local model approximates short-range cell adhesion. Uniqueness is needed for its predicted tissue evolution to be determined by the initial density.

## References

1. J. A. Carrillo, A. Esposito, C. Falcó and A. Fernández-Jiménez, *Competing effects in fourth-order aggregation–diffusion equations*, Proc. Lond. Math. Soc. **129**, e12623 (2024), Introduction, Definition 2.1 and Theorem 2.2. [Article](https://doi.org/10.1112/plms.12623).
2. C. Falcó, R. E. Baker and J. A. Carrillo, *A nonlocal-to-local approach to aggregation-diffusion equations*, SIAM Review **67** (2025), 353–372, §4. [Article](https://doi.org/10.1137/25M1726248).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The formulation is the $`m=2`$ subcritical model and weak solution class of the first paper, which proves existence. The SIAM Review article still identifies uniqueness as unresolved. Searches on 2026-09-22 for fourth-order aggregation–diffusion weak uniqueness, cell-adhesion uniqueness, and the authors’ later papers found no theorem covering this class with vacuum. Classical uniqueness while the mobility stays uniformly positive is insufficient. This is separate from the catalogue’s cubic thin-film positivity problem: both the mobility and the attractive second-order term differ.
