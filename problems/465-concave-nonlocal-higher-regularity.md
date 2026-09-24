# 465. Higher regularity for concave stable nonlocal equations

**Area:** Nonlinear diffusion PDEs; stochastic control

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

Fix $`n\ge2`$, $`0<s<1`$ and $`0<\lambda\le\Lambda`$. For an arbitrary index set $`A`$, let

```math
L_a u(x)=\mathop{\mathrm{PV}}\nolimits\int_{\mathbb R^n}[u(x)-u(x+y)]\frac{k_a(y/|y|)}{|y|^{n+2s}}\,dy,
```

where the angular functions are even, $`\lambda\le k_a\le\Lambda`$, and $`\sup_a\|k_a\|_{C^j(S^{n-1})}\le M_j`$ for every integer $`j\ge1`$. Does there exist $`\alpha\in(0,\min\{s,1-s\})`$ such that every bounded continuous viscosity solution of

```math
\inf_{a\in A}(-L_a u)=0\quad\hbox{in }B_1
```

satisfies $`u\in C^{1+s+\alpha}(B_{1/2})`$ and

```math
\|u\|_{C^{1+s+\alpha}(B_{1/2})}\le C\|u\|_{L^\infty(\mathbb R^n)}?
```

The exponent and constant may depend on $`n,s,\lambda,\Lambda`$ and the prescribed angular smoothness bounds, but not on $`u`$ or the family size. No differentiability of the minimizing index as a function of $`x`$ is assumed.

## Application

The equation is a value equation for control of a jump process, where a controller selects among the available jump kernels. The estimate would control variation of the value gradient even where the optimal choice of kernel changes. Smoothness of each available kernel alone does not give smoothness of that choice.

## References

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. X. Ros-Oton, C. Torres-Latorre and M. Weidner, *Semiconvexity estimates for nonlinear integro-differential equations*, Comm. Pure Appl. Math. (2025), Introduction. [Article](https://doi.org/10.1002/cpa.22237).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

Open Question 3.1 in the book asks whether smooth kernels give $`C^{1+s+\alpha}`$ regularity. The displayed homogeneous equation is its translation-invariant, zero-source formulation. The 2025 paper discusses the remaining gap beyond the established $`C^{\max\{1,2s\}+\varepsilon}`$ estimates. Searches on 2026-09-22 for concave nonlocal higher regularity and smooth stable kernels found no general theorem reaching the target. Linear Schauder estimates and the classical second-order Evans–Krylov theorem concern different operators.
