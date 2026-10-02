# 386. Boundary observation of a Schrödinger field with slower surface dispersion

**Area:** PDE control / dispersive boundary dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-09-22

## Problem statement

On $`\Omega=\{x\in\mathbb R^2:1<|x|<2\}`$ let $`\Gamma_1`$ and $`\Gamma_0`$ be the inner and outer circles. Consider

```math
iz_t+\Delta z=0\quad\text{in }\Omega,\qquad z=0\quad\text{on }\Gamma_0,
```



```math
z_\Gamma=z|_{\Gamma_1},\qquad
iz_{\Gamma,t}+\tfrac12\Delta_\Gamma z_\Gamma-\partial_\nu z=0\quad\text{on }\Gamma_1.
```

With $`\nu`$ outward from $`\Omega`$, set

```math
\|Z\|_{\mathcal E}^2=\int_\Omega|\nabla z|^2\,dx+
\tfrac12\int_{\Gamma_1}|\nabla_\Gamma z_\Gamma|^2\,dS.
```

Is it true that for every $`T>0`$ a constant $`C_T`$ satisfies

```math
\|Z(0)\|_{\mathcal E}^2\le C_T\int_0^T\int_{\Gamma_0}|\partial_\nu z|^2\,dS\,dt
```

for every smooth compatible solution? The fixed coefficient $`1/2`$ selects a concrete case of the unresolved regime in which surface dispersion is weaker than bulk dispersion.

## Application

Dynamic boundary conditions represent surface degrees of freedom coupled to a quantum or dispersive bulk field. The estimate would permit exact control using only the exterior boundary.

## References

1. A. Mercado and R. Morales, *Exact Controllability for a Schrödinger Equation with Dynamic Boundary Conditions*, SIAM Journal on Control and Optimization 61 (2023), 3501–3525, main observability and controllability theorems. [DOI](https://doi.org/10.1137/21M1439407); [author preprint](https://arxiv.org/abs/2301.02573).
2. S. E. Chorfi, L. Maniar and R. Morales, *Controllability and Inverse Problems for Hyperbolic and Dispersive Equations with Dynamic Boundary Conditions*, preprint (2025), equations (4.1)–(4.4) and §5.1. [arXiv:2505.14795](https://arxiv.org/abs/2505.14795).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The SIAM theorem assumes the surface coefficient exceeds the bulk coefficient. Section 5.1 of the 2025 review expressly distinguishes the unresolved Schrödinger regime below that threshold from the negative result for waves. Searches through 22 September 2026 included “Schrödinger dynamic boundary delta less than d observability”, Wentzell control and Mercado–Morales follow-ups. The 2026 inverse-potential reconstruction paper retains the faster-surface hypothesis; no resolution of the stated slower-surface case was located.
