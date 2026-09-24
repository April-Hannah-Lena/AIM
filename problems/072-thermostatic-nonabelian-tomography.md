# 072 — Non-Abelian ray transform for simple Gaussian thermostats

**Area:** Matrix-valued transport tomography

**Status:** 🔵 OPEN

**Last checked:** 2026-09-08

## Problem statement

Let $`(M,g)`$ be a smooth compact oriented surface with boundary and $`E`$ a smooth vector field. Unit-speed thermostat trajectories satisfy

```math
\nabla_{\dot\gamma}\dot\gamma=E-\langle E,\dot\gamma\rangle_g\dot\gamma.
```

Assume the thermostat is simple: its boundary is strictly convex for this flow and trajectories between points are unique and depend smoothly on endpoints. For $`m\ge1`$, let $`A_j`$ be smooth $`\mathfrak u(m)`$-valued one-forms and $`\Phi_j`$ smooth $`\mathfrak u(m)`$-valued functions, where $`\mathfrak u(m)`$ consists of skew-Hermitian matrices. Along each maximal trajectory solve

```math
\dot U_j+(A_j(\dot\gamma)+\Phi_j)U_j=0,\qquad U_j(0)=I_m .
```

If the endpoint matrices agree for every boundary-to-boundary trajectory, must a smooth $`Q:M\to U(m)`$, equal to $`I_m`$ on $`\partial M`$, satisfy

```math
A_2=Q^{-1}A_1Q+Q^{-1}dQ,\qquad
\Phi_2=Q^{-1}\Phi_1Q?
```

## Application

This is identifiability of coupled polarization or internal-state transport along externally forced rays, modulo the unavoidable change of internal basis.

## References

1. Shubham R. Jathar, Manas Kar and Jesse Railo, *Loop Group Factorization Method for the Magnetic and Thermostatic Nonabelian Ray Transforms*, Inverse Problems **41** (2025), 015006; online 2024, introduction and conjectures. [DOI](https://doi.org/10.1088/1361-6420/ada08a), [preprint](https://arxiv.org/abs/2312.06023).
2. Yernat M. Assylbekov and Franklin T. Rea, *The Attenuated Ray Transforms on Gaussian Thermostats with Negative Curvature* (2021 preprint). [Preprint](https://arxiv.org/abs/2102.04571).

## Status review

**Literature check:** Open in cited literature; no later resolution located

Jathar–Kar–Railo explicitly leave the unitary injectivity problem for simple Gaussian thermostats open, while proving the magnetic-flow case and a reduction for thermostats. Assylbekov–Rea impose negative thermostat curvature, a restriction absent above. Searches on 2026-09-08: "nonabelian Gaussian thermostats open" and "nonabelian Gaussian thermostats 2026". No general simple-thermostat resolution was located.
